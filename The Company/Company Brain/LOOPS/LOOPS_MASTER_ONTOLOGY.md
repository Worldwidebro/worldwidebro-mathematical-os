---
type: control-node
status: conceptual
prerequisites: []
requires: []
---

# `LOOPS_MASTER_ONTOLOGY.md`

[[LOOPS]]

├── [[COGNITIVE_LOOPS]]
│   ├── [[THINKING_LOOP]]
│   ├── [[QUESTION_LOOP]]
│   ├── [[REASONING_LOOP]]
│   ├── [[REFLECTION_LOOP]]
│   └── [[LEARNING_LOOP]]
│
├── [[OPERATIONAL_LOOPS]]
│   ├── [[TASK_LOOP]]
│   ├── [[WORKFLOW_LOOP]]
│   ├── [[EXECUTION_LOOP]]
│   ├── [[HANDOFF_LOOP]]
│   └── [[ESCALATION_LOOP]]
│
├── [[BUSINESS_LOOPS]]
│   ├── [[SALES_LOOP]]
│   ├── [[CUSTOMER_LOOP]]
│   ├── [[REVENUE_LOOP]]
│   ├── [[PRODUCT_LOOP]]
│   ├── [[MARKETING_LOOP]]
│   └── [[CAPITAL_LOOP]]
│
├── [[TECHNICAL_LOOPS]]
│   ├── [[BUILD_LOOP]]
│   ├── [[TEST_LOOP]]
│   ├── [[DEPLOY_LOOP]]
│   ├── [[MONITOR_LOOP]]
│   ├── [[INCIDENT_LOOP]]
│   └── [[RECOVERY_LOOP]]
│
├── [[KNOWLEDGE_LOOPS]]
│   ├── [[INGESTION_LOOP]]
│   ├── [[INDEXING_LOOP]]
│   ├── [[LINKING_LOOP]]
│   ├── [[GRAPH_UPDATE_LOOP]]
│   ├── [[RETRIEVAL_LOOP]]
│   └── [[KNOWLEDGE_REFRESH_LOOP]]
│
└── [[STRATEGIC_LOOPS]]
    ├── [[OBJECTIVE_LOOP]]
    ├── [[PRIORITY_LOOP]]
    ├── [[RESOURCE_LOOP]]
    ├── [[PORTFOLIO_LOOP]]
    └── [[STRATEGY_LOOP]]

---

# Universal loop ontology

Every loop can be represented as:

```text id="h2fsrj"
[[TRIGGER]]
    ↓
[[OBSERVE]]
    ↓
[[INTERPRET]]
    ↓
[[DECIDE]]
    ↓
[[ACT]]
    ↓
[[MEASURE]]
    ↓
[[COMPARE]]
    ↓
[[ADJUST]]
    ↓
[[REPEAT]]
```

With:

```text id="qvl7m4"
[[STATE]]
[[INPUT]]
[[TRANSFORMATION]]
[[ACTION]]
[[OUTPUT]]
[[MEASUREMENT]]
[[FEEDBACK]]
[[CORRECTION]]
[[NEXT_STATE]]
```

---

# Nested loops

This is where the architecture becomes much more powerful.

```text id="qf4jhi"
                     [[STRATEGIC LOOP]]
                            │
                     ┌──────┴──────┐
                     ↓             ↓
               [[BUSINESS]]   [[TECHNICAL]]
                     │             │
                ┌────┴────┐   ┌────┴────┐
                ↓         ↓   ↓         ↓
             SALES      PRODUCT BUILD    OPS
                │         │     │         │
                └─────────┴─────┴─────────┘
                            ↓
                     [[EXECUTION LOOP]]
                            ↓
                      [[TASK LOOP]]
                            ↓
                       [[ACTION]]
                            ↓
                       [[OUTCOME]]
                            ↓
                     [[FEEDBACK]]
                            ↺
```

So:

**Loops contain loops.**


---
**Related:** [[WHERE_WE_ARE]] · [[CROSS_LINK_MASTER_ONTOLOGY]]
