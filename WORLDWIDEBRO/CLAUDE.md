# CLAUDE.md — Worldwidebro Operating Constitution

**Version:** 1.0  
**Effective:** 2026-08-04  
**Authority:** CEO / System Architect  
**Scope:** WORLDWIDEBRO system operations

---

## ONE RULE (Non-Negotiable)

**Verify before claiming it works.**

- Check: actual metrics, live systems, real output
- Never trust: documentation, assumptions, "should be working"
- If uncertain: **ask before retrying** — don't loop blindly

---

## CANONICAL IDENTITY

**System Name:** WORLDWIDEBRO (World model + 712+ ventures + operating system)

**Not separate systems:** AI-BOSS, IZA-OS, VEX, AVS are layers/interfaces within WORLDWIDEBRO, not competing systems.

```text
ONE WORLD MODEL (Neo4j)
        │
    ┌───┼───┬───┬───┐
    │   │   │   │   │
   06  05  14  15  ...
  AGENTS BRAIN BUSINESS INDUSTRIES
 (Orchestration) (Intelligence) (Commerce) (Sectors)
```

---

## 20 OPERATIONAL RULES

### Identity (1-3)
1. **WORLDWIDEBRO is canonical.** All entities resolve here. No competing "OS" folders.
2. **Neo4j is the world model.** Graph is truth. Files are storage. Queries are reason.
3. **Aliases resolve to one entity.** MATCH (n)-[:ALIAS_OF]->(canonical) connects AI-BOSS, IZA-OS, etc.

### Structure (4-6)
4. **17 portfolios are views, not trees.** One graph, multiple lenses. No duplication.
5. **Folders organize artifacts; relationships organize meaning.** Graph, not filesystem.
6. **Search before creating. Reuse before rebuilding.** If it exists in Neo4j, use it.

### Knowledge (7-9)
7. **Every asset must be discovered and classified.** No dark data.
8. **Every important asset has an owner.** Orphaned entities get escalated.
9. **Every relationship has a reason.** A uses B means B is actually used.

### Execution (10-13)
10. **Qdrant retrieves context; Neo4j is truth.** Vectors help, graphs decide.
11. **Every decision is recorded.** Who? Why? Confidence? Expected outcome?
12. **Every execution is observable.** Full trace from decision to result.
13. **Every outcome is verified.** Require evidence, not claims.

### Failure & Learning (14-17)
14. **Failures produce recovery.** Detect, fix, or escalate automatically.
15. **Recoveries are recorded.** How we fixed it. Will it work next time?
16. **Learning updates the world model.** Improvements persist in Neo4j.
17. **Agent confidence tracks accuracy.** Good decisions increase score. Bad decrease.

### Technology (18-20)
18. **Tech decisions map to business outcomes.** Optimize for revenue, cost, autonomy.
19. **Naming aliases are metadata, not systems.** Everything resolves canonically.
20. **No competing registries.** Query Neo4j, don't duplicate it.

---

## DATABASES (All Local, Live)

| Service | Port | Type | Location | Verify |
|---------|------|------|----------|--------|
| **Postgres** | 5432 | Operational state | Mac Studio | `psql -U postgres -d ventures` |
| **Neo4j** | 7687 | World model | Mac Studio | `curl http://localhost:7474` |
| **Qdrant** | 6333 | Semantic search | Mac Studio | `curl http://localhost:6333/health` |
| **Redis** | 6379 | Cache/sessions | Mac Studio | `redis-cli PING` |
| **Langfuse** | 3003 | LLM observability | Mac Studio | `curl http://localhost:3003` |

**All running:** `docker ps | grep -E "neo4j|qdrant|postgres|redis|langfuse"`

---

## FOLDER STRUCTURE (21 Tiers)

```
WORLDWIDEBRO/
├── 00_IDENTITY/        Company, mission, aliases
├── 01_DIRECTIVES/      Strategy, policies, current directives
├── 02_EXECUTIVES/      Roles, authority, governance
├── 03_PORTFOLIOS/      17 views: Business, Software, Capital, ...
├── 04_PROJECTS/        Work: active, planned, blocked, completed
├── 05_AI-BRAIN/        Knowledge, graph, vectors, memory
├── 06_AGENTS/          Agents by domain
├── 07_SKILLS/          Skill catalog
├── 08_MCP/             API/tool integrations
├── 09_WORKFLOWS/       Business processes
├── 10_DECISION-ENGINE/ Routing, prioritization
├── 11_EXECUTION/       Running tasks, jobs
├── 12_VERIFICATION/    Tests, quality, completion
├── 13_LEARNING/        Feedback, failures, improvements
├── 14_BUSINESS/        Ventures, revenue, customers
├── 15_INDUSTRIES/      By sector: LT, FIN, CON, RE, ...
├── 16_DATA/            Datasets, exports, backups
├── 17_INFRASTRUCTURE/  Devices, Docker, databases, storage
├── 18_OBSERVABILITY/   Dashboards, metrics
├── 19_TESTS/           Unit, integration, system, autonomy
├── 20_DOCS/            Architecture, guides, research
└── 99_ARCHIVE/         Old systems, deprecated, completed
```

---

## TWO INVARIANTS

1. **Ventures live in Supabase/Neo4j, not files.** Supabase is operational truth. Neo4j is world model.
2. **All code goes through Git + PR.** No direct DB edits except migrations.

---

## THREE SOURCES OF TRUTH (Order)

1. **VENTURE-READINESS-SCORECARD.csv** — Single source for venture state
2. **Neo4j graph** — Entity status, relationships, dependencies
3. **Postgres/Supabase** — Live transactional data

**Rule:** Check CSV first. Never guess.

---

## PROOF: THE AUTONOMY TEST

Your system is alive when it can autonomously:

```
DISCOVER → RETRIEVE → DECIDE → EXECUTE → VERIFY → RECOVER → REMEMBER → LEARN
```

**Single objective test:** "Acquire one medical logistics customer" and trace the complete loop without human intervention.

---

## SESSION START

1. Load sector context (LT/FIN/CON/RE)?
2. Verify infrastructure (docker ps)?
3. Check sources of truth (CSV first)?
4. Set venture context (which venture)?
5. Clarify mission (what are we optimizing for)?

---

**Version:** 1.0  
**Effective:** 2026-08-04  
**Authority:** System Architect  
**Scope:** WORLDWIDEBRO operations
