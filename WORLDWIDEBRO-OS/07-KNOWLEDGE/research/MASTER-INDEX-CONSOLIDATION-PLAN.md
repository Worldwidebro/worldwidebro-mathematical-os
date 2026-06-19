---
references:
  - [[Influence-Venture-Business-OS/REFERENCE/REFERENCE-HUB]]
  - [[Influence-Venture-Business-OS/INFRASTRUCTURE_LAYERS/INFRASTRUCTURE-HUB]]
  - [[Influence-Venture-Business-OS/STRATEGY_LAYERS/STRATEGY-HUB]]
---

# Master Index Consolidation Plan

**Analysis Date:** 2026-06-13  
**Total Masters Found:** 71 files  
**Overlapping/Redundant:** 18-25 files  
**Consolidation Target:** 10-12 unified masters  

---

## CRITICAL OVERLAP #1: REPOSITORY REGISTRIES (7 FILES → 2)

### Current State: 7 duplicate/overlapping registry files

| # | File | Location | Repos | Status | Action |
|---|------|----------|-------|--------|--------|
| 1 | **REPOSITORY-REGISTRY.json** | REFERENCE/ | 1,592 | ✅ CURRENT | **KEEP** |
| 2 | GITHUB-REPOSITORIES-MASTER-LIST.md | REFERENCE/ | ~6 | ⚠️ INDEX | **KEEP** (human-readable) |
| 3 | MASTER-REPO-REGISTRY.csv | venture-hub/ | 550 | ❌ OUTDATED | **DELETE** |
| 4 | MASTER_REPO_REGISTRY_COMPLETE.csv | venture-hub/docs/ | 1,387 | ❌ OUTDATED | **DELETE** |
| 5 | REPO_REGISTRY.json | venture-hub/ | 0 | ❌ EMPTY | **DELETE** |
| 6 | REPO_REGISTRY.json | HRMS/ | 0 | ⚠️ VENTURE-SPECIFIC | **REPLACE** with query script |
| 7 | REPO_REGISTRY.json | Automations/ | 0 | ⚠️ CONFIG-SPECIFIC | **REPLACE** with query script |

### Action Plan
```
WEEK 1: Archive outdated CSVs
  - Move MASTER-REPO-REGISTRY.csv → archive/
  - Move MASTER_REPO_REGISTRY_COMPLETE.csv → archive/
  - Keep for reference only

WEEK 2: Replace venture-specific subsets with query scripts
  - Create REPO-QUERY-FILTER.py to extract repos by:
    - venture_id
    - category
    - capabilities
  - Update HRMS/REPO_REGISTRY.json to be generated from main registry
  - Update Automations/REPO_REGISTRY.json to be generated from main registry
```

**Result:** Single source of truth (REPOSITORY-REGISTRY.json) with 1 markdown index

---

## CRITICAL OVERLAP #2: INDEX MASTERS (8 FILES → 3)

### Current State: 8 overlapping index files

| Index Type | Files | Consolidation |
|------------|-------|----------------|
| **General Indexes** | 00-MASTER-INDEX.md, MASTER-INDEX.md, 000-OBSIDIAN-MASTER-INDEX.md | → **MASTER-INDEX.md** (single entry point) |
| **Resource Indexes** | COMPLETE-RESOURCE-INDEX.md, DASHBOARD-INDEX.md, ARTIFACT-INDEX.md | → **RESOURCE-INVENTORY.md** |
| **Session/Temporal** | SESSION-INDEX-2026-06-11.md (archive when session ends) | → Archive old sessions |

