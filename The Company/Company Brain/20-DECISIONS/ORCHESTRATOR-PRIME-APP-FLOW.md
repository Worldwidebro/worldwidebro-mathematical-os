# Orchestrator Prime: App Flow & User Journeys

**Version:** 1.0  
**Date:** 2026-09-18  
**Status:** Ready for implementation  
**Audience:** Product team, frontend engineers, integration engineers

---

## Overview

Orchestrator Prime is an AI-powered task routing and execution system that classifies incoming tasks using Claude Haiku, matches them to the best available agent from a pool of 318+, executes via OmniRoute, and tracks revenue attribution.

This document shows the complete user journey from task submission through execution and revenue recording.

---

## 1. HAPPY PATH: Task Execution (Complete Flow)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        ORCHESTRATOR PRIME FLOW                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  USER SUBMITS TASK                                                      │
│  ↓                                                                      │
│  Task Input:                                                            │
│  ├─ description: "Send cold emails to 20 prospects"                    │
│  ├─ venture: "OPS-001"                                                 │
│  ├─ urgency: "high"                                                    │
│  ├─ budget: $500                                                       │
│  └─ revenue_target: $5,000                                             │
│                                                                         │
│  ┌────────────────────────────────────────────────────────────────┐   │
│  │  STEP 1: CLASSIFY TASK (Claude Haiku)                          │   │
│  │  ────────────────────────────────────────────────────────────  │   │
│  │  ✓ Extract intent ("outreach")                                │   │
│  │  ✓ Identify capabilities ("write-emails", "personalize")     │   │
│  │  ✓ Suggest autonomy level ("L2")                             │   │
│  │  ✓ Map to logic layers (["LL-009", "LL-010"])                │   │
│  │  ✓ Return TaskClassification object                          │   │
│  └────────────────────────────────────────────────────────────────┘   │
│  Classification Output:                                                 │
│  {                                                                      │
│    intent: "outreach",                                                 │
│    logic_layers: ["LL-009", "LL-010"],                                │
│    required_capabilities: ["write-emails", "personalize", "track-opens"],
│    autonomy_suggested: "L2"                                            │
│  }                                                                      │
│                                                                         │
│  ┌────────────────────────────────────────────────────────────────┐   │
│  │  STEP 2: FIND BEST AGENT                                       │   │
│  │  ────────────────────────────────────────────────────────────  │   │
│  │  ✓ Load 318 agents from AGENT_REGISTRY                         │   │
│  │  ✓ Score each agent:                                           │   │
│  │    - Intent match (40 pts)                                     │   │
│  │    - Capability match (20 pts × capability_count)              │   │
│  │    - Autonomy match (10 pts)                                   │   │
│  │    - ROI rating (20 pts)                                       │   │
│  │  ✓ Rank agents by score                                        │   │
│  │  ✓ Return top 3 candidates                                     │   │
│  └────────────────────────────────────────────────────────────────┘   │
│  Agent Match Output:                                                    │
│  [                                                                      │
│    {                                                                    │
│      agent_id: "agent-outreach-specialist-001",                       │
│      agent_name: "Outreach Specialist",                               │
│      score: 90,                                                        │
│      match_details: {                                                 │
│        intent_match: true,                                            │
│        capabilities: ["write-emails", "personalize"],                │
│        autonomy_level: "L2"                                           │
│      }                                                                │
│    },                                                                 │
│    ...                                                                │
│  ]                                                                     │
│                                                                         │
│  ┌────────────────────────────────────────────────────────────────┐   │
│  │  STEP 3: USER SELECTS AGENT (or auto-select top)               │   │
│  │  ────────────────────────────────────────────────────────────  │   │
│  │  Dashboard shows:                                              │   │
│  │  ┌─────────────────────────────────────────────────────┐      │   │
│  │  │ RECOMMENDED AGENTS FOR: "Send cold emails to..."    │      │   │
│  │  ├─────────────────────────────────────────────────────┤      │   │
│  │  │ [✓] Outreach Specialist (Score: 90)               │      │   │
│  │  │     Capabilities: Email, Personalization           │      │   │
│  │  │     Autonomy: L2 (Assisted)                         │      │   │
│  │  │     Est. ROI: $2,500 per campaign                   │      │   │
│  │  │     [SELECT]                                        │      │   │
│  │  │                                                     │      │   │
│  │  │ [ ] Sales Automation Agent (Score: 78)            │      │   │
│  │  │     Capabilities: Email, CRM Integration           │      │   │
│  │  │     Autonomy: L2 (Assisted)                         │      │   │
│  │  │     Est. ROI: $1,800 per campaign                   │      │   │
│  │  │     [SELECT]                                        │      │   │
│  │  └─────────────────────────────────────────────────────┘      │   │
│  │                                                                │   │
│  │  ✓ User clicks [SELECT] or auto-selects top agent            │   │
│  └────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌────────────────────────────────────────────────────────────────┐   │
│  │  STEP 4: EXECUTE TASK (via OmniRoute)                          │   │
│  │  ────────────────────────────────────────────────────────────  │   │
│  │  ✓ Invoke selected agent via OmniRoute HTTP endpoint           │   │
│  │    POST /route/agent/{agent_id}                               │   │
│  │    Body: {                                                    │   │
│  │      task_id: "task-20260918-001",                            │   │
│  │      description: "Send cold emails to 20 prospects",        │   │
│  │      venture: "OPS-001",                                     │   │
│  │      autonomy_level: "L2",                                   │   │
│  │      budget: 500,                                            │   │
│  │      revenue_target: 5000                                    │   │
│  │    }                                                          │   │
│  │  ✓ Receive execution_id                                       │   │
│  │  ✓ Monitor status polling: PENDING → RUNNING → SUCCESS/FAIL  │   │
│  └────────────────────────────────────────────────────────────────┘   │
│  Execution Output:                                                      │
│  {                                                                      │
│    execution_id: "exec-20260918-001",                                 │
│    agent_id: "agent-outreach-specialist-001",                         │
│    status: "RUNNING",                                                 │
│    started_at: "2026-09-18T14:00:00Z",                                │
│    task_id: "task-20260918-001"                                       │
│  }                                                                      │
│                                                                         │
│  ┌────────────────────────────────────────────────────────────────┐   │
│  │  STEP 5: MONITOR EXECUTION                                     │   │
│  │  ────────────────────────────────────────────────────────────  │   │
│  │  Dashboard shows live progress:                               │   │
│  │  ┌─────────────────────────────────────────────────────┐      │   │
│  │  │ EXECUTION IN PROGRESS                              │      │   │
│  │  ├─────────────────────────────────────────────────────┤      │   │
│  │  │ Agent: Outreach Specialist                         │      │   │
│  │  │ Status: ⏳ RUNNING                                 │      │   │
│  │  │ Progress: 15/20 emails sent                        │      │   │
│  │  │ Elapsed: 2 minutes 30 seconds                      │      │   │
│  │  │ Est. Completion: 5 minutes                         │      │   │
│  │  │                                                     │      │   │
│  │  │ Open Rates:                                        │      │   │
│  │  │ ├─ Sent: 15                                        │      │   │
│  │  │ ├─ Opened: 8 (53%)                                 │      │   │
│  │  │ ├─ Clicked: 3 (20%)                                │      │   │
│  │  │ └─ Replied: 1 (7%)                                 │      │   │
│  │  │                                                     │      │   │
│  │  │ [Pause] [Cancel] [View Details]                    │      │   │
│  │  └─────────────────────────────────────────────────────┘      │   │
│  └────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌────────────────────────────────────────────────────────────────┐   │
│  │  STEP 6: RECEIVE EXECUTION OUTCOME                             │   │
│  │  ────────────────────────────────────────────────────────────  │   │
│  │  ✓ Agent completes task                                        │   │
│  │  ✓ OmniRoute returns ExecutionResult:                          │   │
│  │    - outcome: "success"                                        │   │
│  │    - metrics: {sent: 20, opened: 12, clicked: 3, replied: 2} │   │
│  │    - cost_used: $47.50                                         │   │
│  │    - revenue_generated: $2,500 (estimated from replies)       │   │
│  │    - timestamp: "2026-09-18T14:05:00Z"                        │   │
│  │                                                                │   │
│  │  Dashboard shows completion:                                  │   │
│  │  ┌─────────────────────────────────────────────────────┐      │   │
│  │  │ ✅ EXECUTION COMPLETED                              │      │   │
│  │  ├─────────────────────────────────────────────────────┤      │   │
│  │  │ Emails Sent: 20/20                                  │      │   │
│  │  │ Open Rate: 60% (12/20)                              │      │   │
│  │  │ Click Rate: 15% (3/20)                              │      │   │
│  │  │ Reply Rate: 10% (2/20)                              │      │   │
│  │  │                                                     │      │   │
│  │  │ Cost: $47.50 / Budget: $500 ✓                      │      │   │
│  │  │ Revenue: $2,500 / Target: $5,000 (50% achieved)    │      │   │
│  │  │                                                     │      │   │
│  │  │ [View Details] [Export Report] [Add Feedback]       │      │   │
│  │  └─────────────────────────────────────────────────────┘      │   │
│  └────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌────────────────────────────────────────────────────────────────┐   │
│  │  STEP 7: RECORD EXECUTION & ATTRIBUTE REVENUE                  │   │
│  │  ────────────────────────────────────────────────────────────  │   │
│  │  ✓ Write to task_executions table:                             │   │
│  │    {                                                           │   │
│  │      task_id: "task-20260918-001",                            │   │
│  │      agent_id: "agent-outreach-specialist-001",               │   │
│  │      execution_id: "exec-20260918-001",                       │   │
│  │      venture: "OPS-001",                                      │   │
│  │      status: "success",                                       │   │
│  │      started_at: "2026-09-18T14:00:00Z",                     │   │
│  │      completed_at: "2026-09-18T14:05:00Z",                   │   │
│  │      cost_used: 47.50,                                        │   │
│  │      metrics: {...}                                           │   │
│  │    }                                                           │   │
│  │                                                                │   │
│  │  ✓ Write to revenue_log table:                                 │   │
│  │    {                                                           │   │
│  │      execution_id: "exec-20260918-001",                       │   │
│  │      agent_id: "agent-outreach-specialist-001",               │   │
│  │      venture: "OPS-001",                                      │   │
│  │      revenue_type: "email_replies",                           │   │
│  │      revenue_amount: 2500,                                    │   │
│  │      attribution_method: "reply_count_x_500",                 │   │
│  │      recorded_at: "2026-09-18T14:05:30Z"                     │   │
│  │    }                                                           │   │
│  │                                                                │   │
│  │  ✓ Trigger agent_stats update:                                 │   │
│  │    UPDATE agents SET                                          │   │
│  │      executions_count = executions_count + 1,                 │   │
│  │      success_count = success_count + 1,                       │   │
│  │      total_revenue = total_revenue + 2500,                    │   │
│  │      avg_cost = (total_cost + 47.50) / executions_count,     │   │
│  │      roi = total_revenue / total_cost                        │   │
│  │    WHERE agent_id = "agent-outreach-specialist-001"          │   │
│  │                                                                │   │
│  │  ✓ Update venture_revenue_summary:                             │   │
│  │    UPDATE ventures SET                                        │   │
│  │      mtd_revenue = mtd_revenue + 2500,                        │   │
│  │      ytd_revenue = ytd_revenue + 2500,                        │   │
│  │      agent_executions = agent_executions + 1,                 │   │
│  │      last_execution = "2026-09-18T14:05:00Z"                 │   │
│  │    WHERE venture_id = "OPS-001"                               │   │
│  └────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ✅ TASK COMPLETE                                                      │
│  Revenue recorded, agent stats updated, venture dashboard reflects    │
│  new metrics in real-time.                                            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. TASK CLASSIFICATION FLOW

