# 02 — The Master Orchestrator

**Version:** 1.0  
**Status:** Foundation Architecture  
**Authority:** CP-033 (Execution) + [[REALITY|REALITY.md]]  

> **The Master Orchestrator turns organizational knowledge into distributed work.** Given an objective and the Company Brain's intelligence, it plans, decomposes, discovers, delegates, monitors, evaluates, and learns.

---

## What the Master Orchestrator Is

The Master Orchestrator is **not a UI.** It is the **cognitive loop that continuously observes organizational state, understands what needs to happen, discovers what's capable, plans work, delegates to agents, monitors execution, evaluates results, and updates the Company Brain with what was learned.**

It runs **continuously**, asking one question at a time:

```text
What does the organization need to do next?
    ↓
What objective should we pursue?
    ↓
What capabilities would accomplish this?
    ↓
Who has those capabilities?
    ↓
What are the constraints?
    ↓
What's the plan?
    ↓
How do we decompose it?
    ↓
Which agent should do what?
    ↓
Delegate.
    ↓
Monitor.
    ↓
Did it work?
    ↓
Update Company Brain.
    ↓
What's next?
```

---

## The Master Loop

```text
                        ┌─────────────────────────┐
                        │   COMPANY BRAIN         │
                        │   (Intelligence Layer)  │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │    1. OBSERVE           │
                        │  Current state?         │
                        │  Capacity? Constraints? │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │    2. UNDERSTAND        │
                        │  What's the objective?  │
                        │  Why does it matter?    │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │    3. DISCOVER          │
                        │  What capabilities     │
                        │  already exist?        │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │    4. PLAN              │
                        │  What's the strategy?   │
                        │  What's the sequence?   │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │    5. DECOMPOSE         │
                        │  What tasks?            │
                        │  What dependencies?     │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │    6. MATCH             │
                        │  Which agent for each   │
                        │  task? (by capability,  │
                        │  capacity, cost, track  │
                        │  record)                │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │    7. DELEGATE          │
                        │  Send work to agents.   │
                        │  Package context.       │
                        │  Set deadline.          │
                        │  Await result.          │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │    8. EXECUTE           │
                        │  Agents do the work.    │
                        │  (Orchestrator watches) │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │    9. MONITOR           │
                        │  Is it on track?        │
                        │  Do we need to adjust?  │
                        │  Should we escalate?    │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │   10. EVALUATE          │
                        │  Did it work?           │
                        │  What was the quality?  │
                        │  What was the cost?     │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │   11. VERIFY            │
                        │  Is the result correct? │
                        │  Can we prove it?       │
                        │  What edge cases exist? │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │   12. LEARN             │
                        │  What worked?           │
                        │  What failed?           │
                        │  What changed?          │
                        │  How do we improve?     │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │   13. UPDATE BRAIN      │
                        │  Store results.         │
                        │  Update stats.          │
                        │  Refresh memory.        │
                        │  Adjust next plan.      │
                        └────────────┬────────────┘
                                     │
                                     └──────────────┐
                                                    │
                                     ┌──────────────┘
                                     ▼
                                 [LOOP]
```

---

## Core Subsystems

### 1. Observer (What is the state?)

The Observer continuously queries the Company Brain:
- Current capacity of each agent
- Active tasks and their status
- Incomplete work
- Business objectives and priorities
- Constraints and approvals required

### 2. Understander (Why does it matter?)

The Understander determines:
- What objective should be pursued **now** (vs. later)
- Why it matters (business impact, risk, customer impact)
- What constraints apply (budget, time, people, tech)
- What success looks like (metrics, evidence, verification)

### 3. Discoverer (What's possible?)

The Discoverer queries:
- Capability Registry: What skills do we have?
- Agent Registry: Which agents have those skills?
- Tool Registry: What tools can help?
- Workflow Registry: What repeatable patterns exist?
- Repository Registry: What code is available?
- Research Registry: What research exists?
- Past Success: How have we solved similar problems?

### 4. Planner (What's the strategy?)

