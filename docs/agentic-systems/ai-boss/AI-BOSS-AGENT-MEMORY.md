---
name: docs/agentic-systems/ai-boss/AI-BOSS-AGENT-MEMORY
desc: ...
tags:
  - status/active
  - knowledge/current
id: ai-boss-agent-memory
type: document
status: active
owner: "[[Worldwidebro]]"
source: proprietary
confidence: 1.0
freshness: current
created: 2026-08-04
updated: 2026-08-06T05:46:10Z
---

# docs/agentic-systems/ai-boss/AI-BOSS-AGENT-MEMORY
## Purpose
Define the storage format of memory logs in the Worldwidebro database.

## Core Concept
Memory is stored in `worldwidebro_os.duckdb` and synchronized to Supabase, indexing episodic runs and saving long-term reflection parameters.

## Relations
- Backs [[AI-BOSS/AI-BOSS-DECISION-ENGINE.md]]
