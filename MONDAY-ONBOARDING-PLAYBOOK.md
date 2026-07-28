---
name: monday-launch-playbook
description: Worldwidebro OS + vex onboarding runbook — Monday (Jul 28, 2026)
metadata:
  type: operations
  audience: founders, investors, operators
  status: LIVE
  updated: 2026-07-25
---

# Worldwidebro OS + VEX — Monday Launch Playbook

**Date:** Monday, July 28, 2026  
**Founder:** Antwuan Johns (@worldwidebro)  
**Status:** Operating system live. 712 ventures registered. 5 main ventures active.  

---

## What Is This?

**Worldwidebro Holdings** = Holding company + operating system for venture creation, capital allocation, and autonomous execution.

**VEX** = Public portfolio interface (what investors/partners see at vex-hero-site).

**IZA OS** = Infrastructure layer (what powers everything behind the scenes).

This playbook is how we **onboard, execute, and scale** ventures within the system.

---

## Where We Are RIGHT NOW

### Infrastructure ✅

| Component | Status | Access |
|-----------|--------|--------|
| **Neo4j** | Running | http://localhost:7474 (2,618 nodes, 11,134 edges) |
| **Qdrant** | Running | http://localhost:6333 (1,648 embeddings) |
| **PostgreSQL** | Running | localhost:5432 (Supabase) |
| **Redis** | Running | localhost:6379 (caching) |
| **Ollama** | Mac Studio:11434 | qwen2.5:32b, qwen3:8b (local models) |
| **Tailscale** | Connected | Private network: 100.121.17.63 (MacBook) ↔ 100.87.214.70 (Mac Studio) |
| **vex-hero-site** | Deployed | http://localhost:5173 (React, live) |

### Data Layer ✅

| Source | Location | Purpose |
|--------|----------|---------|
| **Venture Registry** | VENTURES-CAPABILITIES-MAPPED.csv | 712 ventures, sectors, OPCO mapping |
| **Repo Intelligence** | repo-capabilities-backfill.json | 1,639 repos, capability coverage |
| **Venture Readiness** | VENTURE-READINESS-SCORECARD.csv | Completion % per venture |
| **Portfolio** | vex-hero-site/src/data/portfolio.public.json | Public-facing venture showcase |

### 5 Main Ventures (Active)

| Venture | Sector | Stage | Status |
|---------|--------|-------|--------|
| **CON-001: Ace Construction** | Construction | MVP | ✅ Leads flowing, Stripe live |
| **TECH-062: IZA OS** | Technology | MVP | ✅ Founder showcase (vex hero) |
| **STA-001: Staffing OS** | Staffing | MVP | ✅ 74 qualified prospects |
| **RE-001: Real Estate** | Real Estate | MVP | ✅ Market analysis live |
| **FIN-001: Finance OS** | Finance | MVP | ✅ Strategic priority |

**Note:** Other 707 ventures exist in registry. Can activate on demand (5 min each).

---

## Tier 1 Documentation (Complete — Monday Ready) ✅

### Strategic Foundation

| Document | Purpose | Status |
|----------|---------|--------|
| BUSINESS.md | Mission, vision, 4-layer capital model, OPCOs | ✅ |
| OPERATING-MODEL.md | Work flow, approvals, margin capture, delegation mechanics | ✅ |
| DELEGATION-NETWORK.md | 8-layer sector connections, arbitrage matrix | ✅ |
| FUNDING-SOURCES.md | 6 funding types: bootstrap, grants, RBF, debt, equity, gov | ✅ |
| FINANCIAL-OPERATIONS.md | Complete financial stack: funding, credit, insurance, taxes, daily ops | ✅ |
| STAFFING-INDUSTRY-PLAYBOOK.md | STA-001 business model, funnel, operations, financials | ✅ |
| CONSTRUCTION-INDUSTRY-PLAYBOOK.md | CON-001 business model, project execution, crew management | ✅ |
| SECTOR-INTEROPERABILITY-MAP.md | 8-layer API architecture, 5 core hubs, unified gateway | ✅ |

---

## What We're Building (Execution Plan)

### Phase 1: Monday Launch (July 28)

