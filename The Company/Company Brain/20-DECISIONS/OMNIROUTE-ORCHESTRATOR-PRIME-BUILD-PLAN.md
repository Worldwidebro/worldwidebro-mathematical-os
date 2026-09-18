---
title: "OmniRoute Orchestrator Prime — Build Plan"
date: 2026-09-18
status: READY_TO_BUILD
effort: 10 hours
outcome: Wire all 318 agents through OmniRoute dispatch router
---

# OmniRoute Orchestrator Prime — Complete Build Plan

## VISION

Transform OmniRoute into the **Orchestrator Prime (AGT-001)** that routes every task to the best agent from the existing 318.

```
User Task → OmniRoute Orchestrator
  ├─ Parse intent + extract requirements
  ├─ Query AGENTS_INVENTORY_318.yaml
  ├─ Match task to best agent(s)
  ├─ Execute via OmniRoute tools
  ├─ Track execution + outcomes
  └─ Attribute revenue
```

## ARCHITECTURE

### Layer 1: Agent Discovery (Read-Only)
```typescript
// Load from AGENTS_INVENTORY_318.yaml
agents: Agent[] = [
  {
    id: "agent-revenue-cold-email-writer-001",
    name: "Cold Email Writer",
    domain: "14-CAPABILITIES",
    category: "sales",
    description: "...",
    capabilities: ["write-cold-emails", "track-opens", "handle-replies"],
    autonomy_level: "L2",
    status: "READY",
    cost_per_invocation: 0.25,
    estimated_revenue: 10000,
  },
  // ... 317 more
]
```

### Layer 2: Task Classification
```typescript
interface Task {
  id: string;
  description: string;  // "Send cold emails to 20 prospects"
  venture: string;      // "LT-005"
  urgency: "high" | "medium" | "low";
  budget?: number;      // Max cost to spend
  revenue_target?: number;  // Expected outcome value
}

// Classify into logic layers (from LOGIC_LAYERS_REGISTRY)
interface TaskClassification {
  intent: string;           // "outreach"
  logic_layers: string[];   // ["LOGIC-019", "LOGIC-049"]
  required_capabilities: string[];  // ["write-emails", "personalize"]
  autonomy_suggested: "L1" | "L2" | "L3";
}
```

### Layer 3: Agent Matching
```typescript
interface MatchResult {
  agent_id: string;
  agent_name: string;
  confidence_score: 0-100;  // How well does agent match task?
  cost: number;             // $ to execute
  estimated_revenue: number;
  rationale: string;        // Why this agent?
}

async function findBestAgent(task: Task): MatchResult[] {
  // 1. Parse task intent
  const classification = await classifyTask(task);
  
  // 2. Query AGENTS_INVENTORY_318.yaml for agents with required capabilities
  const candidates = agents.filter(a => 
    classification.logic_layers.some(ll => 
      a.capabilities.includes(ll)
    )
  );
  
  // 3. Score each candidate
  const scored = candidates.map(agent => ({
    agent_id: agent.id,
    agent_name: agent.name,
    confidence_score: calculateConfidence(agent, classification),
    cost: agent.cost_per_invocation,
    estimated_revenue: agent.estimated_revenue,
    rationale: `Matches ${classification.required_capabilities.join(", ")}`
  }));
  
  // 4. Return top 3, ranked by ROI
  return scored.sort((a, b) => 
    (b.estimated_revenue / b.cost) - (a.estimated_revenue / a.cost)
  ).slice(0, 3);
}
```

### Layer 4: Execution via OmniRoute
```typescript
async function executeTask(task: Task, agent: MatchResult): Promise<TaskResult> {
  // 1. Invoke agent via OmniRoute
  const execution = await omniroute.invoke({
    agent_id: agent.agent_id,
    task: task.description,
    context: {
      venture: task.venture,
      budget: task.budget,
      autonomy_level: agent.autonomy_level,
    },
    callbacks: {
      onProgress: (status) => logEvent("task_progress", status),
      onComplete: (result) => recordOutcome(result),
    }
  });
  
  // 2. Track execution
  await supabase.from("task_executions").insert({
    task_id: task.id,
    agent_id: agent.agent_id,
    started_at: new Date(),
    status: "in_progress",
    cost_estimated: agent.cost,
    revenue_estimated: agent.estimated_revenue,
  });
  
  // 3. Wait for completion
  const result = await execution.promise;
  
  // 4. Update execution record
  await supabase.from("task_executions").update({
    completed_at: new Date(),
    status: result.success ? "completed" : "failed",
    outcome: result.data,
    cost_actual: result.cost_actual,
  }).eq("task_id", task.id);
  
  return result;
}
```

### Layer 5: Revenue Attribution
```typescript
async function attributeRevenue(task_id: string, revenue: number) {
  // 1. Get execution record
  const execution = await supabase.from("task_executions")
    .select("agent_id, cost_actual")
    .eq("task_id", task_id)
    .single();
  
  // 2. Record revenue
  await supabase.from("revenue_log").insert({
    task_id,
    agent_id: execution.agent_id,
    venture_id: execution.venture_id,
    revenue,
    cost: execution.cost_actual,
    roi: revenue / execution.cost_actual,
    timestamp: new Date(),
  });
  
  // 3. Update agent stats
  await supabase.from("agent_stats").upsert({
    agent_id: execution.agent_id,
    tasks_completed: raw("tasks_completed + 1"),
    total_revenue: raw(`total_revenue + ${revenue}`),
    total_cost: raw(`total_cost + ${execution.cost_actual}`),
    roi_average: raw(`total_revenue / total_cost`),
  });
}
```

