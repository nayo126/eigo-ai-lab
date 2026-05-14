#!/usr/bin/env python3
"""Compile content/posts/*.md into a static SEO site under site/."""
from __future__ import annotations
import html
import json
import re
import shutil
import urllib.parse
import xml.sax.saxutils as sx
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = json.loads((ROOT / "config.json").read_text())
POSTS = ROOT / "content" / "posts"
STATIC = ROOT / "content" / "static"
OUT = ROOT / "site"
LOG = ROOT / "logs" / "build.log"
LOG.parent.mkdir(exist_ok=True)


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line, flush=True)
    with LOG.open("a") as f:
        f.write(line + "\n")


SITE = CONFIG["site"]
MON = CONFIG["monetization"]
BASE_URL = SITE["base_url"].rstrip("/")

# Load minor-friendly monetization IDs (楽天/もしも/忍者AdMax)
MIDS_PATH = Path(MON.get("monetization_ids_file") or "")
try:
    MIDS = json.loads(MIDS_PATH.read_text()) if MIDS_PATH.exists() else {}
except Exception:
    MIDS = {}


def md_to_html(md: str) -> str:
    """Minimal markdown converter — handles headings, lists, paragraphs, bold, links, code spans."""
    lines = md.split("\n")
    out: list[str] = []
    in_list = False
    in_para: list[str] = []

    def flush_para():
        if in_para:
            text = " ".join(in_para).strip()
            if text:
                out.append(f"<p>{inline(text)}</p>")
            in_para.clear()

    def inline(s: str) -> str:
        # links [text](url)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{html.escape(m.group(2))}" rel="noopener" target="_blank">{html.escape(m.group(1))}</a>', s)
        # bold **text**
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        # inline code `code`
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        return s

    for raw_line in lines:
        line = raw_line.rstrip()
        if not line.strip():
            flush_para()
            if in_list:
                out.append("</ul>")
                in_list = False
            continue
        m = re.match(r"^(#{1,4})\s+(.+)$", line)
        if m:
            flush_para()
            if in_list:
                out.append("</ul>")
                in_list = False
            level = len(m.group(1))
            text = inline(m.group(2).strip())
            out.append(f"<h{level}>{text}</h{level}>")
            continue
        if re.match(r"^\s*[-*]\s+", line):
            flush_para()
            if not in_list:
                out.append("<ul>")
                in_list = True
            item = re.sub(r"^\s*[-*]\s+", "", line)
            out.append(f"<li>{inline(item)}</li>")
            continue
        # regular paragraph line
        if in_list:
            out.append("</ul>")
            in_list = False
        in_para.append(line)

    flush_para()
    if in_list:
        out.append("</ul>")

    return "\n".join(out)


def parse_post(path: Path) -> dict | None:
    raw = path.read_text()
    if not raw.startswith("---"):
        return None
    # Find closing --- on its OWN line (not inside JSON values like slugs)
    m = re.search(r"\n---\s*\n", raw[3:])
    if not m:
        return None
    end = 3 + m.start()
    after = 3 + m.end()
    front_raw = raw[3:end].strip()
    body = raw[after:].strip()
    try:
        front = json.loads(front_raw)
    except json.JSONDecodeError as e:
        log(f"frontmatter parse fail {path.name}: {e}")
        return None
    front["body_html"] = md_to_html(body)
    front["body_md"] = body
    front["filename"] = path.name
    return front


def ad_block() -> str:
    """忍者AdMax (年齢制限なし) 広告枠 — IDが入るまでプレースホルダ"""
    tag = (MIDS.get("ninja_admax") or {}).get("ad_tag_html")
    if not tag or tag == "TODO":
        return '<div class="ad-slot ad-placeholder"><span>Ad slot (Adsterra/Ezoic — pending)</span></div>'
    return f'<div class="ad-slot">{tag}</div>'


