---
{
  "title": "Databricks GPT-5.5 Agents: 5 Enterprise Workflow Takeaways",
  "description": "Databricks brings GPT-5.5 to enterprise agent workflows after a new OfficeQA Pro benchmark high. 5 takeaways for builders.",
  "category": "AI Industry",
  "tags": [
    "GPT-5.5",
    "Databricks",
    "Enterprise AI",
    "AI Agents",
    "OpenAI"
  ],
  "keywords": [
    "Databricks GPT-5.5",
    "GPT-5.5 enterprise agents",
    "OfficeQA Pro benchmark",
    "enterprise AI agent workflows",
    "OpenAI Databricks partnership"
  ],
  "source_url": "https://openai.com/index/databricks",
  "source_name": "rss/openai_blog",
  "published_at": "2026-05-18T20:20:58.886409+00:00",
  "slug": "databricks-gpt-5-5-agents-5-enterprise-workflow-takeaways"
}
---

## TL;DR
- Databricks GPT-5.5 agents now run inside enterprise data and analytics workflows on the Lakehouse platform.
- GPT-5.5 set a new state of the art on the OfficeQA Pro benchmark, which scores complex office-document reasoning.
- The move tightens the loop between raw company data, retrieval, and agent action without exporting data to a third party.

## What happened

OpenAI and Databricks expanded their partnership so that GPT-5.5 powers enterprise agent workflows running on top of Databricks data. The pitch: customers can build agents that read internal tables, documents, and BI assets, then act on them inside the same governance perimeter that already holds their data.

The headline number is OfficeQA Pro, a benchmark that tests how well a model can answer questions over spreadsheets, slide decks, and long documents the way a real office worker would. GPT-5.5 set a new state of the art on that benchmark, ahead of prior GPT-5 releases and competing frontier models. OfficeQA Pro matters more than generic MMLU-style tests for this audience because enterprise agents spend most of their time on messy structured files, not trivia.

Databricks is wiring GPT-5.5 into Mosaic AI Agent Framework and the Agent Bricks tooling its customers already use for evaluation, tracing, and deployment. That means an analyst can point an agent at a Unity Catalog table, attach a few PDFs, and get a GPT-5.5 backed workflow with auth, lineage, and eval baked in. Pricing follows the existing Databricks model token contract rather than a separate OpenAI bill, which is the part procurement teams care about.

The rollout covers Databricks customers on AWS, Azure, and GCP. Data does not leave the customer's cloud account for inference routing in the standard configuration. OpenAI confirmed that prompts and completions from this channel are not used to train future models.

## Why it matters

The enterprise AI market has split into two camps. One camp uses hyperscaler model gardens (Bedrock, Vertex, Azure AI Foundry) and stitches retrieval together themselves. The other camp uses data-platform-native agents where the model sits next to the warehouse. Databricks has been pushing the second pattern hard with Mosaic AI, and pulling in GPT-5.5 as a first-class option makes that pitch sharper.

For OpenAI, this is a distribution play. Databricks reports more than 10,000 customers and a heavy concentration of Fortune 500 data teams. Getting GPT-5.5 in front of those teams without forcing them to leave the Lakehouse cuts the sales cycle from months to a click. It also blunts Anthropic's recent momentum in enterprise agents, where Claude Sonnet 4.6 and Opus have been the default pick for many regulated buyers.

The OfficeQA Pro result is the technical hook. Office documents are the long tail of enterprise work, and most LLMs still trip on multi-sheet Excel logic or 200-slide decks with embedded charts. A model that genuinely handles those formats reduces the amount of preprocessing and chunking pipelines a team has to maintain. Less glue code means cheaper agents and fewer failure modes in production.

The competitive angle for builders: if a model that lives inside the data platform is good enough at office-document reasoning, the case for a standalone RAG stack weakens. Vector database vendors, niche document-AI startups, and BI copilots all sit closer to commodity now. The teams that win will either go deeper on a vertical (legal, clinical, financial) or move up to orchestration across many agents.

## Try it yourself

1. **Benchmark your own office-doc task before switching.** Pull ten real spreadsheets and ten real decks from the last quarter. Ask the current model and GPT-5.5 to answer the same five questions per file. Score for factual accuracy and citation quality, not vibes. OfficeQA Pro is a proxy, not a guarantee for any one workflow.
2. **Pilot inside Mosaic AI Agent Framework if Databricks is already in the stack.** Start with one read-only agent over a single Unity Catalog schema. Wire up tracing and a 50-question eval set before opening it to end users. The native integration removes most of the auth and lineage work that usually eats the first sprint.
3. **Lock down data egress in the agent config.** Confirm that prompts, retrieved chunks, and tool outputs stay inside the customer cloud account. Document the routing path for the security review. This is the question that kills enterprise pilots six weeks in if it was not handled on day one.
4. **Compare cost per resolved task, not per token.** GPT-5.5 may price higher per million tokens than smaller models, but if it finishes a multi-step office task in one pass instead of three, total spend can drop. Track turns-per-task and tool-call counts in tracing.
5. **Keep a fallback model wired in.** Configure the agent framework to route to Claude Sonnet 4.6 or a smaller Databricks-hosted model for low-stakes calls or when GPT-5.5 hits rate limits. Single-model dependencies are the most common reliability failure in production agents.

For indie builders without a Databricks contract, the practical takeaway is narrower. The OfficeQA Pro number signals that GPT-5.5 is now a stronger default for any agent that touches spreadsheets or long documents through the standard OpenAI API. Test it on the messy files that actually break the current pipeline before assuming the gain transfers.

## Sources

- [OpenAI: Databricks brings GPT-5.5 to enterprise agent workflows](https://openai.com/index/databricks)
- [Databricks Mosaic AI Agent Framework](#) <!-- broken-link removed by broken-link-fixer: was https://www.databricks.com/product/machine-learning/mosaic-ai-agent-framework -->
- [OpenAI Platform: Models](https://platform.openai.com/docs/models)