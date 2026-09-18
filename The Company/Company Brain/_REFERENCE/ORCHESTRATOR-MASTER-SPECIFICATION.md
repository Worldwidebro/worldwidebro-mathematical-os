# Orchestrator Prime Master Specification

**Version:** 1.0  
**Updated:** 2026-09-18  
**Status:** Production-Ready  
**Owner:** CP-033 (Execution) + CP-027 (Infrastructure)  
**Authority:** [[AGENTS|AGENTS.md]] + [[REALITY|REALITY.md]]

> **This is the single authoritative specification for Orchestrator Prime (AGT-001).** Consolidated from 7 scattered documents. All architectural decisions, schemas, APIs, and implementation details live here.
>
> **Supersedes:**
> - ORCHESTRATOR-PRIME-PRD.md
> - ORCHESTRATOR-PRIME-BACKEND-SCHEMA.md
> - ORCHESTRATOR-PRIME-CLAUDE-HAIKU-IMPLEMENTATION.md
> - ORCHESTRATOR-PRIME-QUICK-REFERENCE.md
> - And 3+ other fragmented specs in 20-DECISIONS/

---

## Executive Summary

**Orchestrator Prime (AGT-001)** is the master routing agent that discovers, selects, and coordinates autonomous task execution across the Company Brain's 318-agent network.

**The Question It Answers:** "Given any task, who is the best agent to execute it?"

**The Problem It Solves:**
- No unified agent discovery (318 agents, but no searchable inventory)
- Suboptimal routing (tasks go to wrong agents, wasting cost)
- No revenue attribution (execution happens, but $ is never tied to agent)
- Manual coordination (system operators manually assign tasks)
- No ROI visibility (impossible to measure agent profitability)

**By Dec 31, 2026:** Every task routes autonomously to the agent maximizing revenue, minimizing cost, with >90% success rate. The system self-learns.

---

## Part 1: Business Requirements

### Goals

| Goal | Target | Owner | Success Metric |
|------|--------|-------|-----------------|
| **Discover best agent** | 318 agents searchable + rankable | Agent Registry | 95%+ of tasks route to correct agent (top 3) |
| **Execute with ROI** | Task → execution → revenue | OmniRoute + Agents | 10x avg ROI per agent, >90% success |
| **Revenue attribution** | Every dollar tied to agent | Supabase + Triggers | 100% attributed, zero orphaned |
| **Autonomous routing** | L2/L3 after Week 1 | OrchestratorPrime | 30+ agents at L3 autonomy by Nov 15 |
| **Fast routing** | <2s task → suggested agents | API + Cache | p95 <2s, p99 <5s |
| **Performance visibility** | Agent leaderboard by ROI | Triggers + Stats | Top 10 + bottom 10 agents visible |

### Key Features

#### Feature 1: Task Classification (Claude Haiku)
**What:** Parse any task → extract intent, required capabilities, logic layers, autonomy level.

**How:** Task → Claude Haiku API → JSON classification in <500ms.

**Why:** Foundation for agent matching; teams understand what a task really requires before routing.

**Acceptance Criterion:** Accuracy >85% against LOGIC_LAYERS_REGISTRY.

#### Feature 2: Agent Discovery & Matching
**What:** Search 318 agents by capability/category/ROI; return ranked top 3.

**How:**
1. Load AGENTS_INVENTORY_318.yaml + Supabase
2. Filter by task intent + required capabilities
3. Score by: confidence (0-100), estimated ROI, cost, venture fit
4. Rank top 3 by ROI/cost ratio

**Why:** Users can't navigate 318 agents; they need instant ranked suggestions.

**Acceptance Criterion:** Best agent in top 1 > 80% of the time.

#### Feature 3: OmniRoute Execution
**What:** Execute selected task with best agent via OmniRoute.

**How:**
1. Pack task + context → OmniRoute payload
2. Call OmniRoute API (agent ID + tool bindings)
3. Monitor execution status
4. Handle failures, timeouts, retries

**Why:** Unified execution layer; agents don't need inter-agent invocation logic.

**Acceptance Criterion:** Success rate >90%, timeouts <5min, retry recovers 80%.

#### Feature 4: Revenue Attribution & Logging
**What:** Track every task: queued → executing → complete → revenue logged → agent stats updated.

