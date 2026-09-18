# Orchestrator Prime — API Reference

**Version:** 1.0  
**Status:** Production-Ready  
**Base URL:** `http://localhost:20128` (local) or `https://api.company-brain.internal` (production)  
**Authentication:** Bearer token (Bitwarden: "OmniRoute — Company Brain")

> **Master API reference for Orchestrator Prime (AGT-001).** All endpoints for task classification, agent discovery, execution, and performance tracking.

---

## Quick Start

**Three-step workflow:**
1. **Classify** → `POST /api/orchestrator/classify-task` (understand what a task needs)
2. **Discover** → `POST /api/orchestrator/find-best-agents` (find top 3 agents)
3. **Execute** → `POST /api/orchestrator/execute-task` (run task with best agent)

**Result:** Async webhook notification on completion with revenue attribution.

---

## 1. Task Classification API

### POST /api/orchestrator/classify-task

**Purpose:** Parse any task description and extract its intent, required capabilities, and suggested autonomy level using Claude Haiku.

**Endpoint:**
```
POST /api/orchestrator/classify-task
Content-Type: application/json
Authorization: Bearer {token}
```

**Request:**
```json
{
  "task_id": "TASK-12345",
  "description": "Send cold emails to 20 prospects in Charlotte and schedule discovery calls",
  "venture": "LT-005",
  "urgency": "high",
  "budget": 500,
  "context": {
    "industry": "healthcare",
    "company_size": "SMB",
    "deal_size": "$50K-$200K"
  }
}
```

**Request Parameters:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| task_id | string | Yes | Unique task identifier |
| description | string | Yes | Natural language task description |
| venture | string | No | Which venture (LT-005, OPS-001, etc.) |
| urgency | enum | No | low, medium, high, critical |
| budget | number | No | Maximum spend allowed ($) |
| context | object | No | Additional context (JSON) |

**Response (200 OK):**
```json
{
  "task_id": "TASK-12345",
  "classification": {
    "intent": "outreach",
    "intent_confidence": 0.95,
    "logic_layers": ["LL-009-Discovery", "LL-010-Outreach"],
    "required_capabilities": ["Cold-Email-Writing", "Discovery-Calls", "Prospect-Research"],
    "required_skills": ["SKL-052", "SKL-053", "SKL-051"],
    "autonomy_suggested": "L2",
    "estimated_complexity": "medium",
    "risk_level": "low"
  },
  "classification_model": "claude-haiku-4.5-20251001",
  "latency_ms": 342,
  "cost_usd": 0.001,
  "timestamp": "2026-09-18T14:32:00Z"
}
```

**Response Fields:**
- `intent` — What is the task really about (outreach, research, analysis, etc.)
- `intent_confidence` — How confident (0-1) in this classification
- `logic_layers` — Which organizational logic layers apply (LL-001 to LL-250)
- `required_capabilities` — What capabilities needed (from CAPABILITY_REGISTRY)
- `required_skills` — Specific skills required (from SKILL_REGISTRY)
- `autonomy_suggested` — Suggested autonomy level (L1, L2, L3)

**Error Responses:**
```json
// 400 Bad Request
{
  "error": "INVALID_REQUEST",
  "message": "description field is required"
}

// 503 Service Unavailable
{
  "error": "CLAUDE_API_DOWN",
  "message": "Claude API unreachable; falling back to keyword matching"
}
```

**SLA:**
- **Latency:** 200-500ms (p95: <1s)
- **Cost:** $0.001 per call
- **Availability:** 99.9% (with fallback keyword matching)

---

## 2. Agent Discovery API

### POST /api/orchestrator/find-best-agents

**Purpose:** Find the top 3 best agents for a task based on capability matching, success rates, and ROI.

**Endpoint:**
```
POST /api/orchestrator/find-best-agents
Content-Type: application/json
Authorization: Bearer {token}
```

**Request:**
```json
{
  "task_id": "TASK-12345",
  "description": "Schedule 20 discovery calls",
  "required_capabilities": ["Cold-Email-Writing", "Discovery-Calls"],
  "venture": "LT-005",
  "budget": 500,
  "revenue_target": 5000,
  "venture_fit_required": true,
  "min_success_rate": 0.75
}
```

**Request Parameters:**
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| task_id | string | Required | Task identifier (from classify-task) |
| description | string | Required | Task description |
| required_capabilities | array | [] | Capabilities required |
| venture | string | No | Filter by venture |
| budget | number | No | Max cost allowed |
| revenue_target | number | No | Expected revenue if successful |
| venture_fit_required | bool | false | Only return agents authorized for this venture |
| min_success_rate | number | 0.0 | Minimum success rate (0-1) |

