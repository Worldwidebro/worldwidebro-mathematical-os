---
name: TASK-16-GO-LIVE-CHECKLIST
title: 'Task 16: Go-Live Checklist (Deploy to Vercel)'
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Task 16: Go-Live Checklist (Deploy to Vercel)
**Date**: 2026-05-14  
**Target Launch**: Week 2 (May 20-24)  
**Status**: Pre-flight checklist ready

---

## Phase 1: Infrastructure Readiness (Days 1-3)

### Supabase Deployment
- [ ] Verify all SQL functions deployed
  - [ ] `calculate_cac()`
  - [ ] `calculate_ltv()`
  - [ ] `calculate_survival_metric()`
  - [ ] `apply_ceo_decision_tree()`
  - [ ] `flag_underperforming_ventures()`
- [ ] Test RPC endpoints (call via REST API)
- [ ] Confirm table structure and permissions
  - [ ] `ventures` table with `survival_metric` column
  - [ ] `venture_metrics` table for audit
  - [ ] `week_0_decisions` table
  - [ ] `week_0_execution_logs` table
  - [ ] `week_0_risks` table
- [ ] Seed initial venture data (5-10 test ventures)
- [ ] Run backfill: `SELECT calculate_survival_metric(id) FOR each venture`
- [ ] Set Row-Level Security (RLS) policies
  - [ ] CFO can read all ventures, write to metrics
  - [ ] CEO can read metrics, write to decisions
  - [ ] CTO can read all, write to execution_logs

### Environment Configuration
- [ ] Set Supabase credentials (SUPABASE_URL, SUPABASE_KEY)
- [ ] Set Twilio credentials (TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER)
- [ ] Set Composio credentials (COMPOSIO_API_KEY)
- [ ] Set Paperclip agent IDs (PAPERCLIP_CEO_ID, PAPERCLIP_CFO_ID, PAPERCLIP_CTO_ID)
- [ ] Verify all 3 environment profiles (dev, staging, prod)

### Paperclip Agent Deployment
- [ ] Deploy CEO agent with decision tree prompt
  - [ ] Test with sample metrics (survival_metric=45, roi=15%)
  - [ ] Verify decision output: `OPTIMIZE`
- [ ] Deploy CFO agent with metrics calculation prompt
  - [ ] Test metrics fetch for 1 venture
  - [ ] Verify survival_metric calculation
- [ ] Deploy CTO agent with execution routing prompt
  - [ ] Test command dispatch for SCALE decision
  - [ ] Verify Composio integration
- [ ] Consolidate duplicate agents (Paperclip UI)
  - [ ] Keep "Worldwidebro CEO", delete "Worldwidebro CEO 2" and "CEO"
  - [ ] Total: 1 CEO, 1 CFO, 1 CTO, 4 Sector PMs

---

## Phase 2: Code Integration (Days 4-7)

### Core Agent Loop
- [ ] Deploy `agent_control_loop.py` as scheduled job
- [ ] Test `python agent_control_loop.py test` mode
  - [ ] Fetches ventures from Supabase
  - [ ] Calculates metrics for each
  - [ ] Makes decisions via CEO agent
  - [ ] Logs to `week_0_decisions` table
- [ ] Verify audit logging
  - [ ] Each decision logged with timestamp, roi, survival_metric
  - [ ] Traceable to venture_id and CEO agent

### Financial Analyst (CFO Agent)
- [ ] Deploy `financial_analyst_cfo.py`
- [ ] Test monthly cycle: `python financial_analyst_cfo.py`
  - [ ] Fetches all ACTIVE ventures
  - [ ] Calls calculate_cac(), calculate_ltv(), calculate_survival_metric()
  - [ ] Flags underperforming (survival < 50)
  - [ ] Escalates risks to CTO
- [ ] Verify Risk table population
  - [ ] Each risk has venture_id, risk_type, severity, description

### SMS Service Integration
- [ ] Deploy `sms_provider_integration.py`
- [ ] Test Twilio connection
  - [ ] Credentials verified
  - [ ] Test SMS send to internal number
  - [ ] Verify delivery via Twilio dashboard
- [ ] Implement message templates for each decision type
  - [ ] KILL: "Venture archived"
  - [ ] OPTIMIZE: "New focus on high-value segment"
  - [ ] SCALE: "Ready for expansion"
  - [ ] COMPOUND: "Aggressive growth phase"