Claude Haiku analyzes the task and extracts operational metadata in ~200-500ms.

```
INPUT: Task Description
├─ Description: "Send cold emails to 20 prospects in Charlotte, NC"
├─ Venture: "OPS-001"
├─ Urgency: "high"
├─ Budget: $100
└─ Revenue Target: $1,500

         ↓

SYSTEM PROMPT (Claude Haiku)
"You are a task classification specialist. Analyze the task description
and respond with ONLY valid JSON (no markdown, no explanation).

Extract:
- intent: primary action type
  (outreach | sales | support | analysis | admin | planning | other)
- logic_layers: relevant LOGIC_LAYERS_REGISTRY references
  (e.g., ["LL-009", "LL-010"])
- required_capabilities: specific capabilities needed
  (e.g., ["write-emails", "personalize"])
- autonomy_suggested: suggested autonomy level
  (L1=report-only | L2=assisted | L3=unattended)"

         ↓

CLAUDE HAIKU API CALL
POST https://api.anthropic.com/v1/messages
{
  "model": "claude-haiku-4-5-20251001",
  "max_tokens": 256,
  "system": "[system prompt above]",
  "messages": [{
    "role": "user",
    "content": "Task: 'Send cold emails to 20 prospects in Charlotte, NC'\nVenture: OPS-001\nUrgency: high\nBudget: $100\n\nRespond ONLY with JSON object (no other text)."
  }]
}

         ↓

CLAUDE HAIKU RESPONSE (in ~200-500ms)
{
  "intent": "outreach",
  "logic_layers": ["LL-009", "LL-010"],
  "required_capabilities": ["write-emails", "personalize", "track-opens"],
  "autonomy_suggested": "L2"
}

         ↓

VALIDATION & ERROR HANDLING

┌─ Check response has text content
│  └─ NO → Fallback to keyword matching
│     (email → outreach, call → sales, book → booking, etc.)
│
├─ Extract JSON from response
│  └─ FAIL → Fallback to keyword matching
│
├─ Validate structure
│  ├─ intent: non-empty string ✓
│  ├─ logic_layers: array ✓
│  ├─ required_capabilities: array ✓
│  └─ autonomy_suggested: L1|L2|L3 ✓
│  └─ INVALID → Fallback to keyword matching
│
└─ Return TaskClassification object

         ↓

OUTPUT: TaskClassification
{
  intent: "outreach",
  logic_layers: ["LL-009", "LL-010"],
  required_capabilities: ["write-emails", "personalize", "track-opens"],
  autonomy_suggested: "L2"
}

         ↓

FALLBACK (if API fails)
Keyword matching on task.description:
- "email" in description → intent: "outreach"
- "call" in description → intent: "sales"
- "book" in description → intent: "booking"
- "demo" in description → intent: "demo"
- "data" in description → intent: "analysis"
- etc.

Returns valid TaskClassification with best-guess intent.

LOGS:
✅ Task classified: intent="outreach", autonomy="L2" [200ms]
⚠️ Could not extract JSON from Claude response, falling back to keyword matching
❌ Failed to classify task with Claude: Timeout
```

