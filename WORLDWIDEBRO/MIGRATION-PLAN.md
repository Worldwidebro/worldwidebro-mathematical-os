# WORLDWIDEBRO Migration Plan
**Date:** 2026-08-04  
**Goal:** Consolidate scattered folders into canonical structure

---

## Current State Audit

### Numbered Folders (Existing)
- `02_PROJECTS/` — old structure at root
- `WORLDWIDEBRO/[00-20,99]/` — new structure (just created)

### OS/System Folders (To Migrate)
| Current | Target | Reason |
|---------|--------|--------|
| `AI-BOSS/` | `WORLDWIDEBRO/06_AGENTS/EXECUTIVE/` + `WORLDWIDEBRO/10_DECISION-ENGINE/` | Orchestration layer |
| `AI-BRAIN/` | `WORLDWIDEBRO/05_AI-BRAIN/` | Knowledge/intelligence layer |
| `iza-os-*` (3 variants) | `WORLDWIDEBRO/05_AI-BRAIN/` + aliases | Intelligence layer |
| `knowledge-graph-os/` | `WORLDWIDEBRO/05_AI-BRAIN/GRAPH/` | Graph DB layer |
| `vex/` | `WORLDWIDEBRO/14_BUSINESS/VEX/` | Marketplace interface |
| `vex-api/` | `WORLDWIDEBRO/03_PORTFOLIOS/SOFTWARE-IP/VEX-API/` | API code |
| `vex-engine/` | `WORLDWIDEBRO/03_PORTFOLIOS/SOFTWARE-IP/VEX-ENGINE/` | Core engine |
| `vex-hero-site/` | `WORLDWIDEBRO/03_PORTFOLIOS/SOFTWARE-IP/VEX-HERO-SITE/` | Marketing site |

### Venture Folders (To Organize)
| Current | Target | Sector |
|---------|--------|--------|
| `con-001-ace-construction/` | `WORLDWIDEBRO/15_INDUSTRIES/CONSTRUCTION/CON-001/` | Construction (CON) |
| `ops-staff-001-staffing/` | `WORLDWIDEBRO/15_INDUSTRIES/STAFFING/STA-001/` | Staffing (STA) |
| `FIN-037-AUTOMATED-TRADING-SYSTEM/` | `WORLDWIDEBRO/15_INDUSTRIES/FINANCIAL/FIN-037/` | Finance (FIN) |
| `mc-006-video-production-company/` | `WORLDWIDEBRO/15_INDUSTRIES/MEDIA/MC-006/` | Media (MC) |
| `realestate-os/` | `WORLDWIDEBRO/15_INDUSTRIES/REAL-ESTATE/RE-001/` | Real Estate (RE) |
| `family-office-os/` | `WORLDWIDEBRO/14_BUSINESS/HOLDING-COMPANY/` | Holding structure |
| Other venture folders | `WORLDWIDEBRO/03_PORTFOLIOS/BUSINESS/` or by sector | Generic portfolio |

### Planning/Documentation (To Archive)
| Current | Target |
|---------|--------|
| `.planning/` | `WORLDWIDEBRO/20_DOCS/RESEARCH/PLANNING/` |
| `.obsidian/` | Keep at root (Obsidian vault settings) |
| Scattered MD files | `WORLDWIDEBRO/20_DOCS/RESEARCH/CHAT-DERIVED/` |

### External/Don't Move
| Folder | Reason |
|--------|--------|
| `.claude/` | Global Claude config (stays at root) |
| `.git/` | Git metadata (stays at root) |
| `.venv-*` | Python virtualenvs (can be rebuilt) |
| `node_modules/` | Dependency folders (can be rebuilt) |

---

## Migration Strategy

### Phase 1: Create Aliases (Non-Destructive)
Don't delete old folders yet. Create symlinks in `99_ARCHIVE/OLD-NAMES/` pointing to new locations.

