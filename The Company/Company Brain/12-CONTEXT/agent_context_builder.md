---
id: KG-028
title: KG-028 — Agent Context Builder
aliases: ["12-CONTEXT/agent_context_builder", "agent_context_builder", "KG-028"]
tags: [context, neo4j, agents, assembly]
status: ACTIVE
updated: 2026-09-12
---

[[STARTHERE]] | [[12-CONTEXT]] | [[16-AGENTS]] | [[INDEX]]

# KG-028: Agent Context Builder

Dynamically extracts a scoped subgraph around active entities, ventures, and capabilities to construct high-density context windows for LLM agents.

- **Implementation Script:** `12-CONTEXT/agent_context_builder.py`
- **MCP Tool Wrapper:** `_MCP/context_assembly_tool.py`
- **FastAPI Route:** `POST /api/graph/context` on `:8000`