### Action Plan
```
WEEK 1: Consolidate into 3 masters
  ✅ MASTER-INDEX.md (CEO Command Center entry point)
     - Links to all 4 hubs (STRATEGY, INFRASTRUCTURE, VENTURES, REFERENCE)
     - Links to resource inventory
     - Links to architecture

  ✅ RESOURCE-INVENTORY.md (all artifacts, dashboards, artifacts)
     - Dashboards: Obsidian, ClickUp, DuckDB
     - Artifacts: generated files, exports
     - Collections: datasets, templates

  ✅ ARCHIVE/ (old sessions, dated indexes)
     - SESSION-INDEX-2026-06-11.md
     - Old dashboard snapshots

WEEK 2: Delete duplicate masters
  ❌ 00-MASTER-INDEX.md
  ❌ 000-OBSIDIAN-MASTER-INDEX.md
  ❌ COMPLETE-RESOURCE-INDEX.md
  ❌ DASHBOARD-INDEX.md
  ❌ ARTIFACT-INDEX.md
```

---

## CRITICAL OVERLAP #3: ARCHITECTURE MASTERS (5 FILES → 1)

### Current State: 5 overlapping architecture/structure files

| File | Purpose | Status |
|------|---------|--------|
| MASTER-FOLDER-STRUCTURE.md | Folder hierarchy | 🔄 Duplicate |
| MASTER-FOLDER-MAP.md | Folder map | 🔄 Duplicate |
| COS-MASTER-ARCHITECTURE.md | Civilization OS | 🔄 Duplicate |
| MASTER-OS-ARCHITECTURE-AND-GAPS.md | OS gaps analysis | 🔄 Duplicate |
| STRUCTURE-INDEX.md | Structure reference | 🔄 Index |

### Action Plan
```
WEEK 1: Merge into unified MASTER-ARCHITECTURE.md
  ✅ New file: MASTER-ARCHITECTURE.md
     - 4-layer structure (STRATEGY, INFRASTRUCTURE, VENTURES, REFERENCE)
     - Folder hierarchy with purpose
     - Cross-references to all hubs
     - Gaps analysis section
     - Tech stack by layer

WEEK 2: Delete redundant files
  ❌ MASTER-FOLDER-STRUCTURE.md
  ❌ MASTER-FOLDER-MAP.md
  ❌ COS-MASTER-ARCHITECTURE.md
  ❌ MASTER-OS-ARCHITECTURE-AND-GAPS.md
  ❌ STRUCTURE-INDEX.md (superseded by MASTER-ARCHITECTURE.md)
```

---

## OVERLAP #4: TASK/WORKFLOW MASTERS (5+ FILES → 1 CURRENT)

### Current State: 5+ task/workflow masters

| File | Purpose | Status |
|------|---------|--------|
| TODO-MASTER-CHECKLIST.md | Task checklist | ⚠️ May be old |
| COMPLETE-MASTER-PLAYBOOK.md | Execution playbook | ⚠️ May be old |
| MIGRATION-MASTER-PLAN.md | Migration steps | ⚠️ May be old |
| WAVE_FINAL_MASTER_PREP.md | Wave execution | ⚠️ Dated |
| ORB-MASTER-CONNECTOR-2026-06-11.md | ORB connector | ✅ Current |

### Action Plan
```
WEEK 1: Keep current, archive old
  ✅ Keep whichever is most recent/complete
     Likely candidates: COMPLETE-MASTER-PLAYBOOK.md or ORB-MASTER-CONNECTOR

  🗄️ Archive old versions to /archive/:
     - TODO-MASTER-CHECKLIST.md (if superseded)
     - WAVE_FINAL_MASTER_PREP.md
     - Any dated playbooks
```

---

## OVERLAP #5: VENTURE/PROJECT MASTERS (3 FILES)

### Current State: 3 venture-specific masters

| File | Focus | Status |
|------|-------|--------|
| 712-VENTURE-WORKFORCE-PLANNING-MASTER.md | Staffing for 712 ventures | ⚠️ Check if current |
| CONSTRUCTION-SECTOR-BANKABILITY-MASTER.md | Construction sector | ⚠️ Check if current |
| SECTOR_FUNDING_STAFFING_MASTER_PLAN.md | Sector-level planning | ⚠️ Check if current |

### Recommendation
```
ACTION: Verify which are current vs archived
  - If all current: keep all 3 (sector-specific)
  - If overlapping: consolidate to 1 VENTURES-MASTER-PLAN.md
```

---

