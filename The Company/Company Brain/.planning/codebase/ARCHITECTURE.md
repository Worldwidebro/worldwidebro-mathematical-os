<!-- refreshed: 2026-09-05 -->
# Architecture

**Analysis Date:** 2026-09-05

## System Overview

The Company Brain is a complete organizational intelligence system organized as a **22-stage cognitive pipeline** flowing through **9 cognitive fabrics**, mapped onto **68 organizational domains** (numbered 00-50 original + 51-67 extension layers), with approximately **~500 control points** orchestrating execution.

```
WORLD (external reality)
  ↓
OBSERVATION → DATA → INFORMATION → KNOWLEDGE → MEMORY
  ↓
RETRIEVAL → CONTEXT → THINKING → THOUGHT → IDEA → VISION
  ↓
INTENTION → GOAL → STRATEGY → PLAN → WORK → EXECUTION
  ↓
RESULT → OUTCOME → LEARNING → EVOLUTION
  ↓
WORLD (changed)
```

This pipeline is realized across 9 cognitive fabrics that stack vertically:

```
┌─────────────────────────────────────────────────┐
│  LEARNING FABRIC (feedback, improvement)        │
│  `44-LEARNING, 45-EVOLUTION, 46-GOVERNANCE`     │
└────────────────┬────────────────────────────────┘
                 ↑
┌────────────────┴────────────────────────────────┐
│  EXECUTION FABRIC (agents, tasks, jobs)         │
│  `22-EXECUTION, 29-OPERATIONS, 49-SYSTEM`       │
└────────────────┬────────────────────────────────┘
                 ↑
┌────────────────┴────────────────────────────────┐
│  AGENT FABRIC (models, routing, inference)      │
│  `16-AGENTS, 17-MODELS, 18-TOOLS, 59-MCP`       │
└────────────────┬────────────────────────────────┘
                 ↑
┌────────────────┴────────────────────────────────┐
│  DECISION FABRIC (evaluation, scoring)          │
│  `20-DECISIONS, 21-POLICY, 24-FINANCE`          │
└────────────────┬────────────────────────────────┘
                 ↑
┌────────────────┴────────────────────────────────┐
│  DISCOVERY FABRIC (search, exploration)         │
│  `38-OPPORTUNITIES, 39-EXPERIMENTS`             │
└────────────────┬────────────────────────────────┘
                 ↑
┌────────────────┴────────────────────────────────┐
│  COGNITION FABRIC (reasoning, ideation)         │
│  `19-ORCHESTRATION, 55-LOOP-ENGINEERING`        │
└────────────────┬────────────────────────────────┘
                 ↑
┌────────────────┴────────────────────────────────┐
│  KNOWLEDGE FABRIC (concepts, models, rules)     │
│  `07-ONTOLOGY, 08-KNOWLEDGE-GRAPH, 09-KNOWLEDGE`│
└────────────────┬────────────────────────────────┘
                 ↑
┌────────────────┴────────────────────────────────┐
│  INFORMATION FABRIC (data, facts, classification)
│  `02-SOURCES, 03-INGESTION, 04-DATA, 05-METADATA`
└────────────────┬────────────────────────────────┘
                 ↑
┌────────────────┴────────────────────────────────┐
│  REALITY FABRIC (world events, observations)    │
│  `00-CONSTITUTION, 01-IDENTITY, 02-SOURCES`     │
└─────────────────────────────────────────────────┘
```

## Component Responsibilities

