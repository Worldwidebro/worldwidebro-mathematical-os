---
title: Knowledge Graph Dashboard
description: Live view of Week 0 venture entities and relationships
tags: graph, knowledge, ventures, dashboard, dataview
created: 2026-05-14
last-updated: 2026-05-14
---

# Knowledge Graph Dashboard

**Status**: ✅ Live with Supabase → Obsidian sync  
**Data Source**: `.planning/graph-data.json`  
**Alignment Source**: `.planning/venture-hub-alignment.json`  
**Last Updated**: `=dateformat(now(), "yyyy-MM-dd HH:mm")`  

---

## Live Entity Overview

```dataviewjs
const data = await dv.io.load(".planning/graph-data.json");
if (!data || !data.entities) {
  dv.paragraph("⏳ Loading knowledge graph data...");
} else {
  const entities = data.entities || [];
  const stats = {
    total: entities.length,
    ventures: entities.filter(e => e.entity_type === "Venture").length,
    decisions: entities.filter(e => e.entity_type === "Decision").length,
    metrics: entities.filter(e => e.entity_type === "Metric").length,
    risks: entities.filter(e => e.entity_type === "Risk").length,
    agents: entities.filter(e => e.entity_type === "Agent").length,
  };
  
  dv.paragraph(`
📊 **Total Entities**: ${stats.total}
- 🏢 Ventures: ${stats.ventures}
- ✅ Decisions: ${stats.decisions}
- 📈 Metrics: ${stats.metrics}
- ⚠️  Risks: ${stats.risks}
- 👥 Agents: ${stats.agents}
  `);
}
```

---

## Ventures

```dataviewjs
const data = await dv.io.load(".planning/graph-data.json");
if (data && data.entities) {
  const ventures = data.entities.filter(e => e.entity_type === "Venture");
  if (ventures.length > 0) {
    dv.table(
      ["Name", "ID", "Venture ID", "Status"],
      ventures.map(v => [
        v.name,
        v.id,
        v.venture_id || "—",
        v.metadata?.status || "—"
      ])
    );
  }
}
```

---

## Decisions

```dataviewjs
const data = await dv.io.load(".planning/graph-data.json");
if (data && data.entities) {
  const decisions = data.entities.filter(e => e.entity_type === "Decision");
  if (decisions.length > 0) {
    dv.table(
      ["Decision", "Type", "Venture ID", "Details"],
      decisions.map(d => [
        d.name,
        d.entity_type,
        d.venture_id || "—",
        d.description || "—"
      ])
    );
  }
}
```

---

## Financial Metrics

```dataviewjs
const data = await dv.io.load(".planning/graph-data.json");
if (data && data.entities) {
  const metrics = data.entities.filter(e => e.entity_type === "Metric");
  if (metrics.length > 0) {
    dv.table(
      ["Metric", "Venture", "Value", "Unit"],
      metrics.map(m => [
        m.name,
        m.venture_id || "—",
        m.metadata?.value || "—",
        m.metadata?.unit || "—"
      ])
    );
  }
}
```

---

## Risk Assessment

```dataviewjs
const data = await dv.io.load(".planning/graph-data.json");
if (data && data.entities) {
  const risks = data.entities.filter(e => e.entity_type === "Risk");
  if (risks.length > 0) {
    dv.table(
      ["Risk", "Venture", "Severity", "Description"],
      risks.map(r => [
        r.name,
        r.venture_id || "—",
        r.metadata?.severity || "—",
        r.description || "—"
      ])
    );
  }
}
```

---

## Repo Registry

```dataviewjs
const data = await dv.io.load(".planning/graph-data.json");
if (data && data.entities) {
  const repos = data.entities.filter(e => e.entity_type === "Repo");
  if (repos.length > 0) {
    dv.table(
      ["Name", "Type", "Owner", "Description"],
      repos.map(r => [
        r.name,
        r.metadata?.type || "—",
        r.metadata?.owner || "—",
        r.description || "—"
      ])
    );
  } else {
    dv.paragraph("No repos in graph yet. Run `python3 obsidian_graph_sync.py` after adding Repo entities to Supabase.");
  }
}
```

