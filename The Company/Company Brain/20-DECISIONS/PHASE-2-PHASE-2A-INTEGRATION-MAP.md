# Phase 2 ↔ Phase 2a Integration Map

**Authority:** CP-027 (Infrastructure) + CP-012 (Agent Control Plane)  
**Created:** 2026-09-17  
**Timeline:** Phase 2 (Sep 17–Oct 1) → Phase 2a (Oct 1–31) → Integration complete by Oct 31  
**Status:** LINKED EXECUTION (sequential handoff)

---

## Executive Summary

**Phase 2** (Graph-Native) builds the knowledge layer.  
**Phase 2a** (Agentic Engineering) builds the execution layer.

Phase 2a **depends on** Phase 2. Without the Neo4j graph, agents have no context. Without agents, the graph is inert.

**Success = Both phases running synchronized by Oct 31.**

---

## Phase 2 Deliverables → Phase 2a Inputs

### Deliverable 1: Neo4j Schema (Sep 17–18)
**Phase 2:** Deploy `COMPANY-BRAIN-GRAPH-SCHEMA.cypher`
- Uniqueness constraints (entity_id, sha256)
- Query indexes (type, confidence, contested, needs_review)
- Relationship model (MENTIONS, RELATES, CONTRADICTS, DERIVED_FROM)
- Integrity gates (dangling refs, provenance, contradictions)

**Phase 2a Uses:**
```cypher
// Agent context query: "What ventures need agents like me?"
MATCH (venture:Entity:Venture)-[:RELATES {type: "needs"}]->(capability:Entity:Capability)
WHERE capability.type = "Cold Email Writing"
RETURN venture.entity_id, venture.name, venture.status, venture.sector
LIMIT 10;

// Capability discovery: "What tools can I use?"
MATCH (cap:Entity:Capability)-[:RELATES {type: "requires"}]->(tool:Entity:Tool)
WHERE tool.risk_level = "read"
RETURN tool.entity_id, tool.name, tool.category, tool.cost_tier;

// Revenue tracking: "Which deal did my work close?"
MATCH (deal:Entity:Deal)-[:RELATES {type: "attributed_to"}]->(agent:Entity:Agent {entity_id: $agent_id})
RETURN deal.value, deal.venture_id, deal.created, agent.entity_id;
```

---

### Deliverable 2: YAML → Neo4j Migration (Sep 19–22)
**Phase 2:** Ingest ~3,000 entities
- 35 Sectors
- 789 Ventures
- 110 Tools
- 16 Agents
- 50+ Capabilities
- 4 Phase 2 docs (Model Router, Tool Gateway, Autonomous Loop, System State)

**Phase 2a Uses:**
```cypher
// Agent discovery: "Who am I? What's my purpose?"
MATCH (a:Entity:Agent {entity_id: "cold-email-writer"})
RETURN a.name, a.purpose, a.autonomy_level, a.status;

// Venture intelligence: "Which ventures are revenue-ready?"
MATCH (v:Entity:Venture)
WHERE v.status = "operating" AND v.confidence >= 0.8
RETURN v.entity_id, v.name, v.sector, v.source_count;

// Opportunity discovery: "What ventures need my capability?"
MATCH (v:Entity:Venture)-[:RELATES {type: "gap"}]->(gap:Entity:Gap)
WHERE gap.description LIKE "%cold%email%"
RETURN v.entity_id, v.name, gap.description, gap.entity_id;
```

---

### Deliverable 3: Integrity Gates (Sep 25)
**Phase 2:** Verify all 5 gates pass
1. 0 dangling references
2. 0 missing provenance (every entity has [:DERIVED_FROM])
3. 0 contradiction inconsistencies (contested flag = true iff [:CONTRADICTS] edges exist)
4. < 50 orphan entities (acceptable for new entities)
5. 14+ sources (10 YAML + 4 Phase 2 docs)

**Phase 2a Guarantees:**
- ✅ No missing context (no query returns null unexpectedly)
- ✅ No orphaned agents (every agent appears in AGENT_REGISTRY.yaml + Neo4j)
- ✅ No conflicting capability claims (contradictions preserved + flagged)
- ✅ Provenance intact (every agent action traceable to source decision)

---

## Phase 2a Execution Layer Feeds Back to Phase 2

