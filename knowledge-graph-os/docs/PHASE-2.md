# Knowledge Graph OS — Phase 2 Architecture

**Tags:** infrastructure, phase-2, graph-engineering  
**Status:** Ready for Round 3 Wiring  
**Updated:** 2026-07-30

---

## Overview

Knowledge Graph OS is a Neo4j + Qdrant intelligence layer that powers agent routing, capability matching, and semantic search across the Venture Nation system.

**Core Components:**
1. **Neo4j Schema** — graph database with 9 node types, 8 relationships, optimized indexes
2. **GraphRouter** — intelligent agent-to-task matching with weighted scoring
3. **Qdrant Config** — vector collections for semantic embeddings (agent, capability, task)
4. **Ingestion Pipeline** — Supabase → Neo4j/Qdrant sync with dedup
5. **Entity Resolver** — conflict resolution and name-based deduplication

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    Knowledge Graph OS                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐         ┌──────────────┐     ┌────────────┐  │
│  │  Supabase    │────────→│   Ingestion  │────→│ Neo4j DB   │  │
│  │ (agents,     │         │  Pipeline    │     │ (9 types,  │  │
│  │  capabilities│         └──────────────┘     │  8 rels)   │  │
│  │  ventures)   │                              └────────────┘  │
│  └──────────────┘                                     ↓         │
│                                                 ┌──────────────┐│
│                                                 │ GraphRouter  ││
│                                                 │ (scoring &   ││
│                                                 │  matching)   ││
│                                                 └──────────────┘│
│                            ↓                                    │
│                    ┌──────────────────┐                         │
│                    │   Qdrant DB      │                         │
│                    │ (embeddings:     │                         │
│                    │  agents,         │                         │
│                    │  capabilities,   │                         │
│                    │  tasks)          │                         │
│                    └──────────────────┘                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
         ↓                                              ↓
    ┌─────────────────────────────────────────────────────────┐
    │      Agent Platform OS / Dispatcher                      │
    │   (uses routing output + vector search for assignments)  │
    └─────────────────────────────────────────────────────────┘
