---
type: control-node
status: conceptual
prerequisites: []
requires: []
---

# `EXECUTIVE_SYSTEM_MASTER_ONTOLOGY.md`

[[EXECUTIVE_SYSTEM]]

├── [[EXECUTIVE_IDENTITY]]
│   ├── [[EXECUTIVE]]
│   ├── [[ROLE]]
│   ├── [[DOMAIN]]
│   ├── [[MISSION]]
│   └── [[RESPONSIBILITY]]
│
├── [[EXECUTIVE_AUTHORITY]]
│   ├── [[DECISION_RIGHTS]]
│   ├── [[RESOURCE_AUTHORITY]]
│   ├── [[DELEGATION_AUTHORITY]]
│   ├── [[APPROVAL_AUTHORITY]]
│   ├── [[ESCALATION_AUTHORITY]]
│   └── [[EMERGENCY_AUTHORITY]]
│
├── [[EXECUTIVE_COGNITION]]
│   ├── [[SITUATIONAL_AWARENESS]]
│   ├── [[STRATEGIC_REASONING]]
│   ├── [[PRIORITIZATION]]
│   ├── [[TRADEOFF_ANALYSIS]]
│   ├── [[RISK_ANALYSIS]]
│   └── [[DECISION_MAKING]]
│
├── [[EXECUTIVE_COORDINATION]]
│   ├── [[DELEGATION]]
│   ├── [[RESOURCE_ALLOCATION]]
│   ├── [[SCHEDULING]]
│   ├── [[CONFLICT_RESOLUTION]]
│   ├── [[HANDOFF]]
│   └── [[ESCALATION]]
│
├── [[EXECUTIVE_CONTROL]]
│   ├── [[MONITORING]]
│   ├── [[POLICY_ENFORCEMENT]]
│   ├── [[PERFORMANCE]]
│   ├── [[RISK]]
│   ├── [[COMPLIANCE]]
│   └── [[AUDIT]]
│
└── [[EXECUTIVE_FEEDBACK]]
    ├── [[OUTCOMES]]
    ├── [[METRICS]]
    ├── [[LESSONS]]
    ├── [[CAPABILITY_GAPS]]
    └── [[STRATEGY_UPDATE]]

## Executive graph

```text id="9zv3gj"
                         [[CEO_AGENT]]
                              │
                ┌─────────────┼──────────────┐
                ↓             ↓              ↓
        [[CHIEF_OF_STAFF]] [[CFO]]         [[CTO]]
                │             │              │
        ┌───────┼──────┐      │        ┌─────┼─────┐
        ↓       ↓      ↓      ↓        ↓     ↓     ↓
     OPS     STRATEGY  PM   FINANCE   DATA  INFRA  AI
        │       │      │      │        │     │     │
        └───────┴──────┴──────┴────────┴─────┴─────┘
                              ↓
                         [[ORCHESTRATOR]]
                              ↓
                           [[AGENTS]]
```

But the executive layer should **delegate downward**, not micromanage every action.

---

# Executive functions

I'd define these as canonical Company Brain executives:

```text id="iwp8s5"
[[CEO_AGENT]]
[[CHIEF_OF_STAFF_AGENT]]
[[COO_AGENT]]
[[CFO_AGENT]]
[[CTO_AGENT]]
[[CIO_AGENT]]
[[CAIO_AGENT]]
[[CMO_AGENT]]
[[CPO_AGENT]]
[[CRO_AGENT]]
[[CHIEF_DATA_AGENT]]
[[CHIEF_SECURITY_AGENT]]
[[CHIEF_LEGAL_AGENT]]
[[CHIEF_RISK_AGENT]]
[[CHIEF_STRATEGY_AGENT]]
```

Their function is:

```text id="b3n9ax"
CEO
→ WHAT MATTERS?

CHIEF_OF_STAFF
→ WHAT NEEDS COORDINATION?

COO
→ WHAT NEEDS TO OPERATE?

CFO
→ WHAT RESOURCES/CAPITAL ARE REQUIRED?

CTO
→ WHAT TECHNOLOGY IS REQUIRED?

CIO
→ WHAT INFORMATION SYSTEMS ARE REQUIRED?

CAIO
→ WHAT AI CAPABILITIES ARE REQUIRED?

CMO
→ WHAT MARKET/DEMAND SYSTEM IS REQUIRED?

CRO
→ WHAT REVENUE SYSTEM IS REQUIRED?

CPO
→ WHAT PRODUCT SYSTEM IS REQUIRED?

CISO
→ WHAT MUST BE PROTECTED?

RISK
→ WHAT CAN GO WRONG?

DATA
→ WHAT DOES THE EVIDENCE SHOW?

STRATEGY
→ WHERE SHOULD THE SYSTEM GO?
```

These are **functional domains**, not rankings.

---

# Executive decision loop

```text id="m3jp9w"
[[EXECUTIVE]]
      ↓
[[OBSERVE]]
      ↓
[[ORIENT]]
      ↓
[[IDENTIFY_GAP]]
      ↓
[[PRIORITIZE]]
      ↓
[[DECIDE]]
      ↓
[[DIRECT]]
      ↓
[[DELEGATE]]
      ↓
[[MONITOR]]
      ↓
[[VERIFY]]
      ↓
[[OUTCOME]]
      ↓
[[LEARN]]
      ↺
```


---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
