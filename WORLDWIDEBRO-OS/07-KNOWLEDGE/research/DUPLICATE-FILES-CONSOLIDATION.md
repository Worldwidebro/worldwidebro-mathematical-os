# Duplicate & Overlapping Files Audit (2026-06-13)

**Status:** 65+ overlapping files identified  
**Action:** Consolidate before OPTION 3 execution  
**Timeline:** Before Week 1 starts

---

## 🔴 CRITICAL DUPLICATES (Must Consolidate)

### 1. Multiple "MASTER" Indexes
| File | Purpose | Status | Action |
|------|---------|--------|--------|
| `00-MASTER-INDEX.md` | ORB references | ACTIVE | Keep (use as primary) |
| `civilization-os-local/MASTER-FOLDER-MAP.md` | Folder organization | DUPLICATE | Archive |
| `WORLDWIDEBRO-UNIFIED-OS/TODO-MASTER-CHECKLIST.md` | Todo tracking | DUPLICATE | Archive |
| `ORB-MASTER-CONNECTOR-2026-06-11.md` | ORB references | DUPLICATE | Merge into 00-MASTER-INDEX |

**Action:** Consolidate into `00-MASTER-INDEX.md` as single source of truth

---

### 2. Multiple "ROADMAP" Files (30+ versions)
| Category | Count | Primary File | Duplicates | Action |
|----------|-------|--------------|-----------|--------|
| BANKABILITY ROADMAP | 20 | `CON-009-ROOFING-COMPANY-BANKABILITY-ROADMAP.md` | CON-001 through CON-020 | Archive (use CSV instead) |
| COMPLETION ROADMAP | 2 | `COMPLETION-PHASES-ROADMAP.md` | `WORLDWIDEBRO-UNIFIED-OS/...` | Keep COMPLETION-PHASES, delete duplicate |
| EXECUTION ROADMAP | 2 | `EXECUTION-ROADMAP-30-DAYS.md` | `Influence-Venture-Business-OS/.../EXECUTION_ROADMAP_FULL.md` | Keep 30-DAYS (more recent) |
| UNIFIED ROADMAP | 1 | `WORLDWIDEBRO-UNIFIED-COMPANY-ROADMAP-2026.md` | None | Keep (definitive) |

**Action:** Delete 20 individual CON roadmaps, consolidate into single sector roadmap CSV

---

### 3. Multiple "REPOSITORY" Registries (6 versions)
| File | Format | Size | Status | Action |
|------|--------|------|--------|--------|
| `Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json` | JSON | 904KB | DEFINITIVE | Keep |
| `civilization-os-local/REPO_REGISTRY.json` | JSON | ? | DUPLICATE | Delete |
| `WORLDWIDEBRO-OS/REGISTRIES/repository_registry_pilot.csv` | CSV | ? | DUPLICATE | Delete |
| `tech_ventures_registry.csv` | CSV | ? | OUTDATED | Delete |

**Action:** Single source: `REPOSITORY-REGISTRY.json`

---

### 4. Multiple "VENTURE" Mappings (8+ versions)
| File | Contains | Status | Action |
|------|----------|--------|--------|
| `.planning/venture-hub-alignment.json` | Supabase-exported | ACTIVE | Keep (automated) |
| `Influence-Venture-Business-OS/VENTURES/VENTURES-HUB.md` | Hub reference | REFERENCE | Keep |
| `MC-OPERATIONS/config/ventures.json` | Legacy config | OLD | Delete |
| `The office/ventures.json` | Legacy config | OLD | Delete |
| `VENTURE-HANDLE-MAP.json` | Active mapping | DEFINITIVE | Keep |
| `pitch-kit/data/venture_registry.json` | Template data | TEMPLATE | Keep |

**Action:** 3 keep, 2 delete, consolidate metadata

---

### 5. Multiple "STRATEGY" Files (9 files)
| Strategy | File | Status | Action |
|----------|------|--------|--------|
| OVERALL | `CONSOLIDATION-STRATEGY.md` | ACTIVE | Keep |
| CHANNEL | `FACELESS-CHANNELS-STRATEGY.md` | ACTIVE | Keep |
| APPLICATION | `ANISSA-APPLICATION-STRATEGY.md` | PERSONAL | Archive |
| JOB MATCHING | `ANISSA-JOB-MATCHING-STRATEGY.md` | PERSONAL | Archive |
| CAPITAL | `WORLDWIDEBRO-UNIFIED-OS/CAPITAL-TARGETING-STRATEGY.md` | DUPLICATE | Merge into CONSOLIDATION-STRATEGY |
| REPOSITORY | `Influence-Venture-Business-OS/REFERENCE/REPO-LAYER-STRATEGY.md` | REFERENCE | Keep |

**Action:** Archive 2 personal, merge capital strategy into consolidation

---

## 🟡 MEDIUM PRIORITY (Clean Up After Week 1)

