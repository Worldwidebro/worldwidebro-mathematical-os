---
id: KG-048
title: KG-048 — Graph API Service
aliases: ["60-APIS/graph_api", "graph_api", "KG-048"]
tags: [api, fastapi, graph, neo4j, qdrant]
status: ACTIVE
updated: 2026-09-12
---

[[STARTHERE]] | [[60-APIS]] | [[08-KNOWLEDGE-GRAPH]] | [[INDEX]]

# KG-048: Graph API Service

FastAPI operational server exposing unified knowledge graph, vector similarity, and capability discovery endpoints across the company Tailscale mesh.

- **Implementation Script:** [`60-APIS/graph_api.py`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/60-APIS/graph_api.py)
- **Port:** `:8000` (Mac Studio M4 Max)
- **Auth:** Bearer token authentication
