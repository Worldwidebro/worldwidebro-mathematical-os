---
title: System Ontology (v2.1)
date: 2026-07-25T22:55:00Z
version: 2.1
---

# IZA OS Ontology

**Updated:** 2026-07-25 | **Status:** ✅ LIVE | **Change:** Added Chat2DB as Database Intelligence Service

---

## 10 Core Entity Types

### 1. **Venture** (712 instances)
- **Stored in:** Neo4j, PostgreSQL
- **Attributes:** id, name, sector, status, MRR, runway_months, capabilities_needed

### 2. **Repository** (1,639 instances)
- **Stored in:** Qdrant, Neo4j
- **Attributes:** id, url, language, stars, capabilities, related_ventures

### 3. **Capability** (25 canonical + 70+ derived)
- **Stored in:** Neo4j, PostgreSQL
- **Attributes:** id, name, category, implemented_by (repos), needed_by (ventures)

### 4. **Skill** (296+ active)
- **Stored in:** Neo4j, MCP_REGISTRY.json
- **Attributes:** id, name, phase (1-14), description, agent_role, tools_used

### 5. **MCP** (18 active)
- **Stored in:** MCP_REGISTRY.json, Neo4j
- **Attributes:** id, name, status, category, capabilities[], used_by[]

### 6. **OPCO** (6 + 18 instances)
- **Stored in:** Neo4j, PostgreSQL
- **Attributes:** id, name, ventures[], sectors, KPIs

### 7. **Sector** (14 canonical → 31 expanded)
- **Stored in:** Neo4j, PostgreSQL
- **Attributes:** id, name, opco_id, venture_count, revenue_potential

### 8. **Infrastructure Service** (16 active)
- **Stored in:** TOPOLOGY.md, Neo4j
- **Attributes:** name, host, port, status, purpose, dependencies
- **Examples:** Neo4j, PostgreSQL, DuckDB, OmniRoute, Traefik, **Chat2DB (NEW)**

### 9. **Entity** (Generic)
- **Stored in:** Neo4j, Supabase
- **Attributes:** id, type, name, associated_venture, created_at, updated_at

### 10. **Chat2DB (Database Intelligence)** ← NEW 2026-07-25
- **Role:** Natural language query interface
- **Connections:** ✅ Neo4j | ✅ PostgreSQL | ✅ DuckDB
- **LLM:** FreeLLMAPI
- **Capabilities:** NL→SQL/Cypher, schema viz, optimization, ERD generation
- **Access:** http://100.87.214.70:8080 (admin/ventures2026)

---

## Key Relationships

| Relationship | From → To | Example |
|--------------|-----------|---------|
| BELONGS_TO_SECTOR | Venture → Sector | CON-001 → Construction |
| NEEDS_CAPABILITY | Venture → Capability | CON-001 needs "payment-processing" |
| IMPLEMENTS_CAPABILITY | Repository → Capability | stripe/repo implements "payment-processing" |
| QUERIES | Chat2DB → Database | Queries Neo4j, PostgreSQL, DuckDB |

---

## Query Routing (Chat2DB)

```
Natural Language Input
    ↓
FreeLLMAPI (SQL/Cypher generation)
    ↓
Route by intent:
    ├─ Graph/relationship? → Neo4j (Cypher)
    ├─ Transactional? → PostgreSQL (SQL)
    └─ Analytics? → DuckDB (SQL)
    ↓
Execute + Visualize
```

---

## Storage Map

| Entity | Primary | Secondary | Query |
|--------|---------|-----------|-------|
| Venture | PostgreSQL | Neo4j | SQL + Cypher |
| Repository | Qdrant | Neo4j | Vector + Graph |
| Capability | Neo4j | PostgreSQL | Graph + FK join |
| Chat2DB | TOPOLOGY.md | Neo4j | Service config |

---

---

## Detailed Entity Schemas (v1.1 - 2026-07-28)

### Entity Properties & Storage

**Venture:** id, name, sector, stage, revenue_usd_monthly, owner, repo_id, created_date, status (883 instances) → Supabase + Neo4j  
**Repository:** id, name, url, venture_id, language, purpose, owner, last_commit_date (700 instances) → GitHub API + repos.json + Neo4j  
**Agent:** id, name, tools[], memory_size_mb, success_rate, decision_authority, owned_ventures[] (22 instances) → agents.json + Neo4j  
**Skill:** id, name, parameters[], mcp_tool, dependencies[] (296 instances) → skills.json + MCP_REGISTRY.json + Neo4j  
**Task:** id, venture_id, agent_id, skill_id, status, cost_usd, created_date, duration_seconds → Supabase + Neo4j  
**Decision:** id, task_id, agent_id, decision_type, rationale, authority_level, timestamp → Supabase + Neo4j  
**Outcome:** id, task_id, result_type, metrics, feedback, learned_pattern → Supabase + Langfuse  
**File:** id (path), repo_id, venture_id, agent_id, skill_ids[], language, purpose, tags[] → file_index.csv + Git repos + Neo4j  
**Relationship:** source_entity_id, relationship_type, target_entity_id, properties{}, created_date → Neo4j + Supabase  
**Organization:** id, name, org_type, role, owns[], parent_org_id → Supabase + Neo4j

### Canonical Relationship Types (12)

OWNS | OPERATES | USES | CREATED | MODIFIED | DEPENDS_ON | OPERATED_BY | GENERATES | EXECUTES | PRODUCES | CREATES | TOUCHES

---

**v2.1 (2026-07-25):** Added Chat2DB  
**v2.0 (2026-07-22):** Initial ontology  
**v1.1 (2026-07-28):** Enhanced with detailed property schemas, storage map, 12 relationship types, 883 ventures × 700 repos × 22 agents × 296 skills
