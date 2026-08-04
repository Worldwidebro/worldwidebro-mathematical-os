---
id: ai-boss-agent-registry
type: document
name: AI BOSS AGENT REGISTRY
status: active
owner: "[[Worldwidebro]]"
created: 2026-08-04
updated: 2026-08-04
source: proprietary
confidence: 1.0
freshness: current
tags:
  - status/active
  - knowledge/current
---

# AI BOSS AGENT REGISTRY
## Purpose
Define the schema, attributes, and tracking mechanisms of all active agents running on the Worldwidebro OS.

## Core Concept
The **Agent Registry** is the central catalog tracking agent metadata, lifecycle states, token budgets, and operational departments.

## Technical Details
Active agent metadata is stored in `agents_index.csv.stub` and registered in Supabase:
- `agent_id`: Canonical ID (e.g. `T3_CONTENT_STRATEGIST_001`).
- `role`: Domain specialty (e.g. Creator, Auditor, Coordinator).
- `department`: Linked department (e.g., Finance, Sales).
- `capabilities`: Linked capabilities (wiki-links in the ontology).
- `status`: Active, Paused, or Decommissioned.

## Relations
- Feeds [[AI-BOSS/AI-BOSS-AGENT-ROLE-SYSTEM.md]]
- Matches [[AI-BOSS/AI-BOSS-AGENT-ORG-CHART.md]]
