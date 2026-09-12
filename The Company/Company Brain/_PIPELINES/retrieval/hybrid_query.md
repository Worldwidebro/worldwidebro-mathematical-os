---
id: KG-017
title: KG-017 — Hybrid Search Pipeline
aliases: ["_PIPELINES/retrieval/hybrid_query", "hybrid_query", "KG-017"]
tags: [pipeline, retrieval, neo4j, qdrant, search]
status: ACTIVE
updated: 2026-09-12
---

[[STARTHERE]] | [[14-CAPABILITIES/CAP-017-hybrid-search|CAP-017]] | [[08-KNOWLEDGE-GRAPH]] | [[INDEX]]

# KG-017: Hybrid Search Pipeline

Unifies Neo4j relational graph traversals with Qdrant vector semantic similarity search.

- **Implementation Script:** [`_PIPELINES/retrieval/hybrid_query.py`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_PIPELINES/retrieval/hybrid_query.py)
- **MCP Tool Wrapper:** [`_MCP/hybrid_query_tool.py`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_MCP/hybrid_query_tool.py)
- **FastAPI Route:** `POST /api/graph/query` on `:8000`
