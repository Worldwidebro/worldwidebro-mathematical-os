---
id: ONT-LIFECYCLE-001
title: "Status Lifecycle & State Transitions Specification"
aliases: ["_ONTOLOGY/STATUS_LIFECYCLE", "Status Lifecycle & State Transitions Specification"]
tags: [ontology, lifecycle, status, state-machine, governance]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[07-ONTOLOGY/README|Ontology Hub]] | [[_ONTOLOGY/COGNITION_FLOW.yaml|Cognition Flow]] | [[46-GOVERNANCE/README|Governance]]

# Status Lifecycle & State Transitions

**Principle:** Every entity in the Company Brain moves through well-defined lifecycle states. This document defines the state machine for different entity types.

---

## Universal Status States

All entities follow a common progression from initial discovery to trusted operational status:

```
DOCUMENTED  →  REGISTERED  →  CONFIGURED  →  AVAILABLE
    ↓                             ↓              ↓
   Found               Added to system       Set up/Ready
   Captured            Indexed/Listed         Tested
   Described           Identity assigned     Production-ready
```

Then, for operational entities:

```
AVAILABLE  →  CONNECTED  →  TESTED  →  ACTIVE  →  TRUSTED
   ↓             ↓            ↓           ↓           ↓
Ready for     Wired to    Verified    Running in   Stable &
use           systems     working     production   Monitored
```

---

## State Definitions

### DOCUMENTED
**When:** Entity first identified or created  
**Characteristics:**
- Exists as concept or prototype
- Has name, description, rationale
- Not yet in production systems
- May be in wiki or design document

**Transitions to:** REGISTERED (when ready for inventory)  
**Examples:**
- New capability idea in RFC
- New venture identified in research
- New risk identified but not tracked
- New process defined but not implemented

**Metadata:**
```yaml
status: DOCUMENTED
created_by: PER-000123
created_date: 2026-09-01
rationale: "..."
readiness_gates:
  - documented: ✓
  - has_owner: ✗
  - has_rationale: ✓
```

---

### REGISTERED
**When:** Entity added to tracking system  
**Characteristics:**
- Has unique ID (TYPE-000001)
- Exists in inventory (registry)
- Has assigned owner/domain
- Has initial metadata

**Transitions to:** CONFIGURED (when dependencies set up)  
**Examples:**
- Venture added to VEX (VEN-500)
- Capability added to registry (CAP-300)
- Agent added to registry (AGT-125)
- KPI added to dashboard (KPI-089)

**Metadata:**
```yaml
status: REGISTERED
ref_id: CAP-000248
type: "Capability"
owner: TEA-000034
domain: "14-CAPABILITIES"
registered_date: 2026-09-01
registered_by: PER-000002
readiness_gates:
  - has_id: ✓
  - in_registry: ✓
  - has_owner: ✓
  - has_domain: ✓
```

---

### CONFIGURED
**When:** Entity configured for use  
**Characteristics:**
- Dependencies understood
- Integration points defined
- Access/permissions configured
- Configuration tested
- Not yet in production

**Transitions to:** AVAILABLE (when ready for deployment)  
**Examples:**
- Service container built
- API endpoints provisioned
- Database schema created
- Workflow defined and triggers configured
- Monitor/alert rules defined

**Metadata:**
```yaml
status: CONFIGURED
ref_id: SVC-000045
owner: TEA-000034
configured_date: 2026-09-01
dependencies:
  - CAP-000248: ✓
  - DST-000087: ✓
integration_points:
  - API-000012: ✓
  - MCP-000005: ✓
access_controls:
  - permissions_assigned: ✓
  - roles_created: ✓
test_result: "PASS"
readiness_gates:
  - dependencies_met: ✓
  - integration_complete: ✓
  - access_configured: ✓
  - tests_pass: ✓
```

---

### AVAILABLE
**When:** Entity ready for deployment but not in production  
**Characteristics:**
- Fully configured and tested
- Can be deployed on demand
- Documentation complete
- Runbooks/procedures exist
- Not yet active in production

**Transitions to:** CONNECTED (when integrated with live systems)  
**Examples:**
- Docker image built, ready to push
- Code branch ready to merge
- New venture setup complete
- Report template created
- Alert rule configured

