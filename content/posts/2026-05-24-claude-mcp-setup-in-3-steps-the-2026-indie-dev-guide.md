---
{
  "title": "Claude MCP Setup in 3 Steps: The 2026 Indie Dev Guide",
  "description": "Wire Claude into your filesystem, GitHub, and browser with MCP. A no-fluff setup guide for Claude Desktop and Claude Code, plus the 5 servers worth installing.",
  "category": "Claude",
  "tags": [
    "Claude",
    "MCP",
    "AI Tools",
    "Developer Workflow",
    "Automation"
  ],
  "pubDate": "2026-05-24",
  "source": "jp-translation",
  "source_path": "auto-blog/site/src/content/blog/claude-mcp設定完全ガイド2026年版3ステップ導入術.md"
}
---

"I want Claude to read my local files." "I want it to hit my database directly." "I want it to post to Slack on its own." If you've thought any of that lately, you're not alone — these requests have exploded since the start of 2026.

The thing that actually makes them possible is **MCP (Model Context Protocol)**. Anthropic's open standard already ships with 100+ official servers, and the community catalog has blown past 1,000.

The catch: the moment people sit down to configure it, they hit a wall. "Where's the JSON file?" "I restarted and the icon never showed up." This guide walks through the fastest path for both Claude Desktop and Claude Code, the servers worth installing on day one, and how to fix the failures that trip everyone up.

## What MCP Actually Is

Short version: MCP is a common protocol that hands Claude an access pass to the outside world.

Out of the box, Claude lives inside a chat window. Want it to read a file? Paste it. Need current data? It can't reach it. Want it to touch another service? You do that part by hand. MCP tears down that wall. Through a server, Claude can connect to your filesystem, GitHub, Slack, a database, a browser — and call those tools itself to get work done.

The mental model that sticks: MCP is like a USB standard that gives Claude hands. The MCP server is the hand; Claude operates through the interface it exposes. You plug in the server you need, and Claude gains that capability without you rewiring anything.

What you get out of it:

- **Automation** — the manual copy-paste loop mostly disappears.
- **Bigger context** — point Claude at an entire internal doc set instead of pasting snippets.
- **Tool consolidation** — drive several SaaS tools from one Claude window.

The spec is open source, with SDKs for both TypeScript and Python, so a custom server is genuinely a few dozen lines of code if you ever need one that doesn't exist yet.

## Setting It Up in Claude Desktop

Short version: edit one config file, restart, done.

Three steps and you're live.

**1. Open the config file.**

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

If you don't want to hunt for it, the app's Settings → Developer → "Edit Config" opens the same file directly.

