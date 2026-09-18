# Orchestrator Prime — State Machine & Decision Trees

**Version:** 1.0  
**Status:** Production-Ready  
**Authority:** [[02-MASTER-ORCHESTRATOR|02-MASTER-ORCHESTRATOR.md]] + [[05-EXECUTION-LOOP|05-EXECUTION-LOOP.md]]

> **Complete state machine and decision trees for the 13-stage Orchestrator loop.** Every decision point, outcome, and transition documented.

---

## Overview

The Orchestrator loop has **13 stages**, each with **decision points** that route to different outcomes:

```
OBSERVE → UNDERSTAND → DISCOVER → PLAN → DECOMPOSE → MATCH → DELEGATE → 
EXECUTE → MONITOR → EVALUATE → VERIFY → LEARN → UPDATEBRAIN → [LOOP]
```

Each stage has:
- **Input State** — What we need to know
- **Processing** — What happens
- **Decision Points** — YES/NO gates
- **Output State** — What we know afterward
- **Transitions** — Where we go next

---

## Stage 1: OBSERVE

**Purpose:** Assess current organizational state (capacity, constraints, objectives).

**Input State:**
- Agent registry (current capacity of 318 agents)
- Active task queue
- Business objectives (from REALITY.md)
- Constraints (budgets, approvals, policies)
- Time of day, priority levels

**Processing:**
```
1. Query Supabase: agent_stats (current tasks, capacity)
2. Query Neo4j: current business objectives
3. Load REALITY.md: facts overrule docs
4. Determine: Can we take on new work?
5. Set priority queue
```

**Decision Point 1: Can we take new work?**
```
IF current_load < capacity AND objectives_exist THEN
  → Continue to UNDERSTAND
ELSE IF current_load >= capacity THEN
  → Wait (queue task for later)
ELSE IF no objectives THEN
  → Halt loop (nothing to do)
```

**Output State:**
- Current capacity available
- Queued objectives ranked by priority
- Constraints to enforce
- Resources available (agents, budget, time)

---

## Stage 2: UNDERSTAND

**Purpose:** Clarify what objective matters most and why.

**Input State:**
- Priority-ordered objectives from OBSERVE
- Business context (revenue targets, risk tolerance)
- Venture stage (early, growth, mature)
- Market conditions

**Processing:**
```
1. Pick highest-priority objective from queue
2. Check: Is this objective still relevant?
   → Query REALITY.md for updates
3. Quantify impact:
   - Revenue impact if successful
   - Risk if we don't do this
   - Dependencies on other work
4. Extract success criteria:
   - What does "done" look like
   - How do we measure it
   - What's the deadline
```

**Decision Point 2: Is objective still relevant?**
```
IF objective_in_reality.md AND objective_aligns_with_strategy THEN
  → Continue to DISCOVER
ELSE IF objective_outdated THEN
  → Remove from queue, next objective
ELSE IF objective_contradicts_constraints THEN
  → Escalate to human (conflict)
```

**Output State:**
- Clarified objective with success criteria
- Revenue/risk quantification
- Deadline and priority
- Known constraints

---

## Stage 3: DISCOVER

**Purpose:** Inventory what capabilities we have to accomplish this objective.

**Input State:**
- Clear objective + success criteria
- Capability registry (307 capabilities)
- Agent registry (318 agents with skills)
- Past execution records

**Processing:**
```
1. Capability Registry:
   - What capabilities does objective require?
   - Do we have them (yes/partial/no)?
2. Agent Registry:
   - Which agents have required capabilities?
   - What's their current ROI/success rate?
3. Past Execution:
   - Have we done similar work?
   - What was the outcome/learning?
4. Qdrant Vector Search:
   - Find semantically similar past tasks
5. Compile: Possible agents + success probability
```

**Decision Point 3: Do we have required capability?**
```
IF capability_exists_AND_agents_available THEN
  → Continue to PLAN (use existing)
ELSE IF capability_partial (50-90% coverage) THEN
  → Continue to PLAN (with gap mitigation)
ELSE IF capability_missing (<50% coverage) THEN
  → Sub-decision: Build/Buy/Train/Partner/Defer?
    - IF urgent AND low-cost → TRAIN existing agent
    - IF urgent AND high-cost → PARTNER/BUY external
    - IF non-urgent → DEFER to later
    - IF strategic → BUILD in-house
```

**Output State:**
- List of agents who could execute this
- Capability gaps identified
- Acquisition plan for gaps (if any)
- Confidence in capability coverage

---

## Stage 4: PLAN

**Purpose:** Create strategy for execution (phases, sequence, dependencies).

