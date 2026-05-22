---
{
  "title": "7 ChatGPT Prompt Rules That Actually Change Your Output Quality",
  "description": "Stop getting generic ChatGPT answers. Seven prompt rules, three copy-paste templates, and the mistakes killing your output quality.",
  "category": "ChatGPT",
  "tags": [
    "ChatGPT",
    "prompt engineering",
    "AI productivity",
    "prompt templates",
    "GPT-5"
  ],
  "pubDate": "2026-05-19",
  "source": "jp-translation",
  "source_path": "auto-blog/site/src/content/blog/chatgptプロンプト書き方の基本7原則と実例集2026.md"
}
---

You ask ChatGPT for something. You get back a wall of generic mush. Meanwhile some person on Twitter is shipping a whole product with the same model. What's going on?

The honest answer: roughly 80% of ChatGPT's output quality is decided by how you write the prompt, not by which model you're paying for. Same GPT-5, same Claude Sonnet 4.6 — wildly different results depending on who's typing.

Here's what actually moves the needle in 2026, plus three templates you can paste in right now.

## Why prompt quality matters more than model choice

ChatGPT is bad at guessing. That's the whole story.

GPT-5 reasons well, but reasoning can't fill in context that isn't there. Type "write me a blog title" and the model has to assume an industry, an audience, a length, a tone. It picks the average of all of those, which is exactly why the output feels average.

Type "blog title for a skincare site targeting women in their 20s, SEO keyword 'pore care,' under 30 characters, include a number" and suddenly the candidates are usable. The model didn't get smarter. You got specific.

Researchers have been calling prompt design "a new programming language" for a couple of years now, and it's not hype — it's a skill that compounds. Get reasonable at it and you immediately outperform 80% of people using the same tools.

## The seven rules

You don't need all seven on every prompt. Pick three to five based on what you're trying to do.

**1. Assign a role first.** "You are a senior copywriter." "You are a tax accountant with 10 years of experience." Setting a role shifts the vocabulary, the assumptions, and the level of detail. It's the single highest-leverage line you can write.

**2. State the goal.** "The purpose is to get readers to sign up for a newsletter." When the model knows what success looks like, it optimizes structure and tone toward that outcome instead of producing something neutral.

**3. Use numbers for constraints.** "Under 500 characters." "Give me 3 options." "5 bullet points." Quantitative limits kill ambiguity. Vague constraints get vague output.

**4. Specify the audience.** "Working parents in their 30s." "Software engineers who've never freelanced." Audience specificity is what makes copy feel written *for* someone instead of *at* someone.

**5. Pin down the output format.** Table, JSON, Markdown with H2 headings, CSV — whatever you actually need. If you have to reformat the output by hand, your prompt was incomplete.

**6. Show examples (few-shot).** One or two examples of the tone or structure you want will outperform a paragraph of description. The model is a pattern matcher; give it a pattern.

**7. Ask for reasoning before the answer.** "Compare three angles before you decide." This works on both GPT-5 and Claude Sonnet 4.6 and produces noticeably more defensible conclusions, especially on judgment calls.

## Three templates worth saving

These are the ones I actually reuse. Fill in the brackets and go.

### Template 1: SEO article outline

```
You are a web writer with 10 years of SEO experience.
Keyword: [your keyword]
Target reader: [who it's for]
Goal: rank on page 1 of Google.

Output:
- 3 title candidates (under 60 characters, include a number)
- Intro paragraph (around 80 words)
- 5 H2 headings
- Keywords to include under each H2
```

### Template 2: Email reply draft

```
You are an executive assistant who writes concise, professional emails.
Context: [who you're replying to and what they want]
Tone: professional but not stiff
Length: under 120 words
No signature. Just a short greeting and the body.
Give me 3 versions.
```

### Template 3: Idea generation

```
You are a brainstorming consultant for new ventures.
Topic: [what you want ideas for]
Constraints: under $700 startup cost, runnable as a side project.
Use the SCAMPER framework. Give me 10 ideas, one line each.
```

Template 1 alone earns its keep if you write any content at all — I run it most days.

## The three mistakes that kill output quality

**Mistake 1: cramming everything into one prompt.** "Write the title, then the body, then social copy, then translate it" — every piece gets worse because the model is splitting attention. Break it into steps. One task per turn, one turn per task.

**Mistake 2: vague adjectives as feedback.** "Make it better." "More professional." These tell the model nothing. Try "lead with a sentence that names the reader's frustration" or "use more emotional verbs in the second paragraph." Specific feedback gets specific revisions.

**Mistake 3: trusting the output.** Even in 2026, ChatGPT hallucinates — especially on numbers, names, dates, and legal details. Treat every output as a first draft. Verify anything load-bearing against a primary source before it goes anywhere public.

## The takeaway

Seven rules: role, goal, constraints, audience, format, examples, reasoning. Mix three to five per prompt. Save the templates. Stop trying to be clever — be specific.

The fastest way to get better at AI is to get better at writing prompts. Pick one rule from this list, use it on your next ten prompts, and notice the difference. Then add another. Within a couple of weeks you'll wonder how you were getting anything done before.