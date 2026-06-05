# Consolidation Strategy — Merge Existing Files Into One Unified Body

**Purpose:** Stop creating duplicates. Consolidate existing docs into ONE authoritative system.

**Status:** 🚨 BLOCKER #1 - Too many overlapping files (20+ system prompts, 5+ capability registries)

**Generated:** 2026-06-05

---

## 🔍 WHAT ALREADY EXISTS (Don't Create — Merge!)

### System Prompts / Operating Brain
| File | Purpose | Status | Action |
|------|---------|--------|--------|
| `venture-hub/docs/AI-EXECUTION-PROTOCOL.md` | **Primary execution framework** | ✅ Complete | KEEP as source |
| `venture-hub/docs/VENTURE-BRAIN-LAYERS.md` | **System architecture** (7 layers) | ✅ Complete | KEEP as source |
| `venture-hub/docs/COMPLETE-OPERATING-MANUAL.md` | **Business models** (Berkshire, PE, VC) | ✅ Complete | CONSOLIDATE with brain layers |
| `venture-hub/docs/BUSINESS-THINKING-LAYERS.md` | **Abstraction stack** (task→civilization) | ✅ Complete | Already authoritative |
| `venture-hub/docs/COMPOSITE-OPERATING-MODEL.md` | **3-layer model** (holdco, GC, AI-native) | ✅ Complete | Already authoritative |
| `venture-hub/docs/EXECUTION-NETWORK-ORCHESTRATION.md` | **Partner orchestration** | ✅ Complete | REFERENCE only |
| ❌ (DO NOT CREATE) `OPERATING-SYSTEM-BRAIN-PROMPT.md` | Unified system prompt | Redundant | **USE AI-EXECUTION-PROTOCOL.md instead** |

**Action:** Update `AI-EXECUTION-PROTOCOL.md` to **reference** business models section from COMPLETE-OPERATING-MANUAL, not duplicate.

---

### Coding Standards / Principles
| File | Purpose | Status | Action |
|------|---------|--------|--------|
| `The office/.agents/principles.json` | **250 engineering rules** (CANONICAL) | ✅ Complete | KEEP as source |
| `The office/scripts/check-principles.sh` | **Validation script** | ✅ Complete | KEEP & extend |
| ❌ (DO NOT CREATE) `CODING-STANDARDS.md` | Enforce principles | Redundant | **USE principles.json** |

**Action:** Create `validate-code-standards.sh` that **wraps** check-principles.sh and adds CLAUDE.md validation.

---

### Capability Mappings
| File | Purpose | Status | Action |
|------|---------|--------|--------|
| `venture-hub/ventures_with_capabilities.csv` | **Ventures → capabilities** (618 rows) | ✅ Complete | KEEP as source |
| `WORLDWIDEBRO-OS/REGISTRIES/capability-component-repo-linkage-v2-REAL-NAMES.json` | **1274 capabilities → 535 repos** | ✅ Complete | CONSOLIDATE |
| `WORLDWIDEBRO-OS/REGISTRIES/repos-by-capability.json` | **Capability → repos reverse map** | ✅ Complete | KEEP as reference |
| `WORLDWIDEBRO-OS/REGISTRIES/ventures-capabilities-parsed.json` | **Parsed venture capabilities** | ✅ Complete | VERIFY accuracy |
| ❌ (DO NOT CREATE) `VENTURES-CAPABILITIES-MAPPED.csv` | Cross-reference | Exists as JSON | **CONSOLIDATE from existing JSONs** |

**Action:** Create **ONE canonical file** that merges all 4 registries into `VENTURES-CAPABILITIES-UNIFIED.json`.

---

### Venture Complexity Analysis
| File | Purpose | Status | Action |
|------|---------|--------|--------|
| `venture-hub/docs/COMPLETE-VENTURE-MAP.md` | **Venture architecture** | ✅ Complete | KEEP |
| `venture-hub/docs/VENTURE-BRAIN-LAYERS.md` | **System routing** | ✅ Complete | KEEP |
| `venture-hub/BUSINESS-LOGIC-LAYERS.md` | **Financial logic** | ✅ Complete | KEEP |

---

## 📊 MOST COMPLEX VENTURES (Ultra-Complex: 6+ Features)

**47 ventures requiring 6+ features (7.6% of portfolio)**

### Most Complex Example
```
Venture ID: a4edc8b5-1635-4e87-85eb-bfcc9e168697
Name: Tax Intelligence Platform
Sector: Tax Services
Required Capabilities (6):
  1. api              → LightRAG or opensre
  2. authentication   → design-system or thunderbolt
  3. database         → Supabase
  4. monitoring       → mission-control + DuckDB
  5. payment          → ❌ MISSING (NO REPO HAS THIS!)
  6. security         → ⚠️ Scattered (need consolidated)
```