def rakuten_cta(keywords: list[str]) -> str:
    """Amazon US affiliate CTA (English audience)."""
    kw = keywords[0] if keywords else "AI tools"
    tag = (CONFIG.get("monetization") or {}).get("amazon_associate_us_tag")
    search_url = f"https://www.amazon.com/s?k={urllib.parse.quote(kw)}"
    if tag and not tag.startswith("TODO"):
        url = f"{search_url}&tag={urllib.parse.quote(tag)}"
        note = ""
    else:
        url = search_url
        note = " (Amazon Associates US tag pending)"
    return (
        f'<aside class="cta-box">'
        f'<h4>📚 Recommended reading on Amazon</h4>'
        f'<p>Search results for "{html.escape(kw)}"{note}</p>'
        f'<a class="cta-btn" href="{html.escape(url)}" rel="sponsored noopener" target="_blank">View on Amazon</a>'
        f'</aside>'
    )


def moshimo_cta(category: str) -> str:
    """No-op for English site (moshimo is JP-only)."""
    return ""


def _unused_moshimo(category: str) -> str:
    aid = (MIDS.get("moshimo") or {}).get("a_id")
    if not aid or aid == "TODO":
        return ""
    return (
        f'<aside class="cta-box">'
        f'<h4>💡 PR</h4>'
        f'<p>"{html.escape(category)}" — '
        f'<a href="https://af.moshimo.com/af/c/click?a_id={html.escape(aid)}" rel="sponsored noopener" target="_blank">詳細を見る</a></p>'
        f'</aside>'
    )


HEAD = """\
<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{description}" />
<meta name="robots" content="index, follow" />
<link rel="canonical" href="{canonical}" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{description}" />
<meta property="og:type" content="{og_type}" />
<meta property="og:url" content="{canonical}" />
<meta name="twitter:card" content="summary" />
{ld_json}
<style>
:root{{--fg:#1a1a1a;--mut:#666;--bg:#fff;--accent:#0066cc;--card:#fafafa;--bd:#e5e5e5;}}
*{{box-sizing:border-box}}body{{margin:0;font-family:-apple-system,"Inter","Helvetica Neue",Arial,sans-serif;color:var(--fg);background:var(--bg);line-height:1.7;font-size:16px}}
a{{color:var(--accent)}}a:hover{{text-decoration:underline}}
header.site{{border-bottom:1px solid var(--bd);padding:14px 20px;display:flex;justify-content:space-between;align-items:center;gap:16px;background:#fff;position:sticky;top:0;z-index:10}}
header.site h1{{font-size:18px;margin:0}}header.site h1 a{{color:var(--fg);text-decoration:none}}
header.site nav a{{margin-left:14px;font-size:14px;color:var(--mut);text-decoration:none}}
main{{max-width:780px;margin:0 auto;padding:24px 20px 80px}}
article header h1{{font-size:28px;line-height:1.4;margin:0 0 8px}}article header .meta{{color:var(--mut);font-size:13px}}
article h2{{font-size:22px;margin:32px 0 12px;border-left:4px solid var(--accent);padding-left:10px}}
article h3{{font-size:18px;margin:24px 0 8px}}
article ul{{padding-left:1.4em}}article li{{margin-bottom:4px}}
article p{{margin:14px 0}}
.tags{{margin:24px 0;display:flex;flex-wrap:wrap;gap:6px}}.tags span{{background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:4px 10px;font-size:12px;color:var(--mut)}}
.cta-box{{background:var(--card);border:1px solid var(--bd);border-radius:8px;padding:14px 18px;margin:24px 0}}.cta-box h4{{margin:0 0 6px;font-size:15px}}.cta-box p{{margin:6px 0;font-size:14px;color:var(--mut)}}
.cta-btn{{display:inline-block;background:var(--accent);color:#fff;padding:8px 16px;border-radius:6px;text-decoration:none;font-size:14px;margin-top:6px}}
.ad-slot{{margin:24px auto;text-align:center;min-height:90px}}.ad-placeholder{{background:#f4f4f4;color:#999;padding:30px 10px;font-size:13px;border:1px dashed #ccc}}
.post-list{{list-style:none;padding:0;margin:0}}
.post-list li{{border-bottom:1px solid var(--bd);padding:18px 0}}
.post-list li time{{color:var(--mut);font-size:12px;display:block;margin-bottom:4px}}
.post-list li h3{{margin:0 0 6px;font-size:18px}}.post-list li h3 a{{color:var(--fg);text-decoration:none}}.post-list li h3 a:hover{{color:var(--accent)}}
.post-list li p{{margin:0;color:var(--mut);font-size:14px}}
footer.site{{border-top:1px solid var(--bd);padding:24px 20px;color:var(--mut);font-size:13px;text-align:center}}
.cat-pill{{display:inline-block;background:var(--accent);color:#fff;padding:2px 8px;border-radius:10px;font-size:11px;margin-right:6px}}
.toc{{background:var(--card);border:1px solid var(--bd);border-radius:8px;padding:12px 18px;margin:18px 0;font-size:14px}}
.toc strong{{display:block;margin-bottom:6px}}
</style>
</head>
<body>
<header class="site">
<h1><a href="/">{site_name}</a></h1>
<nav>
<a href="/">Home</a>
<a href="/categories.html">Categories</a>
<a href="/rss.xml">RSS</a>
</nav>
</header>
<main>
"""