**How:**
1. Create task_executions record (task queued)
2. Update status (execution progress)
3. On completion, parse output for revenue
4. Insert revenue_log entry
5. Trigger updates to agent_stats + venture_revenue_summary

**Why:** No guessing; every dollar tied to which agent earned it.

**Acceptance Criterion:** 100% of executed tasks have revenue_log; zero orphaned records.

---

## Part 2: System Architecture

### High-Level Flow

```
Task Submission
  ↓
[classifyTask() — Claude Haiku]
  ↓
Extract: intent, logic_layers, required_capabilities, autonomy_suggested
  ↓
[findBestAgent() — Agent Discovery]
  ↓
Query AGENTS_INVENTORY + score by ROI/cost
  ↓
Return ranked top 3 agents
  ↓
[executeTask() — OmniRoute]
  ↓
Pack task + context → OmniRoute payload
  ↓
Monitor execution (async webhook)
  ↓
[On Completion: attributeRevenue()]
  ↓
Parse result → extract revenue/cost
  ↓
Insert revenue_log → update agent_stats
  ↓
DONE
```

### Core Integration Points

| System | Role | What's Passed | Response |
|--------|------|---------------|-----------| 
| **Claude Haiku API** | Task classification | Task description + venture | TaskClassification (JSON) |
| **OmniRoute** | Execution engine | Agent ID + tool bindings + task context | async job_id + webhook |
| **Supabase** | State persistence | Task execution records + webhooks | updated rows + event IDs |
| **Qdrant** | Context retrieval | Vector queries for agent context | Top K similar past tasks |
| **Neo4j** | Agent discovery | Capability graph queries | Agent nodes + scores |

---

## Part 3: Implementation

### The Task Classification System (Claude Haiku)

#### Input: Task Object
```typescript
interface Task {
  id?: string;                           // Optional unique ID
  description: string;                   // Required: what to do
  venture: string;                       // Required: venture ID (e.g., "OPS-001")
  urgency?: "high" | "medium" | "low";   // Optional
  budget?: number;                       // Optional: USD
  revenue_target?: number;               // Optional: USD
}
```

#### Output: TaskClassification
```typescript
interface TaskClassification {
  intent: string;                        // "outreach" | "sales" | "support" | "analysis" | "admin" | "planning" | "other"
  logic_layers: string[];                // ["LL-009", "LL-010", ...] (LOGIC_LAYERS_REGISTRY refs)
  required_capabilities: string[];       // ["write-emails", "personalize", "track-opens"]
  autonomy_suggested: "L1" | "L2" | "L3"; // L1=report-only, L2=assisted, L3=unattended
}
```

#### System Prompt (Claude Haiku)
```
You are a task classification specialist. Analyze the task description and respond 
with ONLY valid JSON (no markdown, no explanation).

Extract:
- intent: primary action type
- logic_layers: relevant LOGIC_LAYERS_REGISTRY references (e.g., ["LL-009"])
- required_capabilities: specific skills needed
- autonomy_suggested: recommended autonomy level (L1/L2/L3)

Respond ONLY with a valid JSON object. No other text.
```

#### Implementation Pattern

