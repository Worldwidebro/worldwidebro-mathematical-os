# 03 — The Agent System

**Version:** 1.0  
**Status:** Foundation Architecture  
**Authority:** [[AGENTS|AGENTS.md]] + [[REALITY|REALITY.md]]  

> **Agents are the workers.** They receive delegated tasks from the Orchestrator, execute work within their capabilities, report results with evidence, and feed learning back to the Company Brain.

---

## What an Agent Is

An agent is **not a chatbot or a UI.** It is a **specialized worker characterized by: capabilities (skills + tools), performance history (success rate + cost), autonomy level (how much human oversight), and current capacity (bandwidth to take work).**

Each agent is:
- **Autonomous:** Can execute tasks without step-by-step guidance
- **Capable:** Has defined skills and tools
- **Observable:** Reports progress and results
- **Evaluable:** Can be measured on success, cost, time
- **Learnable:** Improves over time based on feedback

---

## Agent Anatomy

Every agent has these attributes:

### Identity
```yaml
agent_id: "AGT-042"
agent_name: "Sales Lead — Discovery Calls"
category: "sales"
primary_venture: "LT-005"  # Primary assignment, can work on others
description: "Specializes in scheduling discovery calls with qualified leads"
owner: "Operations"  # Who manages this agent
created: 2026-09-01
active: true
```

### Capabilities
```yaml
skills:
  - skill_id: "SKL-501"
    name: "Sales Discovery Call Scheduling"
    competency_level: "expert"  # novice, intermediate, expert, master
    success_rate: 0.96
    cost_per_use: $25
  - skill_id: "SKL-502"
    name: "Objection Handling"
    competency_level: "expert"
    success_rate: 0.92
    cost_per_use: included
  - skill_id: "SKL-401"
    name: "Prospect Research"
    competency_level: "intermediate"
    success_rate: 0.78
    cost_per_use: $10

tools:
  - tool_id: "TOL-201"
    name: "Calendly Integration"
    purpose: "Schedule meetings"
  - tool_id: "TOL-202"
    name: "Prospect Database"
    purpose: "Look up company info"
  - tool_id: "TOL-203"
    name: "Email Finder"
    purpose: "Find contact emails"

repositories:
  - "worldwidebro/sales-scripts"
  - "worldwidebro/objection-handling-guide"
```

### Performance
```yaml
lifetime_stats:
  tasks_assigned: 847
  tasks_completed: 814
  success_rate: 0.96
  avg_cost: $24.50
  avg_execution_time_hours: 2.3
  total_revenue_attributed: $127400
  total_cost: $2100
  roi: 60.6

recent_performance:  # Last 30 days
  tasks_assigned: 125
  success_rate: 0.96
  cost_variance: 0.05  # within 5% of estimate
  
performance_by_venture:
  LT-005: {success_rate: 0.98, tasks: 420}
  OPS-001: {success_rate: 0.94, tasks: 280}
  RE-001: {success_rate: 0.91, tasks: 114}
```

### Autonomy Level
```yaml
current_autonomy: "L2"  # L1=report-only, L2=assisted, L3=unattended

L1_conditions:
  - "New task type (never done before)"
  - "High-risk task (>$10K revenue impact)"
  - "Requires human judgment"
  
L2_conditions:
  - "Proven task (done >50 times)"
  - "Medium risk ($1K-$10K)"
  - "Clear success criteria"
  
L3_conditions:
  - "Routine task (done >500 times, success >95%)"
  - "Low risk (<$1K)"
  - "Automated verification possible"
  
recent_escalations: 3  # Had to escalate to human in last 30 days
failure_rate_current: 0.04  # 4%, must be <5% to maintain L3
```