**Response (200 OK):**
```json
{
  "task_id": "TASK-12345",
  "search_criteria": {
    "required_capabilities": ["Cold-Email-Writing", "Discovery-Calls"],
    "venture": "LT-005"
  },
  "top_agents": [
    {
      "rank": 1,
      "agent_id": "AGT-042",
      "agent_name": "Sales Lead — Discovery Calls",
      "category": "sales",
      "autonomy_level": "L2",
      "confidence_score": 95,
      "reason_matched": "Expert in discovery calls, 96% success rate",
      
      "performance": {
        "success_rate": 0.96,
        "tasks_completed": 814,
        "avg_cost_per_task": 24.50,
        "total_revenue_attributed": 127400,
        "roi_multiple": 60.6
      },
      
      "cost_estimate": 25,
      "revenue_estimate": 5000,
      "estimated_net_profit": 4975,
      "roi_ratio": 199,
      
      "venture_fit": {
        "authorized": true,
        "past_performance_venture": {
          "success_rate": 0.98,
          "tasks_completed": 420
        }
      },
      
      "availability": {
        "current_capacity_used": 4,
        "max_concurrent_tasks": 10,
        "available_capacity": 6,
        "can_accept_now": true
      }
    },
    {
      "rank": 2,
      "agent_id": "AGT-107",
      "agent_name": "Research Lead",
      "category": "research",
      "confidence_score": 72,
      "reason_matched": "Can do discovery calls, but not specialized; 85% success rate",
      "cost_estimate": 35,
      "roi_ratio": 142,
      "availability": {
        "can_accept_now": false,
        "estimated_free_at": "2026-09-22T14:00:00Z"
      }
    },
    {
      "rank": 3,
      "agent_id": "AGT-300",
      "agent_name": "Quality Assurance",
      "category": "qa",
      "confidence_score": 45,
      "reason_matched": "Could execute as fallback; requires escalation",
      "cost_estimate": 50,
      "roi_ratio": 99,
      "availability": {
        "can_accept_now": true
      }
    }
  ],
  "scoring_algorithm": "composite(capability_match=0.4, success_rate=0.3, cost_efficiency=0.2, venture_fit=0.1)",
  "search_duration_ms": 245,
  "timestamp": "2026-09-18T14:32:30Z"
}
```

**Scoring Factors:**
- **Capability Match (40%):** Does agent have required skills?
- **Success Rate (30%):** Historical success on similar tasks
- **Cost Efficiency (20%):** ROI ratio (revenue ÷ cost)
- **Venture Fit (10%):** Has agent worked on this venture before?

**SLA:**
- **Latency:** p95 <500ms, p99 <2s
- **Accuracy:** Best agent in top 1 > 80% of the time
- **Availability:** 99.95%

---

## 3. Task Execution API

### POST /api/orchestrator/execute-task

**Purpose:** Execute a task with a selected agent via OmniRoute (async job).

**Endpoint:**
```
POST /api/orchestrator/execute-task
Content-Type: application/json
Authorization: Bearer {token}
```

**Request:**
```json
{
  "task_id": "TASK-12345",
  "agent_id": "AGT-042",
  "venture_id": "LT-005",
  "description": "Schedule 20 discovery calls with Charlotte healthcare prospects",
  "budget": 500,
  "revenue_target": 5000,
  "autonomy_level": "L2",
  "context": {
    "prospect_list_url": "s3://company-brain/prospects/charlotte-healthcare.csv",
    "script_template": "discovery-call-template-v2",
    "schedule_preference": "morning-appointments"
  },
  "webhook_url": "https://api.company-brain.internal/webhooks/orchestrator/task-completed"
}
```

**Request Parameters:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| task_id | string | Yes | Unique task ID |
| agent_id | string | Yes | Agent to execute (from find-best-agents) |
| venture_id | string | Yes | Venture context |
| description | string | Yes | Task description |
| budget | number | Yes | Max spend ($) |
| revenue_target | number | No | Expected revenue |
| autonomy_level | enum | No | L1, L2, or L3 |
| context | object | No | Task-specific context |
| webhook_url | string | No | Callback URL (async notification) |

**Response (202 Accepted):**
```json
{
  "task_id": "TASK-12345",
  "omniroute_job_id": "JOB-abc123xyz789",
  "status": "queued",
  "agent_id": "AGT-042",
  "agent_name": "Sales Lead — Discovery Calls",
  
  "execution_info": {
    "queued_at": "2026-09-18T14:33:00Z",
    "estimated_start": "2026-09-18T14:33:05Z",
    "estimated_completion": "2026-09-18T14:45:00Z",
    "timeout_seconds": 900,
    "max_retries": 3
  },
  
  "webhook": {
    "url": "https://api.company-brain.internal/webhooks/orchestrator/task-completed",
    "event_id_will_be": "EVT-TASK-12345-*"
  },
  
  "status_check_url": "GET /api/orchestrator/task/TASK-12345/status",
  "poll_interval_seconds": 30,
  
  "timestamp": "2026-09-18T14:33:00Z"
}
```

