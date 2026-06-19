---
references:
  - [[sector-taxonomy-31]]
  - [[holding-company-100m-roadmap]]
  - [[unified-os-architecture]]
---

# Master File Index — Worldwidebro OS

**Last Updated:** 2026-06-13  
**Purpose:** Central navigation for all system files, repos, and resources

---

## 🎯 QUICK ACCESS — Most Important Files

### Company Building (Phase 1 — THIS WEEK)
- **Execution Plan:** `/Users/acebless/Documents/SYSTEM-ENHANCEMENT-ROADMAP.md`
- **Repo Map:** `/Users/acebless/Documents/repos-classified-by-layer.json`
- **Venture-Repo Map:** `/Users/acebless/Documents/venture-to-repos-mapping.json`
- **Gap Analysis:** `/Users/acebless/Documents/capability-gap-analysis.json`

### Knowledge Graph (Visualization)
- **Dashboard:** `/Users/acebless/Documents/KNOWLEDGE-GRAPH-DASHBOARD.md` (open in Obsidian)
- **Graph Data:** `/Users/acebless/Documents/.planning/graph-data.json`
- **Graphify:** `/Users/acebless/Documents/Influence-Venture-Business-OS/INFRASTRUCTURE_LAYERS/worldwidebro-vault/graphify/graph.merged-712.json`

### Venture Structure
- **Ventures by Layer:** `/Users/acebless/Documents/00-OPERATING-SYSTEM/03-VENTURES-BY-LAYER/`
- **All Ventures:** `/Users/acebless/Documents/Influence-Venture-Business-OS/STRATEGY_LAYERS/WORLDWIDEBRO-OS/10_VENTURES/`

---

## 📁 FOLDER STRUCTURE — Where Everything Lives

```
/Users/acebless/Documents/
│
├── 📊 REPO INTELLIGENCE (Created 2026-06-11)
│   ├── repos-index.json (all 700 repos)
│   ├── repos-top-50.json (top 50 by capability)
│   ├── repos-starred-indexed.json (indexed by capability)
│   ├── repos-owned-inventory.json (6 owned repos)
│   ├── repos-classified-by-layer.json ⭐ (OS layer mapping)
│   └── graphify-repo-injection.json (knowledge graph payload)
│
├── 📊 CAPABILITY ANALYSIS (Created 2026-06-11)
│   ├── venture-capability-requirements.json
│   ├── capability-gap-analysis.json ⭐ (7 available, 1 to build)
│   ├── venture-to-repos-mapping.json ⭐ (618 ventures → repos)
│   └── system-enhancement-roadmap.json
│
├── 📋 SYSTEM ROADMAP
│   ├── SYSTEM-ENHANCEMENT-ROADMAP.md ⭐ (3-phase execution)
│   ├── task_plan.md (planning file)
│   ├── progress.md (session progress)
│   └── findings.md (analysis results)
│
├── 🔄 KNOWLEDGE GRAPH
│   ├── obsidian_graph_sync.py (sync script)
│   ├── populate_venture_knowledge_graph.py (fixed)
│   ├── KNOWLEDGE-GRAPH-DASHBOARD.md (Obsidian view)
│   ├── .planning/
│   │   ├── graph-data.json (3362 entities, 3408 relationships)
│   │   └── venture-hub-alignment.json
│   └── .env (Supabase credentials)
│
├── 🏗️ OPERATING SYSTEM
│   ├── 00-OPERATING-SYSTEM/
│   │   ├── 01-ACTIVE-PROJECTS/
│   │   ├── 02-INFRASTRUCTURE/
│   │   ├── 03-VENTURES-BY-LAYER/ ⭐ (Venture organization)
│   │   ├── 04-ARCHIVED/
│   │   └── 05-TEMP-AND-INBOX/
│   │
│   └── Influence-Venture-Business-OS/
│       ├── INFRASTRUCTURE_LAYERS/
│       │   ├── venture-hub/ (repo registry)
│       │   └── worldwidebro-vault/
│       │       ├── graphify/ ⭐ (graph visualization)
│       │       └── obsidian/ (vault)
│       │
│       └── STRATEGY_LAYERS/
│           ├── WORLDWIDEBRO-OS/
│           │   ├── 08_RESEARCH/
│           │   │   └── Ventures-Data/
│           │   │       ├── starred_repos_with_capabilities.csv (700 repos)
│           │   │       ├── ventures_with_capabilities.csv
│           │   │       └── MASTER-REPO-REGISTRY.csv
│           │   │
│           │   └── 10_VENTURES/ (all 712 venture folders)
│           │
│           └── sector-taxonomy-31.md (31 sectors)
│
└── 📚 OTHER RESOURCES
    ├── repos/starred/ (6 owned repos, cloned)
    ├── venture-hub/ (venture registry)
    └── graphify-out/ (graphify exports)
```

