---
references:
  - [[UNIFIED-ORB-NAME-1]]
  - [[LOOP-FRAMEWORK]]
  - [[SKILL-EXECUTION-FRAMEWORK]]
---

# Venture Loops Framework — Graph-Based Execution

**Purpose:** Execute 712 ventures through 14 phases in parallel using explicit graph edges (not sequential chains).

## Graph Architecture

Each venture is a **fractal node** with 14 internal phases. Phases run in **parallel groups**, constrained by **real dependencies only**.

```
Venture Node (Fractal)
├─ Phase Group A (parallel, no deps)
│  ├─ Phase 1: Setup & Environment
│  ├─ Phase 2: Discovery & Research
│  ├─ Phase 3: Ideation & Strategy
│  └─ Phase 4: Planning & Architecture
├─ Phase Group B (waits on Group A completion)
│  ├─ Phase 5: Specification & Design
│  └─ Phase 6: Core Implementation
├─ Phase Group C (parallel, depends on Phase 6)
│  ├─ Phase 7: Testing & Verification
│  ├─ Phase 8: Optimization & Polish
│  └─ Phase 9: Documentation
└─ ... (continues through Phase 14)
```

## Phase Dependency Map (Explicit Edges)

### ✅ Independent (No Edges) — Run in Parallel
- **Phase 1 (Setup)** — No dependencies
- **Phase 2 (Discovery)** — Independent of Phase 1 output (runs parallel with 3, 4)
- **Phase 3 (Strategy)** — Independent of Phase 1 output (runs parallel with 2, 4)
- **Phase 4 (Planning)** — Independent of Phase 1 output (runs parallel with 2, 3)

### 🔗 Has Real Edges — Wait for Dependencies

| Phase | Depends On | Reason |
|-------|-----------|--------|
| **5: Specification** | Phase 4 | Spec requires finalized plan |
| **6: Implementation** | Phase 5 | Code requires spec |
| **7: Testing** | Phase 6 | Tests verify implementation |
| **8: Optimization** | Phase 7 | Optimize based on test results |
| **9: Documentation** | Phase 8 (parallel 6-8) | Document final optimized code |
| **10: Release** | Phase 9 | Release requires docs |
| **11: Growth** | Phase 10 | Growth needs live release |
| **12: Operations** | Phase 11 | Ops maintains live system |
| **13: Advanced** | Phase 12 | Advanced features after proven ops |
| **14: Domain-Specific** | Phase 13 | Specialized tools last |

## Parallel Execution Groups

### Group A: Discovery (Phases 1-4)
**Execution:** Fully parallel (no edges)
```python
wait_for = []  # No dependencies
phase_ids = [1, 2, 3, 4]
asyncio.gather(*[execute_phase(p) for p in phase_ids])
```

### Group B: Specification (Phase 5)
**Execution:** Waits for Group A
```python
wait_for = [1, 2, 3, 4]
asyncio.run(execute_phase(5))
```

### Group C: Build & Test (Phases 6-8)
**Execution:** Serial chain (each depends on previous)
```python
wait_for = [5]
for phase in [6, 7, 8]:
    asyncio.run(execute_phase(phase))
```

### Group D: Polish & Release (Phases 9-10)
**Execution:** Parallel, then serial
```python
wait_for = [8]
# Phase 9 (docs) can run in parallel with 6-8 completion
asyncio.run(execute_phase(9))
asyncio.run(execute_phase(10))
```

### Group E: Operations (Phases 11-14)
**Execution:** Serial (each depends on previous)
```python
wait_for = [10]
for phase in [11, 12, 13, 14]:
    asyncio.run(execute_phase(phase))
```

## Fractal Node Configuration

Each venture spawns as a **fractal child node** with phase-based branching:

```yaml
node:
  name: "venture_{{ venture_id }}"
  title: "{{ venture_name }} Execution"
  path: "03-VENTURES/{{ sector }}/{{ venture_id }}/"
  base: "main"
  scope: "."
  agent: "claude"
  model: "claude-opus-4-8"
  
  # Hard caps per venture
  max-iters: 100          # iterations per phase
  max-depth: 3            # child phases max nesting
  max-children: 5         # parallel phases max
  max-descendants: 20     # total phase nodes
  max-cost: 50            # USD per venture
  max-iter-cost: 5        # USD per phase
  timeout: "8h"           # total venture time
  iter-timeout: "30m"     # phase time
  
  # Execution strategy
  interval: null          # on-demand, not scheduled
  detached: false         # one continuous session
  sync: true              # push to remote per phase
```

