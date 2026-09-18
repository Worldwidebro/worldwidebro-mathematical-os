# 05 — The Execution Loop

**Version:** 1.0  
**Status:** Foundation Architecture  
**Authority:** [[REALITY|REALITY.md]] + Master Orchestrator Loop  

> **The Execution Loop is the complete cycle from objective to outcome.** It binds together the Company Brain, Master Orchestrator, Agents, and Capability System into one continuous, learning system.

---

## The Complete Loop

```text
┌─────────────────────────────────────────────────────────────────────┐
│                         COMPANY BRAIN                              │
│                    (Organizational Intelligence)                   │
│                                                                     │
│  Knows: State, Capabilities, History, Constraints, Priorities      │
│  Provides: Context, Constraints, Memory, Evidence                  │
└────┬────────────────────────────────────────────────────────────────┘
     │
     │ QUERY: "What should we do next?"
     │ RESPONSE: Business objectives, constraints, capacity, precedent
     │
     ▼
┌─────────────────────────────────────────────────────────────────────┐
│            1. OBSERVE — Master Orchestrator                        │
│                                                                     │
│  • What is the current organizational state?                       │
│  • What capacity is available (agent, budget, time)?               │
│  • What constraints exist?                                          │
│  • What's the business priority?                                    │
└────┬────────────────────────────────────────────────────────────────┘
     │
     │ Decision Point: Is there work to do?
     │
     ├─ NO: Sleep until next check (15 min)
     │
     └─ YES: Continue to UNDERSTAND
     │
     ▼
┌─────────────────────────────────────────────────────────────────────┐
│            2. UNDERSTAND — Master Orchestrator                     │
│                                                                     │
│  • What is the objective?                                           │
│  • Why does it matter (business impact)?                            │
│  • What would success look like?                                    │
│  • What are the constraints (budget, deadline, risk)?              │
│  • What have we tried before (from memory)?                         │
└────┬────────────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────────────────┐
│            3. DISCOVER — Master Orchestrator                       │
│                                                                     │
│  Query Capability Registry:                                         │
│  • Does this capability already exist?                              │
│  • Who has it? (Agent Registry)                                     │
│  • What's the cost? (Performance stats)                             │
│  • What's the precedent? (Memory system)                            │
│                                                                     │
│  Possible outcomes:                                                 │
│  ├─ We have it → PLAN with existing capability                    │
│  ├─ We have partial → PLAN to improve + fill gap                  │
│  └─ We don't have it → DECIDE: Build/Buy/Train/Partner/Defer      │
└────┬────────────────────────────────────────────────────────────────┘
     │
     │ Decision Point: Can we proceed?
     │
     ├─ NO (critical capability missing): Escalate to human
     │
     └─ YES (capability exists or acceptable risk): PLAN
     │
     ▼
┌─────────────────────────────────────────────────────────────────────┐
│            4. PLAN — Master Orchestrator                           │
│                                                                     │
│  Create strategy:                                                   │
│  • What's the end-to-end approach?                                  │
│  • What's the sequence (dependencies)?                              │
│  • What's the timeline?                                             │
│  • What's the budget?                                               │
│  • What could go wrong (risks)?                                     │
│  • How will we know if it worked?                                   │
└────┬────────────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────────────────┐
│            5. DECOMPOSE — Master Orchestrator                      │
│                                                                     │
│  Break plan into executable tasks:                                  │
│                                                                     │
│  TASK-1: Market Research (5 days)                                  │
│    ├─ Success criteria: [list]                                     │
│    ├─ Dependencies: none                                            │
│    └─ Deadline: 2026-09-22                                         │
│                                                                     │
│  TASK-2: Competitor Analysis (3 days)                              │
│    ├─ Success criteria: [list]                                     │
│    ├─ Dependencies: TASK-1 (soft)                                  │
│    └─ Deadline: 2026-09-22                                         │
│    ... [etc.]                                                      │
└────┬────────────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────────────────┐
│            6. MATCH — Master Orchestrator                          │
│                                                                     │
│  For each task, score and select the best agent:                   │
│                                                                     │
│  TASK-1: Market Research                                           │
│    ├─ Best match: AGT-107 (Research Lead), score: 95/100          │
│    ├─ Backup: AGT-042 (if AGT-107 full)                           │
│    ├─ Cost estimate: $400                                          │
│    └─ Assignment → AGT-107                                         │
│                                                                     │
│  TASK-2: Competitor Analysis                                       │
│    ├─ Best match: AGT-107, score: 92/100                          │
│    ├─ Cost estimate: $300                                          │
│    └─ Assignment → AGT-107                                         │
│    ... [etc.]                                                      │
└────┬────────────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────────────────┐
│            7. DELEGATE — Master Orchestrator → Agents              │
│                                                                     │
│  Package and send work:                                             │
│                                                                     │
│  TO: AGT-107                                                        │
│  TASK: TASK-1 (Market Research)                                    │
│  ├─ Objective: Understand Charlotte healthcare market              │
│  ├─ Success criteria: [list]                                       │
│  ├─ Deadline: 2026-09-22 18:00                                     │
│  ├─ Budget: $400                                                    │
│  ├─ Context: [Company Brain assembles minimal relevant facts]     │
│  ├─ Tools: [List of available tools]                               │
│  └─ Autonomy: L2 (I'll monitor, escalate if stuck)                │
│                                                                     │
│  AGT-107 responds: "Accepted. Starting now. ETA 2 days."           │
└────┬────────────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────────────────┐
│            8. EXECUTE — Agents (Hours/Days)                        │
│                                                                     │
│  • Agents do the work                                               │
│  • Orchestrator watches for:                                        │
│    - Progress updates (every 2 hours for long tasks)               │
│    - Blockers (agent asks for help)                                │
│    - Cost/time variance (on track?)                                │
│    - Quality signals (is this good work?)                          │
│                                                                     │
│  Agent reports (2-hour checkin):                                    │
│    "On track. Found 2000 prospects. Vetting now. ETA 18 hours."   │
└────┬────────────────────────────────────────────────────────────────┘
     │
     │ Decision Point (continuous): Is execution healthy?
     │
     ├─ NO (blocked, behind, low quality) → Intervene
     │ │  ├─ Request more context from Company Brain
     │ │  ├─ Escalate to human if stuck >30 min
     │ │  └─ Replan if assumptions broken
     │ │
     │ └─ YES: Continue
     │
     ▼
┌─────────────────────────────────────────────────────────────────────┐
│            9. COMPLETE — Agent Reports Result                      │
│                                                                     │
│  Agent submits result with:                                         │
│  ├─ Deliverable (what was produced)                                │
│  ├─ Evidence (how we know it's correct)                            │
│  ├─ Cost (actual vs. estimate)                                     │
│  ├─ Time (actual vs. estimate)                                     │
│  ├─ Learning (what worked, what didn't)                            │
│  └─ Questions (what do you want to know?)                          │
│                                                                     │
│  Example:                                                           │
│    Deliverable: 5000 prospects, validation: verified 500 (100%)    │
│    Cost: $395 (within estimate)                                    │
│    Time: 42 hours (estimate was 40)                                │
│    Learning: LinkedIn was 3x more effective than Clearbit          │
└────┬────────────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────────────────┐
│           10. EVALUATE — Master Orchestrator                       │
│                                                                     │
│  • Did the agent complete the task?                                │
│  • Did it meet the success criteria?                               │
│  • What was the quality?                                           │
│  • What was the actual cost vs. estimate?                          │
│  • What was the actual time vs. estimate?                          │
│                                                                     │
│  Score: "EXCELLENT"                                                │
│    ├─ Deliverable: ✅ Complete (5000 prospects)                    │
│    ├─ Accuracy: ✅ Verified (100% sample)                          │
│    ├─ Cost: ✅ On budget (+$5 variance)                            │
│    ├─ Time: ✅ Nearly on time (+2 hours variance)                  │
│    └─ Overall: ✅ Exceeded expectations                            │
└────┬────────────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────────────────┐
│           11. VERIFY — Evaluation System                           │
│                                                                     │
│  • Spot-check deliverable (sample verification)                   │
│  • Compare to success criteria (checklist)                          │
│  • Validate against evidence (third-party checks)                  │
│  • Assess edge cases (what could fail in production?)              │
│                                                                     │
│  Verification Report:                                              │
│    ├─ Sample: Verified 500/5000 prospects (100% accurate)          │
│    ├─ Deliverable: ✅ Meets all criteria                           │
│    ├─ Evidence strength: 9/10 (high confidence)                    │
│    ├─ Edge cases: May degrade with new demographics                │
│    └─ Risk: LOW. Ready for next stage.                             │
└────┬────────────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────────────────┐
│           12. LEARN — Master Orchestrator                          │
│                                                                     │
│  Extract lessons for future:                                       │
│  ├─ What worked: LinkedIn-first strategy (3x better ROI)           │
│  ├─ What failed: Clearbit had low match rate                       │
│  ├─ Pattern: Multi-source verification increases confidence        │
│  ├─ Recommendation: For next similar task, use LinkedIn-first      │
│  └─ Update: AGT-107 success rate increased to 97% (this venue)    │
└────┬────────────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────────────────┐
│           13. UPDATE BRAIN — Store Results                         │
│                                                                     │
│  Write back to Company Brain:                                       │
│  ├─ Task execution record (success, cost, time, quality)           │
│  ├─ Agent stats (update AGT-107 success rate, capacity)           │
│  ├─ Revenue attribution (if applicable: $X → task → agent → $Y)   │
│  ├─ Memory: "Market research strategy that works for Charlotte"   │
│  ├─ Registries: If new capability discovered, update               │
│  ├─ Workflow: If this becomes repeatable, create template          │
│  └─ Priority: Update next-work based on new information            │
│                                                                     │
│  Company Brain updated. Next work now has:                         │
│  ├─ 5000 qualified prospects (enables next task)                   │
│  ├─ Proven strategy (LinkedIn-first)                               │
│  ├─ Successful agent profile (AGT-107: 97% in Charlotte)          │
│  └─ Confidence: HIGH                                                │
└────┬────────────────────────────────────────────────────────────────┘
     │
     │ Decision Point: Is the overall objective complete?
     │
     ├─ NO (more tasks to do): Go to MONITOR (start watching task 2)
     │
     └─ YES (objective complete): Synthesize results
     │
     ▼
┌─────────────────────────────────────────────────────────────────────┐
│           14. SYNTHESIZE — Bring All Results Together              │
│                                                                     │
│  Combine all task results into unified outcome:                    │
│                                                                     │
│  OBJECTIVE: "Launch HealthRoute in Charlotte"                      │
│  ├─ Market research: COMPLETE ✅ (5000 prospects, $50K TAM)        │
│  ├─ Competitor analysis: COMPLETE ✅ (3 competitors, $85-150)      │
│  ├─ Regulatory: COMPLETE ✅ (no restrictions, local partner needed)│
│  ├─ Financial model: COMPLETE ✅ (breakeven 4mo, payback 8mo)      │
│  └─ Overall: READY TO LAUNCH ✅                                    │
│                                                                     │
│  Decision: Proceed with October 1 launch                            │
│  Confidence: 95% (supported by 4 independent analyses)              │
│  Risk: Low                                                          │
│  Next action: Begin partnership outreach (TASK-3)                  │
└────┬────────────────────────────────────────────────────────────────┘
     │
     │ Update Company Brain with outcome
     │ Mark objective COMPLETE
     │ Record evidence + learning
     │
     ▼
             [LOOP CONTINUES WITH NEXT OBJECTIVE]
            (Orchestrator goes back to OBSERVE)
```

