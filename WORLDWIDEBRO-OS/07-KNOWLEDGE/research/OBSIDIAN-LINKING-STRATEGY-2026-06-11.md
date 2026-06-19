# Obsidian Linking Strategy — Connecting 150 Orphaned Files

**Purpose:** Fix the knowledge graph by linking scattered analysis/strategy files to canonical references.

**Current State:** 150+ files with ZERO [[links]] — knowledge graph is broken.

---

## CANONICAL REFERENCE FILES (The 4 Hubs)

Every new file should link back to one of these:

### 🏛️ STRATEGIC HUB
Reference these for ventures, sectors, roadmaps:
- **sector-taxonomy-31.md** — 31-sector classification
- **holding-company-100m-roadmap.md** — $100M structure (6 stages)
- **completion-phases.md** — Phases A-F roadmap
- **unified-os-architecture.md** — 7-layer system

### 📊 OPERATIONAL HUB
Reference these for execution, loops, automation:
- **LOOPS-SKILLS-ALIGNMENT-VENTURES.md** — Master loop config
- **venture-loops-framework.md** — 4-stage automation
- **WORLDWIDEBRO-OS/01_CEO_COMMAND_CENTER** — Strategic planning

### 🧠 KNOWLEDGE HUB
Reference these for context, memory, structure:
- **MEMORY.md** — Persistent context index
- **FILE-STRUCTURE-MAP-2026-06-11.md** — Folder organization
- **DATA-SOURCES.md** — Where all data lives
- **KNOWLEDGE-GRAPH-DASHBOARD.md** — Obsidian Dataview blocks

### 🔗 DATA HUB
Reference these for ventures, repos, sectors:
- **VENTURE-HANDLE-MAP.json** — All 712 venture handles
- **WORLDWIDEBRO-OS/08_RESEARCH/Ventures-Data** — Master data layer
- **worldwidebro-vault** — Knowledge vault

---

## LINKING RULES BY CATEGORY

### 📈 ANALYSIS FILES (9 files)
**Always link to:** [[DATA-SOURCES.md]], [[sector-taxonomy-31.md]], [[FILE-STRUCTURE-MAP-2026-06-11.md]]

- HRMS-Competitor-Analysis.md → [[sector-taxonomy-31]], [[DATA-SOURCES]]
- construction_analysis.md → [[sector-taxonomy-31]], [[WORLDWIDEBRO-OS/04_SECTORS]]
- full_duplication_analysis.md → [[DATA-SOURCES]], [[MEMORY]]

---

### 🎯 STRATEGY FILES (27 files)
**Always link to:** [[holding-company-100m-roadmap.md]], [[venture-loops-framework.md]], [[completion-phases.md]]

- CON-011-ELECTRICAL-SERVICES-BANKABILITY-ROADMAP.md → [[venture-loops-framework]], [[sector-taxonomy-31]]
- LOOPS-IMPLEMENTATION-ROADMAP.md → [[LOOPS-SKILLS-ALIGNMENT-VENTURES]], [[completion-phases]]
- YES-LLC-STRUCTURE-BLUEPRINT.md → [[holding-company-100m-roadmap]], [[unified-os-architecture]]

---

### ✅ OPERATIONAL FILES (11 files)
**Always link to:** [[LOOPS-SKILLS-ALIGNMENT-VENTURES.md]], [[completion-phases.md]], [[WORLDWIDEBRO-OS/01_CEO_COMMAND_CENTER]]

- MCP-CONFIG-CLEANUP-CHECKLIST.md → [[LOOPS-SKILLS-ALIGNMENT-VENTURES]]
- CLIP-FARMING-CHECKLIST.md → [[venture-loops-framework]]
- PHASE-B-BUILD-CHECKLIST.md → [[completion-phases]]

---

### ⚙️ TECHNICAL FILES (21 files)
**Always link to:** [[unified-os-architecture.md]], [[DATA-SOURCES.md]], [[system-architecture.md]]

- NOTION-OS-INTEGRATION-GUIDE.md → [[DATA-SOURCES]], [[LOOPS-SKILLS-ALIGNMENT-VENTURES]]
- SYSTEM_EXECUTION_READINESS.md → [[unified-os-architecture]], [[completion-phases]]

---

