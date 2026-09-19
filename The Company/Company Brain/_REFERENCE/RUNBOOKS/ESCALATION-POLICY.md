# Escalation Policy — Incident Response & Support

**Authority:** Orchestrator Reliability Team | **Last Updated:** 2026-09-18 | **Version:** 1.0

---

## Three-Level Escalation Model

All operational incidents follow **L1 → L2 → L3** escalation:

- **L1:** On-call Support (Issue Responder, 15-min response)
- **L2:** Infrastructure / Domain Specialist (30-min response)
- **L3:** Executive On-Call (Management escalation, 60-min response)

---

## Incident Triage Matrix

| Severity | MTTR | Detection | L1 Response | L2 Paged | L3 Paged | Examples |
|----------|------|-----------|-----------|----------|----------|----------|
| **Critical** | <5 min | Real-time alerts | Immediate page | Immediate | If unresolved 5 min | All tasks failing, revenue tracking down, auth broken |
| **High** | 10-30 min | Monitoring + user report | Investigate | If unresolved 5 min | If unresolved 15 min | Single capability degraded, Neo4j slow, discovery broken |
| **Medium** | 30-120 min | Daily audit or user report | Ticket tracking | If unresolved 30 min | If unresolved 60 min | API response > 500ms, fallback in use, single agent down |
| **Low** | 1-7 days | Weekly review | Backlog item | Standard schedule | Not paged | Documentation out of date, minor performance drift |

---

## Incident Categories & Routing

### Category: Task Execution & Orchestration

**Runbooks:**
- [[ORCHESTRATOR-TASK-STALLED]] — Task submitted but never completes
- [[DATABASE-POOL-EXHAUSTED]] — Connection pool exhausted, API timeouts

**L1 Suspects:**
1. Task status in Supabase is "running" but OmniRoute job is completed
2. Database connection count near max
3. Task age > 5 minutes

**L2 Escalation Criteria:**
- Affecting > 5 simultaneous tasks
- Recovery attempts failed (Option 1-2)
- Requires code change

**L3 Criteria:**
- Unresolved after 15 minutes
- Revenue impact > $5K/hour
- Multiple cascading failures

---

### Category: Knowledge Graph & Discovery

**Runbooks:**
- [[NEO4J-DISCOVERY-BROKEN]] — Agent discovery returns empty

**L1 Suspects:**
1. Neo4j container crashed (check `docker ps`)
2. Agent matching showing fallback YAML
3. Classification confidence < 0.3

**L2 Escalation Criteria:**
- Neo4j corrupted (failed health check)
- Index rebuild required
- ETL pipeline needs re-run

**L3 Criteria:**
- Unresolved after 20 minutes
- Discovery broken affecting all ventures
- Requires database restore from backup

---

### Category: Authentication & API Keys

**Runbooks:**
- [[AUTH-FAILED]] — Task classification fails with 401

**L1 Suspects:**
1. API key missing or invalid (test with curl)
2. API provider outage (check status page)
3. Key expired (compare with Bitwarden "last modified")

**L2 Escalation Criteria:**
- Multiple API keys invalid
- Requires new key generation from provider
- Env configuration needs update across services

**L3 Criteria:**
- Unresolved after 5 minutes
- Fallback classification in use (accuracy impact)
- Requires credential rotation across infrastructure

---

### Category: Revenue & Financial Tracking

**Runbooks:**
- [[WEBHOOK-HANDLER-DOWN]] — Revenue not attributed

**L1 Suspects:**
1. Webhook handler process not running
2. Database connection pool exhausted
3. revenue_logs table not updating

**L2 Escalation Criteria:**
- Backlog of unprocessed webhooks > 100
- Agent stats not updating (leaderboard stale)
- Financial data integrity concerns

**L3 Criteria:**
- Unresolved after 10 minutes
- Revenue data loss (financial audit impact)
- Multiple concurrent systems down

---

## Severity Assessment

### Critical (Page Immediately)

**Conditions:**
- ❌ NO task submissions succeeding (0% submission success rate)
- ❌ Revenue tracking broken (data not being recorded)
- ❌ All agent discovery failing (fallback only)
- ❌ System-wide authentication failure

**Action:**
1. **Page:** L2 lead immediately (5-min SLA)
2. **Context:** Provide current metrics (task count, error log, last working time)
3. **Escalate to L3:** If L2 can't resolve within 10 min
4. **Communication:** Update status page every 5 min

**Example Page Message:**
```
🚨 CRITICAL: Task Orchestrator Down
- 0 tasks completing (was 45/hour average)
- Last successful task: 14:32 UTC (12 min ago)
- Error: "database connection pool exhausted"
- MTTR: 5 min estimated
- Revenue Impact: ~$100/min
```

