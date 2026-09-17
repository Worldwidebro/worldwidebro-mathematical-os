# Company Brain: Logic Architecture Framework

**Document ID:** LOGIC-ARCH-001  
**Updated:** 2026-09-17  
**Authority:** CP-001 (Strategic) + CP-032 (Execution)  
**Master Registry:** [[_REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml]]

---

## Overview

The **Company Brain** operates as a sophisticated **rule system** that governs what the organization, software, agents, and infrastructure do—when to do it, and how to react when reality changes.

This architecture consolidates **72 distinct logic layers** across **12 master domains** into a coherent, queryable, autonomous system.

---

## The 12 Master Logic Domains

```
                    COMPANY BRAIN
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
       ▼                  ▼                  ▼
   PURPOSE             ECONOMICS          GOVERNANCE
       │                  │                  │
 identity              business            policy
 objectives            revenue             permissions
 strategy              capital             approvals
                      allocation           risk
       │                  │                  │
       └──────────────────┼──────────────────┘
                          │
                          ▼
                    OPERATIONS
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
           process     workflow    scheduling
           routing     dispatch    fulfillment
                          │
                          ▼
                    INTELLIGENCE
                          │
       ┌──────────────────┼──────────────────┐
       ▼                  ▼                  ▼
     agents             models            knowledge
     prompts            context            memory
     tools              retrieval           graph
                          │
                          ▼
                     EXECUTION
                          │
                    events/state
                          │
                          ▼
                   CONTROL SYSTEM
                          │
       ┌──────────────────┼──────────────────┐
       ▼                  ▼                  ▼
     verify             evaluate           observe
     recover            escalate            audit
                          │
                          ▼
                     LEARNING
                          │
                  learn → adapt → improve
```

---

## The Four Core Logic Types

### 1. Declarative Logic — "What is true?"

**Captures current state and ground truth.**

- Databases, registries, policies, knowledge graph
- Facts that don't change unless explicitly updated
- Examples: Customer status, inventory levels, employee roles

**Location:** [[_REGISTRIES/CANONICAL/]], Neo4j nodes, state snapshots

---

### 2. Decision Logic — "Given current state, what should happen?"

**Governs choices between alternatives.**

- Business rules, conditions, thresholds
- Decision engines and frameworks
- Approval gates and permission checks

**Location:** [[20-DECISIONS/]], [[13-WORKFLOWS/APPROVAL-GATES.yaml]]

---

### 3. Procedural Logic — "How do we execute it?"

**Specifies the sequence and methods of action.**

- Operating procedures, workflows, sequences
- Dispatch rules, routing algorithms
- Tool selection and parameter passing

**Location:** [[13-WORKFLOWS/]], [[14-PROCESSES/]], [[17-DISPATCH/]]

---

### 4. Adaptive Logic — "What should we change based on results?"

**Enables continuous improvement.**

- Measurement and feedback loops
- Learning systems that update strategy
- Adaptation rules that modify behavior based on outcomes

**Location:** [[_EVAL/]], [[20-DECISIONS/ADAPTATION-RULES.yaml]]

---

## The Autonomous Loop

```
                  REAL WORLD
                      │
                      ▼
                   EVENTS
                      │
                      ▼
                    STATE
                      │
                      ▼
                KNOWLEDGE/GRAPH
                      │
                      ▼
                BUSINESS RULES
                      │
                      ▼
                DECISION LOGIC
                      │
                      ▼
               OPERATING LOGIC
                      │
                      ▼
                WORKFLOW LOGIC
                      │
                      ▼
                 AGENT LOGIC
                      │
                      ▼
                  TOOL LOGIC
                      │
                      ▼
                   ACTION
                      │
                      ▼
                  VERIFICATION
                      │
             ┌────────┴────────┐
             ▼                 ▼
          SUCCESS            FAILURE
             │                 │
             ▼                 ▼
          MEASURE            RECOVER
             │                 │
             └────────┬────────┘
                      ▼
                  EVALUATION
                      │
                      ▼
                   LEARNING
                      │
                      ▼
                   ADAPT
                      │
                      └──────► LOOP
```