### Agent Actions → Neo4j Graph

**Phase 2a:** Agents run and log actions  
**Phase 2:** Graph captures and learns

```cypher
// When Cold Email Writer sends 50 emails:
CREATE (action:Entity:AgentAction {
  entity_id: "action-" + randomUUID(),
  agent_id: "cold-email-writer",
  venture_id: "OPS-001",
  action_type: "send_email",
  email_count: 50,
  timestamp: datetime(),
  confidence: 0.95
})
-[:DERIVED_FROM]->(:Source {
  title: "AppointmentSetter agent log",
  type: "agent_execution"
})
-[:RELATES {type: "triggered_by"}]->(venture:Entity:Venture {entity_id: "OPS-001"});

// When Discovery Caller books 4 meetings:
CREATE (outcome:Entity:Outcome {
  entity_id: "outcome-meetings-sep17",
  agent_id: "discovery-caller",
  outcome_type: "meetings_booked",
  count: 4,
  confidence: 0.98,
  timestamp: datetime()
})
-[:RELATES {type: "attributed_to"}]->(agent:Entity:Agent {entity_id: "discovery-caller"})
-[:RELATES {type: "generated_by"}]->(action:Entity:AgentAction);

// When Closer closes 1 deal for $5K:
CREATE (deal:Entity:Deal {
  entity_id: "deal-OPS-001-sep17-001",
  agent_id: "closer",
  venture_id: "OPS-001",
  value: 5000,
  currency: "USD",
  status: "won",
  timestamp: datetime(),
  confidence: 1.0
})
-[:RELATES {type: "attributed_to"}]->(agent:Entity:Agent {entity_id: "closer"})
-[:RELATES {type: "originated_from"}]->(outcome:Entity:Outcome)
-[:RELATES {type: "belongs_to"}]->(venture:Entity:Venture {entity_id: "OPS-001"});
```

---

## Synchronized Execution Timeline

### Week 1: Phase 2 Foundation (Sep 17–21)

| Day | Phase 2 | Phase 2a | Integration |
|-----|---------|---------|-------------|
| Mon 17 | Deploy schema + indexes | Read REAL-AGENT-BLUEPRINT.md | Align on Neo4j query interface |
| Tue 18 | Test Cypher templates | Build AGENT_REGISTRY.yaml (318 agents) | Verify agent IDs match Neo4j |
| Wed 19 | Migrate sectors + ventures (824 entities) | Build DISPATCH_ROUTER.js logic | Test router with sample agents |
| Thu 20 | Migrate tools + agents + capabilities | Build SKILL_REGISTRY.yaml | Wire skills to tools |
| Fri 21 | Ingest Phase 2 docs + detect contradictions | Test revenue attribution pipeline (cold email → deal) | Verify deal entity schema |

### Week 2: Phase 2 Verification (Sep 23–27)

| Day | Phase 2 | Phase 2a | Integration |
|-----|---------|---------|-------------|
| Mon 23 | Run integrity gates (5 gates) | Deploy 1st agent (Cold Email Writer) | Agent queries Neo4j for venture list |
| Tue 24 | Gate failures? Fix + re-verify | Agent logs 1st action to Neo4j | Verify action node created correctly |
| Wed 25 | Archive YAML registries | Deploy 2nd agent (Discovery Caller) | Cross-agent context sharing (Neo4j) |
| Thu 26 | Update documentation (YAML → Neo4j) | Deploy 3rd agent (Closer) | End-to-end deal tracking: email → meeting → deal |
| Fri 27 | Commit final state | Tie 3 agents to OPS-001 venture | Verify $500–$1500 revenue from 3 agents |

### Weeks 3–4: Phase 2a Ramp-Up (Oct 1–31) — Phase 2 Complete

Phase 2 work ends; Phase 2a continues deploying 50 agents against live Neo4j graph.

---

## Critical Integration Points

### 1. Neo4j Connection String (Phase 2a Uses)

Phase 2 sets up Neo4j; Phase 2a connects to it.

```javascript
// In Phase 2a agent code:
const neo4j = require('neo4j-driver');
const driver = neo4j.driver(
  'bolt://100.87.214.70:7687',
  neo4j.auth.basic('neo4j', 'changeme')
);

// Query to discover context:
const session = driver.session();
const result = await session.run(
  `MATCH (v:Entity:Venture {entity_id: $venture_id})
   RETURN v.name, v.sector, v.status, v.source_count`,
  { venture_id: 'OPS-001' }
);
```

