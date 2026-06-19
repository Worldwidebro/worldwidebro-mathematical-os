# FILE STRUCTURE MAP — 2026-06-11
**Generated:** 2026-06-11  
**Purpose:** Complete inventory of folder organization and file locations  
**Scope:** /Users/acebless/Documents and key subdirectories

---

## 📊 DIRECTORY STRUCTURE

### ROOT Level (/Users/acebless/Documents/)

**Core Operating System:**
```
/Users/acebless/Documents/
├── WORLDWIDEBRO-OS/                    [Main OS folder structure]
│   ├── 01_CEO_COMMAND_CENTER/          [Strategic planning]
│   │   ├── findings.md                 [Current findings]
│   │   ├── progress.md                 [Execution progress]
│   │   └── task_plan.md                [Master task plan]
│   ├── 07_AUTOMATIONS/                 [Automation scripts]
│   │   ├── Configs/                    [Configuration files]
│   │   │   ├── AUTO-ALIGNMENT-712.json [Venture alignment config]
│   │   │   └── REPO_REGISTRY.json      [Repo registry]
│   │   └── Scripts/                    [Automation scripts]
│   │       ├── align_venture_repo_universe.py
│   │       ├── obsidian_graph_sync.py
│   │       └── populate_ventures_served.py
│   └── 08_RESEARCH/                    [Data research layer]
│       ├── Ventures-Data/              [Venture datasets]
│       │   ├── WORLDWIDEBRO-712-UNIFIED.csv         [Master venture list]
│       │   ├── VENTURE-ID-CROSSWALK.csv             [ID mapping]
│       │   ├── ventures_dependencies.json           [Dependency graph]
│       │   └── [7 other venture CSVs]
│       └── Repo-Analysis/              [Repository analysis]
│           ├── PRIVATE-REPOS-ACCESS-CONTROL.csv
│           ├── construction_analysis.md             [SESSION 2026-06-11]
│           └── full_duplication_analysis.md         [SESSION 2026-06-11]
```

**Key Systems:**
```
├── venture-hub/                        [Master platform repo]
│   ├── ventures-master.csv             [712 ventures]
│   ├── MASTER-REPO-REGISTRY.csv        [985 repos]
│   ├── ventures_with_capabilities.csv  [Capabilities map]
│   ├── VENTURES-CAPABILITIES-LIST.csv  [Capabilities by venture]
│   ├── VENTURES-CAPABILITIES-CROSSREF.csv
│   └── sync_ventures_to_notion.py      [Notion sync script]
├── worldwidebro-vault/                 [Knowledge vault]
│   ├── graphify/                       [Graph visualization]
│   │   └── graph.merged-712.json       [712 ventures graph]
│   └── [other knowledge files]
├── mission-control/                    [Orchestration system]
├── thunderbolt/                        [Agent execution engine]
├── pitch-kit/                          [Investor materials]
└── [20+ other venture folders]
```

**Planning & Analysis:**
```
├── .planning/                          [Strategic planning files]
│   ├── graph-data.json                 [Obsidian export]
│   ├── venture-hub-alignment.json      [Alignment report]
│   ├── FULL-SYSTEM-MATRIX-107.md
│   ├── MASTER-OS-ARCHITECTURE-AND-GAPS.md
│   └── [6 more architecture files]
├── .obsidian/                          [Obsidian vault config]
│   ├── workspace.json
│   ├── graph.json
│   └── [plugin configs]
└── _inbox/                             [Inbox for incoming items]
    └── README.md
```

**Session & Documentation:**
```
├── DATA-SOURCES.md                     [UPDATED 2026-06-11] ✅
├── MIGRATION-LOG-2026-06-02.md         [UPDATED 2026-06-11] ✅
├── SESSION-SUMMARY-2026-06-11.md       [NEW 2026-06-11] ✅
├── FILES-UPDATED-2026-06-11.md         [NEW 2026-06-11] ✅
├── KNOWLEDGE-GRAPH-DASHBOARD.md        [Obsidian dashboard]
├── NOTION-OS-INTEGRATION-GUIDE.md      [Notion setup guide]
├── NOTION-SYNC-SETUP.md                [Notion sync docs]
└── [50+ other documentation files]
```

