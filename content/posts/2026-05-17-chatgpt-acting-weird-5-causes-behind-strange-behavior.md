---
{
  "title": "ChatGPT Acting Weird? 5 Causes Behind Strange Behavior",
  "description": "ChatGPT acting weird? 5 common causes behind odd replies, loops and refusals, plus fixes that work in 2026.",
  "category": "ChatGPT",
  "tags": [
    "ChatGPT",
    "Troubleshooting",
    "Prompt Engineering",
    "LLM",
    "AI Tools"
  ],
  "keywords": [
    "chatgpt acting weird",
    "chatgpt strange behavior",
    "chatgpt not working",
    "chatgpt prompt fixes",
    "chatgpt troubleshooting 2026"
  ],
  "source_url": "https://reddit.com/r/ChatGPT/comments/1tf5bco/whats_this_bheaviour/",
  "source_name": "reddit/r/ChatGPT",
  "published_at": "2026-05-17T08:17:23.919488+00:00",
  "slug": "chatgpt-acting-weird-5-causes-behind-strange-behavior"
}
---

## TL;DR
- A viral r/ChatGPT thread asking "what's this behaviour??" reignited a familiar question: why does ChatGPT suddenly act strange mid-conversation?
- Five repeat causes show up across community reports: context overflow, system prompt drift, safety reroutes, model swaps, and stale memory entries.
- Most odd outputs can be fixed in under a minute with a fresh chat, a memory audit, or a model switch inside the same workspace.

## What happened

A short Reddit post on r/ChatGPT titled "what's this bheaviour??" sparked another round of community debate about ChatGPT acting weird. The original poster shared a screenshot of an unexpected reply, and within hours the comment thread filled with users describing similar oddities: replies cut off mid-sentence, the model repeating the same paragraph twice, refusals on benign prompts, switches between English and another language without being asked, and personas the user never set up.

The thread is one of several that have appeared on r/ChatGPT, r/OpenAI and r/singularity through May 2026. The pattern is consistent. Users open a long chat, send a routine follow-up, and the model returns something that looks broken: a wall of repeating tokens, an apology with no answer, or a sudden swing in tone from technical to casual.

OpenAI has not published a specific incident note tied to the May thread, but the company's status page logged two partial degradations in the prior 14 days, both labeled as elevated error rates on ChatGPT. Independent monitoring sites recorded short spikes in latency on the same days. Neither outage was full, which matches what users describe: not a hard failure, just degraded answers from an otherwise live product.

Developers running the same prompts through the API reported fewer issues than ChatGPT.com users. That gap points to the consumer surface, where memory, custom instructions, voice mode and tools are layered on top of the base model, as the more likely source of the odd behavior rather than the underlying weights.

## Why it matters

For casual users, a glitchy session is annoying. For freelancers, indie hackers and small teams who run client work through ChatGPT, it is a billable hour at risk. A single weird reply during a live demo or a paid coaching call can erode trust in the workflow.

The community pattern also signals a structural issue with how chat products age. The base model is one input, but the actual reply is shaped by saved memories, a system prompt the user cannot see, a router that may swap models silently, and a safety layer that can intervene. Each of those layers is a place where state can drift. The more a user invests in custom instructions and saved memory, the more surface area exists for a mismatch.

Competitive context: Anthropic's Claude and Google's Gemini ship similar features, and both have logged comparable community threads in the past quarter. Switching tools does not remove the underlying problem. What changes is which layer fails first. For Claude, users most often report context window saturation in long Projects. For Gemini, the common complaint is grounding citations that contradict the answer. For ChatGPT, it is memory and persona drift.

The practical takeaway for buyers: pick the tool whose failure mode you can debug fastest in your workflow, not the one with the highest benchmark.

## Try it yourself

Five checks that resolve most reports of ChatGPT acting weird:

1. **Start a fresh chat.** Long sessions accumulate context that competes with the current prompt. If a reply looks broken, copy the last instruction into a new conversation and resend. If the new chat answers cleanly, the prior session was the cause.
2. **Audit saved memory.** Open Settings, then Personalization, then Manage Memory. Delete entries that are outdated, contradictory, or written in a different language than the current task. A single stale line such as "the user prefers responses in German" can flip every future reply.
3. **Check Custom Instructions.** In the same Personalization menu, review the two free-text fields. Long, layered instructions written months ago often conflict with current tasks. Trim to under 200 words per field and test again.
4. **Force a model switch.** Use the model picker at the top of the chat to swap between GPT-5, GPT-5 mini, and the legacy options. If one model returns the bug and another does not on the same prompt, the issue is routing or that specific model, not the prompt itself. Report it via the thumbs-down button so the conversation is flagged.
5. **Disable tools for the test.** Turn off web search, code interpreter, and file uploads, then resend the prompt. Tool calls add an extra round trip and a parsing step where output can break. If the bare model answers correctly, the tool layer is the source.

For team workflows, add one safeguard: keep a separate "clean" ChatGPT account or project with no memory and minimal custom instructions, reserved for client-facing work. When the main account starts acting weird mid-call, switch to the clean one rather than debugging live.

The odd behavior reported on Reddit is rarely a model regression. It is almost always state, configuration, or tool layer drift. Treat the five checks above as a one-minute pre-flight before any session that matters.

## Sources

- [Reddit r/ChatGPT: what's this bheaviour??](https://reddit.com/r/ChatGPT/comments/1tf5bco/whats_this_bheaviour/)
- [OpenAI Status Page](https://status.openai.com/)
- [OpenAI Help: Memory and Custom Instructions](https://help.openai.com/en/articles/8590148-memory-faq)