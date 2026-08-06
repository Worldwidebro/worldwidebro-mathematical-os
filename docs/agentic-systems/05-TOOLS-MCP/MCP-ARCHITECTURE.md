---
name: docs/agentic-systems/05-TOOLS-MCP/MCP-ARCHITECTURE
desc: ...
tags:
  - status/active
  - knowledge/current
id: mcp-architecture
type: document
status: active
owner: "[[Worldwidebro]]"
source: planning
confidence: 1.0
freshness: current
created: 2026-08-04
updated: 2026-08-06T05:46:10Z
---

# docs/agentic-systems/05-TOOLS-MCP/MCP-ARCHITECTURE
## Purpose
Provide a deep architectural dive into MCP specifications, detailing connection layers, JSON-RPC schemas, and message routing.

## Core Concept
MCP defines standard capabilities: **Prompts**, **Resources**, and **Tools**.

## Technical Details
- **Prompts**: Server-defined prompt templates the client can inject.
- **Resources**: Server-read-only data sources (logs, files, database records) requested via URIs (e.g., `gitnexus://repo/status`).
- **Tools**: Client-executable functions with arguments and JSON schemas.

## Relations
- Builds on [[05-TOOLS-MCP/MCP-FUNDAMENTALS.md]]