- [ ] Enable A/B testing framework
  - [ ] Test variant_a vs variant_b tracking

### Composio Command Dispatcher
- [ ] Deploy `composio_command_dispatcher.py`
- [ ] Verify all 91 commands loaded
- [ ] Test routing for each decision type
  - [ ] KILL decision → correct commands routed
  - [ ] OPTIMIZE → 4 commands dispatched
  - [ ] SCALE → 5 commands dispatched
  - [ ] COMPOUND → 5 commands dispatched
- [ ] Implement fallback/retry logic
  - [ ] Max 3 retries per command
  - [ ] Exponential backoff (1s → 2s → 4s)
  - [ ] Escalate to CTO if all retries fail

### Execution Teams
- [ ] Create `lead_activation_team.py` (15 commands)
  - [ ] Implement search_leads, segment_audience, enrich_lead_*
  - [ ] Test with sample segment data
- [ ] Create `outreach_team.py` (32 commands)
  - [ ] Implement contact management, calls, emails
  - [ ] Test with sample contacts
- [ ] Create team capacity monitoring
  - [ ] Track team utilization vs. capital allocated
  - [ ] Alert CTO if capacity exceeded

---

## Phase 3: Testing (Days 8-10)

### Unit Tests
- [ ] Test CFO metrics calculation (±5% accuracy)
- [ ] Test CEO decision tree (all 4 branches)
- [ ] Test CTO command dispatch (all 5 decision types)
- [ ] Test each execution team (sample commands)

### Integration Tests
- [ ] Full cycle: venture → metrics → decision → execution
  - [ ] Use test venture (id: test_001)
  - [ ] Verify each step completes
  - [ ] Check audit trail
- [ ] Error handling
  - [ ] Missing venture data → handled gracefully
  - [ ] Supabase down → retry and log
  - [ ] Composio API down → escalate to CTO

### Load Tests
- [ ] Run with 10 ventures: execution time < 2 min
- [ ] Run with 50 ventures: execution time < 5 min
- [ ] Monitor database query time and optimize if needed

### Security Tests
- [ ] RLS policies prevent unauthorized access
  - [ ] Non-CFO cannot write to venture_metrics
  - [ ] Non-CEO cannot write to week_0_decisions
- [ ] No secrets in logs or audit trail
- [ ] API keys never logged, only masked tokens
- [ ] Supabase keys rotated before launch

---

## Phase 4: Data Validation (Days 11-12)

### Sanity Checks
- [ ] survival_metric for all ventures: 0-100 range
- [ ] ROI calculations: no negative revenue
- [ ] CAC/LTV: no division by zero errors
- [ ] Decisions: only valid types (KILL/OPTIMIZE/SCALE/COMPOUND)

### Sample Data Validation
- [ ] Create 5 test ventures with known metrics
  - [ ] Healthy: survival=80, roi=120% → expect COMPOUND
  - [ ] Caution: survival=60, roi=40% → expect SCALE
  - [ ] Critical: survival=35, roi=25% → expect OPTIMIZE
  - [ ] Dying: survival=20, roi=-10% → expect KILL
  - [ ] Edge case: survival=50 (boundary)
- [ ] Run full cycle, verify decisions match expectations

### Audit Trail Review
- [ ] All decisions logged with full context
- [ ] All executions logged with results
- [ ] All risks logged with severity
- [ ] Timestamps consistent and correct

---

## Phase 5: Deployment (Days 13-14)

### Production Preparation
- [ ] Database backups created
- [ ] Rollback plan documented (restore from backup)
- [ ] On-call runbook ready (escalation path)
- [ ] Monitoring dashboard created
  - [ ] Key metrics: decisions/hour, execution success rate, avg survival_metric
  - [ ] Alerts: if success_rate < 95%, if avg survival < 40

### Vercel Deployment
- [ ] Push agent_control_loop.py to GitHub
- [ ] Deploy via Vercel serverless function
  - [ ] Endpoint: `/api/agents/control-loop`
  - [ ] Method: `POST`
  - [ ] Payload: `{"mode": "test"}` or `{"mode": "continuous"}`
- [ ] Schedule via Vercel cron
  - [ ] Task 9 (CFO): Daily at 9:00 AM UTC
  - [ ] Task 10 (CEO): Every 6 hours (0, 6, 12, 18 UTC)
  - [ ] Task 11 (CTO): On-demand when decision received