| Domain | Responsibility | Layer Position |
|--------|----------------|-----------------|
| `00-CONSTITUTION` | Mission, principles, governance, founding documents | Reality Fabric |
| `01-IDENTITY` | Company structure, holdings, subsidiaries, brands | Reality Fabric |
| `02-SOURCES` | Data sources, APIs, integrations, connectors | Information Fabric |
| `03-INGESTION` | Pipelines, ETL, import processes, data loading | Information Fabric |
| `04-DATA` | Raw normalized, canonical data, data lakes | Information Fabric |
| `05-METADATA` | Schemas, lineage, provenance, data quality, governance | Information Fabric |
| `06-ENTITY-RESOLUTION` | Deduplication, entity linking, reference data | Information Fabric |
| `07-ONTOLOGY` | Conceptual models, vocabularies, taxonomies | Knowledge Fabric |
| `08-KNOWLEDGE-GRAPH` | Neo4j relationships, nodes, edges, analytics | Knowledge Fabric |
| `09-KNOWLEDGE` | Policies, procedures, rules, research, IP | Knowledge Fabric |
| `10-MEMORY` | Episodic, semantic, procedural memory storage | Knowledge Fabric |
| `11-INDEXING` | Full-text, vector, semantic indexes (Qdrant) | Cognition Fabric |
| `12-CONTEXT` | Task context, working memory, retrieved context | Cognition Fabric |
| `13-REPOSITORIES` | Code ownership, repository metadata, quality | Knowledge Fabric |
| `14-CAPABILITIES` | Capability registry, implementations, solutions | Cognition Fabric |
| `15-SKILLS` | Procedure library, instructions, examples | Cognition Fabric |
| `16-AGENTS` | Agent registry, roles, permissions, orchestration | Agent Fabric |
| `17-MODELS` | Model registry, performance, costs, routing | Agent Fabric |
| `18-TOOLS` | Tool/API registry, MCP servers, integrations | Agent Fabric |
| `19-ORCHESTRATION` | Router, planner, scheduler, workflow control | Cognition Fabric |
| `20-DECISIONS` | Decision requests, recommendations, approvals | Decision Fabric |
| `21-POLICY` | Authority, permissions, escalation, rules | Decision Fabric |
| `22-EXECUTION` | Jobs, tasks, transactions, agent runs | Execution Fabric |
| `23-VENTURES` | Venture registry, operations, metrics | (Cross-cutting) |
| `24-FINANCE` | Accounting, budgets, forecasting, costs | Decision Fabric |
| `25-SALES` | Leads, prospects, pipeline, deals | (Cross-cutting) |
| `26-MARKETING` | Campaigns, analytics, attribution, content | (Cross-cutting) |
| `27-CUSTOMERS` | Profiles, support, feedback, satisfaction | (Cross-cutting) |
| `28-PRODUCT` | Strategy, roadmap, releases, features | (Cross-cutting) |
| `29-OPERATIONS` | Processes, SOPs, logistics, workflow | Execution Fabric |
| `30-HR` | Workforce, recruiting, training, culture | (Cross-cutting) |
| `31-LEGAL` | Contracts, IP, compliance, risk | Decision Fabric |
| `32-SECURITY` | Identity, access, vulnerabilities, hardening | Decision Fabric |
| `33-COMPLIANCE` | Regulatory, certifications, controls, audit | Decision Fabric |
| `34-RISK` | Enterprise, financial, operational risk | Decision Fabric |
| `35-ASSETS` | Real estate, equipment, IP, resources | Decision Fabric |
| `36-PARTNERS` | Investors, vendors, partners, alliances | (Cross-cutting) |
| `37-RESEARCH` | Market research, trend analysis, discovery | Discovery Fabric |
| `38-OPPORTUNITIES` | Identified opportunities, market gaps | Discovery Fabric |
| `39-EXPERIMENTS` | Experimentation, A/B testing, validation | Discovery Fabric |
| `40-METRICS` | KPIs, SLIs, SLOs, measurement, tracking | Decision Fabric |
| `41-OBSERVABILITY` | Monitoring, logging, tracing, telemetry | Learning Fabric |
| `42-EVALUATION` | Assessment, scoring, quality metrics | Learning Fabric |
| `43-OUTCOMES` | Recorded outcomes, results, achievements | Learning Fabric |
| `44-LEARNING` | Lessons extracted, knowledge synthesis | Learning Fabric |
| `45-EVOLUTION` | Optimization, improvement, adaptation | Learning Fabric |
| `46-GOVERNANCE` | Change control, audits, accountability | Learning Fabric |
| `47-DOCUMENTS` | Long-form documentation, guides, manuals | (Cross-cutting) |
| `48-AUTOMATION` | Workflow automation, RPA, scheduled tasks | Execution Fabric |
| `49-SYSTEM` | System architecture, infrastructure status | (Infrastructure) |
| `50-MASTER-CONTROL` | Current state, objectives, blockers, health | (Control Plane) |
| `51-CONSTRUCTION` | Domain-specific: construction industry | (Extension, specialized) |
| `52-PEOPLE` | Domain-specific: workforce, talent, individuals | (Extension, specialized) |
| `53-TEAMS` | Domain-specific: team structures, collaboration | (Extension, specialized) |
| `54-FINANCIAL` | Domain-specific: financial services, instruments | (Extension, specialized) |
| `55-LOOP-ENGINEERING` | Loop execution patterns, autonomy levels (L1/L2/L3) | Cognition/Execution |
| `56-ENGINEERING` | Technical infrastructure, deployment, DevOps | (Infrastructure) |
| `57-CODE-INTELLIGENCE` | Code graphs, symbol analysis, repository intelligence | Cognition Fabric |
| `58-LOGISTICS` | Supply chain, routing, distribution | Execution Fabric |
| `59-MCP` | MCP server registry, tools, capabilities | Agent Fabric |
| `60-APIS` | API registry, endpoints, contracts, versions | Agent Fabric |
| `61-KNOWLEDGE-SOURCES` | External knowledge, facts, research sources | Information Fabric |
| `62-TECHNOLOGY` | Technology stack, tools, frameworks, libraries | Agent Fabric |
| `63-CHANGE-MANAGEMENT` | Change requests, impact analysis, rollback | Learning Fabric |
| `64-RELATIONSHIPS` | Entity relationships, connections, networks | Knowledge Fabric |
| `65-SYNERGIES` | Cross-venture synergies, partnerships, leverage | (Cross-cutting) |
| `66-OPPORTUNITIES-ALT` | Alternative opportunities, scenarios | Discovery Fabric |
| `67-EVOLUTION-ALT` | Alternative evolution paths, strategies | Learning Fabric |

