# Sector Readiness — Grounded in Actual Agent Implementations

**Date:** 2026-07-20  
**Basis:** Real agent code in `/Users/acebless/Documents/WORLDWIDEBRO-OS/05-AGENTS/`  
**Status:** What exists vs. what's needed to run each sector

---

## Real Agent Infrastructure (Verified Code)

### 1. AgentFactory (agent_factory.py)
- **What it does:** Spawns a venture folder with standardized structure
- **Inputs:** Venture name + sector
- **Outputs:** 
  - `00_IDENTITY/venture_profile.md` (venture profile)
  - `01_STRATEGY/business_model.md` (business model)
  - `08_TECHNOLOGY/repository_map.md` (tech stack)
  - `09_AI_AGENTS/agent_registry.yaml` (agent config)
  - `venture.json` (state tracking)
  - `14_ANALYTICS/KPI_dashboard.json` (KPI tracking)
- **Status:** ✅ Working (creates folder + files)
- **Zero-token operations:** All local file I/O

### 2. Hermes Agent (hermes.py)
- **What it does:** Chief Operating Intelligence with decision routing
- **Authority tiers:**
  - `<$5K` → auto-approve (execute)
  - `$5K-$25K` → escalate to director
  - `>$25K` → escalate to Hermes (wait for Claude reasoning)
  - Irreversible decisions → escalate to human
- **Output format:** JSON (decision_id, venture_id, amount, authority_required, action)
- **Model:** Claude Opus 4.8
- **Status:** ✅ Working (demo runs successfully)
- **Cost:** ~300 tokens per decision

### 3. AgentTeamOrchestrator (run_agent_team.py)
- **What it does:** Maps agent roles to local task execution
- **Currently implemented tasks:**
  1. `compile-outreach` → runs `compile_outreach.py` (0 tokens, local)
  2. `db-dedupe` (AG-CAO only) → runs `dedupe_twenty_companies.py` (0 tokens, local)
  3. `repo-scan` (AG-CTO only) → runs `scan_repositories.py` (0 tokens, local)
- **Logging:** Writes `agent_execution_logs.jsonl` per venture
- **Status:** ✅ Working for 3 task types
- **Gap:** Only 3 task types mapped; 50+ needed for sector automation

---

## Per-Sector Readiness (What Runs Now)

### CON-001: Construction (120 ventures total)
| Layer | What Exists | What's Needed | Hours to Fix |
|-------|------------|---------------|-------------|
| **Agent Layer** | Hermes (routing), AgentFactory (spawn) | CEO, CTO, CFO agents + task mapping | 8 |
| **Task Layer** | compile-outreach (0 tokens) | estimate, photos, schedule, CRM sync | 16 |
| **Data Layer** | venture.json, agent_registry.yaml | Lead intake form, photo pipeline, contract gen | 12 |
| **Runnable Now?** | ❌ No | Must wire 3+ agents + 5+ tasks | 36 |
| **Bottleneck** | Only 1 task implemented (outreach) | Task-to-agent mapping incomplete | — |

**How to run CON right now:**
```bash
python3 agent_factory.py "My Construction Co" construction
cd my-construction-co/
python3 /Users/acebless/Documents/WORLDWIDEBRO-OS/05-AGENTS/orchestration/run_agent_team.py . AG-CEO compile-outreach
# Result: Outreach templates compiled locally (0 tokens, works)
```

### STA-001: Staffing (95 ventures total)
| Layer | What Exists | What's Needed | Hours to Fix |
|-------|------------|---------------|-------------|
| **Agent Layer** | Hermes (routing), AgentFactory (spawn) | CEO, sourcing agent, matching agent | 8 |
| **Task Layer** | compile-outreach (0 tokens) | candidate-match, availability-sync, placement-approval | 16 |
| **Data Layer** | venture.json | Candidate database schema, Neo4j graph | 8 |
| **Runnable Now?** | ❌ No | Must wire candidate matching + Hermes approval flow | 32 |
| **Bottleneck** | Generic outreach only; no matching logic | Candidate database + ML-ready matching scores | — |

