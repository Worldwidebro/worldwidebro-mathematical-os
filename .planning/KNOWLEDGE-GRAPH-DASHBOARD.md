---
tags: knowledge-graph, dashboard, obsidian
created: 2026-07-21T05:50:03.689337
---

# Knowledge Graph Dashboard

**Last Sync:** 2026-07-21T05:50:03.685683
**Status:** LIVE

---

## System Health

| Metric | Value |
|--------|-------|
| **Total Entities** | 15446 |
| **Ventures** | 0 |
| **Repos** | 0 |
| **Contacts** | 0 |
| **Total Relationships** | 15782 |
| **Repos w/ Connections** | 0 |

---

## Entity Types

```dataview
TABLE WITHOUT ID
    entity_type AS "Type",
    count(rows) AS "Count"
FROM "KNOWLEDGE-GRAPH-DASHBOARD"
GROUP BY entity_type
SORT Count DESC
```

---

## Relationship Types

```dataview
TABLE WITHOUT ID
    relation_type AS "Type",
    count(rows) AS "Count"
FROM "KNOWLEDGE-GRAPH-DASHBOARD"
GROUP BY relation_type
SORT Count DESC
```

---

## Ventures (Top 20)

```dataview
TABLE WITHOUT ID
    entity_name AS "Venture",
    entity_type AS "Type"
FROM "KNOWLEDGE-GRAPH-DASHBOARD"
WHERE entity_type = "VENTURE"
LIMIT 20
```

---

## Repos (Top 20)

```dataview
TABLE WITHOUT ID
    entity_name AS "Repo",
    entity_type AS "Type"
FROM "KNOWLEDGE-GRAPH-DASHBOARD"
WHERE entity_type = "REPO"
LIMIT 20
```

---

## Contacts (Top 20)

```dataview
TABLE WITHOUT ID
    entity_name AS "Contact",
    entity_type AS "Type"
FROM "KNOWLEDGE-GRAPH-DASHBOARD"
WHERE entity_type = "PERSON"
LIMIT 20
```

---

## Data Source

- **Source:** Supabase (graph_entities, graph_relationships)
- **Export:** .obsidian-sync/graph-data.json
- **Alignment:** .obsidian-sync/venture-hub-alignment.json

---

## Sync Status

✅ **Entities imported:** 15446
✅ **Relationships established:** 15782
✅ **Dashboard rendered:** 2026-07-21 05:50:03

---

**Next Steps:**
1. Open this file in Obsidian
2. Verify 8 Dataview blocks render above
3. If blocks show data, graph is connected
4. If blocks are empty, check Supabase connection

---

## Repository Map / Venture Index / Knowledge Graph — Master Index
_Source of truth = CSVs + Supabase, not the GitHub API._

### Venture Index
| File | Rows | What |
|------|------|------|
| `.../INFRASTRUCTURE_LAYERS/venture-hub/ventures-master.csv` | 712 | Canonical ventures (id, name, sector, stage, status, repo_id) |
| `.../venture-hub/ventures_with_capabilities.csv` | 618 | + required_capabilities + top_repo_1/2/3 |
| `08-DATA/registries/ventures.csv` / `venture_capability_map.csv` | — | Registry snapshot + venture->capability |

### Repository Map
| File | Size/Rows | What |
|------|-----------|------|
| `.../REFERENCE/REPOSITORY-REGISTRY.json` | 908K | ~1,592 repos, 10 attributes |
| `.../venture-hub/MASTER-REPO-REGISTRY.csv` | 985 | Repos -> ventures + agents + health_score |
| `08-DATA/registries/repositories.csv` / `venture_repo_map.csv` | 37K / 137K | Flat repo list + venture<->repo edges |

### Knowledge Graph
| File / Store | Size | What |
|--------------|------|------|
| `.obsidian-sync/graph-data.json` | 7.5M | Full entity+relationship export |
| `.obsidian-sync/venture-hub-alignment.json` | 221K | Processed alignment |
| Supabase graph_entities / graph_relationships | — | Source of truth |
| Neo4j 08-DATA/venture-hub-data/neo4j | — | Graph DB |

### Regenerate
- python3 populate_venture_knowledge_graph.py   -> graph_entities + relationships
- python3 obsidian_graph_sync.py                -> .obsidian-sync/*.json + this dashboard
- python3 scan_repositories.py                  -> REPOSITORY-REGISTRY.json
- python3 WORLDWIDEBRO-OS/08-DATA/build_registries.py  -> 08-DATA/registries/*.csv