**Response Fields:**
- `omniroute_job_id` — Use this to track the job
- `status` — Currently: queued, running, completed, failed, timeout
- `webhook` — Will POST to this URL when done
- `status_check_url` — Fallback polling endpoint if webhook fails

**Webhook Notification (POST to webhook_url):**
```json
{
  "webhook_event_id": "EVT-TASK-12345-2026-09-18T14-45-00Z",
  "omniroute_job_id": "JOB-abc123xyz789",
  "task_id": "TASK-12345",
  "agent_id": "AGT-042",
  
  "status": "completed",
  "status_code": "success",
  
  "execution_timing": {
    "queued_at": "2026-09-18T14:33:00Z",
    "started_at": "2026-09-18T14:33:05Z",
    "completed_at": "2026-09-18T14:45:00Z",
    "duration_seconds": 720
  },
  
  "agent_output": {
    "result": "Successfully scheduled 18 of 20 discovery calls",
    "calls_scheduled": 18,
    "calls_failed": 2,
    "prospects_contacted": [
      {
        "company": "Charlotte Medical Center",
        "contact": "john@charlotte-med.com",
        "call_scheduled": "2026-09-22 10:00 AM"
      },
      "..."
    ]
  },
  
  "financials": {
    "revenue_actual": 4500,
    "cost_actual": 22.50,
    "profit_actual": 4477.50,
    "roi_multiple": 199.4
  },
  
  "evidence": {
    "confidence_score": 0.94,
    "verification_method": "call_confirmation_emails_sent",
    "sources_checked": 18
  },
  
  "next_steps": [
    {
      "recommendation": "Follow up on 2 failed calls tomorrow",
      "priority": "medium"
    }
  ]
}
```

**Webhook Fields:**
- `status` — success, failure, timeout, partial_success
- `agent_output` — What the agent actually delivered
- `financials` — Revenue/cost/profit attribution
- `evidence` — Confidence and verification method

**Error Responses:**
```json
// 400 Bad Request
{
  "error": "AGENT_NOT_AVAILABLE",
  "message": "AGT-042 is at capacity (6/10 tasks)"
}

// 402 Budget Exceeded
{
  "error": "BUDGET_EXCEEDED",
  "message": "Estimated cost ($35) exceeds budget ($25)"
}

// 503 Service Unavailable
{
  "error": "OMNIROUTE_DOWN",
  "message": "OmniRoute job queue unavailable"
}
```

**SLA:**
- **Queue Time:** <5 seconds to start execution
- **Task Timeout:** 15 minutes (configurable)
- **Webhook Timeout:** 10 seconds (with 3 retries)
- **Fallback Polling:** Every 30 seconds if webhook fails
- **Availability:** 99.5% (with fallback polling)

---

## 4. Agent Performance & Leaderboard API

### GET /api/orchestrator/agent-stats

**Purpose:** View agent performance metrics and leaderboard rankings.

**Endpoint:**
```
GET /api/orchestrator/agent-stats?limit=10&sort_by=roi_multiple&venture_filter=LT-005
Authorization: Bearer {token}
```

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| limit | integer | 10 | Return top N agents |
| sort_by | enum | roi_multiple | Sort by: roi_multiple, success_rate, total_revenue, total_tasks |
| venture_filter | string | None | Filter by specific venture |
| include_bottom | boolean | false | Include bottom N agents alongside top N |
| days | integer | 30 | Performance window (last N days) |

**Response (200 OK):**
```json
{
  "query": {
    "limit": 10,
    "sort_by": "roi_multiple",
    "venture_filter": "LT-005",
    "time_window": "last_30_days"
  },
  
  "leaderboard": [
    {
      "rank": 1,
      "agent_id": "AGT-042",
      "agent_name": "Sales Lead — Discovery Calls",
      "category": "sales",
      "autonomy_level": "L2",
      
      "performance": {
        "total_tasks": 125,
        "tasks_successful": 120,
        "success_rate": 0.96,
        "avg_execution_time_seconds": 145,
        "last_execution_at": "2026-09-18T14:22:00Z"
      },
      
      "financials": {
        "total_revenue": 125000,
        "total_cost": 2500,
        "total_profit": 122500,
        "avg_revenue_per_task": 1000,
        "avg_cost_per_task": 20,
        "roi_multiple": 50
      },
      
      "trend": {
        "roi_trend_7day": "+5%",
        "success_rate_trend_7day": "stable",
        "tasks_this_week": 15
      }
    },
    {
      "rank": 2,
      "agent_id": "AGT-107",
      "agent_name": "Research Lead",
      "total_tasks": 87,
      "success_rate": 0.85,
      "roi_multiple": 38,
      "total_revenue": 87000,
      "total_profit": 58900
    },
    "..."
  ],
  
  "summary": {
    "total_agents_ranked": 318,
    "avg_success_rate": 0.78,
    "avg_roi_multiple": 12.5,
    "top_10_avg_roi": 45.3
  },
  
  "generated_at": "2026-09-18T14:33:00Z",
  "refresh_frequency": "every_5_minutes"
}
```

