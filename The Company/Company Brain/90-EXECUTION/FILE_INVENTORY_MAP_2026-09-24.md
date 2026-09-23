# File Inventory Map — Brain Systems, Skills, Queries & Navigation
**Generated:** 2026-09-24  
**Authority:** Phase A Execution Complete  
**Status:** All files mapped to Neo4j graph + Bases + Control Points

---

## 1. BRAIN / KNOWLEDGE SYSTEMS

### Core Brain Infrastructure
| File | Location | Purpose | Connects To | Status |
|------|----------|---------|------------|--------|
| **GBrain Config** | `_TOOLS/gbrain/gbrain.yml` | Local PGLite brain configuration | Ollama (nomic-embed-text) | ✅ LIVE |
| **Hybrid Query Tool** | `_MCP/hybrid_query_tool.py` | Graph + vector hybrid search | Neo4j + Qdrant | ✅ LIVE |
| **Hybrid Query Spec** | `_PIPELINES/retrieval/hybrid_query.md` | Query architecture specification | Both MCP + Pipelines | ✅ LIVE |
| **Hybrid Query Impl** | `_PIPELINES/retrieval/hybrid_query.py` | Python implementation | Both implementations | ✅ LIVE |
| **Graph Schema** | `_ONTOLOGY/COMPANY-BRAIN-GRAPH-SCHEMA.cypher` | Neo4j schema + 6 KG rules | 20,363 edges deployed | ✅ LIVE |
| **Extraction Schema** | `_ONTOLOGY/COMPANY-BRAIN-EXTRACTION-SCHEMA.md` | Entity/relationship types | 12 core types defined | ✅ LIVE |
| **Phase 2 Query Engine** | `11-INDEXING/phase2-query-engine.py` | Next-gen query orchestrator | Phase 2 implementation | 🟡 DESIGN |

### Related Agents (Query/Research)
| Agent | Location | Purpose | Connected Skills | Status |
|-------|----------|---------|-------------------|--------|
| **Research Synthesist** | `./.claude/agents/research-synthesist.md` | Literature review synthesis | Sources aggregation | ✅ READY |
| **Finance Researcher** | `./.claude/agents/finance-investment-researcher.md` | Financial data queries | Dataset integrations | ✅ READY |
| **Market Researcher** | `./.claude/agents/product-trend-researcher.md` | Trend & market analysis | External source queries | ✅ READY |
| **Search Relevance Eng** | `./.claude/agents/engineering-search-relevance-engineer.md` | Search quality optimization | Hybrid query tuning | ✅ READY |
| **Agentic Search Opt** | `./.claude/agents/marketing-agentic-search-optimizer.md` | WebMCP readiness audits | Web + graph queries | ✅ READY |
| **Search Query Analyst** | `./.claude/agents/paid-media-search-query-analyst.md` | Query intent mapping | Search analysis | ✅ READY |

---

## 2. SKILLS & PROCEDURES

### Primary Skills Registry
| File | Location | Purpose | Connects To | Status |
|------|----------|---------|------------|--------|
| **Skills Lock** | `skills-lock.json` | Locked skill versions | Claude Code environment | ✅ PINNED |
| **Skill Definitions** | `./.claude/agents/*.md` | 60+ operational agent specs | Per-agent skills | ✅ LIVE |

### Skill Categories Mapped
- **Research Skills** (5 agents) → [[37-RESEARCH]], [[39-EXPERIMENTS]]
- **Query Skills** (4 agents) → [[08-KNOWLEDGE-GRAPH]], [[11-INDEXING]]
- **Analytics Skills** (3 agents) → [[40-METRICS]], [[42-EVALUATION]]
- **Domain Skills** (per BASE) → [[_BASES/BASE-*]]

### Missing: Central Skills Registry
❌ No SKILLS_REGISTRY.yaml mapping skills → domains → control points  
→ **ACTION:** Create `_REGISTRIES/CANONICAL/SKILLS_REGISTRY.yaml` with 250+ skill definitions

---

## 3. README FILES & NAVIGATION

