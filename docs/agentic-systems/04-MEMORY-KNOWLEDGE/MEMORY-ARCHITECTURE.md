---
name: docs/agentic-systems/04-MEMORY-KNOWLEDGE/MEMORY-ARCHITECTURE
desc: ...
tags:
  - status/active
  - knowledge/current
id: memory-architecture
type: document
status: active
owner: "[[Worldwidebro]]"
source: planning
confidence: 1.0
freshness: current
aliases:
  - "Episodic Memory"
  - "Semantic Graph"
created: 2026-08-04
updated: 2026-08-06T05:46:10Z
---

# docs/agentic-systems/04-MEMORY-KNOWLEDGE/MEMORY-ARCHITECTURE
## Purpose
Provide a comprehensive blueprint of agent memory systems, outlining storage, indexing, and compaction layers.

## Core Concept
A robust memory architecture must balance immediate workspace context (Short-Term) with database stores containing historical tasks (Episodic) and structured domain facts (Semantic).

## Technical Details
1. **Short-Term Context**: Pruned via message truncation or summarized recursively using sliding windows.
2. **Episodic Logger**: Saves execution runs into a database (e.g., Supabase table), recording `query -> task -> tool calls -> success code`.
3. **Semantic Graph & Vectors**: Embeds documents using vector algorithms (Qdrant) and maps relationships using Cypher queries (Neo4j).

## Relations
- Governs [[02-AGENT-ANATOMY/AGENT-MEMORY.md]]
