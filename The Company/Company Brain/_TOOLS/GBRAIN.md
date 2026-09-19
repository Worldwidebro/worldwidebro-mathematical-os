[[_TOOLS/README|Tools]] | [[08-KNOWLEDGE-GRAPH/README|08-KNOWLEDGE-GRAPH]] | [[INDEX]]

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


## 4. Canonical Documentation, Conventions & Tutorials
- **Brain-First Lookup Protocol:** [[_TOOLS/gbrain/docs/guides/brain-first-lookup|brain-first-lookup.md]] — Mandatory pre-search protocol before calling external APIs.
- **Brain-First Lookup Convention:** [[_TOOLS/gbrain/skills/conventions/brain-first|brain-first.md]] — Sub-agent lookup order, token matching, and scoring rules.
- **Brain-Agent Execution Loop:** [[_TOOLS/gbrain/docs/guides/brain-agent-loop|brain-agent-loop.md]] — Recursive cycle of retrieval, execution, and ambient writeback.
- **Brains & Sources Architecture:** [[_TOOLS/gbrain/docs/architecture/brains-and-sources|brains-and-sources.md]] — Multi-source mental model, scoped sources, and team sharing.
- **Tutorial: Company Brain Setup:** [[_TOOLS/gbrain/docs/tutorials/company-brain|company-brain.md]] — Garry Tan's recipe for shared institutional memory across 10-50 operators.
- **Brain-Routing Convention:** [[_TOOLS/gbrain/skills/conventions/brain-routing|brain-routing.md]] — Routing rules across personal, venture, and company brains.
- **GBrain Skillpack Anatomy:** [[_TOOLS/gbrain/docs/GBRAIN_SKILLPACK|GBRAIN_SKILLPACK.md]] — Built-in cognitive skills catalog.
- **GBrain Engine Architecture:** [[_TOOLS/gbrain/README|README.md]] — Full engine specification and CLI guide.

---
[[INDEX]] | [[08-KNOWLEDGE-GRAPH/README|08-KNOWLEDGE-GRAPH]] | [[10-MEMORY/README|10-MEMORY]] | [[_TOOLS/README|Tools Gateway]]