### 2. Agent Entity Schema Alignment

Phase 2 creates (:Agent) nodes; Phase 2a agents must match.

**Phase 2 (Neo4j):**
```yaml
(:Agent {
  entity_id: "cold-email-writer",
  name: "Cold Email Writer",
  type: "Agent",
  purpose: "Generate personalized cold emails",
  autonomy_level: "L2",  # Requires human review
  status: "deployed",
  confidence: 0.85,
  created: 2026-09-17
})
```

**Phase 2a (AGENT_REGISTRY.yaml):**
```yaml
cold-email-writer:
  entity_id: cold-email-writer  # MUST MATCH Neo4j
  name: Cold Email Writer
  domain: sales
  category: lead_generation
  autonomy_level: L2
  deployed: true
  model: sonnet
  success_rate: 0.72
```

✅ **Same entity_id, same properties.**

### 3. Capability Discovery Path

Phase 2 stores capabilities in graph; Phase 2a queries for them.

```cypher
// Phase 2 created this:
(:Capability {
  entity_id: "KG-017",
  name: "Hybrid Search (Graph + Vector)",
  type: "Capability",
  layer: 7,
  confidence: 0.9
})
-[:RELATES {type: "requires"}]->(:Tool {entity_id: "neo4j"})
-[:RELATES {type: "requires"}]->(:Tool {entity_id: "qdrant"});

// Phase 2a queries:
MATCH (cap:Entity:Capability {entity_id: "KG-017"})
-[:RELATES {type: "requires"}]->(tool:Entity:Tool)
RETURN tool.entity_id, tool.name, tool.cost_tier;
// Returns: neo4j, qdrant (for context retrieval)
```

### 4. Revenue Attribution Pipeline

Phase 2 creates entity structure; Phase 2a flows revenue through it.

```
Agent Action (Neo4j Entity)
  ↓ [:RELATES {type: "triggered"}]
Venture (Neo4j Entity)
  ↓ [:RELATES {type: "generated"}]
Deal (Neo4j Entity)
  ↓ [:RELATES {type: "attributed_to"}]
Agent (Neo4j Entity, update confidence)
  ↓ (query for metrics)
Revenue Report
```

**Phase 2a queries Phase 2 graph:**
```cypher
// "How much revenue did I generate this month?"
MATCH (agent:Entity:Agent {entity_id: "cold-email-writer"})
-[:RELATES {type: "attributed_to"}]-(deal:Entity:Deal)
WHERE deal.status = "won" AND deal.created >= $start_date
RETURN SUM(deal.value) AS total_revenue, COUNT(deal) AS deal_count;
```

---

## Failure Modes & Recovery

### Failure 1: Phase 2 Delayed (Schema Not Ready by Oct 1)

**Impact:** Phase 2a agents have no context, can't discover ventures/capabilities.

**Recovery:**
1. Phase 2a agents operate without Neo4j (fallback to YAML registries)
2. Actions logged to CSV instead of Neo4j
3. Once Phase 2 complete, replay CSV actions into Neo4j
4. Confidence reset to 0.5 (unverified until replayed)

**Mitigation:** Deploy Phase 2 schema by Sep 21 (not Oct 1).

---

### Failure 2: Neo4j Connection Drops Mid-Phase-2a

**Impact:** Agents can't query context, revenue tracking breaks.

**Recovery:**
1. Agents use local cache (last 100 queries) until connection restored
2. Actions queued in Redis, replayed when online
3. Revenue audit trail in PostgreSQL (backup)
4. Contradiction detection paused (restart on reconnect)

**Mitigation:** Implement circuit breaker pattern in agent code.

---

### Failure 3: Schema Mismatch (Phase 2a Agents Expect Different Entity Structure)

**Impact:** Agent queries return null, revenue attribution fails.

**Recovery:**
1. Phase 2 runs schema migration script
2. Rename properties (e.g., `agent_id` → `entity_id`)
3. Backfill missing edges
4. Phase 2a updates queries to new schema
5. Re-test revenue attribution

