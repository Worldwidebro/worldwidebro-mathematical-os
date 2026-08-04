---
id: agent-anatomy
type: document
name: AGENT ANATOMY
status: active
owner: "[[Worldwidebro]]"
created: 2026-08-04
updated: 2026-08-04
source: planning
confidence: 1.0
freshness: current
aliases:
  - "Agent Architecture"
  - "Cognitive Anatomy"
tags:
  - status/active
  - knowledge/current
---

# AGENT ANATOMY
## Purpose
Map the cognitive and physical components of an agent to technical abstractions (Model, Memory, Tools, Policies).

## Core Concept
An agent consists of a **Brain** (Model & Reasoning), a **Memory** (Context & Databases), and a **Body** (Tools & Actions), constrained by **Governance** (Policies).

```
                 AGENT
       ┌───────────┼───────────┐
       ▼           ▼           ▼
     MODEL      MEMORY       TOOLS
     (Brain)   (Context)    (Action)
       │           │           │
       ▼           ▼           ▼
   REASONING    HISTORY     MCP/APIs
       └───────────┬───────────┘
                   ▼
                POLICY (Governance)
```

## Technical Details
- **Model**: The core LLM responsible for reasoning, intent extraction, and choice generation.
- **Memory**: The short-term context window + long-term episodic/semantic stores.
- **Tools**: Executable functions (local shell, browser claw, database connections).
- **Policies**: System boundaries, guardrails, budget allocation limits, and permissions.

## Relations
- Governs [[02-AGENT-ANATOMY/AGENT-STATE.md]]
- Restricts [[02-AGENT-ANATOMY/AGENT-TOOLS.md]]
