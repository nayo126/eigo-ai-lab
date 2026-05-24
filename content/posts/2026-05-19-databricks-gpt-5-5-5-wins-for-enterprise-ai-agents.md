---
{
  "title": "Databricks GPT-5.5: 5 Wins for Enterprise AI Agents",
  "description": "Databricks brings GPT-5.5 to enterprise agent workflows after a state-of-the-art OfficeQA Pro benchmark result.",
  "category": "AI Industry",
  "tags": [
    "Databricks",
    "GPT-5.5",
    "AI agents",
    "OpenAI",
    "enterprise AI"
  ],
  "keywords": [
    "Databricks GPT-5.5",
    "GPT-5.5 enterprise agents",
    "OfficeQA Pro benchmark",
    "enterprise agent workflows",
    "OpenAI Databricks partnership"
  ],
  "source_url": "https://openai.com/index/databricks",
  "source_name": "rss/openai_blog",
  "published_at": "2026-05-19T08:21:04.718442+00:00",
  "slug": "databricks-gpt-5-5-5-wins-for-enterprise-ai-agents"
}
---

## TL;DR
- Databricks GPT-5.5 is now powering enterprise agent workflows across the lakehouse platform, with deeper hooks into governed data and tool use.
- GPT-5.5 set a new state of the art on the OfficeQA Pro benchmark, which measures multi-step reasoning over realistic office tasks.
- The move puts pressure on rivals like Snowflake Cortex and AWS Bedrock to match both the raw model quality and the agent tooling layered on top.

## What happened

Databricks has rolled GPT-5.5 into the agent stack that customers use to build production assistants on top of their own data. The integration covers Mosaic AI Agent Framework, the Genie business-intelligence interface, and the Agent Bricks tooling that lets teams compose long-running workflows.

The headline result behind the deal is OpenAI's claim that GPT-5.5 set a new state of the art on OfficeQA Pro, a benchmark designed to test how well a model handles realistic enterprise office work. OfficeQA Pro mixes spreadsheet reasoning, document grounding, multi-step planning and tool calls, the same shape of work that enterprise agents are usually deployed to handle.

For Databricks customers, the practical effect is that GPT-5.5 becomes a first-class option inside the same governance surface as their warehouse tables, vector indexes and Unity Catalog policies. That means agent runs can read curated tables, call internal APIs and write back to managed data while staying inside the customer's existing audit trail, instead of routing through a separate consumer endpoint.

Neither company has shared customer-facing pricing details in the public note beyond confirming that GPT-5.5 is available to Databricks customers through the platform's model-serving endpoints. The OfficeQA Pro benchmark result is the primary technical claim being used to justify the upgrade over previous-generation models.

## Why it matters

The enterprise agent market has been stuck on a familiar pattern: a strong base model plus a thin wrapper of retrieval and tools, often deployed by a systems integrator. The Databricks-OpenAI integration tightens that loop.

Three shifts stand out.

First, the benchmark choice signals where the competition is heading. Generic reasoning scores like MMLU have lost most of their decision-making weight for buyers. OfficeQA Pro-style benchmarks, focused on multi-turn, tool-using work over messy documents, map much more directly to procurement criteria. Expect more vendors to point to office-task and agent-trajectory benchmarks rather than pure knowledge tests.

Second, the deal is a defensive play for Databricks against Snowflake. Snowflake Cortex has been pitching a similar story with a mix of in-house and partner models. Anchoring GPT-5.5 inside Mosaic AI gives Databricks a clear answer when a buyer asks which lakehouse can run the strongest commercial agent model against their own governed data without copying it out.

Third, it raises the floor for in-house builds. Teams that were stitching together their own agent loops on top of vanilla API calls now have a managed alternative with built-in evaluation, logging and policy controls. That tilts the build-versus-buy decision toward buy for routine enterprise workflows, while leaving room for custom builds where the data, latency or cost profile is unusual.

For independent builders, the takeaway is more pointed. Differentiation on prompt engineering or basic RAG is getting thinner. Workflow design, domain-specific evals and integration depth are where defensible value lives.

## Try it yourself

1. **Re-score your agent against an office-task benchmark.** Pull a small slice of OfficeQA Pro-style tasks (spreadsheet edits, document Q&A with citations, multi-step planning) and run your current stack through it. A 20-question custom eval beats relying on vendor marketing scores.
2. **Audit where your agent crosses the governance line.** List every place the agent reads or writes data outside a governed system. Each one is a future security review. If a lakehouse-native option like Mosaic AI Agent Framework removes a hop, that is worth real money over a year.
3. **Add a model-swap layer if you have not already.** Wrap the model call so swapping GPT-5.5 in for an older model is a config change, not a refactor. Vendors will keep shipping upgrades; the teams that benefit are the ones that can A/B in a day.
4. **Write a one-page eval rubric for agent runs.** Score success, partial success and failure modes (wrong tool, hallucinated value, infinite loop). Run it weekly. Most agent quality regressions show up in failure-mode mix shifts long before they show up in headline accuracy.
5. **Decide your build-vs-buy line in writing.** Pick one workflow currently handled by custom code and price out the managed alternative. Even if the answer is keep building, the exercise forces a clear view of total cost, including evals and oncall.

None of these require a Databricks contract. They are the same moves that make any agent stack more defensible whether the underlying model is GPT-5.5, Claude Sonnet 4.6 or an open-weight option.

## Sources

- [Databricks brings GPT-5.5 to enterprise agent workflows (OpenAI)](https://openai.com/index/databricks)
- [Mosaic AI Agent Framework (Databricks docs)](#) <!-- broken-link removed by broken-link-fixer: was https://docs.databricks.com/en/generative-ai/agent-framework/index.html -->
- [Snowflake Cortex AI overview](https://www.snowflake.com/en/data-cloud/cortex/)