The Planner creates a plan:
```yaml
objective: "Launch HealthRoute in Charlotte by Oct 1"
success_criteria:
  - 25 partnerships established
  - $2K MRR in month 1
  - <4 hour average delivery time
  - >95% customer satisfaction
strategy:
  - Phase 1: Market research (1 week) — 5 agents in parallel
  - Phase 2: Partnership outreach (2 weeks) — 3 agents + 1 skill
  - Phase 3: Operations setup (1 week) — 2 agents
  - Phase 4: Launch (1 day) — All hands
timeline: 5 weeks
budget: $15K
risks: [regulatory, partner availability, launch timing]
```

### 5. Decomposer (What are the tasks?)

The Decomposer breaks the plan into tasks:
```
TASK-001: Market Research
  Dependencies: none
  Owner: Agent assignment TBD
  Deadline: 2026-09-22
  Success metric: Research report + 5000 prospect list
  
TASK-002: Competitor Analysis
  Dependencies: TASK-001 (soft)
  Owner: Agent assignment TBD
  Deadline: 2026-09-22
  Success metric: Competitive matrix + pricing analysis

TASK-003: Regulatory Analysis
  Dependencies: none
  Owner: Agent assignment TBD
  Deadline: 2026-09-22
  Success metric: Compliance checklist + partner list
  
... (20+ more tasks)
```

### 6. Matcher (Which agent?)

The Matcher scores each agent for each task:

```
TASK-001: Market Research

Agent AGT-107 (Research Lead)
  Capability match: 95/100 ✅
  Past success: 92% (similar tasks)
  Current capacity: 40/100 (can take it)
  Cost: $400
  Risk: Low
  Score: 92 → RECOMMENDED

Agent AGT-042 (Sales Lead)
  Capability match: 60/100 (sales focused, not research)
  Past success: 85% (can do it, not optimal)
  Current capacity: 10/100 (almost full)
  Cost: $300 (cheaper)
  Risk: Medium (stretched thin)
  Score: 51 → POSSIBLE BACKUP
```

**Ranking:** 1. AGT-107, 2. AGT-042 (if AGT-107 unavailable), 3. Escalate to human

### 7. Delegator (Send the work)

The Delegator packages and sends work:

```
TO: AGT-107 (Research Lead)
TASK: TASK-001 (Market Research — Charlotte Healthcare)

OBJECTIVE:
  Understand the Charlotte healthcare delivery market.

DELIVERABLE:
  Research report including:
    - Market size & TAM
    - Competitor landscape (top 5)
    - Regulatory environment
    - Prospect list (5000+)
    - Pricing analysis
    - Risk assessment

CONTEXT:
  [Company Brain assembles here — only relevant facts]
  - Previous LT research in Memphis (similar market)
  - Healthcare regulatory summary (North Carolina specific)
  - Competitive list (starter)
  - Prospect data (Charlotte zip codes)

DEADLINE: 2026-09-22 18:00
BUDGET: $400
AUTONOMY: L2 (I'll monitor, escalate if you get stuck)

VERIFICATION:
  I will verify by:
    - Checking sources cited
    - Validating 10 random prospects
    - Comparing to industry benchmarks
```

### 8. Executor (Agents do work)

Agents execute with full context and autonomy:
- They have the objective, context, tools, and deadline
- They can request more context mid-execution
- They escalate if blocked
- They report results with evidence

### 9. Monitor (Track progress)

The Orchestrator watches:
- Task progress (% complete)
- Resource usage (budget, time, capacity)
- Blockers (is the agent stuck?)
- Quality signals (is the work on track?)
- Risks (should we adjust the plan?)

### 10. Evaluator (Did it work?)

The Evaluator asks:
- Did the agent complete the task?
- Did it meet the success criteria?
- What was the quality?
- What was the cost (time + money)?
- What went well? What went wrong?

### 11. Verifier (Can we prove it?)

The Verifier checks:
- Are the results correct?
- Can we validate against reality?
- What edge cases might break this?
- What evidence supports this?
- What could we be wrong about?

### 12. Learner (What did we learn?)

The Learner extracts:
- What worked? (Pattern for future use)
- What failed? (Prevention strategy)
- What surprised us? (Update mental models)
- What changed? (Adjust next plan)
- How should we improve? (Agent development)

### 13. Brain Updater (Store it)

The Updater writes back:
- Task execution record (to task_executions)
- Agent performance (update agent_stats)
- Revenue (if applicable, to revenue_logs)
- Memory (episodic + lessons learned)
- Registries (if capabilities/agents/skills changed)

---

## Decision Framework

