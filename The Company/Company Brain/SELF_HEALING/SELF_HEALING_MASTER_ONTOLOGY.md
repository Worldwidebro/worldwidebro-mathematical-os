---
type: control-node
status: conceptual
prerequisites: []
requires: []
---

# `SELF_HEALING_MASTER_ONTOLOGY.md`

[[SELF_HEALING]]

├── [[DETECTION]]
│   ├── [[HEALTH_CHECK]]
│   ├── [[HEARTBEAT]]
│   ├── [[TELEMETRY]]
│   ├── [[ANOMALY]]
│   ├── [[ERROR]]
│   ├── [[TIMEOUT]]
│   ├── [[DRIFT]]
│   └── [[FAILURE]]
│
├── [[DIAGNOSIS]]
│   ├── [[SYMPTOM]]
│   ├── [[FAILURE_CLASSIFICATION]]
│   ├── [[ROOT_CAUSE]]
│   ├── [[DEPENDENCY_ANALYSIS]]
│   ├── [[IMPACT_ANALYSIS]]
│   └── [[BLAST_RADIUS]]
│
├── [[RECOVERY]]
│   ├── [[RETRY]]
│   ├── [[BACKOFF]]
│   ├── [[RESTART]]
│   ├── [[ROLLBACK]]
│   ├── [[FAILOVER]]
│   ├── [[REROUTE]]
│   ├── [[REBUILD]]
│   ├── [[RESTORE]]
│   └── [[ISOLATE]]
│
├── [[VERIFICATION]]
│   ├── [[HEALTH_RECHECK]]
│   ├── [[CONNECTIVITY_TEST]]
│   ├── [[FUNCTIONAL_TEST]]
│   ├── [[DATA_VALIDATION]]
│   ├── [[REGRESSION_TEST]]
│   └── [[EVIDENCE]]
│
├── [[LEARNING]]
│   ├── [[INCIDENT_RECORD]]
│   ├── [[ROOT_CAUSE_RECORD]]
│   ├── [[LESSON]]
│   ├── [[PATTERN]]
│   ├── [[CAPABILITY_GAP]]
│   └── [[PREVENTION]]
│
└── [[GOVERNANCE]]
    ├── [[SAFE_ACTION]]
    ├── [[AUTHORIZED_ACTION]]
    ├── [[HUMAN_APPROVAL]]
    ├── [[ESCALATION]]
    └── [[AUDIT]]

---

# The self-healing loop

```text id="o7z0h9"
[[MONITOR]]
    ↓
[[DETECT]]
    ↓
[[CLASSIFY]]
    ↓
[[DIAGNOSE]]
    ↓
[[DECIDE]]
    ↓
[[RECOVER]]
    ↓
[[TEST]]
    ↓
[[VERIFY]]
    ↓
[[RESUME]]
    ↓
[[RECORD]]
    ↓
[[LEARN]]
    ↓
[[PREVENT]]
    ↺
```

Critical rule:

```text id="v91fcz"
[[RECOVERY]]
      ≠
[[VERIFIED_RECOVERY]]
```

And:

```text id="w9v8xb"
[[RESTARTED]]
      ≠
[[HEALTHY]]
```

A container coming back online doesn't prove the application is functioning.

---

# Healing levels

```text id="i8z8kz"
[[L0]] OBSERVE
     ↓
[[L1]] ALERT
     ↓
[[L2]] SAFE_AUTOMATIC_RECOVERY
     ↓
[[L3]] ADVANCED_AUTOMATIC_RECOVERY
     ↓
[[L4]] HUMAN_ESCALATION
     ↓
[[L5]] SYSTEM_REDESIGN
```

Example:

```text id="qpm6y7"
OmniRoute fails
    ↓
Health check
    ↓
Retry
    ↓
Restart container
    ↓
Connectivity test
    ↓
Provider test
    ↓
Claude test
    ↓
Verified?
    ├── YES → RESUME
    └── NO → FAILOVER / ESCALATE
```


---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