✅ **COMPLETE — All Tier 1 Docs:**
- Strategic foundation: BUSINESS, OPERATING-MODEL, DELEGATION-NETWORK
- Financial architecture: FUNDING-SOURCES, FINANCIAL-OPERATIONS
- Industry playbooks: STAFFING, CONSTRUCTION
- API architecture: SECTOR-INTEROPERABILITY-MAP
- Infrastructure: Neo4j (2,618 nodes), Qdrant (1,648 vectors), PostgreSQL, Redis, Ollama, Tailscale ✅

⏳ **This Week (Mon-Wed):**
- Test 5-sector critical path (FIN→STA→CON→RE→VEX)
- Deploy vex-api backend (npm install → config → verify endpoints)
- Confirm financial workflows (payroll, AP/AR, tax, capital approval)
- Update this playbook with launch verification checklist

✅ **READY TO LAUNCH:**
- Corporate strategy (BUSINESS.md)
- Operational model with financial approvals (OPERATING-MODEL.md)
- Sector delegation flows (DELEGATION-NETWORK.md)
- Complete financial operations (FINANCIAL-OPERATIONS.md)
- Industry playbooks with unit economics (STAFFING, CONSTRUCTION)
- API architecture for 38-sector interoperability (SECTOR-INTEROPERABILITY-MAP.md)

### Phase 2: Autonomous Scaling (August)

- Activate 20-50 ventures in parallel
- Deploy VEX orchestration (opportunities, delegations, margins)
- Policy engine (approval thresholds, reinvestment rules)
- Real-time dashboard (KPIs, cash, delegation velocity)

### Phase 3: Capital Layers (September+)

- Layer 2 products ($20K-$30K/mo)
- Layer 3 acquisitions ($24K-$75K/mo)
- Layer 4 investments ($8K-$15K/mo)

---

## Monday Morning Checklist

### What Works NOW (Use This)

- ✅ Add venture to CSV
- ✅ Neo4j shows venture
- ✅ vex displays it
- ✅ Supabase tracks phases
- ✅ Ollama executes skills locally

### What's Manual (Acceptable for Now)

- ⏳ Phase execution (Python script, not automated)
- ⏳ Evolver optimization (runs, but not integrated)
- ⏳ Dashboard (use Neo4j browser)
- ⏳ Fractal orchestration (not needed yet for 5 ventures)

### What's Blocked (Don't Use)

- ❌ Automatic phase parallelization
- ❌ Budget enforcement
- ❌ Approval gates
- ❌ Multi-venture parallel execution

---

## How to Onboard a Venture (Monday)

### 5-Minute Process

**Step 1: Add to Registry**
```bash
# Edit VENTURES-CAPABILITIES-MAPPED.csv
# Add one line:
CON-002,New Venture Name,Construction,MVP

# Save and commit
git add VENTURES-CAPABILITIES-MAPPED.csv
git commit -m "Add CON-002 to registry"
```

**Step 2: Sync to Graph**
```bash
python3 populate_venture_knowledge_graph.py
# Takes ~30 seconds
# Writes to Neo4j, Qdrant, Supabase
```

**Step 3: Verify**
```bash
# Check Neo4j
open http://localhost:7474
# Query: MATCH (v:Venture {id:'CON-002'}) RETURN v

# Check vex
open http://localhost:5173/dashboard
# CON-002 appears in list
```

**Step 4: Execute Phase 1**
```bash
python3 execute_phase.py --venture CON-002 --phase 1
# Phase 1 = Setup (initialize branch, create STATUS.md, sync data)
# Takes ~2 minutes
```

**Step 5: Confirm Completion**
```bash
# Check Supabase
supabase db pull  # or open dashboard
SELECT * FROM phase_executions WHERE venture_id='CON-002'
# Should show: phase_id=1, status=completed
```

**Done.** Venture is operational.

---

## How to Execute a Phase (Monday+)

### Phases 1-5 (Available Now)

| Phase | Name | Skills | Duration | Who |
|-------|------|--------|----------|-----|
| 1 | Setup | Initialize branch | ~2 min | Automated |
| 2 | Discovery | Research venture market | ~15 min | Agent (Ollama) |
| 3 | Strategy | Define positioning | ~15 min | Agent (Ollama) |
| 4 | Planning | Create roadmap | ~20 min | Agent (Ollama) |
| 5 | Specification | Write spec | ~25 min | Agent (Ollama) |