**Input State:**
- Objective with success criteria
- Available capabilities (agents)
- Constraints (budget, time, permissions)
- Capability gaps + acquisition plan

**Processing:**
```
1. Strategy Design:
   - What's the optimal sequence?
   - What phases/stages?
   - What dependencies?
2. Resource Allocation:
   - Which agents for which phases?
   - Budget allocation per phase
   - Timeline per phase
3. Risk Identification:
   - What could go wrong?
   - Fallback strategies?
   - Escalation triggers?
4. Approval Gates:
   - Does this need human approval?
   - Budget threshold? (budgets > $5K)
   - Strategic risk? (ventures outside approved list)
```

**Decision Point 4: Is plan feasible?**
```
IF total_cost <= budget AND timeline_acceptable AND agents_available THEN
  → Continue to DECOMPOSE
ELSE IF total_cost > budget THEN
  → DECISION: Reduce scope OR increase budget?
    - IF reduce_scope: Back to PLAN (smaller objective)
    - IF increase_budget: Escalate to human
ELSE IF agents_unavailable:
  → DECISION: Wait for capacity OR find alternatives?
    - IF wait: Queue task, back to OBSERVE
    - IF alternatives: Back to DISCOVER (find new agents)
```

**Output State:**
- Phase-by-phase plan
- Resource allocation (agents, budget, time)
- Risk matrix + mitigation strategies
- Approval status (approved/needs-escalation)

---

## Stage 5: DECOMPOSE

**Purpose:** Break plan into discrete, executable tasks.

**Input State:**
- Approved plan with phases
- Resource allocation
- Success criteria for objective
- Dependencies between phases

**Processing:**
```
1. Task Breakdown:
   - Each phase → tasks
   - Each task is 15-60 minutes of agent work
2. Task Dependencies:
   - Task A must finish before Task B?
   - Parallel vs. sequential?
3. Task Specifications:
   - For each task: ID, description, success criteria, deadline
   - Context needed (data, references, approval rules)
4. Validation:
   - Sum of task costs = plan cost?
   - Sum of task times = plan timeline?
```

**Example Decomposition:**
```
Objective: Launch healthcare delivery in Charlotte

Phase 1: Market Research (Parallel, 5 days)
  ├─ TASK-001: Market sizing (TAM, SAM, SOM)
  ├─ TASK-002: Competitor analysis (top 5)
  └─ TASK-003: Regulatory analysis (NC healthcare rules)

Phase 2: Partnership Outreach (Sequential after Phase 1, 2 weeks)
  ├─ TASK-004: ID 20 potential hospital partners
  ├─ TASK-005: Cold outreach campaign (emails + calls)
  └─ TASK-006: Schedule partnership calls

Phase 3: Financial Modeling (Parallel after research, 1 week)
  └─ TASK-007: Build financial model (3-year projection)
```

**Decision Point 5: Are all tasks decomposed?**
```
IF all_phases_have_tasks AND all_tasks_have_success_criteria THEN
  → Continue to MATCH
ELSE
  → Back to DECOMPOSE (keep breaking down)
```

**Output State:**
- List of 5-20 discrete tasks
- Task dependencies (DAG)
- Task specifications (description, criteria, deadline)
- Readiness for agent assignment

---

## Stage 6: MATCH

**Purpose:** Assign best agent to each task.

**Input State:**
- List of discrete tasks
- Agent registry with capabilities
- Performance metrics (success rate, ROI)
- Agent capacity
- Venture permissions

**Processing:**
```
FOR EACH task:
  1. Extract required capability
  2. Query AGENT_REGISTRY:
     - Filter by capability
     - Filter by venture permission
     - Filter by autonomy level
  3. Score each candidate agent:
     - Capability match (40%)
     - Success rate on this type (30%)
     - Cost efficiency (20%)
     - Availability (10%)
  4. Return top 3 ranked agents
  5. Assign best available agent
```

**Scoring Example:**
```
TASK-005: Cold outreach campaign to hospitals

Candidates:
  AGT-042 (Sales Lead — Discovery Calls)
    - Capability match: 95/100 (expert in outreach)
    - Success rate: 96/100 (96% on similar tasks)
    - Cost efficiency: 85/100 ($25/task, high ROI)
    - Availability: 60/100 (6/10 capacity used)
    - TOTAL SCORE: 91/100 → ASSIGN ✓

  AGT-107 (Research Lead)
    - Capability match: 65/100 (can do it, not specialized)
    - Success rate: 80/100 (good but not best)
    - Availability: 30/100 (almost full)
    - TOTAL SCORE: 68/100 → BACKUP

  AGT-053 (Product Manager)
    - Capability match: 40/100 (not qualified)
    - TOTAL SCORE: 45/100 → NOT RECOMMENDED
```