---

## Key Decision Points

### At Each Stage:

| Stage | Decision | YES → | NO → |
|-------|----------|-------|------|
| **1. OBSERVE** | Is there work? | UNDERSTAND | Sleep |
| **2. UNDERSTAND** | Do we know why? | DISCOVER | Escalate |
| **3. DISCOVER** | Can we do it? | PLAN | Acquire capability |
| **4. PLAN** | Is the plan sound? | DECOMPOSE | Revise plan |
| **5-6. DECOMPOSE+MATCH** | Are agents ready? | DELEGATE | Wait for capacity |
| **7. DELEGATE** | Agent accepted? | EXECUTE | Find backup agent |
| **9. EVALUATE** | Did it work? | VERIFY | Analyze failure |
| **11. VERIFY** | Can we trust it? | LEARN | Request rework |
| **14. SYNTHESIZE** | Is objective done? | UPDATE BRAIN | Continue loop |

---

## Failure Handling

### If Agent Fails (At Step 8-9):

```
DETECT FAILURE (task missed deadline, low quality, error)
    ↓
ANALYZE: Why did this agent fail?
    ├─ Capability gap? (agent overmatched)
    ├─ Context gap? (missing information)
    ├─ Blocker? (external dependency failed)
    ├─ Overloaded? (too much capacity)
    └─ First-time task? (new capability)
    ↓
RECOVER:
    ├─ Same agent + more context/time?
    ├─ Different agent (better fit)?
    ├─ Escalate to human?
    └─ Redesign task?
    ↓
RETRY or ESCALATE
```