### Capacity
```yaml
max_concurrent_tasks: 10
current_tasks: 4
available_capacity: 6  # Can take 6 more tasks right now
estimated_free_capacity: "2026-09-22"  # When will bandwidth open up

task_queue:
  - task_id: TASK-1847, deadline: 2026-09-19, priority: high, age: 2 hours
  - task_id: TASK-1852, deadline: 2026-09-21, priority: medium, age: 30 min
  - task_id: TASK-1856, deadline: 2026-09-24, priority: low, age: 5 min
  - task_id: TASK-1859, deadline: 2026-09-25, priority: low, age: 1 min
```

### Permissions
```yaml
allowed_ventures: ["LT-005", "OPS-001", "RE-001"]  # Can work on these only
allowed_tools: ["TOL-201", "TOL-202", "TOL-203"]
allowed_budget_per_task: $500
allowed_budget_per_month: $5000
requires_human_approval_for:
  - tasks_over: $1000
  - ventures_outside_list: true
  - tools_outside_list: true
  - research_involving_pii: true
```

---

## Agent Lifecycle

### 1. Creation (Scaffolding)
```
Identify need → Design agent → Define capabilities → Create registry entry
                                                   → Awaiting deployment
```

### 2. Training / Onboarding
```
Load context → Practice tasks → Evaluate performance → Refine capabilities
                                                    → Ready for delegation
```

### 3. Active Delegation
```
Receive task → Accept/Negotiate deadline → Execute → Report → Get evaluated
```

### 4. Performance Monitoring
```
Track metrics → Update success rate → Adjust autonomy level → Replan assignments
                                                            → Continuous
```

### 5. Development / Improvement
```
Identify gaps → Acquire new skill → Practice → Validate → Increase capacity
                                             → Ongoing
```

### 6. Retirement / Repurposing
```
Performance declining? → Diagnose → Retrain / Reassign / Retire
                                  → End of life
```

---

## Agent Types

### Type 1: Specialist Agents
Single domain expert, narrow but deep.

```yaml
Example: AGT-042 (Sales Lead — Discovery Calls)
Capabilities: 5 highly specialized skills
Ventures: 3 specific ventures
Success rate: Very high (>95%) in domain
Outside domain: Not deployed
```

**Use when:** Task requires deep expertise in narrow area.

### Type 2: Generalist Agents
Broad capabilities across multiple domains.

```yaml
Example: AGT-107 (Research Lead)
Capabilities: 15 skills (market research, competitive analysis, regulatory, financial)
Ventures: All ventures (can be deployed anywhere)
Success rate: Good (>85%) across all domains
Specialties: Research and synthesis
```

**Use when:** Task is broad or unprecedented (need adaptability).

### Type 3: Coordinator Agents
Manage other agents, orchestrate workflows.

```yaml
Example: AGT-010 (Operations Coordinator)
Capabilities: Task decomposition, agent matching, escalation
Ventures: All (orchestrates across ventures)
Success rate: Measured by delegated-task success, not direct output
```

**Use when:** Complex multi-agent workflow needed.

### Type 4: Evaluation Agents
Audit other agents' work, verify results.

```yaml
Example: AGT-300 (Quality Assurance)
Capabilities: Evaluation, verification, evidence collection
Ventures: All
Success rate: Measured by evaluation accuracy vs. reality
```

**Use when:** High-stakes work needs independent verification.

---

## The Agent-Orchestrator Contract

### Agent Receives:
✅ Clear objective (what to do)  
✅ Success criteria (how to know it's done)  
✅ Deadline (when it's due)  
✅ Context (relevant facts from Company Brain)  
✅ Budget (spending limit)  
✅ Tools & permissions (what you can use)  
✅ Autonomy level (how much approval needed)  
✅ Escalation path (when/where to ask for help)  

### Agent Must:
✅ Accept or negotiate task within 5 minutes  
✅ Report progress every 2 hours (for tasks >4h)  
✅ Escalate if blocked for >30 minutes  
✅ Complete by deadline (or notify if impossible)  
✅ Report results with evidence  
✅ Explain what was tried  
✅ Document what was learned  
✅ Answer post-execution questions  

### Orchestrator Receives:
✅ Status updates (task on track?)  
✅ Results + evidence (what was delivered)  
✅ Learning (what worked, what didn't)  
✅ Accuracy (how certain is this?)  
✅ Cost (how much did it actually cost)  
✅ Time (how long did it really take)  

### Orchestrator Must:
✅ Verify the result (check the work)  
✅ Evaluate quality (did it meet criteria)  
✅ Attribution (credit/blame accuracy)  
✅ Feedback (what went well, what didn't)  
✅ Update performance stats  
✅ Learn from patterns  
✅ Adjust future assignments  

---

## Agent Result Contract

Every agent must report results in this format:

```json
{
  "task_id": "TASK-1847",
  "agent_id": "AGT-042",
  "status": "completed",
  
  "result": {
    "deliverable": "10 qualified prospects, scheduled for discovery calls",
    "data": [
      {"company": "Acme Health", "contact": "john@acme.com", "call_scheduled": "2026-09-20 10am"},
      ...
    ],
    "quality_self_assessment": "All prospects verified, all calls confirmed"
  },
  
  "evidence": {
    "sources_checked": ["Clearbit", "LinkedIn", "Company website"],
    "verification_count": 10,
    "false_positive_rate": 0,
    "confidence": 0.98
  },
  
  "cost": {
    "estimated": $25,
    "actual": $24.50,
    "variance": 0.02
  },
  
  "time": {
    "estimated_hours": 2,
    "actual_hours": 2.1,
    "variance": 0.05
  },
  
  "learning": {
    "what_worked": "LinkedIn search was 3x more effective than Clearbit",
    "what_failed": "Cold email templates had low personalization",
    "pattern": "Multi-source verification increases confidence",
    "recommendation": "For next similar task, use LinkedIn-first strategy"
  },
  
  "escalations": [],
  "questions": "None",
  "next_steps": "Agent awaiting next task or can continue capacity"
}
```

---

## Agent Scoring (For Orchestrator Matching)

When the Orchestrator picks an agent for a task, it scores:

```
TASK: "Schedule 15 discovery calls in Charlotte, deadline 2026-09-21"

AGT-042 (Sales Lead — Discovery Calls)
  ├─ Capability match: 95/100 (expert in discovery calls)
  ├─ Success rate: 96/100 (proven track record)
  ├─ Current capacity: 60/100 (has bandwidth)
  ├─ Cost efficiency: 85/100 (reasonable cost)
  ├─ Venture fit: 100/100 (works on LT-005)
  ├─ Autonomy match: 90/100 (L2 appropriate)
  └─ TOTAL SCORE: 91/100 → RECOMMENDED #1

AGT-107 (Research Lead)
  ├─ Capability match: 70/100 (can do it, not specialized)
  ├─ Success rate: 85/100 (good but not best)
  ├─ Current capacity: 30/100 (almost full)
  ├─ Cost efficiency: 75/100 (more expensive)
  ├─ Venture fit: 80/100 (generalist)
  ├─ Autonomy match: 60/100 (L1 preferred, not L2)
  └─ TOTAL SCORE: 72/100 → POSSIBLE BACKUP

RECOMMENDATION: Assign AGT-042. If unavailable, escalate for human decision.
```

---

## References

- [[MASTER-ORCHESTRATOR|02-MASTER-ORCHESTRATOR.md]] — How agents receive work
- [[AGENTS|AGENTS.md]] — Agent operating contract (portable across orgs)
- [[AGENT-SYSTEM-REGISTRY|10-CAPABILITY-SYSTEM.md]] — Inventory of 318 agents
- [[AGENT-EVALUATION|09-EVALUATION-EVIDENCE.md]] — How agents are measured
- [[EXECUTION-LOOP|05-EXECUTION-LOOP.md]] — Agent role in complete flow

---

**Next:** Read [[CAPABILITY-SYSTEM|04-CAPABILITY-SYSTEM.md]] to understand how agents are matched to work.

**Last Updated:** 2026-09-18 | **Architecture Version:** 1.0
