# Phase 2: Graph-Native Migration (YAML → Neo4j)

**Authority:** Knowledge Graph Engineer Framework  
**Status:** APPROVED (User chose Option B)  
**Timeline:** Phase 2 Sprint (Sep 17–Oct 1, 2026)  
**Scope:** Complete migration from dual-layer (YAML + Neo4j) to graph-native architecture

---

## Executive Summary

**From:** Fragmented dual-layer system
- YAML registries (Sectors, Ventures, Tools, Agents, Capabilities)
- Neo4j relationships (manually wired)
- No unified provenance or contradiction detection

**To:** Graph-native Company Brain
- Every entity = (:Entity) node
- Every relationship = typed [:RELATES] edge
- Unified provenance via [:DERIVED_FROM]->(Source)
- Contradiction detection enabled
- Single source of truth (Neo4j graph)

**Migration Steps:**
1. Define complete schema (COMPANY-BRAIN-GRAPH-SCHEMA.cypher) ✅
2. Create Cypher MERGE templates for each entity type
3. Build LangGraph ingestion pipeline
4. Migrate YAML registries → nodes + edges
5. Ingest Phase 2 docs with full provenance
6. Verify integrity gates
7. Retire YAML registries

---

## Step 1: Complete Schema ✅

**File:** `_ONTOLOGY/COMPANY-BRAIN-GRAPH-SCHEMA.cypher`

Defines:
- Entity uniqueness constraints (entity_id)
- Source uniqueness constraints (sha256)
- Query indexes (type, confidence, contested, needs_review)
- Relationship model (MENTIONS, RELATES, CONTRADICTS, SUPPORTS, DERIVED_FROM, SUPERSEDED_BY, MERGED_INTO)
- Integrity gates (dangling references, provenance, contradictions)
- Audit log schema
- Navigation views (promoted entities, active contradictions, knowledge gaps)

---

## Step 2: Cypher MERGE Templates (Next)

For each entity type, create a template that:
1. Extracts entity from YAML source
2. Computes SHA256 of source
3. Checks for existing entity (by entity_id)
4. Merges or updates with new properties
5. Creates [:DERIVED_FROM]->(Source) edge
6. Flags duplicates or contradictions

### Template: Ventures (Example)

```cypher
// MERGE Venture from YAML
// Input: yaml_venture object with {ref_id, name, sector, status, properties...}

WITH {
  entity_id: yaml_venture.ref_id,
  name: yaml_venture.name,
  type: "Venture",
  sector: yaml_venture.sector,
  status: yaml_venture.status,
  confidence: 0.8,
  source_count: 1,
  created: datetime(),
  updated: datetime(),
  contested: false,
  needs_review: false
} AS venture_props,
datetime() AS now,
"YAML:ventures-by-sector.yaml" AS source_title

MERGE (v:Entity {entity_id: venture_props.entity_id})
ON CREATE SET v += venture_props
ON MATCH SET 
  v.updated = now,
  v.source_count = v.source_count + 1,
  v.needs_review = CASE WHEN v.source_count < 2 THEN true ELSE false END

WITH v, source_title, now

// Create/link Source node
MERGE (s:Source {sha256: apoc.util.md5([source_title, datetime().epochMillis])})
ON CREATE SET 
  s.title = source_title,
  s.type = "registry",
  s.date = now,
  s.url = "/Volumes/LaCie/Company-Brain/_REGISTRIES/CANONICAL/ventures-by-sector.yaml",
  s.raw_path = "/Volumes/LaCie/Company-Brain/_REGISTRIES/CANONICAL/ventures-by-sector.yaml",
  s.metadata = {format: "yaml", entity_count: 789}

// Create provenance edge
MERGE (v)-[:DERIVED_FROM]->(s)

RETURN v.entity_id AS venture_id, v.source_count AS sources, s.sha256 AS source_hash;
```

### Templates to Create

**Entity Types (Priority Order):**
1. Ventures (789)
2. Sectors (35)
3. Tools (110)
4. Agents (16)
5. Capabilities (50+)
6. Gaps (from Phase 2 docs)
7. Solutions (from Phase 2 docs)
8. Repositories (1,740)
9. Relationships (all edge types)

---

## Step 3: LangGraph Ingestion Pipeline

**Purpose:** Automate YAML → Neo4j migration with traceability

**Architecture:**

```
Input: YAML file
  ↓
Parse YAML → Extract entities
  ↓
For each entity:
  ├─ Compute SHA256(source)
  ├─ Check if entity_id exists in Neo4j
  ├─ MERGE node (Cypher template)
  ├─ Create [:DERIVED_FROM]->(Source)
  ├─ Log event to AuditLog
  └─ Collect contradictions
  ↓
Verify integrity gates:
  ├─ Dangling references
  ├─ Provenance completeness
  ├─ Contradiction consistency
  └─ Orphan detection
  ↓
Report: {entities_created, entities_updated, contradictions_detected, gates_pass}
```

**Tools:**
- Python + Neo4j driver
- YAML parsing (PyYAML)
- LangGraph for orchestration
- SHA256 hashing (hashlib)
- Cypher execution

**Key Decision Gate:**
If contradictions detected, flag for human review before auto-promotion.

---

## Step 4: YAML Registry Migration (Phase 2a)

**Registries to Migrate:**