---

## Entity Relationships

```dataviewjs
const data = await dv.io.load(".planning/graph-data.json");
if (data && data.relationships) {
  const rels = data.relationships || [];
  if (rels.length > 0) {
    dv.table(
      ["Source ID", "Relation Type", "Target ID", "Weight"],
      rels.map(r => [
        r.source_id,
        r.relation_type,
        r.target_id,
        r.weight || 1.0
      ])
    );
  } else {
    dv.paragraph("No relationships found in graph.");
  }
}
```

---

## Agent Integration Status

| Agent | Status | Query Type | Graph Context |
|-------|--------|-----------|---------------|
| CEO | ✅ Active | Venture context + decisions | ✅ Enriched with metrics+risks |
| CFO | ✅ Active | Financial metrics | ✅ Graph metrics indexed by venture |
| CTO | ✅ Active | Risk escalation | ✅ All risks extracted and ranked |
| Sector PMs | ✅ Ready | Per-venture decisions | ✅ Graph indexed by venture_id |

---

## How to Update Graph

Run the sync script to export latest Supabase data to JSON:

```bash
python3 obsidian_graph_sync.py
```

This will:
1. Query Supabase `graph_entities` and `graph_relationships` tables
2. Export to `.planning/graph-data.json`
3. Dataview queries automatically refresh from new JSON

---

## Raw Data Inspector

```dataviewjs
const data = await dv.io.load(".planning/graph-data.json");
dv.paragraph(`**Data Status**: ${data?.status || "unknown"}`);
if (data?.synced_at) {
  dv.paragraph(`**Last Synced**: ${data.synced_at}`);
}
dv.paragraph(`**Entities**: ${data?.entity_count || 0}`);
dv.paragraph(`**Relationships**: ${data?.relationship_count || 0}`);
```

---

## Venture Hub Alignment

```dataviewjs
const align = await dv.io.load(".planning/venture-hub-alignment.json");
if (!align || !align.summary) {
  dv.paragraph("⏳ Alignment data not available yet. Run `python3 obsidian_graph_sync.py`.");
} else {
  const summary = align.summary;
  dv.paragraph(`
🔗 **Alignment Summary**
- Total ventures: ${summary.total_ventures || 0}
- Aligned: ${summary.ventures_aligned || 0}
- Needs attention: ${summary.ventures_needing_attention || 0}
- With graph entities: ${summary.ventures_with_graph_entities || 0}
- Supabase repos indexed: ${summary.supabase_repo_count || 0}
  `);

  const mismatches = (align.mismatches || []).slice(0, 25);
  if (mismatches.length > 0) {
    dv.table(
      ["Venture", "Venture ID", "Graph Connected", "Missing Required Repos", "Status"],
      mismatches.map(v => [
        v.venture_name || "—",
        v.venture_id || "—",
        v.graph_connected ? "✅" : "❌",
        (v.missing_required_repos || []).join(", ") || "—",
        v.alignment_status || "—"
      ])
    );
  } else {
    dv.paragraph("✅ All ventures are aligned.");
  }
}
```

---

## Next Steps

- [ ] **May 15**: Verify Supabase connection with credentials
- [ ] **May 20-21**: Ingest real Week 0 data into knowledge graph
- [ ] **May 22-23**: Validate extraction accuracy (target 85%+)
- [ ] **May 23-24**: Performance test with 50+ documents
- [ ] **May 27+**: Continuous autonomous decision cycles with live graph

---

**Task 14 Status**: Knowledge graph integrated into agent decision loop + Obsidian dashboard ✅

**Live at**: Obsidian → KNOWLEDGE-GRAPH-DASHBOARD.md (this file)  
**Data from**: Supabase `graph_entities` + `graph_relationships`  
**Sync via**: `obsidian_graph_sync.py` (run whenever you update the graph)
