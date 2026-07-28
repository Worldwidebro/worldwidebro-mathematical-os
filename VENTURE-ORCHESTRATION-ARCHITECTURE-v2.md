# Venture Orchestration Architecture v2 — Layered & Decoupled

**Problem with v1:** Hard-coded phases, business logic tangled in orchestrator, no skill evolution.

**Solution:** Five decoupled layers, each reusable across any industry/venture model.

---

## Five-Layer Stack

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 5: Mission Control (Dashboard + Analytics)            │
│  • Real-time phase progress, cost tracking, blockers       │
│  • Skill effectiveness rankings (which phase_*.md works)   │
│  • Human decisions (approve, block, adjust)                │
└──────────────────┬──────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ Layer 4: Governance (Policy Engine)                         │
│  • Budget caps, approval gates, retry limits               │
│  • Model constraints, security policies                     │
│  • Enforcement (block execution if policy violated)        │
└──────────────────┬──────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ Layer 3: Orchestration (GraphOrchestrator + Evolver)        │
│  • DAG Scheduler: phase_definitions.yaml → execution      │
│  • Evolver: autonomous skill evolution (observe→refine)   │
│  • Layered fan-in: 30-50 ventures per batch               │
│  • Continuous loop: error → signal → gene → improved skill │
└──────────────────┬──────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ Layer 2: Execution (Fractal Runtime)                        │
│  • Root node: orchestrator (reads venture registry)        │
│  • 712 child nodes: one per venture (git worktrees)        │
│  • Phase nodes: execute skills via fractal workers         │
│  • Outcome tracking: SQLite + Supabase                     │
└──────────────────┬──────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ Layer 1: Skills & Models                                    │
│  • phase_*.md artifacts (Evolver-optimized)                │
│  • Model routing: Ollama (free) → Gemini → Claude-Opus     │
│  • Tools: MCP servers, knowledge graphs                     │
└──────────────────────────────────────────────────────────────┘
```

---

## Layer 1: Skills & Models (Reusable Assets)

**Components:**
- `phase_planning.md` — skill definition (optimized by Evolver)
- `phase_implementation.md` — implementation skill
- `phase_testing.md` — testing skill
- Model router: task complexity → optimal model + cost

**Evolver Loop (Installed):**
```bash
evolver --loop
# Continuously:
#  1. Read ./memory/ for phase failures
#  2. Select Gene/Capsule from skill store
#  3. Emit GEP prompt → update phase_*.md
#  4. Record EvolutionEvent (audit trail)
#  5. Next venture run uses improved skill
```

---

## Layer 2: Execution (Fractal Runtime)

**Hierarchy:**
```
Root Node
├─ Venture 001 (git worktree)
│  ├─ Phase 1-4 (parallel)
│  ├─ Phase 5 (waits on 4)
│  └─ Phases 6-14 (serial with edges)
└─ Venture 712 (git worktree)
```

**Each venture node:** Budget cap, iteration limit, timeout, SQLite logging.

---

## Layer 3: Orchestration (Graph + Evolution)

**GraphOrchestrator executes phase DAG:**
```yaml
phases:
  planning:
    depends_on: [discovery]
    skills: ["/superpowers:writing-plans"]
    max_cost_usd: 5
    
  implementation:
    depends_on: [specification]
    skills: ["/feature-dev"]
    max_cost_usd: 20
    approval_required: false
```

**Evolver optimizes:** Scans memory/ → refines phase_*.md → improves success rates.

---

## Layer 4: Governance (Policy Engine)

**Enforces:**
- Budget limits per venture/phase
- Approval gates (phase 10+ needs human sign-off)
- Model constraints (security phases → Claude-Opus only)
- Retry policy (max 3 retries on transient failure)

---

## Layer 5: Mission Control (Dashboard)

**Real-time:**
- Phase % complete, cost tracking, blockers
- Skill rankings (which phase_*.md has best success rate)
- Human decisions (approve, block, adjust policy)

---

## How Evolver Closes the Loop

**Without:** Phase fails → manual fix → redeploy (slow).  
**With Evolver:** Phase fails → Evolver selects Gene → updates phase_*.md → next run succeeds (autonomous).

---

**Status:** Evolver installed. Ready to wire into venture nodes.  
**Next:** Build policy-gate.py (Layer 4) + dashboard (Layer 5).
