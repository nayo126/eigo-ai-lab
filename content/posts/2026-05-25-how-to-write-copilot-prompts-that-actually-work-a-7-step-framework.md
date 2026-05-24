---
{
  "title": "How to Write Copilot Prompts That Actually Work: A 7-Step Framework",
  "description": "Copilot output lives or dies by how you prompt it. Here's a 7-step framework — role, context, constraints — to get cleaner code and fewer rewrites.",
  "category": "AI Tools",
  "tags": [
    "GitHub Copilot",
    "prompt engineering",
    "AI coding",
    "developer productivity",
    "Microsoft 365 Copilot"
  ],
  "pubDate": "2026-05-25",
  "source": "jp-translation",
  "source_path": "auto-blog/site/src/content/blog/copilotプロンプト作り方成果10倍の7ステップ2026.md"
}
---

You started using Copilot, and something feels off. The answers aren't quite what you asked for. Maybe it even feels a step behind ChatGPT or Claude. The tool isn't the problem — the way you're talking to it is.

Copilot is unusually sensitive to how you frame a request. GitHub Copilot Chat and Microsoft 365 Copilot are built to work *inside* your workflow, not as standalone chatbots. They pull context automatically: your open files, your repo, your Outlook thread, your Teams history. That changes everything about how you should prompt them. Drop in a generic ChatGPT-style prompt and you'll get generic results.

Here's the framework I use, broken into seven steps with templates you can copy straight into your editor.

## The core pattern: role × context × constraints

Every reliable Copilot prompt I write has three layers stacked on top of each other: **role definition, context, and constraints.**

The reason is simple. Copilot is optimized to answer as a continuation of whatever you're already doing. GitHub Copilot reads the surrounding code. Microsoft 365 Copilot reads your recent messages and documents. So the question isn't "what do I tell it about my situation" — it already knows a lot of that. The question is *what do I add* that it can't infer.

The skeleton looks like this:

```
You are a [role].
Working within [current situation / assumptions],
your goal is to [objective].
Follow these [constraints / output format].
```

Developers who share prompt breakdowns online consistently report the same thing: three-layer prompts produce far fewer rewrite cycles than one-liners. A vague "tell me about X" wastes the part of Copilot that's actually good. The structure below is just a practical way to fill in those three layers.

## Steps 1–3: Build the foundation

Get the skeleton right first. Skip this and no amount of clever phrasing later will save you — the output stays inconsistent.

### Step 1: Define a role in one line

Open with a single sentence that assigns a role. It shifts the vocabulary and the lens Copilot uses to answer.

- ❌ "Review this code."
- ✅ "You are a senior engineer with 10 years of TypeScript and React experience. Review the code below."

In GitHub Copilot Chat, the role line measurably changes which review angles it prioritizes — performance, type safety, readability — and the language it reaches for.

### Step 2: Hand it context as a bullet list

Copilot parses structured bullets more reliably than a wall of prose. Give it the facts in a scannable block:

```
Context:
- Project: admin dashboard for an e-commerce site
- Stack: TypeScript / Next.js 15
- Problem: the orders list page takes 3+ seconds to render
- Constraint: existing DB schema cannot change
```

This takes thirty seconds and it's the highest-leverage thing you can do. Half of bad Copilot output is just missing context the model had no way to know.

### Step 3: Make the goal measurable

State what "done" looks like in numbers or concrete states. Not "make it faster" — "get first contentful paint under one second." The moment the target is specific, the quality of the proposed solutions jumps, because Copilot can actually optimize toward something instead of guessing at your intent.

## Steps 4–5: Tighten precision with constraints

Foundation done. Now you sharpen the output.

### Step 4: Specify the output format

Tell Copilot exactly how you want the answer shaped: "as a Markdown table," "diff format only," "code blocks with language tags." Without this, every response comes back in a different shape, which makes reviewing and reusing the output a chore.

Some formats worth standardizing on:

- **Code suggestions:** "Return only the changed lines as a diff. Add a one-line comment explaining each change."
- **Design discussions:** "List pros, cons, and your recommended choice as three bullet sections."
- **Email drafts:** "Output in this order: subject, body, one-line summary."