This loop runs continuously at multiple autonomy levels:
- **L1 (Report)** → Agent proposes, human confirms
- **L2 (Assisted)** → Agent executes with human oversight  
- **L3 (Unattended)** → Agent operates autonomously post-verification

---

## 72 Logic Layers Organized by Domain

### PURPOSE DOMAIN (Logics 1–3)
- [[1. Identity Logic\|01-IDENTITY/README.md]] → CP-001
- [[2. Objective Logic\|00-CONSTITUTION/OBJECTIVES.md]] → CP-002
- [[3. Strategy Logic\|20-DECISIONS/STRATEGY-FRAMEWORK.md]] → CP-003

### BUSINESS DOMAIN (Logics 4–11)
- [[4. Business Logic\|_REGISTRIES/CANONICAL/BUSINESS_RULES.yaml]] → CP-004
- [[5. Economic Logic\|20-DECISIONS/ECONOMIC-MODEL.md]] → CP-005
- [[6. Revenue Logic\|30-REVENUE/REVENUE-LOOPS.md]] → CP-006
- [[7. Pricing Logic\|30-REVENUE/PRICING-STRATEGY.md]] → CP-007
- [[8. Customer Logic\|31-CUSTOMER/CUSTOMER-ONTOLOGY.md]] → CP-008
- [[9. Sales Logic\|32-SALES/SALES-PROCESS.md]] → CP-009
- [[10. Marketing Logic\|33-MARKETING/MARKETING-STRATEGY.md]] → CP-010
- [[11. Product Logic\|34-PRODUCT/PRODUCT-DEFINITION.md]] → CP-011

### OPERATIONS DOMAIN (Logics 12–14, 25–30)
- [[12. Operating Logic\|_REGISTRIES/CANONICAL/OPERATING_PROCEDURES.yaml]] → CP-012
- [[13. Workflow Logic\|13-WORKFLOWS/WORKFLOW-DEFINITIONS.yaml]] → CP-013
- [[14. Process Logic\|14-PROCESSES/PROCESS-LIBRARY.md]] → CP-014
- [[25. Scheduling Logic\|15-TIMING/SCHEDULE-ENGINE.md]] → CP-025
- [[26. Routing Logic (Ops)\|16-AGENTS/ROUTING-ENGINE.md]] → CP-026
- [[27. Dispatch Logic\|17-DISPATCH/DISPATCH-RULES.yaml]] → CP-027
- [[28. Inventory Logic\|18-INVENTORY/INVENTORY-STATE.md]] → CP-028
- [[29. Supply-Chain Logic\|19-ORCHESTRATION/SUPPLY-CHAIN.md]] → CP-029
- [[30. Human/HR Logic\|35-TEAM/HR-LIFECYCLE.md]] → CP-030

### DECISION & POLICY DOMAIN (Logics 15–20)
- [[15. Decision Logic\|20-DECISIONS/DECISION-FRAMEWORK.md]] → CP-015
- [[16. Policy Logic\|00-CONSTITUTION/POLICIES.md]] → CP-016
- [[17. Permission Logic\|_MCP/PERMISSIONS.yaml]] → CP-017
- [[18. Approval Logic\|13-WORKFLOWS/APPROVAL-GATES.yaml]] → CP-018
- [[19. Risk Logic\|20-DECISIONS/RISK-MATRIX.md]] → CP-019
- [[20. Compliance Logic\|36-LEGAL/COMPLIANCE-RULES.md]] → CP-020

### FINANCIAL DOMAIN (Logics 21–24)
- [[21. Financial Logic\|37-FINANCE/FINANCIAL-FLOWS.md]] → CP-021
- [[22. Accounting Logic\|37-FINANCE/ACCOUNTING-RULES.yaml]] → CP-022
- [[23. Capital Logic\|38-CAPITAL/ALLOCATION-STRATEGY.md]] → CP-023
- [[24. Resource Logic\|24-RESOURCES/RESOURCE-ALLOCATION.md]] → CP-024