**Performance:**
- Model: claude-haiku-4-5-20251001
- Tokens: 256 max (sufficient for JSON response)
- Latency: 200–500ms typical
- Cost: ~$0.001 per classification
- Fallback rate target: <5%

---

## 3. AGENT MATCHING FLOW

Scores 318 agents by intent, capability, autonomy, and ROI to find the best match.

```
INPUT: TaskClassification
{
  intent: "outreach",
  required_capabilities: ["write-emails", "personalize", "track-opens"],
  autonomy_suggested: "L2"
}

         ↓

LOAD AGENTS
├─ Read AGENT_REGISTRY.yaml (318 agents)
├─ Filter for status="READY"
├─ Load agent metadata:
│  ├─ agent_id
│  ├─ category (intent)
│  ├─ description
│  ├─ autonomy_level
│  ├─ roi_rating
│  └─ capabilities (derived from description)
└─ Result: 250+ ready agents

         ↓

SCORE EACH AGENT
For each agent:

  Score = 0
  
  ┌─ INTENT MATCH (40 points max)
  │  if (agent.category === classification.intent) {
  │    score += 40
  │  }
  │
  ├─ CAPABILITY MATCH (20 points per matching capability)
  │  classification.required_capabilities.forEach((cap) => {
  │    if (agent.description.toLowerCase().includes(cap)) {
  │      score += 20
  │    }
  │  })
  │  max: 3 capabilities × 20 = 60 points
  │
  ├─ AUTONOMY MATCH (10 points)
  │  if (agent.autonomy_level === classification.autonomy_suggested) {
  │    score += 10
  │  }
  │
  ├─ ROI RATING (20 points max)
  │  score += (agent.roi_rating / 5) × 20
  │  (assumes roi_rating is 1–5 scale)
  │
  └─ MAX POSSIBLE SCORE: 130 points

EXAMPLE SCORING:
┌─────────────────────────────────────────────────────┐
│ Agent: Outreach Specialist                          │
├─────────────────────────────────────────────────────┤
│ Intent Match (outreach = outreach): +40             │
│ Capabilities:                                       │
│   ├─ write-emails: FOUND → +20                     │
│   ├─ personalize: FOUND → +20                      │
│   └─ track-opens: FOUND → +20                      │
│ Autonomy Match (L2 = L2): +10                      │
│ ROI Rating (4.8/5): +19.2 ≈ +19                   │
│                                                     │
│ TOTAL SCORE: 40 + 60 + 10 + 19 = 129 / 130        │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Agent: Sales Automation Agent                       │
├─────────────────────────────────────────────────────┤
│ Intent Match (sales ≠ outreach): +0                │
│ Capabilities:                                       │
│   ├─ write-emails: FOUND → +20                     │
│   ├─ personalize: NOT FOUND → +0                   │
│   └─ track-opens: NOT FOUND → +0                   │
│ Autonomy Match (L2 = L2): +10                      │
│ ROI Rating (4.2/5): +16.8 ≈ +17                   │
│                                                     │
│ TOTAL SCORE: 0 + 20 + 10 + 17 = 47 / 130         │
└─────────────────────────────────────────────────────┘

         ↓

RANK AGENTS
agents.sort((a, b) => b.score - a.score)

         ↓

RETURN TOP 3
[
  {
    rank: 1,
    agent_id: "agent-outreach-specialist-001",
    agent_name: "Outreach Specialist",
    score: 129,
    match_details: {
      intent_match: true,
      capabilities: ["write-emails", "personalize", "track-opens"],
      autonomy_level: "L2",
      roi_rating: 4.8
    },
    estimated_roi: "$2,500–$5,000 per campaign"
  },
  {
    rank: 2,
    agent_id: "agent-email-marketing-001",
    agent_name: "Email Marketing Specialist",
    score: 105,
    match_details: {
      intent_match: true,
      capabilities: ["write-emails", "personalize"],
      autonomy_level: "L2",
      roi_rating: 4.1
    },
    estimated_roi: "$1,500–$3,000 per campaign"
  },
  {
    rank: 3,
    agent_id: "agent-sales-automation-001",
    agent_name: "Sales Automation Agent",
    score: 78,
    match_details: {
      intent_match: false,
      capabilities: ["write-emails"],
      autonomy_level: "L2",
      roi_rating: 4.2
    },
    estimated_roi: "$1,200–$2,000 per campaign"
  }
]

         ↓

DASHBOARD DISPLAYS TOP 3 + SELECTION UI
User sees ranked list with scores and estimated ROI,
clicks [SELECT] on preferred agent.
```