---

### High (Page Within 5 min)

**Conditions:**
- ⚠️ Single capability/pathway degraded (30-70% success rate)
- ⚠️ Database or Neo4j showing degradation (latency > 2s)
- ⚠️ Fallback mode active (reduced quality, temporary)
- ⚠️ Discovery latency > 5s consistently

**Action:**
1. **Page:** Domain specialist (L2)
2. **Investigate:** Root cause analysis (use runbooks)
3. **Attempt:** Recovery steps (Option 1-2 in runbook)
4. **Escalate:** If unresolved after 10 min, notify L3

**Example Page Message:**
```
⚠️ HIGH: Neo4j Discovery Slow
- Discovery queries taking 3-5s (normal: 200ms)
- Fallback YAML in use for 15 min
- Incident started: 14:45 UTC
- Likely cause: Missing indexes or high memory
- Owner: Knowledge Graph Team
```

---

### Medium (Ticket + 30-min Check-in)

**Conditions:**
- ℹ️ Single agent degraded or unavailable
- ℹ️ Capability performing at 70%+ but with issues
- ℹ️ API response time 500-1000ms
- ℹ️ Monitoring shows non-critical anomaly

**Action:**
1. **Ticket:** Create in ClickUp with Runbook link
2. **Context:** Attach logs, metrics, reproduction steps
3. **Assign:** Domain team (not on-call)
4. **Check-in:** 30 min later if unresolved
5. **Escalate:** If still unresolved after 60 min

**Example Ticket:**
```
Title: Medium - API Response Time Degradation
Severity: Medium (MTTR 30-120 min)
Impact: ~5% of tasks seeing > 1s latency
Root Cause: Unknown (investigate)
Runbook: Check Neo4j query latency (NEO4J-DISCOVERY-BROKEN step 4)
Assigned: @knowledge-graph-team
Due: 2 hours (with escalation)
```

---

### Low (Backlog Item)

**Conditions:**
- 📋 Minor performance drift (within acceptable SLA)
- 📋 Documentation out of date
- 📋 Observability enhancement needed
- 📋 Found during weekly audit, non-urgent

**Action:**
1. **Backlog:** Add to standard ClickUp backlog
2. **Priority:** Set to "Low"
3. **Cadence:** Address in normal sprint planning
4. **No escalation:** Standard priority

---

## Escalation Paths

### Critical → L2 (5 min) → L3 (10 min)

```
Incident Detected
    ↓
L1 Immediate Page (< 1 min)
    ├─ Attempt Option 1 (Restart service)
    ├─ Attempt Option 2 (Fallback/workaround)
    ↓ (after 5 min)
Escalate to L2
    ├─ Run full root cause analysis
    ├─ Attempt Option 3 (Advanced recovery)
    ├─ Coordinate with other teams if needed
    ↓ (after 10 min if unresolved)
Escalate to L3
    ├─ CEO/CTO level decision
    ├─ Resource allocation
    ├─ Communication to customers
    ├─ Post-mortem planning
```

### High → L2 (5 min) → L3 (15 min)

```
Issue Detected (alert or user report)
    ↓
L1 Triage (< 2 min)
    ├─ Identify severity (High?)
    ├─ Check runbook
    ↓
Page L2 (< 5 min)
    ├─ Root cause analysis
    ├─ Recovery attempts
    ↓ (after 10 min if unresolved)
Escalate to L3 (< 15 min total)
    ├─ Approval for downtime/data changes
    ├─ Resource coordination
```

### Medium → Ticket → L2 Check-in

```
Issue Reported
    ↓
L1 Creates Ticket (< 5 min)
    ├─ Assign to domain team
    ├─ Add runbook link
    ↓
L2 Investigates (30 min)
    ├─ Root cause analysis
    ├─ Proposed fix
    ↓ (after 30 min)
Check-in: Resolved or Escalate?
    ├─ If resolved → close ticket
    ├─ If not → escalate to High + page L3
```

---

## Contact Information

### L1 (Support On-Call)
- **Team:** Issue Responder / Orchestrator Support
- **Alert Channel:** PagerDuty (orchestrator-incidents)
- **Backup:** @ops-team-lead in Slack
- **Response SLA:** 15 min (automated page)

### L2 (Domain Specialists)
| Domain | Owner | Contact | Alert |
|--------|-------|---------|-------|
| **Orchestrator** | @orchestrator-lead | Slack + PagerDuty | orchestrator-p2 |
| **Knowledge Graph** | @neo4j-lead | Slack + PagerDuty | kg-p2 |
| **Infrastructure** | @infra-lead | Slack + PagerDuty | infra-p2 |
| **Security** | @security-lead | Slack + PagerDuty | security-p2 |
| **Revenue** | @finance-lead | Slack + PagerDuty | revenue-p2 |