### INTELLIGENCE DOMAIN (Logics 31–40)
- [[31. Agent Logic\|16-AGENTS/AGENT-DIRECTIVES.yaml]] → CP-031
- [[32. Prompt Logic\|_PROMPTS/PROMPT-LIBRARY.md]] → CP-032
- [[33. Context Logic\|_PIPELINES/CONTEXT-ASSEMBLY.md]] → CP-033
- [[34. Memory Logic\|_MEMORY/MEMORY-POLICY.yaml]] → CP-034
- [[35. Retrieval Logic\|_PIPELINES/RETRIEVAL-ENGINE.md]] → CP-035
- [[36. Tool Logic\|_MCP/TOOL-REGISTRY.yaml]] → CP-036
- [[37. Model Logic\|_REGISTRIES/CANONICAL/MODEL_REGISTRY.yaml]] → CP-037
- [[38. Routing Logic (AI)\|16-AGENTS/ROUTING-ENGINE.md]] → CP-038
- [[39. Orchestration Logic\|19-ORCHESTRATION/ORCHESTRATION-RULES.yaml]] → CP-039
- [[40. Loop Logic\|_PIPELINES/LOOP-PATTERNS.md]] → CP-040

### STATE & EVENT DOMAIN (Logics 41–45)
- [[41. Event Logic\|_PIPELINES/EVENT-HANDLERS.yaml]] → CP-041
- [[42. State Logic\|_MEMORY/STATE-MACHINE.yaml]] → CP-042
- [[43. Temporal Logic\|_REGISTRIES/CANONICAL/TEMPORAL-RULES.yaml]] → CP-043
- [[44. Dependency Logic\|_ONTOLOGY/DEPENDENCY-GRAPH.xml]] → CP-044
- [[45. Graph Logic\|_ONTOLOGY/KNOWLEDGE-GRAPH-SCHEMA.xml]] → CP-045

### DATA & VALIDATION DOMAIN (Logics 46–50)
- [[46. Data Logic\|_ONTOLOGY/DATA-SCHEMA.xml]] → CP-046
- [[47. Validation Logic\|_PIPELINES/VALIDATION-RULES.yaml]] → CP-047
- [[48. Verification Logic\|20-DECISIONS/VERIFICATION-FRAMEWORK.md]] → CP-048
- [[49. Evaluation Logic\|_EVAL/EVALUATION-RUBRICS.yaml]] → CP-049
- [[50. Quality Logic\|_REGISTRIES/CANONICAL/QUALITY-STANDARDS.yaml]] → CP-050

### EXCEPTION & RECOVERY DOMAIN (Logics 51–54)
- [[51. Exception Logic\|13-WORKFLOWS/EXCEPTION-HANDLING.yaml]] → CP-051
- [[52. Recovery Logic\|20-DECISIONS/RECOVERY-PROCEDURES.md]] → CP-052
- [[53. Fallback Logic\|_MCP/FALLBACK-ROUTES.yaml]] → CP-053
- [[54. Escalation Logic\|13-WORKFLOWS/ESCALATION-RULES.yaml]] → CP-054

### SECURITY & OBSERVABILITY DOMAIN (Logics 55–58)
- [[55. Security Logic\|_INFRASTRUCTURE/SECURITY-POLICY.yaml]] → CP-055
- [[56. Privacy Logic\|00-CONSTITUTION/PRIVACY-POLICY.md]] → CP-056
- [[57. Observability Logic\|_INFRASTRUCTURE/OBSERVABILITY-CONFIG.yaml]] → CP-057
- [[58. Audit Logic\|20-DECISIONS/AUDIT-FRAMEWORK.md]] → CP-058

