---
{
  "title": "How to Connect MCP to Claude in 5 Minutes (2026 Guide)",
  "description": "A no-fluff walkthrough for wiring MCP servers into Claude Desktop, the three errors that trip everyone up, and three workflows that actually save freelancers ho",
  "category": "Claude",
  "tags": [
    "Claude",
    "MCP",
    "AI workflow",
    "automation",
    "developer tools"
  ],
  "pubDate": "2026-05-23",
  "source": "jp-translation",
  "source_path": "auto-blog/site/src/content/blog/claude-mcp接続方法を5分で完全マスター2026年最新.md"
}
---

"I want to hook MCP up to Claude, but I have no idea which part of the config file to touch." "I followed the official docs and it just errors out." If you've hit either wall, you're not alone — MCP setup questions have exploded over the past few months.

Here's the short version: connecting an MCP server to Claude comes down to adding a correct block of JSON to `claude_desktop_config.json` and restarting the app. That's it. Below I'll walk through the exact steps, the three failure modes that catch nearly everyone, and a few workflows that pay for the setup time within a day.

## What MCP actually is (30-second version)

MCP (Model Context Protocol) is an open protocol Anthropic released at the end of 2024. It's a standardized way to connect Claude to your local machine and external services safely. The cleanest mental model: it's USB-C for AI tools — one common port, swap in whatever you need.

The servers you'll reach for most:

- **filesystem** — read and write local files
- **github** — manage repos, open PRs
- **brave-search** — pull live web search results
- **postgres / sqlite** — query a database directly
- **slack** — post to channels, pull history

Tool-calling accuracy over MCP has jumped noticeably in recent Claude releases, which is the real reason it's worth setting up now. It's past the "cute demo" stage and into "I run this every day" territory.

## Connecting it in Claude Desktop — 5 steps

### Step 1: Open the config file

On macOS it lives at `~/Library/Application Support/Claude/claude_desktop_config.json`. On Windows it's `%APPDATA%\Claude\claude_desktop_config.json`. If the file doesn't exist yet, just create it.

### Step 2: Write the JSON

Here's the minimal config to wire up the filesystem server:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/yourname/Documents"
      ]
    }
  }
}
```

That last argument is the directory Claude is allowed to touch. Point it at a real working folder, not your home root.

### Step 3: Get Node.js in place

`npx` needs Node.js 18 or newer. Run `node -v` to check. If it's missing or outdated, grab it from nodejs.org. This is the single most common reason a server "silently doesn't start" — no Node, no npx, no MCP.

### Step 4: Fully quit and relaunch Claude Desktop

The config is **not** hot-reloaded. Closing the window isn't enough either — quit the app completely, including the tray/menu-bar process, then reopen it. Half the "it's not working" reports are just a window that was closed but not killed.

### Step 5: Confirm the connection

Look for the hammer icon at the bottom-left of the input box. Click it and you should see your registered tools listed. If they're there, you're live.

## The three errors everyone hits

**Error 1: "The server won't start."**
Nine times out of ten this is a bad path. On Windows, escape your backslashes as `\\`. On macOS, use an absolute path — no `~`, no relative shortcuts. Fix the path and the server usually comes right up.

**Error 2: "The hammer icon never shows up."**
That's a JSON syntax error. A missing comma or an unclosed quote will silently break the whole file. Open it in an editor with syntax checking (VS Code is fine) or paste it into an online JSON linter. Thirty seconds of validation beats an hour of guessing.

**Error 3: "Permission denied / can't read the files."**
The filesystem server only grants access to the directory you explicitly listed. If Claude can't see your Desktop or Downloads, it's because you didn't add them to the args. List every folder you actually plan to work in.

## Three MCP workflows worth setting up

This is where it stops being a toy. A few combinations that genuinely move the needle:

1. **Auto-drafting blog posts.** Pair `filesystem` with `brave-search` and tell Claude: "Research the latest trends on X and save a 2,000-word draft to `/blog`." You come back to a finished first draft instead of a blank page.

2. **Managing client deliverables.** Hook up the GitHub MCP and have Claude generate a README and a TODO list per project repo automatically. If you're freelancing on Upwork or similar, this roughly doubles how fast you can turn work around — less time on scaffolding, more on the actual job.

3. **Faster data analysis.** Connect the SQLite MCP to a local database and run queries in plain English. No more digging through Excel formulas or remembering exact SQL syntax — describe what you want and read the result.

A handful of freelancers chaining five-plus MCP servers together are already reporting they've doubled their monthly income off the efficiency gains. The window where this is still an edge — rather than table stakes — won't last forever. Most of 2026, at a guess.

## A quick note on cost

Worth saying plainly because it comes up constantly: the MCP protocol itself is free, and it works on Claude Desktop's free plan. The official servers — filesystem, github, and friends — cost nothing. A few servers like brave-search need an API key, and once you blow past their free tier you're into usage-based pricing. But you can get a full local setup running for $0.

## FAQ

**Where is the Claude MCP config file?**
macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`. Windows: `%APPDATA%\Claude\claude_desktop_config.json`. Create it if it's not there, and fully restart Claude Desktop after editing — changes don't apply until you do.

**Why won't my MCP server be recognized?**
Almost always a JSON mistake. The big three: a trailing comma, a missing double quote, or a wrong path in `command`. If `npx` can't be found, install Node.js 18+ and point `command` at an absolute path.

**Does using MCP cost anything?**
The protocol is free and runs on the free Claude Desktop plan. Official servers are free too. Some — like brave-search — require an API key and bill by usage once you exceed the free tier.

**How is MCP different from Claude API tool use?**
MCP connects local machines and external services through one shared standard, and runs inside the Claude Desktop app. API tool use has to be implemented in code, tool by tool. With MCP you add a JSON block once and reuse it everywhere — that reusability is the whole point.

## Bottom line

Connecting MCP to Claude is two moves: write the JSON, restart the app. The only hard part is the first time. Once a server is wired in, adding more takes a couple of minutes each. Start with filesystem, get comfortable, then expand into GitHub and SQLite — that's the shortest path. If you want an edge with AI in your workflow, get this set up this week.