```typescript
class OrchestratorPrime {
  private claudeClient: Anthropic | null = null;

  private getClaudeClient(): Anthropic {
    if (!this.claudeClient) {
      this.claudeClient = new Anthropic({
        apiKey: process.env.ANTHROPIC_API_KEY || "",
      });
    }
    return this.claudeClient;
  }

  async classifyTask(task: Task): Promise<TaskClassification> {
    try {
      const client = this.getClaudeClient();
      const response = await client.messages.create({
        model: "claude-haiku-4-5-20251001",
        max_tokens: 256,
        messages: [
          {
            role: "user",
            content: `Task: "${task.description}"\nVenture: ${task.venture}\nUrgency: ${task.urgency || "medium"}\n\nRespond with ONLY valid JSON.`,
          },
        ],
      });

      // Parse response
      const textContent = response.content[0];
      if (!textContent || textContent.type !== "text") {
        return this.getDefaultClassification(task);
      }

      const jsonMatch = textContent.text.match(/\{[\s\S]*\}/);
      if (!jsonMatch) {
        return this.getDefaultClassification(task);
      }

      const classification = JSON.parse(jsonMatch[0]);

      // Validate required fields
      if (
        !classification.intent ||
        !Array.isArray(classification.logic_layers) ||
        !Array.isArray(classification.required_capabilities) ||
        !classification.autonomy_suggested
      ) {
        return this.getDefaultClassification(task);
      }

      return classification as TaskClassification;
    } catch (error) {
      console.error("❌ Task classification failed:", error);
      return this.getDefaultClassification(task); // Fallback to keyword matching
    }
  }

  private getDefaultClassification(task: Task): TaskClassification {
    // Keyword matching fallback
    const desc = task.description.toLowerCase();
    let intent = "other";
    
    if (desc.includes("email")) intent = "outreach";
    else if (desc.includes("call") || desc.includes("schedule")) intent = "sales";
    else if (desc.includes("book") || desc.includes("meeting")) intent = "booking";
    else if (desc.includes("analyze")) intent = "analysis";

    return {
      intent,
      logic_layers: [],
      required_capabilities: [],
      autonomy_suggested: "L2",
    };
  }
}
```

#### Error Handling Modes

| Mode | Trigger | Response | Log |
|------|---------|----------|-----|
| **Normal** | Claude returns valid JSON | Full TaskClassification | ✅ Task classified |
| **No Text** | Claude returns empty response | Keyword matching fallback | ⚠️ No text in response |
| **Bad JSON** | JSON extraction fails | Keyword matching fallback | ⚠️ Could not extract JSON |
| **Invalid Structure** | Missing required fields | Keyword matching fallback | ⚠️ Invalid structure |
| **API Error** | 401/500/timeout | Keyword matching fallback | ❌ Failed to classify |

#### Performance Metrics
- **First call:** 200-500ms ($0.001)
- **Subsequent calls:** 200-500ms ($0.001 each)
- **100 classifications:** 20-50s ($0.10)
- **1,000 classifications:** 200-500s (~$1.00)

---

### Agent Discovery & Matching

#### Algorithm

```typescript
async findBestAgent(task: Task): Promise<MatchResult[]> {
  // 1. Classify task
  const classification = await this.classifyTask(task);

  // 2. Get ready agents from inventory
  const readyAgents = this.getReadyAgents(); // From AGENTS_INVENTORY_318.yaml

  // 3. Score each agent
  const scored = readyAgents.map((agent) => {
    let score = 0;

    // Match intent (40 points)
    if (classification.intent === agent.category) {
      score += 40;
    }

    // Match capabilities (20 points each)
    classification.required_capabilities.forEach((cap) => {
      if (agent.description.includes(cap)) {
        score += 20;
      }
    });

    // Match autonomy level (10 points)
    if (agent.autonomy_level === classification.autonomy_suggested) {
      score += 10;
    }

    // Venture fit (30 points)
    if (agent.ventures.includes(task.venture)) {
      score += 30;
    }

    // ROI factor (weighted by historical success)
    const rofactor = agent.roi_score || 0.5;
    score *= roifactor;

    return {
      agent_id: agent.id,
      agent_name: agent.name,
      confidence_score: score,
      estimated_roi: agent.estimated_roi,
      cost: agent.cost_per_invocation,
      roi_ratio: agent.estimated_roi / agent.cost_per_invocation,
    };
  });

  // 4. Sort by ROI/cost ratio
  return scored.sort((a, b) => b.roi_ratio - a.roi_ratio).slice(0, 3); // Top 3
}
```

---

### OmniRoute Execution

#### Execution Contract

```typescript
interface ExecutionRequest {
  agent_id: string;              // "AGT-NNN"
  agent_name: string;
  task_id: string;
  task_description: string;
  venture_id: string;
  budget: number;                // Max spend (USD)
  revenue_target: number;        // Expected revenue (USD)
  context: Record<string, any>;  // Task-specific context
  autonomy_level: "L1" | "L2" | "L3";
  timeout_seconds: number;       // Max execution time
}

interface ExecutionResult {
  job_id: string;                // OmniRoute async job ID
  status: "queued" | "running" | "completed" | "failed" | "timeout";
  agent_output: Record<string, any>;
  actual_revenue?: number;       // $ earned by this task
  cost_actual?: number;          // $ spent
  error?: string;
  completed_at?: timestamp;
}
```

