# Graph Layers 6-11 Integration Architecture

**Authority → State → Lifecycle → Event → Evidence → Decision**

This document shows how the six operational layers orchestrate together to create a complete system for understanding what happened, who authorized it, how we know it, and what we should do next.

---

## The Six Layers (Operational Chain)

### Layer 6: Authority Graph
**Question:** "Who/what can act?"

- Defines [[AUTHORITY-*]] roles and permissions
- Gates what state transitions are allowed
- Approves decisions and financial actions
- Establishes delegation chains

### Layer 7: State Graph
**Question:** "What condition is it in RIGHT NOW?"

- Tracks current [[STATE-*]] for every entity
- Connects to valid [[TRANSITION-*]] paths
- Enforces state machine constraints
- Enables state-based queries

### Layer 8: Lifecycle Graph
**Question:** "How much longer can it stay here? What comes next?"

- Defines [[STAGE-*]] progression journey
- Sets duration budgets and deadlines
- Establishes [[MILESTONE-*]] requirements
- Gates stage transitions with [[GATE-*]] decisions

### Layer 10: Event Graph
**Question:** "What actually happened? When? To whom? By whom?"

- **IMMUTABLE** audit trail of every occurrence
- Records [[EVENT-StateChanged]], [[EVENT-PaymentReceived]], [[EVENT-DecisionApproved]], etc.
- Every state change generates an event
- Events are append-only, never modified or deleted

### Layer 11: Evidence Graph
**Question:** "How do we KNOW what we claim?" (Operationalizes ANTIGRAVITY Rule 31)

- Backs [[CLAIM-*]] with [[EVIDENCE-*]]
- Tracks [[VERIFICATION-*]] by appropriate authorities
- Flags [[CONTRADICTION-*]] that must be resolved
- Enforces: **No claim without evidence = UNVERIFIED**

### Layer 14: Decision Graph
**Question:** "What choice was made? By whom? Based on what? With what outcome?"

- Documents every [[DECISION-*]] with options analyzed
- Records [[APPROVAL-*]] chain
- Tracks [[OUTCOME-*]] against expectations
- Captures learnings for future decisions

---

## How They Wire Together

### Path 1: State Transition Triggers Event

```
[[Authority-CEO]] has authority to change venture from [[STATE-Building]] to [[STATE-Selling]]
         ↓
Transition is valid in [[State-Machine-Venture]]
         ↓
CEO exercises authority → decision approved via [[GATE-Building-to-Selling]]
         ↓
[[EVENT-StateChanged]] is recorded (immutable)
         ↓
[[EVIDENCE-GateApprovalRecord]] backs the claim "venture moved to Selling"
         ↓
[[Outcome]] is measured when venture actually changes state
```

### Path 2: Decision Drives State Change

```
[[DECISION-OPS001-Scale]] is proposed with [[OPTION-Aggressive-Scaling]] and [[OPTION-Pause-Evaluate]]
         ↓
[[DECISION-MATRIX-*]] evaluates options against [[CRITERIA-*]] using [[EVIDENCE-*]]
         ↓
[[AUTHORITY-CEO]] CHOOSES [[OPTION-Aggressive-Scaling]]
         ↓
[[APPROVAL-RECORD-*]] documents authorization
         ↓
Decision execution begins
         ↓
[[EVENT-DecisionExecuted]] recorded
         ↓
Venture state changes from [[STATE-Generating-Revenue]] to [[STATE-Scaling]] (autorized by [[AUTHORITY-CEO]])
         ↓
[[OUTCOME-OPS001-Scale-Success]] measured: "MoM growth 25%, target achieved"
         ↓
Positive [[OUTCOME]] adds confidence for future similar decisions
```

### Path 3: Lifecycle Milestones Generate Events

```
Venture in [[STAGE-Validation]] with [[MILESTONE-LT005-FirstCustomer]] required
         ↓
Customer acquired (observable [[EVENT-CustomerAcquired]])
         ↓
Milestone marked as [[ACHIEVED]] via [[VERIFICATION-TeamLead]]
         ↓
[[EVENT-MilestoneAchieved]] recorded with [[EVIDENCE-CustomerRecord]]
         ↓
Progress toward [[GATE-Validation-to-Building]] unlocked
         ↓
When all milestones complete, [[DECISION-LT005-Gate-Validation-to-Building]] can proceed
```

### Path 4: Evidence Backs Decisions

```
[[CLAIM-LT005-Generating-$1800-Revenue]] requires evidence
         ↓
[[EVIDENCE-BankStatement]] shows $1,800 deposit
[[EVIDENCE-Invoice]] shows $1,800 charged
[[EVIDENCE-CustomerDatabase]] shows active subscription
         ↓
No [[CONTRADICTION-*]] exists
         ↓
[[VERIFICATION-CFO]] confirms all evidence
         ↓
Status: [[CLAIM-VERIFIED]] with 85-95% confidence
         ↓
[[DECISION-Venture-Status-Generating-Revenue]] can be made with confidence
         ↓
Venture [[STATE-*]] updated to [[STATE-Generating-Revenue]] (authorized by [[AUTHORITY-CEO]])
```

---

## Critical Invariants

### Invariant 1: Authority Precedes State Change
```
NO state change is allowed without:
  ✓ [[AUTHORITY-*]] that permits this transition
  ✓ [[APPROVAL-*]] from that authority
  ✓ [[EVENT-*]] recording the change
  ✓ [[EVIDENCE-*]] supporting the state (via Decision or other claim)
```

### Invariant 2: Evidence Precedes Claim Status
```
NO [[CLAIM-*]] can have status:
  ✓ VERIFIED — without at least one [[EVIDENCE-*]]
  ✓ DISPUTES — without explicit [[CONTRADICTION-*]]
  ✓ ACCEPTED — without [[VERIFICATION-*]] from appropriate [[AUTHORITY-*]]
```

### Invariant 3: Events are Immutable
```
Once [[EVENT-*]] created:
  ✗ Cannot be deleted
  ✗ Cannot be modified
  ✗ Cannot have timestamp changed
  ✓ Can be supplemented with explanatory [[EVIDENCE-*]]
  ✓ Can be disputed with [[CONTRADICTION-*]]
```

### Invariant 4: Lifecycle Progression is Ordered
```
Entity progresses through [[STAGE-*]] in order:
  Stage(N) → [[MILESTONE-*]] required → [[GATE-*]] decision → Stage(N+1)
  
  Cannot skip stages (unless explicitly permitted via [[can_skip: true]])
  Cannot exceed stage [[max_duration_days]] without escalation
```

### Invariant 5: Decisions Require Options & Criteria
```
[[DECISION-*]] cannot be made without:
  ✓ At least 2 [[OPTION-*]]
  ✓ Evaluation against all [[CRITERIA-*]]
  ✓ [[EVIDENCE-*]] supporting scores
  ✓ Recommendation based on weighted scores
  ✓ Approval from [[AUTHORITY-*]]
```

---

## Query Patterns Across Layers

### "Why is this venture in [[STATE-Dormant]]?"
```
START: Venture in [[STATE-Dormant]]
  → Find latest [[EVENT-StateChanged]] to [[STATE-Dormant]]
  → Event was triggered by [[DECISION-Pause]] or [[EVENT-Manual-Transition]]
  → If by decision, find [[DECISION-*]] and its rationale
  → Find [[APPROVAL-*]] that authorized it
  → Find [[OUTCOME-*]] if decision was made
  → Link to [[LIFECYCLE-*]] stage and [[MILESTONE-*]] status
RESULT: Complete audit trail of why and how venture entered Dormant state
```

### "Can we approve $50K spend for [[VENTURE-CON001]]?"
```
START: $50K capital request
  → Query [[AUTHORITY-CFO]]: "Do you have authority for $50K?"
  → Yes: [[AUTHORITY-CFO]] can approve < $250K
  → Lookup [[APPROVAL_CHAIN-CapitalRequest]]: requires [[AUTHORITY-VPOps]] + [[AUTHORITY-CFO]]
  → Collect [[EVIDENCE-*]] for business case (market size, unit economics, etc.)
  → No [[CONTRADICTION-*]] between evidence sources
  → Build [[DECISION-MATRIX-*]] with options and criteria
  → Obtain [[APPROVAL-RECORD-*]] from each required authority
  → Record [[EVENT-ApprovalGranted]]
  → Generate [[OUTCOME-*]] tracking: "Spend approved, delivered on time?"
RESULT: Fully auditable approval trail with full evidence chain
```

### "Which decisions led to [[STATE-Generating-Revenue]]?"
```
START: Venture in [[STATE-Generating-Revenue]]
  → Find all [[EVENT-StateChanged]] to this state
  → Trace back to [[DECISION-*]] that triggered state change
  → For each decision:
    - What [[OPTION-*]] was chosen?
    - What [[CRITERIA-*]] drove the choice?
    - What [[EVIDENCE-*]] supported it?
    - What was the [[OUTCOME-*]]?
  → Build full decision causality graph
RESULT: Complete causality trace from decisions to current state
```

### "What evidence supports our [[CLAIM-Revenue-Accuracy]]?"
```
START: Revenue claim for [[VENTURE-LT005]]: "$1,800/month"
  → Find all [[EVIDENCE-*]] types:
    - [[EVIDENCE-BankStatement]]: $1,800 deposits ✓
    - [[EVIDENCE-Invoice]]: $1,800 line items ✓
    - [[EVIDENCE-CustomerDatabase]]: active subscriptions ✓
  → Check for [[CONTRADICTION-*]]:
    - Bank says $1,800 ✓
    - CRM says $2,000 ✗ (CONTRADICTION!)
  → Find [[VERIFICATION-*]] explaining discrepancy
  → Mark [[CLAIM-*]] as VERIFIED (for bank) or DISPUTED (for CRM)
  → Recommend investigation: "Why CRM ≠ Bank?"
RESULT: Confidence score 60-85% (moderate) due to unresolved contradiction
```

---

## Authority Flows

### Approval Flow for Major Decision
```
[[DECISION-Proposed]] by [[PERSON-VPOps]]
         ↓
[[AUTHORITY-VPOps]] has authority < $50K ✓
         ↓
Request escalates to [[AUTHORITY-CEO]]: needs $50K approval
         ↓
[[AUTHORITY-CEO]] reviews [[EVIDENCE-*]], [[DECISION-MATRIX-*]]
         ↓
[[AUTHORITY-CEO]] delegates to [[AUTHORITY-CFO]] (via [[DELEGATION-CEO-to-CFO-Financial]])
         ↓
[[AUTHORITY-CFO]] approves ✓
         ↓
[[APPROVAL-RECORD-*]] created with digital signature
         ↓
[[EVENT-ApprovalGranted]] recorded (immutable)
         ↓
[[DECISION-*]] status → APPROVED
         ↓
Authorized to execute
```

### Escalation When Authority Insufficient
```
[[PERSON-VentureManager]] wants to spend $100K
         ↓
Query [[AUTHORITY-VentureManager]]: max $5K ✗
         ↓
Escalate to [[AUTHORITY-OperationsDirector]]: max $50K ✗
         ↓
Escalate to [[AUTHORITY-VPOps]]: max $50K ✗
         ↓
Escalate to [[AUTHORITY-CFO]]: max $100K ✓
         ↓
[[APPROVAL-CHAIN-CapitalRequest-$100K]]: requires [[AUTHORITY-CFO]] + [[AUTHORITY-CEO]]
         ↓
Both approvals obtained
         ↓
Decision executable
```

---

## The Complete Loop (Virtuous Cycle)

```
1. PROBLEM IDENTIFIED
   ↓
2. DECISION PROPOSED
   (Define options, build criteria)
   ↓
3. EVIDENCE GATHERED
   (Bank statements, customer records, audits)
   ↓
4. CONTRADICTIONS RESOLVED
   (Reconcile conflicting sources)
   ↓
5. DECISION MATRIX BUILT
   (Score options against criteria)
   ↓
6. RECOMMENDATION MADE
   ↓
7. APPROVAL OBTAINED
   (From appropriate [[AUTHORITY-*]])
   ↓
8. DECISION EXECUTED
   (State change, resource allocation, etc.)
   ↓
9. EVENT RECORDED
   (Immutable audit trail)
   ↓
10. OUTCOME MEASURED
    (Did we achieve the goal?)
    ↓
11. LEARNING CAPTURED
    (What should change next time?)
    ↓
12. POLICY UPDATED
    (Future decisions informed by outcome)
    ↓
[Loop back to 1]
```

---

## Neo4j Wiring (Implementation Guide)

All six layers will be modeled in Neo4j as:

### Nodes
```
(:Authority {id, name, level, scope})
(:State {id, name, entity_type})
(:Stage {id, lifecycle, name, duration_days})
(:Event {id, event_type, timestamp, entity_id, status})
(:Evidence {id, type, source, grading, expires_at})
(:Decision {id, title, status, chosen_option})
```

### Relationships
```
(Authority)-[:AUTHORIZES]->(StateTransition)
(StateTransition)-[:TRIGGERS]->(Event)
(Event)-[:EVIDENCED_BY]->(Evidence)
(Evidence)-[:BACKS]->(Claim)
(Claim)-[:INFORMS]->(Decision)
(Decision)-[:RESULTED_IN]->(Outcome)
(Outcome)-[:TEACHES]->(Learning)
```

### Queries
```cypher
// Complete audit trail for one venture
MATCH (v:Venture {id: "LT005"})
      -[:HAS_EVENT]->(e:Event)
      -[:EVIDENCED_BY]->(ev:Evidence)
RETURN v, e, ev ORDER BY e.timestamp

// What decisions led to current state?
MATCH (v:Venture {id: "LT005"})
      -[:HAS_STATE]->(s:State)
      <-[:RESULTS_IN]-(d:Decision)
RETURN d, d.chosen_option, d.rationale

// Authority hierarchy for approval
MATCH (a:Authority)-[:DELEGATES]->(b:Authority)
RETURN a.name, b.name ORDER BY a.level, b.level
```

---

## Status

✅ All 6 layers defined with complete entity/relationship/constraint specs  
✅ Integration points documented  
✅ Critical invariants specified  
✅ Query patterns for cross-layer navigation  
✅ Authority flows for approval chains  
✅ Neo4j wiring architecture ready  

🚧 Next: Populate with real Company Brain data (ventures, decisions, evidence)  
🚧 Then: Build Learning Graph (layer 16) and Intent Graph (layer 15)  
🚧 Finally: Wire layers 12-13 (Resources, Risk) and remaining layers  

