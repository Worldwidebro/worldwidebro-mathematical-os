# Skill Execution Dashboard Hub

**Central index connecting all dashboard orbs in Obsidian graph**

> **Tip:** Open Obsidian Graph View (Ctrl+G / Cmd+G) to visualize this network as connected nodes

---

## 🗺️ Your Dashboard Ecosystem

```
                ┌─────────────────────────┐
                │ skill-execution-        │
                │ framework (master)      │
                │ • 296 skills            │
                │ • 14 phases             │
                │ • Supabase schema       │
                └────────────┬────────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
     ┌──────────▼──────────┐  ┌──────────▼─────────┐
     │ SKILL-PROGRESS-     │  │ SKILL-PROGRESS-    │
     │ DASHBOARD           │  │ BY-SECTOR          │
     │ (overview)          │  │ (details)          │
     │ • 6 Dataview blocks │  │ • 31 sector tabs   │
     │ • All ventures      │  │ • Health scoring   │
     │ • Sector rankings   │  │ • Drill-down       │
     └─────────┬───────────┘  └─────────┬──────────┘
               │                         │
               └────────────┬────────────┘
                            │
           ┌────────────────▼─────────────┐
           │ DASHBOARD-SETUP-GUIDE        │
           │ (operations manual)          │
           │ • Quick start                │
           │ • Refresh procedures         │
           │ • Troubleshooting            │
           │ • All 4 dashboards linked    │
           └──────────────────────────────┘
```

---

## 📊 Dashboard Files (Fully Connected)

### 1. [[skill-execution-framework]]
**Master Reference Document**
- Location: `.claude/projects/.../memory/skill-execution-framework.md`
- Contains: 296 skills, 14 phases, Supabase schema
- Links to: All other dashboards

### 2. [[SKILL-PROGRESS-DASHBOARD]]
**Developer Overview Dashboard**
- Location: `.planning/SKILL-PROGRESS-DASHBOARD.md`
- Contains: 6 Dataview blocks (ventures, sectors, phases, timing, blockers, feed)
- Links to: [[skill-execution-framework]], [[SKILL-PROGRESS-BY-SECTOR]], [[DASHBOARD-SETUP-GUIDE]]
- Refresh: Every 5 minutes (automatic)

### 3. [[SKILL-PROGRESS-BY-SECTOR]]
**Sector Deep-Dive Dashboards**
- Location: `.planning/SKILL-PROGRESS-BY-SECTOR.md`
- Contains: Overview table + 31 individual sector tabs
- Links to: [[skill-execution-framework]], [[SKILL-PROGRESS-DASHBOARD]], [[DASHBOARD-SETUP-GUIDE]]
- Use for: Exploring specific sectors (AI, Construction, SaaS, etc.)

### 4. [[DASHBOARD-SETUP-GUIDE]]
**Operations & Setup Manual**
- Location: `Documents/DASHBOARD-SETUP-GUIDE.md`
- Contains: Architecture, quick start, refresh, troubleshooting, optimization
- Links to: [[skill-execution-framework]], [[SKILL-PROGRESS-DASHBOARD]], [[SKILL-PROGRESS-BY-SECTOR]]
- Reference: All files, locations, and procedures

---

## 🎯 Start Here Based on Your Role

### I'm a Developer
1. Read [[skill-execution-framework]] (understand the system)
2. Open [[SKILL-PROGRESS-DASHBOARD]] (real-time overview)
3. Check [[SKILL-PROGRESS-BY-SECTOR]] (dive into your sector)
4. Reference [[DASHBOARD-SETUP-GUIDE]] (for setup/troubleshooting)