**Scoring Rationale:**
- Intent match is most important (40 pts) — wrong category = wrong tool
- Capabilities are critical (20 pts each) — can't do the job without them
- Autonomy alignment matters (10 pts) — L1 agents for reports, L2 for assisted, L3 for autonomous
- ROI rating (20 pts) — reward high-performing agents

---

## 4. EXECUTION FLOW

Agent execution via OmniRoute with status monitoring and outcome collection.

```
USER SELECTS AGENT
(clicks [SELECT] on Outreach Specialist)

         ↓

INVOKE AGENT VIA OMNIROUTE
POST http://100.87.214.70:20128/route/agent/{agent_id}

REQUEST BODY:
{
  "task_id": "task-20260918-001",
  "venture_id": "OPS-001",
  "description": "Send cold emails to 20 prospects in Charlotte, NC",
  "urgency": "high",
  "budget": 500,
  "revenue_target": 5000,
  "autonomy_level": "L2",
  "context": {
    "prospects_file": "s3://bucket/prospects-charlotte.csv",
    "email_template": "cold-outreach-v2",
    "followup_delay_hours": 48
  }
}

         ↓

OMNIROUTE RETURNS EXECUTION ID
{
  "execution_id": "exec-20260918-001",
  "agent_id": "agent-outreach-specialist-001",
  "task_id": "task-20260918-001",
  "status": "PENDING",
  "created_at": "2026-09-18T14:00:00Z",
  "estimated_completion": "2026-09-18T14:05:00Z"
}

         ↓

MONITOR STATUS (Poll every 5 seconds)
GET http://100.87.214.70:20128/executions/{execution_id}

         ↓

STATUS PROGRESSION

┌─────────────────────────────────────────────────────┐
│ Time  │ Status     │ Progress  │ Metrics             │
├─────────────────────────────────────────────────────┤
│ 14:00 │ PENDING    │ 0/20      │ Initializing...     │
│ 14:01 │ RUNNING    │ 5/20      │ 5 emails sent       │
│ 14:02 │ RUNNING    │ 12/20     │ 8 opened, 2 clicked │
│ 14:03 │ RUNNING    │ 18/20     │ 10 opened, 3 clicked│
│ 14:04 │ RUNNING    │ 20/20     │ 12 opened, 3 clicked│
│ 14:05 │ SUCCESS    │ 20/20     │ 12 opened, 2 replies│
└─────────────────────────────────────────────────────┘

         ↓

DASHBOARD LIVE UPDATES
┌──────────────────────────────────────────────┐
│ EXECUTION IN PROGRESS                       │
│ Agent: Outreach Specialist                 │
│ Status: ⏳ RUNNING                          │
├──────────────────────────────────────────────┤
│ Progress: 20/20 emails sent (100%)          │
│ Elapsed: 4:32                               │
│ Opens: 12 (60%)                             │
│ Clicks: 3 (15%)                             │
│ Replies: 2 (10%)                            │
│                                              │
│ Cost Used: $40 / $500 budget (8%)          │
│ Revenue Est: $1,000 (2 replies × $500)     │
│                                              │
│ [View Details] [Download Report] [Pause]   │
└──────────────────────────────────────────────┘

         ↓

RECEIVE FINAL OUTCOME
GET http://100.87.214.70:20128/executions/{execution_id}

RESPONSE:
{
  "execution_id": "exec-20260918-001",
  "agent_id": "agent-outreach-specialist-001",
  "task_id": "task-20260918-001",
  "status": "SUCCESS",
  "started_at": "2026-09-18T14:00:00Z",
  "completed_at": "2026-09-18T14:05:00Z",
  "duration_seconds": 300,
  
  "metrics": {
    "emails_sent": 20,
    "emails_opened": 12,
    "open_rate": 0.60,
    "clicks": 3,
    "click_rate": 0.15,
    "replies": 2,
    "reply_rate": 0.10
  },
  
  "financial": {
    "cost_used": 40.00,
    "cost_per_email": 2.00,
    "roi_estimate": 1.25,
    "revenue_generated": 1000.00
  },
  
  "output": {
    "sent_emails_file": "s3://bucket/executions/exec-001/emails-sent.csv",
    "opens_file": "s3://bucket/executions/exec-001/opens.csv",
    "replies_file": "s3://bucket/executions/exec-001/replies.csv",
    "summary_report": "s3://bucket/executions/exec-001/summary.pdf"
  }
}

         ↓

DASHBOARD SHOWS COMPLETION
┌──────────────────────────────────────────────┐
│ ✅ EXECUTION COMPLETED                      │
├──────────────────────────────────────────────┤
│ Duration: 4 minutes 20 seconds              │
│                                              │
│ EMAIL METRICS:                              │
│ ├─ Sent: 20/20 (100%)                      │
│ ├─ Opened: 12 (60%)                        │
│ ├─ Clicked: 3 (15%)                        │
│ └─ Replied: 2 (10%)                        │
│                                              │
│ FINANCIAL:                                  │
│ ├─ Cost Used: $40 (8% of budget)          │
│ ├─ Revenue Generated: $1,000               │
│ ├─ ROI: 25× (1000/40)                     │
│ └─ Outcome: ✅ PROFITABLE                  │
│                                              │
│ [View Report] [Download Data] [Feedback]   │
└──────────────────────────────────────────────┘
```