## Pattern Overview

**Overall:** Multi-layered cognitive pipeline architecture

**Key Characteristics:**
- **22-stage pipeline** ensures information is progressively transformed (data → information → knowledge → decisions → execution → outcomes → learning)
- **9 fabric layers** implement separation of concerns (reality observation, information processing, knowledge synthesis, reasoning, decision-making, agent execution, and learning)
- **Bidirectional flow** with feedback loops: execution produces outcomes which flow back through learning to evolve knowledge and strategy
- **Abstraction inversions** at key points: capabilities abstract agent work; skills abstract capability procedures; control points abstract organizational decisions
- **Domain isolation** via 68 numbered folders; cross-cutting concerns (ventures, products, customers) appear in multiple fabrics but maintain single sources of truth via registries

## Layers

**22-Stage Cognitive Pipeline:**

The 22 stages are organized into logical groups within the 9 fabrics:

1. **Observation Group** (stages 1-2, Reality Fabric):
   - Stage 1: WORLD — External reality
   - Stage 2: OBSERVATION — Events detected/captured

2. **Data Group** (stages 3-4, Information Fabric):
   - Stage 3: DATA — Raw data ingested
   - Stage 4: INFORMATION — Cleaned, classified facts

3. **Knowledge Group** (stages 5-6, Knowledge Fabric):
   - Stage 5: KNOWLEDGE — Concepts, rules, models
   - Stage 6: MEMORY — Consolidated storage for retrieval

4. **Retrieval & Context Group** (stages 7-8, Cognition Fabric):
   - Stage 7: RETRIEVAL — Indexing and search mechanisms
   - Stage 8: CONTEXT — Assembled task-relevant knowledge

5. **Reasoning Group** (stages 9-10, Cognition Fabric):
   - Stage 9: THINKING — Mental processes, analysis
   - Stage 10: THOUGHT — Structured conclusions

6. **Ideation Group** (stages 11-12, Cognition Fabric):
   - Stage 11: IDEA — Conceptual solutions, insights
   - Stage 12: VISION — Desired future state

7. **Planning Group** (stages 13-15, Decision & Cognition Fabrics):
   - Stage 13: INTENTION — Will to act, commitment
   - Stage 14: GOAL — Objective, target outcome
   - Stage 15: STRATEGY — High-level approach

8. **Execution Planning Group** (stages 16-17, Execution Fabric):
   - Stage 16: PLAN — Detailed task breakdown
   - Stage 17: WORK — Specific tasks/jobs

9. **Execution & Outcomes Group** (stages 18-20, Execution & Learning Fabrics):
   - Stage 18: EXECUTION — Actual task performance
   - Stage 19: RESULT — Immediate output/artifact
   - Stage 20: OUTCOME — Evaluated result against goal

10. **Learning Loop** (stages 21-22, Learning Fabric):
    - Stage 21: LEARNING — Lessons extracted, patterns identified
    - Stage 22: EVOLUTION — Strategy/knowledge adaptation

## Data Flow

### Primary Request Path