### If Plan Fails (At Step 4):

```
DETECT PLAN BROKEN (assumptions were wrong, market changed, etc.)
    ↓
REPLAN:
    ├─ Gather new information (query Company Brain)
    ├─ Adjust strategy
    ├─ Adjust timeline/budget
    └─ Retry
    ↓
Or escalate to human for decision
```

### If Objective Unreachable:

```
DETECT IMPOSSIBLE (can't get capability, won't fit budget, deadline passed)
    ↓
OPTIONS:
    ├─ Defer (wait for capability to become available)
    ├─ Reduce scope (partial success ok?)
    ├─ Cancel (no longer needed)
    └─ Escalate (stakeholder decision)
```

---

## Continuous Monitoring

While a task is executing (Step 8), the Orchestrator continuously monitors:

- **Every 30 minutes:** Is the agent working?
- **Every 2 hours:** Get progress update
- **Every 4 hours:** Check budget/time variance
- **On escalation:** Drop everything, help agent

The Company Brain provides:
- Additional context if agent asks
- Real-time constraint updates (budget changed, deadline moved)
- Escalation contacts (if agent is stuck)

---

## The Loop Properties

### Continuous
```
The loop never stops. Even when there's no work, it checks every 15 minutes.
```

### Recursive
```
Each task IS the loop. Decompose a task → those subtasks are their own loops.
```