**Decision Point 6: Can all tasks be assigned?**
```
IF all_tasks_assigned THEN
  → Continue to DELEGATE
ELSE IF some_tasks_unassigned THEN
  → DECISION: Find alternative agents OR escalate?
    - IF escalate: Escalate unassigned tasks to human
    - IF alternative: Back to MATCH (expand search criteria)
```

**Output State:**
- Task-to-agent assignments (each task → primary agent + backup)
- Autonomy level per task (L1/L2/L3)
- Total cost for objective
- Deadlines for each task

---

## Stage 7: DELEGATE

**Purpose:** Package task + context and send to agent.

**Input State:**
- Task-to-agent assignments
- Task specifications (description, criteria, deadline)
- Context (data, references, approval rules)
- Budget per task

**Processing:**
```
FOR EACH assigned task:
  1. Build task payload:
     - task_id, description, success_criteria, deadline
     - budget (individual + aggregate)
     - autonomy_level (L1/L2/L3)
     - context (venture, data, references)
  2. Determine escalation rules:
     - When to ask for human approval
     - When to escalate to backup agent
     - When to halt and alert
  3. Send task via OmniRoute:
     - POST /api/orchestrator/execute-task
     - Receive job_id + webhook_url
  4. Store task_execution record (Supabase)
```

**Decision Point 7: Did all tasks get delegated?**
```
IF all_tasks_queued THEN
  → Continue to EXECUTE
ELSE IF OmniRoute_unavailable THEN
  → Retry with exponential backoff (3 tries)
  → If still down: Escalate to human
ELSE IF task_rejected (budget/permission) THEN
  → Escalate to human OR modify task
```

**Output State:**
- All tasks queued with OmniRoute job IDs
- Webhooks registered for all tasks
- task_execution records created (status: queued)
- Fallback polling URLs active

---

## Stage 8: EXECUTE

**Purpose:** Agents execute; Orchestrator watches.

**Input State:**
- All tasks queued (omniroute_job_ids assigned)
- Expected timeline per task
- Monitoring triggers
- Escalation rules

**Processing:**
```
1. Agent begins execution (OmniRoute)
2. Orchestrator monitors:
   - Has task started? (check in 5 seconds)
   - Is it progressing? (check every 2 minutes)
   - Any errors? (check logs)
3. Webhook notifications arrive (async)
4. Task status: queued → running → completed
```

**Decision Point 8: Is execution on track?**
```
MONITOR EVERY 2 MINUTES:

IF task_still_running AND elapsed_time < expected_time THEN
  → Continue monitoring (normal)
ELSE IF task_still_running AND elapsed_time > expected_time * 1.5 THEN
  → DECISION: Escalate to L1 (human) OR extend deadline?
    - L2/L3: Auto-extend (log as anomaly)
    - L1: Alert human operator
ELSE IF task_timed_out (>15 min) THEN
  → Terminate, mark failed, escalate
ELSE IF error_detected THEN
  → Log error, attempt 1st retry
```

**Output State:**
- Task progress (% complete, items processed)
- Timing (queued_at, started_at, elapsed)
- Early indications of success/failure
- Agent feedback/progress messages

---

## Stage 9: MONITOR

**Purpose:** Continuously watch execution and alert on anomalies.

**Input State:**
- Task execution status
- Expected timeline vs. actual
- Agent logs/messages
- Capacity of dependent tasks

**Processing:**
```
FOR EACH running task:
  1. Check agent status (via OmniRoute logs)
  2. Measure progress:
     - % complete
     - Items/step processed
     - Remaining work estimate
  3. Detect anomalies:
     - Too slow? (behind timeline)
     - Errors? (agent logs)
     - Hung? (no progress in 5 min)
  4. Check blockers:
     - Is task blocked on other task?
     - Missing data or approval?
  5. Alert if anomaly detected
```

**Decision Point 9: Do we need to intervene?**
```
IF task_on_track THEN
  → Continue monitoring
ELSE IF task_slow (> 1.5x expected) THEN
  → Escalate: Ask agent for ETA update
ELSE IF task_blocked THEN
  → Unblock or terminate + retry
ELSE IF task_failed THEN
  → Jump to EVALUATE (failure path)
```

**Output State:**
- Real-time task progress dashboard
- Escalation alerts (if any)
- Revised ETA if task is slow
- Decision: continue monitoring OR escalate

---

## Stage 10: EVALUATE

**Purpose:** Did the task succeed? What was the quality?

**Input State:**
- Task completion status
- Agent output/deliverable
- Success criteria from original task
- Cost + time actual vs. estimate

**Processing:**
```
1. Completion Status:
   - Did agent report "done"?
   - Is deliverable present?
   - Are there errors?
2. Quality Assessment:
   - Does deliverable meet success_criteria?
   - Are there gaps or issues?
   - Confidence score (how certain)?
3. Financial Assessment:
   - Cost actual vs. estimate
   - Revenue actual vs. target (if applicable)
   - ROI: revenue ÷ cost
4. Learning:
   - What went well?
   - What went poorly?
   - Surprises?
```

**Decision Point 10: Did task succeed?**
```
IF deliverable_meets_criteria AND no_errors THEN
  → Continue to VERIFY (success path)
ELSE IF deliverable_partial (80-99% criteria) THEN
  → DECISION: Accept with caveats OR retry?
    - High confidence: VERIFY with note
    - Low confidence: RETRY with same/different agent
ELSE IF task_failed (<80% criteria) THEN
  → Jump to RETRY (failure path)
ELSE IF task_exceeded_budget THEN
  → Alert (document cost overrun)
```

**Output State:**
- Quality assessment (pass/partial/fail)
- Financial summary (cost, revenue, ROI)
- Learning points (what worked, what didn't)
- Decision: proceed to VERIFY or RETRY

---

## Stage 11: VERIFY

**Purpose:** Independently validate that result is actually correct.

**Input State:**
- Task output (evaluated in EVALUATE)
- Quality assessment
- Success criteria
- Available verification methods

**Processing:**
```
1. Verification Method Selection:
   - Automated: Run tests, check data integrity
   - Sampling: Spot-check 10% of results
   - External: Validate against authoritative source
   - Human: Have person review
2. Execute Verification:
   - Run checks
   - Collect evidence
   - Confidence score (0-100)
3. Document Verification:
   - What was checked
   - Evidence collected
   - Confidence level
```

**Example Verification:**
```
TASK-005 Output: "Successfully scheduled 18 of 20 discovery calls"

Verification Method:
  1. Automated: Check call confirmations in calendar system
  2. Sampling: Email 5 random prospects to confirm calls
  3. Evidence: Screenshots + confirmation emails
  4. Confidence: 94/100 (18 confirmed, 2 pending response)

VERIFIED: ✓ Task successful
```

**Decision Point 11: Is result valid?**
```
IF confidence >= 90% THEN
  → Continue to LEARN (verified success)
ELSE IF confidence 70-90% THEN
  → DECISION: Accept with caveat OR redo?
    - If critical task: Redo with better agent
    - If nice-to-have: Accept, document limitation
ELSE IF confidence < 70% THEN
  → DECISION: Redo task OR escalate to human
    - Redo: Back to MATCH (find better agent)
    - Escalate: Escalate for human review
```

**Output State:**
- Verification result (verified/unverified/partial)
- Confidence score
- Evidence collected
- Decision: accept OR redo

---

## Stage 12: LEARN

**Purpose:** Extract learning from task execution for future improvement.

**Input State:**
- Task outcome (success/failure/partial)
- Agent performance metrics
- Cost vs. estimate
- Time vs. estimate
- Learning points noted in EVALUATE

**Processing:**
```
1. Pattern Detection:
   - Did similar agents handle similar tasks better/worse?
   - Is there a pattern to success/failure?
   - Does agent performance match historical average?
2. Agent Learning:
   - Update agent success_rate
   - Update agent cost_per_task
   - Update agent roi_multiple
   - Flag if agent trending down
3. Capability Learning:
   - Did capability work as expected?
   - Any gaps discovered?
   - Success rate for this capability
4. Decision Learning:
   - Did we pick the right agent?
   - Did we set right deadline/budget?
   - Should we adjust scoring for future?
```

**Decision Point 12: Are there learnings?**
```
IF pattern_detected (agent consistently underperforming) THEN
  → Flag for retraining or retirement
ELSE IF capability_gap_discovered THEN
  → Add to capability_gap_matrix
  → Update acquisition plan (if gap is frequent)
ELSE IF process_improvement_found THEN
  → Document improvement
  → Share with team
ELSE
  → Normal: Continue to UPDATEBRAIN
```

**Output State:**
- Agent performance update (new stats)
- Capability assessment update
- Process improvements (if any)
- Learning record for future reference

---

## Stage 13: UPDATEBRAIN

**Purpose:** Store results and learning back to Company Brain.

**Input State:**
- Task execution record (status, cost, time)
- Verification result
- Learning points
- Agent performance updates
- Revenue attribution (if applicable)

**Processing:**
```
1. Supabase Updates:
   - Update task_execution record (final status)
   - Create revenue_log entry (revenue + cost)
   - Update agent_stats (new performance metrics)
2. Neo4j Updates:
   - Update agent nodes (performance + ROI)
   - Add task execution edge (if creating relationship)
   - Update capability coverage (% of ventures with capability)
3. Memory System:
   - Store episodic memory (what happened)
   - Update long-term memory (patterns)
   - Update agent memory (feedback to agent)
4. Triggers:
   - Update venture_revenue_summary
   - Update leaderboard (if top 10 agent)
   - Alert if agent trending down
```

**Decision Point 13: Is update successful?**
```
IF all_updates_successful THEN
  → Loop complete, back to OBSERVE
ELSE IF database_write_fails THEN
  → Retry up to 3 times
  → If still failing: Alert operator (data loss risk)
ELSE IF partial_update THEN
  → Log partial update, alert for manual reconciliation
```

**Output State:**
- All task data persisted to Supabase
- All learning persisted to Neo4j
- Agent stats updated
- Company Brain updated with new knowledge
- Ready for next iteration

---

## Loop Closure & Return to OBSERVE

```
Task Complete
    ↓
OBSERVE: Check if more work
    ├─ IF capacity AND objectives: Continue with next task
    ├─ IF no capacity: Queue task, wait for capacity
    └─ IF no objectives: Halt until new objective
```

---

## Failure Paths

### Path A: Agent Fails During Execution

```
EXECUTE → MONITOR (detect failure)
    ↓
Retry Agent:
  1. Was it transient error? (network, timeout)
     → YES: Retry same agent (up to 3 tries)
     → NO: Escalate to MATCH
  2. Retry with same agent + same budget?
     → YES if confidence > 70%
     → NO if confidence < 70%: Find better agent
  3. If all retries fail → Terminal failure
```

### Path B: Task Takes Too Long

```
EXECUTE → MONITOR (detect delay)
    ↓
Escalate to Human:
  1. Alert: Task X is behind by 2 hours
  2. Options:
     a) Extend deadline + continue
     b) Swap to faster agent + restart
     c) Reduce scope + proceed with less
  3. Human decision → Resume execution
```

### Path C: Verification Fails

```
VERIFY (detect invalid result)
    ↓
Redo Decision:
  1. Was agent not qualified?
     → MATCH (find better agent)
  2. Was deadline too short?
     → PLAN (extend deadline)
  3. Is objective unclear?
     → UNDERSTAND (clarify objective)
```

---

## Decision Point Summary

| Stage | Decision | YES Path | NO Path |
|-------|----------|----------|---------|
| **1. OBSERVE** | Can take new work? | UNDERSTAND | Wait/Halt |
| **2. UNDERSTAND** | Objective still relevant? | DISCOVER | Remove/Escalate |
| **3. DISCOVER** | Have required capability? | PLAN (use existing) | PLAN (acquire) |
| **4. PLAN** | Plan feasible? | DECOMPOSE | Reduce/Escalate |
| **5. DECOMPOSE** | All tasks decomposed? | MATCH | Decompose more |
| **6. MATCH** | All tasks assigned? | DELEGATE | Find alternatives |
| **7. DELEGATE** | All tasks queued? | EXECUTE | Retry/Escalate |
| **8. EXECUTE** | On track? | MONITOR | Escalate/Extend |
| **9. MONITOR** | Need intervention? | EVALUATE (if done) | Alert/Unblock |
| **10. EVALUATE** | Task succeed? | VERIFY | Retry |
| **11. VERIFY** | Result valid? | LEARN | Redo/Escalate |
| **12. LEARN** | Learnings? | UPDATEBRAIN | UPDATEBRAIN |
| **13. UPDATEBRAIN** | Update OK? | OBSERVE (loop) | Alert/Reconcile |

---

## References

- [[02-MASTER-ORCHESTRATOR|02 — The Master Orchestrator]] — 13-stage loop description
- [[05-EXECUTION-LOOP|05 — The Execution Loop]] — 14-stage detailed flow
- [[ORCHESTRATOR-MASTER-SPECIFICATION|Master Specification]] — Implementation details
- [[ORCHESTRATOR-API-REFERENCE|API Reference]] — How to invoke each stage

---

**Last Updated:** 2026-09-18 | **Version:** 1.0 | **Authority:** CP-033 (Execution)