**To make STA runnable:**
- Neo4j must have candidate-graph (500 candidate nodes min)
- Matching algorithm must score compatibility (3-5 feature vectors)
- Placement approval must route through Hermes at $500-2000 thresholds

### RE-001: Real Estate (110 ventures total)
| Layer | What Exists | What's Needed | Hours to Fix |
|-------|------------|---------------|-------------|
| **Agent Layer** | Hermes (routing), AgentFactory (spawn) | CEO, listing agent, market analyst | 8 |
| **Task Layer** | compile-outreach (0 tokens) | list-property, market-analysis, lead-nurture | 20 |
| **Data Layer** | venture.json | Property listings (SQL), market comps (Qdrant vectors) | 12 |
| **Runnable Now?** | ❌ No | Must wire property listing + market data pipeline | 40 |
| **Bottleneck** | No property data integration; market data static | Need real MLS/Zillow integration or mock data | — |

### EDU-001: Education (85 ventures total)
| Layer | What Exists | What's Needed | Hours to Fix |
|-------|------------|---------------|-------------|
| **Agent Layer** | Hermes (routing), AgentFactory (spawn) | CEO, curriculum agent, instructor-match | 8 |
| **Task Layer** | compile-outreach (0 tokens) | enroll-student, generate-curriculum, track-progress | 20 |
| **Data Layer** | venture.json | Course catalog (Neo4j), student progress (Supabase) | 10 |
| **Runnable Now?** | ❌ No | Must wire course + student data + completion tracking | 38 |
| **Bottleneck** | No course schema; progress tracking missing | Need course graph + completion milestones | — |

### FIN-001: Finance (105 ventures total)
| Layer | What Exists | What's Needed | Hours to Fix |
|-------|------------|---------------|-------------|
| **Agent Layer** | Hermes (routing + amount-based approval), AgentFactory (spawn) | CEO, analyst, risk agent | 8 |
| **Task Layer** | compile-outreach (0 tokens) | risk-score, deal-approval, position-size | 24 |
| **Data Layer** | venture.json | Position ledger, risk model (Neo4j), portfolio state | 12 |
| **Runnable Now?** | ⚠️ Partial | Hermes decision routing works; risk logic missing | 44 |
| **Bottleneck** | Risk scoring not implemented; position sizing manual | Need risk model in Neo4j + position-sizing algorithm | — |

### LOG-001: Logistics (197 ventures total)
| Layer | What Exists | What's Needed | Hours to Fix |
|-------|------------|---------------|-------------|
| **Agent Layer** | Hermes (routing), AgentFactory (spawn) | CEO, dispatcher, route-optimizer | 8 |
| **Task Layer** | compile-outreach (0 tokens) | dispatch-job, optimize-route, track-shipment | 24 |
| **Data Layer** | venture.json | Shipment ledger (Supabase), route graph (Neo4j) | 12 |
| **Runnable Now?** | ❌ No | Must wire job dispatch + route optimization | 44 |
| **Bottleneck** | No job/shipment data; no route optimizer | Need job schema + TSP solver or routing API | — |

---

## What's Runnable RIGHT NOW (No Hours Needed)

### 1. Venture Spawning
```bash
python3 agent_factory.py "Test Venture" construction
# Creates: venture folder + agent_registry.yaml + KPI dashboard
# Status: ✅ Works immediately
```

### 2. Outreach Compilation
```bash
cd <venture-folder>
python3 /path/to/run_agent_team.py . AG-CEO compile-outreach
# Generates: outreach templates (0 tokens, local file I/O)
# Status: ✅ Works immediately
```

### 3. Decision Routing (Hermes)
```bash
python3 hermes.py  # Pass decision JSON
# Routes: <$5K (auto) → $5-25K (director) → >$25K (Claude) → irreversible (human)
# Status: ✅ Works immediately
```

---