```

---

## Neo4j Schema

### Node Types (9)

| Label | Properties | Purpose |
|-------|------------|---------|
| **Agent** | id, name, type, org_id, availability, cost_per_hour, success_rate, status, created_at, updated_at | Autonomous actors (AI, human, system) |
| **Task** | id, name, status, priority, venture_id, created_at, updated_at, due_at | Units of work to be routed |
| **Capability** | id, name, category, description, cost_estimate, success_baseline, complexity | Skills agents possess |
| **Tool** | id, name, service, endpoint, rate_limit_per_hour, cost_per_call, status | External services & APIs |
| **Workflow** | id, name, type, status, venture_id, success_rate, avg_duration_mins | Orchestration patterns |
| **Step** | id, step_number, name, estimated_duration_mins, required_capabilities[], depends_on_step_ids[] | Workflow tasks |
| **Metric** | id, name, unit, venture_id, metric_type, current_value, target_value, measured_at | KPI tracking |
| **Venture** | id, name, sector, stage, readiness, revenue_monthly, created_at | Business initiatives |
| **OPCO** | id, name, type, parent_id, headcount, budget_monthly | Organizational units |

### Relationship Types (8)

| Relationship | From → To | Properties | Meaning |
|---|---|---|---|
| **HAS_CAPABILITY** | Agent → Capability | proficiency (0-1), last_used_at, num_uses | Agent has this skill |
| **REQUIRES_CAPABILITY** | Task → Capability | criticality (0-1), optional | Task needs this skill |
| **USES** | Agent/Task → Tool | call_count, last_called_at, cost_total | Consumes external service |
| **ASSIGNED_TO** | Task → Agent | assigned_at, started_at, completed_at, success, error_msg | Task dispatched to agent |
| **EXECUTED** | Task → Workflow | step_number, duration_secs, cost_incurred, success | Task ran in workflow |
| **PART_OF** | Step → Workflow | — | Step belongs to workflow |
| **TRACKS** | Metric → Venture | — | Metric measures venture |
| **PART_OF_ORG** | Agent/Venture → OPCO | — | Entity belongs to org |

### Indexes & Constraints

**Unique Constraints:**
- Agent(id), Task(id), Capability(id), Tool(id), Workflow(id), Step(id), Metric(id), Venture(id), OPCO(id)

**Performance Indexes:**
- Agent(org_id, status) — composite for org-scoped queries
- Task(status, venture_id) — multi-level filtering
- Capability(name, category) — matching
- Tool(service, status) — availability checks
- Workflow(venture_id), Venture(sector, stage)

---

## GraphRouter Algorithm

**Goal:** Find the best agent for a task by matching required capabilities + scoring.

**Input:**
```typescript
task_id: string
required_capabilities: string[]
preferred_org_id?: string
max_cost_per_hour?: number
```

**Scoring Formula:**

```
final_score = (
  weighted_success * 0.40 +
  org_proximity * 0.20 +
  cost_score * 0.20 +
  load_factor * 0.20
)
```

- **weighted_success (40%)** — agent's historical success_rate
- **org_proximity (20%)** — same org=1.0, different=0.3, none=0.5
- **cost_score (20%)** — inverse of cost/max_cost (lower cost = higher score)
- **load_factor (20%)** — agent availability (workload inverse)

**Capability Matching:**
- Agents must have ≥80% of required capabilities
- Capability gap logged in metadata

**Output:**
```typescript
{
  agent_id: string
  agent_name: string
  final_score: number (0-1)
  confidence: number (based on success_rate)
  scores: {
    weighted_success: number
    org_proximity: number
    cost_score: number
    load_factor: number
  }
  metadata: {
    matches_required_capabilities: boolean
    capability_gap_count: number
  }
}
```

---

## Qdrant Vector Collections

### Collections (3)

| Collection | Vector Size | Distance | Use Case |
|---|---|---|---|
| **agent_embeddings** | 384 | cosine | Semantic agent search (find similar agents) |
| **capability_embeddings** | 384 | cosine | Find related capabilities |
| **task_embeddings** | 384 | cosine | Match task descriptions to agents |

### Payload Schema Example (agent_embeddings)

```json
{
  "id": "agent-001",
  "name": "Code Review Agent",
  "type": "ai",
  "org_id": "engineering",
  "capabilities": ["code-review", "pr-analysis", "testing"],
  "availability": 0.95,
  "success_rate": 0.87,
  "cost_per_hour": 0.50,
  "embedding_model": "nomic-embed-1.5",
  "created_at": "2026-07-01T10:00:00Z",
  "updated_at": "2026-07-30T15:30:00Z"
}
```

**HNSW Index Config:**
- m = 16 (connections per node)
- ef_construct = 200 (index-time search width)
- full_scan_threshold = 10000 (switch to brute-force after this many vectors)

---

## Ingestion Pipeline Flow

**Phase 1: Fetch from Supabase**
1. Read `agents` table → create Agent nodes
2. Read `capabilities` table → create Capability nodes
3. Read `ventures` table → create Venture nodes

**Phase 2: Link Entities**
1. Read `agent_capabilities` table → create HAS_CAPABILITY relationships
2. Link ventures to agents by sector/org matching → PART_OF_ORG relationships

**Phase 3: Deduplicate**
1. EntityResolver finds agents/capabilities with same name + org
2. Merge under primary ID (newest), redirect all edges
3. Log conflicts in resolution_log

**Phase 4: Embed to Qdrant** (Round 3)
1. Query all agents/capabilities/tasks from Neo4j
2. Call Anthropic embeddings API for semantic vectors
3. Upsert to Qdrant with full payloads

**Error Handling:**
- Retry logic on Supabase/Neo4j timeouts (3 attempts, exponential backoff)
- Dedup detection prevents duplicate creation
- Resolution log tracks all merges for audit

---

## Entity Resolver

**Deduplication Rules:**

| Type | Match Criteria | Action |
|---|---|---|
| Agent | Same name + org_id + created_at(older) | Keep newer, merge relationships |
| Capability | Same name + category | Consolidate under primary ID |

**Conflict Resolution Precedence:**
1. Keep entity with newest `updated_at`
2. Log all conflicts in audit trail
3. DETACH DELETE old duplicate

---

## Round 3 Wiring Checklist

- [ ] **Database Connection**
  - [ ] Neo4j driver initialized with credentials (URI, user, password)
  - [ ] Qdrant client initialized (host, port, API key)
  - [ ] Supabase client connected (URL, API key)

- [ ] **Schema Deployment**
  - [ ] Run schema.cypher against Neo4j (creates indexes, constraints, node labels)
  - [ ] Verify no existing data conflicts

- [ ] **Ingestion**
  - [ ] IngestionPipeline.ingest() executes all phases
  - [ ] EntityResolver.resolve_agent_duplicates() + resolve_capability_duplicates()
  - [ ] Verify sync stats (agents_synced, capabilities_synced, relationships_created)

- [ ] **Embedding**
  - [ ] Call Anthropic embeddings API for each agent/capability/task
  - [ ] Upsert vectors to Qdrant with payloads
  - [ ] Verify collection health (vector count, avg distance metrics)

- [ ] **Routing Integration**
  - [ ] GraphRouter.find_best_agent() connected to agent-platform-os dispatcher
  - [ ] Test routing with sample tasks (verify scoring + confidence)
  - [ ] Monitor query latency (target <100ms for routing decision)

- [ ] **Health Checks**
  - [ ] EntityResolver.health_check() returns agent/capability counts
  - [ ] GraphRouter.health_check() confirms schema freshness
  - [ ] IngestionPipeline.health_check() verifies Neo4j connectivity

---

## Performance Targets

| Metric | Target | Notes |
|---|---|---|
| Agent routing decision | <100ms | Includes graph query + scoring |
| Capability matching query | <50ms | Leveraging indexes |
| Vector search (Qdrant) | <200ms | For semantic fallback |
| Ingestion (1000 agents) | <30s | Batch writes to Neo4j |
| Duplicate detection | <5s | Scan all agents by name |

---

## Known Limitations & Upgrade Paths

**Current Scope:**
- Single Neo4j instance (no clustering)
- In-memory Qdrant (no persistence)
- Synchronous ingestion (no streaming)

**ponytail notes:**
- Global Neo4j lock on ingestion → per-org locks if throughput matters
- Capability matching uses 80% threshold (heuristic) → ML-based matching if accuracy issues
- Vector search is semantic fallback → move to hybrid (BM25 + vector) if full-text matters

---

## Integration Points

### Agent Platform OS Dispatcher
```typescript
import { GraphRouter } from '@knowledge-graph-os/neo4j-routing';