### 🎓 FRAMEWORK FILES (72 files)
**Always link to:** [[sector-taxonomy-31.md]], [[holding-company-100m-roadmap.md]]

- AZRIEL-TESTBED-FRAMEWORK.md → [[holding-company-100m-roadmap]], [[completion-phases]]
- DATA-SOURCES.md → [[MEMORY.md]], [[FILE-STRUCTURE-MAP-2026-06-11.md]]
- EMPIRE-ALIGNMENT-MAP.md → [[holding-company-100m-roadmap]], [[sector-taxonomy-31]]

---

## CLAUDE.MD UPDATES NEEDED

Add this new section after line 67 (Storage Hierarchy):

```markdown
# File Creation Guidelines — Obsidian Linking

When creating ANY new markdown file, link it to the canonical reference hubs. 
This prevents orphaned files and keeps the knowledge graph connected.

## The 4 Canonical Hubs (Always Reference One)

1. **Strategic Hub** → sector-taxonomy-31.md, holding-company-100m-roadmap.md, completion-phases.md
2. **Operational Hub** → LOOPS-SKILLS-ALIGNMENT-VENTURES.md, venture-loops-framework.md, WORLDWIDEBRO-OS/01_CEO_COMMAND_CENTER
3. **Knowledge Hub** → MEMORY.md, FILE-STRUCTURE-MAP-2026-06-11.md, DATA-SOURCES.md
4. **Data Hub** → VENTURE-HANDLE-MAP.json, WORLDWIDEBRO-OS/08_RESEARCH/Ventures-Data

## Required Header for Every New File

```yaml
---
references:
  - [[canonical-hub-1]]
  - [[canonical-hub-2]]
  - [[specific-venture-or-sector-if-applicable]]
---
```

## Decision Tree Before Creating a File

- **Sector-specific?** Link to [[sector-taxonomy-31]]
- **About loops/automation?** Link to [[venture-loops-framework]] + [[LOOPS-SKILLS-ALIGNMENT-VENTURES]]
- **Strategic/roadmap?** Link to [[holding-company-100m-roadmap]] + [[completion-phases]]
- **System architecture?** Link to [[unified-os-architecture]]
- **Data/research?** Link to [[DATA-SOURCES]] + [[FILE-STRUCTURE-MAP-2026-06-11]]
- **Operational/checklist?** Link to [[WORLDWIDEBRO-OS/01_CEO_COMMAND_CENTER]]

## Result

Before: Orphaned file, 0 connections, undiscoverable
After: Linked file, 3+ connections, discoverable from hub

Example newly linked file header:
```
---
references:
  - [[venture-loops-framework]]
  - [[sector-taxonomy-31]]
  - [[completion-phases]]
---

# CON-011 Electrical Services Roadmap

This roadmap implements the [[venture-loops-framework]] stages...
```
```

---

## EXECUTION: Link Existing 150 Files

Create a batch linking script:

```bash
#!/bin/bash

# For each category, add reference header + 2-3 [[links]] in intro

# ANALYSIS FILES (9)
for file in HRMS-Competitor-Analysis.md construction_analysis.md full_duplication_analysis.md; do
  # Add to top: references: [[DATA-SOURCES]], [[sector-taxonomy-31]]
done

# STRATEGY FILES (27)
for file in CON-011-*.md LOOPS-Implementation-Roadmap.md YES-LLC-Structure-Blueprint.md; do
  # Add to top: references: [[venture-loops-framework]], [[completion-phases]]
done

# OPERATIONAL FILES (11)
for file in *-CHECKLIST.md; do
  # Add to top: references: [[LOOPS-SKILLS-ALIGNMENT-VENTURES]]
done

# TECHNICAL FILES (21)
for file in NOTION-OS-*.md *-ARCHITECTURE.md; do
  # Add to top: references: [[unified-os-architecture]], [[DATA-SOURCES]]
done

# FRAMEWORK FILES (72)
for file in [remaining]; do
  # Add to top: references: [[sector-taxonomy-31]], [[holding-company-100m-roadmap]]
done
```

---

## RESULT

✅ **Before:** 150 orphaned files, 0 connections
✅ **After:** 150 linked files, 450+ [[references]]

Files become discoverable via Obsidian graph: Hub → Related files → Specific analysis
