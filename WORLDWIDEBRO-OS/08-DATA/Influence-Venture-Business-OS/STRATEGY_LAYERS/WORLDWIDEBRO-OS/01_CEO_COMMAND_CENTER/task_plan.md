# Task: Organize Ventures & Repos Registry

**Goal:** Consolidate 712 ventures and their repo mappings into a single unified source of truth.

**Status:** In Progress (Phase 1)

---

## Phases

### Phase 1: Audit Current State ✅
- [x] Map actual venture folders (9 in WORLDWIDEBRO-OS/10_VENTURES/)
- [x] Identify scattered ventures (con-001, bw-001, venture-factory-core at root)
- [x] Identify client work (YES-LLC-CONTRACTOR-DELIVERY = Wave rideshare)
- [x] Count repos in /integrations/ (8 core)
- [x] Find data files (multiple CSVs with different schemas)

### Phase 2: Consolidate Venture Folders (NEXT)
- [ ] Move `con-001-ace-construction/` → `WORLDWIDEBRO-OS/10_VENTURES/Operations_Ventures/`
- [ ] Move `bw-001-lash-extension-studio/` → `WORLDWIDEBRO-OS/10_VENTURES/SaaS_Ventures/`
- [ ] Investigate `venture-factory-core/`
- [ ] Create `WORLDWIDEBRO-OS/00_CLIENT_WORK/`
- [ ] Move `YES-LLC-CONTRACTOR-DELIVERY/` → `WORLDWIDEBRO-OS/00_CLIENT_WORK/YES-LLC-Wave-Rideshare/`

### Phase 3: Find & Use Venture-Repo Linkage CSV (PENDING)
- [ ] Locate venture-repo linkage CSV
- [ ] Map ventures to repos
- [ ] Create consolidated mapping file

### Phase 4: Create Master Registry (PENDING)
- [ ] ventures-repos-map.json
- [ ] repos-registry.json
- [ ] ventures-master.json

---

## Decisions

**Structure:**
```
WORLDWIDEBRO-OS/
├── 00_CLIENT_WORK/ (← NEW)
│   └── YES-LLC-Wave-Rideshare/
└── 10_VENTURES/
    ├── Operations_Ventures/
    └── SaaS_Ventures/
```
