---
id: mcp-fundamentals
type: document
name: MCP FUNDAMENTALS
status: active
owner: "[[Worldwidebro]]"
created: 2026-08-04
updated: 2026-08-04
source: planning
confidence: 1.0
freshness: current
aliases:
  - "Model Context Protocol"
  - "MCP Standard"
tags:
  - status/active
  - knowledge/current
---

# MCP FUNDAMENTALS
## Purpose
Introduce the Model Context Protocol (MCP), explaining why standardizing the client-server-tool link is critical for agent scalability.

## Core Concept
**MCP** (Model Context Protocol) is an open-standard protocol designed to link LLM applications (clients) to data sources and execution engines (servers) securely and consistently.

```
┌───────────────┐           Model Context Protocol           ┌──────────────┐
│  MCP Client   │◄──────────────────────────────────────────►│  MCP Server  │
│  (AI Agent)   │                                            │ (Files/APIs) │
└───────────────┘                                            └──────────────┘
```

## Technical Details
MCP solves the "custom tool integration" bottleneck:
- **Clients**: Frameworks/IDE layers (e.g., Claude Desktop, Antigravity IDE, vex-api) that handle orchestration.
- **Servers**: Lightweight services exposing resources, prompts, and tools.
- **JSON-RPC**: Protocol messaging format running over Stdio or SSE.

## Relations
- Details: [[05-TOOLS-MCP/MCP-ARCHITECTURE.md]]
- Implemented in [[05-TOOLS-MCP/MCP-SERVERS.md]]
