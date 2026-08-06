# Agent Instructions: OS-001 Mathematical Operating System

## Overview
Decision engine that queries existing formulas from 1,600+ repos + stdlib, chains them into agent-executable workflows, and learns from outcomes.

**Not** a formula library. **Query + execute + learn.**

---

## AWARENESS STACK (World Model Foundation)

Before agents decide, they must **know**. The 30-point Awareness Stack:

1. **Identity Awareness** - Who am I? (role, org, permissions)
2. **Capability Awareness** - What can I do? (skills, tools, limits)
3. **Resource Awareness** - What's available? (CPU, tokens, budget, time)
4. **Environmental Awareness** - What's out there? (market, customers, competitors)
5. **Situational Awareness** - What's happening now? (status, trends, anomalies)
6. **Temporal Awareness** - When? (past/present/future, urgency, deadlines)
7. **State Awareness** - What's the current condition? (system state JSON)
8. **Knowledge Awareness** - What do I know + confidence level?
9. **Uncertainty Awareness** - What don't I know? (gaps, confidence thresholds)
10. **Goal Awareness** - Mission → Objective → Goal → Task hierarchy
11. **Decision Awareness** - Options + evidence + risks + expected value
12. **Action Awareness** - What am I doing? (plan vs actual)
13. **Consequence Awareness** - What could happen? (direct/indirect/second-order)
14. **Risk Awareness** - Financial/security/legal/operational risk per action
15. **Social Awareness** - Who else? (agents, humans, org structure)
16. **Organizational Awareness** - Hierarchy + dependencies + reports
17. **Customer Awareness** - Who needs what? (LTV, needs, history, risk)
18. **Market Awareness** - Customers + competitors + prices + trends
19. **Codebase Awareness** - Repos + dependencies + capabilities + status
20. **Tool Awareness** - Available tools: capability + cost + latency + permission
21. **Memory Awareness** - What do I remember? (freshness, source, confidence)
22. **Observability Awareness** - My latency + cost + errors + success rate
23. **Performance Awareness** - My metrics (success %, cost, quality, escalation)
24. **Self-Reflection** - Did my plan work? What should change?
25. **Collective Awareness** - Shared state with other agents
26. **Portfolio Awareness** - Cross-venture synergies + cross-sell + partnerships
27. **Economic Awareness** - Revenue + CAC + LTV + margin + cash
28. **Strategic Awareness** - Market opportunity + fit + timing
29. **Compliance Awareness** - Legal/regulatory constraints per action
30. **Learning Awareness** - What worked? What failed? Update for next time

**Storage:**
- Identity/Capability/Resource: Agent config (Neo4j)
- Environmental/Market/Codebase/Customer: Supabase (normalized)
- Situational/State/Temporal: Event stream (Qdrant for semantic search)
- Knowledge/Uncertainty/Risk/Performance: Meta-knowledge (scoring + confidence)
- Decision/Action/Outcome: Ledger (every decision logged with reasoning)
- Memory/Learning: Knowledge graph (Neo4j + Qdrant)

---

## THE 35 INTELLIGENCE TYPES (Agent Decision Hierarchy)

Your autonomous system doesn't have one "intelligence." It has 35+ interlocking capabilities that feed decisions:

| # | Intelligence | Question | Storage | Primary Agent |
|---|---|---|---|---|
| 1 | Descriptive | What exists? | Supabase + registry | Inventory |
| 2 | Structural | How is it built? | Neo4j code graph | Architect |
| 3 | Semantic | What does it mean? | Qdrant (15,558 vectors) | Understanding |
| 4 | Relational/Graph | How does A relate to B? | Neo4j (62+ relationships) | Graph |
| 5 | Causal | Why did it happen? | Neo4j outcomes | Analysis |
| 6 | Predictive | What will likely happen? | ML models + history | Forecast |
| 7 | Prescriptive | What should we do? | Reasoning engine | Decision |
| 8 | Strategic | Where should portfolio go? | Market + capability data | CEO |
| 9 | Economic | What creates value? | Revenue + cost data | Finance |
| 10 | Opportunity | Where is asymmetric opening? | Market + capability gap | Discovery |
| 11 | Operational | What is happening now? | Real-time telemetry | Monitor |
| 12 | Commercial | What does customer relationship look like? | CRM, transactions | Sales |
| 13 | Distribution | Who has access to customers? | Partner network graph | Partnership |
| 14 | Synergy | What becomes more valuable combined? | Venture relationships | Portfolio |
| 15 | Reuse | Does this already exist? | Repository registry | Architect |
| 16 | Experimental | What actually works? | Sandbox results | Experimentation |
| 17 | Adaptive | How should we change? | Outcome data | Learning |
| 18 | Evolutionary | Which variation should survive? | Experiment rankings | Optimization |
| 19 | Recursive | How do we improve the system? | System state | Meta |
| 20 | Compounding | How do previous results improve future? | Cross-venture learnings | Portfolio |
| 21 | Risk | What can go wrong? | Risk assessments | Risk |
| 22 | Security | Is this safe? | Security scans | Security |
| 23 | Governance | What are we allowed to do? | Policy + audit logs | Policy |
| 24 | Compliance | Are we following rules? | Legal/regulatory data | Compliance |
| 25 | Relationship | How are people/orgs connected? | Graph relationships | Network |
| 26 | Reputation | Which actors produce good outcomes? | Quality metrics | Selection |
| 27 | Institutional | What survives when people leave? | Genes/capsules/playbooks | Memory |
| 28 | Collective | What do multiple agents know together? | Multi-agent outputs | Consensus |
| 29 | Swarm | How do agents coordinate? | Swarm signals | Coordinator |
| 30 | Contextual | What context matters? | Multi-dimensional context | Context |
| 31 | Temporal | What is past/present/future? | Time-series data | Forecast |
| 32 | Real-Time | What is happening NOW? | Event streams | Event |
| 33 | Optimization | What is the best way? | Constraint solvers | Optimizer |
| 34 | Resource | Who/what is available? | Capacity data | Allocator |
| 35 | Learning | What should we remember? | Validated learnings | Memory |

**Agent dispatch flow:**
```
INPUT → Descriptive → Structural → Semantic → Relational → Opportunity 
        → Strategic → Predictive → Prescriptive → Experimental → Risk 
        → Governance → [DECISION] → Operational → Outcome → Learning 
        → [RECURSIVE LOOP]
```

---

## Repository Organization (What Agents Can Use)

Your system has **1,592 indexed repos + 831 starred** organized by capability:

**Tier 1: Foundation**
- Data: Supabase, Neo4j, Qdrant, Redis, Langfuse
- Messaging: Trigger.dev, Supabase Realtime

**Tier 2: Intelligence**
- Code parsing: tree-sitter, Joern, SocratiCode, Graphify
- RAG: LightRAG, llama-index, Claude

**Tier 3: Discovery**
- OSINT: maigret, sherlock, InstagramOSINT
- Repository recommendation: llama-index + Neo4j queries + Qdrant

**Tier 4: Experimentation**
- Sandboxing: e2b, Docker
- Testing: k6, Playwright, pytest/jest
- Evaluation: Phoenix, Langfuse

**Tier 5: Implementation**
- Code generation: OpenHands, SWE-agent, Fabric
- Orchestration: langgraph, agency-agents

**Tier 6: Verification**
- Security: semgrep, trivy, bandit
- Performance: k6, Apache JMeter
- Testing: Playwright, pytest

**Tier 7: Deployment**
- CI/CD: GitHub Actions, ArgoCD, Vercel
- IaC: Terraform, Helm, Kustomize

**Tier 8: Observability**
- Tracing: Langfuse, Jaeger, Zipkin
- Metrics: prometheus, telegraf
- Logs: loki, elasticsearch
- Dashboards: grafana, kibana