1. **Observation** (`00-CONSTITUTION` → `02-SOURCES`) — External world event or data source signals Company Brain
2. **Ingestion** (`03-INGESTION`) — Pipeline ingests raw data
3. **Data Storage** (`04-DATA`, `05-METADATA`) — Canonical data stored with lineage
4. **Entity Resolution** (`06-ENTITY-RESOLUTION`) — Deduplication and linking
5. **Knowledge Graph** (`08-KNOWLEDGE-GRAPH`, `07-ONTOLOGY`) — Relationships and concepts established
6. **Indexing** (`11-INDEXING`) — Full-text, vector, semantic indexes populated (Neo4j, Qdrant)
7. **Capability Routing** (`14-CAPABILITIES`, `19-ORCHESTRATION`) — Which capability should execute?
8. **Agent Selection** (`16-AGENTS`, `17-MODELS`, `18-TOOLS`) — Which agent? Which model? Which tools?
9. **Context Assembly** (`12-CONTEXT`, `10-MEMORY`) — Gather relevant facts, memory, policies
10. **Execution** (`22-EXECUTION`) — Agent performs work (task/job/transaction)
11. **Outcome Capture** (`43-OUTCOMES`) — Result recorded
12. **Evaluation** (`42-EVALUATION`, `40-METRICS`) — Measure against KPIs
13. **Learning** (`44-LEARNING`) — Extract lessons, update policies, improve models
14. **Evolution** (`45-EVOLUTION`) — Improve strategy, optimize capabilities

### Secondary Flows

**Decision Flow:** Request (`20-DECISIONS`) → Policy evaluation (`21-POLICY`, `31-LEGAL`, `32-SECURITY`) → Authorization (`21-POLICY`) → Approval/Denial

**Financial Flow:** Cost estimation (`24-FINANCE`) → Budget check → Allocation decision → Execution tracking → Outcome reporting (`43-OUTCOMES`) → Financial close (`24-FINANCE`)

**Venture Lifecycle:** Registry entry (`23-VENTURES`) → Capability mapping (`14-CAPABILITIES`) → Execution (`22-EXECUTION`) → Metrics tracking (`40-METRICS`) → Outcome recording (`43-OUTCOMES`)

**State Management:**
- **Working memory** (current task context): `12-CONTEXT`
- **Episodic memory** (event history): `10-MEMORY`, `22-EXECUTION`
- **Semantic memory** (facts, concepts): `08-KNOWLEDGE-GRAPH`, `09-KNOWLEDGE`
- **Procedural memory** (skills, policies): `15-SKILLS`, `21-POLICY`
- **Persistent state** (database): Neo4j (`08-KNOWLEDGE-GRAPH`), Qdrant (`11-INDEXING`), PostgreSQL (`49-SYSTEM`)

## Key Abstractions

**Capability:**
- Purpose: Represents "what the organization can do" independent of implementation
- Examples: `14-CAPABILITIES/solutions/` (300+ capability implementations)
- Pattern: Capability → Implemented by Tool/Agent → Used by Person/Team → Produces Outcome

**Skill:**
- Purpose: Encodes "how to do X" (procedure-oriented, step-by-step)
- Examples: `15-SKILLS/` (296+ slash commands indexed by workflow phase)
- Pattern: Procedure with examples, prerequisites, success criteria

**Agent:**
- Purpose: Autonomous entity (human or AI) that executes work using capabilities/skills
- Examples: `16-AGENTS/` (26+ routing agents, specialized personas)
- Pattern: Agent has role, permissions, tools, knowledge, autonomy level (L1/L2/L3)

**Control Point (CBP):**
- Purpose: Decision/permission point in organizational flow
- Examples: ~500 control points (CBP-000001 to CBP-000500) mapped to domains and layers
- Pattern: Layer + Domain + Decision Type → Control Point → Implemented via Agent/Tool/Policy

**Model:**
- Purpose: AI/ML model choice: which LLM, which parameters, which cost profile
- Examples: `17-MODELS/` (registry of Claude, Qwen, local models)
- Pattern: Model → Provider (Claude API, exo, ollama) → Router (LiteLLM, OmniRoute)

**Tool:**
- Purpose: External API/MCP endpoint/executable script
- Examples: `18-TOOLS/`, `59-MCP/`, `60-APIS/` (16+ registered tools)
- Pattern: Tool → SDK/Client → Agent invocation → Result

## Entry Points

**Knowledge Entry:**
- Location: `02-SOURCES/` (data ingestion starts here)
- Triggers: API webhook, file upload, manual entry, scheduled import
- Responsibilities: Validate source format, route to appropriate ingestion pipeline (`03-INGESTION`)

**Query Entry:**
- Location: `11-INDEXING/` (vector/semantic/full-text search)
- Triggers: Agent query, user search, capability routing need
- Responsibilities: Find relevant knowledge, rank by relevance, assemble into context

**Execution Entry:**
- Location: `22-EXECUTION/` (job/task scheduling)
- Triggers: Decision approved, capability needed, loop triggered
- Responsibilities: Create task, assign to agent, monitor, capture outcome