### Common Pattern (92.4% of ventures: 4-5 features)
```
Pattern 1: api + authentication + dashboard + database + portfolio
  → 51 ventures need this
  → Repos: LightRAG, design-system, Supabase, DuckDB

Pattern 2: api + authentication + database + monitoring + security
  → 47 ventures need this
  → Repos: LightRAG, mission-control, design-system, DuckDB, (security?)
```

**Key Insight:** The complexity reveals REAL GAPS:
- ❌ Payment processing (47+ ventures need it, 0 repos provide it)
- ⚠️ Security hardening (scattered across docs, no unified repo)
- ✅ API/auth/data/monitoring (well-covered)

---

## 🔗 UNIFIED BODY STRUCTURE (Proposed)

### Layer 1: Source of Truth
```
venture-hub/
├── CLAUDE.md                              (master instructions - link to AI-EXECUTION-PROTOCOL)
├── ventures-master.csv                    (712 ventures: id, name, sector, stage, repo_url)
├── MASTER-REPO-REGISTRY.csv               (985 repos: name, venture_id, health, priority)
├── docs/
│   ├── AI-EXECUTION-PROTOCOL.md          (system prompt + execution contract)
│   ├── VENTURE-BRAIN-LAYERS.md           (7-layer architecture)
│   └── COMPLETE-OPERATING-MANUAL.md      (business models)
└── registries/
    └── VENTURES-CAPABILITIES-UNIFIED.json (NEW: merged from 4 sources)
```

### Layer 2: Governance (7 Starred Repos)
```
Each repo (civilization-os-local/, design-system/, etc.):
├── CLAUDE.md                             (shared or symlink from venture-hub)
├── components.md                         (what this repo exports: {component: [capabilities]})
├── CAPABILITIES.md                       (which ventures use us: auto-generated from UNIFIED)
└── patterns.md                           (coding rules for this repo)
```

### Layer 3: Validation
```
scripts/
├── validate-code-standards.sh            (check principles.json + CLAUDE.md in all repos)
├── validate-starred-repos.py             (verify all 7 have CLAUDE, components, CAPABILITIES, patterns)
└── validate-capabilities-coverage.py     (check for gaps like "payment" and "security")
```

---

## ✅ WHAT TO DO (Priority Order)

### PHASE 0 (Now: 1 hour): Consolidate Existing Capability Registries
- [ ] Read all 4 capability JSON/CSV files
- [ ] Identify conflicts (which is most current?)
- [ ] Merge into `VENTURES-CAPABILITIES-UNIFIED.json`
- [ ] Validate against 47 ultra-complex ventures
- [ ] Add to DATA-SOURCES.md as canonical reference

### PHASE 1 (Next: 2 hours): Fix 7 Starred Repos
For each: civilization-os-local, iza-os-rag-system, design-system, mission-control, thunderbolt, pitch-kit, LightRAG

- [ ] Add/verify CLAUDE.md (symlink to venture-hub if identical)
- [ ] Create components.md (export inventory)
- [ ] Create CAPABILITIES.md (auto-generated from UNIFIED registry)
- [ ] Create patterns.md (coding rules)

### PHASE 2 (Follow: 1 hour): Deduplicate
- [ ] Remove design-system-integrated, design-system-live (keep base, symlink others)
- [ ] Consolidate fin-001-repo, genixbank-repo (keep primary, link secondary)
- [ ] Update education ventures folder (add CAPABILITIES.md linking to registry)

### PHASE 3 (Skip): Don't Create These
❌ `OPERATING-SYSTEM-BRAIN-PROMPT.md` — Use `venture-hub/docs/AI-EXECUTION-PROTOCOL.md`  
❌ `CODING-STANDARDS.md` — Use `The office/.agents/principles.json`  
❌ `VENTURES-CAPABILITIES-MAPPED.csv` — Use `VENTURES-CAPABILITIES-UNIFIED.json`  

---

## 📊 Result: One Unified Body

**Before (Fragmented):**
- 20+ system prompt docs (overlapping)
- 5+ capability registries (conflicting)
- 3× design-system versions (duplicate)
- 2× GenixBank implementations (parallel)
- 7 starred repos (no governance)
- 550 venture repos (unmapped)

**After (Unified):**
- 1 execution protocol (AI-EXECUTION-PROTOCOL.md)
- 1 unified registry (VENTURES-CAPABILITIES-UNIFIED.json)
- 1 design-system (consolidated)
- 1 GenixBank (canonical)
- 7 starred repos with consistent CLAUDE.md + components.md + CAPABILITIES.md + patterns.md
- 550 venture repos auto-generated from template

**Benefit:** When building venture for "Tax Intelligence Platform":
1. Look up in VENTURES-CAPABILITIES-UNIFIED.json
2. Find needs: api, auth, db, monitoring, payment, security
3. Traverse to repos (LightRAG, design-system, mission-control, ...)
4. Check each repo's components.md
5. Assemble venture by combining components
6. **Gaps are visible** (payment, security = red flags)

---

## 🚀 Next Step

Read the 4 capability registry files and consolidate into ONE.
