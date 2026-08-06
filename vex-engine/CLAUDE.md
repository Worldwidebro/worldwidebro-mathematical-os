---
name: vex-engine/CLAUDE
title: CLAUDE.md — VEX Engine (Orchestrator)
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# CLAUDE.md — VEX Engine (Orchestrator)

**Scope:** Agent orchestration, workflow dispatch, policy enforcement  
**Updated:** 2026-08-05  
**Phase:** 8-10 (Agent Routing → Execution)  
**Framework:** Node.js or Python (TBD)

---

## What This Repo Does

VEX Engine provides:
- Agent registry and routing (capability → agent(s))
- Workflow dispatch to Trigger.dev
- Policy enforcement (every action audited)
- Agent coordination (multi-step workflows)
- Result collection and action logging

---

## Environment Variables

```env
SUPABASE_URL=http://localhost:5432
SUPABASE_SERVICE_ROLE_KEY=<from Supabase>
NEO4J_URL=bolt://localhost:7687
QDRANT_URL=http://localhost:6333
TRIGGER_DEV_API_KEY=<from Trigger.dev>
ANTHROPIC_API_KEY=<from Anthropic>
```

---

## Flow: Capability → Agent → Trigger.dev → Result

```
1. User: "Find staffing candidates"
2. Orchestrator: Which agents handle "Candidate Matching"?
   → Neo4j returns [staffing-agent]
3. Select + dispatch to Trigger.dev
4. Poll job status
5. On completion, log to action_ledger:
   { "agent_id": "staffing-agent", "status": "success", 
     "cost_cents": 25, "revenue_cents": 150, "roi": 6.0 }
```

---

## Phase Gates

| Phase | Deliverable |
|-------|-------------|
| **8** | Agent router working (Neo4j → agent) |
| **9** | Trigger.dev integration complete |
| **10** | First agent execution end-to-end |
| **11** | Policy verification + auditing |
| **12** | Action ledger recording + ROI |

---

## Commands

```bash
npm install
npm run dev          # Start :4000
npm run agent-test   # Test agent dispatch
npm run ledger-test  # Test ledger recording
```

---

## Critical Rules

1. **Every action gets audited** — No silent failures.
2. **Policy check before dispatch** — Verify cost, permissions.
3. **Callback registration mandatory** — Poll or receive webhook.
4. **Ledger is immutable** — Postgres audit trail.

---

## Related

- Root CLAUDE.md: `~/.claude/CLAUDE.md`
- VEX Core: `/Users/acebless/Documents/vex`
- VEX API: `/Users/acebless/Documents/vex-api`