**SLA:**
- **Latency:** p95 <500ms
- **Freshness:** Updated every 5 minutes
- **Availability:** 99.9%

---

## 5. Task Status & Polling API

### GET /api/orchestrator/task/{task_id}/status

**Purpose:** Fallback polling if webhook never arrives (or for status checks).

**Endpoint:**
```
GET /api/orchestrator/task/TASK-12345/status
Authorization: Bearer {token}
```

**Response (200 OK):**
```json
{
  "task_id": "TASK-12345",
  "omniroute_job_id": "JOB-abc123xyz789",
  "status": "running",
  
  "progress": {
    "percent_complete": 65,
    "items_processed": 13,
    "items_total": 20,
    "current_operation": "Contacting prospect #14"
  },
  
  "timing": {
    "queued_at": "2026-09-18T14:33:00Z",
    "started_at": "2026-09-18T14:33:05Z",
    "elapsed_seconds": 125,
    "estimated_remaining_seconds": 65
  },
  
  "next_poll_in_seconds": 30
}
```

---

## Error Handling & Fallbacks

### Global Error Codes

| Code | HTTP | Meaning | Fallback |
|------|------|---------|----------|
| INVALID_REQUEST | 400 | Malformed request | Return error, no retry |
| UNAUTHORIZED | 401 | Invalid/expired token | Re-authenticate |
| FORBIDDEN | 403 | Insufficient permissions | Escalate to admin |
| NOT_FOUND | 404 | Resource not found | Check task_id |
| CONFLICT | 409 | Task already executing | Check current status |
| RATE_LIMITED | 429 | Too many requests | Backoff + retry |
| SERVICE_UNAVAILABLE | 503 | Backend down | Retry with exponential backoff |

### Retry Logic

```
Transient errors (429, 503):
  → Retry 1: 1 second delay
  → Retry 2: 2 second delay
  → Retry 3: 4 second delay
  → After 3 retries: give up and alert operator

Permanent errors (400, 401, 403):
  → No retry; return error immediately
```

---

## Rate Limits

- **Classify Task:** 100 requests/minute
- **Find Best Agents:** 200 requests/minute
- **Execute Task:** 50 requests/minute
- **Query Stats:** 1000 requests/minute

---

## Authentication

**Bearer Token (from Bitwarden):**
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Token Expires:** 24 hours (refresh before expiry)

---

## Testing & Examples

### End-to-End Workflow

```bash
# 1. Classify task
curl -X POST http://localhost:20128/api/orchestrator/classify-task \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "task_id": "TASK-TEST-001",
    "description": "Send 20 cold emails to healthcare prospects"
  }'

# Response: {task_id, classification: {intent, capabilities, autonomy_suggested}}

# 2. Find best agents
curl -X POST http://localhost:20128/api/orchestrator/find-best-agents \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "task_id": "TASK-TEST-001",
    "description": "Send 20 cold emails to healthcare prospects",
    "venture": "LT-005"
  }'

# Response: {top_agents: [{rank, agent_id, confidence_score, roi_ratio}]}

# 3. Execute with best agent
curl -X POST http://localhost:20128/api/orchestrator/execute-task \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "task_id": "TASK-TEST-001",
    "agent_id": "AGT-042",
    "venture_id": "LT-005",
    "description": "Send 20 cold emails to healthcare prospects"
  }'

# Response: {omniroute_job_id, webhook_url} → webhook fires on completion
```

---

## References

- [[ORCHESTRATOR-MASTER-SPECIFICATION|Master Specification]] — Full implementation details
- [[ORCHESTRATOR-STATE-MACHINE|State Machine]] — Decision tree for each stage
- [[AGENTS|AGENTS.md]] — Agent operating contract
- OmniRoute API Docs: `http://100.87.214.70:20128/docs`

---

**Last Updated:** 2026-09-18 | **Version:** 1.0 | **Authority:** CP-033 (Execution)