## What's NOT Runnable (Blockers)

| Blocker | Affects | Fix Hours | Why |
|---------|---------|-----------|-----|
| Only 3 tasks mapped | All sectors (5+) | 40 | Each sector needs 8+ task types; only compile-outreach, db-dedupe, repo-scan exist |
| No candidate/property/course data | STA, RE, EDU | 30-40 | No schema, no data pipeline, no integration |
| Risk scoring not implemented | FIN | 20 | Hermes routes decisions but risk model is empty |
| Neo4j graph not populated | STA (candidates), LOG (routes) | 16 | Neo4j container may not be running; no data loader |
| Matching algorithm missing | STA (main blocker) | 16 | Can't execute placements without compatibility scoring |

---

## Minimum Viable Path to "First Sector Running"

**Target: Make CON (Construction) autonomous in 48 hours**

### Phase 1: Wire Missing Tasks (24 hours)
1. Map `estimate-job` task → call estimation logic (**4h**)
2. Map `photo-intake` task → webhook to photo service (**4h**)
3. Map `contract-gen` task → call contract templates (**4h**)
4. Map `schedule-inspection` task → call calendar API (**4h**)
5. Map `send-invoice` task → call invoicing MCP (**4h**)
6. **Result:** 5 new task types available for AG-CEO

### Phase 2: Test Full Workflow (24 hours)
1. Spawn a test venture (**1h**)
2. Run compile-outreach → estimate-job → photo-intake → contract-gen (**4h**)
3. Route $5K proposal through Hermes (**2h**)
4. Create simple e2e test (**4h**)
5. Document "How to run CON sector" (**3h**)
6. **Result:** CON sector is functional end-to-end

### By End of Phase 2:
- ✅ Construction ventures can accept jobs
- ✅ Outreach → estimate → contract → invoice (full pipeline)
- ✅ Hermes routes approval decisions
- ✅ Agents log execution to venture JSON
- ✅ You can measure: deals/week, pipeline, revenue

---

## Next 48 Hours (Reality-Based)

**Do NOT build theoretical PRDs. Execute this:**

1. **Hour 1-8:** Wire 5 missing task types into AgentTeamOrchestrator
   - File: `/Users/acebless/Documents/WORLDWIDEBRO-OS/05-AGENTS/orchestration/run_agent_team.py`
   - Pattern: Copy `db-dedupe` task block 5 times, map to real scripts

2. **Hour 8-16:** Create or mock data for first sector (CON)
   - venture.json structure exists
   - Add JSON sample with 3 sample jobs

3. **Hour 16-32:** Run full e2e test (spawn venture → run 5 tasks → Hermes approval)
   - Bash script: loop through tasks, collect logs

4. **Hour 32-48:** Repeat for STA (Staffing) with candidate matching as proof-of-concept
   - Add mock candidate database (Neo4j or JSON)
   - Add simple scoring algorithm

**Result after 48h:**
- 2 sectors (CON + STA) with wired agents
- ~30 lines of new code per task
- Full e2e logs showing Hermes routing + task execution
- Proof that the system works end-to-end

---

## File References

**Agent Code:**
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/05-AGENTS/agent_factory.py`
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/05-AGENTS/hermes.py`
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/05-AGENTS/orchestration/run_agent_team.py`

**Registry:**
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/sector_registry.yaml`
- `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/registries/agent_registry.yaml`

**Supporting Scripts (need to map):**
- `compile_outreach.py` (exists, working)
- `dedupe_twenty_companies.py` (exists, mapped)
- `scan_repositories.py` (exists, mapped)

---

## The Real Gap

You have **3 agent implementations** (Factory, Hermes, Orchestrator) and **1 working task type** (compile-outreach).

You need **50+ task types** wired in (estimate, photo, contract, schedule, invoice, match, dispatch, analyze, etc.).

**That's the work. Not theory. Just mapping tasks to scripts.**

---

*This document is based on code that exists and runs. Not a roadmap. An inventory.*
