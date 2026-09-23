# Missing Registries, Inventories, Indexes & Tables of Contents Audit
**Generated:** 2026-09-25  
**Scope:** Complete audit of metadata infrastructure  
**Purpose:** Identify gaps in discovery, navigation, and governance systems

---

## EXECUTIVE SUMMARY

**Registry Ecosystem Status:**
- ✅ **Registries:** 33 exist (but NAMING INCONSISTENT)
- ✅ **Inventories:** 1 exists (underdeveloped)
- ✅ **Indexes:** 3 exist (scattered)
- ❌ **Master TOC:** Missing (critical gap)
- ❌ **Metadata Registry:** Missing (controls all others)

**Critical Finding:** Registries exist but lack a **META-REGISTRY** that catalogs them all. Each registry is an orphaned island.

---

## SECTION 1-3: ACTION PRIORITY PLAN STATUS

### **Priority Item #2: ✅ CONTROL_BASES_REGISTRY**
**Status:** COMPLETE ✅  
**File:** `CBP_REGISTRY_EXPANDED.yaml` (5,617 lines)  
**Implementation:** All 500 bases (B001-B500) defined  
**Deployed:** Sep 25, 2026  
**Missing:** Integration into Neo4j (Phase B)

### **Priority Item #3: ❌ AGENT_MASTER_REGISTRY.md**
**Status:** INCOMPLETE  
**Issue:** 318 agents scattered across:
- `~/.claude/agents/*.md` (318 files)
- `./.agents/agents/researcher.md` (duplicate)
- `AGENTS_REGISTRY.yaml` (exists but partial)
- `AGENTS_INVENTORY_318.yaml` (exists but metadata-only)

**What's Missing:**
- Single canonical agent definition file
- Unified agent ID system (AGT-001 to AGT-318)
- Agent → skill mappings
- Agent → base assignments
- Agent → capability mapping

**Action Needed:** Consolidate into `16-AGENTS/AGENT_MASTER_REGISTRY.md`

### **Priority Item #4: ❌ REGISTRY NAMING STANDARDIZATION**
**Status:** INCOMPLETE  
**Problem:** Inconsistent naming across 33 registries

| Current Name | Should Be | Consistency |
|---|---|---|
| AGENT_REGISTRY.yaml | ❌ Duplicate | Duplicate with AGENTS_REGISTRY.yaml |
| AGENTS_REGISTRY.yaml | ✅ Correct | AGENTS_REGISTRY.yaml |
| AGENTS_INVENTORY_318.yaml | ⚠️ Hybrid | Mixed naming (Registry + Inventory) |
| AGENT_MASTER_REGISTRY.md | ⏳ Planned | Doesn't exist yet |
| BASE-REGISTRY.yaml | ❌ Wrong | Should be BASES_REGISTRY.yaml |
| CBP_REGISTRY.yaml | ✅ Correct | But CBP_REGISTRY_EXPANDED.yaml duplicates it |
| CAPABILITY_REGISTRY.yaml | ✅ Correct | Follows pattern |
| SKILL_REGISTRY.yaml | ✅ Correct | Follows pattern |
| SCENARIO_REGISTRY.yaml | ✅ Correct | Follows pattern |

**Action Needed:** Consolidate duplicates + standardize naming

---

## PART 2: COMPLETE REGISTRY AUDIT (33 REGISTRIES)

### **A. ENTITY REGISTRIES (Who/What/Where)**
| Registry | Count | Status | Naming | Gap |
|----------|-------|--------|--------|-----|
| **AGENT_REGISTRY.yaml** | ? | ❌ DUPLICATE | Wrong pattern | CONSOLIDATE with AGENTS_REGISTRY.yaml |
| **AGENTS_REGISTRY.yaml** | 318 | ⚠️ PARTIAL | Correct | Needs master definitions + assignments |
| **AGENTS_INVENTORY_318.yaml** | 318 | ⚠️ METADATA | Hybrid | Metadata-only, no definitions |
| **PEOPLE-REGISTRY.yaml** | ~21 | ✅ LIVE | Correct | Complete (but linked to agents?) |
| **ROLES-REGISTRY.yaml** | ~40+ | ✅ LIVE | Correct | Complete |
| **ECOSYSTEM_150_ENTITY_REGISTRY.yaml** | 150 | ✅ LIVE | Correct | Complete (family office entities) |
| **ECOSYSTEM_150_ENTITY_REGISTRY.json** | 150 | ⚠️ DUPLICATE | Wrong format | JSON + YAML duplicate |