**Metadata:**
```yaml
status: AVAILABLE
ref_id: CNT-000098
owner: TEA-000034
available_since: 2026-09-01
deployment_instructions: "kubectl apply -f..."
test_status: "PASS"
documentation: "✓ README, ✓ API docs, ✓ runbook"
dependencies_satisfied: true
readiness_gates:
  - documentation_complete: ✓
  - deployment_path_defined: ✓
  - all_tests_pass: ✓
  - stakeholders_aware: ✓
```

---

### CONNECTED
**When:** Entity integrated with live systems  
**Characteristics:**
- Deployed to production
- Receiving traffic/being used
- Live monitoring in place
- Performance baseline established
- Not yet fully trusted

**Transitions to:** TESTED (when stability verified)  
**Examples:**
- Service deployed to Kubernetes
- Agent connected to webhook
- API endpoint live and receiving requests
- Data pipeline running
- Monitor collecting data

**Metadata:**
```yaml
status: CONNECTED
ref_id: SVC-000045
owner: TEA-000034
connected_date: 2026-09-01
connected_by: PER-000004
deployment:
  - environment: "production"
  - version: "v1.2.3"
  - start_time: "2026-09-01T10:30:00Z"
monitoring:
  - metrics_collector: "datadog"
  - logs_destination: "CloudWatch"
  - alerts_configured: true
error_rate: "0.02%"
latency_p99: "145ms"
readiness_gates:
  - in_production: ✓
  - receiving_traffic: ✓
  - monitoring_active: ✓
  - baseline_established: ✓
```

---

### TESTED
**When:** Entity demonstrates stable production behavior  
**Characteristics:**
- 2+ weeks of production data
- Error rate stable and acceptable
- No critical issues
- Performance meets expectations
- Ready for SLA/SLO commitments

**Transitions to:** ACTIVE (when SLA commitments made)  
**Examples:**
- Service running 2 weeks, error rate <1%
- Agent running 100+ tasks, 98% success rate
- API handling peak load with <500ms P99
- Database backups verified for 2 weeks
- Loop executed 8+ times with expected results

**Metadata:**
```yaml
status: TESTED
ref_id: SVC-000045
owner: TEA-000034
test_period: "2026-09-01 to 2026-09-15"
test_period_duration_days: 14
performance_metrics:
  error_rate: "0.02%"
  latency_p99: "145ms"
  availability: "99.95%"
  success_rate: "99.98%"
stability_assessment: "STABLE"
critical_issues_found: 0
major_issues_found: 0
minor_issues_found: 1
readiness_gates:
  - production_time_minimum: ✓ (14+ days)
  - error_rate_acceptable: ✓ (<1%)
  - no_critical_issues: ✓
  - performance_meets_expectations: ✓
```

---

### ACTIVE
**When:** Entity committed in production with SLA  
**Characteristics:**
- Formal SLA/SLO published
- On-call rotation assigned
- Runbooks documented
- Escalation path defined
- Incident response ready

**Transitions to:** TRUSTED (when SLA consistently met)  
**Examples:**
- Service with 99.95% uptime SLA
- Agent with published response time SLO
- KPI dashboard with alert thresholds
- Loop with committed execution schedule
- API with published rate limits

**Metadata:**
```yaml
status: ACTIVE
ref_id: SVC-000045
owner: TEA-000034
activated_date: 2026-09-15
activated_by: PER-000005
sla:
  availability_target: "99.95%"
  response_time_p99: "<200ms"
  error_rate_target: "<0.5%"
slo:
  availability_target: "99.9%"
  latency_p99: "<150ms"
monitoring:
  - sli_availability: "datadog/uptime"
  - sli_latency: "datadog/p99_latency"
  - sli_error_rate: "datadog/error_pct"
on_call:
  - primary: PER-000123
  - secondary: PER-000124
  - rotation_schedule: "weekly"
runbook: "docs/runbooks/svc-000045.md"
escalation_path: "Tier 1 → Tier 2 Eng → Team Lead → Manager"
readiness_gates:
  - sla_defined: ✓
  - slo_defined: ✓
  - sli_implemented: ✓
  - on_call_assigned: ✓
  - runbook_complete: ✓
  - escalation_defined: ✓
```

---

### TRUSTED
**When:** Entity consistently meets SLA/SLO for 90+ days  
**Characteristics:**
- SLA met for 90+ days
- Handled production incidents successfully
- Team has high confidence
- Optimization/enhancement mode
- Baseline for comparison/benchmarking

