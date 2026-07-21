---
type: chat-summary
date: 2026-07-21
duration: 1 hour (05:45am - 05:55am EDT)
topic: Data Pipeline Architecture & System Integration
---

# Chat Summary: Data Pipeline & Orchestration (2026-07-21)

**User Question:** Where do files live, what's completed, what's understood about vex, what's left?

---

## Files From This Chat: Where They Live

### Created (In .planning/)
| File | Created | Status | Purpose |
|------|---------|--------|---------|
| `.planning/PROJECT-INDEX.md` | ✅ This chat | Live | 5-wave master plan (entry point) |
| `.planning/PROJECT-CODE-CONSOLIDATION.md` | ✅ This chat | Live | Wave 2 spec: extract 380+ duplicates |
| `.planning/PROJECT-INFRASTRUCTURE-DOCS.md` | ✅ This chat | Live | Wave 3 spec: 100-map atlas |
| `.planning/PROJECT-SYSTEM-VERIFICATION.md` | ✅ This chat | Live | Wave 5 spec: end-to-end proof |
| `.planning/CHAT-2026-07-21-DATA-PIPELINE-SUMMARY.md` | ✅ This file | Live | This summary |

### Referenced (Already Exist)
| File | Location | Purpose |
|------|----------|---------|
| `populate_venture_knowledge_graph.py` | `/Documents/` | Sync Supabase → Neo4j |
| `obsidian_graph_sync.py` | `/Documents/` | Export graph to Obsidian |
| `sync_ventures_to_notion.py` | `/Documents/` | Sync ventures → Notion |
| `populate_twenty_ventures.py` | `/Documents/` | Sync ventures → TwentyHQ |
| `dedupe_twenty_companies.py` | `/Documents/` | Remove CRM duplicates |
| `find_duplicate_repos.py` | `/Documents/` | Detect repo clones |
| `run_repo_intelligence_pipeline.py` | `/Documents/` | Scan repos for capabilities |
| `operating_system_schema.sql` | `/Documents/` | Master DB schema |
| `TOOL_CAPABILITY_MAP.md` | `/Documents/` | Business goals → MCPs |
| `vex-hero-site/` | `/Documents/vex-hero-site/` | Public venture directory |
| `WORLDWIDEBRO-OS/` | `/Documents/WORLDWIDEBRO-OS/` | Master venture registry |

---

## What's Been Completed

### Analysis ✅
- ✅ Located all 7 sync scripts (exist but unorchestrated)
- ✅ Identified critical gap: **no orchestrator.py**
- ✅ Verified databases are running (Neo4j, Qdrant, Supabase, DuckDB)
- ✅ Mapped connection between 5-wave plan and data pipeline

### Understanding ✅
- ✅ **Architecture correction:** IZA OS (infrastructure) ≠ venture
- ✅ **Data flow model:** Events → Supabase → Sync → Query
- ✅ **Workflow philosophy:** Code-first (Python/TypeScript/Bash), not n8n-first
- ✅ **Knowledge engineering pattern:** 7-layer deduplication (inventory → fingerprint → classify → relate → cluster → enrich → synthesize)
- ✅ **What vex is:** Public venture directory (React app, Vercel deployed, currently reads static data)

### Documentation ✅
- ✅ 5-wave plan with explicit dates (2026-07-21 → 2026-08-04)
- ✅ 4 project specs with checklists and success criteria
- ✅ Master outcome defined: "production-ready infrastructure, <1% error, <500ms latency"

---

## What's Understood About Vex

**vex-hero-site** = `/Documents/vex-hero-site/` (React app, Vercel deployed)

### Current State
- ✅ Live at vex-hero-site (public URL)
- ✅ Displays all 712 ventures by sector
- ✅ Shows venture details, capabilities, status
- ❌ Reads **static JSON exports**, not live databases
- ❌ Not connected to Supabase, Neo4j, or real-time data

### In The 5-Wave Plan
- **Wave 2-3:** Code consolidation + infrastructure docs (prep work)
- **Wave 4:** Wire MCP + Neo4j schema enhancements
- **Wave 5:** **Rebuild vex to query live databases**
  - Change: static JSON → live Supabase queries
  - Prove: all 16 sector pages render in browser
  - Verify: real-time data updates work
  - Timeline: 2-3 hours (2026-07-30 → 2026-08-04)

### Dependency Chain
```
vex needs live data
    ↓
Live data needs orchestrator.py
    ↓
Orchestrator needs 7 sync scripts tested
    ↓
Tests need disk space (Wave 0 cleanup)
```

---

## What's Left to Do

### Immediate (Blocking Everything)
❌ **Build orchestrator.py** — Chain 7 sync scripts
   - Status: Does not exist
   - Effort: 1-2 hours
   - Blocker for: Waves 1-5