### L3 (Executive)
- **On-Call:** CEO / CTO (rotating weekly)
- **Page:** Only for critical issues > 10 min
- **Slack:** #critical-incidents-exec

---

## Incident Response Workflow

### Phase 1: Detection (Automated)
```
Alert Rule Triggered
    ↓
Send to PagerDuty → L1 Notified
    ↓
Create Slack thread #incidents
```

**Key Actions:**
- Set incident status in OpsGenie
- Notify affected teams via Slack mention
- Post to #incidents channel immediately

### Phase 2: Triage (L1, 0-5 min)
```
L1 Assigned
    ↓
Acknowledge page (< 1 min)
    ↓
Check runbook for category
    ↓
Run diagnosis steps
    ↓
Attempt Option 1 recovery
```

**Key Actions:**
- Respond in Slack with status
- Link relevant runbook in thread
- Update incident severity if needed

### Phase 3: Escalation Decision (L1, 5 min)
```
Is Option 1 working?
    ├─ YES → Monitor + document
    │   └─ Update Slack: "Issue resolved, monitoring"
    │   └─ Post-incident review within 24h
    │
    └─ NO → Page L2
        └─ Update Slack: "Escalating to @l2-team"
        └─ Provide context summary
```

### Phase 4: Resolution (L2, 5-30 min)
```
L2 Receives Page
    ↓
Full root cause analysis
    ↓
Attempt Option 2-3 recovery
    ↓
Execute approved fix
    ↓
Verify resolution
    └─ SUCCESS → Communicate resolution
    └─ FAIL → Escalate to L3
```

### Phase 5: Escalation to L3 (L2, 10 min)
```
L2: Issue unresolved after 10 min
    ↓
Page L3 immediately
    ↓
Include:
    ├─ Root cause summary
    ├─ Attempts made
    ├─ Current impact
    ├─ Resource needs
    └─ Proposed solution
    ↓
L3 makes decision
    ├─ Approve fix + resources
    ├─ Or activate backup/failover
    ├─ Or coordinate external escalation
```

### Phase 6: Communication & Recovery

**During Incident:**
- Update #incidents channel every 10 min
- Communicate to customers (if critical)
- Track timeline in incident document

**After Resolution:**
- Post "All Clear" message
- Schedule post-mortem (24 hours for critical, 48h for high)
- Create action items for prevention

**Post-Mortem (24h):**
- Timeline of incident
- Root cause
- Detection gaps
- Prevention measures
- Owner & deadline for follow-ups

---

## Key Metrics & Thresholds

### Alerting Thresholds

| Metric | Threshold | Severity | Action |
|--------|-----------|----------|--------|
| Task success rate | < 95% | Medium | Investigate |
| Task success rate | < 80% | High | Page L2 |
| Task success rate | < 50% | Critical | Page L2 + L3 |
| Discovery latency | > 2s | Medium | Monitor |
| Discovery latency | > 5s | High | Page L2 |
| Database connections | > 80% of max | Medium | Check pool |
| Database connections | > 95% of max | Critical | Page immediately |
| API response time (p95) | > 500ms | Medium | Investigate |
| API response time (p95) | > 2000ms | High | Page L2 |
| Revenue data lag | > 5 min | High | Page revenue team |
| Revenue data lag | > 15 min | Critical | Page L2 + L3 |

---

## Prevention & Long-Term Measures

### Weekly Audit
```
Every Monday 10 AM UTC:
- Review alert trends
- Check metrics dashboards
- Identify prevention opportunities
- Create "Low" priority tickets
- Update runbooks based on incidents
```

### Monthly Review
```
First Thursday of month:
- Analyze all incidents from prior month
- Calculate MTTR by category
- Identify systemic issues
- Plan prevention work
- Update escalation policy if needed
```

### Quarterly Audit
```
End of quarter:
- Review escalation effectiveness
- Measure page volume and MTTR
- Identify missing runbooks
- Plan capability improvements
- Update contact information
```

---

## Related Documentation

- [[ORCHESTRATOR-TASK-STALLED]] — Common incident
- [[NEO4J-DISCOVERY-BROKEN]] — Knowledge graph issues
- [[DATABASE-POOL-EXHAUSTED]] — Connection management
- [[WEBHOOK-HANDLER-DOWN]] — Revenue tracking
- [[AUTH-FAILED]] — Authentication issues
- [[README|_REFERENCE/RUNBOOKS/README.md]] — Runbooks index

---

**Version:** 1.0 | **Last Updated:** 2026-09-18 | **Next Review:** 2026-10-18