---

## 5. REVENUE ATTRIBUTION FLOW

Execution outcome → Revenue recorded → Agent stats updated → Dashboard reflects metrics.

```
EXECUTION COMPLETE
status: "SUCCESS"
metrics: {
  emails_sent: 20,
  emails_opened: 12,
  replies: 2
}

         ↓

CALCULATE REVENUE
Revenue Attribution Model:

  Method 1: REPLY COUNT
  ───────────────────
  revenue = replies × $500  (per reply value)
  revenue = 2 × $500 = $1,000

  Method 2: ENGAGEMENT RATE
  ────────────────────────
  revenue = (open_rate × $200) + (click_rate × $300)
  revenue = (0.60 × $200) + (0.15 × $300) = $120 + $45 = $165
  
  [Use the higher value: $1,000]

  Method 3: VENTURE-SPECIFIC ALLOCATION
  ───────────────────────────────────────
  if venture.type === "staffing":
    revenue = verified_leads × $500
  if venture.type === "logistics":
    revenue = opened_rate × venture.value_per_lead

         ↓

WRITE TO DATABASE TABLES

1. TASK_EXECUTIONS TABLE
   ──────────────────────
   INSERT INTO task_executions VALUES (
     task_id: "task-20260918-001",
     agent_id: "agent-outreach-specialist-001",
     execution_id: "exec-20260918-001",
     venture_id: "OPS-001",
     description: "Send cold emails to 20 prospects in Charlotte, NC",
     status: "success",
     autonomy_level: "L2",
     started_at: "2026-09-18T14:00:00Z",
     completed_at: "2026-09-18T14:05:00Z",
     duration_seconds: 300,
     cost_used: 40.00,
     budget: 500.00,
     metrics: {
       "emails_sent": 20,
       "emails_opened": 12,
       "open_rate": 0.60,
       "clicks": 3,
       "click_rate": 0.15,
       "replies": 2,
       "reply_rate": 0.10
     },
     metadata: {
       "classification": {
         "intent": "outreach",
         "autonomy_suggested": "L2"
       }
     },
     created_at: "2026-09-18T14:05:30Z"
   )
   
   → Supabase task_executions table updated
   → GraphQL API now returns this execution

2. REVENUE_LOG TABLE
   ──────────────────
   INSERT INTO revenue_log VALUES (
     execution_id: "exec-20260918-001",
     agent_id: "agent-outreach-specialist-001",
     venture_id: "OPS-001",
     revenue_type: "email_replies",
     revenue_amount: 1000.00,
     attribution_method: "reply_count_x_500",
     confidence: 0.95,
     notes: "2 replies × $500/reply",
     recorded_at: "2026-09-18T14:05:30Z"
   )
   
   → Revenue log created
   → Finance dashboard can now query this revenue

3. AGENT_STATS TABLE (UPDATE)
   ──────────────────────────
   UPDATE agents SET
     executions_count = executions_count + 1,              -- 47 → 48
     success_count = success_count + 1,                   -- 46 → 47
     failure_count = failure_count + 0,                   -- stays 1
     total_revenue = total_revenue + 1000.00,             -- $45,320 → $46,320
     total_cost = total_cost + 40.00,                     -- $895 → $935
     avg_cost = total_cost / executions_count,            -- $895/47 → $935/48 = $19.48
     avg_revenue_per_execution = total_revenue / executions_count,
     roi = total_revenue / total_cost,                    -- $46,320/$935 = 49.5×
     last_execution_id = "exec-20260918-001",
     last_execution_at = "2026-09-18T14:05:00Z",
     success_rate = success_count / executions_count      -- 47/48 = 97.9%
   WHERE agent_id = "agent-outreach-specialist-001"
   
   → Agent dashboard updated
   → Agent ranking changes (ROI improves)
   → Agent appears higher in future matches

4. VENTURE_REVENUE_SUMMARY TABLE (UPDATE)
   ──────────────────────────────────────
   UPDATE ventures SET
     mtd_revenue = mtd_revenue + 1000.00,                 -- $12,540 → $13,540
     ytd_revenue = ytd_revenue + 1000.00,                 -- $345,200 → $346,200
     agent_executions_count = agent_executions_count + 1, -- 23 → 24
     agent_generated_revenue = 1000.00,
     last_execution_id = "exec-20260918-001",
     last_execution_at = "2026-09-18T14:05:00Z",
     agent_roi_avg = agent_generated_revenue / agent_costs,
     updated_at = "2026-09-18T14:05:30Z"
   WHERE venture_id = "OPS-001"
   
   → Venture dashboard updated
   → Revenue metrics reflect new total
   → Performance trends update in real-time

         ↓

TRIGGER DOWNSTREAM EFFECTS

AGENT DISCOVERY & ROUTING:
  Agent scoring in next task now includes:
  - Higher ROI (49.5× vs 48.1× before)
  - Better success rate (97.9% vs 97.8%)
  - More recent execution (just now)
  
  → Agent moves up in future ranking for similar tasks

VENTURE PERFORMANCE:
  OPS-001 dashboard now shows:
  - MTD revenue: $13,540 (updated from $12,540)
  - Agent-generated: $1,000 this month
  - Best performing agent: Outreach Specialist
  
  → Founder sees real-time revenue growth
  → Decision to expand agent budget / scale campaigns

FINANCIAL RECONCILIATION:
  Finance team sees in GL:
  - Revenue GL: +$1,000 (email campaign revenue)
  - Cost GL: -$40 (agent execution cost)
  - Net profit: +$960
  
  → Bank deposit matches GL within 24 hours
  → No reconciliation issues

         ↓

DASHBOARD STATE UPDATES
┌──────────────────────────────────────────────────────────┐
│ ORCHESTRATOR PRIME DASHBOARD                             │
├──────────────────────────────────────────────────────────┤
│ LAST EXECUTION                                           │
│ Agent: Outreach Specialist                              │
│ Task: Send cold emails to 20 prospects                 │
│ Status: ✅ SUCCESS                                       │
│ ROI: 25× ($1,000 revenue / $40 cost)                    │
│ Completed: 14:05 (4 min 20 sec)                        │
│                                                          │
│ VENTURE METRICS (OPS-001)                               │
│ ├─ This Month: $13,540                                  │
│ ├─ Agent-Generated: $1,000 (7%)                         │
│ └─ Best Agent: Outreach Specialist (ROI: 49.5×)        │
│                                                          │
│ AGENT PERFORMANCE                                        │
│ Outreach Specialist:                                    │
│ ├─ Executions: 48                                       │
│ ├─ Success Rate: 97.9%                                  │
│ ├─ Total Revenue: $46,320                               │
│ ├─ Avg Cost: $19.48                                     │
│ └─ ROI: 49.5×                                           │
│                                                          │
│ [View Full Report] [Export Data] [Schedule Next]        │
└──────────────────────────────────────────────────────────┘
```

