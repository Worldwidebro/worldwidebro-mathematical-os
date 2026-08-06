---
name: AGENT-CONFLICT-REMEDIATION
title: Agent Conflict Remediation Plan
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Agent Conflict Remediation Plan
**Date**: May 11, 2026  
**Detected by**: Agent Conflict Detector  
**Status**: Ready for implementation  

---

## Critical Issues (Must Fix Before Task 9-11)

### 1. **DUPLICATE CEOs** 🔴 HIGH
**Problem**: 3 CEO agents (Worldwidebro CEO, Worldwidebro CEO 2, CEO)
**Impact**: Conflicting capital allocation decisions, unclear escalation path
**Solution**: Keep ONE CEO agent, delete the other two

**Action**:
```bash
# Keep "Worldwidebro CEO" (primary)
# Delete "Worldwidebro CEO 2" and "CEO" from Paperclip
curl -X DELETE http://localhost:3101/api/companies/1450a240-2be1-4dc6-b74c-ada307ca6ddb/agents/{id}
```

---

### 2. **METRICS OWNERSHIP CONFLICT** 🔴 HIGH
**Problem**: Operations Manager AND Financial Analyst both claim metrics tracking
- Ops Manager: "Monitor venture health metrics (CAC, LTV, churn, margin)"
- CFO/Analyst: "Calculate and track CAC/LTV for each venture"

**Impact**: Inconsistent metric definitions, conflicting reports
**Solution**: CFO owns ALL financial metric calculations, Ops Manager requests via API

**Decision Authority Matrix**:
| Metric | Owner | Consumer |
|--------|-------|----------|
| CAC/LTV/Churn | Financial Analyst (CFO) | Ops Manager, CEO, Sector PMs |
| Gross Margin | Financial Analyst (CFO) | Ops Manager, CEO |
| Burn Rate | Financial Analyst (CFO) | CEO, Ops Manager |
| Health Score | Financial Analyst (CFO) | All agents |

---

### 3. **RISK ESCALATION DUPLICATION** 🔴 HIGH
**Problem**: All 4 Sector PMs + Financial Analyst claim risk flagging
- Analyst: "Flag ventures underperforming against targets"
- Sector PMs: "Escalate sector-wide risks to CEO"

**Impact**: Critical risks over-escalated or missed
**Solution**: 
- Financial Analyst (CFO) flags ALL financial/performance risks
- Sector PMs escalate STRATEGIC/SECTOR-SPECIFIC risks
- All escalations route through Operations Manager to CEO

**Risk Categories**:
- **Financial Risks** (Analyst owns): Low LTV/CAC, margin compression, burn rate
- **Operational Risks** (Ops Manager owns): Team capacity, execution delays, process failures
- **Strategic Risks** (CEO owns): Market changes, competitive threats, macro trends
- **Sector Risks** (Sector PMs own): Regulatory changes, sector-specific challenges

---

## Medium Issues (Optimize Before Launch)

### 4. **SECTOR PM COORDINATION**
**Problem**: All 4 Sector PMs independently claim venture_ops and strategic responsibility
**Solution**: Establish clear boundaries
- Each PM owns ventures IN THEIR SECTOR ONLY
- Cross-sector coordination goes through Ops Manager
- Strategic decisions escalate through CEO

---

## Proposed Decision Authority Hierarchy

```
CEO (Final Authority)
├── Financial Analyst (CFO)
│   ├── Metrics: CAC, LTV, churn, margin, burn rate, health score
│   ├── Reports: Monthly financial performance by venture & sector
│   └── Risk Flags: Performance vs. KPI targets
│
├── Operations Manager (CTO)
│   ├── Execution: Day-to-day venture operations
│   ├── Metrics: Operational KPIs (team health, task completion)
│   ├── Coordination: Routes sector decisions to CEO
│   └── Risk Flags: Operational & execution risks
│
└── Sector Leads (PM role)
    ├── Financial Services Lead
    ├── Construction Lead
    ├── E-Commerce Lead
    └── SaaS Lead
    
    Each manages:
    ├── Ventures: Only in their sector
    ├── Health: Local monitoring (requests full metrics from CFO)
    └── Risk Flags: Sector-specific strategic risks (escalate via Ops)
```

---

## Implementation Checklist

### Phase 1: Consolidate Structure (30 min)
- [ ] Delete duplicate CEO agents from Paperclip
- [ ] Verify single CEO remains as decision authority
- [ ] Document decision matrix in system prompts (once prompts are persisted)

### Phase 2: Clarify Responsibilities (20 min)
- [ ] Update Financial Analyst system prompt: "You OWN all metric calculations. No other agent calculates metrics."
- [ ] Update Ops Manager prompt: "Request metrics from CFO via API. Do not calculate yourself."
- [ ] Update Sector PM prompts: "Escalate financial risks to CFO. Escalate operational risks to Ops Manager."

### Phase 3: Test Authority Flow (15 min)
- [ ] Run decision scenario: "venture X has CAC/LTV ratio of 2x (below 3x target)"
  - Expected: Financial Analyst flags, escalates to CEO via Ops Manager
  - Result: Ops Manager implements CEO decision to optimize or kill
  
- [ ] Run cross-sector scenario: "Construction Lead needs marketing budget increase"
  - Expected: Routes through Ops Manager → CEO for approval
  - Result: CEO approves/denies with visibility across all sectors

---

## Risk of Not Fixing

### Before Tasks 9-11 (Agent Autonomy):
- Duplicate CEO logic will cause conflicting autonomous decisions
- Metric conflicts will make financial analysis unreliable
- Risk escalation duplicates will flood CEO with alerts

### Timeline Impact:
**Fixes this week (May 12)**: Unblocks Tasks 9-11 start (May 15)
**Skip this week**: Tasks 9-11 inherit broken authority, 2-week delay to debug

---

## Files Updated
- This file (AGENT-CONFLICT-REMEDIATION.md) - new
- agent_conflict_detector.py - saved results
- aoc_tasks table - audit trail of conflicts detected

---

## Next Step
Once consolidated, run `agent_control_loop.py` test mode to verify decisions propagate correctly through the new hierarchy.

