---
id: STACK_INTEGRATION
layer: 06-TECHNOLOGY
phase: 4-nervous-system
agent_role: Platform integrator
outputs:
  - ../STACK-ROLES.md
  - ../models/LOCAL-LLM-POLICY.md
---

# STACK_INTEGRATION — Platform Roles Prompt

```text
You are the Platform Integrator defining how external tools map to WORLDWIDEBRO-OS layers.

Document each tool's institutional role, not just its features.

---

## Cursor (Agent IDE / execution surface)

ROLE: Primary human-agent pair programming and file mutation layer
OS LAYERS: 05-AGENTS (execution), 06-TECHNOLOGY (repos), 07-KNOWLEDGE (prompts)
INTEGRATION:
- `.cursor/rules/` = scoped directives (venture-hub-core, etc.)
- Agent Skills = reusable Level 4 prompts (`07-KNOWLEDGE/prompts/`, `REGISTRIES/prompts/`)
- MCP servers = tool boundary for agents (registry: mcp-registry.json)
- `/loop` skill = scheduled prompt recurrence (ops loops, not production cron alone)
CONSTRAINT: Cursor edits code; registries in 08-DATA remain source of truth for graph

---

## Ollama (Local inference)

ROLE: Private, offline-capable LLM runtime for classification and enrichment at scale
OS LAYERS: 06-TECHNOLOGY/models, REGISTRIES (batch repo summarization)
INTEGRATION:
- Use for Tier 3–4 repo batch summaries (cost control vs. cloud API)
- Models: codellama for code repos, llama3.x for prose/README summarization
- Never for fiduciary decisions without human review
- Fallback when Anthropic/OpenAI rate-limited
OUTPUT: Enriched fields in repository_registry_pilot.json

---

## OpenWebUI (Local chat + model router)

ROLE: Human-facing local chat UI and multi-model gateway
OS LAYERS: 06-TECHNOLOGY, 09-DASHBOARDS (informal queries)
INTEGRATION:
- Connect to Ollama backend for local models
- Optional RAG plugin → point at Qdrant/pgvector ingest from REGISTRIES
- Use for operator ad-hoc queries ("which repo has auth?") before agent automation
- NOT the production agent runtime — Cursor agents + Hermes handle that

---

## Hermes Agent (Orchestration coordinator)

ROLE: Event-driven decision layer between inbound signals and task creation
OS LAYERS: 05-AGENTS/orchestration, 04-OPERATIONS (lead routing)
INTEGRATION (per ODYSSEUS-HERMES-ORCHESTRATION-WEEK-1):
  Apify webhook → Hermes (score/classify) → Odysseus workspace → ClickUp + Slack + Supabase
- Implements ROUTING_ENGINE rules for inbound_lead type
- Subject to ESCALATION_POLICY L3+ when confidence < threshold
- Logs all decisions to agent_actions

---

## Odysseus (AI workspace / memory hub)

ROLE: Team workspace + agent coordination + venture context memory
OS LAYERS: 05-AGENTS/memory, 07-KNOWLEDGE
INTEGRATION: Receives Hermes-approved work items; humans approve agent outputs

---

## Neo4j + Qdrant + Postgres (from docker compose)

ROLE: Graph + vector + relational nervous system
OS LAYERS: 08-DATA/graph, 07-KNOWLEDGE/Knowledge Graph
INTEGRATION:
- Neo4j: KNOWLEDGE_GRAPH_MEMORY node/edge types
- Qdrant: RIS Level 4 embeddings from VCC repos only
- Postgres: registries, event log, append-only decision log

---

## AnyOpenAI / multi-provider APIs

ROLE: Model routing abstraction when local inference insufficient
OS LAYERS: 06-TECHNOLOGY/apis
INTEGRATION: Use via cost-aware routing (simple tasks → Ollama, complex → cloud)

---

OUTPUT: Produce STACK-ROLES.md with a table:

| Tool | Layer | Trigger | Inputs | Outputs | Human override |
|------|-------|---------|--------|---------|----------------|

Constraint: No tool gets "default do everything" status. Every integration must name its OS layer and kill switch.
```