**2. Add an `mcpServers` block.**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/yourname/Documents"]
    }
  }
}
```

**3. Fully quit Claude Desktop and reopen it.**

"Fully quit" matters — closing the window isn't enough. Kill it from the dock or system tray so the background process actually restarts.

After the relaunch, look for the hammer icon below the input box. If it's there, you're connected. Type something like "list the files in my Documents folder" and Claude will reach into your local disk through MCP to answer.

Two prerequisites cover roughly 90% of "it won't work" cases: make sure Node.js and `npx` are installed, and make sure your JSON is valid — no trailing commas, no unclosed brackets. Get those two right and the rest tends to fall into place.

## Setting It Up in Claude Code

In Claude Code, the big win is that you add servers from the CLI with a single command instead of hand-editing JSON.

```bash
claude mcp add filesystem npx -y @modelcontextprotocol/server-filesystem ~/projects
```

That writes the config for you. To verify, run `claude mcp list`. To remove a server, `claude mcp remove <name>`. To check live status from inside a session, type `/mcp` for a full readout.

The other thing that makes the CLI worth it is scopes:

- `--scope user` — loaded across every project you work on.
- `--scope project` — scoped to the repo, written to `.mcp.json`, committable for the whole team.
- `--scope local` — your machine only, not shared.

For team work, commit a `project`-scoped `.mcp.json` and every contributor inherits the same toolset automatically. New-hire onboarding goes from "here's a wiki page of setup steps" to "clone the repo, you already have everything." That alone is reason enough to standardize on it.

## Five MCP Servers Worth Installing

Grouped by what they're actually good for, here are the ones earning their keep right now.

- **filesystem** — read and write local files. Install this first; everything else builds on having Claude work against real files.
- **github** — create issues, review PRs, search code straight from Claude. If you live in GitHub, this is the highest-leverage one.
- **playwright** — drive a browser. Web scraping and repetitive click-through tasks become "describe it once" instead of "do it 40 times."
- **postgres** — hand SQL queries off to Claude. Pairs perfectly with any kind of data-analysis freelancing.
- **slack** — post to channels, search history, send DMs without leaving the window.

For a freelance or side-project workflow, the **filesystem + github + playwright** trio is the sweet spot — it's not unusual for it to cut hands-on time by more than half. There's a widely shared Reddit thread where one dev reported shaving roughly 40 hours a month off their workload after adopting MCP. Your mileage will vary, but the direction is real: the more of your work is "move data between a file, a repo, and a browser," the more this stack erases.

## Common Failures and How to Fix Them

The places people get stuck are predictable, so front-load the fixes.

- **No icon after restart.** Almost always a JSON syntax error. Open the file in VS Code (or any editor with linting) and check for red squiggles before blaming anything else.
- **"Command not found."** Run `which npx` in your terminal, grab the full path it prints, and put that absolute path in the `command` field. The app doesn't always inherit your shell's `PATH`.
- **Permission errors.** On macOS, the first run needs you to grant Accessibility and Full Disk Access in System Settings. Until you do, file operations silently fail.
- **Need to pass secrets.** Use an `env` key in the server block to inject API keys and tokens per server, rather than leaking them into args.
- **Want to limit access to one directory.** Scope the filesystem server by passing only the target path as an argument — don't hand it your whole home folder.

You can read server logs from the Developer tab in settings. When something throws, copy the error text verbatim and paste it into Claude — more often than not it'll diagnose the cause and hand you the fix.

## A Few Habits That Keep It Sane

Once you've got more than one server running, two practices save you grief.

Start narrow on permissions. It's tempting to point filesystem at `~` and be done, but the first time Claude rewrites a file you didn't mean to touch, you'll wish you'd scoped it to a project directory. Grant the minimum and widen it when you actually need to.

Keep secrets out of version control. The `project`-scoped `.mcp.json` is great for sharing which servers a repo uses — but if a server needs an API key, pass it through environment variables, not literals in the committed file. Otherwise you've published a token to your whole team and your git history.

## Wrapping Up

Setting up Claude MCP comes down to editing one JSON file on Desktop, or running one command in Claude Code. Once it's in place, file management, GitHub work, and browser automation all collapse into the chat window — which is where the real efficiency gain lives.

Start with filesystem. Get comfortable with Claude reading and writing real files, then add servers that match your actual work — github if you ship code, postgres if you wrangle data, playwright if you automate the web. Build the stack one piece at a time and you'll never hit the wall of a setup you don't understand.

## FAQ

**Where is the Claude Desktop config file (`claude_desktop_config.json`)?**
On macOS it's at `~/Library/Application Support/Claude/claude_desktop_config.json`; on Windows it's `%APPDATA%\Claude\claude_desktop_config.json`. The fastest route is Settings → Developer → "Edit Config," which opens it directly.

**I configured a server but the icon never appears. Why?**
Usually a JSON mistake or a stale app process. Check for trailing commas and unclosed brackets, then fully quit Claude from the dock or system tray before relaunching. Also confirm `npx` is on your `PATH`.

**Is setup different between Claude Desktop and Claude Code?**
Yes. Desktop means hand-editing the JSON file; Claude Code uses the `claude mcp add` command in your terminal and can record servers per project in `.mcp.json`, which makes team sharing far easier.

**Which servers should a beginner install first?**
filesystem, github, and playwright (browser control). They let you immediately feel local file access and code management, they're all official or near-official, and each adds with a single `npx` line.
---

A couple of notes on choices I made: I dropped the affiliate card, the cross-site link blocks, and the JSON-LD schema since those are site-template cruft, not article content. I kept a tightened FAQ because it carries real reader value and helps land in the target word range. The Reddit "40 hours/month" claim is preserved but hedged ("widely shared," "your mileage will vary") since it's an unverified anecdote. No ¥/note/クラウドワークス conversions were needed — the original had none.