# Company Brain — Knowledge Graph Extraction Schema

**Purpose:** Define how to extract entities and relationships from Company Brain sources  
**Authority:** Knowledge Graph Engineer (Phase C: Schema Mapping)  
**Updated:** 2026-09-23  
**Status:** Extraction templates ready for Phase B (LangGraph orchestrator)

---

## Core Entity Types for Company Brain

### Organizational Entities
| Type | ID | Example | Source Types |
|------|----|---------| -------------|
| **Venture** | VEN | LT-005 (HealthRoute Medical Courier) | registry, database, decision |
| **Sector** | SEC | SEC-009 (Logistics) | registry, audit |
| **OpCo** | OPC | OpCo-Logistics | registry, database |
| **Person** | PER | Antwuan Johns (Founder) | decision, audit, external |
| **Team** | TEA | Revenue Loop Team | code, decision |
| **Role** | ROL | Venture Manager | decision, audit |

### Capability & Execution Entities
| Type | ID | Example | Source Types |
|------|----|---------| -------------|
| **Capability** | CAP | CAP-087 (Real-time Dispatch Routing) | registry, code, architecture |
| **Agent** | AGT | AGT-231 (Logistics Dispatch Agent) | architecture, code, decision |
| **Workflow** | WFL | FLOW-031 (Order to Delivery) | code, decision, audit |
| **Loop** | LOP | Revenue Loop L2 | decision, audit |
| **Skill** | SKL | Venture Analysis Skill | code, architecture |
| **Tool** | TOL | Make.com, n8n | code, external |
| **MCP** | MCP | OmniRoute MCP | architecture, code |

### Knowledge & Results Entities
| Type | ID | Example | Source Types |
|------|----|---------| -------------|
| **Dataset** | DST | ALL_789_VENTURES.csv | database, registry, code |
| **Report** | RPT | VENTURE-READINESS-SCORECARD | audit, decision |
| **Analysis** | ANL | Sector competition analysis | decision, audit |
| **Decision** | DEC | "Expand to 36 sectors" | decision |
| **Outcome** | OUT | $7.5K revenue (Week 1) | audit, database |
| **Lesson** | LES | "Supabase is ground truth, not YAML" | audit, decision |

---

## Core Relationship Types for Company Brain

### Structure & Containment
| Relationship | Source → Target | Property | Example |
|--------------|-----------------|----------|---------|
| **OPERATES_IN** | Venture → Sector | primary (bool) | LT-005 OPERATES_IN SEC-009 |
| **CONTAINS_VENTURE** | Sector → Venture | count | SEC-009 CONTAINS_VENTURE LT-005 |
| **ASSIGNED_TO** | Venture → OpCo | ownership | LT-005 ASSIGNED_TO OpCo-Logistics |
| **MEMBER_OF** | Person → Team | role | Antwuan MEMBER_OF Revenue Loop Team |

### Capability & Dependencies
| Relationship | Source → Target | Property | Example |
|--------------|-----------------|----------|---------|
| **REQUIRES** | Venture → Capability | criticality | LT-005 REQUIRES CAP-087 (CRITICAL) |
| **IMPLEMENTS** | Agent → Capability | status | AGT-231 IMPLEMENTS CAP-087 (COMPLETE) |
| **DEPENDS_ON** | Workflow → Tool | failure_impact | FLOW-031 DEPENDS_ON Make.com (CRITICAL) |
| **USES** | Agent → Skill | context | AGT-231 USES Venture Analysis SKL |

### Evidence & Decision
| Relationship | Source → Target | Property | Example |
|--------------|-----------------|----------|---------|
| **EVIDENCED_BY** | Decision → Report | confidence | "Expand sectors" EVIDENCED_BY VENTURE-READINESS-SCORECARD (0.85) |
| **GENERATED_BY** | Outcome → Capability | measurement | $7.5K Revenue OUT GENERATED_BY Revenue Loop LOP |
| **LEARNED_FROM** | Agent → Lesson | update_frequency | AGT-231 LEARNED_FROM "Supabase is truth" (weekly) |
| **CONTRADICTS** | Venture → Venture | (auto-detected) | LT-005 (SEC-001 in CSV) CONTRADICTS LT-005 (SEC-017 in registry) |

---

## Extraction Templates by Source Type

### 1. Registry Sources (ventures-by-sector.yaml, SECTOR-REGISTRY.yaml)

**Source Properties:**
```yaml
sha256: "a3f9..." # File hash
type: "registry"
title: "ventures-by-sector.yaml"
date: "2026-09-23"
raw_path: "_REGISTRIES/CANONICAL/ventures-by-sector.yaml"
```

