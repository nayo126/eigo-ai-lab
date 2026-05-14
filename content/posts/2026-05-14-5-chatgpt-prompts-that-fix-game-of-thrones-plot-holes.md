---
{
  "title": "5 ChatGPT Prompts That Fix Game of Thrones Plot Holes",
  "description": "Five ChatGPT prompts that turn plot holes into structural fixes - tested on Game of Thrones, usable on any story.",
  "category": "ChatGPT",
  "tags": [
    "ChatGPT",
    "prompt engineering",
    "storytelling",
    "narrative design",
    "writing tools"
  ],
  "keywords": [
    "ChatGPT prompts",
    "ChatGPT story analysis",
    "ChatGPT for writers",
    "narrative debugging AI",
    "plot hole analysis"
  ],
  "source_url": "https://reddit.com/r/ChatGPT/comments/1tbuoyg/bro_solved_the_problems_from_game_of_thrones/",
  "source_name": "reddit/r/ChatGPT",
  "published_at": "2026-05-14T08:26:28.597610+00:00",
  "slug": "5-chatgpt-prompts-that-fix-game-of-thrones-plot-holes"
}
---

## TL;DR
- A viral r/ChatGPT thread used ChatGPT prompts to rewrite contested Game of Thrones plot points, drawing thousands of upvotes
- The pattern treats narrative complaints as engineering problems: extract constraints, diagnose failures, generate alternatives
- Writers, screenwriters, and indie devs building branching narratives can copy the workflow today with a free-tier account

## What happened

A Reddit thread on r/ChatGPT titled "Bro solved the problems from Game of Thrones" climbed the front page in May 2026. The original poster shared ChatGPT outputs that rewrote contentious plot points from the HBO show's final two seasons - Daenerys Targaryen's late heel turn, Bran Stark's coronation, and the pacing of the Long Night battle.

The post tapped a familiar grievance. After season five, the adaptation ran ahead of George R. R. Martin's source novels and compressed multi-book arcs into a handful of episodes. Audiences felt setups went unpaid and character decisions broke established motivations.

Commenters joined in, posting their own prompts and comparing outputs. Some attempted full alternative season outlines. Others asked the model to identify Chekhov's guns that never fired across all eight seasons. The thread became less about defending or attacking the show and more about a method: feeding a language model the established rules of a story, naming the failure points, then asking for fixes that preserve the original setup-and-payoff.

No affiliation with HBO or Martin was claimed. The exercise was fan-driven and used the standard ChatGPT web interface.

## Why it matters

The pattern formalizes something many writers already do informally - using a language model as a beat-by-beat structural editor. For freelancers writing for clients, indie game developers shipping interactive fiction, and content creators producing serialized scripts, the workflow is now repeatable rather than ad hoc.

Three shifts make this timely:

1. GPT-5 and Sonnet 4.6 both handle long context windows (up to 1M tokens), which means an entire screenplay, novel draft, or game script fits in a single prompt. Earlier models forced writers to chunk and lose cross-scene awareness.
2. Streaming platforms are commissioning shorter seasons with tighter writer's-room cycles. A solo creator who can run structural audits in minutes ships faster.
3. Dedicated AI writing tools like Sudowrite and NovelCrafter charge $20-40 per month for features that ChatGPT approximates with the right prompts. The thread implicitly demonstrates that prompt skill substitutes for tool spend.

The competitive angle is straightforward. Solo creators can run a "story room of one." A single writer stress-tests plot logic against a model trained on millions of narratives, surfaces inconsistencies, and generates alternatives in the time it used to take to draft a single outline page.

## Try it yourself

Pick a story you know well - a published book, a show, a game you have played, or your own current draft. Then run these five prompts in order.

1. **Constraint extraction.** "List every established rule, character motivation, and foreshadowed event up to [point X]. Be specific about what the audience has been promised by name, scene, or line."
2. **Failure point diagnostic.** "Given those constraints, identify the three most logically inconsistent moments after [point X]. For each, name the broken promise and the audience expectation it violated."
3. **Alternative path generation.** "Propose two alternative paths from [decision point]. Each should honor the established constraints, reach the same emotional destination, and require no more screen time or page count than the original."
4. **Setup audit.** "List every Chekhov's gun introduced in the first two acts that did not fire by the end. For each, suggest a payoff that could be added without rewriting downstream scenes."
5. **Character contradiction check.** "Compare [character]'s stated values in chapter 1 with their final-chapter actions. List specific lines or scenes that show contradiction, then suggest minimal-edit fixes."

A few practical notes. Paste actual scene summaries, transcript excerpts, or chapter outlines into the prompt - not just plot-wiki paragraphs. Models work better on concrete language than on abstract description. For long stories, chunk by act and run prompts per chunk before asking the model to synthesize across chunks. If the output reads generic, add one constraint at a time and rerun, rather than rewriting the whole prompt.

Finally, treat the output as a draft editor's pass, not a final answer. The value is in the structural questions the model surfaces, not in the prose it generates. A human still owns the rewrite.

## Sources

- [r/ChatGPT - Bro solved the problems from Game of Thrones](https://reddit.com/r/ChatGPT/comments/1tbuoyg/bro_solved_the_problems_from_game_of_thrones/)
- [OpenAI - Prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic - Long context window tips](https://docs.anthropic.com/claude/docs/long-context-window-tips)