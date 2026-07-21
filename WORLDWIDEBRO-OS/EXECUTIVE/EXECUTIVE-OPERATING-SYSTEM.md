# Executive Operating System: AI Boss OS Command Center

**Date:** 2026-07-20  
**Scope:** Strategic governance of 712-venture operating system  
**Authority:** CEO, CFO, CTO, CMO, COO, Board

---

## The Command Chain

```
BOARD / SHAREHOLDERS
    ↓
CEO (Strategy)
    ├─ CFO (Finance)
    ├─ CTO (Technology)
    ├─ CMO (Growth)
    └─ COO (Operations)
        ↓
DIRECTIVES (Rules that cascade)
        ↓
OPERATING SYSTEMS (Execute rules)
        ↓
AI AGENTS (Coordinate work)
        ↓
712 VENTURES (Create value)
```

---

## Your Role

| Role | Decides | Authority | Reports |
|---|---|---|---|
| CEO | Strategy, priorities, vision | All strategic decisions | Board |
| CFO | Capital allocation, budgets | Decisions >$5K | CEO |
| CTO | Technology, architecture | Tech decisions, infrastructure | CEO |
| CMO | Growth, market strategy | Customer priorities | CEO |
| COO | Operations, efficiency | Process optimization | CEO |

---

## Current Priorities (P0-P2)

### P0: Complete Observability (CTO, Deadline: 2026-07-30)
- [ ] Fix Grafana login + reset password
- [ ] Wire Prometheus to all services
- [ ] Verify Langfuse traces live
- [ ] Cluster exo for distributed inference

### P1: Wire Task Types (Deadline: 2026-08-15)
- [ ] 10 core task types (estimate-job, risk-score, etc.)

### P2: CEO Dashboard Complete (Deadline: 2026-08-30)
- [ ] Real-time venture visibility
- [ ] Financial + risk + opportunity views

---

## How to Execute a Directive

**Example: Fix Observability (P0)**

1. **Read:** `DIRECTIVES/OPERATING-DIRECTIVES/OBSERVABILITY-DIRECTIVE.md`
2. **Run:** `./scripts/check-tools.sh --verbose` (see what's broken)
3. **Execute:**
   - CTO: Wire Prometheus targets
   - DevOps: Reset Grafana password
   - Agent team: Wire Langfuse tracing
   - Infra: Cluster exo
4. **Verify:** `./scripts/check-tools.sh` (all healthy)
5. **Report:** Update `DIRECTIVES/DECISIONS/DECISION-HISTORY.md`

---

## Approval Authority

| Decision | Authority | Process |
|---|---|---|
| <$5K | Venture founder | Direct execute |
| $5K-$25K | Director | Approve + execute |
| >$25K | Hermes + CEO | Reasoning + approval |
| Irreversible | CEO | Full authority |
| Strategic | Board | Quarterly |

---

## This Is How You Govern 712 Ventures

**You set directives. All 712 inherit them. Done.**

---

*Start reading: EXECUTIVE/CEO/CEO-MISSION.md*
