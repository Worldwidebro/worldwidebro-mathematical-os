# MEMORY-MODEL — Formal Specification of the Four-Tier Memory System

[[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[_MEMORY/MEMORY-ARCHITECTURE|MEMORY-ARCHITECTURE]] | [[_MEMORY/MEMORY-RETRIEVAL|MEMORY-RETRIEVAL]] | [[STARTHERE]]

> **Canonical Document ID:** `MEM-MOD-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)

---

## 1. Overview

Human cognition and autonomous agents both require distinct memory subsystems specialized for duration, retrieval mechanism, and semantic mutability. Company Brain models memory across four primary tiers, bound together by an associative relationship graph.

```text
┌─────────────────────────────────────────────────────────────┐
│ 1. WORKING MEMORY (Session & Active Task)                   │
│    - Fast, ephemeral, high-detail                           │
│    - Volatile RAM, active file buffers, subagent state      │
└──────────────────────────────┬──────────────────────────────┘
                               │ (graduation / logging)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. EPISODIC MEMORY (Chronological Event History)            │
│    - Temporal narrative of actions, events, and results     │
│    - JSONL transcripts, git commits, OpenObserve telemetry   │
└──────────────────────────────┬──────────────────────────────┘
                               │ (consolidation & extraction)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. SEMANTIC MEMORY (Structured World Knowledge)             │
│    - Entities, ventures, repos, technologies, stable facts   │
│    - Qdrant vector store, Wikidata QIDs, canonical YAMLs    │
└──────────────────────────────┬──────────────────────────────┘
                               │ (distillation & codification)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. PROCEDURAL MEMORY (Executable Operating Capabilities)    │
│    - Reusable skills, runbooks, schemas, code patterns, SOPs│
│    - .agents/skills/, FastMCP tools, validated scripts      │
└─────────────────────────────────────────────────────────────┘
                               ▲
                               │
               ASSOCIATIVE GRAPH LAYER (Neo4j)
               Connects all 4 tiers via typed relationships
```

---

## 2. Detailed Tier Specifications

### Tier 1: Working Memory (WM)
- **Scope:** Current task lifecycle, single conversation, or execution subagent.
- **Components:**
  - Active goal and sub-goals.
  - Active constraints and uncommitted diffs.
  - Current blockers and intermediate tool outputs.
- **Eviction Policy:** Cleared on task completion or summarized into episodic memory.

### Tier 2: Episodic Memory (EM)
- **Scope:** Event stream across sessions, days, and deployment cycles.
- **Schema:**
  ```json
  {
    "episode_id": "EP-20260905-001",
    "timestamp": "2026-09-05T11:00:00Z",
    "trigger": "User request to wire OmniRoute and Antigravity",
    "actions_taken": ["Built FastMCP adapter", "Configured LaunchAgent"],
    "outcome": "OmniRoute daemon running on port 20128",
    "verified": true,
    "lessons": ["better-sqlite3 outputs debug messages to stdout, requiring filter"]
  }
  ```
- **Retrieval:** Recency-weighted semantic search across recent transcripts.

### Tier 3: Semantic Memory (SM)
- **Scope:** Permanent conceptual truths about the ecosystem (713 ventures, 893 owned repos, 904 external repos).
- **Attributes:** Entity ID, Canonical Name, Sector, Wikidata QID, Technical Stack, Capabilities.
- **Retrieval:** Vector similarity (cosine distance via Qdrant) + graph traversal (Neo4j).

### Tier 4: Procedural Memory (PM)
- **Scope:** Step-by-step instructions on *how* to execute tasks successfully.
- **Components:**
  - 45 Antigravity rules (`ANTIGRAVITY.md`).
  - Modular skills (`.agents/skills/*/SKILL.md`).
  - Shell harnesses (`_CLI/`).
  - FastMCP tool definitions (`_MCP/fastmcp_server.py`).
- **Retrieval:** Capability mapping (`CAP-*` IDs) and task intent matching.