#### Webhook Handler (Receives Result)

On OmniRoute completion, webhook posts to `/api/webhooks/orchestrator/task-completed`:

```json
{
  "webhook_event_id": "EVT-12345",
  "omniroute_job_id": "JOB-abc123",
  "status": "completed",
  "agent_output": {
    "result": "Successfully sent 20 emails",
    "actual_revenue": 500,
    "cost_actual": 25
  },
  "completed_at": "2026-09-18T14:32:00Z"
}
```

#### Handler Logic

1. Correlate webhook → task_executions by `omniroute_job_id`
2. Update `task_executions.status = completed`
3. Parse `agent_output` for revenue
4. Create `revenue_log` entry
5. Trigger `update_agent_stats()` + `update_venture_revenue_summary()`

---

## Part 4: Database Schema

### Supabase Tables

#### task_executions (Primary Record)

```sql
CREATE TABLE task_executions (
  -- Identity
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  task_id TEXT UNIQUE NOT NULL,
  
  -- Classification
  task_type VARCHAR(50) NOT NULL,
  domain VARCHAR(50) NOT NULL,
  priority INTEGER DEFAULT 5,
  
  -- Source & Routing
  source_venture_id VARCHAR(50),
  source_user_id UUID,
  requested_capability VARCHAR(100),
  
  -- OmniRoute Integration
  omniroute_job_id TEXT UNIQUE,
  omniroute_status VARCHAR(50) DEFAULT 'pending',
  omniroute_result JSONB,
  
  -- Execution Tracking
  assigned_agent_id VARCHAR(50),
  assigned_agent_name VARCHAR(255),
  execution_started_at TIMESTAMP,
  execution_completed_at TIMESTAMP,
  execution_duration_ms INTEGER,
  
  -- Webhook State
  webhook_received_at TIMESTAMP,
  webhook_event_id TEXT,
  webhook_processed BOOLEAN DEFAULT FALSE,
  webhook_processed_at TIMESTAMP,
  
  -- Result Tracking
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  error_code VARCHAR(50),
  error_message TEXT,
  retry_count INTEGER DEFAULT 0,
  max_retries INTEGER DEFAULT 3,
  
  -- Revenue Attribution
  attributed_revenue DECIMAL(10, 2),
  attributed_deal_id VARCHAR(50),
  revenue_attributed_at TIMESTAMP,
  
  -- Context & Metadata
  input_params JSONB NOT NULL,
  context_window_tokens INTEGER,
  model_used VARCHAR(50),
  cost_estimate DECIMAL(8, 4),
  cost_actual DECIMAL(8, 4),
  
  -- Audit
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  
  INDEX idx_task_type (task_type),
  INDEX idx_omniroute_job_id (omniroute_job_id),
  INDEX idx_assigned_agent (assigned_agent_id),
  INDEX idx_status (status),
  INDEX idx_webhook_processed (webhook_processed),
  INDEX idx_created_at (created_at DESC)
);
```

#### revenue_logs (Attribution Record)

```sql
CREATE TABLE revenue_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  task_execution_id UUID NOT NULL REFERENCES task_executions(id),
  
  agent_id VARCHAR(50) NOT NULL,
  venture_id VARCHAR(50),
  
  revenue_amount DECIMAL(10, 2) NOT NULL,
  cost_amount DECIMAL(10, 2),
  net_profit DECIMAL(10, 2) GENERATED ALWAYS AS (revenue_amount - cost_amount),
  
  source TEXT, -- "webhook", "manual_entry", "api_call"
  verified_by_user_id UUID,
  verified_at TIMESTAMP,
  
  created_at TIMESTAMP DEFAULT NOW(),
  
  INDEX idx_agent_id (agent_id),
  INDEX idx_venture_id (venture_id),
  INDEX idx_created_at (created_at DESC)
);
```

#### agent_stats (Leaderboard)