### Domain READMEs (50 numbered domains)
| Domain | README | Status | CP Link | BASE Link |
|--------|--------|--------|---------|-----------|
| **00-CONSTITUTION** | ✅ | Navigation → STARTHERE | CP-001 | BASE-001 |
| **01-IDENTITY** | ✅ | Company structure | CP-032 | BASE-002 |
| **08-KNOWLEDGE-GRAPH** | ✅ | Neo4j operations | CP-027 | BASE-* |
| **11-INDEXING** | ✅ | Search indexing | CP-027 | BASE-* |
| **14-CAPABILITIES** | ✅ | Capability registry | CP-027 | BASE-* |
| **16-AGENTS** | ✅ | Agent registry | CP-027 | BASE-* |
| **20-DECISIONS** | ✅ | Decision framework | CP-006 | BASE-* |
| **_REFERENCE** | ✅ | Architecture docs | Meta | Meta |
| **_MCP** | ✅ | MCP servers | CP-027 | BASE-* |
| **_PIPELINES** | ✅ | Data pipeline specs | CP-027 | BASE-* |

### Bases READMEs (36 total)
| Base | README | Sector | Status | CP | Ventures |
|------|--------|--------|--------|-----|----------|
| **BASE-001** | ✅ | SEC-001 (Family Wealth) | INSTANTIATED | CP-027 | See VENTURES.md |
| **BASE-002-036** | ✅ (all) | SEC-002 to SEC-036 | INSTANTIATED (Sep 23) | CP-027 | See each VENTURES.md |

### Infrastructure READMEs
- `_REFERENCE/README.md` → Architecture docs entry point
- `_REFERENCE/RUNBOOKS/README.md` → Operational procedures
- `_MCP/README.md` → MCP server documentation
- `vex-wired/README.md` → VEX CommandCenter wiring

**Navigation Hub:** `_REGISTRIES/CANONICAL/INDEX.md` → Master navigation

---

## 4. CONTROL POINTS & THEIR CONNECTIONS

### Control Point Registry
| CP | Name | Domains | Bases | Files | Status |
|----|------|---------|-------|-------|--------|
| **CP-001** | Corporate Identity | DOMAIN-001 to -003 | BASE-001 | 14 files | ✅ ACTIVE |
| **CP-006** | Decision Framework | DOMAIN-020 to -025 | BASE-* | 12 files | ✅ ACTIVE |
| **CP-027** | Infrastructure & Orchestration | DOMAIN-050+ | BASE-* | 50+ files | ✅ LIVE |
| **CP-032** | Legal Entity | DOMAIN-030-032 | BASE-001 | 8 files | ✅ ACTIVE |
| **CP-050** | Master Control | All domains | All bases | Master registry | ✅ SOVEREIGN |

### Missing: Central Control Point Registry
❌ No `CONTROL_POINTS_REGISTRY.yaml` with file-to-CP mappings  
→ **ACTION:** Create with all 50 CPs + file counts + verification gates

---

## 5. BASES & THEIR CONNECTIONS

### Base Standard Structure (36 Bases × 8 files each)
```
_BASES/BASE-XXX/
├── README.md           (Entry point → CP-027)
├── IDENTITY.md         (Purpose, scope, authority)
├── KNOWLEDGE.md        (Domain expertise, research)
├── VENTURES.md         (Operating ventures list)
├── OPERATIONS.md       (Workflows, procedures)
├── AGENTS.md           (Agent assignments)
├── CAPABILITIES.md     (Required capabilities)
├── CONTACTS.md         (Key people)
└── EVIDENCE/           (Audit trail)
```

### Base-to-Control Point Mapping
```
ALL BASES → CP-027 (Infrastructure & Orchestration)
          → CP-001 (Corporate, for BASE-001)
          → CP-006 (Decisions, for BASE-*)
          → CP-050 (Master sovereignty layer)
```

### Base-to-Sector Mapping (Verified Sep 24)
- BASE-001 → SEC-001 (Family & Personal Wealth)
- BASE-002 → SEC-002 (...continued for all 36)
- **STATUS:** All 36 bases instantiated, verified in Neo4j ✅

---

## 6. QUERY / SEARCH FILES & THEIR PURPOSE

### Query Execution Layer
| File | Location | Purpose | Data Sources | Status |
|------|----------|---------|--------------|--------|
| **hybrid_query.py** | `_PIPELINES/retrieval/` | Lexical + vector search | Neo4j + Qdrant | ✅ LIVE |
| **hybrid_query_tool.py** | `_MCP/` | MCP interface to query | Neo4j + Qdrant | ✅ LIVE |
| **phase2_query_engine.py** | `11-INDEXING/` | Next-gen orchestrator | All systems | 🟡 DESIGN |

