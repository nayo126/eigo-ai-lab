---
{
  "title": "Set Up Claude MCP in 15 Minutes: The 2026 Quick-Start Guide",
  "description": "A no-fluff walkthrough for wiring up Claude MCP on Desktop and Claude Code in 15 minutes, plus fixes for the errors that trip everyone up.",
  "category": "Claude",
  "tags": [
    "Claude MCP",
    "Model Context Protocol",
    "Claude Code",
    "AI Tools",
    "Developer Workflow"
  ],
  "pubDate": "2026-05-24",
  "source": "jp-translation",
  "source_path": "auto-blog/site/src/content/blog/claude-mcp設定方法を15分で完了する2026最新手順.md"
}
---

You heard MCP makes Claude dramatically faster to work with, sat down to set it up, and then hit a wall of English-only docs and JSON that wouldn't validate. Edit the config, add a server, restart, and the tools still don't show up.

The failure points are almost always the same. This is the stripped-down path: get MCP running from zero in about 15 minutes, on both Claude Desktop and Claude Code, with the common traps headed off before you hit them.

## What MCP Actually Is (and Why It Matters)

MCP (Model Context Protocol) is an open standard Anthropic shipped in November 2024. It's a common protocol for connecting Claude to external tools and data.

Before MCP, hooking Claude up to read your Notion or touch your local files meant building a one-off API integration every time. MCP standardizes that connection into a unit called a "server," so a single config file lets Claude reach across multiple tools at once.

### What you can do with it

Three main buckets:

- **Local file access** — read and write files in your Documents folder, your project directory, wherever you point it
- **External services** — GitHub, Notion, Slack, Google Drive, and more
- **Databases and APIs** — PostgreSQL, SQLite, any REST API you wire up

If you're freelancing, this is where it earns its keep: point Claude at every doc in a client project and have it draft meeting notes, or push research straight into Notion as you go — no glue code required.

### Desktop vs. Claude Code

MCP works in both the Claude Desktop app and Claude Code (the CLI), but the config location and syntax differ. Desktop uses `claude_desktop_config.json`. Claude Code uses `.mcp.json` or CLI commands. Worth knowing up front so you don't paste the wrong thing in the wrong place.

## Claude Desktop Setup (5 Steps)

In short: drop your server info into the config file as JSON, then fully restart the app. That's the whole game.

### Step 1: Open the config file

The paths, by OS:

- **macOS** — `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows** — `%APPDATA%\Claude\claude_desktop_config.json`

Easiest route: launch Claude Desktop, go to **Claude → Settings → Developer tab → Edit Config**. That opens the right JSON file directly, which beats hunting down the path by hand.

### Step 2: Add the mcpServers section

If the file is empty or just contains `{}`, paste this template:

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

Swap `/Users/yourname/Documents` for the absolute path of whatever folder you want Claude to reach.

### Step 3: Confirm Node.js is installed

That `npx` command needs Node.js. If you don't have it, grab the LTS build from [nodejs.org](https://nodejs.org/). Run `node -v` — if it prints a version number, you're set.

### Step 4: Fully quit and restart Claude Desktop

Use **Quit Claude** from the menu to close it completely, then reopen. Just closing the window won't reload the config — this is the single most common reason people think their setup "didn't work."

### Step 5: Verify the connection

Look for the 🔨 icon at the bottom-left of the input box. If it's there, you're connected. Click it to see the list of tools the MCP server exposes.

## Claude Code Setup

With Claude Code (the CLI), one command adds a server — you almost never have to hand-write JSON.

### Add a server via CLI

In your terminal:

```bash
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem /Users/yourname/Documents
```

Everything after `--` is the command Claude Code will run. Once it's added, `claude mcp list` shows your registered servers.

### Choosing a scope

Claude Code gives you three scopes:

- **local** (default) — your machine only
- **project** — saved as `.mcp.json` in the project, shareable with your team
- **user** — shared across all your projects

Working with a team? Add `-s project` and the server config gets committed to the repo so everyone gets it.

## 5 MCP Servers Worth Installing

The trick is to add only what you'll use. Load up a dozen servers and startup gets sluggish.

- **filesystem** — the go-to for local file access. Official Anthropic server.
- **github** — run issue, PR, and code searches directly
- **postgres** — query a database in plain language
- **brave-search** — web search (needs an API key; free tier is 2,000 calls/month)
- **memory** — gives Claude persistent long-term memory

The official server list lives at [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) and gets updated regularly. Count third-party servers and you're looking at 100+ options.

## When It Breaks: Troubleshooting

Nine times out of ten, a dead MCP setup comes down to one of three things: a JSON syntax error, Node.js not installed, or a forgotten restart.

### No tool icon showing up

Paste your config into [JSONLint](https://jsonlint.com/) and check the syntax. A missing or extra comma is the usual culprit — also watch for "smart" curly quotes if you copied the template through an editor that auto-formats.

### "Server disconnected" error

Check the logs. On macOS they're written to `~/Library/Logs/Claude/mcp*.log`, so run `tail -f` on them while you restart and the cause usually jumps out. Most often the `command` you specified isn't on your PATH, or a required environment variable is missing.

### npx is slow or times out

The first launch downloads the package, which routinely takes ~30 seconds — that's normal. To speed it up, install globally with `npm install -g @modelcontextprotocol/server-filesystem` and point `command` straight at `mcp-server-filesystem`.

### Permission errors

If the filesystem server throws "Permission denied" on macOS, you need to grant Claude Full Disk Access: **System Settings → Privacy & Security → Full Disk Access**, then add Claude.

## Wrapping Up

Setting up Claude MCP boils down to adding JSON to a config file and restarting the app. Once your first server (filesystem) works, GitHub, Notion, and the rest follow the exact same pattern.

If you're using Claude for client work or to cut down on busywork, MCP is about as high-ROI as setup investments get. Spend the 15 minutes, get Claude reading your own Documents folder, and build from there.

## FAQ

### Is Claude MCP free to set up?

The Claude Desktop app supports MCP on the free plan, and editing the config or adding servers costs nothing. Some connected services — GitHub integration, certain search servers — require their own API key or account, but the MCP layer itself is free.

### I added a server but no tools appear. Why?

Usually a forgotten restart or a JSON syntax slip. Fully quit and relaunch (don't just close the window), and check `claude_desktop_config.json` for missing commas or unclosed brackets. A missing Node.js install is the other frequent offender.

### Are Desktop and Claude Code configured differently?

Yes. Desktop means opening the config file from the GUI and editing JSON; Claude Code means running `claude mcp add` from the terminal. They store config in separate places, and a server added in one does not show up in the other.

### Where is the MCP config file?

On macOS, Claude Desktop stores it at `~/Library/Application Support/Claude/claude_desktop_config.json`. On Windows it's under `%APPDATA%\Claude\`. You can also open it directly from the app's Developer settings via "Edit Config."