---
id: DOC-AGENT-FIRM-001
title: Agent Layer ↔ Firm Architecture Wiring
description: How ROLE → AGENT → COMPANY → FIRM → VENTURE ties together
updated: 2026-09-10
status: COMPLETE
---

# Agent Layer ↔ Firm Architecture Wiring

**The missing link:** How your 360-role catalog, agent runtime, company model, and 789 ventures all fit together.

---

## TL;DR: Five Layers, One System

```
WORLDWIDEBRO HOLDINGS (Strategic Layer)
    ↓ owns & governs
PRIVATE FIRM (Operating Entity)
    ↓ manages
COMPANY (Organizational Container)
    ↓ staffs
DEPARTMENT (Functional Cluster)
    ↓ organizes
ROLE (Numbered Seat R000–R359)
    ├── Occupied by: PERSON | AGENT | AUTOMATION
    └── Implements: CAPABILITY
        ├── Used by: VENTURE
        └── Serves: SECTOR (market/industry)
```

---

## How It Works: Four Concrete Examples

### **Example 1: OPS-001 Staffing Placement**

**The Structure:**
```
OPS-001 Venture (Staffing Placement)
  ├── Sector: SEC-017 (Logistics & Transportation)
  ├── Capability: CAP-047 (Sales Pipeline)
  └── Company: "OPS-001 Staffing"
        ├── Dept: Sales
        │   ├── ROLE #165 (SDR): AGENT (SDRAgent)
        │   └── ROLE #164 (AE): HUMAN [approval_required=true]
        ├── Dept: Operations
        │   └── ROLE #251: AGENT (OperationsAgent)
        └── Dept: Finance
            └── ROLE #221: AGENT (FinanceAgent)
```

**Workflow:**
- Task: "Find 50 staffing placements"
- R#165 (SDR Agent): Prospect research + qualification
- Handoff → R#164 (AE Human): Review, approve, sign contracts
- Handoff → R#251 (Ops Agent): Create assignments
- Handoff → R#221 (Finance Agent): Invoice draft

**Key Points:**
- R#165 (SDR) is AI-capable, approval_required=False
- R#164 (AE) is money-touching, approval_required=True
- R#221 (Controller) drafts only, humans sign

---

### **Example 2: LT-005 Medical Courier (Dispatch Loop)**

**Real-Time Dispatch:**
```
Event: Medical facility: "3 specimens to Lab A, STAT"
  ↓
AGENT R#327 (Logistics Manager)
  ├── NLP (CAP-017): Parse pickup/dropoff
  ├── Database (CAP-012): Route optimization
  ├── Execute: "Dispatch Driver-7 to Facility X (5 min ETA)"
  └── Monitor: GPS, accuracy
    ├── If on-time: Log success
    └── If delay: Escalate to HUMAN R#251
```

**Continuous Eval:**
```
Every 100 dispatches:
  ↓ AGENT R#348 (AI Eval)
  ├── Check: On-time rate ≥95%, cost <$5/dispatch
  ├── If pass: Continue unattended
  └── If fail: Escalate to HUMAN R#340 (AI Ops Director)
```

---

### **Example 3: CON-001 Construction (Idea→Ship)**

**Six-Step Workflow:**
```
CHIEF OF STAFF (R#4) routes to product
  ↓
R#141 (VP Marketing, HUMAN): Set launch goal
  ↓
R#152 (Product Marketing, AGENT): Write messaging
  ↓
R#24 (Product Manager, HUMAN): Write spec
  ↓
R#57 (Software Engineer, AGENT): Implement
  ↓
R#114 (SDET, AGENT): Verify correctness
  ↓
R#109 (Release Engineer, AGENT): Ship (canary→100%)
  ↓
R#348 (AI Eval, AGENT): Measure conversion
    ├── Target: >2% lead conversion
    ├── Pass: "Ready for volume"
    └── Fail: Escalate to R#141 (HUMAN)
```

**Approval Gates:**
- R#141 (VP Marketing): approval_required=False
- R#24 (PM): approval_required=False
- R#57 (Engineer): approval_required=False
- All others: Report results, humans make "go/no-go" calls

---

### **Example 4: FIN-037 Trading (Money Gate)**

**Critical Seats (All money-touching):**
```
AGENT R#83 (ML Engineer)
  ├── Predicts: EUR/USD → 1.1075 (65% confidence)
  ├── Recommends: Buy €10M (notional $11.05M)
  └── Exceeds threshold ($50K) → Requires approval
    ↓
AGENT R#342 (Automation Engineer)
  ├── Validates: Position limits, margin, counterparty risk
  ├── Creates: Trade order draft
  └── Routes to: HUMAN R#221 (Controller)
      ├── Approves → EXECUTE (fund transfer, settlement)
      └── Rejects → REVERT + log decision
    ↓
AGENT R#88 (AI Eval)
  ├── Post-execution metric: Prediction accuracy
  ├── Feeds back: Model calibration
  └── Quarterly review: Model drift detection
```

