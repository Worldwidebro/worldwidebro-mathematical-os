---
name: OBSIDIAN-GRAPH-SETUP
title: Obsidian Knowledge Graph Setup
desc: ...
tags: obsidian, dataview, knowledge-graph, setup
description: Live Supabase ↔ Obsidian Dataview sync
created: 2026-05-14
updated: 2026-08-06T05:46:10Z
---

# Obsidian Knowledge Graph Setup

Your knowledge graph is now **live in Obsidian** with automatic Supabase sync.

## How It Works

```
Supabase (graph_entities + graph_relationships)
    ↓
obsidian_graph_sync.py (exports to JSON)
    ↓
.planning/graph-data.json (Obsidian data source)
    ↓
KNOWLEDGE-GRAPH-DASHBOARD.md (Dataview queries)
    ↓
Live dashboard in Obsidian vault
```

## Your Setup

### ✅ Already Installed
- **Data sync script**: `obsidian_graph_sync.py`
- **Dataview queries**: Embedded in `KNOWLEDGE-GRAPH-DASHBOARD.md`
- **Data file**: `.planning/graph-data.json` (auto-generated)

### ✅ What You Need
- **Obsidian Dataview plugin** (required for queries)
  - In Obsidian: Settings → Community Plugins → Browse → Search "Dataview" → Install
  - Enable the plugin

### ✅ Current Status
- 17 entities synced (Ventures, Decisions, Metrics, Risks)
- 3 relationships mapped (benefits, risks)
- Dashboard ready to view

## Using the Dashboard

1. **Open KNOWLEDGE-GRAPH-DASHBOARD.md** in Obsidian
   - Dataview queries automatically load from `graph-data.json`
   - Tables show all entities by type
   - Relationships displayed in separate section

2. **Refresh the data** when the graph updates:
   ```bash
   python3 obsidian_graph_sync.py
   ```
   This syncs the latest Supabase data to `graph-data.json`

3. **Query the graph** directly:
   - CEO reasoning: What are the current ventures and their metrics?
   - CFO analysis: Which ventures have highest CAC/LTV ratio?
   - CTO risk: What are the top 3 risks across all ventures?

## Dataview Queries Included

Each section in the dashboard uses dataviewjs to:

- **Entity Overview**: Count and categorize all 17 entities
- **Ventures Table**: List all ventures with status and capital allocation
- **Decisions Table**: Show decisions by type and venture
- **Metrics Table**: Display financial metrics (CAC, LTV, survival_metric)
- **Risks Table**: Rank risks by severity
- **Relationships Table**: Show entity connections

## Architecture

```
┌─ Supabase Postgres
│  ├─ graph_entities (17 rows)
│  └─ graph_relationships (3 rows)
│
├─ obsidian_graph_sync.py
│  └─ Fetches via Supabase API
│     Exports to JSON
│
└─ .planning/graph-data.json
   └─ Consumed by Dataview
      Displayed in KNOWLEDGE-GRAPH-DASHBOARD.md
```

## Development Notes

### Adding New Entities
1. Extract in `lightrag_demo.py` (pattern matching)
2. Sync to Supabase via `lightrag_supabase_sync.py`
3. Run `python3 obsidian_graph_sync.py`
4. Dashboard auto-refreshes

### Custom Dataview Queries
You can add custom queries to the dashboard. Basic syntax:

```dataviewjs
const data = await dv.io.load(".planning/graph-data.json");
const ventures = data.entities.filter(e => e.entity_type === "Venture");
dv.table(["Name", "Status"], ventures.map(v => [v.name, v.metadata.status]));
```

### Troubleshooting

**Dataview not showing data:**
- Ensure Dataview plugin is enabled
- Check that `.planning/graph-data.json` exists
- Reload Obsidian (Cmd+R on Mac)

**Graph data not updating:**
- Run `python3 obsidian_graph_sync.py` to refresh
- Verify Supabase credentials in environment variables

**Missing entities/relationships:**
- Check `graph-data.json` file directly with `cat .planning/graph-data.json | jq`
- Verify Supabase tables have data: `SELECT COUNT(*) FROM graph_entities;`

## Next Steps

- **May 15**: Monitor dashboard during agent decision cycles
- **May 20-21**: Ingest real Week 0 data → watch dashboard update live
- **May 22-23**: Validate accuracy (85%+ target) via dashboard
- **Ongoing**: Use dashboard as source of truth for venture health

---

**Status**: ✅ Live and ready to use

**How to verify**:
1. Open KNOWLEDGE-GRAPH-DASHBOARD.md in Obsidian
2. If you see a table with entities, you're good!
3. Run `python3 obsidian_graph_sync.py` anytime to refresh data
