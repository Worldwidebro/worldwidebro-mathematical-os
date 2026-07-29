# Ferrari Activation Plan — Wire the System

**Date:** 2026-07-28  
**Goal:** Connect existing components (venture_loop, vex-api, iza-os, graphify) into one operational system  
**Timeframe:** 4 hours (Phase 1 only)

---

## Status: Pre-Activation

| Layer | Component | Status | Action |
|-------|-----------|--------|--------|
| **STRUCTURAL** | civilization-os | ✗ MISSING | Create from WORLDWIDEBRO-OS-COMPLETE-BLUEPRINT.md |
| | family-office-os | ✗ MISSING | Create (capital routing + OPCO structure) |
| | Venture folders | ✓ Exists (scattered) | Organize into 15 OPCOs |
| **OPERATIONAL** | vex-api | ✓ Exists | Add capital allocation endpoints |
| | venture_loop.py | ✓ Exists | Wire feedback loop (01_loop_feedback_collector.py exists) |
| | 01_loop_feedback_collector.py | ✓ Ready | Integrate into venture_loop |
| | 02_agent_scorer.py | ✓ Ready | Run weekly on feedback logs |
| **INFORMATION** | mathematical-os | ✗ MISSING | Organize formulas from 1,600 repos |
| | knowledge-graph-os | ✗ MISSING | Schema + ingestion (Qdrant + Neo4j) |
| | graphify_analysis.py | ✓ Exists | Extract relationships |
| **AGENTS** | iza-os-intelligence | ✓ Exists | Wire to vex-api |
| | agent-platform-os | ✗ MISSING | Create from AI-AGENT-TEAM-ARCHITECTURE.md |

---

## Phase 1: Essential Wiring (This Week)

### Step 1: Commit Learning Loop Files (30 min)
```bash
cd /Users/acebless/Documents
git add 01_loop_feedback_collector.py 02_agent_scorer.py
git commit -m "wiring: feedback loop + agent scoring"
git push origin 2026-06-19-os-consolidation
```

**Verify:**
```bash
python3 01_loop_feedback_collector.py test_run_001 success 45.50 120
python3 02_agent_scorer.py
```

---

### Step 2: Create civilization-os (1 hour)

**Source:** WORLDWIDEBRO-OS-COMPLETE-BLUEPRINT.md (already written)

**Repo:** Create `/Users/acebless/Documents/civilization-os/`

**Structure:**
```
civilization-os/
├── README.md (= WORLDWIDEBRO-OS-COMPLETE-BLUEPRINT.md)
├── ONTOLOGY.md (entities, relationships, types)
├── TOPOLOGY.md (system layers, dependencies)
├── GOVERNANCE.md (decision rights, escalation)
└── INTEGRATION.md (how each OPCO connects)
```

**Wire to:** family-office-os (capital allocation decisions reference civilization structure)

---

### Step 3: Create family-office-os (1 hour)

**Source:** OPERATIONAL-LAYER-CAPITAL-ROUTING.md + STRUCTURAL-LAYER-OPCO-ORGANIZATION.md

**Repo:** Create `/Users/acebless/Documents/family-office-os/`

**Structure:**
```
family-office-os/
├── README.md (capital allocation + OPCO structure)
├── CAPITAL-ALLOCATION.md (allocation formula, tables)
├── OPCO-STRUCTURE.md (15 OPCOs, folder templates)
├── supabase/
│   ├── migrations/
│   │   ├── opco_capital_allocations.sql
│   │   ├── capital_deployment_log.sql
│   │   └── capital_decisions.sql
│   └── schema.md
└── AGENTS.md (OPCO agent instructions)
```

**Supabase Tables:**
- `opco_capital_allocations` (id UUID, opco_name TEXT, allocation_date DATE, approved_amount DECIMAL(15,2), allocated_amount DECIMAL(15,2), status TEXT, approved_by TEXT, approval_date TIMESTAMP)
- `capital_deployment_log` (id UUID, opco_name TEXT, venture_id TEXT, amount_deployed DECIMAL(15,2), deployment_date DATE, predicted_roi_pct DECIMAL(5,2), actual_roi_pct DECIMAL(5,2), formula_used TEXT)
- `capital_decisions` (id UUID, decision_type TEXT, opco_name TEXT, amount DECIMAL(15,2), decision_maker TEXT, decision_date TIMESTAMP, reasoning TEXT, approval_status TEXT)

**Wire to:**
- vex-api (capital_allocation endpoints)
- venture_loop.py (capital deployment triggers)
- agent_scorer.py (ROI feedback → formula updates)

---

### Step 4: Wire vex-api ↔ venture_loop (1 hour)

**File:** `/Users/acebless/Documents/vex-api/src/api/capital-routing.ts` (NEW)

**What it does:**
1. Receives weekly allocation from family-office-os
2. Routes to ventures in Supabase
3. Triggers venture_loop.py to deploy capital
4. Logs predictions + actual ROI

**Connection points:**
```
family-office-os (allocation) 
  → vex-api (capital-routing endpoint)
    → Supabase (opco_capital_allocations table)
      → venture_loop.py (execute deployment)
        → 01_loop_feedback_collector.py (log outcome)
          → 02_agent_scorer.py (calculate success rate)
            → mathematical-os (update formula rankings)
```

---

### Step 5: Organize Loose Files (30 min)

| File | Current | New Home |
|------|---------|----------|
| venture_loop.py | /Documents/ | mathematical-os/loops/ |
| con-os-functions.py | /Documents/ | civilization-os/sector-os/ |
| graphify_analysis.py | /Documents/ | knowledge-graph-os/ingestion/ |
| 01_loop_feedback_collector.py | /Documents/ | mathematical-os/loops/ |
| 02_agent_scorer.py | /Documents/ | mathematical-os/loops/ |

---

## Phase 2: Knowledge Graph (Next Week)

- Create knowledge-graph-os
- Ingest 1,600 repos into Neo4j + Qdrant
- Create mathematical-os (formula index)
- Wire to agent-platform-os

---

## Test: Ferrari Runs

After Phase 1, verify:

```bash
# 1. Allocation flows
curl http://localhost:3000/api/capital-allocation

# 2. Venture loop executes
python3 venture_loop.py dispatch --opco FINANCE

# 3. Feedback collects
python3 01_loop_feedback_collector.py run_001 success 45.50 120

# 4. Scores update
python3 02_agent_scorer.py

# 5. Check Supabase
SELECT COUNT(*) FROM opco_capital_allocations;
SELECT COUNT(*) FROM capital_deployment_log;
```

---

## Why This Order

1. **Feedback loop first** (01/02) — enables learning
2. **Civilization** — defines what we're organizing
3. **Family-office** — routes capital based on civilization structure
4. **vex-api wiring** — connects family-office to ventures
5. **Loose files** — find their homes once homes exist

No new frameworks. Just organizing what exists + connecting pipes.

---

**Status:** Ready to execute. 4 hours to Phase 1 complete.