**Extraction Pattern:**
```python
# For each sector entry:
entity_type = "Sector"
entity_id = "SEC-001"
name = "Beauty & Wellness"
confidence = 1.0  # Registry is authoritative

# For each venture in sector:
entity_type = "Venture"
entity_id = "LT-005"
name = "HealthRoute Medical Courier"
confidence = 1.0

# Create relationship:
relationship = {
    "subject": "LT-005",
    "object": "SEC-001",
    "type": "OPERATES_IN",
    "confidence": 1.0,
    "claim": "HealthRoute operates in Beauty & Wellness sector"
}
```

**Contradiction Detection:**
- If CSV says LT-005 → SEC-001 but registry says SEC-017: CREATE [:CONTRADICTS] edge
- Set contested=true on both LT-005 entries
- Preserve both source_sha values

---

### 2. Database Sources (Supabase ventures, OpCos, sectors tables)

**Source Properties:**
```yaml
sha256: "b4f2..." # Query result hash
type: "database"
title: "Supabase ventures table (2026-09-23)"
date: "2026-09-23"
raw_path: "supabase://project/table/ventures"
```

**Extraction Pattern:**
```python
# For each ventures row:
entity_type = "Venture"
entity_id = row["venture_id"]  # e.g., "LT-005"
name = row["venture_name"]
confidence = 0.95  # Database is high-confidence source

# For related OpCo:
entity_type = "OpCo"
entity_id = row["opco_id"]
name = row["opco_name"]
confidence = 0.95

# Relationship:
relationship = {
    "subject": "LT-005",
    "object": row["opco_id"],
    "type": "ASSIGNED_TO",
    "confidence": 0.95,
    "claim": f"Venture {row['venture_name']} assigned to {row['opco_name']}"
}
```

**Threshold-Gating:**
- Supabase data (confidence 0.95) + CSV data (confidence 1.0) = source_count >= 2
- Venture is promoted (needs_review=false)
- Entry into lookup view

---

### 3. Architecture Sources (COMPANY-BRAIN-GRAPH-SCHEMA.cypher, etc.)

**Source Properties:**
```yaml
sha256: "c5d3..."
type: "architecture"
title: "COMPANY-BRAIN-GRAPH-SCHEMA.cypher"
date: "2026-09-23"
raw_path: "_ONTOLOGY/COMPANY-BRAIN-GRAPH-SCHEMA.cypher"
```

**Extraction Pattern:**
```python
# For each constraint/index:
entity_type = "Schema"
entity_id = "constraint_entity_unique"
name = "Entity Uniqueness Constraint"
confidence = 0.9  # Architecture docs are declarative

# For each relationship definition:
entity_type = "Relationship"
entity_id = "rel_mentions"
name = "MENTIONS (Source mentions Entity)"
confidence = 0.9

# Relationship:
relationship = {
    "subject": "Source",
    "object": "Entity",
    "type": "MENTIONS",
    "confidence": 0.9,
    "claim": "Source document mentions entity"
}
```

---

### 4. Decision Sources (ADRs, meeting notes, audit logs)

**Source Properties:**
```yaml
sha256: "d6e4..."
type: "decision"
title: "2026-09-25 Founder Decisions: Venture Count Reality"
date: "2026-09-25"
raw_path: "_REGISTRIES/CANONICAL/INDEX.md"
```

**Extraction Pattern:**
```python
# For each decision recorded:
entity_type = "Decision"
entity_id = "DEC-SEP25-001"
name = "Venture Count Reality: 580 vs 789"
confidence = 0.7  # Decisions are forward-looking, may change

# For each supporting analysis:
entity_type = "Analysis"
entity_id = "ANL-DEDUP-001"
name = "Deduplication audit findings"
confidence = 0.85

# Relationship:
relationship = {
    "subject": "DEC-SEP25-001",
    "object": "ANL-DEDUP-001",
    "type": "EVIDENCED_BY",
    "confidence": 0.85,
    "claim": "Decision to investigate venture count grounded in deduplication analysis"
}
```

---

### 5. Audit Sources (REALITY.md, ground truth ledgers)

**Source Properties:**
```yaml
sha256: "e7f5..."
type: "audit"
title: "REALITY.md — Ground Truth Ledger (2026-09-23)"
date: "2026-09-23"
raw_path: "REALITY.md"
```