### Multiple "PLAN" Files (25 versions)
- 03-30-DAY-CASH-FLOW-PLAN.md ✅ (needed for OPTION 1)
- 712-VENTURE-WORKFORCE-PLANNING-MASTER.md (old)
- PLANE-INTEGRATION-task_plan.md (integration test, archive)
- Multiple task_plan.md files in subdirectories (archive)

**Action:** Delete task_plan.md files, keep high-level 30-DAY-CASH-FLOW-PLAN

---

### Multiple "CHECKLIST" Files (14 versions)
- PHASE-1-ENTITY-FORMATION-CHECKLIST.md ✅ (keep)
- CLIP-FARMING-CHECKLIST.md ✅ (keep)
- EDUCATION-TECH-STACK-CHECKLIST.md (archive)
- AGENTIC-INBOX-IMPLEMENTATION-CHECKLIST.md (old)

**Action:** Keep 2, archive 12

---

## 🟢 LOW PRIORITY (Informational Only)

- Individual CON-001 through CON-020 bankability roadmaps (use CSV index instead)
- Re-001, RE-002 venture files (template)
- Integration test reports (PLANE, SKILLSLLM)
- Legacy automation documentation

---

## Consolidated Structure (Post-Cleanup)

```
/Users/acebless/Documents/
├── 00-MASTER-INDEX.md (single source of truth for references)
├── WORLDWIDEBRO-UNIFIED-COMPANY-ROADMAP-2026.md (12-month plan)
├── EXECUTION-ROADMAP-30-DAYS.md (current execution plan)
├── COMPLETION-PHASES-ROADMAP.md (6-phase model)
├── CONSOLIDATION-STRATEGY.md (strategic direction)
├── FACELESS-CHANNELS-STRATEGY.md (content strategy)
├── OPTION-3-ECOSYSTEM-MAPPING-TASKS.md (ACTIVE)
├── OPTION-1-CLARITY-ANALYSIS-TASKS.md (ACTIVE)
├── OPTION-2-LAUNCH-MACHINE-TASKS.md (ACTIVE)
├── 03-30-DAY-CASH-FLOW-PLAN.md
├── PHASE-1-ENTITY-FORMATION-CHECKLIST.md
├── CLIP-FARMING-CHECKLIST.md
├── Influence-Venture-Business-OS/
│   ├── REFERENCE/REPOSITORY-REGISTRY.json (definitive)
│   ├── INFRASTRUCTURE_LAYERS/REPOSITORY-INTELLIGENCE-SYSTEM.md
│   ├── INFRASTRUCTURE_LAYERS/venture-hub/
│   └── VENUES/VENTURES-HUB.md
├── .planning/
│   ├── venture-hub-alignment.json (auto-synced from Supabase)
│   └── graph-data.json (auto-synced)
└── archive/ (moved here)
    ├── old-roadmaps/
    ├── old-registries/
    └── integration-tests/
```

---

## Action Plan (For After OPTION 3 Week 1)

### Immediate (Do NOT do during OPTION 3)
- Keep all current files (don't break anything)

### After Week 1 (Friday Jun 13 EOD)
1. Create `/Users/acebless/Documents/archive/` folder
2. Move 20 CON-XXX roadmaps to archive
3. Delete 4 old registry files (keep REPOSITORY-REGISTRY.json only)
4. Delete MC-OPERATIONS/config/ventures.json
5. Delete The office/ventures.json
6. Update 00-MASTER-INDEX.md with consolidated references
7. Delete 12 old checklist files

### After Week 2 (Friday Jun 20 EOD)
- Delete old PLANE integration files
- Delete old SKILLSLLM integration files
- Archive old task_plan.md files

### Ongoing
- Single source for each category:
  - Roadmap: `WORLDWIDEBRO-UNIFIED-COMPANY-ROADMAP-2026.md`
  - Registry: `REPOSITORY-REGISTRY.json`
  - Venture mapping: `VENTURE-HANDLE-MAP.json` + auto-synced JSON
  - Tasks: `OPTION-X-*.md` files

---

## Don't Touch These (Critical Path)

- `WORLDWIDEBRO-UNIFIED-COMPANY-ROADMAP-2026.md` ✅
- `EXECUTION-ROADMAP-30-DAYS.md` ✅
- `OPTION-3-ECOSYSTEM-MAPPING-TASKS.md` ✅
- `OPTION-1-CLARITY-ANALYSIS-TASKS.md` ✅
- `OPTION-2-LAUNCH-MACHINE-TASKS.md` ✅
- `Influence-Venture-Business-OS/REFERENCE/REPOSITORY-REGISTRY.json` ✅
- `VENTURE-HANDLE-MAP.json` ✅
- `.planning/venture-hub-alignment.json` ✅

---

**Status:** Analysis complete. Ready for OPTION 3 execution. Archive cleanup after Week 1.

