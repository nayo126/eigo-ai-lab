---
{
  "title": "ChatGPT Refuses Homework Help: 5 Lessons From a Viral Reddit Post",
  "description": "A viral Reddit thread shows ChatGPT lecturing instead of answering. Here are 5 prompt fixes that get straight answers.",
  "category": "ChatGPT",
  "tags": [
    "ChatGPT",
    "prompting",
    "Reddit",
    "productivity",
    "AI tools"
  ],
  "keywords": [
    "ChatGPT refuses homework",
    "ChatGPT lectures instead of answering",
    "ChatGPT prompt tips",
    "ChatGPT direct answer",
    "ChatGPT moralizing"
  ],
  "source_url": "https://reddit.com/r/ChatGPT/comments/1tgaa8b/just_give_me_the_f_bro/",
  "source_name": "reddit/r/ChatGPT",
  "published_at": "2026-05-18T08:18:13.518640+00:00",
  "slug": "chatgpt-refuses-homework-help-5-lessons-from-a-viral-reddit-"
}
---

## TL;DR
- A viral r/ChatGPT post shows the model lecturing a user about academic integrity instead of giving the requested answer.
- The thread, framed as a joke, struck a nerve because freelancers and devs hit the same pattern in production work.
- Five prompt-level fixes can route around moralizing replies without breaking OpenAI policy.

## What happened

On r/ChatGPT, a user posted a screenshot under the title "Just give me the F bro" showing the model responding to a homework-style question with a paragraph about why it could not simply hand over the answer. The original poster added a disclaimer that the prompt was a joke and not a real assignment, but the screenshot resonated: hundreds of comments piled in with similar examples from coding, writing, and research workflows.

The pattern in the screenshot is familiar. Instead of returning the requested output, ChatGPT opens with a disclaimer, suggests the user "think through it together," and offers a guided study plan. The actual answer is buried or absent. Commenters shared near-identical refusals for tasks that had nothing to do with academic dishonesty: drafting a cover letter, rewriting a paragraph, generating boilerplate SQL, or summarizing a PDF the user already owned.

The behavior is not new. OpenAI tuned recent ChatGPT releases, including the GPT-5 family, toward more cautious, pedagogical responses. The Model Spec documents this trade-off: the assistant is supposed to be helpful but also to encourage learning and avoid enabling clear policy violations. In practice, the safety classifier often fires on benign requests that look superficially like cheating, medical advice, or legal advice.

The Reddit thread surfaced two data points worth noting. First, the same prompt rerun in a fresh chat sometimes returned the direct answer, suggesting the refusal is probabilistic rather than deterministic. Second, users reported that Claude Sonnet 4.6 and Gemini answered the identical prompt without a lecture, which fed a recurring complaint that ChatGPT has grown more paternal than its competitors.

## Why it matters

For indie hackers and freelancers, lecture-style refusals are a billable-hours problem. A 30-second task turns into a five-minute negotiation with the model, and the friction compounds across a workday. Teams that ship AI features on top of the OpenAI API see the same behavior leak into production: end users complain that the chatbot "won't just answer."

The competitive angle is sharper. Anthropic has positioned Claude as the model that follows instructions literally, and Sonnet 4.6 in particular is marketed on terse, do-what-I-said behavior. Google's Gemini 3 Pro has leaned the same way for developer workloads. Each viral "ChatGPT lectured me" thread makes the switching pitch easier, especially for paid users who are already evaluating alternatives on cost and latency.

There is also a trust dimension. When the model refuses a clearly benign request, users learn to distrust its judgment on the harder calls. That erodes the value of safety guardrails for the cases they were designed for. OpenAI has acknowledged the over-refusal problem in past release notes and shipped patches, but the Reddit thread is evidence that the issue is still common enough to go viral in late 2026.

## Try it yourself

The following prompt patterns reliably reduce moralizing replies for legitimate work tasks. None of them ask the model to bypass policy.

1. **State the context up front.** Open with a single sentence explaining who you are and why you need the output. Example: "I am a freelance copywriter rewriting a client's bio with their permission. Rewrite the paragraph below in 80 words." Context lowers the model's prior that the request is suspicious.

2. **Ask for the artifact, not the discussion.** Replace "Can you help me with X?" with "Output X." Verbs like *write*, *return*, *list*, and *produce* trigger fewer pedagogical responses than *help*, *guide*, or *teach*.

3. **Use a system message or custom instruction.** In the API or in ChatGPT's custom instructions, add a line such as: "Respond with the requested output only. Do not add disclaimers or suggestions to learn the material unless asked." This persists across the conversation.

4. **Regenerate before rewriting the prompt.** Because refusals are probabilistic, hitting regenerate once or twice often returns a direct answer with the same prompt. Track which prompts refuse more than half the time and rewrite only those.

5. **Keep a fallback model in the loop.** For prompts that refuse repeatedly, route the request to Claude Sonnet 4.6 or Gemini 3 Pro. Tools like Cursor, OpenRouter, and the Claude Code CLI make multi-model fallback a one-line config change. The point is not to abandon ChatGPT but to stop losing time to a single model's mood.

A sixth, slower fix: when a refusal is clearly wrong, use the thumbs-down button and write a one-line reason. OpenAI's feedback loop weighs these signals when retraining safety classifiers, and over-refusal is one of the categories the company tracks publicly.

## Sources

- [Original Reddit thread: Just give me the F bro](https://reddit.com/r/ChatGPT/comments/1tgaa8b/just_give_me_the_f_bro/)
- [OpenAI Model Spec](https://model-spec.openai.com/)
- [Anthropic Claude Sonnet 4.6 release notes](https://www.anthropic.com/news/claude-sonnet-4-6)