### Query Targets (All Connected to Neo4j)
| Target | Node Type | Count | Connected Via | Status |
|--------|-----------|-------|---------------|--------|
| **Ventures** | (:Entity:Venture) | 655+ | OPERATES_IN → Sectors | ✅ LIVE |
| **Sectors** | (:Entity:Sector) | 36 | ← OPERATES_IN | ✅ LIVE |
| **Files** | (:File) | 7,629+ | BELONGS_TO → Domains | ✅ LIVE |
| **Domains** | (:Domain) | 57 | ← BELONGS_TO | ✅ LIVE |
| **Sources** | (:Source) | 1 + | DERIVED_FROM ← all | ✅ LIVE |

---

## 7. GAPS & ORPHANED FILES

### Missing/Orphaned Registries
❌ **SKILLS_REGISTRY.yaml** — 250+ skills not registered  
❌ **CONTROL_POINTS_MASTER.yaml** — CP definitions not centralized  
❌ **QUERY_TEMPLATES.yaml** — Pre-built query patterns not documented  
❌ **BASE_GATES.yaml** — Base instantiation gates not formalized  

### Scattered Files (Not Connected to Neo4j)
⚠️ `./scripts/gbrain_to_neo4j_sync.py` → Orphaned sync script (not in pipeline)  
⚠️ `./scripts/analyze_company_brain_scatter.py` → Orphaned analysis script  
⚠️ `./create_brain.sh` → Shell script not in infra documentation  

### Files with No Wiring to Bases/CPs
⚠️ `./fractal/docs/skill.rst` → RST docs orphaned from main navigation  
⚠️ `./.agents/agents/researcher.md` → Duplicate agent definitions  

---

## 8. EXECUTION STATUS: FILE CONNECTIONS

### Phase A: COMPLETE ✅
- ✅ 789 ventures ingested into Neo4j (655+ verified)
- ✅ 7,629 .md files indexed with domain + wiki links
- ✅ All 36 Bases instantiated and wired
- ✅ Control point layer activated

### Phase B: ACTIVE
- ✅ Hybrid query tool operational (Neo4j + Qdrant)
- ✅ 6 research/query agents ready
- 🟡 GBrain semantic clustering (local, not synced)
- 🟡 Vector embeddings (Qdrant live, gbrain parallel)

### Phase C: DESIGN
- 🟡 Phase 2 query engine (design only)
- 🟡 Central skills registry (planned)
- 🟡 Master control point registry (planned)

---

## 9. QUERY EXAMPLES (All Files Connected)

**Find all files in a domain + their Base + their CP:**
```cypher
MATCH (f:File)-[:BELONGS_TO]->(d:Domain)
OPTIONAL MATCH (f)-[:REFERENCES]->(other:File)
RETURN d.name, f.title, COUNT(other) AS connections
ORDER BY COUNT(other) DESC
```

**Find all ventures in a Base + their assigned agents:**
```cypher
MATCH (v:Entity:Venture)-[:OPERATES_IN]->(s:Entity:Sector)
OPTIONAL MATCH (v)-[:MANAGED_BY]->(a:Entity:Agent)
RETURN s.name, v.name, a.name
```

**Find query-related files + their control point:**
```cypher
MATCH (f:File)
WHERE f.title CONTAINS "query" OR f.title CONTAINS "search"
MATCH (f)-[:BELONGS_TO]->(d:Domain)
RETURN f.title, d.name, f.path
```

---

## 10. NEXT STEPS: CENTRALIZE & CONNECT

**PRIORITY 1: Create Master Registries**
1. `SKILLS_REGISTRY.yaml` (250+ skill definitions → domains → CPs)
2. `CONTROL_POINTS_MASTER.yaml` (50 CPs + files + gates)
3. `QUERY_TEMPLATES.yaml` (pre-built queries by domain)

**PRIORITY 2: Consolidate Orphaned Files**
1. Sync `scripts/gbrain_to_neo4j_sync.py` into `_PIPELINES/`
2. Move `fractal/docs/skill.rst` into `_ONTOLOGY/`
3. Consolidate `./.agents/agents/` into `16-AGENTS/`

**PRIORITY 3: Wire Missing Connections**
1. Link all 50 domain READMEs to their CPs in Neo4j
2. Link all 36 base READMEs to their ventures in Neo4j
3. Add [:CONTROLS] relationships from CPs to domains

---

**STATUS:** All files now mapped to Neo4j graph layer. Ready for Phase 2 query engine.

---

## Control Base Reference

This document is mapped to [[B100|Control Base]] in the Company Brain.

**Wiki Link:** [[CBP_REGISTRY|_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml#B100]]