#!/usr/bin/env python3
"""Take trend items and write Japanese SEO articles via the `claude` CLI."""
from __future__ import annotations
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = json.loads((ROOT / "config.json").read_text())
DATA = ROOT / "data"
POSTS = ROOT / "content" / "posts"
POSTS.mkdir(parents=True, exist_ok=True)
LOG = ROOT / "logs" / "generate.log"
LOG.parent.mkdir(exist_ok=True)


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line, flush=True)
    with LOG.open("a") as f:
        f.write(line + "\n")


def slugify(text: str) -> str:
    # ASCII fallback - for Japanese titles we just use a hash + date
    base = re.sub(r"[^a-zA-Z0-9-]+", "-", text.lower())
    base = re.sub(r"-+", "-", base).strip("-")  # collapse repeats, no leading/trailing "-"
    if len(base) < 4:
        base = f"post-{abs(hash(text)) & 0xFFFFFFFF:x}"
    return base[:60]


PROMPT_HEAD = """\
You are an SEO writer for "AI Lab Daily", a daily practical-guide blog for indie hackers, freelancers and devs in the US/UK/AU. Rewrite the source story below as a publishable English article.

## Hard rules
- Word count: 600-1200 words
- Use these markdown sections **in this exact order**:
  1. `## TL;DR` - 3 bullet points, one line each
  2. `## What happened` - facts, numbers, who did what
  3. `## Why it matters` - industry impact, competitive angle
  4. `## Try it yourself` - 3-5 concrete actions a reader can take today
  5. `## Sources` - original link + 1-2 related (markdown link list)
- No first-person ("I"). Keep an editorial neutral voice.
- No hype words: ultimate, game-changer, revolutionary, must-have, insane, crazy
- Model/product names stay in English (Claude, ChatGPT, GPT-5, Sonnet 4.6)
- Title and first 100 chars MUST include the primary SEO keyword

## Output format
Output **exactly one JSON object** - no prose, no code fences.

{
  "title": "<60 chars, includes SEO keyword, a number is preferred>",
  "description": "<120 chars meta description>",
  "category": "Claude" | "ChatGPT" | "Gemini" | "Cursor" | "AI Tools" | "AI Industry",
  "tags": ["up to 5 English tags"],
  "keywords": ["5 SEO keywords, mix head and long-tail"],
  "body_md": "<article body in markdown, 600-1200 words>"
}
"""


def call_claude(prompt: str, retries: int = 2) -> str:
    import sys
    # prefer shared lib, fall back to local
    sys.path.insert(0, "/Users/tsukaking/.claude/lib")
    sys.path.insert(0, str(Path(__file__).parent))
    try:
        from rate_limit_helper import (
            looks_like_rate_limit, looks_like_native_binary_missing,
            mark_rate_limited, mark_clear, is_currently_blocked,
        )
    except ImportError:
        from rate_limit_helper import looks_like_rate_limit, mark_rate_limited, mark_clear, is_currently_blocked
        looks_like_native_binary_missing = lambda t: False

    if is_currently_blocked("claude_cli"):
        log("claude_cli is currently rate-limited; skipping (watchdog will retry)")
        return ""

    cli = CONFIG.get("claude_cli", "claude")
    for attempt in range(retries + 1):
        try:
            r = subprocess.run(
                [cli, "-p", prompt, "--output-format", "text"],
                capture_output=True, text=True, timeout=420,
            )
            if r.returncode == 0 and r.stdout.strip():
                mark_clear("claude_cli")
                return r.stdout.strip()
            combined = (r.stderr or "") + " " + (r.stdout or "")
            log(f"claude attempt {attempt+1} failed rc={r.returncode} err={combined[:300]}")
            if looks_like_native_binary_missing(combined):
                mark_rate_limited("claude_cli", combined[:300], reason="native_missing") if hasattr(mark_rate_limited, "__call__") else None
                log("claude native binary missing -> state file written, abort run")
                return ""
            if looks_like_rate_limit(combined):
                mark_rate_limited("claude_cli", combined[:300])
                log("rate limit detected -> state file written, abort run")
                return ""
        except subprocess.TimeoutExpired:
            log(f"claude attempt {attempt+1} timed out")
        except Exception as e:
            log(f"claude attempt {attempt+1} error: {e}")
    return ""


def extract_json(text: str) -> dict | None:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    s = text.find("{")
    e = text.rfind("}")
    if s == -1 or e == -1 or e <= s:
        return None
    try:
        return json.loads(text[s:e + 1])
    except json.JSONDecodeError as err:
        log(f"json decode fail: {err}")
        return None


def write_post(art: dict, source: dict) -> Path | None:
    title = (art.get("title") or "").strip()
    body = (art.get("body_md") or "").strip()
    if not title or len(body) < 400:
        log(f"reject: too short ({len(body)} chars)")
        return None

    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    slug = slugify(art.get("title", ""))
    # if all-japanese the slug fallback is hash; prefix with date for uniqueness
    fname = f"{date}-{slug}.md"
    out = POSTS / fname

    front = {
        "title": title,
        "description": (art.get("description") or "")[:200],
        "category": art.get("category") or "AI業界",
        "tags": art.get("tags") or [],
        "keywords": art.get("keywords") or [],
        "source_url": source.get("url"),
        "source_name": source.get("source"),
        "published_at": datetime.now(timezone.utc).isoformat(),
        "slug": slug,
    }
    fm = "---\n" + json.dumps(front, ensure_ascii=False, indent=2) + "\n---\n\n"
    out.write_text(fm + body)
    return out


def main() -> int:
    log("=== generate start ===")
    trends_path = DATA / "trends.json"
    if not trends_path.exists():
        log("no trends.json; run fetch_sources first")
        return 1
    pool = json.loads(trends_path.read_text()).get("items", [])
    if not pool:
        log("trends empty")
        return 0

    want = CONFIG["generation"].get("articles_per_run", 3)
    written = 0
    for src in pool:
        if written >= want:
            break
        title = src.get("title", "").strip()
        body = src.get("body", "").strip()
        if not title:
            continue

        prompt = (
            PROMPT_HEAD
            + "\n## 元ソース\n"
            + f"- source: {src.get('source')}\n"
            + f"- url: {src.get('url')}\n"
            + f"- title: {title}\n"
            + f"- body excerpt:\n{body[:1200]}\n"
        )
        log(f"calling claude for: {title[:80]}")
        raw = call_claude(prompt)
        if not raw:
            log("empty claude response, skip")
            continue
        art = extract_json(raw)
        if not art:
            (DATA / "last_raw.txt").write_text(raw)
            log("json extract fail, raw saved")
            continue
        path = write_post(art, src)
        if path:
            log(f"WROTE {path.name} ({len(art.get('body_md',''))} chars)")
            written += 1

    log(f"=== generate done, wrote {written} ===")
    return 0 if written > 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