| Registry | Records | Entity Type | Status |
|----------|---------|-------------|--------|
| ventures-by-sector.yaml | 789 | Venture | Tier-1 |
| sectors.yaml | 35 | Sector | Tier-1 |
| tools-registry.yaml | 110 | Tool | Tier-2 |
| agents-registry.yaml | 16 | Agent | Tier-2 |
| capability-registry.yaml | 50+ | Capability | Tier-2 |
| repository-registry.yaml | 1,740 | Repository | Tier-3 |

**Execution Order:**
1. **Day 1:** Sectors + Ventures (35 + 789 entities)
2. **Day 2:** Tools + Agents + Capabilities (110 + 16 + 50)
3. **Day 3:** Repositories (1,740)
4. **Day 4:** Verify + Audit

---

## Step 5: Phase 2 Architecture Document Ingestion

**Four Phase 2 Docs to Ingest:**
1. MODEL-ROUTER-ARCHITECTURE.md
2. TOOL-GATEWAY-PERMISSIONS.md
3. AUTONOMOUS-LOOP-SPECIFICATION.md
4. SYSTEM-STATE-MODEL.md

**For Each Doc:**
1. Compute SHA256(document)
2. Extract entities:
   - Component: Model Router, Tool Gateway, Autonomous Loop, System State
   - Decision: Route 80% to local, approval gates, heartbeat schedule
   - Tool: qwen2.5-coder, hermes3, claude (routing decisions)
3. Create (:Component), (:Decision), (:Tool) nodes
4. Create [:RELATES] edges with {type: "enables", "depends_on", "powers"}
5. Create [:DERIVED_FROM]->(Source) edges with SHA256
6. Flag contradictions with YAML claims

**Example: Autonomous Loop from YAML vs. Phase 2 Doc**

YAML might say: "Loop: observe → plan → execute"  
Phase 2 doc says: "Loop: observe → understand → plan → execute → verify → record → learn" (7 steps)

→ Create (:CONTRADICTS) edge, flag contested: true, preserve both claims for human review

---

## Step 6: Integrity Gate Verification

**Before promoting to production, verify:**

### Gate 1: Dangling References
```cypher
MATCH (s)-[r:MENTIONS]->(e) WHERE NOT e:Entity 
RETURN COUNT(*) AS dangling_refs;
// Must be = 0
```

### Gate 2: Provenance Completeness
```cypher
MATCH (e:Entity) WHERE NOT (e)-[:DERIVED_FROM]->(:Source) 
RETURN COUNT(*) AS orphan_entities;
// Must be = 0
```

### Gate 3: Contradiction Consistency
```cypher
MATCH (e:Entity)-[c:CONTRADICTS]->() WHERE NOT e.contested 
RETURN COUNT(*) AS inconsistent;
// Must be = 0
```

### Gate 4: Orphan Detection (Warning, not fail)
```cypher
MATCH (e:Entity) WHERE NOT ()-[:RELATES|:MENTIONS|:SUPPORTS|:DEPENDS_ON|:USES]->(e) 
RETURN COUNT(*) AS isolated_entities;
// Acceptable if < 50 (new entities, not yet wired)
```

### Gate 5: Source Coverage
```cypher
MATCH (s:Source) RETURN COUNT(*) AS total_sources;
// Should equal: 10 YAML registries + 4 Phase 2 docs = 14 sources
```

---

## Step 7: YAML Retirement (Phase 2b)

**After Migration Verified:**

1. Archive YAML registries to `_ARCHIVE/YAML/` (read-only)
2. Update all documentation to reference Neo4j graph
3. Update APIs to query Neo4j instead of YAML files
4. Wire OmniRoute to use graph entities
5. Set up weekly sync integrity checks (append-only history via [:SUPERSEDED_BY])

---

## Success Criteria

✅ **Entities:** All 789 ventures, 35 sectors, 110 tools, 16 agents, 50+ capabilities in Neo4j  
✅ **Provenance:** Every entity traces to (:Source) via [:DERIVED_FROM]  
✅ **Contradictions:** YAML claims vs. Phase 2 docs detected and preserved  
✅ **Integrity Gates:** All 5 gates pass (0 dangling, 0 orphans, 14 sources)  
✅ **Relationships:** All YAML relationships (contains, belongs_to, uses) converted to [:RELATES] edges  
✅ **Confidence:** Single-source entities flagged needs_review: true; 2+ sources → promoted  
✅ **Documentation:** All registries → Neo4j queries; YAML archived

---

## Blockers & Dependencies

| Blocker | Resolution | Dependency |
|---------|-----------|-----------|
| Neo4j connection unstable | Verify docker context + password | Step 1 |
| YAML parsers fail on escaping | Test with sample ventures | Day 1 |
| Duplicate entity_ids | Review sector taxonomy | Day 1 |
| Contradiction explosion | Human review gate (don't auto-promote) | Step 6 |
| Phase 2 docs not finalized | Use latest commit SHA for now | Step 5 |

---

## Next Action

**Unit 6:** Execute Phase 2a (Sector + Venture migration)
- Read ventures-by-sector.yaml
- Build Cypher MERGE loop
- Execute: 35 sectors + 789 ventures → Neo4j
- Verify: Integrity gates pass

**Timeline:** Phase 2 Sprint (Sep 17–Oct 1)  
**Owner:** Knowledge Graph Engineer pattern (user's framework)

---

**Updated:** 2026-09-17  
**Authority:** [[STARTHERE]], [[ANTIGRAVITY]], [[REALITY]]