**Decision Entry:**
- Location: `20-DECISIONS/` (decision request)
- Triggers: Policy escalation, threshold exceeded, human request
- Responsibilities: Evaluate criteria, check authorization, recommend or approve

**Learning Entry:**
- Location: `43-OUTCOMES/` (outcome recording)
- Triggers: Task completion, project milestone, quarterly review
- Responsibilities: Capture result, evaluate against goal, extract lesson

## Architectural Constraints

- **Unidirectional data flow** (with feedback loops): Reality → Observation → Data → Information → Knowledge → Cognition → Decision → Execution → Outcomes → Learning (→ evolution of Knowledge)
- **Neo4j as single source of truth for relationships**: All entity-to-entity connections stored in Neo4j; registries are secondary views
- **Qdrant for semantic search**: Vector embeddings of all knowledge, procedures, capabilities; powers "find similar" across organizational domains
- **PostgreSQL for transactional state**: Execution tracking, outcomes, metrics; supports ACID guarantees
- **Local-first infrastructure**: Mac Studio (100.87.214.70) runs Neo4j, Qdrant, Postgres, LiteLLM, Langfuse via Docker
- **No global state in agents**: Each agent instance fetches context at start; state lives in databases only
- **Strict authorization boundary at `21-POLICY`**: Execution (`22-`) never proceeds without policy check, even for internal agents
- **Loop autonomy levels**: L1 (report-only, human confirms), L2 (agent executes with oversight), L3 (unattended autonomous execution after verification)

## Anti-Patterns

### Bypassing Entity Resolution

**What happens:** Data ingested directly to `04-DATA` without deduplication against `06-ENTITY-RESOLUTION`, creating duplicate entities in Neo4j

**Why it's wrong:** Neo4j relationships become ambiguous; queries for "Company X" return 3 nodes instead of 1; analysis produces inconsistent results

**Do this instead:** Every source ingestion to `03-INGESTION` must call entity resolution at `06-ENTITY-RESOLUTION` before graph insertion. See: `_PIPELINES/ingestion/entity-resolution-step.py`

### Hardcoding Agent Selection

**What happens:** Capability directly calls Agent X instead of routing through `19-ORCHESTRATION`/`14-CAPABILITIES`, making it impossible to swap agents or models

**Why it's wrong:** Tightly couples capability to specific agent implementation; prevents parallel execution, cost optimization, or failover

**Do this instead:** Capability definition references agent role (not ID). Orchestrator looks up agent by role at runtime via `16-AGENTS`. See: `14-CAPABILITIES/solutions/` pattern

### Skipping Knowledge Graph for "Faster" Direct Queries

**What happens:** Agent queries PostgreSQL directly instead of using Neo4j for relationship traversal

**Why it's wrong:** Misses organizational context; cannot discover "what this decision affects"; analytics become isolated; auditing breaks

**Do this instead:** Always route complex queries through `08-KNOWLEDGE-GRAPH` first. Use Cypher for multi-hop relationships. Fall back to SQL only for time-series/metrics data. See: `_PIPELINES/retrieval/context-compiler.py`

## Error Handling

**Strategy:** Tri-level escalation with automatic retry + human escalation + rollback

**Patterns:**
- **Level 1 (Automatic Recovery)**: Retry with exponential backoff (tasks, API calls); timeout after 3 attempts; captured in execution logs
- **Level 2 (Policy Escalation)**: If L1 fails, check `21-POLICY` for escalation path; attempt mitigation via fallback agent/model/capability
- **Level 3 (Human Escalation)**: If L2 exhausted, create `20-DECISIONS` record with full context; notify humans; wait for decision
- **Rollback**: All tasks under `22-EXECUTION` are transactional; failed execution rolls back writes to Neo4j/Qdrant, maintains PostgreSQL audit log

## Cross-Cutting Concerns

**Logging:** Structured JSON logs via Python `logging` module to PostgreSQL `execution_logs` table; indexed by task_id, agent_id, timestamp; queryable via Grafana (`41-OBSERVABILITY`)

**Validation:** Schema validation on ingestion (`03-INGESTION`), on entity resolution (`06-ENTITY-RESOLUTION`), on knowledge graph insertion (`08-KNOWLEDGE-GRAPH`); schemas stored in `05-METADATA`

**Authentication:** Agent identity via `16-AGENTS` record + assigned permissions via `21-POLICY`; policy engine enforces at `20-DECISIONS` / `22-EXECUTION` boundary

**Audit Trail:** All decisions, executions, outcomes recorded in PostgreSQL; queryable for compliance audits; linked to Neo4j via decision ID

---

*Architecture analysis: 2026-09-05*
