---
id: TOOL-GBRAIN-001
title: GBrain — Persistent Agent Memory & Knowledge Graph
aliases: ["GBrain", "gbrain", "garrytan/gbrain", "Garry Tan Brain"]
tags: [tools, memory, pglite, knowledge-graph, gbrain]
status: ACTIVE
updated: 2026-09-12
---

[[STARTHERE]] | [[AGENTS]] | [[08-KNOWLEDGE-GRAPH]] | [[13_ENGINEERING/INFRASTRUCTURE/05_STORAGE/STORAGE|STORAGE]] | [[INDEX]]

# GBrain (`garrytan/gbrain`)

**Authority:** CP-004 (Data) & CP-027 (Infrastructure)  
**Status:** ✅ `INSTALLED & OPERATIONAL` (`_TOOLS/gbrain`, CLI script at `scripts/gbrain`)  
**Engine:** Embedded PGLite (WASM Postgres + pgvector) for local-first zero-dependency storage.

---

## 1. System Overview
GBrain is Garry Tan's persistent, markdown-first AI agent memory system. It provides cognitive agents (Claude Code, Hermes, Antigravity) with long-term memory, multi-hop semantic synthesis, and self-wiring knowledge graph traversal.

## 2. Key Architecture & Features
- **Hybrid Search:** Combines BM25 keyword full-text search with pgvector cosine semantic embeddings.
- **Memory Verbs:** Implements the 7 core memory verbs (`capture`, `think`, `brainstorm`, `lsd`, `code-def`, `code-refs`, `reconcile-links`).
- **Code Indexing (Cathedral II):** Cross-file symbol definition and caller/callee AST graph parsing.
- **Storage:** Local PGLite database under `_TOOLS/gbrain/` synchronized into Company Brain's Neo4j relational graph (`scripts/gbrain_to_neo4j_sync.py`).

## 3. CLI Invocations
```bash
./scripts/gbrain --help                  # View command suite
./scripts/gbrain query "<phrase>"        # Run hybrid retrieval over venture files
./scripts/gbrain think "<question>"      # Multi-hop cited knowledge synthesis
./scripts/gbrain health                  # Health and sync status
```