FOOT = """\
</main>
<footer class="site">
© {year} {site_name} — {tagline}<br>
This site contains affiliate links (Amazon Associates). Purchases may earn us a small commission at no extra cost to you.
</footer>
</body>
</html>
"""


def render_head(title: str, description: str, canonical: str, og_type: str = "website", ld_json: str = "") -> str:
    return HEAD.format(
        title=html.escape(title),
        description=html.escape(description or SITE["description"]),
        canonical=html.escape(canonical),
        og_type=og_type,
        site_name=html.escape(SITE["name"]),
        ld_json=ld_json,
    )


def render_foot() -> str:
    return FOOT.format(year=datetime.now().year, site_name=html.escape(SITE["name"]), tagline=html.escape(SITE["tagline"]))


def ld_article(post: dict, canonical: str) -> str:
    obj = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": post["title"],
        "description": post.get("description", ""),
        "datePublished": post.get("published_at"),
        "dateModified": post.get("published_at"),
        "author": {"@type": "Person", "name": SITE["author"]},
        "publisher": {"@type": "Organization", "name": SITE["name"]},
        "mainEntityOfPage": canonical,
        "keywords": ", ".join(post.get("keywords") or []),
    }
    return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False)}</script>'


def build_post_page(post: dict) -> str:
    slug = post["slug"]
    canonical = f"{BASE_URL}/posts/{slug}.html"
    head = render_head(post["title"], post.get("description", ""), canonical, og_type="article", ld_json=ld_article(post, canonical))
    tags_html = "".join(f"<span>{html.escape(t)}</span>" for t in post.get("tags") or [])
    pub = post.get("published_at", "")[:10]
    cat = post.get("category", "AI業界")
    body_html = post["body_html"]
    out = []
    out.append(head)
    out.append('<article>')
    out.append('<header>')
    out.append(f'<div><span class="cat-pill">{html.escape(cat)}</span></div>')
    out.append(f'<h1>{html.escape(post["title"])}</h1>')
    out.append(f'<div class="meta">Published: {pub} | Category: {html.escape(cat)}</div>')
    out.append('</header>')
    out.append(ad_block())
    out.append(body_html)
    out.append(rakuten_cta(post.get("keywords") or post.get("tags") or []))
    out.append(moshimo_cta(cat))
    out.append(ad_block())
    if post.get("source_url"):
        out.append(f'<p style="font-size:13px;color:var(--mut)">元情報: <a href="{html.escape(post["source_url"])}" rel="noopener" target="_blank">{html.escape(post.get("source_name",""))}</a></p>')
    if tags_html:
        out.append(f'<div class="tags">{tags_html}</div>')
    out.append('</article>')
    out.append(render_foot())
    return "\n".join(out)


def build_index(posts: list[dict]) -> str:
    canonical = BASE_URL + "/"
    ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": SITE["name"],
        "url": BASE_URL,
        "description": SITE["description"],
    }, ensure_ascii=False)
    head = render_head(SITE["name"] + " — " + SITE["tagline"], SITE["description"], canonical,
                       ld_json=f'<script type="application/ld+json">{ld}</script>')
    out = [head]
    out.append(f'<h1 style="margin-top:10px">{html.escape(SITE["name"])}</h1>')
    out.append(f'<p style="color:var(--mut)">{html.escape(SITE["tagline"])}</p>')
    out.append(ad_block())
    out.append('<ul class="post-list">')
    for p in posts[:30]:
        slug = p["slug"]
        pub = p.get("published_at", "")[:10]
        out.append(
            f'<li>'
            f'<time datetime="{pub}">{pub}</time>'
            f'<h3><a href="posts/{slug}.html">{html.escape(p["title"])}</a></h3>'
            f'<p>{html.escape((p.get("description") or "")[:120])}</p>'
            f'</li>'
        )
    out.append('</ul>')
    out.append(render_foot())
    return "\n".join(out)