### **B. BUSINESS REGISTRIES (Ventures/Operations)**
| Registry | Count | Status | Naming | Gap |
|----------|-------|--------|--------|-----|
| **VENTURE-REGISTRY.yaml** | 789 | ✅ LIVE | Correct | Complete |
| **OPCO-REGISTRY.yaml** | 35 | ✅ LIVE | Correct | Complete |
| **SECTOR-REGISTRY.yaml** | 36 | ✅ LIVE | Correct | Complete |
| **SITES_REGISTRY.yaml** | 95 | ✅ LIVE | Correct | Vercel deployments |
| **SCENARIOS_REGISTRY.yaml** | ? | ✅ LIVE | Correct | Make.com scenarios |
| **CAPABILITY_REGISTRY.yaml** | 300+ | ✅ LIVE | Correct | Complete |
| **SKILL_REGISTRY.yaml** | ? | ✅ PARTIAL | Correct | Incomplete (skills scattered) |

### **C. INFRASTRUCTURE REGISTRIES (Tools/Systems)**
| Registry | Count | Status | Naming | Gap |
|----------|-------|--------|--------|-----|
| **TOOL_GATEWAY_REGISTRY.yaml** | 110 | ✅ LIVE | Correct | OmniRoute tools |
| **LOGIC_LAYERS_REGISTRY.yaml** | 72 | ✅ LIVE | Correct | Cognitive pipeline layers |
| **FILE_FORMAT_REGISTRY.yaml** | 10 | ✅ LIVE | Correct | File format mappings |
| **REPOSITORY_REGISTRY.yaml** | 1,740 | ✅ LIVE | Correct | All repos |
| **TOKEN-USAGE-REGISTRY.yaml** | ? | ✅ LIVE | Correct | Model usage tracking |

### **D. GOVERNANCE REGISTRIES (Controls/Compliance)**
| Registry | Count | Status | Naming | Gap |
|----------|-------|--------|--------|-----|
| **CBP_REGISTRY_EXPANDED.yaml** | 500 | ✅ NEW | Correct | 500-Bases model (Sep 25) |
| **CBP_REGISTRY.yaml** | 50 | ✅ LIVE | Correct | But superseded by EXPANDED |
| **DOCUMENT_CONTROL_REGISTRY.yaml** | 25 | ✅ LIVE | Correct | SOC 2 / ISO 27001 |
| **TEST_REGISTRY.yaml** | ? | ✅ LIVE | Correct | Test definitions |

### **E. CAPITAL/INVESTMENT REGISTRIES**
| Registry | Count | Status | Naming | Gap |
|----------|-------|--------|--------|-----|
| **CAPITAL_FACILITIES_REGISTRY.yaml** | ? | ✅ LIVE | Correct | Infrastructure assets |
| **INVESTOR_SOURCE_REGISTRY.csv** | ? | ✅ LIVE | Correct | CSV format (inconsistent) |
| **LOI_REGISTRY.yaml** | ? | ✅ LIVE | Correct | Letters of Intent |
| **GRANT_OPPORTUNITY_REGISTRY.yaml** | ? | ✅ LIVE | Correct | Grant opportunities |

### **F. DATA/KNOWLEDGE REGISTRIES**
| Registry | Count | Status | Naming | Gap |
|----------|-------|--------|--------|-----|
| **RESEARCH-SOURCE-REGISTRY.yaml** | ? | ✅ LIVE | Correct | External research sources |
| **REVENUE_EVIDENCE_REGISTRY.yaml** | ? | ✅ LIVE | Correct | Revenue proof sources |
| **BUSINESS-METRIC-REGISTRY.yaml** | ? | ✅ LIVE | Correct | KPI definitions |
| **CONNECTIVITY-REGISTRY.yaml** | ? | ✅ LIVE | Correct | System connections |
| **50_STATE_REAL_ESTATE_DATA_REGISTRY.csv** | 50 | ⚠️ CSV FORMAT | Wrong | Should be YAML |

---

## PART 3: INVENTORIES (What We Have)

### **Existing Inventories**
| Inventory | Count | Status | Purpose |
|-----------|-------|--------|---------|
| **AGENTS_INVENTORY_318.yaml** | 318 | ✅ EXISTS | Agent metadata |

**What's Missing:**
- ❌ REGISTRIES_INVENTORY.yaml — Catalog of all 33 registries
- ❌ DOMAINS_INVENTORY.yaml — All 71 domains (00-50 + infrastructure)
- ❌ CAPABILITIES_INVENTORY.yaml — Coverage analysis (owned vs. external)
- ❌ TOOLS_INVENTORY.yaml — 110 OmniRoute tools
- ❌ FILES_INVENTORY.yaml — 7,629 .md files (we indexed in Neo4j)
- ❌ SKILLS_INVENTORY.yaml — All skills (currently scattered)
- ❌ DEPENDENCIES_INVENTORY.yaml — Inter-system dependencies
- ❌ GAPS_INVENTORY.yaml — All known gaps + TODOs

---

## PART 4: INDEXES & NAVIGATION