---

## 6. ERROR PATHS & Recovery

### Error 1: No Matching Agent Found

```
CLASSIFICATION COMPLETE
intent: "synthesize_complex_research"  ← rare intent

         ↓

AGENT MATCHING
Score all 318 agents by intent match...
❌ NO AGENT with category="synthesize_complex_research"
❌ All scores below 30 (threshold for match)

         ↓

DECISION POINT
┌─ Is autonomy_level = "L1" (report only)?
│  └─ YES: Accept low-confidence match, show warning
│  └─ NO: Proceed to fallback
│
└─ Fallback Options:
   ├─ Option 1: Show user the top 3 agents by capability match
   │            (even with low scores)
   │            "No perfect match. Here are your best options."
   │
   ├─ Option 2: Suggest human intervention
   │            "This task requires custom work. Contact team leads."
   │
   └─ Option 3: Defer to General Agent (L1 only)
                Suggest a routing assistant to decompose task

         ↓

UI SHOWS FALLBACK
┌───────────────────────────────────────────┐
│ ⚠️  NO PERFECT MATCH FOUND                │
├───────────────────────────────────────────┤
│ Your task requires specialized skills     │
│ we don't have in our agent pool yet.      │
│                                            │
│ CLOSEST MATCHES:                          │
│ 1. Research Analyst (Score: 28/100)      │
│    Specialties: Data analysis, synthesis  │
│    Autonomy: L1 (report-only)             │
│                                            │
│ 2. Content Strategist (Score: 24/100)    │
│    Specialties: Research, writing         │
│    Autonomy: L1 (report-only)             │
│                                            │
│ RECOMMENDATIONS:                          │
│ • Decompose into smaller tasks            │
│ • Use option 1 (Research Analyst)         │
│   and add human review step               │
│ • Contact support to onboard new agent    │
│                                            │
│ [Use Option 1] [Decompose] [Contact]     │
└───────────────────────────────────────────┘

         ↓

LOG
❌ No agent found for intent "synthesize_complex_research"
   Classified task as L1 (report-only)
   Suggested fallback: Research Analyst (score: 28)
   Action: Show user options, require manual selection
```

### Error 2: OmniRoute Execution Fails

```
AGENT SELECTED
Agent: Outreach Specialist
Task: Send cold emails

         ↓

INVOKE AGENT VIA OMNIROUTE
POST /route/agent/agent-outreach-specialist-001
⚠️  Connection timeout (30s)

         ↓

ERROR HANDLING
┌─ Retry Logic:
│  ├─ Attempt 1: TIMEOUT → Wait 2s, retry
│  ├─ Attempt 2: TIMEOUT → Wait 5s, retry
│  └─ Attempt 3: TIMEOUT → FAIL
│
└─ Fallback:
   ├─ Is agent simply offline? (check health)
   │  └─ YES: Use backup agent, log incident
   │  └─ NO: Proceed to error UI
   │
   └─ Show user error + recovery options

         ↓

UI SHOWS ERROR
┌────────────────────────────────────────────┐
│ ❌ EXECUTION FAILED                         │
├────────────────────────────────────────────┤
│ Agent: Outreach Specialist                │
│ Error: Connection timeout (OmniRoute)     │
│ Time: 14:00:15 UTC                        │
│                                             │
│ RECOVERY OPTIONS:                          │
│ 1. Retry with same agent                  │
│    [Retry] (wait 5s for recovery)         │
│                                             │
│ 2. Use backup agent (Email Marketing)     │
│    [Switch Agent]                         │
│                                             │
│ 3. Contact support                        │
│    [Get Help]                             │
│                                             │
│ 4. Defer until OmniRoute recovers         │
│    [Defer] (auto-retry in 5 min)         │
└────────────────────────────────────────────┘

         ↓

LOG & INCIDENT
❌ Execution failed for agent-outreach-specialist-001
   OmniRoute error: Connection timeout
   Incident type: INFRASTRUCTURE
   Severity: HIGH (revenue-impacting)
   Alert: Ops team notified
   Status: Monitoring (recovery in progress)
```