**Test & Support:**
```
├── test_notion_sync.py                 [Notion sync test]
├── sync_ventures_to_notion.py          [Sync script]
├── populate_venture_knowledge_graph.py  [Graph population]
├── insert_repos_to_graph.py            [Repo insertion]
└── load_ventures_unified.py            [Data loader]
```

---

## 📁 DETAILED FOLDER BREAKDOWN

### WORLDWIDEBRO-OS/ (Complete Structure)

**Layer 1: CEO Command Center**
```
01_CEO_COMMAND_CENTER/
├── findings.md                 [2026-06-09] — Current state findings
├── progress.md                 [2026-06-09] — Execution progress tracker
└── task_plan.md                [2026-06-09] — Master task roadmap
```

**Layer 7: Automations**
```
07_AUTOMATIONS/
├── Configs/
│   ├── AUTO-ALIGNMENT-712.json [Venture alignment rules]
│   └── REPO_REGISTRY.json      [Repo registry config]
└── Scripts/
    ├── align_venture_repo_universe.py    [Multi-venture alignment]
    ├── obsidian_graph_sync.py           [Graph → Obsidian export]
    └── populate_ventures_served.py      [Venture population]
```

**Layer 8: Research**
```
08_RESEARCH/
├── Ventures-Data/
│   ├── WORLDWIDEBRO-712-UNIFIED.csv              [Master list]
│   ├── VENTURE-ID-CROSSWALK.csv                  [ID mapping]
│   ├── ventures_dependencies.json                [Dependency graph]
│   ├── WORLDWIDEBRO-VENTURES-REPOS-ALIGNMENT.csv [Venture-repo map]
│   ├── ventures_enriched_option_b.json
│   ├── ventures_classification_final.csv
│   └── ventures_master_with_sectors.csv
│
└── Repo-Analysis/
    ├── PRIVATE-REPOS-ACCESS-CONTROL.csv
    ├── construction_analysis.md           [NEW 2026-06-11]
    ├── full_duplication_analysis.md      [NEW 2026-06-11]
    └── phase2_3_plan.md                  [NEW 2026-06-11]
```

---

## 🗂️ TOP-LEVEL DOCUMENTATION (50+ files)

**Session & Status Documents:**
```
✅ SESSION-SUMMARY-2026-06-11.md       [NEW 2026-06-11] — Complete session overview
✅ DATA-SOURCES.md                     [UPD 2026-06-11] — Data source inventory
✅ MIGRATION-LOG-2026-06-02.md         [UPD 2026-06-11] — Migration history
✅ FILES-UPDATED-2026-06-11.md         [NEW 2026-06-11] — File update log
✅ FILE-STRUCTURE-MAP-2026-06-11.md    [NEW 2026-06-11] — This file
```

**Integration & Setup:**
```
✅ NOTION-OS-INTEGRATION-GUIDE.md      [2026-06-10] — Notion integration
✅ NOTION-SYNC-SETUP.md                [2026-06-10] — Sync instructions
✅ KNOWLEDGE-GRAPH-DASHBOARD.md        [Current] — Obsidian dashboard
```

**System & Architecture:**
```
📋 CONSOLIDATION-STRATEGY.md           [Architecture reference]
📋 PROBLEM-TO-OFFER-ARCHITECTURE.md    [Offer architecture]
📋 CUSTOMER-ACQUISITION-ENGINE.md      [Customer acquisition]
📋 [30+ other strategic documents]
```

**Venture & Team:**
```
📊 712-VENTURE-WORKFORCE-PLANNING-MASTER.md    [Workforce allocation]
📊 ACE-CONSTRUCTION-TEST-RESULTS.md            [CON-001 results]
📊 ANISSA-APPLICATION-STRATEGY.md              [Team member plans]
📊 [20+ other venture-specific docs]
```

---

## 📦 REPOSITORY FOLDERS (Submodules/Clones)

**Infrastructure:**
```
├── mission-control/          [Orchestration]
├── thunderbolt/              [Agent execution]
├── pitch-kit/                [Investor materials]
└── [8 other core systems]
```

