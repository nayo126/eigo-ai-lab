---
{
  "title": "How to Launch Claude Code: A 5-Minute Setup Guide for Beginners",
  "description": "Claude Code launches with a single command, but the setup around it trips people up. Here's the full flow from install to first prompt, plus fixes for when it w",
  "category": "Claude",
  "tags": [
    "Claude Code",
    "CLI tools",
    "AI coding",
    "developer setup",
    "terminal"
  ],
  "pubDate": "2026-05-24",
  "source": "jp-translation",
  "source_path": "auto-blog/site/src/content/blog/claude-code-起動方法を5分で解説初心者向け完全手順2026.md"
}
---

You installed Claude Code, opened your terminal, and… now what? If you're not used to the command line, the first step is usually where momentum dies. You're staring at a blinking cursor with no idea what to type.

Good news: launching Claude Code is one command. The hard part isn't the launch itself — it's the prep that comes before it and the errors that show up after. Get those two right and you'll be handing tasks to an AI inside your codebase in under five minutes.

Here's the whole flow, from a fresh install to your first working prompt, written so it makes sense even if you've never lived in a terminal.

## The launch command is just `claude`

Straight to the point: you start Claude Code by typing `claude` and hitting Enter.

```bash
claude
```

Claude Code is a CLI tool, and the installer registers it as a global command — so once it's set up, `claude` works from any directory. Run it and you drop into interactive mode, ready to type instructions.

For that single word to work, two things have to be true:

1. **Node.js 18 or newer** is installed.
2. **Claude Code itself** is installed.

Miss either one and you'll get the dreaded `command not found`. If you haven't installed it yet, this is the command:

```bash
npm install -g @anthropic-ai/claude-code
```

The `-g` flag means a global install, which is what makes `claude` available everywhere instead of being locked to one project folder. Give it a minute or two to finish.

## Three things to do before you launch

A clean launch comes down to a little prep. Knock these out first.

**1. Move into your project folder**

This is the one people skip, and it matters. Claude Code treats whatever directory you launched it from as its working directory — that's the context it reads and edits. So don't fire off `claude` from your home folder. `cd` into the project you actually want to work on first.

```bash
cd ~/projects/my-app
claude
```

If the project lives on your desktop, it's `cd ~/Desktop/my-app`. Launch from the wrong place and Claude will happily start reading the wrong files.

**2. Check your Node version**

Run this:

```bash
node -v
```

If the number is 18 or higher, you're fine. If it's lower — or nothing prints at all — grab the latest LTS from the Node.js site, or use `nvm` to install something current like Node 20. An outdated runtime is one of the most common reasons the launch errors out before it even starts.

**3. Have your login ready**

The first time you run `claude`, it'll ask you to authenticate with your Anthropic account. If you're on a Claude Pro or Max plan, you'll log in with that account. If you're using the API directly, have your API key handy so you're not scrambling when the prompt appears.

## What the first launch actually looks like

Run `claude` for the first time and your browser pops open to a login screen. Here's the play-by-play.

First you pick an authentication method. Pro and Max subscribers link their account by following the on-screen flow. Once that completes, control returns to the terminal and you'll see something like **"Login successful."** That's it — you're in.

Now you've got a prompt waiting for input. Try something simple to confirm it's working:

```
List every file in this folder.
```

Plain English is fine. Claude Code reads the directory and reports back. That moment — when it actually understands your repo and responds — is when the tool clicks.

A couple of things worth knowing right away:

- **To quit:** type `/exit`, or press `Ctrl + C` twice. (One `Ctrl + C` just cancels the current operation; it doesn't close the session.)
- **To resume your last session:** launch with `claude --continue` and it picks up the previous conversation instead of starting cold.

After this first login, you won't have to authenticate again. Your token is saved, so from now on `claude` drops you straight into the session.

## When it won't launch: a checklist

"I typed the command and nothing happens" is one of the most common Claude Code complaints, and the causes are predictable. Work through these top to bottom.

**You get `command not found`**

Either the install didn't go through, or the install location isn't on your PATH. First, confirm it's actually installed:

```bash
npm list -g
```

If Claude Code isn't in that list, reinstall it. If it *is* listed but the command still fails, fully close your terminal and reopen it — sometimes the PATH only updates in a fresh shell. If it still won't resolve, your npm global bin directory probably isn't in your shell config (`.zshrc`, `.bashrc`, etc.); adding it there fixes it permanently.

**You get `permission denied`**

This usually fails at the `npm install` step because npm can't write to its global directory. Two ways out: prefix the install with `sudo` (quick fix on macOS/Linux), or — the cleaner option — reconfigure npm to install global packages under your home directory so you never need elevated permissions again. The second approach saves you headaches down the line.

**The login page never opens**

If your browser doesn't launch automatically, Claude Code prints a URL in the terminal — copy it and paste it into your browser by hand. On corporate networks or behind a VPN, the auth handshake can get blocked; if you're stuck there, temporarily disabling the VPN and retrying usually does it.

When in doubt, `claude --help` lists every command and flag. Make checking it your first reflex when something behaves unexpectedly — it'll often answer the question faster than searching.

## Wrapping up

Launching Claude Code is genuinely just `claude`. The pieces that make or break a smooth start sit around that command: getting Node.js in place, `cd`-ing into the right project, and clearing the first login.

And when it won't start, the cause almost always boils down to one of three things — incomplete install, missing permissions, or a PATH that isn't set. Work the checklist calmly and it will run.

Best way to get comfortable: spin up a small throwaway folder, launch Claude in it, and ask it to do something trivial. Once you've felt what it's like to hand real work to an AI sitting inside your codebase, the rest stops feeling intimidating.

## FAQ

### Why do I get `command not found: claude`?

The install didn't complete, or the command isn't on your PATH. Re-run `npm install -g @anthropic-ai/claude-code` and reopen your terminal. It also happens when npm's global bin path isn't added to your shell config — add it there to fix it for good.

### Which Node.js version does Claude Code need?

Node.js 18 or higher. Check with `node -v`, and if you're below 18, update via the official site or `nvm` (Node 20 is a safe choice). An older runtime will throw an error before the session starts.

### How do I exit Claude Code?

Type `/exit` in interactive mode, or press `Ctrl + C` twice. A single `Ctrl + C` only cancels the current operation — the session keeps running.

### Is Claude Code free, or do I need to pay?

You need either a Claude Pro/Max subscription or pay-as-you-go API access. The Max plan runs roughly $100–200/month depending on tier; once subscribed, just follow the login flow on first launch and you're set.