## BUILD PHASES (10 Hours Total)

### Phase 1: Scaffolding (2 hours)
- [ ] Create `orchestrator-prime.ts` entry point
- [ ] Create Supabase tables:
  - `task_queue` (incoming tasks)
  - `task_executions` (who ran it, cost, outcome)
  - `revenue_log` (revenue attribution)
  - `agent_stats` (per-agent metrics)
- [ ] Load and parse AGENTS_INVENTORY_318.yaml
- [ ] Verify OmniRoute connection

### Phase 2: Task Classification (2 hours)
- [ ] Implement `classifyTask()` using Claude Haiku
  - Parse intent (outreach, support, analysis, etc.)
  - Extract logic layers needed
  - Identify required capabilities
  - Suggest autonomy level
- [ ] Create LOGIC_LAYERS_REGISTRY mapping (if missing)
- [ ] Test with 5 sample tasks

### Phase 3: Agent Matching (2 hours)
- [ ] Implement `findBestAgent()` with capability matching
- [ ] Implement confidence scoring:
  - Direct capability match: +50 points
  - Domain relevance: +25 points
  - Success rate on similar tasks: +15 points
  - Cost efficiency: +10 points
- [ ] Implement ROI ranking
- [ ] Test matching with known task→agent pairs

### Phase 4: Execution & Tracking (2 hours)
- [ ] Wire OmniRoute invocation
- [ ] Implement progress tracking + logging
- [ ] Create Supabase event logger
- [ ] Build outcome recorder
- [ ] Test end-to-end execution with 1 agent

### Phase 5: Revenue Attribution (1 hour)
- [ ] Implement `attributeRevenue()` function
- [ ] Wire outcome hooks to revenue calculation
- [ ] Create agent ROI dashboard query
- [ ] Test attribution with sample execution

### Phase 6: API & Integration (1 hour)
- [ ] Create `/api/orchestrate` POST endpoint
  - Accept: { description, venture, budget, revenue_target }
  - Return: { task_id, suggested_agents, status }
- [ ] Create `/api/task/{id}/status` GET endpoint
- [ ] Create `/api/revenue/summary` dashboard endpoint
- [ ] Wire Make.com webhook trigger (optional)

## DEPLOYMENT CHECKLIST

- [ ] All 318 agents loaded and queryable
- [ ] Task classification working (5/5 test cases pass)
- [ ] Agent matching working (top agent correct for each task)
- [ ] OmniRoute execution tested (1 agent end-to-end)
- [ ] Revenue attribution tested (revenue recorded accurately)
- [ ] API endpoints live and tested
- [ ] Dashboard queries working
- [ ] Error handling in place (agent unavailable, OmniRoute timeout, etc.)
- [ ] Logging complete (task, execution, revenue)

## INTEGRATION POINTS

### OmniRoute
- **Connection:** localhost:20128 or 100.87.214.70:20128
- **Method:** HTTP or MCP (standard OmniRoute client)
- **Agent invocation:** `omniroute.invoke(agent_id, task_context)`

### Supabase
- **Database:** aipehhzlsmfxxzwceppd
- **Tables:** task_queue, task_executions, revenue_log, agent_stats
- **Realtime:** Use for live dashboard updates

### Make.com (Optional)
- **Trigger:** Webhook on new task (POST /api/orchestrate)
- **Action:** Invoke Orchestrator Prime via API
- **Outcome:** Send status updates to Slack

## SUCCESS CRITERIA

1. **Discovery:** Can find any agent from 318 by keyword (e.g., "cold email" → Cold Email Writer)
2. **Matching:** Selects correct agent for task (e.g., "send emails" → Agent-Revenue-Cold-Email-Writer-001)
3. **Execution:** Task executes via OmniRoute and completes successfully
4. **Attribution:** Revenue correctly attributed to agent + venture
5. **Observable:** Dashboard shows task status, agent performance, revenue flow
6. **Repeatable:** Same task type routes to same agent consistently

## QUICK START (After Build Complete)

```bash
# Send task via API
curl -X POST http://localhost:5173/api/orchestrate \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Send cold emails to 20 LT-005 prospects",
    "venture": "LT-005",
    "budget": 50,
    "revenue_target": 1500
  }'

# Returns:
{
  "task_id": "TASK-2026-09-18-001",
  "suggested_agents": [
    {
      "agent_id": "agent-revenue-cold-email-writer-001",
      "name": "Cold Email Writer",
      "confidence": 95,
      "cost": 0.25,
      "estimated_revenue": 1500
    }
  ],
  "status": "queued"
}

# Check status
curl http://localhost:5173/api/task/TASK-2026-09-18-001/status

# View revenue attribution
curl http://localhost:5173/api/revenue/summary?venture=LT-005
```

## TIMELINE

- **Today (Sep 18):** Finalize plan
- **Tomorrow (Sep 19):** Complete build (Phase 1-6)
- **Sep 20:** Integration testing + dashboard
- **Sep 21:** Deploy + first revenue agents live
- **Sep 22:** Expand to 10+ agents in Oct 2026 tier

## NOTES

- **Agent files location:** Most agents already defined in `.agents/agents/` or `16-AGENTS/`
- **Capabilities mapping:** Some agents may not have explicit capabilities listed yet—we'll add those during Phase 2
- **OmniRoute tools:** Can leverage OmniRoute's 110 existing tools for execution
- **Fallback:** If OmniRoute invocation fails, fall back to Make.com scenario execution
- **Cost tracking:** Use actual OmniRoute cost + Supabase logging cost for accurate ROI

---

**READY TO BUILD? Start with Phase 1 scaffold.**