const router = new GraphRouter(uri, user, password);
const best_agent = await router.find_best_agent(
  task_id,
  ['code-review', 'testing'],
  'engineering', // preferred_org
  50 // max_cost_per_hour
);
```

### Supabase Sync Triggers
- Whenever `agents` table changes → re-ingest agent nodes
- Whenever `capabilities` table changes → update capability nodes + rebuild embeddings
- Ingestion can run on-demand via CLI or scheduled job

---

## Monitoring & Alerts

**Key Metrics:**
- Neo4j graph health (node/relationship count, orphans)
- Routing latency percentiles (p50, p95, p99)
- Capability gap rate (% of routing requests with missing capabilities)
- Deduplication conflicts per hour (spike = data quality issue)
- Qdrant vector collection freshness (last embedding time)

**Alerting:**
- Routing latency >200ms → investigate graph query bottlenecks
- Duplicate risk >100 → run EntityResolver.health_check()
- Qdrant embedding staleness >1 day → re-trigger ingestion

---

## Files & Structure

```
knowledge-graph-os/
├── neo4j-schema/
│   └── schema.cypher           # Node labels, rels, indexes, constraints
├── neo4j-routing/
│   ├── package.json
│   └── router.ts               # GraphRouter class
├── qdrant-config/
│   ├── package.json
│   └── config.ts               # Collection definitions
├── ingestion-pipeline/
│   ├── package.json
│   └── ingest.ts               # Supabase → Neo4j/Qdrant sync
├── entity-resolver/
│   ├── package.json
│   └── resolver.ts             # Dedup & conflict resolution
├── docs/
│   └── PHASE-2.md              # This file
└── package.json                # Workspaces root
```

---

## References

- **Graph Engineering Blueprint** — High-level system design
- **Family Office OS** — Venture/agent/capability entity types
- **Civilization OS** — Ontology for cross-cutting concepts
- **Neo4j Best Practices** — Index/constraint strategy
- **Qdrant Docs** — Vector search, HNSW tuning