```sql
CREATE TABLE agent_stats (
  id UUID PRIMARY KEY,
  agent_id VARCHAR(50) UNIQUE NOT NULL,
  
  total_tasks_executed INTEGER DEFAULT 0,
  successful_tasks INTEGER DEFAULT 0,
  success_rate DECIMAL(4, 2),
  
  total_revenue DECIMAL(12, 2) DEFAULT 0,
  total_cost DECIMAL(12, 2) DEFAULT 0,
  total_profit DECIMAL(12, 2) GENERATED ALWAYS AS (total_revenue - total_cost),
  
  avg_revenue_per_task DECIMAL(10, 2),
  roi_multiple DECIMAL(8, 2),
  
  last_execution_at TIMESTAMP,
  updated_at TIMESTAMP DEFAULT NOW(),
  
  INDEX idx_roi_multiple (roi_multiple DESC),
  INDEX idx_success_rate (success_rate DESC)
);
```

---

## Part 5: API Reference

### POST /api/orchestrator/classify-task

**Purpose:** Classify a task using Claude Haiku.

**Request:**
```json
{
  "description": "Send cold emails to 20 prospects",
  "venture": "OPS-001",
  "urgency": "high",
  "budget": 500
}
```

**Response (200):**
```json
{
  "intent": "outreach",
  "logic_layers": ["LL-009", "LL-010"],
  "required_capabilities": ["write-emails", "personalize"],
  "autonomy_suggested": "L2"
}
```

**Latency:** 200-500ms | **Cost:** $0.001

---

### POST /api/orchestrator/find-best-agents

**Purpose:** Find top 3 agents for a task.

**Request:**
```json
{
  "task_id": "TASK-12345",
  "description": "Schedule discovery calls",
  "venture": "LT-005"
}
```

**Response (200):**
```json
{
  "top_agents": [
    {
      "rank": 1,
      "agent_id": "AGT-042",
      "agent_name": "Sales Lead — Discovery Calls",
      "confidence_score": 95,
      "estimated_roi": 2500,
      "cost": 25,
      "roi_ratio": 100
    },
    ...
  ]
}
```

---

### POST /api/orchestrator/execute-task

**Purpose:** Execute task with selected agent via OmniRoute.

**Request:**
```json
{
  "task_id": "TASK-12345",
  "agent_id": "AGT-042",
  "venture_id": "LT-005",
  "description": "Schedule 10 discovery calls",
  "budget": 500,
  "revenue_target": 5000,
  "autonomy_level": "L2"
}
```

**Response (202 Accepted):**
```json
{
  "omniroute_job_id": "JOB-abc123",
  "status": "queued",
  "webhook_url": "https://api.company-brain.internal/webhooks/orchestrator/task-completed"
}
```

**Webhook (POST to webhook_url on completion):**
```json
{
  "webhook_event_id": "EVT-12345",
  "omniroute_job_id": "JOB-abc123",
  "status": "completed",
  "agent_output": {
    "result": "Successfully scheduled 9 calls",
    "actual_revenue": 4500,
    "cost_actual": 22
  },
  "completed_at": "2026-09-18T14:32:00Z"
}
```

---

### GET /api/orchestrator/agent-stats

**Purpose:** Leaderboard of top/bottom agents by ROI.

**Query Params:**
- `limit=10` (top N agents)
- `sort_by=roi_multiple` (or success_rate, total_revenue)
- `venture_filter=LT-005` (optional)

**Response (200):**
```json
{
  "leaderboard": [
    {
      "rank": 1,
      "agent_id": "AGT-042",
      "agent_name": "Sales Lead",
      "total_tasks": 125,
      "success_rate": 0.96,
      "total_revenue": 125000,
      "total_cost": 2500,
      "roi_multiple": 50,
      "last_execution_at": "2026-09-18T14:22:00Z"
    }
  ]
}
```

---

## Part 6: Operational Runbook

### Normal Operation (Happy Path)

```
1. Task submitted via API → POST /api/orchestrator/classify-task
2. Claude Haiku classifies (200-500ms)
3. Call POST /api/orchestrator/find-best-agents
4. Neo4j queries capabilities + Supabase scores by ROI
5. Return top 3 ranked agents
6. User/system selects best agent
7. POST /api/orchestrator/execute-task
8. OmniRoute accepts job (status: queued)
9. Return async job_id + webhook_url
10. OmniRoute executes (background)
11. On completion, OmniRoute POSTs webhook
12. Handler correlates task_executions → updates status
13. Parse revenue from agent_output
14. Insert revenue_log → trigger agent_stats update
15. Dashboard shows updated leaderboard (live)
```