**Mitigation:** Finalize schema before Phase 2a starts (both teams sign off by Sep 25).

---

## Success Criteria (Oct 31 Checkpoint)

### Phase 2 Complete ✅
- [ ] 3,000 entities in Neo4j (Ventures, Sectors, Tools, Agents, Capabilities)
- [ ] Every entity has [:DERIVED_FROM]->(Source) provenance
- [ ] 5 integrity gates pass (0 dangling, 0 orphans, 14+ sources)
- [ ] YAML registries archived (read-only)
- [ ] Documentation updated (YAML → Neo4j queries)

### Phase 2a Complete ✅
- [ ] 50 agents deployed (L1/L2 mix)
- [ ] All agents query Neo4j for context
- [ ] Revenue attribution pipeline working (email → meeting → deal → $revenue)
- [ ] 10+ agents live in production (OPS-001, LT-005, CALLCENTER, etc.)
- [ ] $500K+ revenue attributed to Phase 2a agents by Dec 31

### Integration Complete ✅
- [ ] Agent entity_ids in AGENT_REGISTRY.yaml match Neo4j (:Agent) nodes
- [ ] Agent queries return correct venture/capability context (no nulls)
- [ ] Revenue flows from agent actions → deals → Neo4j Deal entities → revenue reports
- [ ] Dispatch router ranks agents by trustworthiness + success_rate (sourced from Neo4j)
- [ ] Contradictions in venture claims visible to agents (contested: true flag)
- [ ] Zero manual data syncing between Phase 2 and Phase 2a (all Neo4j)

---

## Dependencies & Blockers

| Blocker | Owner | Deadline |
|---------|-------|----------|
| Neo4j schema finalized | Phase 2 | Sep 18 |
| AGENT_REGISTRY.yaml schema agreed | Phase 2a | Sep 20 |
| Cypher query patterns documented | Phase 2 | Sep 21 |
| Agent context queries tested | Phase 2a | Sep 27 |
| Revenue attribution schema validated | Both | Sep 27 |
| Phase 2 integrity gates pass | Phase 2 | Sep 25 |
| Phase 2a dispatch router ready | Phase 2a | Oct 1 |

---

## Handoff Protocol (Sep 30 → Oct 1)

**Phase 2 to Phase 2a Handoff Checklist:**

```bash
# Phase 2 engineer runs:
1. Verify Neo4j is live: curl -u neo4j:changeme http://100.87.214.70:7474/
2. Count entities: MATCH (e:Entity) RETURN COUNT(*) AS entity_count
3. Verify gates: MATCH (s:Source) RETURN COUNT(*) AS source_count (should be 14+)
4. Export schema: docker exec company-brain-neo4j cypher-shell -u neo4j -p changeme "SHOW CONSTRAINTS"
5. Create Neo4j query guide: Write 5 example queries for Phase 2a agents
6. Sign off: "Phase 2 schema ready for agent integration"

# Phase 2a engineer confirms:
1. Neo4j connection working: Test 3 sample queries
2. Agent entity_ids match Neo4j: Spot-check 5 agents
3. Capability discovery working: Query for "Cold Email" capability
4. Revenue schema understood: Walk through deal → revenue flow
5. Sign off: "Phase 2a agents ready to start executing"
```

---

## Git Commits

**Phase 2 Final Commit:**
```
feat(phase-2): Graph-native complete — 3000 entities, 5 gates pass, ready for Phase 2a integration
```

**Phase 2a Integration Commit:**
```
feat(phase-2a): Wire agent registry to Neo4j — agents query context, revenue attribution live
```

---

## Next Review Points

- **Sep 25:** Phase 2 integrity gates pass (GO/NO-GO for Phase 2a start)
- **Oct 1:** Phase 2a agents first deployed (query Neo4j for context)
- **Oct 15:** 10 agents live, first revenue attributed
- **Oct 31:** Phase 2 + Phase 2a integration complete, 50 agents operating

---

**Updated:** 2026-09-17  
**Authority:** [[PHASE-2-GRAPH-NATIVE-MIGRATION]] ↔ [[PHASE-2A-AGENTIC-ENGINEERING-PLAN]]  
**Next:** Execute Phase 2 (Sep 17–Oct 1), then Phase 2a (Oct 1–31)