def build_categories(posts: list[dict]) -> str:
    canonical = BASE_URL + "/categories.html"
    head = render_head("カテゴリ — " + SITE["name"], "カテゴリ別記事一覧", canonical)
    out = [head, "<h1>カテゴリ別</h1>"]
    by_cat: dict[str, list[dict]] = {}
    for p in posts:
        by_cat.setdefault(p.get("category", "AI業界"), []).append(p)
    for cat, lst in sorted(by_cat.items()):
        out.append(f'<h2>{html.escape(cat)} <small style="color:var(--mut);font-size:14px">({len(lst)})</small></h2>')
        out.append('<ul class="post-list">')
        for p in lst[:20]:
            out.append(f'<li><h3><a href="posts/{p["slug"]}.html">{html.escape(p["title"])}</a></h3></li>')
        out.append('</ul>')
    out.append(render_foot())
    return "\n".join(out)


def build_sitemap(posts: list[dict]) -> str:
    urls = [BASE_URL + "/", BASE_URL + "/categories.html"]
    urls += [f"{BASE_URL}/posts/{p['slug']}.html" for p in posts]
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        parts.append(f"<url><loc>{sx.escape(u)}</loc><lastmod>{today}</lastmod></url>")
    parts.append("</urlset>")
    return "\n".join(parts)


def build_rss(posts: list[dict]) -> str:
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<rss version="2.0"><channel>',
             f"<title>{sx.escape(SITE['name'])}</title>",
             f"<link>{sx.escape(BASE_URL)}/</link>",
             f"<description>{sx.escape(SITE['description'])}</description>",
             f"<language>{SITE['lang']}</language>"]
    for p in posts[:30]:
        url = f"{BASE_URL}/posts/{p['slug']}.html"
        pub = p.get("published_at", datetime.now(timezone.utc).isoformat())
        parts.append("<item>")
        parts.append(f"<title>{sx.escape(p['title'])}</title>")
        parts.append(f"<link>{sx.escape(url)}</link>")
        parts.append(f"<guid isPermaLink='true'>{sx.escape(url)}</guid>")
        parts.append(f"<pubDate>{sx.escape(pub)}</pubDate>")
        parts.append(f"<description>{sx.escape(p.get('description',''))}</description>")
        parts.append("</item>")
    parts.append("</channel></rss>")
    return "\n".join(parts)


def main() -> int:
    log("=== build start ===")
    OUT.mkdir(exist_ok=True)
    (OUT / "posts").mkdir(exist_ok=True)

    # copy static assets if any
    if STATIC.exists():
        for p in STATIC.rglob("*"):
            if p.is_file():
                dest = OUT / p.relative_to(STATIC)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(p, dest)

    posts: list[dict] = []
    for md in sorted(POSTS.glob("*.md")):
        parsed = parse_post(md)
        if parsed:
            posts.append(parsed)
    posts.sort(key=lambda p: p.get("published_at") or "", reverse=True)
    log(f"loaded {len(posts)} posts")

    for p in posts:
        (OUT / "posts" / f"{p['slug']}.html").write_text(build_post_page(p))
    (OUT / "index.html").write_text(build_index(posts))
    (OUT / "categories.html").write_text(build_categories(posts))
    (OUT / "sitemap.xml").write_text(build_sitemap(posts))
    (OUT / "rss.xml").write_text(build_rss(posts))
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n")
    (OUT / "CNAME").write_text("")  # placeholder for custom domain later
    (OUT / ".nojekyll").write_text("")  # GH Pages: serve all dirs

    log(f"built {len(posts)} post pages + index + categories + sitemap + rss")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