**Expected Duration:** 2-30 seconds (sync tasks) + OmniRoute async execution

---

### Fallback Modes

**If Claude Haiku fails:**
→ Keyword matching (email → outreach, call → sales, etc.)
→ Log warning + continue with lower confidence

**If OmniRoute times out (>5 min):**
→ Task marked failed, retry logic engages
→ Up to 3 retries with exponential backoff
→ After 3 failures, mark as terminal failure + alert

**If webhook never arrives:**
→ Polling fallback: `/api/orchestrator/task/{id}/poll` (every 30s)
→ After 1 hour of no response, mark as stale + alert operator

---

## Part 7: Monitoring & Alerts

### Key Metrics

| Metric | Target | Alert Threshold | Owner |
|--------|--------|------------------|-------|
| Task classification accuracy | >85% | <75% | Orchestrator |
| Agent discovery (best in top 1) | >80% | <60% | Agent Registry |
| Execution success rate | >90% | <80% | OmniRoute |
| Webhook response time | p95 <2s | >5s | API |
| Revenue attribution latency | <1s | >5s | Supabase |
| Agent leaderboard freshness | <5 min | >15 min | Triggers |

### Dashboard Queries

```sql
-- Accuracy (compare classification intent vs actual agent category)
SELECT 
  COUNT(*) as total_tasks,
  COUNT(CASE WHEN classification_intent = assigned_agent_category THEN 1 END) as correct,
  ROUND(COUNT(CASE WHEN classification_intent = assigned_agent_category THEN 1 END) * 100.0 / COUNT(*), 2) as accuracy_pct
FROM task_executions
WHERE created_at > NOW() - INTERVAL '24 hours'
  AND status = 'success';

-- Success rate by agent
SELECT 
  agent_id,
  COUNT(*) as total_tasks,
  COUNT(CASE WHEN status = 'success' THEN 1 END) as successful,
  ROUND(COUNT(CASE WHEN status = 'success' THEN 1 END) * 100.0 / COUNT(*), 2) as success_rate
FROM task_executions
WHERE created_at > NOW() - INTERVAL '7 days'
GROUP BY agent_id
ORDER BY success_rate DESC;

-- Revenue attribution pipeline
SELECT 
  status,
  COUNT(*) as count,
  ROUND(AVG(EXTRACT(EPOCH FROM (revenue_attributed_at - execution_completed_at))), 2) as avg_attribution_latency_sec
FROM task_executions
WHERE revenue_attributed_at IS NOT NULL
  AND created_at > NOW() - INTERVAL '24 hours'
GROUP BY status;
```

---

## Part 8: Known Limitations & Roadmap

### Current Limitations (v1.0)

- [ ] Single-agent routing (no multi-agent task orchestration)
- [ ] No feedback loop (agent scores static, not adaptive)
- [ ] No cost prediction (cost_estimate is placeholder)
- [ ] No context retrieval from Qdrant (vector context not integrated yet)
- [ ] No Neo4j graph querying (falling back to YAML inventory)

### Roadmap

| Phase | Date | Capability | Effort |
|-------|------|-----------|--------|
| **v1.0** | Sep 2026 | Basic routing, revenue attribution | DONE ✅ |
| **v1.1** | Oct 2026 | Qdrant context + Neo4j queries | 8h |
| **v1.2** | Nov 2026 | Adaptive scoring + feedback loop | 12h |
| **v1.3** | Dec 2026 | Cost prediction + budget enforcement | 10h |
| **v2.0** | Jan 2027 | Multi-agent orchestration | 20h |

---

## References

- [[AGENTS|AGENTS.md]] — Agent operating contract
- [[REALITY|REALITY.md]] — Truth ledger
- [[LOGIC_LAYERS_REGISTRY|_REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml]] — Layer reference
- [[AGENTS_INVENTORY_318|_REGISTRIES/AGENTS_INVENTORY_318.yaml]] — Agent catalog
- OmniRoute API: `http://100.87.214.70:20128/docs`

---

**Last Updated:** Sep 18, 2026 | **Next Review:** Oct 15, 2026