### Error 3: Revenue Calculation Error

```
EXECUTION COMPLETE
metrics: {
  replies: 2,
  opens: 12,
  clicks: 3
}

         ↓

CALCULATE REVENUE
revenue = replies × $500 = 2 × $500 = $1,000

         ↓

WRITE TO DATABASE
INSERT INTO revenue_log...
❌ DATABASE ERROR: Constraint violation
   "venture_id OPS-001 not found"

         ↓

ERROR HANDLING
┌─ Check venture_id exists
│  ├─ Retry INSERT with venture_id lookup
│  └─ FAIL → Use fallback
│
├─ Create revenue_pending record (not finalized)
│  ├─ Mark as "unreconciled"
│  ├─ Set flag: "requires_manual_review"
│  └─ Store full metrics for later processing
│
└─ Alert finance team
   "Revenue record requires verification"

         ↓

UI SHOWS WARNING
┌────────────────────────────────────────────┐
│ ⚠️  EXECUTION COMPLETED WITH WARNING       │
├────────────────────────────────────────────┤
│ Agent: Outreach Specialist                │
│ Task: Send cold emails (20)               │
│ Result: ✅ SUCCESS (emails sent)          │
│                                             │
│ ⚠️  REVENUE PENDING:                       │
│ Expected revenue: $1,000                   │
│ Status: Waiting for verification          │
│ Action: Finance team will review          │
│                                             │
│ WHAT HAPPENED:                             │
│ Execution succeeded, but venture data     │
│ validation failed. Revenue is held         │
│ pending manual review.                     │
│                                             │
│ [View Metrics] [Contact Finance]          │
└────────────────────────────────────────────┘

         ↓

LOG
⚠️  Execution succeeded, but revenue record failed
    execution_id: exec-20260918-001
    metrics_collected: replies=2, opens=12, clicks=3
    estimated_revenue: $1,000
    error: venture_id "OPS-001" validation failed
    status: revenue_pending (requires_manual_review)
    assigned_to: finance_team
    timestamp: 2026-09-18T14:05:35Z
```

---

## 7. DASHBOARD STATE AT EACH STEP

### Step 0: Task Input Screen

```
┌─────────────────────────────────────────────────────────┐
│ ORCHESTRATOR PRIME                                      │
│ ─ Describe your task                                    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│ TASK DESCRIPTION (required)                            │
│ ┌──────────────────────────────────────────────────────┐
│ │ Send cold emails to 20 prospects in Charlotte, NC   │
│ │ and track opens/clicks for follow-up calls          │
│ │                                                      │
│ │                                                      │
│ │                                                      │
│ └──────────────────────────────────────────────────────┘
│                                                          │
│ VENTURE (required)                                      │
│ ┌──────────────────────────────────────────────────────┐
│ │ [dropdown: Select venture...]                        │
│ │ ├─ OPS-001 (Staffing)                               │
│ │ ├─ LT-005 (Logistics)                               │
│ │ ├─ RE-001 (Real Estate)                             │
│ │ └─ ...                                               │
│ └──────────────────────────────────────────────────────┘
│                                                          │
│ URGENCY (optional)                                      │
│ ◉ Low   ○ Medium   ◉ High   ○ ASAP                     │
│                                                          │
│ BUDGET (optional)                                       │
│ ┌──────────────────────────────────────────────────────┐
│ │ $500                                                 │
│ └──────────────────────────────────────────────────────┘
│                                                          │
│ REVENUE TARGET (optional)                              │
│ ┌──────────────────────────────────────────────────────┐
│ │ $5,000                                               │
│ └──────────────────────────────────────────────────────┘
│                                                          │
│                     [Submit Task] [Clear]               │
└─────────────────────────────────────────────────────────┘
```

### Step 1: Classifying Task

```
┌─────────────────────────────────────────────────────────┐
│ ORCHESTRATOR PRIME                                      │
│ ─ Analyzing your task...                                │
├─────────────────────────────────────────────────────────┤
│                                                          │
│ Task: Send cold emails to 20 prospects in Charlotte   │
│                                                          │
│ ⏳ CLASSIFYING...                                       │
│                                                          │
│ Analyzing with Claude Haiku...                         │
│ Estimated time: 200–500ms                              │
│                                                          │
│                                                          │
│ [████████░░░░░░░░░░] 40% complete                     │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Step 2: Agent Matching

```
┌─────────────────────────────────────────────────────────┐
│ ORCHESTRATOR PRIME                                      │
│ ─ Finding best agents...                                │
├─────────────────────────────────────────────────────────┤
│                                                          │
│ Classification Result:                                  │
│ Intent: Outreach                                       │
│ Capabilities: write-emails, personalize, track-opens  │
│ Autonomy: L2 (Assisted)                                │
│                                                          │
│ Searching 318 agents for best match...                │
│ Scoring by: Intent, Capabilities, Autonomy, ROI      │
│                                                          │
│ [████████████████░░] 80% complete                     │
│                                                          │
│ Found: 156 candidate agents                           │
│ Ranking by score...                                    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Step 3: Agent Selection