### Slack Notifications
- [ ] Set up bot for real-time alerts
  - [ ] New decision: `"CEO: SCALE venture X, capital=$50K"`
  - [ ] Risk flagged: `"⚠️ venture Y survival_metric=28 — CRITICAL"`
  - [ ] Execution complete: `"✅ SCALE execution: 500 leads sourced, 120 calls completed"`
- [ ] Daily summary: metrics dashboard link + top decisions

### Documentation
- [ ] README updated with deployment instructions
- [ ] OPERATIONS-EXECUTION-LAYER.md linked from main docs
- [ ] AGENT-SYSTEM-PROMPTS.md versioned (v1.0)
- [ ] Architecture diagram: data flow Week 0 cycle

---

## Phase 6: Go-Live (Day 15)

### Launch Steps
1. [ ] CFO agent goes live (7:00 AM UTC)
   - [ ] Calculates metrics for all ventures
   - [ ] Log: "Financial Analyst monthly cycle complete"
2. [ ] Wait 30 min for metrics to populate
3. [ ] CEO agent goes live (7:30 AM UTC)
   - [ ] Reads metrics from Supabase
   - [ ] Makes decisions for all ventures
   - [ ] Log: "CEO decision cycle complete"
4. [ ] CTO agent goes live (7:45 AM UTC)
   - [ ] Executes decisions via Composio
   - [ ] Commands dispatched to teams
   - [ ] Log: "Execution batch complete"

### First 24-Hour Monitoring
- [ ] Check Slack notifications (zero critical alerts)
- [ ] Review audit trail for all 3 agents
- [ ] Verify decision distribution (should be diverse, not all KILL)
- [ ] Confirm SMS campaigns sent (check Twilio dashboard)
- [ ] Monitor database performance (query times < 100ms)

### First Week Checklist
- [ ] Run 7 complete decision cycles (daily)
- [ ] No unplanned downtime
- [ ] Success rate ≥ 98%
- [ ] Adjust decision thresholds if needed
  - [ ] If too many COMPOUNDs: raise roi threshold from 100% to 120%
  - [ ] If too many KILLs: lower survival threshold from 30 to 25

---

## Rollback Plan

**If critical issue detected**:
1. [ ] Scale agent to 0 instances (pause all decisions)
2. [ ] Investigate root cause via logs (check `/api/agents/logs`)
3. [ ] Revert last Supabase migration if needed
4. [ ] Restore backup from pre-launch (T-24h)
5. [ ] Re-run metrics calculation for affected period
6. [ ] Notify CEO, CTO, CFO of incident

**Recovery Time Target**: 30 minutes to stable state

---

## Post-Launch (Weeks 2-4)

### Week 2: Stabilization
- [ ] Monitor decision quality (CEO feedback on decisions)
- [ ] Track execution results (leads sourced, SMS delivered, calls completed)
- [ ] Adjust thresholds based on real-world performance
- [ ] Add Sector PM advisory layer (read-only initially)

### Week 3: Optimization
- [ ] Analyze decision outcomes (did SCALE decisions lead to revenue growth?)
- [ ] A/B test SMS message variants
- [ ] Add Sector PM decision authority (OPTIMIZE decisions only)
- [ ] Increase cycle frequency (12-hour CEO decisions)

### Week 4: Scale
- [ ] Add second venture cohort to system
- [ ] Enable cross-venture capital reallocation (CEO decision)
- [ ] Full Sector PM autonomy (all decision types)
- [ ] Deploy monitoring dashboard to stakeholders

---

## Success Metrics

| Metric | Target | Threshold |
|---|---|---|
| Decision Accuracy | 90%+ (CFO/CEO decisions accurate) | > 80% acceptable |
| Execution Success Rate | 98%+ (commands execute successfully) | > 95% acceptable |
| System Uptime | 99.9% | > 99% acceptable |
| Decision Latency | < 5 min (metrics → CEO decision → CTO execution) | < 10 min acceptable |
| Audit Trail Completeness | 100% (all decisions logged) | > 95% acceptable |
| Risk Detection | Survival < 50 flagged within 24h | < 48h acceptable |

---

## Owner: CTO (Operations Manager)
Execution owner: Worldwidebro CEO  
Review/approval: CFO (metrics), Sector PMs (advisory)

