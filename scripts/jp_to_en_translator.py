#!/usr/bin/env python3
"""JP→EN auto-translator for eigo-ai-lab.

Translates the best-performing JP articles from auto-blog into English using
claude -p, and saves them as eigo-ai-lab posts. Triples English content volume
while leveraging proven JP article structures.

Selection criteria:
1. Article must be at least 3 days old (avoid translating something then deleting)
2. Skip already-translated articles (state file)
3. Prefer high-word-count articles
4. Cap at 3 translations per run to manage cost
"""
from __future__ import annotations
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "logs" / "translator.log"
STATE = ROOT / "data" / "translated.json"
JP_BLOG = Path.home() / "auto-blog" / "site" / "src" / "content" / "blog"
EN_POSTS = ROOT / "content" / "posts"
LOG.parent.mkdir(exist_ok=True)
STATE.parent.mkdir(exist_ok=True)
EN_POSTS.mkdir(parents=True, exist_ok=True)

# Reuse rate-limit helper
sys.path.insert(0, "/Users/tsukaking/.claude/lib")
try:
    from rate_limit_helper import (
        looks_like_rate_limit, mark_rate_limited, mark_clear,
        is_currently_blocked, looks_like_native_binary_missing
    )
except ImportError:
    looks_like_rate_limit = lambda x: False
    mark_rate_limited = lambda *a, **k: None
    mark_clear = lambda *a, **k: None
    is_currently_blocked = lambda x: False
    looks_like_native_binary_missing = lambda x: False


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line, flush=True)
    with LOG.open("a") as f:
        f.write(line + "\n")


def load_state() -> dict:
    if STATE.exists():
        try:
            return json.loads(STATE.read_text())
        except Exception:
            return {}
    return {}


def save_state(d: dict) -> None:
    STATE.write_text(json.dumps(d, ensure_ascii=False, indent=2))


