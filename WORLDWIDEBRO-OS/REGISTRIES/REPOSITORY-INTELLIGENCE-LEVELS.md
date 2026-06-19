# Repository Intelligence Levels (L1–L7)

**Principle:** Owning 1,400 repos ≠ having 1,400 repos as intelligence.  
**Goal:** Turn repositories into a **queryable knowledge system**.

Related: [[REPOSITORY-INTELLIGENCE-SYSTEM]] | [[repo_vocabulary.json]] | [[repo-classification-prompts.md]]

---

## Level 1: Raw Repositories

```text
GitHub → Repo 1 … Repo 1400
```

**Problem:** No concept search, overlap detection, reuse discovery, or strategic queries.

**Status:** You have this (853 owned + 700 starred indexed locally).

---

## Level 2: Repository Registry

Every repo becomes an **entity** with metadata + strategic fields.

| Field group | Examples |
|-------------|----------|
| Git metadata | name, owner, language, stars, license, url |
| Intelligence | purpose, capabilities, dependencies, tech_stack |
| Venture | related_ventures, venture_tier, decision_action |
| Graph prep | graph_edges, related_repositories |

**Artifact:** `repository_registry_pilot.csv`  
**Script:** `repo_classification_pilot.py`  
**Status:** ✅ Pilot runnable (deterministic, no API)

---

## Level 3: Repository Intelligence

AI-generated summaries beyond metadata:

- Problem solved, target user, inputs/outputs
- Use cases, alternatives, commercial potential

**Artifact:** `repository_registry_pilot.json` (rich records) + optional LLM pass  
**Script:** `repo_classification_phase1.py --llm` (enrichment on Tier 1–2 only)  
**Status:** 🔶 Heuristic summaries in pilot; full LLM enrichment queued

---

## Level 4: Embeddings (RAG)

Chunk README, docs, architecture → vector store.

**Ask:** "Which repos help with workflow automation?" / "Which replace Zapier?"

**Stack (already in ecosystem):**
- LightRAG (`iza-os-rag` skill) — vault + ventures
- pgvector / Supabase — structured + semantic
- Chroma — venture-hub pattern

**Status:** 🔶 LightRAG exists; repo README ingest not wired to registry yet

---

## Level 5: Knowledge Graph

RAG alone misses **relationships**.

**Nodes:** REPOSITORY, VENTURE, CAPABILITY, TECHNOLOGY, TOOL, AGENT, WORKFLOW  
**Edges:** USES, ENABLES, POWERS, DEPENDS_ON, REPLACES, MONETIZES

**Artifact:** `repository_graph_edges_pilot.csv`  
**Downstream:** Neo4j / Obsidian graph sync / LightRAG entity ingest

**Status:** ✅ Pilot edges generated from venture-capability matching

---

## Level 6: Repo-to-Venture Mapping

Every repo gets a **role**:

```text
Infrastructure | Backend | Frontend | AI | Agent | Automation
Data | Analytics | Security | Revenue Product | Internal Tool
```

Mapped in registry as `venture_studio_role` + `related_ventures`.

**Active ventures (pilot scope):**
- Product: marketplace-core, CON-009–012, LT-009
- Ops: OPS-001, CON-001, RE-001

**Status:** ✅ In pilot classifier via `venture_capability_needs` in `repo_vocabulary.json`

---

## Level 7: Strategic Queries

Example prompts once L2–L5 are live:

```text
What repos help me build a marketplace?
Which repos could become standalone businesses?
Which repos overlap?
What is missing from my stack?
Which repos could be wrapped and sold?
```

**Venture architect prompt** (run against registry + graph):

```text
Act as a venture architect. Analyze my repository knowledge graph.
For every repository determine: infrastructure value, reusability, revenue potential,
strategic importance, dependencies, venture opportunities.
Produce: Core OS Stack, Shared Services, Venture Enablement, Revenue Candidates,
Ignore list, Consolidate list, Missing Components.
Optimize for leverage, reuse, and speed.
```

**Status:** 🔶 Answerable on pilot CSV today; full accuracy needs L4 ingest

---

## Pipeline (implementation map)

```text
GitHub
  ↓ clone / sync (The office/repos.json, repos-index.json)
Level 2  Extract metadata + classify     → repository_registry_pilot.csv
Level 3  AI summaries (Tier 1–2 only)    → repository-intelligence-detailed.json
Level 4  Embed READMEs/docs              → pgvector / LightRAG
Level 5  Graph edges                       → repository_graph_edges_pilot.csv → Neo4j
Level 6  Venture roles                     → venture_capability_needs mapping
Level 7  Agent query layer                 → iza-os-rag + registry SQL/CSV
```

---

## File index

| File | Level |
|------|-------|
| `repo_vocabulary.json` | L2–L6 controlled vocabulary |
| `repo_classification_pilot.py` | L2 + L3 (heuristic) |
| `repo_classification_phase1.py` | L3 (LLM enrichment) |
| `repo-classification-prompts.md` | L3 prompt templates |
| `repository_registry_pilot.csv` | L2 output |
| `repository_graph_edges_pilot.csv` | L5 output |
| `REPOSITORY-INTELLIGENCE-SYSTEM.md` | 7-layer classification framework |

---

## Next steps

1. Run `python3 repo_classification_pilot.py --pilot 100`
2. Review Tier 1–2 rows → LLM enrich with `repo_classification_phase1.py`
3. Ingest pilot registry into LightRAG (`--source=registry`)
4. Full scan: `python3 repo_classification_pilot.py --all`
5. Gap analysis: compare `marketplace-core` needs vs registry capabilities
