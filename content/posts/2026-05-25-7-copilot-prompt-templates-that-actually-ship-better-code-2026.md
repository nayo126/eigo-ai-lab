---
{
  "title": "7 Copilot Prompt Templates That Actually Ship Better Code (2026)",
  "description": "GitHub Copilot and Microsoft 365 Copilot don't respond to prompts like ChatGPT does. Here are 7 copy-paste templates that get you usable output on the first try",
  "category": "AI Tools",
  "tags": [
    "GitHub Copilot",
    "prompt engineering",
    "Microsoft 365",
    "developer productivity",
    "AI coding"
  ],
  "pubDate": "2026-05-25",
  "source": "jp-translation",
  "source_path": "auto-blog/site/src/content/blog/copilotプロンプトテンプレ厳選7選2026年最新版.md"
}
---

You type a clear instruction into Copilot and get back code that's almost right but not quite. You tweak the comment, retry, tweak again. Twenty minutes later you've written the function yourself anyway.

The gap between people who get real leverage out of Copilot and people who fight it isn't talent. It's prompt quality. And the catch is that Copilot doesn't reward the same prompting habits that work on ChatGPT or Claude.

GitHub Copilot and Microsoft 365 Copilot are context-dependent tools. They read your open files, your cursor position, your existing document — not just the words you type. That changes the whole approach. Below are seven templates I keep on hand, plus the reasoning behind why they work, so you can adapt them instead of copying blindly.

## Why Copilot prompts aren't ChatGPT prompts

With ChatGPT or Claude, the winning move was always a long, detailed prompt — spell out every constraint, give it role-play context, list your requirements. Copilot is the opposite. It already has context (your codebase, your open Word doc), so a wall of text often makes things worse.

What Copilot rewards instead is a clean surrounding environment. Three habits move the needle more than any clever wording:

- **Put your intent in a comment at the top of the file.** One to three lines of plain English is the strongest prompt you can give Copilot.
- **Name things specifically.** `userPurchaseHistory` produces far better completions than `data`. The variable name *is* part of the prompt.
- **Show one example right before.** Copilot mimics the pattern immediately above the cursor — it behaves like few-shot prompting without you asking.

One more thing that comes up constantly in dev communities: write your file names and identifiers in English. Copilot's training data is overwhelmingly English, so `calculateMonthlyRevenue` gets sharper completions than the same function named in any other language. It works either way, but you're leaving accuracy on the table otherwise.

## Three core templates for generating code

### 1. The function spec

Write the contract as a comment block, then hit enter:

```
// Function: calculateMonthlyRevenue
// Input:  array of sales [{date: 'YYYY-MM-DD', amount: number}]
// Output: totals per month {'2026-05': 1000, ...}
// Errors: skip entries with an invalid date
```

When the spec is laid out as a bulleted contract like this, Copilot's first suggestion is usable almost every time. The key is listing the behavior, not describing it in prose. Inputs, outputs, edge cases — three lines and you're done.

### 2. Tests first

Write only the `describe` and `it` blocks before any implementation exists. Copilot reads the assertions and works backward to produce code that satisfies them. This works in Jest, Vitest, and Pytest equally well, and if you already lean TDD it fits your workflow perfectly — you get the test suite and the implementation in one pass.

### 3. Refactor in place

Drop a one-line comment directly above the code you want changed:

```
// rewrite the above using async/await
// convert the loop above to map/filter
```

Copilot reads the block it sits on top of and rewrites it. The trick is keeping the transformation rule to a single sentence. Vague instructions like "clean this up" give vague results; a specific operation gives a specific rewrite.

## Templates for writing with Microsoft 365 Copilot

### 4. Meeting-notes extractor

Paste your transcript into Word, open the Copilot side panel, and give it this:

```
Extract decisions, action items, and deadlines from this document
as a table. Mark any item with no clear owner as "TBD."
Keep each entry to one short sentence.
```