```bash
cd WORLDWIDEBRO/99_ARCHIVE/OLD-NAMES/
ln -s ../../06_AGENTS/EXECUTIVE/AI-BOSS AI-BOSS
ln -s ../../05_AI-BRAIN AI-BRAIN
ln -s ../../05_AI-BRAIN/KNOWLEDGE IZA-OS
ln -s ../../14_BUSINESS/VEX VEX
```

This allows:
- Old code paths to still work
- Git submodules to still find modules
- No disruption while we verify new paths work

### Phase 2: Create Canonical Locations
Build the new folder structure and populate it with actual content from old locations.

### Phase 3: Update Git References
Update any hard-coded paths in code/config to point to new canonical locations.

### Phase 4: Archive Old Folders
Move original folders to `99_ARCHIVE/` once migration is verified.

---

## Mapping: What Goes Where

### WORLDWIDEBRO/00_IDENTITY/
```
COMPANY.md → Worldwidebro Holdings
PURPOSE.md → Why the company exists
MISSION.md → What we're trying to achieve
VISION.md → Where we're going
VALUES.md → What we believe
PRINCIPLES.md → How we operate
CULTURE.md → Organizational norms
LEGACY.md → History of AI-BOSS, IZA-OS, etc.
BRANDS.md → VEX, AVS, CIVILIZATION-OS
ALIASES.md → Map all names to canonical entities
```

### WORLDWIDEBRO/01_DIRECTIVES/
```
CURRENT/ → Active strategies, directives, policies
COMPANY/ → Company-level strategy
INVESTMENT/ → Capital allocation
PRODUCT/ → Product strategy
ENGINEERING/ → Technical standards
OPERATIONS/ → Operational procedures
```

### WORLDWIDEBRO/03_PORTFOLIOS/SOFTWARE-IP/
```
vex-api/ (from vex-api/)
vex-engine/ (from vex-engine/)
vex-hero-site/ (from vex-hero-site/)
[all other repos with code]
```

### WORLDWIDEBRO/05_AI-BRAIN/
```
GRAPH/ → Neo4j schema, queries
KNOWLEDGE/ → Documents, sources, claims
MEMORY/ → Short/long term memory structures
VECTOR/ → Qdrant collections, embeddings
CONTEXT/ → Context retrieval strategies
AWARENESS/ → 12-layer awareness dashboards
DATA-QUALITY/ → Freshness, duplicates, orphans
```

(Merge contents of `AI-BRAIN/`, `iza-os-*`, `knowledge-graph-os/`)

### WORLDWIDEBRO/06_AGENTS/EXECUTIVE/
```
orchestration/ → Decision logic (from AI-BOSS/)
routing/ → Capability routing
priority/ → Prioritization logic
```

### WORLDWIDEBRO/14_BUSINESS/
```
HOLDING-COMPANY/ → Corporate structure
VEX/ → Marketplace (from vex/)
CUSTOMERS/ → Customer management
SALES/ → Sales processes
REVENUE/ → Revenue tracking
```

### WORLDWIDEBRO/15_INDUSTRIES/
```
CONSTRUCTION/
  └─ CON-001/ (from con-001-ace-construction/)
STAFFING/
  └─ STA-001/ (from ops-staff-001-staffing/)
FINANCIAL/
  └─ FIN-037/ (from FIN-037-AUTOMATED-TRADING-SYSTEM/)
REAL-ESTATE/
  └─ RE-001/ (from realestate-os/)
MEDIA/
  └─ MC-006/ (from mc-006-video-production-company/)
TECHNOLOGY/
  └─ [tech ventures]
MARKETPLACE/
  └─ [marketplace ventures]
```

### WORLDWIDEBRO/20_DOCS/RESEARCH/
```
CHAT-DERIVED/ → Outputs from this chat
PLANNING/ → Contents of .planning/
ARCHITECTURE/ → System design docs
```

### WORLDWIDEBRO/99_ARCHIVE/OLD-NAMES/
```
AI-BOSS → symlink to 06_AGENTS/EXECUTIVE/
AI-BRAIN → symlink to 05_AI-BRAIN/
IZA-OS → symlink to 05_AI-BRAIN/
VEX → symlink to 14_BUSINESS/VEX/
[old git repos before cleanup]
```

