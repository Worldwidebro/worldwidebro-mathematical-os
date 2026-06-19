---
tags: knowledge-graph, dashboard, obsidian
created: 2026-06-16T17:13:10.022318
---

# Knowledge Graph Dashboard

**Last Sync:** 2026-06-16T17:13:10.019904
**Status:** LIVE

---

## System Health

| Metric | Value |
|--------|-------|
| **Total Entities** | 7082 |
| **Ventures** | 100 |
| **Repos** | 0 |
| **Contacts** | 0 |
| **Total Relationships** | 7276 |
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
- **Export:** .planning/graph-data.json
- **Alignment:** .planning/venture-hub-alignment.json

---

## Sync Status

✅ **Entities imported:** 7082
✅ **Relationships established:** 7276
✅ **Dashboard rendered:** 2026-06-16 17:13:10

---

**Next Steps:**
1. Open this file in Obsidian
2. Verify 8 Dataview blocks render above
3. If blocks show data, graph is connected
4. If blocks are empty, check Supabase connection