### Defensive
```
Every stage has a decision point. If uncertain, escalate.
```

### Evidence-Driven
```
Nothing moves forward without verification.
```

### Learning-Enabled
```
Every execution updates the Company Brain for the next execution.
```

### Failure-Safe
```
When things break, the system detects it, analyzes it, and recovers.
```

---

## References

- [[COMPANY-BRAIN|01-COMPANY-BRAIN.md]] — Intelligence source (stages 1-2)
- [[MASTER-ORCHESTRATOR|02-MASTER-ORCHESTRATOR.md]] — Decision-maker (stages 3-6, 10-13)
- [[AGENT-SYSTEM|03-AGENT-SYSTEM.md]] — Workers (stages 7-9)
- [[CAPABILITY-SYSTEM|04-CAPABILITY-SYSTEM.md]] — Inventory (stages 3)

---

## Summary

**The Execution Loop is the complete organizational operating model:**

1. Brain provides intelligence
2. Orchestrator makes decisions
3. Agents execute work
4. Capabilities enable execution
5. Results update the Brain
6. Loop continues

This is not a UI. This is how the organization works.

---

**Next:** All 5 foundation documents are now complete. Every other system (agents, skills, tools, workflows, research, evaluation, verification) hangs off these 5.

**Last Updated:** 2026-09-18 | **Architecture Version:** 1.0
