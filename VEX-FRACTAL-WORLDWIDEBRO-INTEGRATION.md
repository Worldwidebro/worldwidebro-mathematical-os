---
references:
  - [[venture-loops-framework]]
  - [[unified-company-roadmap-2026]]
  - [[complete-os-architecture-map]]
---

# VEX ↔ Fractal ↔ Worldwidebro Integration

**Purpose:** Wire the public portfolio interface (vex) to the execution engine (fractal) via the knowledge graph (worldwidebro-os infrastructure).

## System Architecture

```
VEX Hero Site (Frontend)
├─ portfolio.public.json (713 ventures)
├─ Hero pages (sectors, ventures)
└─ Operations interface (lead form, funding commands)

        ↓ (Supabase read/write)

Knowledge Graph Backend
├─ Neo4j: 2,618 nodes, 11,134 edges (ventures, repos, caps, skills)
├─ Qdrant: 1,648+ vectors (semantic search)
├─ Supabase: transactional data + audit trail
└─ DuckDB: analytics + cost tracking

        ↓ (Fractal orchestration)

Execution Layer
├─ venture-loops-framework: 14 phases with explicit edges
├─ GraphOrchestrator: respect only real dependencies
├─ Fractal nodes: 712 ventures in parallel
└─ SkillOpt: continuous phase skill improvement
```

## Data Flow: vex → Fractal → Results

### 1. User Clicks "Execute" on vex
- portfolio.public.json shows 713 ventures
- User selects sector + goal
- OpcoFundingCommand writes to venture_runs table
- Timestamp: ISO-8601 (e.g., 2026-07-25T08:35:00Z)

### 2. Webhook: Supabase → Fractal
- n8n trigger on venture_runs INSERT
- Payload: {venture_ids, sector, goal, timestamp}
- Fractal spawn: root orchestrator node

### 3. Execution: Fractal Spawns 712 Ventures
- Each venture gets isolated git worktree
- Phase executor runs phases 1-14 respecting edges
- Phase 1-4: parallel (no deps)
- Phase 5+: serial with explicit wait conditions
- Each phase writes to phase_executions table
- Timestamp format: ISO-8601

### 4. Results Stream Back to vex
- Supabase realtime subscription in React
- Dashboard updates as phase_executions table fills
- Cost tracking via DuckDB aggregation
- Blocker detection: silent node failures flagged

## Integration Points

**A. Portfolio → Queue (vex writes)**
- Table: venture_runs
- Fields: venture_id, sector, goal, user_id, status, created_at
- Trigger: n8n webhook → fractal spawn

**B. Execution → Live Updates (fractal writes)**
- Table: phase_executions
- Fields: venture_id, phase_id (1-14), status, cost_usd, duration_seconds, completed_at
- Trigger: Supabase realtime → vex React update

**C. Results → Feedback (SkillOpt reads)**
- Query: phase_executions failures by phase/venture
- Action: best_phase_*.md skill artifacts updated
- Frequency: nightly rollout + reflection

## Worldwidebro Identity

**portfolio.public.json founder block:**
```json
{
  "name": "Antwuan Johns",
  "handle": "worldwidebro",
  "email": "winnerscirclewcllc@gmail.com",
  "proof": [
    "15-layer operating system",
    "1,400+ repository intelligence",
    "Knowledge graph infrastructure",
    "Multi-agent execution loops"
  ]
}
```

**Function:** Public identity layer. vex displays this proof + links to repos.

## Deployment Phases

| Phase | Component | Status |
|-------|-----------|--------|
| 1 | vex + Supabase schema | ✅ Done |
| 2 | venture-loops-framework + orchestration_patterns | ✅ This turn |
| 3 | Fractal venture-executor skill | ⏳ Next |
| 4 | Real-time dashboard (vex phase progress UI) | ⏳ Week 2 |
| 5 | SkillOpt learning loop | ⏳ Week 3 |

## Quick Test: 712 Ventures in Parallel

```bash
# 1. vex reads portfolio
curl http://localhost:5173/api/ventures | jq '.length'  # Should be 713

# 2. User executes via vex (simulated)
curl -X POST http://localhost:3000/api/execute-ventures \
  -H "Content-Type: application/json" \
  -d '{"sector": "CONSTRUCTION", "goal": "Execute all"}' \
  # Writes to venture_runs

# 3. Fractal spawns
fractal spawn construction_batch --max-descendants 712 --max-cost 50000

# 4. Monitor execution
fractal open  # TUI dashboard shows node tree + cost

# 5. Query results
duckdb worldwidebro_os.duckdb \
  "SELECT sector, COUNT(*) as ventures, SUM(cost_usd) as total_cost FROM phase_executions WHERE completed_at IS NOT NULL GROUP BY sector;"

# 6. vex dashboard live
open http://localhost:5173/dashboard
```

---

**Files Created This Turn:** venture-loops-framework.md, orchestration_patterns.py (updated)  
**Files Next:** venture-executor.md (fractal skill), PhaseProgressDashboard.tsx (vex component)
