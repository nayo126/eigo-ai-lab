#!/usr/bin/env python3
"""Generate a weekly roundup post that links to the last 7-10 days of articles.

Roundup posts are good for:
  - Internal linking (SEO link juice)
  - Shareability (people share weekly summaries)
  - Backlink magnets (other sites cite roundups)

Output: content/posts/{YYYY-MM-DD}-ai-weekly-roundup.md
Runs Sundays via launchd.
"""
from __future__ import annotations
import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = json.loads((ROOT / "config.json").read_text())
POSTS = ROOT / "content" / "posts"
LOG = ROOT / "logs" / "digest.log"
LOG.parent.mkdir(exist_ok=True)


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line, flush=True)
    with LOG.open("a") as f:
        f.write(line + "\n")


def parse_post(path: Path) -> dict | None:
    try:
        raw = path.read_text()
    except Exception:
        return None
    if not raw.startswith("---"):
        return None
    m = re.search(r"\n---\s*\n", raw[3:])
    if not m:
        return None
    front_raw = raw[3:3 + m.start()].strip()
    try:
        front = json.loads(front_raw)
    except json.JSONDecodeError:
        return None
    front["filename"] = path.name
    return front


def main() -> int:
    log("=== weekly_digest start ===")
    today = datetime.now(timezone.utc)
    cutoff = today - timedelta(days=7)
    is_japanese = CONFIG.get("_lang_override") != "en"

    candidates: list[dict] = []
    for md in sorted(POSTS.glob("*.md")):
        front = parse_post(md)
        if not front:
            continue
        # skip prior digests so we don't include them in new digests
        if "weekly-roundup" in front.get("slug", ""):
            continue
        pub_raw = front.get("published_at", "")
        try:
            pub = datetime.fromisoformat(pub_raw.replace("Z", "+00:00"))
        except ValueError:
            continue
        if pub < cutoff:
            continue
        candidates.append(front)

    candidates.sort(key=lambda p: p.get("published_at", ""), reverse=True)
    log(f"candidates in last 7 days: {len(candidates)}")
    if len(candidates) < 3:
        log("not enough articles to summarize (need >= 3); skip")
        return 0

    picks = candidates[:10]
    base_url = CONFIG["site"]["base_url"].rstrip("/")

    if is_japanese:
        title = f"今週のAIニュース10選 ({today.strftime('%Y/%m/%d')}付)"
        description = f"{today.strftime('%Y年%m月%d日')}までの1週間で報じられたClaude・ChatGPT・AIツール最新ニュースをまとめて紹介します。"
        body_lines = [
            f"## 今週のAIハイライト",
            "",
            f"過去7日間に当サイトで取り上げたAIニュースの中から、特に注目すべき{len(picks)}本を厳選しました。",
            "",
            f"## 注目記事 {len(picks)}選",
            "",
        ]
        for i, p in enumerate(picks, 1):
            url = f"{base_url}/posts/{p.get('slug')}.html"
            body_lines.append(f"### {i}. [{p['title']}]({url})")
            body_lines.append("")
            body_lines.append(f"{p.get('description', '')}")
            body_lines.append("")
            cat = p.get("category", "")
            if cat:
                body_lines.append(f"カテゴリ: **{cat}**")
                body_lines.append("")

        body_lines.extend([
            "## 今週の傾向",
            "",
            "1週間のAI業界の動きを振り返ると、特定のテーマに関するニュースが目立ちました。詳しくは各記事をご覧ください。",
            "",
            "## まとめ",
            "",
            "AIツールの進化は週単位で大きく変わります。当サイトは毎日3記事ペースで最新動向をフォロー。週末はこのような週次ロードマップ的記事で振り返ります。",
        ])
        cat = "AI業界"
        tags = ["週次まとめ", "AIニュース", "Claude", "ChatGPT", "ロードマップ"]
        keywords = ["AI 週次まとめ", "今週のAI", "AIニュース まとめ", "Claude 最新", "ChatGPT 最新"]
    else:
        title = f"AI Weekly Roundup ({today.strftime('%Y-%m-%d')})"
        description = f"The week's top AI news on Claude, ChatGPT, Cursor and emerging tools, curated."
        body_lines = [
            "## This week's AI highlights",
            "",
            f"Hand-picked {len(picks)} stories from the past 7 days on Claude, ChatGPT, Cursor and the broader AI tooling space.",
            "",
            "## Top stories",
            "",
        ]
        for i, p in enumerate(picks, 1):
            url = f"{base_url}/posts/{p.get('slug')}.html"
            body_lines.append(f"### {i}. [{p['title']}]({url})")
            body_lines.append("")
            body_lines.append(f"{p.get('description', '')}")
            body_lines.append("")
            cat = p.get("category", "")
            if cat:
                body_lines.append(f"Category: **{cat}**")
                body_lines.append("")
        body_lines.extend([
            "## Trends this week",
            "",
            "Across the week's coverage, certain themes stood out. Click through each story for the details.",
            "",
            "## Takeaways",
            "",
            "AI tooling shifts week-to-week. We publish three deep-dive stories every day; on Sundays we look back like this.",
        ])
        cat = "AI Industry"
        tags = ["Weekly Roundup", "AI News", "Claude", "ChatGPT", "Roundup"]
        keywords = ["AI weekly roundup", "this week in AI", "AI news summary", "Claude weekly", "ChatGPT weekly"]

    body_md = "\n".join(body_lines)
    slug = f"ai-weekly-roundup-{today.strftime('%Y%m%d')}"
    front = {
        "title": title,
        "description": description,
        "category": cat,
        "tags": tags,
        "keywords": keywords,
        "source_url": "",
        "source_name": "weekly-digest-internal",
        "published_at": today.isoformat(),
        "slug": slug,
    }
    fm = "---\n" + json.dumps(front, ensure_ascii=False, indent=2) + "\n---\n\n"
    out_path = POSTS / f"{today.strftime('%Y-%m-%d')}-{slug}.md"
    out_path.write_text(fm + body_md)
    log(f"WROTE digest: {out_path.name} ({len(picks)} articles included)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