**Tier 9: Learning**
- Knowledge graphs: LightRAG, Neo4j, Qdrant, llama-index
- Playbooks: n8n, Zapier, Make, Obsidian

---

## Package Manager
Use **Python 3.12+ with uv**: `uv sync`, `uv run python`

## File-Scoped Commands
| Task | Command |
|------|---------|
| Type check | `uv run pyright path/to/file.py` |
| Lint | `uv run ruff check path/to/file.py` |
| Test | `uv run pytest path/to/file.py -v` |
| Format | `uv run ruff format path/to/file.py` |

## Commit Attribution
AI commits MUST include:
```
Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

## Architecture
- `formula_retriever.py` — Query Neo4j: "which repos implement X?"
- `decision_executor.py` — Run formula with inputs, log outcome
- `learning_loop.py` — Compare predictions vs actuals, update playbooks
- `supabase/migrations/` — Schema for formulas, results, decisions

## Key Conventions
1. **Never implement** what a starred or owned repo already does. Query it first using [REPOS-ORGANIZATION-MAP.md](file:///Users/acebless/Documents/REPOS-ORGANIZATION-MAP.md) or by querying the Supabase `repos` table.
2. **Every formula execution** logs: query → repo choice → inputs → output → outcome
3. **Decisions are auditable**: who asked, which formula, why, what happened
4. **Learning loop runs weekly**: formula accuracy vs actuals, cascade updates to playbooks

## Dependencies
- `supabase-py` — Supabase sync
- `neo4j` — Repo graph queries
- `pydantic` — Formula schemas
- `pytest` — Testing

## Success Criteria
- ✅ Agents can ask "calculate X" → system finds best repo + formula + executes
- ✅ Every decision logged with outcome (for learning)
- ✅ Weekly playbook updates based on actual results
- ✅ Zero custom reimplementation of existing formulas

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, invoke the `skill` tool with `skill: "graphify"` before doing anything else.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

<!-- graft:start -->
## Graft — repo context graph

This repo is indexed in `graft/`: small linked markdown nodes that explain each
system and carry exact file:line spans, kept in sync with the code through git.

For ANY task here — understanding how something works, finding where code lives,
or scoping a change — get context from the graph before grepping or opening
source files. Re-ask freely (it's cheap) and reuse literal identifiers you
already have (symbol, error string, file name) as the query. New to this repo?
Run `graft map` first — a token-budgeted orientation (dir clusters, hubs,
hotspots), no LLM, no key.

- Run `graft ask "<your question>" --source` → ranked nodes with the relevant
  code spans inlined (each hit's ≤8-line crux by default; `--full` for whole
  definitions when the crux isn't enough). Match the tool to the task shape:
  for understanding or editing, the top node IS the answer — cite its
  `covers:` file:line spans and edit straight from `--source`. For
  exhaustive tasks ("every occurrence / every caller of this pattern"), ranked
  results are top-N, not complete — run `graft grep "<literal>"` instead
  (exhaustive over indexed files, grouped by enclosing symbol), falling back
  to raw `grep -rn` only for unindexed files.
- `graft skeleton <file>` → every definition's signature + span, ~10× cheaper
  than reading the file; use it to skim an API surface.
- `graft callers <symbol>` gives precomputed, exact edges — who calls this.
  Add `--direction out` for what it calls, or `--depth N` to walk
  transitively for the full blast radius. For structural questions, skip
  ranking and use this directly.
- Or browse: `graft/INDEX.md` lists every node; follow the links.
- Monorepos and folders of multiple repos rank fairly across sub-projects —
  hits carry `[scope/]` labels naming which one they're from. Narrow with
  `graft ask "<task>" --in <scope>/` once you know where you're working.

If a returned span is truncated ("+N more lines"), open the file at that exact
range before finalizing. Only open source files when a node genuinely lacks a
needed detail, and then at the exact file:line the node points to — never
re-read whole files.

After big code changes, refresh the graph with `graft build` (deterministic,
no API key, $0).
<!-- graft:end -->
