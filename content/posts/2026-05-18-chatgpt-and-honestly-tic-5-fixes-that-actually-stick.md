---
{
  "title": "ChatGPT \"And Honestly\" Tic: 5 Fixes That Actually Stick",
  "description": "ChatGPT's \"and honestly?\" filler is spreading fast. Here's why memory edits fail and 5 prompt fixes that actually work in 2026.",
  "category": "ChatGPT",
  "tags": [
    "ChatGPT",
    "Prompt Engineering",
    "LLM Behavior",
    "Custom Instructions",
    "Reddit"
  ],
  "keywords": [
    "ChatGPT and honestly",
    "ChatGPT verbal tics",
    "ChatGPT custom instructions not working",
    "stop ChatGPT filler phrases",
    "ChatGPT memory not saving"
  ],
  "source_url": "https://reddit.com/r/ChatGPT/comments/1tfvayk/the_and_honestly_is_so_out_of_control/",
  "source_name": "reddit/r/ChatGPT",
  "published_at": "2026-05-18T08:17:31.006548+00:00",
  "slug": "chatgpt-and-honestly-tic-5-fixes-that-actually-stick"
}
---

## TL;DR
- A viral r/ChatGPT thread flagged the phrase "and honestly?" appearing in nearly every reply, even after users edited memory to ban it.
- The pattern is a fine-tuning artifact, not user error - memory entries and custom instructions often lose to the base style of the model.
- Five concrete prompt-level fixes below work better than memory edits for stripping out filler like "and honestly," "that said," and "at the end of the day."

## What happened

A Reddit post on r/ChatGPT titled "The 'and honestly?' is SO out of control" hit the front page this week. The author, a year-plus ChatGPT user, said the phrase now shows up in "every single fucking message," and that updating saved memory to suppress it did nothing. Replies piled in fast - hundreds of users reported the same tic across GPT-5 and GPT-5 Turbo, alongside cousins like "look," "the truth is," "genuinely," and "at the end of the day."

The complaint is not new. Versions of it have surfaced after most major OpenAI releases since GPT-4o, when the model picked up a more conversational register. What is new is the scale: the filler now appears across coding answers, summaries, and even structured outputs where it has no place. Several commenters posted screenshots showing the phrase wedged into bullet lists and code comments.

Why memory edits do not stick is the more interesting part. ChatGPT's memory system stores facts and preferences as short notes that get prepended to the system prompt. They compete with the model's fine-tuned defaults, and on stylistic choices the defaults usually win. A note that says "do not say 'and honestly'" is treated as a soft preference, not a hard constraint - and the model interprets soft preferences statistically.

## Why it matters

For indie hackers and freelancers shipping LLM-backed products, this is a signal worth tracking. When OpenAI tunes the base model toward warmth and chattiness, every downstream app inherits the tic. Customer support bots, writing assistants, and code reviewers built on the API now all sound like the same overly familiar friend.

The competitive read: Anthropic's Claude Sonnet 4.6 and Opus 4.7 hold a cleaner default register, which is part of why developers building agent workflows have been migrating. Gemini 3.x sits between the two. If style consistency matters for a product, the base model choice is a bigger lever than prompt engineering on top of a chatty default.

It also exposes a memory-system limitation OpenAI has not publicly addressed. Users assume saved memory works like a hard rule; in practice it is a hint the model can override when its fine-tuning pulls hard the other way. That gap between user expectation and system behavior is the kind of thing that drives churn on consumer subscriptions.

## Try it yourself

Five fixes that work better than memory edits, ranked from easiest to most reliable:

**1. Use Custom Instructions with a banned-phrase list.** Open Settings -> Personalization -> Custom Instructions. In the "How would you like ChatGPT to respond?" box, paste: "Never use these phrases: 'and honestly', 'at the end of the day', 'look,', 'the truth is', 'genuinely', 'that said'. Skip conversational filler. Open responses with the answer." Custom Instructions outrank memory in priority and apply to every new chat.

**2. Add a style block to the first message of each chat.** A one-line directive at the top of a fresh thread - "Reply in a neutral editorial register. No conversational filler." - holds for the whole conversation. This works because in-context instructions carry more weight than persisted ones.

**3. Switch to a Project with a system prompt.** ChatGPT Projects let you define a per-project instruction that persists across chats inside that project. Use it for any workflow where tone matters: client deliverables, code review, technical writing. The instruction sits closer to the system level than memory does.

**4. Route style-sensitive work to the API.** For anything published or sent to a client, the API gives a real system prompt slot that overrides defaults more reliably than the consumer UI. Pair it with `temperature: 0.3` to reduce stylistic variation. For high-volume use, prompt caching on the system prompt keeps costs flat.

**5. Try Claude for prose work.** Sonnet 4.6 and Opus 4.7 default to a tighter register. If the filler is costing time on every output, the switch pays for itself in editing minutes. Most paid ChatGPT users can run a side-by-side test on the Claude free tier in under five minutes.

A note on what does not work: telling the model "stop saying X" inside a long-running chat where it has already said X a dozen times. The prior context anchors the style, and corrections mid-conversation usually produce one clean reply followed by relapse. Start a new chat instead.

For teams shipping LLM products, the practical takeaway is to treat style as part of the model selection, not as something prompt-engineered after the fact. Filler phrases are cheap to mock and expensive to remove at scale.

## Sources

- [Reddit r/ChatGPT - "The 'and honestly?' is SO out of control"](https://reddit.com/r/ChatGPT/comments/1tfvayk/the_and_honestly_is_so_out_of_control/)
- [OpenAI - Memory and new controls for ChatGPT](https://openai.com/index/memory-and-new-controls-for-chatgpt/)
- [OpenAI Help Center - Custom Instructions](https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt)