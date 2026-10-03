---
type: execution-control-ontology
canonical: true
authority: task-state-engine
updated_at: 2026-10-02T20:00:00Z
source_of_truth: true
---

# TASK_EXECUTION_MASTER_ONTOLOGY — Work Execution Control Plane

**Complete lifecycle governance for work: from discovery → assignment → execution → handoff → rotation → verification → completion → learning → update.**

This is the execution-control layer that prevents fake completion and ensures every task's actual state is continuously reconstructed, not merely declared.

---

## [[TASK_EXECUTION]] — Master Hierarchy

```
[[TASK_EXECUTION]]
│
├── [[WORK]]
│   ├── [[OBJECTIVE]]      — Strategic intent
│   ├── [[OUTCOME]]        — Measurable result
│   ├── [[REQUIREMENT]]    — What must be satisfied
│   ├── [[INITIATIVE]]     — Multi-quarter program
│   ├── [[PROJECT]]        — Scoped work package
│   ├── [[EPIC]]           — Feature-level grouping
│   ├── [[TASK]]           — Discrete unit of work
│   ├── [[SUBTASK]]        — Task decomposition
│   └── [[ACTION]]         — Atomic operation
│
├── [[TASK_STATE]]         — 23 possible states
├── [[UNCOMPLETED_WORK]]   — 10 failure modes
├── [[TASK_DEFINITION]]    — Contract for what/why/how
├── [[OWNERSHIP]]          — 8 roles (owner, assignee, executor, reviewer, approver, backup, escalation, accountable)
├── [[AGENT_WORK]]         — Agent type assignment
├── [[DELEGATION]]         — Claim/accept/reject/reassign
├── [[HANDOFF]]            — Full state transfer (not just a title)
├── [[ROTATION]]           — Policy-driven reassignment
├── [[EXECUTION]]          — Plan → Action → Checkpoint → Error → Recovery
├── [[DEPENDENCIES]]       — BLOCKS, BLOCKED_BY, REQUIRES, ENABLES
├── [[PROGRESS]]           — %, stage, checkpoints, milestones
├── [[VERIFICATION]]       — Self-check → Peer → Test → Evidence
├── [[COMPLETION]]         — DONE, PARTIAL, VERIFIED, DEPLOYED, CLOSED
├── [[UPDATING]]           — Cascading updates to related systems
├── [[FEEDBACK]]           — Learning loop (result → lesson → improvement)
└── [[AUDIT]]              — Immutable history (created, updated, state, assignment, handoff, rotation)
```

---

## [[TASK_STATE]] — 23 Canonical States

```
[[IDEA]]                  — Concept, not yet formalized
     ↓
[[CAPTURED]]              — Documented in system
     ↓
[[BACKLOG]]               — Waiting prioritization
     ↓
[[READY]]                 — Meets DoD, can be assigned
     ↓
[[ASSIGNED]]              — Owner designated
     ↓
[[CLAIMED]]               — Executor accepts responsibility
     ↓
[[IN_PROGRESS]]           — Active work
     │
     ├─→ [[WAITING]]      — Blocked on external event
     ├─→ [[BLOCKED]]      — Cannot proceed (action required)
     ├─→ [[PAUSED]]       — Intentionally suspended
     ├─→ [[HANDOFF_PENDING]]  — Ready to hand to new owner
     └─→ [[ROTATION_PENDING]] — Time to rotate workers
     │
[[REVIEW]]                — Work submitted for peer/manager review
     ↓
[[VERIFICATION]]          — Testing/evidence collection
     │
     ├─→ [[PASS]]         — All criteria met
     └─→ [[FAIL]]         — Return to IN_PROGRESS
     │
[[COMPLETED]]             — Work physically done (not verified)
     ↓
[[VERIFIED]]              — Evidence confirms done, acceptance criteria satisfied
     ↓
[[DEPLOYED]]              — Live/shipped/in production
     ↓
[[CLOSED]]                — Task fully resolved, audit trail preserved

[[FAILED]]                — Attempt did not produce required result
     ↓
[[REOPENED]]              — Re-attempted after analysis

[[CANCELLED]]             — Work no longer needed
[[DEFERRED]]              — Intentionally postponed
[[ARCHIVED]]              — Completed but kept for reference
```

---

## [[UNCOMPLETED_WORK]] — 10 Failure Modes

Every unfinished task falls into exactly one category:

```
[[INCOMPLETE]]
└── No execution has started or is in progress

[[PARTIAL]]
└── Some acceptance criteria satisfied; remainder needed

[[BLOCKED]]
└── Cannot proceed; external blocker or missing capability

[[WAITING]]
└── Work halted; awaiting external event/person/decision

[[STALE]]
└── Requirements or context may no longer be current

[[OVERDUE]]
└── Deadline passed; clock expired

[[FAILED]]
└── Execution attempt did not produce required result

[[ABANDONED]]
└── Execution stopped without formal closure or rework

[[UNASSIGNED]]
└── No accountable executor designated

[[UNVERIFIED]]
└── Claimed complete but evidence is missing or insufficient
```

---

## [[TASK_STATE]] ≠ [[TASK_TRUTH]]

**This is the critical rule.**

A task can declare:
```yaml
status: completed
```

While the system observes:
```yaml
verification: failed
evidence: missing
actual_state: unverified
```

Therefore, every task maintains **three parallel states:**

```
[[DECLARED_STATE]]   — What the task claims (status field)
        +
[[OBSERVED_STATE]]   — What the system detects (metrics, logs, tests)
        +
[[VERIFIED_STATE]]   — What humans/tests confirm (evidence, approval)
        =
[[ACTUAL_TASK_STATE]] — Ground truth (no fakes)
```

---

## [[TASK_DEFINITION]] — Contract for Work

Every task must answer:

```
[[TASK_ID]]               — Unique identifier (TASK-000001)
[[TITLE]]                 — Human-readable name
[[DESCRIPTION]]           — What needs to be done
[[WHY]]                   — Strategic context/reason
[[OBJECTIVE]]             — What we're trying to achieve
[[EXPECTED_OUTCOME]]      — Measurable result
[[ACCEPTANCE_CRITERIA]]   — How we know it's done (7-point scale)
[[DEFINITION_OF_DONE]]    — Quality bar (tests pass, docs updated, etc.)
[[PRIORITY]]              — P0/P1/P2/P3 (business priority)
[[URGENCY]]               — Hours/days/weeks (time sensitivity)
[[IMPACT]]                — Revenue, risk, UX, technical debt
[[EFFORT]]                — Hours estimated
[[RISK]]                  — Known risks/failure modes
[[DEADLINE]]              — Hard cutoff or target date
[[CONSTRAINTS]]           — Limitations on approach
[[DEPENDENCIES]]          — What this task requires
[[OWNER]]                 — Accountable party
[[APPROVAL_GATE]]         — Who must verify completion
```

---

## [[OWNERSHIP]] — 8 Roles

```
[[OWNER]]                 — Accountable for completion (makes final call)
[[ASSIGNEE]]              — Primary executor (may delegate further)
[[EXECUTOR]]              — Doing the work (may rotate)
[[REVIEWER]]              — Reviews work quality/correctness
[[APPROVER]]              — Business/technical approval gate
[[BACKUP]]                — Ready to take over if primary blocked
[[ESCALATION_OWNER]]      — Resolves blockers/conflicts
[[ACCOUNTABLE_PARTY]]     — Final authority if responsibility unclear
```

**Rule: Every task must have at least [[OWNER]] and [[EXECUTOR]]. They can be the same person.**

---

## [[DELEGATION]] — Workflow States

```
[[ASSIGN]]        → [[ASSIGNED]]
     ↓
[[CLAIM]]         → [[CLAIMED]]
     ↓
[[ACCEPT]]        → [[IN_PROGRESS]]

or

[[REJECT]]        → [[REASSIGN]]
                → [[ASSIGN]] (to next person)

[[REASSIGN]]      → Task moves to new executor
[[ESCALATE]]      → Problem moves to higher authority
[[DECOMPOSE]]     → Task split into subtasks
[[PARALLELIZE]]   → Multiple tasks start simultaneously
```

---

## [[HANDOFF]] — Full State Transfer (Not Just a Title)

Handoff is when work moves from one executor to another **with complete state**.

**Sending worker prepares:**

```
[[HANDOFF_PACKAGE]]
│
├── [[OBJECTIVE]]              — What we're solving
├── [[CURRENT_STATE]]          — System state at handoff moment
├── [[WORK_COMPLETED]]         — What's done (commits, files, data)
├── [[WORK_REMAINING]]         — What's not done
├── [[FILES_CHANGED]]          — Git diffs (or file listing)
├── [[COMMITS]]                — Commit hashes for reference
├── [[DATA]]                   — Input/output/state changes
├── [[DECISIONS]]              — Key architectural choices made
├── [[ASSUMPTIONS]]            — What we're assuming is true
├── [[BLOCKERS]]               — Problems we hit and workarounds
├── [[DEPENDENCIES]]           — What this depends on
├── [[TEST_RESULTS]]           — What passed/failed locally
├── [[EVIDENCE]]               — Screenshots, logs, proofs
├── [[RISKS]]                  — What could go wrong
├── [[NEXT_ACTION]]            — Exact next step for new worker
└── [[CONTEXT]]                — Mental model / reasoning
```

**Receiving worker confirms:**

```
[[HANDOFF_UNDERSTOOD]]    → YES / NO

If NO:
[[CLARIFICATION_NEEDED]]  → Questions for sending worker
[[RESEND_HANDOFF]]        → New handoff package with answers

If YES:
[[HANDOFF_ACCEPTED]]
        ↓
[[CONTINUATION]]
        ↓
[[NEW_WORKER_EXECUTION]]
```

**Golden rule:** You should not get "Here is the task. Good luck." You should get **"Here is the exact system state required to continue without reconstructing the previous worker's context."**

---

## [[ROTATION]] — Systematic Reassignment

Rotation is different from handoff. **Rotation is policy-driven; handoff is event-driven.**

Rotation triggers:

```
[[ROTATION_TRIGGER]]
│
├── [[TIME_LIMIT]]             — Max 3 hours on a task
├── [[CAPACITY_LIMIT]]         — Worker at max parallel tasks
├── [[AGENT_LIMIT]]            — Agent has bandwidth limit (Haiku vs Sonnet)
├── [[SPECIALIST_REQUIRED]]    — Need different skill (code → review)
├── [[FAILURE]]                — Approach not working; try new executor
├── [[PRIORITY_CHANGE]]        — Task priority changed; reassign accordingly
├── [[DEPENDENCY]]             — Blocker resolved; rotate to ready
└── [[SCHEDULE]]               — Time-based rotation policy
```

Rotation process:

```
[[ACTIVE_WORK]]
      ↓
[[ROTATION_TRIGGERED]]
      ↓
[[ROTATION_ENGINE]]
      ├── [[FIND_CANDIDATE]]      — Who's available?
      ├── [[SKILL_MATCH]]         — Right skills?
      ├── [[CAPACITY_CHECK]]      — Have bandwidth?
      ├── [[AUTHORITY_CHECK]]     — Authority to do this work?
      └── [[CONTEXT_TRANSFER]]    — State handed off
             ↓
       [[ROTATION_EXECUTE]]
             ↓
       [[NEW_WORKER]]
             ↓
       [[CONTINUATION]]
```

---

## [[EXECUTION]] — The Work Loop

```
[[START]]
   ↓
[[PLAN]]              — Decompose task into subtasks
   ↓
[[DECOMPOSITION]]     — Map to actions, tools, dependencies
   ↓
[[ACTION]]            — Do the work
   ↓
[[TOOL_USE]]          — Invoke capabilities, agents, APIs
   ↓
[[PROGRESS]]          — Track % complete, stage, checkpoints
   ├─→ [[CHECKPOINT]] — Intermediate validation
   ├─→ [[ERROR]]      — Something failed
   │    ├─→ [[RECOVERY]]   → Retry, workaround, escalate
   │    └─→ [[ESCALATION]] → Move to higher authority
   └─→ [[CONTINUE]]   → Keep going
   ↓
[[STOP]]              — Halt (completed, blocked, or cancelled)
```

---

## [[DEPENDENCIES]] — Relationship Map

```
[[BLOCKS]]            — This task blocks another
[[BLOCKED_BY]]        — This task is blocked by another
[[REQUIRES]]          — This task needs another to complete first
[[ENABLES]]           — This task enables another to start
[[PREDECESSOR]]       — Must happen before this
[[SUCCESSOR]]         — Must happen after this
[[EXTERNAL_DEPENDENCY]]  — Depends on external system/person
[[HUMAN_DEPENDENCY]]     — Depends on human decision/action
```

**Never execute a task without first resolving all [[BLOCKED_BY]] dependencies.**

---

## [[VERIFICATION]] — Reality Check

**Verification is not optional. Verification prevents fake completion.**

```
[[COMPLETION_CLAIM]]
       ↓
[[SELF_CHECK]]        — Executor: "Does this meet acceptance criteria?"
       │
       ├─→ [[PASS]]   → Continue
       └─→ [[FAIL]]   → Back to work
       ↓
[[PEER_REVIEW]]       — Another human: "Is this correct?"
       │
       ├─→ [[APPROVED]]   → Continue
       └─→ [[REJECTED]]   → Back to work
       ↓
[[TEST]]              — Automated tests run
       │
       ├─→ [[PASS]]   → Continue
       └─→ [[FAIL]]   → Back to work
       ↓
[[EVIDENCE]]          — Gather proof (logs, screenshots, data)
       │
       ├─→ [[SUFFICIENT]] → Continue
       └─→ [[MISSING]]    → Back to work
       ↓
[[ACCEPTANCE_CRITERIA_CHECK]]
       │
       ├─→ [100% MET]   → VERIFIED
       ├─→ [[PARTIAL]]    → Back to work
       └─→ [[NOT_MET]]    → Back to work
       ↓
[[VERIFIED]] = [[COMPLETED]] + [[EVIDENCE]] + [[APPROVAL]]
```

---

## [[COMPLETION]] — Four States, Not One

```
[[DONE]]              — Executor says it's done (not verified)
[[PARTIAL]]           — Some criteria met; remainder needed
[[VERIFIED]]          — Independent confirmation: evidence + test + approval
[[DEPLOYED]]          — Live/shipped/in production
[[CLOSED]]            — Task + audit trail archived; work resolved
```

**A task is NOT complete until [[VERIFIED]]. [[DONE]] ≠ [[VERIFIED]].**

---

## [[UPDATING]] — Cascading Changes

When a task changes, what else must be updated?

```
[[EVENT]]
   ↓
[[CHANGE_DETECTED]]
   ├── Task state changes
   ├── Owner/executor changes
   ├── Deadline changes
   ├── Dependency resolves
   └── Blocker identified
       ↓
[[IMPACT_ANALYSIS]]
   ├── Which other tasks are affected?
   ├── Which registries need updating?
   ├── Which documents are now stale?
   └── Which workflows need re-routing?
       ↓
[[UPDATE_REQUIRED]]
   │
   ├── [[TASK]]                → State/owner/deadline update
   ├── [[WHERE_WE_ARE]]        → Current status changes
   ├── [[CODEBASE]]            → Code/commit changes
   ├── [[INFRASTRUCTURE]]      → System state changes
   ├── [[DATA_FLOW]]           → Data/process changes
   ├── [[KNOWLEDGE_GRAPH]]     → Entity/relationship updates
   ├── [[REGISTRIES]]          → Capability/venture/sector updates
   └── [[SOURCE_OF_TRUTH]]     → Cascade verification
           ↓
       [[UPDATE]]
           ↓
       [[VALIDATION]]
           ↓
       [[AUDIT]]
           ↓
   [[NEW_SYSTEM_STATE]]
```

---

## [[FEEDBACK]] — Learning Loop

Every completed task produces learning:

```
[[OUTCOME]]           — What resulted?
       ↓
[[LESSON]]            — What did we learn?
       ├── [[POSITIVE]] — What went well?
       ├── [[NEGATIVE]] — What could improve?
       └── [[NEUTRAL]]  — What was new information?
       ↓
[[ERROR_PATTERN]]     — Did we hit a known problem?
[[BOTTLENECK]]        — Did execution stall somewhere?
[[CAPABILITY_GAP]]    — Did we lack a capability?
[[PROCESS_IMPROVEMENT]]  — How could the process be better?
[[AUTOMATION_OPPORTUNITY]]  — What could be automated?
       ↓
[[KNOWLEDGE_UPDATE]]
       ├── [[KNOWLEDGE_GRAPH]] — Add new relationship/fact
       ├── [[WHERE_WE_ARE]]    — Update capability inventory
       └── [[REGISTRIES]]      — Update capability registry
       ↓
[[NEXT_TASK_IMPROVED]] — Better planning, estimation, execution
```

---

## [[AUDIT]] — Immutable History

Every task maintains a complete audit trail:

```
[[CREATED_AT]]        — Timestamp (never changes)
[[CREATED_BY]]        — Creator (never changes)
[[UPDATED_AT]]        — Last modification
[[UPDATED_BY]]        — Last modifier

[[STATE_HISTORY]]
   └── {state: IDEA → CAPTURED → READY → ASSIGNED → IN_PROGRESS → VERIFIED → CLOSED}
       {timestamp, actor, reason}

[[ASSIGNMENT_HISTORY]]
   └── {assigned_to: Owner1 → Owner2 → Owner3}
       {timestamp, actor, reason}

[[HANDOFF_HISTORY]]
   └── {from: Worker1, to: Worker2, timestamp, state_at_handoff}

[[ROTATION_HISTORY]]
   └── {from: Worker1, to: Worker2, trigger, timestamp}

[[DECISION_HISTORY]]
   └── {decision: chose X over Y, timestamp, rationale, actor}

[[EVIDENCE]]
   └── {test_results, screenshots, logs, approvals}
       {collected_at, verified_by}

[[CHANGE_LOG]]
   └── {what changed, when, who, why}
       {immutable, timestamped, auditable}
```

---

## Master Cross-Link Map

```
[[OBJECTIVE]]
      ↓
[[REQUIREMENT]]
      ↓
[[TASK_DEFINITION]]
      ├── [[OWNER]]
      ├── [[ASSIGNEE]]
      ├── [[EXECUTOR]]
      ├── [[CAPABILITY]]
      ├── [[AGENT]]
      ├── [[REPOSITORY]]
      ├── [[WORKFLOW]]
      ├── [[DEPENDENCY]]
      └── [[DEADLINE]]
              ↓
        [[EXECUTION]]
              ↓
       ┌──────┼─────────┬──────────┐
       ↓      ↓         ↓          ↓
   [[DONE]] [[BLOCKED]] [[HANDOFF]] [[ROTATION]]
       │       │          │          │
       │       ↓          ↓          ↓
       │  [[ESCALATE]] [[TRANSFER]] [[REASSIGN]]
       │                                │
       └────────┬─────────────────────┘
                ↓
          [[VERIFICATION]]
                ↓
             [[EVIDENCE]]
                ↓
            [[OUTCOME]]
                ↓
            [[FEEDBACK]]
                ↓
           [[LEARNING]]
                ↓
        [[KNOWLEDGE_GRAPH]]
                ↓
          [[WHERE_WE_ARE]]
                ↓
          [[NEXT_TASK]] ↺
```

---

## The Ontology Hierarchy

```
[[TASKS]]
├── [[TASK_EXECUTION]]               — This document
├── [[TASK_STATE]]                   — 23 states
├── [[UNCOMPLETED_WORK]]             — 10 failure modes
├── [[TASK_DEFINITION]]              — Task contract
├── [[TASK_OWNERSHIP]]               — 8 roles
├── [[DELEGATION]]                   — Assign/claim/accept
├── [[HANDOFFS]]                     — Full state transfer
├── [[ROTATIONS]]                    — Policy-driven reassignment
├── [[WORK_QUEUES]]                  — By priority, urgency, deadline
├── [[BLOCKERS]]                     — Blocking tasks registry
├── [[DEPENDENCIES]]                 — Task relationship map
├── [[CHECKPOINTS]]                  — Intermediate validation gates
├── [[VERIFICATION]]                 — Evidence + approval gates
├── [[COMPLETION]]                   — DONE vs VERIFIED
├── [[UPDATES]]                      — Cascading changes
├── [[CHANGE_LOG]]                   — Immutable history
├── [[AUDIT_LOG]]                    — Audit trail
├── [[FEEDBACK_LOOPS]]               — Learning from outcomes
├── [[WORKFLOWS]]                    — Multi-task orchestration
├── [[AGENTS]]                        — Who/what executes
├── [[CAPABILITIES]]                 — Required to execute
├── [[REPOSITORIES]]                 — Code artifacts
├── [[DECISIONS]]                    — Key trade-offs
├── [[OUTCOMES]]                     — Results delivered
└── [[SOURCE_OF_TRUTH]]              — Authoritative reality
```

---

## The Master Rule: NO FAKE COMPLETION

```
[[DECLARED_STATE]]   ← What the task claims
        +
[[OBSERVED_STATE]]   ← What the system detects
        +
[[VERIFIED_STATE]]   ← What humans/tests confirm
        =
[[ACTUAL_TASK_STATE]] ← Ground truth (immutable, auditable)
```

**If declared ≠ verified, the system defaults to [[UNVERIFIED]].**

**If observed contradicts verified, [[BLOCKED]] with escalation.**

**If history shows pattern of false claims → agent's autonomy reduced to L1 (report-only).**

---

## Implementation Checklist

- [ ] Map all existing work to this ontology
- [ ] Create TASK_STATE statemachine validator
- [ ] Implement [[DECLARED_STATE]] + [[OBSERVED_STATE]] + [[VERIFIED_STATE]] tracking
- [ ] Build verification gate that requires evidence before [[VERIFIED]]
- [ ] Create handoff template with all [[HANDOFF_PACKAGE]] fields mandatory
- [ ] Implement rotation engine that triggers on [[ROTATION_TRIGGER]]
- [ ] Set up cascading updates when task state changes
- [ ] Wire feedback loop to [[KNOWLEDGE_GRAPH]] for learning capture
- [ ] Create audit log immutability enforcement
- [ ] Build dashboard showing [[UNCOMPLETED_WORK]] by category
- [ ] Test: Task claims [[COMPLETED]], system catches missing evidence

---

**This is the execution control plane that prevents fake completion and ensures every work item's actual state is continuously reconstructed from reality, not merely declared.**

---

**Related:** [[WHOAMI.md]] · [[WHERE_WE_ARE.md]] · [[DATA_FLOW.md]] · [[INFRASTRUCTURE.md]] · [[CROSS_LINK_MASTER_ONTOLOGY.md]]

**Master execution framework: Complete task lifecycle from discovery to learning.**
