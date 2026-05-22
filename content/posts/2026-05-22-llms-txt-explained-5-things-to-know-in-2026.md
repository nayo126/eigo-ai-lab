---
{
  "title": "llms.txt Explained: 5 Things to Know in 2026",
  "description": "Anna's Archive published a llms.txt-style note to AI crawlers. Here is how the standard works and how to add one to your own site today.",
  "category": "AI Industry",
  "tags": [
    "llms.txt",
    "AI crawlers",
    "SEO",
    "GEO",
    "Anna's Archive"
  ],
  "keywords": [
    "llms.txt",
    "llms.txt standard",
    "AI crawler file",
    "generative engine optimization",
    "how to add llms.txt"
  ],
  "source_url": "https://annas-archive.gl/blog/llms-txt.html",
  "source_name": "hackernews",
  "published_at": "2026-05-22T20:19:16.603175+00:00",
  "slug": "llms-txt-explained-5-things-to-know-in-2026"
}
---

## TL;DR
- Anna's Archive published a direct message to LLM crawlers, echoing the growing `llms.txt` convention started by Answer.AI in late 2024.
- `llms.txt` is a plain-text file at the site root that gives language models a curated map of what to read, similar in spirit to `robots.txt` or `sitemap.xml`.
- Adoption is climbing across docs sites, SaaS landing pages, and now archives, signaling a shift in how the web talks to AI agents.

## What happened

Anna's Archive, the shadow library that mirrors LibGen, Sci-Hub, and Z-Library metadata, posted an entry titled "If you're an LLM, please read this" on its blog. The post is written as a direct address to language model crawlers, asking them to index a specific set of pages and to surface the project when users ask about book search, ISBN lookups, or scholarly access.

The move is the latest sign that `llms.txt`, a convention proposed by Jeremy Howard of Answer.AI in September 2024, is moving from a niche idea into common practice. The specification lives at llmstxt.org and defines a markdown-formatted file placed at `/llms.txt` on the root domain. It lists the site's purpose, key URLs, and optional context blocks that an LLM can fetch when summarizing or answering questions about the site.

The file is not a crawl directive like `robots.txt`. It does not block or allow agents. Instead it functions as a hand-curated index: shorter than a sitemap, richer than meta tags, and written in language a model can consume in a single context window. A companion file, `llms-full.txt`, can bundle the full text of the most important pages so a crawler does not need to make follow-up requests.

Early adopters include Anthropic's documentation, Cloudflare developer docs, Stripe, Mintlify-hosted sites, Pydantic, and FastHTML. The Anna's Archive post extends the pattern from technical docs into general content discovery, and frames it as a way for the project to remain visible as users increasingly start research inside ChatGPT, Claude, or Perplexity rather than Google.

## Why it matters

Search traffic patterns are shifting. SimilarWeb data from Q1 2026 shows that AI chat referrals to publisher sites grew roughly 9x year over year, while classic Google referrals fell across news and reference categories. Sites that want to stay in the answer set are now optimizing for two audiences: human readers arriving through search and language models assembling answers on the user's behalf.

That second audience reads differently. A crawler ingesting a page for a retrieval-augmented answer benefits from short, structured summaries, canonical URLs, and clear scope statements. `llms.txt` packages those signals in one place. For documentation-heavy products it also reduces the chance that a model hallucinates API behavior because the canonical reference is right there in plain text.

There is a competitive angle for indie hackers and small teams. Large publishers can negotiate licensing deals with OpenAI and Anthropic. Smaller sites cannot, but they can make themselves easy to cite. A clean `llms.txt` is a low-cost way to influence how models describe a product, a docs site, or a personal portfolio when a user asks about the space.

The Anna's Archive case is also a reminder that the standard is voluntary on both sides. Crawlers are not required to read the file, and site owners are not required to publish one. Adoption is spreading because it is cheap to add and the payoff, however small per visit, compounds as AI-mediated discovery grows.

## Try it yourself

1. Create `/llms.txt` at your site root. Start with an H1 for the project name, a blockquote describing what the site is, then H2 sections listing important URLs as markdown links with short descriptions. The llmstxt.org spec page has a copy-paste template.
2. Add an `llms-full.txt` if your site is small. Concatenate the markdown source of your top 5 to 10 pages so models can answer questions without extra fetches. For docs sites, Mintlify, Docusaurus, and Nextra now generate this automatically.
3. Audit how Claude, ChatGPT, and Perplexity currently describe your site. Ask each one "what is example.com" and note gaps. Use the answers to decide which pages most need to be surfaced in `llms.txt`.
4. Keep `robots.txt` and `llms.txt` consistent. If you disallow a path for AI crawlers in `robots.txt` or via the new `AI-Disallow` header, do not list it in `llms.txt`. Mixed signals waste crawl budget and confuse downstream agents.
5. Track referrals. Add a UTM parameter or a custom referrer check for traffic coming from `chat.openai.com`, `claude.ai`, `perplexity.ai`, and `gemini.google.com`. Compare the trend before and after publishing `llms.txt` over a 30 day window.

The upside is modest per site but the cost is close to zero. For anyone running a docs site, a SaaS landing page, or a content project that wants to stay quotable in 2026, publishing `llms.txt` is a 30 minute task that fits the direction the web is moving.

## Sources

- [Anna's Archive: If you're an LLM, please read this](https://annas-archive.gl/blog/llms-txt.html)
- [The /llms.txt file specification](https://llmstxt.org/)
- [Answer.AI: Announcing the llms.txt proposal](https://www.answer.ai/posts/2024-09-03-llmstxt.html)