### Phases 6-14 (Coming Soon)

Will add as Phase 1-5 stabilize.

### To Execute Manually

```bash
# Run phase executor
python3 execute_phase.py \
  --venture CON-001 \
  --phase 2 \
  --model ollama  # local; or claude-opus for quality

# Output:
# - Writes phase output to venture branch
# - Logs to Supabase (phase_executions)
# - Reports cost/duration
# - Flags blockers
```

---

## Where Data Lives

### For Operations

| Need | Location | Access |
|------|----------|--------|
| **Venture status** | Supabase (venture_runs table) | Browser query |
| **Phase progress** | Supabase (phase_executions table) | Browser query |
| **Venture details** | Neo4j | http://localhost:7474 |
| **Repo intelligence** | Qdrant (embeddings) | Python API |
| **Public portfolio** | vex-hero-site | http://localhost:5173 |

### For Development

| Need | Location | Access |
|------|----------|--------|
| **Venture registry** | VENTURES-CAPABILITIES-MAPPED.csv | Git repo |
| **Phase definitions** | phase_definitions.yaml | Git repo (not yet) |
| **Phase skills** | phase_*.md files | Git repo (foundation only) |
| **Execution scripts** | execute_phase.py, populate_venture_knowledge_graph.py | Git repo |
| **Evolver config** | .env + .evolver/ | Local |

---

## Success Metrics (Monday = Victory If)

✅ **One venture** (CON-001) executes Phase 1 → Phase 5 successfully  
✅ **New venture onboarded** (CON-002) in under 5 minutes  
✅ **Data pipeline** runs without manual intervention  
✅ **vex shows** all 5 ventures with current phase  
✅ **Runbook works** — someone else can onboard venture without help  

---

## Troubleshooting (Monday)

| Problem | Fix |
|---------|-----|
| Neo4j not responding | `docker ps` → restart if needed |
| Qdrant empty | Run `python3 build_repo_rag.py` |
| PostgreSQL connection error | Check `.env` has SUPABASE_URL + KEY |
| Phase executor crashes | Check venture_id exists in registry |
| vex doesn't show new venture | Run sync script (`populate_venture_knowledge_graph.py`) |

---

## Slack Channels (For Updates)

- **#ventures** — Live venture status, blockers
- **#infraops** — System health, Docker issues
- **#iza-os** — IZA OS updates, capability mapping
- **#vex** — Portfolio/public updates

---

## Post-Monday (This Week)

- [ ] Wire Evolver into phase execution
- [ ] Build real-time dashboard (Supabase → vex)
- [ ] Add Phase 2-5 skills
- [ ] Test multi-phase execution (Phase 1 → Phase 5)
- [ ] Document policy engine (budgets, approvals)

---

## Post-Week 1 (This Month)

- [ ] Fractal orchestration (scale to 712 ventures)
- [ ] Parallel phase execution (phases 1-4 together)
- [ ] Automated skill evolution (Evolver loop)
- [ ] Dashboard live (real-time phase tracking, cost analytics)
- [ ] CI/CD for ventures (auto-deploy when phase completes)

---

## The Big Picture

**What we're doing:** Building an operating system where ventures are:
- Creatable in 5 minutes
- Executable in phases (not monolithic)
- Automatable at scale (712 parallel)
- Evolvable (skills improve over time)
- Capital-generative (4 layers of revenue)

**Monday's goal:** Prove one venture works end-to-end, so we can onboard 100 more by end of August.

**Long-term (6 months):** 100 ventures generating $57K-$135K/mo combined. All automated. All auditable.

---

## Quick Links

- **Neo4j:** http://localhost:7474
- **vex:** http://localhost:5173
- **Supabase:** (check .env for URL)
- **Repo:** https://github.com/Worldwidebro/WORLDWIDEBRO-OS
- **Runbook:** This file

---

**Last Updated:** July 25, 2026 @ 9:00 AM  
**Next Review:** Monday 7 AM (post-launch debrief)  
**Owner:** Antwuan Johns (@worldwidebro)
