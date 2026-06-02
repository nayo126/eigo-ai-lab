---
{
  "title": "10 Claude Code Prompts That Triple My Freelance Output",
  "description": "The gap between slow and fast Claude Code users isn't skill — it's prompt design. Here are 10 copy-paste prompts that cut my build time, plus the anti-patterns ",
  "category": "Claude",
  "tags": [
    "Claude Code",
    "AI prompts",
    "freelance",
    "developer productivity",
    "AI coding"
  ],
  "pubDate": "2026-06-02",
  "source": "jp-translation",
  "source_path": "auto-blog/site/src/content/blog/claude-codeおすすめプロンプト10選副業効率3倍の実例集.md"
}
---

"I started using Claude Code, but the output isn't as good as I expected." If that's you, you're not alone — and the problem usually isn't the tool.

Two devs can run the exact same setup and get wildly different results. One ships a feature in an hour; the other spends the afternoon fighting half-right code. The difference is almost never raw skill. It's **how they write the prompt**.

Claude Code — the terminal-based coding environment running Claude Sonnet 4.6 and Opus 4.8 — mirrors what you give it. Vague instructions get vague answers. Specific instructions get output that's genuinely close to shippable. If you're learning to code and trying to pull in a few hundred extra dollars a month from coding gigs, tightening your prompts is the single highest-leverage thing you can do.

Below are 10 prompts I actually use, copy-paste ready, plus the mistakes that quietly kill your output.

## The Prompt Structure Worth Memorizing

Bottom line: structure every non-trivial prompt as **role → context → task → constraints → output format**. That ordering removes ambiguity about what the model should assume, what it should build, and where to stop.

"Build me a login feature" leaves the language, framework, and auth method undefined, so you get a generic guess back. Rewrite it like this:

```
You're an experienced backend engineer.
This project runs on Next.js 15 + TypeScript.
Build a login API using email and password.
Constraints: hash passwords with bcrypt, return errors as JSON.
Output: only the code for app/api/login/route.ts.
```

Five extra lines, and the quality of what comes back changes completely. "Context is everything" gets repeated in dev communities for a reason, and Claude Code is no exception.

It feels like overhead at first. Save it as a template and it costs you a few seconds each time.

## Prompts for Generating and Fixing Code

These are the workhorses. Copy them as-is.

**1. Get the lay of the land**
```
Read this repo's structure and summarize the role of each
major file as a bullet list.
```
Perfect first move when you pick up a new gig and inherit an unfamiliar codebase.

**2. Bug fix with repro context**
```
I'm getting this error: [paste the log]
List 3 likely causes, then propose a fix starting with the
most probable one. Quote the actual lines — no guessing.
```

**3. Targeted refactor**
```
Rewrite this function for readability without changing behavior.
Don't annotate with comments — instead explain your reasoning
in 3 separate lines.
```

**4. Generate tests**
```
Write unit tests for this function using Vitest.
Include 2 happy paths, 2 failure cases, and 1 boundary case.
```

The trick here is **specifying counts**. "Write some tests" often produces exactly one. Pin it with numbers — "2 happy paths, 2 failure cases" — and coverage goes up. Models are far better at concrete quantities than fuzzy ones like "a few."

## Applied Prompts That Speed Up Freelance Work

If you're knocking out gigs on Upwork or one-off contracts, Claude Code earns its keep well beyond writing code.

**5. Auto-generate docs**
```
Write a README for this project. Cover setup steps, environment
variables, and run commands. Keep it readable for non-engineers.
```
A clean README attached to your deliverable is an easy way to look more professional than the next freelancer.

**6. Commit message suggestions**
```
Review the current changes and propose 3 commit messages in
Conventional Commits format.
```

**7. Design review**
```
Flag the risks in this approach across 3 angles: maintainability,
performance, and security. No need to compliment anything.
```
That last line does real work. Without it, the model opens with praise and dilutes the actual problems you need to hear about.

**8. Reverse questions for learning**
```
List 3 concepts in this code I probably don't fully understand,
and explain each one for a beginner using an analogy.
```

Freelancing isn't only about delivering fast — it's about deepening your understanding so you can charge more. Use Claude Code as a tutor and every gig compounds your skills instead of just burning your time.

## Anti-Patterns That Quietly Wreck Your Output

A few common mistakes drag everyone down. Watch for these.

**NG1: Cramming everything into one prompt**
Ask it to "build login, payments, and email sending all at once" and every piece comes out half-baked. Split the work — one prompt, one objective.

**NG2: Hand it off and walk away**
```
Just build me a decent app.
```
This is the worst-performing prompt there is. Claude Code is capable, but with no defined goal it returns code that merely *looks* plausible. At minimum, spell out the three pillars: feature, tech stack, and constraints.

**NG3: Saying "it's broken" with no error attached**
Asking for help without a log or screenshot is like telling a doctor "fix me" without describing the symptom. Build the habit of pasting a four-part status block (**prompt 9**):
```
What I'm trying to do / What actually happens /
Full error text / What I've already tried
```

And **prompt 10: iterate**. Don't chase a perfect one-shot. Treat it as a conversation — "now change this part to that" — and you'll finish faster overall. Claude Code holds the immediate context, so incremental diff-style instructions land cleanly.

## Wrapping Up

Your results with Claude Code come down to prompt design far more than the model's horsepower. Keep the **role → context → task → constraints → output format** template in your back pocket, specify counts, and always share errors in full. Those three habits alone will visibly shrink your build time.

All 10 prompts above are copy-paste ready. Make one your default opening move on your next gig. Small improvements stack up — and over time they push both your rate and your speed higher.

## FAQ

**Which is better for code generation, Claude Code or ChatGPT?**
Claude Code's edge is that it reads and writes whole files in your terminal, handles multi-file edits, and runs tests in one flow. For a quick standalone snippet, ChatGPT is plenty — but for reworking an existing project or doing real freelance work, Claude Code is the more efficient pick.

**How much does Claude Code cost?**
Claude Pro is $20/month. The higher Max tier runs $100 or $200/month. If you're using it seriously for paid work, Max is the comfortable choice, but Pro is more than enough to start.

**Can I freelance with Claude Code as a complete beginner?**
Yes. For simpler gigs — HTML tweaks, WordPress customization — you can get a long way by instructing via prompts and pasting errors to fix them. Start with small coding jobs in the $100–300 range and spend a few months building your foundation.

**Why doesn't Claude Code produce the code I want?**
Usually because the instruction is vague. Name the language, framework, and version (e.g., Next.js 15), and write in the role → context → task → constraints → output format order. Don't expect perfection on the first pass — two or three rounds of correction is the normal path to a clean result.