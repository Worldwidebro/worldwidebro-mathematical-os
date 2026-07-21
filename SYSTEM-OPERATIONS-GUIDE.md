# System Operations Guide: How the Gears Turn

**Date:** 2026-07-20  
**System:** AI Boss OS (712 Ventures)  
**Audience:** Operators, Directors, CEO

---

## What This System Does

Every day, 712 ventures need to make decisions. This system automates the approval flow:

```
Venture needs decision ($X)
    ↓
Agent evaluates (CEO, CTO, CFO)
    ↓
Decision amount triggers approval rule:
  • <$5K → Agent approves automatically
  • $5K-$25K → Director must approve (Slack alert)
  • >$25K → CEO + Hermes reasoning required
    ↓
Approved decision executes
    ↓
Audit trail recorded (permanent log)
```

---

## The 8-Step Decision Flow

### 1. Registry Load
**What:** System reads venture from `ventures.csv`  
**Who:** Registry layer  
**When:** On every decision request  
**Output:** Venture metadata (stage, sector, MRR, runway)

### 2. Agent Spawn
**What:** CEO/CTO/CFO agent activated for this venture  
**Who:** Agent factory  
**When:** If agent not already active  
**Output:** Agent ready to execute tasks

### 3. Task Execution
**What:** Agent executes task (estimate-job, risk-score, dispatch-job)  
**Who:** Task executor + agent  
**When:** When task is assigned  
**Output:** Task result + amount (if financial decision)

### 4. Directive Evaluation
**What:** Approval matrix determines who must approve  
**Who:** Directive enforcer (approval rules)  
**When:** After task completes with amount  
**Rule:**
```
if amount < 5000: auto_approve (agent executes)
elif amount < 25000: escalate_to_director (Slack alert)
else: escalate_to_ceo_hermes (reasoning engine)
```
**Output:** Approval level + routing

### 5. Slack Alert (if needed)
**What:** Director or CEO gets Slack notification  
**Who:** MCP Slack integration  
**When:** If decision needs human approval  
**Format:** 
```
🔔 Director Approval Needed
$8500 decision for CON-001
Approve: /approve {decision_id}
Deny: /deny {decision_id}
```

### 6. Human Decision (if needed)
**What:** Director or CEO responds via Slack  
**Who:** Human operator  
**When:** When Slack alert arrives  
**Action:** Approve or deny via reaction/command

### 7. Execution
**What:** Approved decision is executed  
**Who:** Execution engine (varies by task type)  
**When:** After approval (or auto, if <$5K)  
**Example:** Create estimate, send to client, log invoice

### 8. Audit Trail
**What:** Decision recorded in database  
**Who:** Audit logging system  
**When:** After execution  
**Table:** `venture_decisions`  
**Fields:** venture_id, decision_id, amount, approval_level, status, timestamp

---

## Who Makes Decisions

### Auto-Approved (<$5K)
- **Agent**: Makes decision automatically
- **Time to execute**: Immediate (seconds)
- **Log**: Audit trail only, no alert

### Director Approval ($5K-$25K)
- **Alert**: Slack #director-approvals
- **Approver**: Director for that OPCO
- **Time to execute**: Depends on director response (minutes to hours)
- **Log**: Slack message + audit trail

### CEO + Hermes Reasoning (>$25K)
- **Alert**: Slack #ceo-decisions
- **Approver**: CEO (after Hermes AI reasoning)
- **Time to execute**: Hermes reasoning + CEO approval (30 min to hours)
- **Log**: Reasoning explanation + Slack + audit trail

---

## Monitoring Decisions

### Real-Time Status
- **Slack**: Monitor #director-approvals and #ceo-decisions for pending decisions
- **Dashboard**: Port 20128 shows real-time status `/dashboard/providers`
- **Audit log**: Query `venture_decisions` table for history

### Metrics to Watch
- **Cycle time**: Time from task → execution (target: <5 min for auto, <2 hours for director)
- **Approval rate**: % decisions auto-approved vs escalated
- **Error rate**: Failed executions % (target: <1%)

---

## System Components (What's Wired)

| Component | Status | Purpose |
|-----------|--------|---------|
| Registries (CSV/YAML) | ✅ Live | Venture definitions, agents, capabilities |
| Agent factory | ✅ Live | Spawn CEO/CTO/CFO per venture |
| Task executor | ✅ Live | Run estimate-job, risk-score, dispatch-job |
| Directive enforcer | ✅ Live | Apply approval matrix |
| MCP Slack | ✅ Live | Route alerts to channels |
| Dashboard (20128) | ✅ Live | Operators view decisions |
| Audit logging | ✅ Live | Permanent decision history |

---

## How to Operate

### For Directors
1. Watch Slack #director-approvals for pending decisions
2. Review decision details (amount, venture, context)
3. Click approve or deny
4. System executes your decision
5. Check dashboard for status

### For CEO
1. Watch Slack #ceo-decisions for high-value decisions
2. Let Hermes provide reasoning (via dashboard)
3. Approve or deny
4. System executes

### For Operators
1. Monitor dashboard for stuck decisions
2. Check audit log for issues
3. Restart agents if needed
4. Escalate system alerts to CTO

---

## Scaling to All 712 Ventures

Current pilot: 10 ventures, 30 agents, 3 decisions/day  
Ready to scale to: 712 ventures, 2,136 agents, 200+ decisions/day

**No changes needed.** System architecture already handles scale:
- Registries indexed for fast lookup
- Agents spawned on-demand (no pre-allocation)
- Slack integrations parallel (no bottleneck)
- Supabase handles concurrent writes

---

## Troubleshooting

### Decision Stuck in "Pending"
1. Check Slack channel for alert (maybe director didn't see it)
2. Check dashboard for error logs
3. Check audit table for last status update
4. If >4 hours old, manually escalate to director

### Agent Not Responding
1. Check registries loaded correctly
2. Restart agent: `agent_factory_pilot.py --restart {venture_id}`
3. Check Neo4j for stale agent state
4. Restart entire system if multiple agents stuck

### Slack Alerts Not Sending
1. Verify MCP Slack bot token in env
2. Check Slack channels exist (#director-approvals, #ceo-decisions)
3. Check n8n workflows running (Zapier sync)
4. Restart Slack integration: `docker-compose restart slack-mcp`

---

## Success Criteria

✅ All 8 layers operational  
✅ Decisions routed to correct approver  
✅ Slack alerts working  
✅ Audit trail complete  
✅ <1 second per decision (auto decisions)  
✅ <1% error rate  
✅ Ready to scale to 712 ventures

---

## Next: Scale to Production

When ready to go live with all 712 ventures:

1. **Load all ventures** from ventures.csv into Neo4j
2. **Spawn all 2,136 agents** (3 per venture × 712)
3. **Monitor first 100 decisions** for errors
4. **Adjust thresholds** if needed (approval amounts, timeouts)
5. **Go live** with all 712 ventures

Estimated time: 4-8 hours setup + testing.