**Control Plane Override:**
- If predicted move > $1M notional: Requires CP-030 (Fintech) board approval
- If model confidence < 60% on 5 consecutive trades: Escalate to R#80 (Chief AI Officer)

---

## Neo4j Graph Integration

```cypher
(FIRM {id:"wwb"})
  -[:OWNS]-> (COMPANY {id:"OPS-001"})
    -[:HAS_DEPARTMENT]-> (DEPT {id:"dept-sales"})
      -[:HAS_ROLE]-> (ROLE {id:"R165"})
        -[:STAFFED_BY]-> (OCCUPANT)
          CASE OCCUPANT:
            ├── AGENT {id:"SDRAgent"} [ai_capable=true]
            ├── PERSON {id:"person-anissa"} [human=true]
            └── AUTOMATION {id:"zapier-task-67"}
        -[:IMPLEMENTS]-> (CAP {id:"CAP-047"})
          -[:USED_BY]-> (VENTURE {id:"OPS-001"})
            -[:SERVES]-> (SECTOR {id:"SEC-017"})

(ROLE {id:"R165"})
  -[:DOWNSTREAM]-> (ROLE {id:"R164"})
    -[:REQUIRES_APPROVAL]-> (ROLE {id:"R164"})
      ← means R#164 must review before execution
```

---

## 6 Tier-0 Ventures: Integration Status

| Venture | Primary Role | Occupant | Approval | Status |
|---------|-------------|----------|----------|--------|
| **OPS-001** | R#165 (SDR) | AGENT | No | ✅ Ready |
| **LT-005** | R#327 (Logistics) | AGENT | No | ✅ Ready |
| **CALLCENTER** | R#251 (Ops) | AGENT | No | ✅ Ready |
| **CON-001** | R#141 (VP Mkt) | HUMAN | No | 🟡 6h API build |
| **RE-001** | R#24 (PM) | HUMAN | No | 🟡 25h engine build |
| **LT-011** | R#251 (Ops) | TBD | No | 🔴 1h assessment |

---

## Control Planes Map

**Each venture region governed by a control plane:**

| CP | Governs | Budget | Revenue Target | Approval Authority |
|----|---------|--------|-----------------|-------------------|
| **CP-017** | LT sector (Logistics) | $2.5M/Q | $500K/Q | <$10K: Agent; $10K–$100K: VP Sales; >$100K: Committee |
| **CP-021** | Revenue (Sales) | $5M/Q | $2M/Q | <$50K: AE; >$50K: CRO approval |
| **CP-030** | Fintech | $1.5M/Q | $300K/Q | <$50K: Controller; >$50K: CFO approval |

---

## How Approval Gates Work

**Three money-touching seats (always require human):**

```python
APPROVAL_REQUIRED_ROLES = {
    164,   # Account Executive (closes deals >$10K)
    221,   # Controller (accounting entries >$10K)
    317,   # M&A Analyst (acquisitions >$500K)
}

# Runtime enforcement:
class Runtime:
    def dispatch(self, task: Task, role_number: int) -> AgentResult:
        agent = self.agent_for(role_number)
        result = agent.run(task)
        
        if self.role.approval_required:
            result.requires_approval = True
            return result.finish()  # Not executed yet
        return result  # Executed
```

**Human review queue:**

```
Agent R#164 drafts: "Contract with Northwind, $42K"
  ├── Returns: requires_approval=True
  └── System queues for: HUMAN R#164 (Account Executive)
      ├── Reviews: Contract terms, pricing, terms
      ├── If OK: Approves → Contract signed, revenue booked
      └── If no: Rejects → Agent retries with feedback
```

---

## Summary: The Complete System

**Five-layer hierarchy:**

1. **WORLDWIDEBRO HOLDINGS** → Principal/family office
2. **PRIVATE FIRM** → Operating entity (governs all portfolio)
3. **COMPANY** (e.g., "OPS-001 Staffing") → Container for one or more ventures
4. **DEPARTMENT** (e.g., "Sales") → Functional cluster
5. **ROLE** (e.g., R#165 SDR) → Numbered seat
   - Occupied by: PERSON | AGENT | AUTOMATION
   - Implements: CAPABILITY
   - Used by: VENTURE
   - Serves: SECTOR

**Data sources (the truth):**

- **Neo4j**: All relationships (IMPLEMENTS, STAFFED_BY, REQUIRES, etc.)
- **Supabase**: Live transactional state (who's deployed, current KPIs)
- **MASTER-ROLE-REGISTRY.md**: Static authority (seat definitions)
- **Ventures table**: Which ventures are active, their sector, revenue

**Governance:**

- **Control Planes**: Budget, approval thresholds, KPI targets, escalation paths
- **Approval Gates**: Money-touching seats require human sign-off
- **Continuous Eval**: AI Evaluation Agent (#348) measures every deployed agent weekly

The agent layer **executes** your firm structure. It's not separate from it—it's the operational manifestation of it.

---

**Generated:** 2026-09-10  
**Related:** _AGENTS/agent_layer.py, 01-IDENTITY/MASTER-ROLE-REGISTRY.md, STARTHERE.md