### **Existing Indexes**
| Index | Count | Status | Purpose |
|-------|-------|--------|---------|
| **INDEX.md** | ~50 links | ✅ EXISTS | Master navigation |
| **MASTER_DISCOVERY_INDEX.yaml** | ? | ✅ EXISTS | Discovery metadata |
| **SKILLS-INDEX.json** | ? | ✅ EXISTS | Skill search |

**What's Missing:**
- ❌ REGISTRY_INDEX.yaml — Master index of all 33 registries
- ❌ AGENT_INDEX.yaml — All 318 agents (searchable)
- ❌ CAPABILITY_INDEX.yaml — Capability discovery + gap analysis
- ❌ DOMAIN_INDEX.yaml — All 71 domains with cross-links
- ❌ CONTROL_BASE_INDEX.yaml — B001-B500 discovery
- ❌ VENTURE_INDEX.yaml — 789 ventures (queryable)
- ❌ ENTITY_RELATIONSHIP_INDEX.yaml — All entity connections

---

## PART 5: MASTER TABLE OF CONTENTS (CRITICAL GAP)

### **What Should Exist (But Doesn't)**

**A. META-REGISTRY (Master of Masters)**
```yaml
# _REGISTRIES/CANONICAL/META-REGISTRY.yaml
# Catalogs ALL 33 registries + their status
registries:
  - id: REG-001
    name: AGENTS_REGISTRY
    file: AGENTS_REGISTRY.yaml
    type: entity
    count: 318
    status: ACTIVE
    owner: CP-027
    source_of_truth: 16-AGENTS
    freshness_sla: weekly
    last_updated: 2026-09-25
    
  - id: REG-002
    name: VENTURES_REGISTRY
    file: VENTURE-REGISTRY.yaml
    type: business
    count: 789
    status: ACTIVE
    owner: CP-050
    source_of_truth: 23-VENTURES
    freshness_sla: daily
    last_updated: 2026-09-25
    
  # ... 31 more registries
```

**B. MASTER TABLE OF CONTENTS**
```
_REGISTRIES/CANONICAL/
├── 00-README.md (START HERE)
├── 01-META-REGISTRY.yaml (catalogs all registries)
├── 02-REGISTRY-INDEX.md (navigation)
├── 03-INVENTORY-INDEX.md (what we have)
├── 04-MISSING-INDEX.md (gaps + TODOs)
│
├── ENTITY_REGISTRIES/
│   ├── AGENTS_REGISTRY.yaml
│   ├── PEOPLE-REGISTRY.yaml
│   └── ...
│
├── BUSINESS_REGISTRIES/
│   ├── VENTURES_REGISTRY.yaml
│   ├── SECTORS_REGISTRY.yaml
│   └── ...
│
├── GOVERNANCE_REGISTRIES/
│   ├── CONTROL_BASES_REGISTRY.yaml (B001-B500)
│   ├── CONTROL_POINTS_REGISTRY.yaml (CP-001-CP-050)
│   └── ...
│
└── DATA_REGISTRY_ALIGNMENT_MATRIX.yaml
    (Cross-reference: which registries feed which others)
```

**C. REGISTRY DEPENDENCY GRAPH**
```yaml
# _REGISTRIES/CANONICAL/REGISTRY-DEPENDENCIES.yaml
# Shows data flow between registries

AGENTS_REGISTRY feeds:
  - CONTROL_BASES_REGISTRY (B-nodes assign agents)
  - PEOPLE-REGISTRY (agent owners)
  - SCENARIOS_REGISTRY (agent role assignments)

VENTURE_REGISTRY feeds:
  - CONTROL_BASES_REGISTRY (ventures in B-nodes)
  - REVENUE_EVIDENCE_REGISTRY (venture revenue)
  - CAPABILITY_REGISTRY (venture needs)

# ... 30+ more dependencies
```

---

## PART 6: MISSING REGISTRIES (8 CRITICAL)

| #  | Registry | Purpose | Status | Blocker |
|----|----------|---------|--------|---------|
| 1  | **META-REGISTRY.yaml** | Catalog of all 33 registries | ❌ MISSING | BLOCKS all navigation |
| 2  | **TERMINOLOGY_REGISTRY.yaml** | Canonical terminology (venture→VEN, sector→SEC) | ❌ MISSING | BLOCKS Neo4j queries |
| 3  | **LIFECYCLE_REGISTRY.yaml** | State enums per entity type | ❌ MISSING | BLOCKS unified status |
| 4  | **ENVIRONMENT_REGISTRY.yaml** | local/staging/production | ❌ MISSING | BLOCKS deployment |
| 5  | **QUERY_TEMPLATES.yaml** | Pre-built Cypher + hybrid search patterns | ❌ MISSING | BLOCKS user queries |
| 6  | **AGENT_MASTER_REGISTRY.md** | Canonical agent definitions (consolidate 318) | ❌ MISSING | BLOCKS agent discovery |
| 7  | **REGISTRY-DEPENDENCIES.yaml** | Data flow between registries | ❌ MISSING | BLOCKS impact analysis |
| 8  | **SYSTEMS_INTEGRATION_MATRIX.yaml** | Which systems feed which | ❌ MISSING | BLOCKS dependency mapping |