## Execution Flow in Fractal

**Orchestrator Node** (root):
1. Read `VENTURES-CAPABILITIES-MAPPED.csv`
2. Group ventures by sector (parallelizable)
3. Spawn **712 venture child nodes** (bounded by `max-descendants`)
4. Each child executes phases with graph edges

**Venture Node** (child):
1. Parse phase dependency map
2. Execute Group A (parallel): `asyncio.gather(phases 1-4)`
3. Fan-in: Consolidate Group A results
4. Execute remaining groups respecting edges
5. Commit phase outputs to venture branch
6. Report metadata to root SQLite

**Root Consolidation** (fan-in with batching):
```python
# Layer 1: Batch venture results (30 ventures per batch)
batch_summaries = await asyncio.gather(*[
    summarize_venture_batch(batch) for batch in venture_batches
])

# Layer 2: Final consolidation
report = await consolidate_all_batches(batch_summaries)
```

## Supabase Tracking Schema

```sql
-- Phase execution tracking
CREATE TABLE phase_executions (
  id UUID PRIMARY KEY,
  venture_id VARCHAR,
  phase_id INT (1-14),
  phase_name VARCHAR,
  status VARCHAR (pending, running, completed, failed),
  depends_on INT[] (phase IDs this depends on),
  waited_for_phases INT[] (which phases this actually waited for),
  cost_usd DECIMAL,
  duration_seconds INT,
  worktree_branch VARCHAR,
  output_summary TEXT,
  created_at TIMESTAMP,
  completed_at TIMESTAMP
);

-- Venture-level orchestration
CREATE TABLE venture_runs (
  id UUID PRIMARY KEY,
  venture_id VARCHAR,
  fractal_node_id VARCHAR,
  run_status VARCHAR (pending, running, completed, failed),
  group_a_start TIMESTAMP,
  group_a_complete TIMESTAMP,
  group_b_start TIMESTAMP,
  total_cost_usd DECIMAL,
  total_duration_seconds INT,
  created_at TIMESTAMP
);
```

## Cost Optimization (Graph vs Sequential)

### Sequential Execution (Old Model)
```
712 ventures × 14 phases × 5 min avg = 49,280 minutes (34 days)
Cost: 712 × $0.10/phase = $71.20 per full venture execution
```

### Parallel Execution (Graph Model)
```
712 ventures in parallel:
  Group A (4 phases parallel): 5 min
  Group B-E (10 phases, mixed): 15 min
  Total per venture: ~20 min
  
All 712 at once: 20 min wall clock
Cost: Same $71.20 per venture, but 712× speedup in throughput
```

## Monitoring & Debugging

**Fractal TUI Dashboard shows:**
- Tree of 712 venture nodes + phase children
- Real-time phase execution status
- Cost tracking per node + total
- Iteration counts, depth, parallelism
- Branch/commit status per worktree

**SQLite query for cost anomalies:**
```sql
SELECT venture_id, SUM(cost_usd) as total_cost
FROM phase_executions
WHERE created_at > NOW() - INTERVAL 1 DAY
GROUP BY venture_id
HAVING total_cost > 10
ORDER BY total_cost DESC;
```

## Integration with Skill Execution Framework

Each **phase** maps to 1-4 **skills** from the 296-skill library:

```python
phase_skills = {
    1: ["/getting-started", "/init", "/configure-ecc"],
    2: ["/deep-research", "/iza-os-rag", "/socraticode:codebase-exploration"],
    3: ["/superpowers:brainstorming", "/strategic-compact"],
    4: ["/superpowers:writing-plans", "/planning-with-files"],
    5: ["/design-task", "/postman:setup", "/postman:generate-spec"],
    6: ["/feature-dev", "/agentic-engineering", "/run"],
}
```

**Execution:** Each phase node runs the assigned skills in order, reporting results to Supabase.

## Quick Start: Launch a Venture

```bash
# From project root
fractal spawn venture_orchestrator \
  --name venture_executor \
  --scope "03-VENTURES/" \
  --max-descendants 712 \
  --max-cost 50000 \
  --title "712 Ventures Parallel Execution"
```

---

**Related:** [[complete-os-architecture-map]], [[skill-execution-framework]], [[unified-company-roadmap-2026]]