**Extraction Pattern:**
```python
# For each verified fact:
entity_type = "Fact"  # or specific type (Venture, Sector, etc.)
entity_id = "FACT-NEO4J-001"
name = "Neo4j running with 20,363 edges"
confidence = 1.0  # Audit is ground truth

# For each finding or contradiction:
entity_type = "Finding"
entity_id = "FIND-SEP25-002"
name = "Venture count discrepancy (82-90% error in SEC-014, SEC-024, SEC-029)"
confidence = 1.0

# Relationship to affected entity:
relationship = {
    "subject": "FIND-SEP25-002",
    "object": "SEC-014",
    "type": "CONTRADICTS",
    "confidence": 1.0,
    "claim": "Registry claims 117 ventures; CSV shows 21 (82% discrepancy)"
}
```

---

## Extraction Rules & Gates

### Pre-Extraction (Orient Phase)
1. **Compute SHA256** of raw source (never use supplied path)
2. **Read graph config:** current entity types, relationship types, domain focus
3. **Check for existing source:** if sha256 exists and hash matches, skip re-extraction
4. **Scan for stale sources:** if source.date < 90 days ago AND newer source exists, flag for re-ingest

### Extraction (Analyze Phase)
1. **LLM structured output** → entities + relationships (use pydantic models)
2. **Assign confidence** based on how explicitly text supports claim (0..1)
3. **For each entity:** compare against existing node (is it consistent or contradictory?)
4. **Assess domain relevance:** out-of-scope content still ingests as Source node

### Merge (Merge Phase)
1. **MERGE Source node** (sha256 is unique key)
2. **MERGE Entity nodes** (entity_id is unique key)
3. **MERGE Relationships** with type + source_sha + created timestamp
4. **Threshold-gate:** if source_count < 2, flag needs_review=true
5. **Detect contradictions:** same entity pair, same rel type, different claims → [:CONTRADICTS]

### Verify (Verify Phase)
Hard gates (must all pass):
- ✅ Source node exists for every extraction
- ✅ Zero dangling [:MENTIONS] references
- ✅ Every entity has ≥1 [:DERIVED_FROM] edge
- ✅ No unflagged orphan entities
- ✅ contested=true iff [:CONTRADICTS] edge exists
- ✅ Audit log entry written with timestamp, action, entity counts, contradictions

---

## Example: Ingesting ventures-by-sector.yaml

**Source:** `_REGISTRIES/CANONICAL/ventures-by-sector.yaml`  
**Expected Extraction:**

```
Entities Created:
  - SEC-001: Beauty & Wellness
  - SEC-009: Logistics
  - LT-005: HealthRoute Medical Courier
  - LT-011: CarrierDispatch TMS
  - RE-001: WorldwideBro Real Estate
  - OPS-001: CareerOps Staffing
  ... (789 ventures total)

Relationships Created:
  - LT-005 OPERATES_IN SEC-001 (confidence 1.0)
  - LT-011 OPERATES_IN SEC-009 (confidence 1.0)
  - RE-001 OPERATES_IN SEC-012 (confidence 1.0)
  - OPS-001 OPERATES_IN SEC-014 (confidence 1.0)
  ... (N relationships total)

Contradictions Detected:
  - LT-005 OPERATES_IN SEC-001 (from ventures.yaml, sha256 a3f9...)
    CONTRADICTS
    LT-005 OPERATES_IN SEC-017 (from registry YAML, sha256 b4f2...)
  → Both edges preserved, contested=true on LT-005

Verification:
  ✅ Source node exists
  ✅ All [:MENTIONS] resolve to real entities
  ✅ All entities have [:DERIVED_FROM]
  ✅ 0 orphan entities
  ✅ contested=true iff [:CONTRADICTS] exists
  ✅ Audit log: 789 entities, 1 contradiction detected
```

---

## Extraction Confidence Scoring

| Source Type | Default Confidence | Notes |
|-------------|-------------------|-------|
| **Registry** | 1.0 | Authoritative, signed off |
| **Audit** | 1.0 | Ground truth, verified |
| **Database** | 0.95 | Live state, transactional |
| **Code/Architecture** | 0.9 | Declarative specs |
| **Decision/Planning** | 0.7 | Forward-looking, may change |
| **External/Third-party** | 0.6–0.85 | Source-dependent credibility |
| **LLM Extraction** | 0.75–0.95 | Depends on extraction confidence output |

**Threshold for Promotion:**
- Single source: source_count=1, needs_review=true (excluded from lookup views)
- Multi-source: source_count≥2, needs_review=false (included in lookup views)

---

## Next Steps (Phase B & A)

**Phase B:** Build LangGraph orchestrator (extract → merge → detect → verify → navigate)  
**Phase A:** Ingest all Company Brain sources into Neo4j live graph

See: `_ONTOLOGY/COMPANY-BRAIN-LANGGRAPH-ORCHESTRATOR.md` (forthcoming)