**Ventures (Sample):**
```
├── ec-001-angels-in-daylight/
├── bw-001-lash-extension-studio/
├── fin-001-genixbank-lite/
├── con-001-ace-construction/
└── [650+ other venture folders]
```

**Analysis Systems:**
```
├── civilization-os-local/    [Core OS logic]
├── iza-os-rag-system/        [RAG/semantic search]
├── worldwidebro-vault/       [Knowledge vault]
└── venture-factory-core/     [Venture creation]
```

---

## 📊 FILE STATISTICS

**By Type:**
```
Markdown files:      150+ (documentation, guides, analysis)
CSV files:           20+ (ventures, repos, capabilities data)
JSON files:          15+ (configs, graphs, alignments)
Python scripts:      8+ (sync, automation, analysis)
SQL files:           2+ (schema definitions)
Configuration:       5+ (.env, settings, configs)
```

**By Size:**
```
Large (>10MB):       repo_venture_mapping.json (1.4MB)
Medium (1-10MB):     graph.merged-712.json, various CSVs
Small (<1MB):        Most Python scripts, docs, configs
```

**By Update Frequency:**
```
Updated Today:       SESSION-SUMMARY-2026-06-11.md, etc. ✅
Updated This Week:   DATA-SOURCES.md, MIGRATION-LOG.md
Updated This Month:  Most architecture docs
```

---

## 🎯 FOLDER PURPOSES AT A GLANCE

| Folder | Purpose | Files | Status |
|--------|---------|-------|--------|
| WORLDWIDEBRO-OS/ | Master OS structure | 20+ | ✅ Current |
| venture-hub/ | Master platform | 10+ CSVs | ✅ Synced |
| .planning/ | Strategic planning | 12+ docs | ✅ Updated |
| .obsidian/ | Obsidian vault | 5+ config | ✅ Active |
| worldwidebro-vault/ | Knowledge graph | graph JSON | ✅ Merged |
| 50+ venture folders | Individual ventures | Code repos | ⏳ Partial |

---

## 📍 KEY NAVIGATION PATHS

**For Data Analysis:**
```
/WORLDWIDEBRO-OS/08_RESEARCH/Ventures-Data/WORLDWIDEBRO-712-UNIFIED.csv
↓
Contains: 1,633 ventures with metadata
Use: Primary venture source of truth
```

**For Repo Mapping:**
```
/venture-hub/repo_venture_mapping.json
↓
Contains: 1,669 repos mapped to ventures
Use: Repo-venture cross-reference
```

**For Knowledge Graph:**
```
/.planning/graph-data.json
↓
Contains: Exported entities and relationships
Use: Obsidian semantic search
```

**For Automation:**
```
/WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/
├── obsidian_graph_sync.py     → Exports graph to Obsidian
├── populate_ventures_served.py → Ventures population
└── align_venture_repo_universe.py → Universe alignment
```

---

## ✅ ORGANIZATION STATUS

**Well-Organized:**
- ✅ WORLDWIDEBRO-OS layer structure (7 folders)
- ✅ venture-hub system files
- ✅ .planning/ strategic documents
- ✅ Python automation scripts

**Partially Organized:**
- ⚠️ 50+ venture folders (mixed quality)
- ⚠️ Session documentation in root (should be in /sessions/)
- ⚠️ Analysis files in /tmp/ (not persistent)

**Needs Organization:**
- 📋 Root-level docs (150+ files) — Consider /docs/ folder
- 📋 Session summaries — Consider /sessions/2026-06 folder
- 📋 Test files — Consider /tests/ folder

---

## 🚀 RECOMMENDED FOLDER IMPROVEMENTS

**Short Term:**
1. Create `/sessions/2026-06/` → Move session summaries here
2. Create `/docs/architecture/` → Move strategic docs
3. Create `/analysis/2026-06/` → Move analysis files from /tmp/

**Medium Term:**
1. Consolidate 150+ root docs into `/docs/`
2. Archive old sessions (pre-2026-05) into `/archive/`
3. Standardize venture folder naming

**Long Term:**
1. Build automated file organization via script
2. Implement folder-level README files
3. Create web-based folder browser for team visibility

---

**File map last updated: 2026-06-11**
**Next update: When major folder reorganization occurs**
