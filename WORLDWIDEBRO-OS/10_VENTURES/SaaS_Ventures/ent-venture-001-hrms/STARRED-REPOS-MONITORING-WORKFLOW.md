# STARRED-REPOS-MONITORING-WORKFLOW: Real-Time Operations Observability

## Overview

Defines monitoring, alerting, and SLA tracking for 12 starred repositories across 4-tier deployment stack. Ensures visibility into system health, deployment progress, and agent decision-making.

**Last Updated**: 2026-06-02  
**Framework Version**: 1.0  
**Owned By**: hrms-operations-ai-001 (primary), hrms-founder-001 (oversight)

---

## Monitoring Stack

### Observability Pipeline
```
Repos (build logs, runtime logs, git events)
  ↓
Supabase (audit logs, agent decisions, customer events)
  ↓
Qdrant (vector embeddings of system state)
  ↓
Dashboard (venture-hub real-time sync)
  ↓
Alerts (Slack #hrms on SLA breach, deployment blocker, anomaly)
```

### Metrics by Tier

#### **Tier 0: Foundation (civilization-os + iza-os-rag-system)**
| Metric | Target | Alert Threshold | Check Interval |
|--------|--------|-----------------|-----------------|
| Knowledge graph indexing latency | <100ms | >500ms | 5m |
| Entity count (17+ required) | 17+ | <15 | 1h |
| RAG embedding freshness | <1h old | >4h old | 30m |
| Vector DB query latency | <200ms | >1000ms | 5m |
| MCP server availability | 99.9% | <99% | 10m |

#### **Tier 1: Core (the-office, venture-hub, venture-factory-core, autonomous-venture-studio)**
| Metric | Target | Alert Threshold | Check Interval |
|--------|--------|-----------------|-----------------|
| Dashboard render latency | <500ms | >2000ms | 10m |
| Real-time sync delay | <1s | >5s | 5m |
| Agent decision latency (RACI evaluation) | <2s | >10s | 5m |
| Venture provisioning success rate | 99% | <95% | hourly |
| API availability | 99.95% | <98% | 10m |

#### **Tier 2: Ventures (con-001-ace-construction, con-012-hvac-services, lt-009-hvac-technician-dispatch)**
| Metric | Target | Alert Threshold | Check Interval |
|--------|--------|-----------------|-----------------|
| Customer portal response time | <1s | >3s | 5m |
| Payment processing success rate | 99.5% | <97% | hourly |
| Dispatch route calculation time | <5s | >15s | 10m |
| Technician availability display | real-time | >30s stale | 5m |

#### **Tier 3: Templates (pitch-kit, ai-venture-studio-template, business-template-marketplace)**
| Metric | Target | Alert Threshold | Check Interval |
|--------|--------|-----------------|-----------------|
| Template rendering latency | <2s | >5s | hourly |
| Marketplace API response time | <1s | >3s | hourly |
| License validation latency | <500ms | >2000ms | hourly |

---

## Deployment Status Tracking

### Deployment Sequence Monitoring
```
Seq 1-2 (Tier 0)     → Gate: "Knowledge graph ready"
Seq 3-5 (Tier 1)     → Gate: "Core infrastructure ready"
Seq 6-8 (Tier 2)     → Gate: "Venture implementations live"
Seq 9-11 (Tier 3)    → Gate: "Templates integrated"
Seq 12 (Parallel)    → Gate: "Simulation engine ready"
```

**Status Checks Per Gate**:
- Knowledge graph: entity count, indexing latency, Supabase sync
- Core infrastructure: dashboard load time, real-time sync, auth SLA
- Ventures: customer portal, payment processing, dispatch accuracy
- Templates: rendering latency, marketplace availability, license validation

---

## Agent Decision Monitoring

### Decision Log Tracking
Every agent decision logged to Supabase `agent_decisions` table with:
- Agent ID (hrms-support-ai-001 etc)
- Decision type (escalation, approval, routing, etc)
- RACI role invoked (Responsible, Accountable, Consulted, Informed)
- Resolution time (vs SLA target)
- Outcome (approved, denied, escalated, delegated)

### SLA Compliance Dashboard
Real-time display in venture-hub showing:
- Support Escalations: 4h SLA (target: 95% on-time)
- Sales Deals >$500/month: 8h SLA (target: 95% on-time)
- Payment Disputes: 24h SLA (target: 99% on-time)
- Feature Releases: 24h SLA (target: 95% on-time)
- Compliance/Audit: 48h SLA (target: 100% on-time)

---

## Alert Rules

