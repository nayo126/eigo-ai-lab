---
{
  "title": "ChatGPT Prompting: 7 Patterns That 3x Your Output Quality",
  "description": "Stop getting generic answers from ChatGPT. Lock in role, constraints, and output format, set custom instructions once, and pull real work-grade responses every ",
  "category": "ChatGPT",
  "tags": [
    "ChatGPT",
    "prompt engineering",
    "custom instructions",
    "AI productivity",
    "role prompting"
  ],
  "pubDate": "2026-06-03",
  "source": "jp-translation",
  "source_path": "auto-blog/site/src/content/blog/chatgptプロンプト設定の方法精度が3倍変わる7つの型.md"
}
---

You've seen it. Two people open the same ChatGPT, type a question about the same thing, and one walks away with a usable draft while the other gets a wall of hedged generalities. Same model. Same subscription. Wildly different results.

The gap isn't the AI. It's how the prompt is set up. Change the way you frame the request and the quality of what comes back changes completely — not by a little, by a lot.

Here's the setup I use to get work-grade output, plus copy-paste templates you can drop in today.

## The core: lock in role, constraints, and output format

If you take one thing from this, take this. The single highest-leverage move in ChatGPT is specifying three things on every non-trivial prompt:

- **Role** — who it's answering as: "You're a senior copy editor."
- **Constraints** — the context and limits: "Reader is a beginner freelancer, no jargon."
- **Output format** — how it should come back: "Five bullet points, under 15 words each."

The reason is mechanical. ChatGPT is built to answer vague questions vaguely. Give it a role and it locks in the vocabulary and point of view. Give it constraints and it narrows the scope. Give it a format and the structure stays consistent. Fill those three slots and the same question produces something you can actually ship.

Skip them — type something like "how do I write a blog post?" — and you get textbook filler that applies to nobody. Think of the setup as handing the model the assumptions it should reason from *before* it starts writing. That's the whole game.

## Set custom instructions once, stop repeating yourself

ChatGPT lets you bake in your context so you're not retyping it every session. It's called **Custom Instructions**, under Settings → Personalization → Custom Instructions.

There are two boxes:

1. **"What should ChatGPT know about you?"** — your work, your goals, your level of expertise.
2. **"How should ChatGPT respond?"** — tone, length, formatting preferences.

Say you write content on the side. In box one: "I write web content as a freelancer. My readers are 20–30-something office workers." In box two: "Lead with the conclusion, use headers, footnote any technical terms." Now ChatGPT carries those assumptions into every chat without you spelling them out again.

Newer model generations also got noticeably better at pulling context across past conversations, on top of this stored profile. Set it once and the boilerplate you type at the start of each session drops by half, easily. If you're trying to claw back working hours, this is the first place to spend ten minutes.

## Use role prompting to raise the expertise floor

Opening a prompt with "You are a ___" is called **role prompting**, and it works because the role swaps out which vocabulary and reasoning patterns the model reaches for.

Concretely:

```
You're an SEO consultant with 10 years of experience.
Propose an article outline that can rank for the keyword below.
Give me 5 H2 headings, each with a one-line note on its purpose.
Keyword: "remote side hustle for beginners"
```

Splitting the role from the task like this gets you something far more practical than just "make me an outline."

Pick the role to match the job: "professional proofreader," "ex-hiring-manager running a mock interview," "a tax accountant's assistant." Developer and writing communities have reported the same thing for years — adding a role alone visibly bumps output quality. The trick is specificity: tack on years of experience or a niche so the model has something concrete to anchor to. "Senior backend engineer who's shipped payment systems" beats "engineer" every time.

## Pin the format and show an example to get exactly what you pictured

The last piece is **specifying the output format** and **showing an example** (few-shot prompting).

For format, name the shape you want: "as a table," "as JSON," "as an email under 100 words." Leave it open and ChatGPT defaults to long explanatory prose you then have to rewrite before it's useful.

To tighten it further, show one or two samples:

```
Write 3 headlines in this format.
Example:
- Time-saving → "Done in 3 minutes — never agonize over dinner again"
- Budgeting → "Save $70 a month: a quick household audit"
Theme: "getting started with a side hustle"
```

Hand it a model to imitate and it'll copy the tone and structure. The same principle holds across other models too — Claude, Gemini, whatever you're running. So when a prompt isn't landing, don't pile on more explanation. Show one example. It's faster and it works better than another paragraph of instructions.

## Putting it together

The whole approach collapses into a short loop: lock in role, constraints, and output format; store your context once in custom instructions; teach the format with an example. That's it. No clever tricks, no secret syntax.

Set your custom instructions today, add a role to your next prompt, and the responses you get back will look like they came from a different tool. Start with one setup that fits your actual work and build from there.

---

**Quick answers**

**Why does adding a role improve accuracy?** It pins down the vocabulary and viewpoint. "You're a professional editor" pulls in an editor's terminology and judgment, so you get specific, work-grade advice instead of generalities.

**Should I specify length and bullet formatting?** Yes. "Five bullets, under 15 words each" stabilizes the structure. Without a format, you get long generic prose that buries the point.

**What happens with a one-line question?** "How do I write a blog post?" gets you advice that fits everyone and helps no one. With no role, constraints, or format, the model can't narrow anything down.

**What goes in the constraints?** Your audience, assumptions, and limits — e.g., "reader is a beginner, no jargon." That scopes the answer to the right vocabulary and depth.