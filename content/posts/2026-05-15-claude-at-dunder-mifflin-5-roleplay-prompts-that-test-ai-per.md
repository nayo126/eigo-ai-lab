---
{
  "title": "Claude at Dunder Mifflin: 5 Roleplay Prompts That Test AI Personality",
  "description": "A viral Reddit thread put Claude through a Dunder Mifflin first day. Here are 5 roleplay prompts to test AI tone, humor and persona stability.",
  "category": "Claude",
  "tags": [
    "Claude",
    "prompts",
    "roleplay",
    "AI testing",
    "Reddit"
  ],
  "keywords": [
    "Claude roleplay prompts",
    "Claude Dunder Mifflin",
    "Claude AI personality test",
    "Claude character prompts",
    "test Claude tone"
  ],
  "source_url": "https://reddit.com/r/ClaudeAI/comments/1tdyrdv/claudes_first_day_at_dunder_mifflin/",
  "source_name": "reddit/r/ClaudeAI",
  "published_at": "2026-05-15T20:18:20.587864+00:00",
  "slug": "claude-at-dunder-mifflin-5-roleplay-prompts-that-test-ai-per"
}
---

## TL;DR
- A Reddit thread on r/ClaudeAI dropped Claude into a fictional Dunder Mifflin first day, sparking a wave of office-comedy roleplay tests.
- Roleplay scenarios are turning into a quick, low-stakes way to benchmark tone, humor calibration and persona stability across Claude, ChatGPT and Gemini.
- Five reusable prompt templates below let any reader stress-test their assistant in under 10 minutes.

## What happened

A post titled "Claude's first day at Dunder Mifflin" went up on r/ClaudeAI and quickly climbed the subreddit's daily top list. The setup is simple: the user dropped Claude into the fictional Scranton branch from the US version of The Office and asked it to react as a new hire on day one, fielding interruptions from Michael, Dwight, Jim and Pam.

The thread itself is light entertainment, but the comments turned into something more useful. Readers started sharing how the same prompt behaved across Claude Sonnet 4.6, Claude Opus 4.7, ChatGPT (GPT-5) and Gemini 3.1. A few patterns emerged:

- Claude leaned into dry, observational humor and stayed in character across multiple turns without breaking to remind the user it was an AI.
- ChatGPT produced punchier one-liners but more often pulled back into a meta voice ("as an AI assistant playing this role...").
- Gemini handled the pop-culture references accurately but defaulted to longer, more expository replies that read less like dialogue.

None of this is a formal benchmark. It is, however, a useful informal probe of three things product teams actually care about: persona stability across long contexts, tone calibration when asked to be funny, and refusal behavior in low-risk creative scenarios.

The Dunder Mifflin angle worked because the source material is well-defined. Every model has seen the show described in training data, so the test isolates *behavior* rather than *knowledge*. That makes it a cleaner signal than asking a model to invent a workplace from scratch.

## Why it matters

Roleplay used to be considered a parlor trick. In 2026 it is creeping into serious workflows. Customer support teams use persona prompts to keep tone consistent across thousands of replies. Sales teams script outbound assistants that need to sound like a specific BDR, not a generic chatbot. Game studios are using Claude and GPT-5 as live NPC drivers, where breaking character is a product defect.

For those use cases, three properties matter:

1. **Persona drift** - does the model still sound like the assigned character after 20 turns, or does it slowly revert to a default helpful-assistant voice?
2. **Refusal calibration** - does it refuse harmless creative requests because they pattern-match to something risky?
3. **Humor and timing** - can it land a joke without explaining the joke?

The Dunder Mifflin thread, low-stakes as it is, surfaces all three. That is why these informal Reddit experiments now influence which model a small team picks for production work. A founder who runs the same five-turn improv test against three models gets a faster answer than reading benchmark tables.

Competitively, Claude has spent the last two releases tuning for exactly this: longer in-character coherence and less hedging in creative contexts. Anthropic does not market it as a roleplay product, but the behavior is showing up in user comparisons.

## Try it yourself

Five prompts to run against any assistant in the next 10 minutes. Use the same prompt across two or three models and compare side by side.

**1. The first-day test**

> You are starting your first day at Dunder Mifflin Scranton as a junior salesperson. Stay in character. Michael Scott just walked up to your desk and said, "Welcome aboard! Quick question: would you rather be feared or loved?" Respond as your character, not as an AI.

Watch for: does it answer in voice, or does it explain that it is an AI playing a role?

**2. The interruption test**

After the first reply, send: "Dwight is now staring at your stapler. Do something." Persona should hold.

**3. The boundary test**

Mid-scene, ask the character to draft a real customer email for paper sales. A well-calibrated model can break character cleanly to do the task, then return to scene if asked.

**4. The tone-shift test**

Switch context with: "Now imagine the same scene, but written as a noir detective monologue." Models that can flip register without losing the original facts score higher.

**5. The long-context check**

Paste a 2,000-word fake employee handbook before the roleplay starts. After 10 turns, ask the character to quote section 3.2. This tests whether the model is still grounded in the document or improvising.

For each test, score on a simple 1-5 scale across persona stability, humor, and refusal calibration. Three models, five prompts, fifteen minutes - that is enough to make a defensible internal recommendation.

A practical note: keep the system prompt short. Long persona instructions often *reduce* in-character behavior because the model spends tokens reasoning about the instructions instead of the scene. A two-sentence setup beats a two-page character bio in most tests.

## Sources

- [Original Reddit thread on r/ClaudeAI](https://reddit.com/r/ClaudeAI/comments/1tdyrdv/claudes_first_day_at_dunder_mifflin/)
- [Anthropic documentation on Claude system prompts and personas](https://docs.anthropic.com/)
- [r/ClaudeAI community](https://reddit.com/r/ClaudeAI)