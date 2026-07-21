# Repo-Intelligence / Venture-OS — Completion Guide

**The whole remaining path is DETERMINISTIC local Python — it costs ~0 LLM tokens.**
Run the commands below; nothing here needs an agent, a subscription, or the Anthropic API.
Stack used (all local, already running): Ollama `nomic-embed` :11434, Qdrant :6333, Neo4j :7474 (`neo4j`/`ventures2026`).

Last verified: 2026-06-28.

---

## 1. STATUS — what is DONE

| Layer | State | Artifact |
|-------|-------|----------|
| Inventory (1,597 repos) | done | `REPOSITORY-REGISTRY.json` |
| Canonical vocabulary (25 terms) | done | `WORLDWIDEBRO-OS/08-DATA/registries/capability_vocabulary.json` |
| Capability catalog | done | `registries/capabilities-catalog.json` |
| Repo summaries (~43 tok each) | done | `repo-summaries.json` (1,595) |
| Embeddings (all repos) | done | Qdrant `repositories` = 1,597 |
| README corpus (PASS 1) | done | `readmes.json` (350/358) + re-embedded |
| Capability backfill (PASS 2 repo side) | done | `repo-capabilities-backfill.json` — coverage 10% -> 70.9% |
| Venture->Capability (PASS 2 venture side) | done | `venture-capabilities-proposed.csv` |
| Neo4j graph | done | 2,187 IMPLEMENTS, 6,542 NEEDS, 1,008 BELONGS_TO, 725k bridge paths |
| Retrieval layer | done | `retrieve.py` (query -> <=15 repos + venture + OPCO, ~100x compression) |
| Acceptance test | done | passes (recruiting, construction) |

The system already answers business questions grounded in code reality. Everything below is hardening, not redesign.

---

## 2. REMAINING — DONE (2026-06-28)

All three were built and run:

### B. Duplicate detector (PASS 3) — `find_duplicate_repos.py` ✅
- `duplicates-report.json`: 51 clusters, 305 repos (many `iza-os-*` near-dupes). Run: `python3 find_duplicate_repos.py`

### C. Execution readiness (Stage 12) — `build_execution_readiness.py` ✅
- `execution-readiness.csv` (uses `gh auth token`). Run: `python3 build_execution_readiness.py`

### D. Dependency / install map (skills + MCPs) — `build_dependency_map.py` ✅
- `DEPENDENCY-MAP.json` + Neo4j (:MCP)-[:PROVIDES]->(:Capability), (:Skill) nodes.
- Graph now: 1701 Repo, 25 Capability, 712 Venture, 18 OPCO, 7 Entity, 16 MCP, 9 Skill;
  edges IMPLEMENTS 2187, NEEDS 6542, PROVIDES 22, BELONGS_TO 1008.
- The OS can now answer per venture: capabilities needed -> repos that implement -> MCPs that provide -> OPCO/Holding.
- Run: `python3 build_dependency_map.py`

---

## 3. FULL REBUILD / REFRESH — copy-paste run order (all local, ~0 LLM tokens)

```bash
cd /Users/acebless/Documents
# 1. registry already current (regen only if repos changed): python3 scan_repositories.py
python3 build_capability_catalog.py            # capability join catalog
python3 build_repo_summaries.py                # ~43-token cards
python3 build_repo_rag.py --build              # embed all 1,597 into Qdrant
python3 build_readme_corpus.py                 # READMEs for high-value (uses gh auth token)
python3 build_capability_backfill.py           # repo capability coverage -> ~71%
python3 build_venture_capabilities.py          # venture NEEDS edges
python3 build_repo_graph.py                    # load/refresh Neo4j chain
# then the two to build:
python3 find_duplicate_repos.py                # PASS 3 (after script written)
python3 build_execution_readiness.py           # Stage 12 (after script written)
# verify:
python3 retrieve.py "which existing repos support launching a recruiting business?"
```

Token cost of the entire pipeline: zero LLM calls. Embeddings use local Ollama; everything else is deterministic Python + local DBs.

---

## 4. OPTIONAL — the ONLY step that needs an LLM (gated, do later)

Stage 11/13 "what business role could this repo play" / per-repo business mapping. Gate to high-value repos only (`strategic_value`/`revenue >= 6` -> ~358), run on local qwen3:8b via Ollama (still no API tokens). Do NOT run across all 1,597. Skip until the deterministic layer above is locked.

---

## 5. SCHEMA CONTRACT (PASS 3 vocab lock)

`capability_vocabulary.json` is the source of truth. Rule: no new canonical capability without review; merge duplicates into aliases. All scripts read it — never hardcode capability lists elsewhere.

---

## 6. KNOWN DATA NOTES

- `.env` `GITHUB_TOKEN` is a placeholder — scripts use `gh auth token` instead.
- Old `venture_capability_map.csv` is UUID-orphaned/dead — superseded by `venture-capabilities-proposed.csv`.
- Capability coverage 71% (not 100%) — the 29% uncovered are mostly sparse owned repos with empty PURPOSE; semantic search still reaches them.
- CLAUDE.md Data Layer section updated to Qdrant/Neo4j (Chroma/LightRAG are dead).