The Orchestrator makes decisions by asking:

### Can We Do This?
```
Objective → Required Capability → Capability Registry
         → Do we have it? (YES/NO/PARTIAL)
         → If NO → Can we build? (time/cost/risk)
         → If PARTIAL → What's the gap?
         → Decision: Build / Buy / Partner / Defer
```

### Who Should Do This?
```
Task → Required Skills → Agent Registry
    → Filter by: [capability match] [availability] [cost] [past performance]
    → Score by: capability (40%) + success_rate (30%) + capacity (20%) + cost (10%)
    → Select: Top-ranked agent (or escalate if no match)
```

### When Should We Do This?
```
Objective → Business Impact (revenue? risk? dependency?)
         → Agent Capacity (who's available?)
         → Dependencies (what must finish first?)
         → Deadline (hard or soft?)
         → Priority (score vs. other work)
         → Schedule: ASAP / This week / This month / Defer
```

### How Do We Know It Worked?
```
Task → Success Criteria
    → Measurement (how to verify?)
    → Evidence (what proof is needed?)
    → Verification (who checks? how?)
    → Confidence (how certain are we?)
```

---

## Failure Modes & Recovery

### If an agent fails:
```
Task execution fails → Evaluate reason
                   → Retry with same agent? (if transient error)
                   → Switch agent? (if agent overmatched)
                   → Escalate? (if no other agent available)
                   → Human review? (if too high-risk to automate)
```

### If a plan fails:
```
Plan blocked → Diagnose blocker
            → Remove blocker? (adjust dependencies, get approval, etc.)
            → Skip task? (is it critical?)
            → Find workaround? (alternative path?)
            → Replan? (different strategy)
            → Escalate? (human decision)
```

### If the objective is unreachable:
```
Objective → Remove? (no longer needed)
         → Defer? (can't do now, try later)
         → Scale back? (partial success ok?)
         → Escalate? (stakeholder decision)
```

---

## Key Invariants

The Orchestrator **never**:
- ❌ Claims work is done without verification
- ❌ Delegates to an agent without checking capacity
- ❌ Ignores evidence of failure
- ❌ Continues a plan when it's obviously not working
- ❌ Forgets to update the Company Brain with results
- ❌ Executes work that violates policies/permissions
- ❌ Assigns work beyond an agent's capability
- ❌ Skips evaluation to save time

The Orchestrator **always**:
- ✅ Checks if capability exists before planning
- ✅ Scores agents by multiple dimensions (not just one)
- ✅ Packages context specific to the task
- ✅ Monitors work in progress
- ✅ Evaluates results against criteria
- ✅ Updates the Company Brain with learning
- ✅ Verifies before claiming success
- ✅ Escalates when uncertain

---

## The Orchestrator-Brain-Agent Contract

### Orchestrator → Brain:
"Before I delegate, I need to know: current state, past performance, available capabilities, constraints, and what mattered last time"

### Brain → Orchestrator:
"Here's the current state (confidence scores included), here's what worked before, here's who has what skills, here's your constraints"

### Orchestrator → Agent:
"I need you to accomplish X. Here's why it matters. Here's the context you need. Here's your deadline. Here's how I'll verify. Tell me if you need more context."

### Agent → Orchestrator:
"I'm working on it. I've hit a blocker here. I'm done. Here's the result. Here's the evidence."

### Orchestrator → Brain:
"Here's what happened. Here's what we learned. Here's the evidence. Update your state. Here's what we should do next."

---

## References

- [[COMPANY-BRAIN|01-COMPANY-BRAIN.md]] — The intelligence this orchestrator uses
- [[AGENT-SYSTEM|03-AGENT-SYSTEM.md]] — The workers executing delegated tasks
- [[CAPABILITY-SYSTEM|10-CAPABILITY-SYSTEM.md]] — The inventory of what's possible
- [[EXECUTION-LOOP|05-EXECUTION-LOOP.md]] — The complete flow from decision to learning
- [[ORCHESTRATOR-MASTER-SPECIFICATION|ORCHESTRATOR-MASTER-SPECIFICATION.md]] — Implementation details

---

**Next:** Read [[AGENT-SYSTEM|03-AGENT-SYSTEM.md]] to understand who does the work.

**Last Updated:** 2026-09-18 | **Architecture Version:** 1.0