### I'm an Executive
1. Read [[DASHBOARD-SETUP-GUIDE]] (quick start)
2. Open Grafana (http://localhost:3000)
3. View "Skill Execution Metrics" dashboard
4. Check "Venture Health Portfolio" dashboard

### I'm Operations
1. Reference [[DASHBOARD-SETUP-GUIDE]] (operations section)
2. Run refresh script (every 5 minutes automatically)
3. Monitor logs in `.claude/hooks/dashboard-refresh.log`
4. Check [[SKILL-PROGRESS-DASHBOARD]] for status

---

## 🔗 Wiki Link Network Summary

**Total Connected Nodes:** 7
- [[skill-execution-framework]] (foundation)
- [[SKILL-PROGRESS-DASHBOARD]] (overview)
- [[SKILL-PROGRESS-BY-SECTOR]] (details)
- [[DASHBOARD-SETUP-GUIDE]] (operations)
- [[OBSIDIAN-GRAPH-STACK]] (advanced semantic layer)
- [[REPOSITORY-INTELLIGENCE-SYSTEM]] (repo classification & ecosystem)
- [[DASHBOARD-INDEX]] (this hub - central node)

**Connection Pattern:** Fully bidirectional (every doc links to every other doc)

**Graph Type:** Fully connected star topology with DASHBOARD-INDEX at center

---

## 📈 Data Pipeline Overview

```
Supabase (Source)
    ↓ (5-min sync)
DuckDB (Analytics)
    ├→ venture_progress.sql
    ├→ sector_progress.sql
    ├→ skill_timing.sql
    └→ phase_blockers.sql
        ↓
    Obsidian Dataview
    ├→ [[SKILL-PROGRESS-DASHBOARD]]
    └→ [[SKILL-PROGRESS-BY-SECTOR]]
        ↓
    Grafana (Executive)
    ├→ Skill Execution Metrics
    └→ Venture Health Portfolio
```

**Automation:** `dashboard-refresh-5m.sh` (in `.claude/hooks/`)

---

## 📋 Complete File Inventory

| File | Type | Location | Purpose | Links To |
|------|------|----------|---------|----------|
| skill-execution-framework.md | Master | memory/ | Framework + schema | All dashboards |
| SKILL-PROGRESS-DASHBOARD.md | Obsidian | .planning/ | Developer overview | All docs |
| SKILL-PROGRESS-BY-SECTOR.md | Obsidian | .planning/ | Sector details | All docs |
| DASHBOARD-SETUP-GUIDE.md | Guide | Documents/ | Operations manual | All docs |
| DASHBOARD-INDEX.md | Index | .planning/ | This hub (you are here) | All docs |
| venture_progress.sql | Query | analytics-queries/ | Venture metrics | Referenced in setup |
| sector_progress.sql | Query | analytics-queries/ | Sector metrics | Referenced in setup |
| skill_timing.sql | Query | analytics-queries/ | Skill timing | Referenced in setup |
| phase_blockers.sql | Query | analytics-queries/ | Blocker analysis | Referenced in setup |
| skill-execution.json | Grafana | grafana/dashboards/ | Executive dashboard | Referenced in setup |
| venture-health.json | Grafana | grafana/dashboards/ | Health dashboard | Referenced in setup |
| duckdb.yml | Config | grafana/datasources/ | DuckDB connection | Referenced in setup |
| dashboard-refresh-5m.sh | Script | .claude/hooks/ | Refresh automation | Referenced in setup |

---

## 🚀 Quick Navigation

**Want to explore?**
1. Open Obsidian
2. Press `Ctrl+G` (Windows/Linux) or `Cmd+G` (Mac)
3. See all 5 nodes connected as a graph
4. Click any node to navigate

**Want to understand the system?**
- Start: [[skill-execution-framework]]

**Want real-time data?**
- Go: [[SKILL-PROGRESS-DASHBOARD]]

**Want sector details?**
- Check: [[SKILL-PROGRESS-BY-SECTOR]]

**Want to set it up?**
- Read: [[DASHBOARD-SETUP-GUIDE]]

---

## ✨ Connected Node Status

- ✅ [[skill-execution-framework]] — Active (master reference)
- ✅ [[SKILL-PROGRESS-DASHBOARD]] — Active (6 blocks)
- ✅ [[SKILL-PROGRESS-BY-SECTOR]] — Active (31 sectors)
- ✅ [[DASHBOARD-SETUP-GUIDE]] — Active (operations manual)
- ✅ [[DASHBOARD-INDEX]] — Active (this hub)

**Graph Connectivity:** Fully connected (all nodes link to all other nodes)

**Last Updated:** 2026-06-11 20:25 UTC

---

## 📚 Related Frameworks

These dashboards are part of a larger integrated system:

**Skill Execution System:**
- [[skill-execution-framework]] — 296 slash commands × 14 phases
- 712 ventures tracked across 31 sectors
- Real-time execution auditing via Supabase
- Multi-layer visualization (Obsidian + Grafana)

**Repository Intelligence System:**
- [[REPOSITORY-INTELLIGENCE-SYSTEM]] — 1,400+ repos classified across 7 layers
- Repo-to-venture mapping
- Component library assembly
- Ecosystem graph relationships

**Graph & Knowledge Systems:**
- [[OBSIDIAN-GRAPH-STACK]] — Advanced semantic search + graph databases
- [[OPERATING_SYSTEM_ARCHITECTURE]] — Complete OS with AI agent layers

---

**This is your central hub. Click any link above to navigate the dashboard ecosystem.**

