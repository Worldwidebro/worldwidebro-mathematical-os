# Venture-GitHub-Graph Flow Map

Last updated: 2026-05-22  
Purpose: Show how venture data, GitHub repos (owned/starred), and graph tooling should connect in one operational pipeline.

---

## 1) What each file family does

### Venture demand side
- `ventures_enriched_option_b.json`: canonical venture IDs, names, sectors, capability matches.
- `ventures_dependencies.json`: venture-level required repos and dependency tiers.
- `ventures_with_capabilities.csv`: tabular capability view for ventures.
- `verify_venture_repo_matching.py`: checks venture-to-repo matching consistency.
- `.planning/venture-hub-alignment.json`: generated alignment status snapshot.

### GitHub supply side
- `github_repos_sync.py`: sync repo metadata from GitHub to Supabase `repos`.
- `classify_repos_heuristic.py`: classify owned/starred repos into institutional functions.
- `classify_repos_institutional.py`: LLM-assisted repo classification path.
- `starred_repos_with_capabilities.csv`: starred repos plus inferred capability tags.
- `STARRED-REPOS-CATEGORIZED.md`: categorized starred repo sets by function.
- `starred-repos-capabilities.md`: capability map and integration tiers.

### Graph and dashboard side
- `obsidian_graph_sync.py`: pulls `graph_entities` and `graph_relationships` from Supabase to local JSON.
- `.planning/graph-data.json`: Obsidian-facing graph snapshot.
- `KNOWLEDGE-GRAPH-DASHBOARD.md`: Dataview dashboard (graph + alignment sections).

### Master/architecture docs
- `MASTER-INDEX.md`: central navigation and system intent.
- `VENTURE-OPERATIONS-FRAMEWORK.md`: business architecture and operating model.

---

## 2) End-to-end relationship chain

1. Venture files define what each venture needs (`venture_id`, required capabilities/repos).  
2. GitHub sync/classification files define what repos can provide (owned + starred).  
3. Matching and verification connect ventures to repos.  
4. Graph ingestion writes entities/relationships into Supabase graph tables.  
5. Obsidian sync exports graph/alignment JSON for local visibility.  
6. Dashboard renders current state for decision support.

Formula:  
`venture requirements` + `repo capabilities` + `graph links` = `venture-hub operating context`

---

## 3) Current blockers observed

- GitHub auth invalid in local CLI session blocks trusted owned/starred sync checks.
- Supabase `403 Forbidden` blocks live graph export (`graph-data.json` can become empty/error state).
- Venture UUIDs and legacy demo venture IDs are mixed in historical artifacts.
- Some docs are aspirational while runtime scripts are partially connected.

---

## 4) Does Graphify help?

Yes, but as a visualization and exploration layer, not as the core data pipeline.

Graphify is most useful when:
- you already have normalized nodes/edges (ventures, repos, capabilities, dependencies),
- graph data is refreshed on schedule,
- and you need network questions answered quickly (for example: "which repos unblock venture X?").

Graphify is less useful when:
- auth/sync pipelines are failing,
- IDs are inconsistent,
- or graph tables are stale.

Practical view: Graphify is high-value after pipeline health is restored.

---

## 5) Starred repos map: how they should work together

Use starred repos as capability accelerators around a core backbone.

### Backbone stack (recommended order)
1. Ingest: `firecrawl`, `crawl4ai`, `docling`, `opendataloader-pdf`
2. Retrieval/graph: `llama_index`, `LightRAG`, `graphiti`, `graphify`
3. Orchestration: `langgraph`, `crewAI`, `ruflo`, `n8n`
4. Memory/context: `mem0`, `claude-mem`, `cognee`, `context-hub`
5. Observability: `prometheus`, `grafana`, `loki`, `sentry`, `opentelemetry-collector`
6. Interfaces/workflow: `mcp`, `mcp-registry`, `postgres-mcp`, `git-mcp`

### Functional lanes
- OSINT/contact enrichment lane: `maigret` + `sherlock` + `Claude-OSINT`
- Knowledge lane: `LightRAG` + `llama_index` + `graphify`
- Automation lane: `langgraph` + `crewAI` + `n8n`
- Reliability lane: `prometheus` + `grafana` + `loki` + `sentry`

### How they compose in venture-hub
- Venture requires capability -> select candidate repos from starred/owned map.
- Classify and score fit -> write selected repo links to venture dependencies.
- Materialize venture-repo edges in graph tables.
- Visualize with Graphify and dashboard for decision cycles.

---

## 6) What "connected" looks like

- GitHub sync success: repos table populated with owned/starred metadata.
- Classification success: institutional function + capability tags present.
- Graph sync success: non-zero entities/relationships in `.planning/graph-data.json`.
- Alignment success: `.planning/venture-hub-alignment.json` shows aligned ventures > 0.
- Dashboard reflects both graph counts and mismatch table meaningfully.

---

## 7) Single operator loop

Run in this order:

1. `python3 github_repos_sync.py`
2. `python3 classify_repos_heuristic.py`
3. venture matching/verifier scripts
4. graph ingestion scripts
5. `python3 obsidian_graph_sync.py`
6. review `KNOWLEDGE-GRAPH-DASHBOARD.md`

If step 1 or step 5 fails auth, all downstream visibility is unreliable.