### DEPLOYMENT & INFRASTRUCTURE DOMAIN (Logics 59–62)
- [[59. Deployment Logic\|_INFRASTRUCTURE/DEPLOYMENT-STRATEGY.md]] → CP-059
- [[60. Infrastructure Logic\|_INFRASTRUCTURE/INFRASTRUCTURE-CONFIG.yaml]] → CP-060
- [[61. Resource/Compute Logic\|_INFRASTRUCTURE/COMPUTE-ALLOCATION.yaml]] → CP-061
- [[62. Cost Logic\|37-FINANCE/COST-ACCOUNTING.md]] → CP-062

### LEARNING & ADAPTATION DOMAIN (Logics 63–65)
- [[63. Learning Logic\|_EVAL/LEARNING-SYSTEM.md]] → CP-063
- [[64. Adaptation Logic\|20-DECISIONS/ADAPTATION-RULES.yaml]] → CP-064
- [[65. Knowledge Logic\|_MEMORY/KNOWLEDGE-MANAGEMENT.md]] → CP-065

### ONTOLOGY & GOVERNANCE DOMAIN (Logics 66–68)
- [[66. Ontology Logic\|_ONTOLOGY/MASTER-ONTOLOGY.xml]] → CP-066
- [[67. Governance Logic\|00-CONSTITUTION/GOVERNANCE-FRAMEWORK.md]] → CP-067
- [[68. Lifecycle Logic\|_REGISTRIES/CANONICAL/LIFECYCLE-STAGES.yaml]] → CP-068

### PORTFOLIO & INVESTMENT DOMAIN (Logics 69–72)
- [[69. Portfolio Logic\|01-IDENTITY/PORTFOLIO-STRATEGY.md]] → CP-069
- [[70. Investment Logic\|38-CAPITAL/INVESTMENT-CRITERIA.md]] → CP-070
- [[71. Innovation Logic\|39-INNOVATION/INNOVATION-PIPELINE.md]] → CP-071
- [[72. Exit/Harvest Logic\|40-EXITS/EXIT-STRATEGY.md]] → CP-072

---

## Master Discovery Path

**Need to find a logic?**

1. **By question:** Search [[LOGIC_LAYERS_REGISTRY.yaml]] for core question
2. **By domain:** [[SECTOR_INDEX]] → find sector → find control plane
3. **By registry:** [[_REGISTRIES/CANONICAL/NAVIGATION_ALIASES.yaml]] → search topic
4. **By control plane:** [[_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml]] → CP-XXX
5. **By agent:** [[16-AGENTS/README.md]] → find agent → links to logics it governs

---

## How to Use This Framework

### For Architects
Map your system's behavior to the appropriate logic layers. Each layer is independently queryable and testable.

### For Agents
When executing decisions:
1. Check STATE (Logics 41–45)
2. Retrieve KNOWLEDGE (Logics 33, 34, 35)
3. Query BUSINESS RULES (Logics 4–20)
4. Execute PROCEDURE (Logics 12–14, 25–30)
5. Use TOOLS (Logic 36)
6. VERIFY result (Logic 48)
7. EVALUATE outcome (Logic 49)
8. LEARN for next cycle (Logics 63–64)

### For Governance
Each control plane (CP-001 through CP-072) is a **decision authority** and **oversight point**. Audits, policies, and permissions are tied to these layers.

---

## Key Properties

**Composable:** Each logic is independent; multiple logics can be combined for complex decisions.

**Queryable:** Every logic maps to registries, documents, or code that can be inspected.

**Auditable:** State changes, decisions, and actions trace back to specific logic layers.

**Testable:** Logic can be verified in isolation before deployment.

**Swappable:** Models, tools, and agents can be changed without rewriting logic.

---

## References

- Master Registry: [[_REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml]]
- Control Planes: [[_REGISTRIES/CANONICAL/CBP_REGISTRY.yaml]]
- Navigation: [[_REGISTRIES/CANONICAL/NAVIGATION_ALIASES.yaml]]
- Master Index: [[INDEX]]