**Transitions to:** ACTIVE (downgrade if SLA breached) or maintenance  
**Examples:**
- Service with 99.97% uptime last quarter
- Agent with 99.5% task success rate
- Database backup verified 100+ times
- Loop executing flawlessly for 3 months
- API serving 99.9% of requests under SLA

**Metadata:**
```yaml
status: TRUSTED
ref_id: SVC-000045
owner: TEA-000034
trusted_since: 2026-12-15
last_sla_review: 2026-12-15
sla_performance_90d:
  availability: "99.98%"  # (target: 99.95%)
  latency_p99: "128ms"    # (target: <200ms)
  error_rate: "0.015%"    # (target: <0.5%)
incidents_90d:
  major: 0
  minor: 1
confidence_level: "HIGH"
team_sentiment: "Stable, focusing on enhancements"
readiness_gates:
  - sla_met_90d: ✓
  - incidents_handled: ✓
  - no_critical_issues: ✓
  - team_confident: ✓
next_phase: "Optimization & scaling"
```

---

## State Transitions by Entity Type

### Services (SVC)
```
DOCUMENTED → REGISTERED → CONFIGURED → AVAILABLE → CONNECTED → TESTED → ACTIVE → TRUSTED
```

### Capabilities (CAP)
```
DOCUMENTED → REGISTERED → CONFIGURED → AVAILABLE → ACTIVE → TRUSTED
```

### Loops (LOP)
```
DOCUMENTED → REGISTERED → TESTED → ACTIVE → TRUSTED
```

### Metrics/KPIs (MTR, KPI)
```
DOCUMENTED → REGISTERED → TESTED → ACTIVE → TRUSTED
```

### Decisions (DEC)
```
DOCUMENTED → ACTIVE → TRUSTED (or SUPERSEDED)
```

### Policies (POL)
```
DOCUMENTED → REGISTERED → ACTIVE → TRUSTED
```

---

## Downgrade Conditions

An entity can downgrade if:

- **SLA breach:** ACTIVE/TRUSTED → TESTED (failed SLA)
- **Critical issue:** Any → DOCUMENTED (major rewrite needed)
- **Obsolescence:** ACTIVE/TRUSTED → DOCUMENTED (superseded)
- **Unmet dependency:** TESTED → CONFIGURED (critical dep fails)

**Downgrade requires:**
- Formal decision (DEC entity)
- Root cause analysis
- New state assigned with rationale
- Timeline for remediation

**Example:**
```yaml
downgrade:
  from_status: "TRUSTED"
  to_status: "TESTED"
  reason: "Database performance degradation"
  triggered_date: "2026-09-20"
  root_cause: "Missing index on venture_id"
  remediation:
    - add_index: "CREATE INDEX ON ventures(venture_id)"
    - retest_period: "7 days"
    - re_evaluate: "2026-09-27"
  decision: "DEC-000098"
```

---

## Lifecycle Diagram

```
DOCUMENTED
    ↓
REGISTERED
    ↓
CONFIGURED
    ↓
AVAILABLE
    ↓
CONNECTED (parallel testing)
    ↓
TESTED ←─────────────────── (downgrade)
    ↓
ACTIVE ←───── (SLA breach downgrade)
    ↓
TRUSTED
    ↓
(SUPERSEDED or MAINTENANCE)
```

---

## Quality Standards

1. **State progression tracked** — Date, actor, rationale recorded
2. **Readiness gates explicit** — Clear transition conditions
3. **Performance baselines** — Established at CONNECTED, verified at TESTED
4. **SLA/SLO transparency** — Published with ACTIVE status
5. **Incident handling** — Critical issues trigger downgrade review

**Status:** Active | **Last Updated:** 2026-09-01
---

## Connected Subsystems
- **Ontology Hub:** [[07-ONTOLOGY/README|07-ONTOLOGY]]
- **Cognition Flow:** [[_ONTOLOGY/COGNITION_FLOW.yaml|Cognition Flow Matrix]]
- **Governance Portal:** [[46-GOVERNANCE/README|46-GOVERNANCE]]
- **Truth Status Standard:** [[_ONTOLOGY/TRUTH_STATUS.yaml]]