```
┌──────────────────────────────────────────────────────────┐
│ ORCHESTRATOR PRIME                                       │
│ ─ Select an agent to execute your task                   │
├──────────────────────────────────────────────────────────┤
│                                                           │
│ RECOMMENDED AGENTS FOR "Send cold emails..."             │
│                                                           │
│ [✓] Outreach Specialist                                │
│     Match Score: 129/130 (99%)                          │
│     ├─ Intent: outreach ✓                              │
│     ├─ Capabilities: write-emails, personalize,        │
│     │              track-opens ✓                       │
│     ├─ Autonomy: L2 (Assisted) ✓                       │
│     ├─ Success Rate: 97.9%                             │
│     ├─ Total Revenue Generated: $46,320                │
│     ├─ Avg ROI: 49.5×                                  │
│     └─ Est. This Campaign: $2,500–$5,000              │
│     [SELECT]                                            │
│                                                           │
│ [ ] Email Marketing Specialist                         │
│     Match Score: 105/130 (81%)                         │
│     ├─ Intent: outreach ✓                              │
│     ├─ Capabilities: write-emails, personalize ✓      │
│     ├─ Autonomy: L2 (Assisted) ✓                       │
│     ├─ Success Rate: 93.2%                             │
│     ├─ Total Revenue Generated: $28,940                │
│     ├─ Avg ROI: 31.2×                                  │
│     └─ Est. This Campaign: $1,500–$3,000              │
│     [SELECT]                                            │
│                                                           │
│ [ ] Sales Automation Agent                            │
│     Match Score: 78/130 (60%)                          │
│     ├─ Intent: sales ✗                                │
│     ├─ Capabilities: write-emails ✓                   │
│     ├─ Autonomy: L2 (Assisted) ✓                       │
│     ├─ Success Rate: 88.7%                             │
│     ├─ Total Revenue Generated: $15,670                │
│     ├─ Avg ROI: 22.1×                                  │
│     └─ Est. This Campaign: $1,200–$2,000              │
│     [SELECT]                                            │
│                                                           │
│ Need a different agent? [Show More] [Custom Search]    │
└──────────────────────────────────────────────────────────┘
```

### Step 4: Execution in Progress

```
┌──────────────────────────────────────────────────────────┐
│ ORCHESTRATOR PRIME                                       │
│ ─ Execution in progress...                               │
├──────────────────────────────────────────────────────────┤
│                                                           │
│ AGENT: Outreach Specialist                              │
│ STATUS: ⏳ RUNNING                                      │
│                                                           │
│ Progress: 15/20 emails sent (75%)                      │
│ Elapsed: 2 minutes 30 seconds                          │
│ Est. Completion: 3 minutes 30 seconds                  │
│                                                           │
│ ┌──────────────────────────────────────────────────────┐
│ │ REAL-TIME METRICS                                    │
│ ├──────────────────────────────────────────────────────┤
│ │ Sent:    ████████████████░░ 15/20                   │
│ │ Opened:  █████████░░░░░░░░░ 8/15 (53%)              │
│ │ Clicked: ████░░░░░░░░░░░░░░ 2/15 (13%)              │
│ │ Replied: ░░░░░░░░░░░░░░░░░░ 0/15 (0%)               │
│ │                                                      │
│ │ Cost Used: $30 / $500 budget (6%)                   │
│ │ Est. Revenue: $500 (1 expected reply @ $500)        │
│ └──────────────────────────────────────────────────────┘
│                                                           │
│ [Pause] [Cancel] [View Details]                        │
│                                                           │
│ Last Update: 14:02:30 UTC                              │
└──────────────────────────────────────────────────────────┘
```

### Step 5: Execution Completed

```
┌──────────────────────────────────────────────────────────┐
│ ORCHESTRATOR PRIME                                       │
│ ─ Execution completed                                    │
├──────────────────────────────────────────────────────────┤
│                                                           │
│ ✅ AGENT: Outreach Specialist                          │
│ ✅ STATUS: SUCCESS                                      │
│                                                           │
│ Duration: 4 minutes 20 seconds                         │
│                                                           │
│ FINAL METRICS                                            │
│ ┌──────────────────────────────────────────────────────┐
│ │ Emails Sent:    20/20 (100%)                        │
│ │ Opened:         12/20 (60%)                         │
│ │ Clicked:        3/20 (15%)                          │
│ │ Replied:        2/20 (10%)                          │
│ └──────────────────────────────────────────────────────┘
│                                                           │
│ FINANCIAL SUMMARY                                        │
│ ┌──────────────────────────────────────────────────────┐
│ │ Cost Used: $40 / $500 budget (8%) ✓                │
│ │ Est. Revenue: $1,000 (2 replies × $500) ✓           │
│ │ ROI: 25× ($1,000 / $40)                             │
│ │ Outcome: PROFITABLE ✓                               │
│ └──────────────────────────────────────────────────────┘
│                                                           │
│ VENTURE IMPACT (OPS-001)                                │
│ ├─ Monthly Revenue: $13,540 (↑ $1,000 this hour)      │
│ ├─ Agent-Generated: +$1,000                            │
│ └─ Best Agent: Outreach Specialist (ROI: 49.5×)       │
│                                                           │
│ [Download Report] [View Details] [Schedule Next]      │
│ [Add Feedback] [Share Results]                         │
└──────────────────────────────────────────────────────────┘
```

---

## Summary

**Orchestrator Prime User Journey:**

1. **Input** → User submits task with venture, urgency, budget
2. **Classify** → Claude Haiku extracts intent, capabilities, autonomy (200–500ms)
3. **Match** → Score 318 agents by intent, capability, autonomy, ROI
4. **Select** → User picks best agent from top 3 recommendations
5. **Execute** → OmniRoute invokes agent, streams live metrics
6. **Monitor** → Dashboard shows real-time progress (sent, opened, clicked, replied)
7. **Complete** → Agent finishes, returns outcome and metrics
8. **Attribute** → Revenue calculated, recorded to task_executions + revenue_log
9. **Update** → Agent stats + venture summary refresh in real-time
10. **Dashboard** → Founder sees new revenue metrics immediately

**Key Design Decisions:**
- Claude Haiku for classification (fast + cheap, with keyword fallback)
- Scoring formula weights intent (40) > capability (60) > autonomy (10) > ROI (20)
- Live streaming of metrics during execution for transparency
- Revenue attribution via reply count ($500/reply) with alternative models
- Comprehensive error handling with fallback agents + manual review options
- All states logged for audit trail + observability

---

**File:** `/Users/acebless/Documents/The Company/Company Brain/20-DECISIONS/ORCHESTRATOR-PRIME-APP-FLOW.md`  
**Created:** 2026-09-18  
**Status:** Ready for frontend implementation