### Critical Alerts (Slack #hrms with @hrms-founder-001 mention)
- Tier 0 service unavailable (>15 min)
- API availability <95%
- Payment processing success rate <90%
- Customer data breach or security incident
- Founder escalation requested

### Warning Alerts (Slack #hrms without mention)
- SLA approach: escalation within 80% of SLA time
- Resource usage >80% of baseline
- Deployment gate blocked for >2 hours
- Vector DB latency >500ms (trend)

### Info Alerts (Dashboard only, no Slack post)
- Routine sync latencies
- Template rendering >2s but <5s
- Non-critical metric drift

---

## Monitoring Workflow: Daily Operations

### 07:00 (Morning Sync - hrms-operations-ai-001)
1. Check Tier 0 health (knowledge graph, vector DB, MCP servers)
2. Review overnight agent decisions (any escalations? any blocks?)
3. Check venture portal availability
4. Post daily metrics to #hrms (MRR, customer count, decision velocity, any SLA breaches)

### 12:00 (Mid-Day Check - hrms-operations-ai-001)
1. Deployment gate status (how close to next gate unlock?)
2. Payment processing (any failed charges? any disputes?)
3. Dispatch accuracy (technician ETA vs actual for con-012)

### 17:00 (End-Of-Day Review - hrms-founder-001 spot-check)
1. Agent decision quality (are escalations being made correctly? are decisions aligned with RACI?)
2. Customer satisfaction (any complaints? any churn signals?)
3. Tomorrow's blockers (any maintenance windows? deployments scheduled?)

### Weekly (Friday EOD - hrms-founder-001)
1. Deployment progress vs 12-step schedule
2. Agent performance (decision latency, escalation rate, SLA compliance)
3. Cost tracking vs budget (Supabase, Stripe, ClickUp, shared services)
4. Venture metrics (MRR, customer count, churn, LTV)

---

## Automated Remediation

### Auto-Retry Rules
- API calls: retry 3x with exponential backoff
- Sync failures: retry every 10s for 5 minutes then alert
- Vector DB indexing failures: retry with priority flag

### Circuit Breaker Rules
- If Tier 0 unavailable >15 min: deactivate all agents, activate founder-override mode
- If payment processing fails 3x: route all charges through manual review queue
- If dispatch engine offline: activate fallback static routing, alert technicians

---

## Cost Monitoring

### Monthly Cost Breakdown
| Service | Baseline | Growth Threshold | Alert At | Owner |
|---------|----------|-----------------|----------|-------|
| Supabase | $25/mo | $50/mo | $75/mo | hrms-operations-ai-001 |
| Qdrant | $50/mo | $100/mo | $150/mo | hrms-operations-ai-001 |
| ClickUp | $300/mo | $500/mo | $750/mo | hrms-founder-001 |
| Stripe | 2.9% + $0.30 | 3% of MRR | >$500/mo fees | hrms-sales-ai-001 |
| Google Maps | $100/mo | $200/mo | $300/mo | hrms-product-ai-001 |
| **Total Est.** | **$475/mo** | — | **$1200/mo** | hrms-founder-001 |

---

## Escalation Paths

### Incident Escalation
```
Alert Fires
  ↓
Auto-remediation triggered (3s)
  ↓
If auto-remediation succeeds → close ticket
  ↓
If auto-remediation fails → escalate to hrms-operations-ai-001 (10s)
  ↓
If ops-ai cannot resolve → escalate to hrms-founder-001 (2m timeout)
  ↓
If founder unavailable → activate emergency procedures (see Handoff_Procedures.json)
```

### Decision Escalation (SLA tracked)
```
Agent makes decision
  ↓
Check decision against RACI matrix
  ↓
If decision authority unclear → escalate to hrms-founder-001
  ↓
Founder decides within escalation SLA (4-48h depending on type)
  ↓
Document decision in agent_decisions log, update Agent_Manifest.json if rule change needed
```

---

## Audit Trail

| Field | Value |
|-------|-------|
| Created By | hrms-operations-ai-001 |
| Created Date | 2026-06-02T00:00:00Z |
| Last Updated By | hrms-operations-ai-001 |
| Last Updated Date | 2026-06-02T00:00:00Z |
| Change Summary | Created initial monitoring workflow: observability pipeline, SLA tracking, alert rules, cost monitoring |
| Version | 1.0 |

---

## Contact

**Primary Owner**: hrms-operations-ai-001  
**Backup Owner**: hrms-founder-001  
**On-Call**: See Agent_Manifest.json for 24/7 rotation  
**Escalation Email**: winnerscirclewcllc@gmail.com