---

## Execution Checklist

- [ ] **Phase 1: Create root README and CLAUDE.md**
  - [ ] WORLDWIDEBRO/README.md (what is this system?)
  - [ ] WORLDWIDEBRO/CLAUDE.md (operating constitution)
  - [ ] WORLDWIDEBRO/ONTOLOGY.md (canonical vocabulary)
  - [ ] WORLDWIDEBRO/ROADMAP.md (four phases)
  - [ ] WORLDWIDEBRO/SYSTEM-MAP.md (ASCII architecture)

- [ ] **Phase 2: Move high-value content**
  - [ ] Move 02_PROJECTS/ → WORLDWIDEBRO/04_PROJECTS/ACTIVE/
  - [ ] Move AI-BOSS/ → WORLDWIDEBRO/06_AGENTS/ + WORLDWIDEBRO/10_DECISION-ENGINE/
  - [ ] Move AI-BRAIN/ → WORLDWIDEBRO/05_AI-BRAIN/
  - [ ] Move IZA-OS variants → WORLDWIDEBRO/05_AI-BRAIN/
  - [ ] Move VEX variants → WORLDWIDEBRO/14_BUSINESS/VEX/ + WORLDWIDEBRO/03_PORTFOLIOS/SOFTWARE-IP/
  - [ ] Move ventures → WORLDWIDEBRO/15_INDUSTRIES/[SECTOR]/

- [ ] **Phase 3: Organize planning docs**
  - [ ] Move .planning/ → WORLDWIDEBRO/20_DOCS/RESEARCH/PLANNING/
  - [ ] Extract chat output → WORLDWIDEBRO/20_DOCS/RESEARCH/CHAT-DERIVED/

- [ ] **Phase 4: Create aliases**
  - [ ] Symlink old paths → new canonical locations
  - [ ] Verify git submodules still resolve

- [ ] **Phase 5: Create catalogues**
  - [ ] WORLDWIDEBRO/03_PORTFOLIOS/SOFTWARE-IP/REPOSITORY-CATALOG.md
  - [ ] WORLDWIDEBRO/15_INDUSTRIES/VENTURE-CATALOG.md
  - [ ] WORLDWIDEBRO/06_AGENTS/AGENT-CATALOG.md
  - [ ] WORLDWIDEBRO/07_SKILLS/SKILL-CATALOG.md
  - [ ] WORLDWIDEBRO/08_MCP/MCP-CATALOG.md

- [ ] **Phase 6: Create observability**
  - [ ] Dashboard 01 (World) spec
  - [ ] Dashboard 02 (CEO) spec
  - [ ] Dashboard 03 (Business) spec
  - [ ] ...through 10

- [ ] **Phase 7: Verification**
  - [ ] All links working
  - [ ] All imports resolving
  - [ ] Git history intact
  - [ ] No data loss

---

## Rationale: Why This Structure

| Decision | Why |
|----------|-----|
| **WORLDWIDEBRO is canonical root** | Single identity prevents fragmentation |
| **15_INDUSTRIES by sector** | Aligns with economic reality (LT, FIN, CON, RE) |
| **03_PORTFOLIOS as views** | 17 lenses over same world, not duplicate systems |
| **05_AI-BRAIN unified** | Merge AI-BOSS, IZA-OS, VEX into one nervous system |
| **Aliases in 99_ARCHIVE** | Non-breaking migration path |
| **20_DOCS/RESEARCH/CHAT-DERIVED** | Preserve knowledge extracted from conversations |
| **18_OBSERVABILITY separate** | 10 dashboards serve specific audiences |

---

## Success Criteria

✅ All content discoverable from WORLDWIDEBRO/  
✅ No duplicate systems (one world model, many views)  
✅ Aliases allow old paths to work  
✅ Catalogues show what exists where  
✅ CLAUDE.md governs the structure  
✅ ROADMAP.md defines next 4 phases  
✅ Git history preserved  
