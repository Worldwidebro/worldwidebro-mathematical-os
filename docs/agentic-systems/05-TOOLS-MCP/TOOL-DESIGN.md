---
name: docs/agentic-systems/05-TOOLS-MCP/TOOL-DESIGN
desc: ...
tags:
  - status/active
  - knowledge/current
id: tool-design
type: document
status: active
owner: "[[Worldwidebro]]"
source: planning
confidence: 1.0
freshness: current
created: 2026-08-04
updated: 2026-08-06T05:46:10Z
---

# docs/agentic-systems/05-TOOLS-MCP/TOOL-DESIGN
## Purpose
Provide best practices for design, schemas, and error boundaries of agent-facing tools.

## Core Concept
A tool should be designed with tight, descriptive scopes. An agent is only as capable as the clarity and error-resilience of its tools.

## Technical Details
1. **Descriptions**: Use clear, concise tool and parameter descriptions. The LLM uses these to decide *when* and *how* to call the tool.
2. **Error Recovery**: Tools should return verbose errors to the agent instead of throwing raw system exceptions (e.g., return "Error: Directory '/src' does not exist" instead of throwing `FileNotFoundError`).
3. **Granularity**: Keep tools focused (e.g., `view_file` and `replace_file_content` instead of a single `edit_code` tool).

## Relations
- Governed by [[02-AGENT-ANATOMY/AGENT-TOOLS.md]]
- Registered in [[05-TOOLS-MCP/TOOL-REGISTRY.md]]
