---
name: docs/agentic-systems/ai-boss/AI-BOSS-CAPABILITY-GRAPH
desc: ...
tags:
  - status/active
  - knowledge/current
id: ai-boss-capability-graph
type: document
status: active
owner: "[[Worldwidebro]]"
source: proprietary
confidence: 1.0
freshness: current
created: 2026-08-04
updated: 2026-08-06T05:46:10Z
---

# docs/agentic-systems/ai-boss/AI-BOSS-CAPABILITY-GRAPH
## Purpose
Document the Neo4j Graph schema mapping Repositories, Capabilities, and Ventures.

## Core Concept
The **Capability Graph** resolves the join: `Venture -> Sector -> Capability -> Tool -> Repository`. It ensures that when an agent asks to "calculate X", the OS finds the exact code asset that implements the logic.

```
(:Venture {id: 'CON-001'})-[:REQUIRES]->(:Capability {name: 'Estimating'})-[:IMPLEMENTED_BY]->(:Repository {url: 'github.com/...'})
```

## Technical Details
Graph updates are triggered by `build_kg.py` and `obsidian_graph_build.py` based on markdown files in the vault. Relationships are parsed from wiki-links in the `## Capabilities` and `## Dependencies` headers.

## Relations
- Built by [[build_kg.py]]
- Syncs to [[obsidian_graph_sync.py]]