❌ **Test each sync script** — Verify which work fully
   - `populate_twenty_ventures.py` — partial (371/713 companies)
   - `sync_ventures_to_notion.py` — untested
   - `dedupe_twenty_companies.py` — needs flag
   - `find_duplicate_repos.py` — untested
   - `run_repo_intelligence_pipeline.py` — untested
   - Effort: 1-2 hours per script
   - Blocker for: Waves 1-5

❌ **Add cron job** — Automate nightly sync
   - Status: Not configured
   - Effort: 30 minutes
   - Blocker for: Wave 1+

### Wave 0 (Disk Cleanup - **Currently Blocking Waves 1-5**)
⏳ **Recovery in progress**
   - MacBook Air: 95% full (19GB free of 460GB) — need 100GB+
   - Mac Studio: 94% full (29GB free of 460GB) — need 100GB+
   - Status: Cleanup scripts mentioned as "running"
   - Timeline: 6-8 hours (2026-07-21 → 2026-07-22)
   - **This must complete before Wave 1 starts**

### Wave 1 (Analysis Agents - Blocked by Wave 0)
⏳ **Parallel agents analyze codebase**
   - Serena: Code duplication detection
   - Graphify: Venture relationship mapping
   - SocratiCode: Semantic indexing
   - GitNexus: Impact analysis
   - Timeline: 4-6 hours (2026-07-22 → 2026-07-23)
   - **Depends on:** Wave 0 ✓

### Waves 2-3 (Parallel: Code Consolidation + Infrastructure Docs)
⏳ **Wave 2: Code Consolidation** (3-4 hours, 2026-07-24 → 07-26)
   - Extract 380+ duplicates → shared-venture-lib
   - Create venture template scaffold
   - Generate before/after metrics
   - **Depends on:** Wave 0 ✓

⏳ **Wave 3: Infrastructure Docs** (4-5 hours, 2026-07-24 → 07-27)
   - 5 new topology docs
   - Extend Neo4j schema (9 entities, 8 relationships)
   - Prove 3 Cypher views work
   - **Depends on:** Wave 0 ✓

### Wave 4 (MCP + Schema - Depends on Waves 2-3)
⏳ **Deploy MCP servers + enhance Neo4j** (3-4 hours, 2026-07-28 → 07-29)
   - Wire MCP tools to schema
   - Connect Ollama to agents
   - Verify data flows through system
   - **Depends on:** Waves 2 ✓ + 3 ✓

### Wave 5 (System Verification - Depends on Waves 2-4)
⏳ **Rebuild vex + prove end-to-end** (2-3 hours, 2026-07-30 → 08-04)
   - Rebuild vex-hero-site to query live databases
   - Wire MCP Ollama queries
   - Run 100 Cypher views against live data
   - Verify all 16 sector pages render
   - **Depends on:** Waves 2 ✓ + 3 ✓ + 4 ✓
   - **Proves:** vex reads real data, not static JSON

---

## Summary Table

| Item | Status | Effort | Blocker? |
|------|--------|--------|----------|
| **Orchestrator.py** | ❌ Missing | 1-2h | YES (everything) |
| **Test 7 sync scripts** | ⏳ Partial | 2-3h | YES (Waves 1+) |
| **Add cron job** | ❌ Missing | 30m | YES (Wave 1+) |
| **Wave 0 (Disk)** | 🟡 In progress | 6-8h | YES (all Waves) |
| **Wave 1 (Agents)** | 🟡 Queued | 4-6h | Depends on Wave 0 |
| **Wave 2 (Code)** | 🟡 Ready | 3-4h | Depends on Wave 0 |
| **Wave 3 (Docs)** | 🟡 Ready | 4-5h | Depends on Wave 0 |
| **Wave 4 (Schema)** | 🟡 Ready | 3-4h | Depends on Waves 2-3 |
| **Wave 5 (Verify + vex)** | 🟡 Ready | 2-3h | Depends on Waves 2-4 |
| **Master Outcome** | 🟡 On track | 2 weeks total | Depends on all Waves |

---

## Next Decision

**User asked "what's left?"** — Here's the critical path:

```
NOW (Today)
    ├─ Finish Wave 0 disk cleanup (in progress)
    ├─ Build orchestrator.py (1-2h, unblocks everything)
    └─ Test each sync script (2-3h, unblocks Waves 1+)

Then (2026-07-22)
    └─ Run Wave 1 agents (4-6h)

Then (2026-07-24)
    ├─ Wave 2: Code consolidation (parallel)
    └─ Wave 3: Infrastructure docs (parallel)

Then (2026-07-28)
    └─ Wave 4: MCP + Neo4j schema

Finally (2026-07-30)
    └─ Wave 5: Rebuild vex + end-to-end verification
```

**Recommendation:** Don't wait for perfect Wave 0. Start orchestrator.py while disk cleanup runs (different resources — I/O vs. CPU).