## OVERLAP #6: REGISTRY/AGENT MASTERS (4 FILES)

### Current State: Agent/operation registries

| File | Purpose | Status |
|------|---------|--------|
| MASTER_AGENT_REGISTRY.md | Agent registry | ⚠️ Check freshness |
| DECISION-RECORD-REGISTRY.md | Decisions made | ⚠️ Check freshness |
| MASTER-AGENT-SPEC.md | Agent specifications | ⚠️ Check freshness |
| AI-BOSS-HOLDINGS-REPO-OS-INDEX.md | Holdings OS index | ⚠️ Check freshness |

### Recommendation
```
ACTION: Verify which are authoritative vs duplicates
  - Consolidate overlapping agent registries
  - Keep decision registry separate (audit trail)
```

---

## CONSOLIDATION SUMMARY

### Files to DELETE (archive to /archive/)
```
❌ MASTER-REPO-REGISTRY.csv
❌ MASTER_REPO_REGISTRY_COMPLETE.csv
❌ venture-hub/REPO_REGISTRY.json (if empty)
❌ 00-MASTER-INDEX.md
❌ 000-OBSIDIAN-MASTER-INDEX.md
❌ COMPLETE-RESOURCE-INDEX.md
❌ DASHBOARD-INDEX.md
❌ ARTIFACT-INDEX.md
❌ MASTER-FOLDER-STRUCTURE.md
❌ MASTER-FOLDER-MAP.md
❌ COS-MASTER-ARCHITECTURE.md
❌ MASTER-OS-ARCHITECTURE-AND-GAPS.md
❌ STRUCTURE-INDEX.md
❌ TODO-MASTER-CHECKLIST.md (if superseded)
❌ WAVE_FINAL_MASTER_PREP.md
```

**Total: 15 files to archive**

### Files to KEEP (unified masters)
```
✅ REPOSITORY-REGISTRY.json (1,592 repos - Phase 2 complete)
✅ GITHUB-REPOSITORIES-MASTER-LIST.md (human-readable index)
✅ MASTER-INDEX.md (CEO Command Center entry point)
✅ RESOURCE-INVENTORY.md (NEW - consolidated dashboards/artifacts)
✅ MASTER-ARCHITECTURE.md (NEW - unified folder structure)
✅ COMPLETE-MASTER-PLAYBOOK.md (or most current equivalent)
✅ SECTOR_FUNDING_STAFFING_MASTER_PLAN.md (venture-specific, keep if current)
✅ ORB-MASTER-CONNECTOR-2026-06-11.md (current ORB connector)
✅ MASTER_AGENT_REGISTRY.md (if authoritative)
✅ DECISION-RECORD-REGISTRY.md (audit trail - keep)
```

**Total: 10 unified masters**

---

## EXECUTION TIMELINE

### WEEK 1 (Immediate)
- [ ] Archive 15 outdated files to `/archive/`
- [ ] Create RESOURCE-INVENTORY.md (consolidate dashboards)
- [ ] Create MASTER-ARCHITECTURE.md (consolidate structure files)

### WEEK 2 (Quick merge)
- [ ] Verify venture-specific masters are still current
- [ ] Create REPO-QUERY-FILTER.py for dynamic registry filtering
- [ ] Update venture-specific REPO_REGISTRY.json files to reference main

### WEEK 3 (Verification)
- [ ] Test that unified masters work in Obsidian
- [ ] Verify all cross-references are valid
- [ ] Update MEMORY.md index to point to new unified masters

---

## IMPACT

**Before Consolidation:**
- 71 master indexes scattered across 40+ locations
- 7 overlapping repository registries (confusing, outdated copies)
- 8 overlapping index files (hard to find things)
- 5 overlapping architecture files (contradictory information)

**After Consolidation:**
- 10 unified masters in logical locations
- Single source of truth for repositories (REPOSITORY-REGISTRY.json)
- Clear entry point (MASTER-INDEX.md)
- Unified architecture view (MASTER-ARCHITECTURE.md)
- 15 archived files for historical reference

---

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
