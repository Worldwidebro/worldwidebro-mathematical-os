---
name: docs/agentic-systems/06-MULTI-AGENT/AGENT-HANDOFFS
desc: ...
tags:
  - status/active
  - knowledge/current
id: agent-handoffs
type: document
status: active
owner: "[[Worldwidebro]]"
source: planning
confidence: 1.0
freshness: current
created: 2026-08-04
updated: 2026-08-06T05:46:10Z
---

# docs/agentic-systems/06-MULTI-AGENT/AGENT-HANDOFFS
## Purpose
Explain the Handoff pattern, showing how agents transfer state and execution control to another agent.

## Core Concept
A **Handoff** occurs when Agent A completes its scope of work (or detects a task out of its scope) and transfers execution control and state context to Agent B.

## Technical Details
Handoff implementation details:
- **Control Handover**: Agent A calls a special handoff tool containing Agent B's ID and the updated task parameters.
- **Context Preservation**: The conversation history (or state summaries) is packaged and forwarded, ensuring Agent B has all historical context needed.

## Relations
- Composes [[06-MULTI-AGENT/MULTI-AGENT-FUNDAMENTALS.md]]
- Contrast with [[06-MULTI-AGENT/AGENT-DELEGATION.md]]