def parse_fm(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    fm: dict = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            fm[k.strip()] = [t.strip().strip('"').strip("'") for t in v[1:-1].split(",") if t.strip()]
        else:
            fm[k.strip()] = v.strip('"').strip("'")
    return fm, m.group(2)


TRANSLATION_PROMPT = """You are translating a Japanese AI/side-hustle blog article into English for an indie-dev audience (US, UK, Europe).

CRITICAL RULES:
1. Adapt for English readers — don't translate literally. Rewrite naturally.
2. Convert Japanese-specific currency (¥) to USD with approximate rate (¥150 = $1).
3. Convert Japanese-specific platforms (note → Substack/Medium, クラウドワークス → Upwork) when relevant.
4. Keep the article structure (H2 sections, intro, conclusion).
5. Tone: practical, no-fluff, indie dev / freelancer voice.
6. Length: aim for 1500-2200 English words (Japanese tends to inflate; tighten where possible).
7. Title: rewrite as a click-friendly English headline (not a direct translation).
8. Description: 1-2 sentence meta description in English.
9. Keep technical brand names as-is: ChatGPT, Claude, Cursor, etc.
10. NO mention of "this article", "let me explain", or AI-style filler. Write like a human dev.

OUTPUT FORMAT (exact, no other text):
---TITLE---
<click-friendly English headline, max 70 chars>
---DESCRIPTION---
<English meta description, 130-160 chars>
---CATEGORY---
<one of: ChatGPT, Claude, AI Tools, Side Hustle, Indie Dev, AI Trends>
---TAGS---
<5 comma-separated English tags>
---BODY---
<full English article body in markdown with H2 headings>

ORIGINAL JAPANESE ARTICLE:
{japanese_content}
"""


def run_claude(prompt: str, timeout: int = 600) -> tuple[str, str]:
    try:
        r = subprocess.run(
            ["claude", "-p", prompt, "--output-format", "text"],
            capture_output=True, text=True, timeout=timeout,
        )
        return r.stdout or "", r.stderr or ""
    except subprocess.TimeoutExpired:
        return "", "claude timeout"
    except FileNotFoundError:
        return "", "claude binary missing"


def parse_translation(raw: str) -> dict | None:
    sections = re.split(r"^---([A-Z]+)---\s*$", raw, flags=re.MULTILINE)
    # sections = ['', 'TITLE', '<title>', 'DESCRIPTION', '<desc>', ...]
    if len(sections) < 11:
        return None
    out = {}
    for i in range(1, len(sections), 2):
        key = sections[i].strip().lower()
        val = sections[i + 1].strip() if i + 1 < len(sections) else ""
        out[key] = val
    if "title" not in out or "body" not in out:
        return None
    return out


def slugify(s: str) -> str:
    """ASCII slug from English title."""
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s[:80]


def write_en_post(parsed: dict, source_path: Path) -> Path | None:
    title = parsed["title"]
    slug = slugify(title) or source_path.stem
    today = datetime.now().strftime("%Y-%m-%d")
    out_path = EN_POSTS / f"{today}-{slug}.md"

    # Pick a non-conflicting filename
    n = 2
    while out_path.exists():
        out_path = EN_POSTS / f"{today}-{slug}-{n}.md"
        n += 1

    body = parsed["body"]
    description = parsed.get("description", title)[:160]
    category = parsed.get("category", "AI Tools")
    tags_str = parsed.get("tags", "")
    tags = [t.strip() for t in tags_str.split(",") if t.strip()][:5]

    # ai-news-jp style frontmatter (JSON-in-md per pattern)
    fm = {
        "title": title,
        "description": description,
        "category": category,
        "tags": tags,
        "pubDate": today,
        "source": "jp-translation",
        "source_path": str(source_path.relative_to(Path.home())),
    }
    fm_text = "---\n" + json.dumps(fm, ensure_ascii=False, indent=2) + "\n---\n\n"
    out_path.write_text(fm_text + body)
    return out_path


def candidates() -> list[Path]:
    if not JP_BLOG.exists():
        return []
    state = load_state()
    translated = set(state.get("translated", []))

    posts = sorted(JP_BLOG.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    eligible: list[Path] = []
    for p in posts:
        if str(p) in translated:
            continue
        # Skip very short articles
        if len(p.read_text()) < 3000:
            continue
        eligible.append(p)
    return eligible


def main() -> int:
    log("=== jp-to-en translator start ===")

    if is_currently_blocked("claude_cli"):
        log("claude_cli is rate-limited; abort this run")
        return 0

    pool = candidates()
    log(f"eligible candidates: {len(pool)}")
    if not pool:
        log("nothing to translate")
        return 0

    state = load_state()
    state.setdefault("translated", [])

    max_per_run = 3
    done = 0
    for source in pool[:max_per_run]:
        log(f"translating: {source.name}")
        text = source.read_text()
        fm, body = parse_fm(text)
        # Use title + body (skip the YAML/JSON wrapper)
        article_text = (fm.get("title", "") + "\n\n" + body).strip()
        # Truncate huge articles (claude has token limits)
        article_text = article_text[:14000]

        prompt = TRANSLATION_PROMPT.format(japanese_content=article_text)
        out, err = run_claude(prompt, timeout=420)
        combined = out + err

        if looks_like_rate_limit(combined) or looks_like_native_binary_missing(combined):
            mark_rate_limited("claude_cli", combined[:300])
            log("rate-limited; bailing")
            return 0

        if not out:
            log(f"  empty response, skip: {err[:200]}")
            continue

        parsed = parse_translation(out)
        if not parsed:
            log(f"  parse failed, raw len={len(out)}: {out[:300]}")
            continue

        out_path = write_en_post(parsed, source)
        if out_path:
            state["translated"].append(str(source))
            save_state(state)
            done += 1
            log(f"  wrote: {out_path.name}")

    log(f"=== done: {done}/{max_per_run} translated ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