---

## PART 7: MISSING INVENTORIES (8 CRITICAL)

| # | Inventory | Purpose | Status |
|---|-----------|---------|--------|
| 1 | **REGISTRIES_INVENTORY.yaml** | All 33 registries + metadata | ❌ MISSING |
| 2 | **DOMAINS_INVENTORY.yaml** | All 71 domains (00-50 + infra) | ❌ MISSING |
| 3 | **CAPABILITIES_INVENTORY.yaml** | Coverage analysis (owned vs external) | ❌ MISSING |
| 4 | **TOOLS_INVENTORY.yaml** | 110 OmniRoute tools | ❌ MISSING |
| 5 | **SKILLS_INVENTORY.yaml** | All skills + domain mapping | ❌ MISSING |
| 6 | **DEPENDENCIES_INVENTORY.yaml** | Inter-system dependencies | ❌ MISSING |
| 7 | **GAPS_INVENTORY.yaml** | Known gaps + TODOs | ❌ MISSING |
| 8 | **CONTROL_BASES_INVENTORY.yaml** | All 500 bases + status | ✅ READY (CBP_REGISTRY_EXPANDED.yaml) |

---

## PART 8: MISSING INDEXES (7 CRITICAL)

| # | Index | Purpose | Status |
|---|-------|---------|--------|
| 1 | **REGISTRY_INDEX.yaml** | Navigation to all 33 registries | ❌ MISSING |
| 2 | **AGENT_INDEX.yaml** | Search + discovery for 318 agents | ❌ MISSING |
| 3 | **CAPABILITY_INDEX.yaml** | Capability discovery + gaps | ❌ MISSING |
| 4 | **DOMAIN_INDEX.yaml** | All 71 domains + cross-links | ❌ MISSING |
| 5 | **CONTROL_BASE_INDEX.yaml** | B001-B500 discovery | ✅ READY (in CBP_REGISTRY_EXPANDED.yaml) |
| 6 | **VENTURE_INDEX.yaml** | 789 ventures (searchable) | ❌ MISSING |
| 7 | **ENTITY_RELATIONSHIP_INDEX.yaml** | All entity connections | ❌ MISSING |

---

## SUMMARY: WHAT'S BLOCKING NAVIGATION

**The Problem:** 33 registries exist but are orphaned. There's no master index that says:
- "What registries do we have?"
- "Which registry is authoritative for X?"
- "How do registries feed each other?"
- "What's the current state of each registry?"

**The Cost:** Every lookup requires manual registry browsing.

**The Solution:** 3-layer metadata infrastructure:

```
LAYER 1: META-REGISTRY (1 file)
  ↓ Catalogs all 33 registries
  ↓
LAYER 2: REGISTRY-INDEX + DEPENDENCIES (2 files)
  ↓ Shows relationships between registries
  ↓
LAYER 3: ENTITY INDEXES (7 files)
  ↓ Enables discovery of agents, capabilities, domains, etc.
```

---

## ACTION PLAN (Priority Order)

### **WEEK 1 (Critical Path)**
1. ✅ Create `META-REGISTRY.yaml` — Catalog all 33 registries
2. ✅ Create `TERMINOLOGY_REGISTRY.yaml` — Canonical terms
3. ✅ Create `AGENT_MASTER_REGISTRY.md` — Consolidate 318 agents
4. ✅ Rename + deduplicate (AGENT_REGISTRY.yaml ← AGENTS_REGISTRY.yaml, etc.)
5. ✅ Create `REGISTRY-DEPENDENCIES.yaml` — Data flow map

### **WEEK 2 (Discovery Layer)**
6. Create `REGISTRY_INDEX.yaml` — Navigation to all registries
7. Create `AGENT_INDEX.yaml` — Search all 318 agents
8. Create `DOMAIN_INDEX.yaml` — Navigate 71 domains
9. Create `VENTURE_INDEX.yaml` — Search 789 ventures
10. Create `CAPABILITY_INDEX.yaml` — Gap analysis

### **WEEK 3 (Governance)**
11. Create `LIFECYCLE_REGISTRY.yaml` — State enums
12. Create `ENVIRONMENT_REGISTRY.yaml` — Deployment targets
13. Create `QUERY_TEMPLATES.yaml` — Pre-built queries
14. Wire all into Neo4j schema

---

**Status:** All 33 registries exist but lack metadata infrastructure. 15 critical files needed to make them discoverable and interconnected.