The phrase "as a table" is doing the heavy lifting. Ask Copilot to "summarize" and you'll get a loose bullet list; ask for a specific structure and it delivers a structure.

### 5. Email replies in Outlook

Outlook's Copilot reply feature gets erratic when you only feed it adjectives like "polite" or "professional." Constrain it with numbers instead:

```
Politeness 3/5, under 120 words, propose 3 alternative dates, no emoji.
```

Numeric limits keep the output stable across runs. "Friendly but brief" is interpreted differently every time; "under 120 words" is not.

## Two advanced templates that pay off in freelance work

### 6. Competitor analysis

When you've pulled competitor data into Excel and want Copilot to make sense of it:

```
Using competitor name (col A), monthly price (col B), and feature count (col C),
pick the top 3 best value-for-money options with reasons.
Each reason: under 15 words and must include a number.
```

The line "must include a number" alone kills the wishy-washy answers. If you do research-heavy writing on the side, this turns an hour of manual comparison into a 30-second pass.

### 7. SEO article outline

Pair this with Word and Microsoft 365 Copilot when you're drafting content:

```
Keyword: [insert]
Audience: working professionals, new to side hustles
Structure: conclusion-first, 5 H2 sections, ~150 words each
Must include: 2 concrete examples, 3 statistics, 1 counterargument
Banned phrases: "in today's world", "it's worth noting", "delve into"
```

Banning phrases is the most underused tactic here. AI defaults to a handful of filler constructions; explicitly forbidding them is the fastest way to make the draft sound like a person wrote it.

## Pricing, briefly

Worth knowing before you build a workflow around either tool: GitHub Copilot is $10/month or $100/year for individuals, and it's free for students and maintainers of popular open-source projects. Microsoft 365 Copilot runs $30/user/month on an annual plan, and it requires a qualifying Microsoft 365 license on top of that. The two are separate products with separate billing, even though they share a name.

## Copilot vs. ChatGPT: when to reach for which

These tools aren't competitors so much as different stages of the same job:

- **Copilot** wins at in-editor work — completing the function you're halfway through, refactoring a selection, finishing a test. It thrives on existing context.
- **ChatGPT or Claude** wins at the blank page — architecture decisions, long-form drafting, talking through an approach before you write a line.

In practice the efficient split is: use ChatGPT to think through the design and review the result, then let Copilot fill in the continuation as you type. If Copilot keeps missing, open the related files so they sit in your tabs, write the type definitions or function signature first, and use Copilot Chat's `/explain` and `/fix` to narrow things down conversationally.

## The real move: grow your own template library

Seven templates are a starting point, not a finish line. The thing that actually compounds is forking these into versions tuned to your own stack, your own clients, your own voice.

Copilot doesn't remember your wins between sessions — it isn't learning your preferences in the background. So when you land on a prompt that consistently works, save it. A Notion page, a plain text file, a snippets manager, whatever you'll actually reopen. Then paste it in every time.

The people who get paid for AI work treat prompts as an asset, not a throwaway. Add one template a day to your own collection and in three months you'll have a workflow nobody can copy, because it's shaped entirely around how you work.

## FAQ

**Do GitHub Copilot and Microsoft 365 Copilot need different prompting?**
Yes. GitHub Copilot reads your open files and cursor position, so the leverage is in function names and comments that signal intent. Microsoft 365 Copilot works off the existing content in Word or Excel, so short instructions that name the target range and output format win.

**What do I do when Copilot won't produce the code I want?**
Open the relevant files so they stay in your tabs, then write the spec as a comment directly above where the code should go. Adding type definitions or the function signature first sharpens the output. If it's still off, switch to Copilot Chat and use `/explain` and `/fix` to refine interactively.

**Which should I use — Copilot or ChatGPT?**
Copilot for completion and editor-bound work; ChatGPT or Claude for designing from scratch and long-form generation. The productive pattern is to have one continue your existing code while the other handles spec discussion and review.