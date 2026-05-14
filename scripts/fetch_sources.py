#!/usr/bin/env python3
"""Pull trending AI-related stories from Reddit + HackerNews + RSS sources."""
from __future__ import annotations
import json
import random
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
CONFIG = json.loads((ROOT / "config.json").read_text())
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
LOG = ROOT / "logs" / "fetch.log"
LOG.parent.mkdir(exist_ok=True)

UAS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
]

RSS_FEEDS = {
    "anthropic_news": "https://www.anthropic.com/news/rss.xml",
    "openai_blog": "https://openai.com/blog/rss.xml",
    "google_ai_blog": "https://blog.google/technology/ai/rss/",
    "huggingface_blog": "https://huggingface.co/blog/feed.xml",
}


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line, flush=True)
    with LOG.open("a") as f:
        f.write(line + "\n")


def http_get(url: str, timeout: int = 20, retries: int = 2, want_json: bool = False):
    last_err = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": random.choice(UAS),
                "Accept": "application/json, text/xml, */*;q=0.5",
                "Accept-Language": "en-US,en;q=0.9,ja;q=0.8",
            })
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read().decode("utf-8", errors="ignore")
                return json.loads(raw) if want_json else raw
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (403, 429, 503) and attempt < retries:
                time.sleep(2 + attempt * 3)
                continue
            break
        except Exception as e:
            last_err = e
            break
    log(f"GET fail {url[:80]}: {last_err}")
    return None


def fetch_reddit(sub: str, min_score: int, max_age_h: int) -> list[dict]:
    out: list[dict] = []
    for host in ("www.reddit.com", "old.reddit.com"):
        data = http_get(f"https://{host}/r/{sub}/hot.json?limit=30&t=day", want_json=True)
        if data:
            break
        time.sleep(1.0)
    if not data:
        return []
    now = time.time()
    for c in data.get("data", {}).get("children", []):
        p = c.get("data", {})
        if p.get("stickied") or p.get("over_18"):
            continue
        age_h = (now - p.get("created_utc", 0)) / 3600
        if age_h > max_age_h or (p.get("score") or 0) < min_score:
            continue
        title = (p.get("title") or "").strip()
        if not title:
            continue
        out.append({
            "source": f"reddit/r/{sub}",
            "id": f"reddit-{p.get('id')}",
            "title": title,
            "body": (p.get("selftext") or "").strip()[:2000],
            "score": p.get("score"),
            "comments": p.get("num_comments"),
            "url": f"https://reddit.com{p.get('permalink','')}",
            "age_hours": round(age_h, 1),
        })
    return out


def fetch_hn(top_n: int, keywords: list[str]) -> list[dict]:
    ids = http_get("https://hacker-news.firebaseio.com/v0/topstories.json", want_json=True)
    if not isinstance(ids, list):
        return []
    out: list[dict] = []
    for item_id in ids[:top_n]:
        time.sleep(0.05)
        item = http_get(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json", want_json=True)
        if not item or item.get("type") != "story":
            continue
        title = (item.get("title") or "").strip()
        if not title or not any(k in title.lower() for k in keywords):
            continue
        out.append({
            "source": "hackernews",
            "id": f"hn-{item_id}",
            "title": title,
            "body": (item.get("text") or "")[:2000],
            "score": item.get("score"),
            "comments": item.get("descendants"),
            "url": item.get("url") or f"https://news.ycombinator.com/item?id={item_id}",
            "age_hours": round((time.time() - item.get("time", 0)) / 3600, 1),
        })
    return out


def fetch_rss(name: str, url: str) -> list[dict]:
    raw = http_get(url)
    if not raw:
        return []
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        log(f"RSS parse fail {name}: {e}")
        return []
    out: list[dict] = []
    # Atom + RSS 2.0 both
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    items = list(root.iter("item")) + list(root.iter("{http://www.w3.org/2005/Atom}entry"))
    for it in items[:10]:
        title = (it.findtext("title") or it.findtext("atom:title", default="", namespaces=ns) or "").strip()
        link_el = it.find("link")
        link = ""
        if link_el is not None:
            link = (link_el.text or link_el.get("href") or "").strip()
        if not link:
            atom_link = it.find("atom:link", namespaces=ns)
            if atom_link is not None:
                link = atom_link.get("href", "")
        body = (it.findtext("description") or it.findtext("summary") or "").strip()[:2000]
        if not title:
            continue
        # rough id from link or title
        ident = f"{name}-{abs(hash(link or title)) & 0xFFFFFFFF:x}"
        out.append({
            "source": f"rss/{name}",
            "id": ident,
            "title": title,
            "body": body,
            "score": None,
            "comments": None,
            "url": link,
            "age_hours": None,
        })
    return out


def main() -> int:
    log("=== fetch start ===")
    src = CONFIG["sources"]
    items: list[dict] = []

    for sub in src.get("reddit_subs", []):
        got = fetch_reddit(sub, src["reddit_min_score"], src["reddit_max_age_hours"])
        log(f"reddit r/{sub}: {len(got)}")
        items.extend(got)
        time.sleep(1.5 + random.random())

    hn = fetch_hn(src.get("hn_top_count", 50), [k.lower() for k in src.get("hn_keywords", [])])
    log(f"hackernews: {len(hn)}")
    items.extend(hn)

    for name, url in RSS_FEEDS.items():
        got = fetch_rss(name, url)
        log(f"rss {name}: {len(got)}")
        items.extend(got)
        time.sleep(1.0)

    # Sort by score (RSS items get a baseline so they aren't crushed)
    def rank(it):
        s = it.get("score") or 0
        if it["source"].startswith("rss/"):
            s = 500  # treat official blog posts as high-priority
        return s
    items.sort(key=rank, reverse=True)

    hist_path = DATA / "fetched_history.json"
    history = set()
    if hist_path.exists():
        try:
            history = set(json.loads(hist_path.read_text()))
        except Exception:
            pass
    fresh = [x for x in items if x.get("id") and x["id"] not in history]
    log(f"total: {len(items)}  fresh: {len(fresh)}")

    out = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "count": len(fresh),
        "items": fresh[:80],
    }
    (DATA / "trends.json").write_text(json.dumps(out, ensure_ascii=False, indent=2))
    history.update(x["id"] for x in fresh if x.get("id"))
    hist_path.write_text(json.dumps(sorted(history)[-3000:]))
    log(f"wrote {len(out['items'])} items -> data/trends.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
