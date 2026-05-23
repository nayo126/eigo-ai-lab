---
{
  "title": "7 Claude MCP Servers That Actually Earn Their Keep in 2026",
  "description": "A no-fluff rundown of the 7 Claude MCP servers worth installing for real freelance and indie work, plus setup gotchas and three workflows that save hours.",
  "category": "Claude",
  "tags": [
    "Claude",
    "MCP",
    "AI Tools",
    "Automation",
    "Freelancing"
  ],
  "pubDate": "2026-05-23",
  "source": "jp-translation",
  "source_path": "auto-blog/site/src/content/blog/claude-mcpおすすめ厳選7選2026年最新版.md"
}
---

You've heard of Claude's Model Context Protocol, you've skimmed the docs, and you've still got no idea which servers are actually worth wiring up. Fair. The official list is long, half of it is demo-grade, and nothing tells you what moves the needle when you're billing hours or shipping a side project at night.

Pick wrong and you bloat Claude with tools it fumbles over on every request. Pick right and Claude reaches into your GitHub, your Drive, and your Notion on its own — closer to having an assistant than a chatbot. Here are the seven MCP servers I'd actually install in 2026, scoped to freelance and indie work rather than enterprise theater.

## What MCP Actually Is

MCP (Model Context Protocol) is an open standard Anthropic shipped at the end of 2024 to connect LLMs to external tools through one shared interface. Before it, every AI had its own plugin spec. MCP made the connectors portable: build once, run it across any client that speaks the protocol.

In Claude Desktop you register servers in a single config file (`claude_desktop_config.json`), and from then on Claude calls those tools mid-conversation without being told twice. Wire up the GitHub server and "list the PRs I merged last week" just works — Claude queries the repo and answers.

The part people miss: **most MCP servers run locally**. Your data doesn't bounce through some third party's backend, which makes them reasonable for client work and anything mildly sensitive. The flip side is that server selection and permissions are on you. That's what the back half of this post is about.

## The 7 Servers Worth Installing

Skip the catalog-browsing. These seven cover the work that actually pays.

### 1. Filesystem

The classic. Give Claude read/write access to a local folder and you can search filenames, rewrite drafts, and reorganize directories in plain English. Point it at your drafts folder or asset stash and you're running in five minutes. If you install nothing else, install this one first.

### 2. GitHub

Drive repos, issues, and PRs directly from a conversation. Beyond code generation, it handles the chores: "group open issues by label and count them," or "update the README to match the latest commit." If you do any engineering work for clients, this is non-negotiable.

### 3. Notion

The database integration is the real draw. Hand Claude your task board, client records, and research notes, then fire off compound requests like "pull only the tasks due this week and draft a Slack message about them." One prompt, done.

### 4. Google Drive

Search across Sheets and Docs at once. Where it earns its slot: referencing an invoice template or an old proposal while it drafts a new document, so you're not copy-pasting boilerplate every time.

### 5. Slack

Summarize DMs and channel history, then draft replies. If you run a community or a paid Discord/Slack on the side, the time saved on triage adds up fast.

### 6. Brave Search

Adds real web search to Claude, which kills most hallucination on research tasks. Devs on Reddit keep reporting it's steadier than ChatGPT's browsing for fact-grounded answers.

### 7. Playwright

Browser automation. Form fills, price checks, light scraping — the repetitive routines you'd otherwise do by hand get handed to Claude.

## Three Rules for Not Screwing Up the Selection

Install too many servers and Claude burns cycles deciding which tool to reach for, and responses crawl. Narrow it down with these.

**Rule 1: Pick from your own work log.** Write down the three tasks you repeated most in the last week, then install only the servers that automate those. Sorting the marketplace by popularity and grabbing the top results is how you end up with a junk drawer.

**Rule 2: Keep write access minimal.** For Filesystem, scope it to one working folder, not your whole home directory. For GitHub, read-only on public repos unless you genuinely need more. Grant the smallest permission that does the job.

**Rule 3: Stick to official or well-known OSS.** There are documented cases of rogue MCP servers lifting your auth tokens. Pull from Anthropic's official repos or projects with 1,000+ stars and you avoid the obvious traps.

## Setup and the Three Things That Trip People Up

Open Claude Desktop, then **Settings → Developer → Edit Config**. Add your server to `claude_desktop_config.json`, restart the app, and it's live.

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/yourname/work"]
    }
  }
}
```

Three failure modes show up over and over:

1. **No Node.js installed.** If `npx` doesn't run, none of your servers start. Check this first.
2. **Bad absolute paths.** On Windows it's almost always an unescaped backslash.
3. **Tokens in plaintext.** Don't hardcode GitHub or Notion tokens in the JSON — pass them through environment variables.

Once it's running, ask Claude to "show me the tools you have access to." Whatever's wired up correctly shows up. If something's missing, your config almost certainly has a syntax error.

## Three Stacks That Map to Real Income

**Stack 1 — Full-stack blogging.** Filesystem + GitHub + Notion. Plan posts in Notion, write the drafts as local Markdown, publish by pushing to GitHub. Ask Claude to "run an SEO pass on this week's three posts" and it reads across all the files at once. Works the same whether you publish to your own site, Substack, or Medium.

**Stack 2 — Client-work automation.** Google Drive + Slack + Notion. Pull a proposal draft from Drive, summarize the Slack thread, drop meeting notes into Notion — all directed in plain language, no app-switching.

**Stack 3 — Research at speed.** Brave Search + Playwright + Filesystem. Competitor and keyword research that used to eat an hour drops to roughly fifteen minutes. On a $300/month research retainer, that's the difference between a thin margin and a real one.

## Start With Two, Then Earn the Rest

The right answer for Claude MCP isn't "everything" — it's the minimum that pays off. Install Filesystem plus the one server closest to your actual work, and run them hard for a week.

If your task time drops by a third, that's your signal to add another. The AI freelance market keeps getting more crowded in 2026, and the gap between people who've internalized this tooling and people who haven't is only widening. Open the config file today and ship the first one.

## FAQ

**Is Claude MCP free to set up?**
The servers themselves are open and free, and most integrations (GitHub, Notion, etc.) start on a free API tier. You'll still need Claude Pro ($20/month) or pay-as-you-go API usage — budget $20–30/month for serious use.

**Where do I configure the servers?**
In Claude Desktop's `claude_desktop_config.json`. On Mac it lives in `~/Library/Application Support/Claude/`. Edit it, save, restart the app, and the connections load.

**How is this different from ChatGPT plugins?**
MCP is Anthropic's open standard — build a connector once and reuse it across any compatible client. ChatGPT plugins are OpenAI-specific and don't port. MCP wins on both portability and its security model for external tool access.

**How many servers can I run at once?**
There's no hard cap; you can register ten-plus. But the more you add, the slower Claude gets at choosing tools. For freelance use, three to five hits the sweet spot between capability and responsiveness.