---

## 🔑 KEY FILES BY PURPOSE

### For Company Building This Week
1. **Read:** `SYSTEM-ENHANCEMENT-ROADMAP.md` (execution plan)
2. **Reference:** `repos-classified-by-layer.json` (which repos to use)
3. **Reference:** `capability-gap-analysis.json` (what to build vs adopt)
4. **Execute:** Follow Phase 1 in roadmap

### For Understanding the System
1. **Visualize:** Open Obsidian, press `Cmd+G` to see knowledge graph
2. **Or:** View `graph.merged-712.json` in Graphify
3. **Or:** Read `KNOWLEDGE-GRAPH-DASHBOARD.md` in Obsidian

### For Finding Ventures
1. Navigate to: `00-OPERATING-SYSTEM/03-VENTURES-BY-LAYER/`
2. Or: `Influence-Venture-Business-OS/STRATEGY_LAYERS/WORLDWIDEBRO-OS/10_VENTURES/`

### For Finding Repos
1. JSON: `repos-index.json` (all 700)
2. Top tier: `repos-top-50.json` (50 most important)
3. By OS layer: `repos-classified-by-layer.json`
4. In GitHub: `/Users/acebless/Documents/repos/starred/` (6 cloned)

---

## 🎯 SYMLINKS FOR EASY ACCESS

Create these shortcuts to avoid deep folder diving:

```bash
# Add to ~/.zshrc or ~/.bash_profile

alias ventures="cd ~/Documents/00-OPERATING-SYSTEM/03-VENTURES-BY-LAYER"
alias repos="cd ~/Documents/repos/starred"
alias roadmap="open ~/Documents/SYSTEM-ENHANCEMENT-ROADMAP.md"
alias graph="open ~/Documents/KNOWLEDGE-GRAPH-DASHBOARD.md"
alias capability="cat ~/Documents/capability-gap-analysis.json | jq"
alias venture-repos="cat ~/Documents/venture-to-repos-mapping.json | jq"
```

Then use:
```bash
ventures      # Jump to venture folder
roadmap       # Open roadmap in editor
graph         # Open Obsidian dashboard
capability    # View capability gaps
```

---

## 🗺️ HOW EVERYTHING CONNECTS

```
Repos (700)
    ↓
Capabilities (1276 unique)
    ↓
Core Capabilities (11 types)
    ↓
Ventures (1504 in graph, 618 with requirements)
    ↓
Sectors (31)
    ↓
Operating System (unified infrastructure)
    ↓
Company Building (Phase 1-3 roadmap)
```

---

## ✅ STATUS

- ✅ All files created and indexed
- ✅ Knowledge graph live (Supabase + Obsidian)
- ✅ Roadmap defined (3 phases)
- ✅ Repos mapped to ventures
- ⏳ Phase 1 (wiring) ready to execute

---

## 🚀 NEXT STEPS

1. **Navigate:** Use symlinks above to quickly access files
2. **Visualize:** Open Obsidian, press `Cmd+G` to see graph
3. **Execute:** Follow `SYSTEM-ENHANCEMENT-ROADMAP.md` Phase 1
4. **Track:** All files synced to Supabase knowledge graph

---

**Quick Links:**
- 🎯 Execution: `SYSTEM-ENHANCEMENT-ROADMAP.md`
- 📊 Data: `venture-to-repos-mapping.json`
- 🔍 Gaps: `capability-gap-analysis.json`
- 📈 Graph: `KNOWLEDGE-GRAPH-DASHBOARD.md`