### Step 5: Spell out what NOT to do

This one surprises people. Telling Copilot what to avoid is often as powerful as telling it what to do.

```
Constraints:
- Don't pull in heavy new dependencies
- Keep comments in plain English, no jargon
- Don't guess — if something's unclear, ask me first
```

That last line matters more than the rest. Left to its own devices, Copilot fills gaps with assumptions and barrels ahead. "Ask me if anything's unclear" stops it from confidently building the wrong thing, and it kills a huge share of off-target suggestions before they happen.

## Steps 6–7: The techniques that separate pros

This is where prompting starts paying off in real productivity — whether that's your day job or freelance work.

### Step 6: Use few-shot examples to lock in style

Few-shot just means showing one to three examples before you make the real request. It's the fastest way to get output in *your* voice instead of generic AI-speak.

Say you're drafting an email in Microsoft 365 Copilot. Paste two of your own past emails, then ask it to match the tone. The difference is night and day — the output stops reading like a stranger wrote it.

```
Here are examples of how I usually write emails:
[Example 1] ...
[Example 2] ...
Using the same tone, draft an email to schedule next week's meeting.
```

The same trick works for code style, commit messages, PR descriptions, documentation — anything where consistency matters.

### Step 7: Turn prompts into reusable assets

Rewriting the same prompt from scratch every time is a waste. Save the ones that work and build a library.

How I'd organize it:

1. **GitHub Copilot:** drop shared project rules into `.github/copilot-instructions.md` so every prompt inherits them automatically.
2. **Microsoft 365 Copilot:** save reusable prompts in Copilot Lab.
3. **Personal stash:** keep a Notion page or a plain text file sorted by use case — "code review," "meeting summary," "bug triage."

If you do any freelance dev work or AI writing on the side, this prompt library translates directly into delivery speed. Once you've got 20 solid templates, the per-project time often drops by more than half. You're not reinventing the prompt each time — you're filling in the blanks.

## A quick worked example

Putting all seven steps together, here's what a real Copilot Chat prompt looks like:

```
You are a senior frontend engineer fluent in React and TypeScript.

Context:
- Component: orders table in a Next.js 15 admin dashboard
- Problem: re-renders on every keystroke in the search box
- Constraint: can't add new state libraries

Goal: cut unnecessary re-renders so typing stays under 50ms latency.

Output:
- Diff format, changed lines only
- One-line comment per change explaining why
- If the fix needs info I haven't given, ask before assuming
```

Notice there's no "please help me" filler and no vague ask. Role, context, measurable goal, format, and a guardrail against guessing — all five live in one block. That's the whole game.

## The fastest route to better Copilot output

The foundation is the three-layer structure: role × context × constraints. Layer on a measurable goal, a format spec, an explicit don't-do list, a few-shot example, and a saved template, and the output quality stops being a coin flip.

Don't try to overhaul everything at once. Take one task you're doing today and run it through this frame. Do that for a week and the shift is obvious — you go from being jerked around by the AI to actually driving it.

Prompting isn't a talent. It's a pattern. The people who learn the pattern are the ones who pull ahead.

## FAQ

**What's the real difference between prompting Copilot and ChatGPT?**
ChatGPT needs you to spell out every detail in text. Copilot already pulls context from your code, Outlook, and Teams. So keep the role and constraints tight, and point it at the specific files or threads you want it to reference rather than re-describing them.

**How do I get more accurate results from GitHub Copilot Chat?**
Open the target file, reference it with `#file` or a selection, and add one sentence covering language, framework, and expected behavior. "Convert this React function to TypeScript and fix all type errors without leaving any" works far better than "fix this," because the constraint is baked in.

**What's a good Microsoft 365 Copilot prompt?**
Anything that pins down scope, format, and length: "Summarize the decisions from last week's Teams meeting in five bullets," or "Draft three reply options to this email, 200 words each." Specifying the reference range and output shape beats a vague request every time.

**What do I do when Copilot just won't give me the answer I want?**
Add three things: an explicit role, the exact files or conversations it should reference, and constraints on format and length. Don't aim for perfect on the first shot — read the output, then iterate with targeted follow-ups like "make the third point more concrete."