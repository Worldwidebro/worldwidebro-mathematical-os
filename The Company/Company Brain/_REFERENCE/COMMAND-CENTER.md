# Command Center — Real-Time Orchestrator Monitoring

**Purpose:** How to view the Master Orchestrator's 13-stage loop in action. Real-time visibility into task execution, agent discovery, revenue attribution.

**Status:** Operational | **Last Updated:** 2026-09-18 | **Audience:** Operators, executives, on-call engineers

---

## One-Sentence Summary

The Command Center is **three dashboards** showing **what the Orchestrator is doing right now** (task execution), **who's handling it** (agent capacity), and **what the Company Brain knows** (context search).

---

## Three Core Dashboards

### Dashboard 1: Task Execution (The Loop)
**What:** Real-time view of tasks flowing through the 13-stage Orchestrator loop

**Why:** Detect stalled tasks, see agent assignments, understand throughput, catch failures early

**Key Metrics:**
- Tasks in each stage (OBSERVE → LEARN → UPDATEBRAIN)
- Task success rate (%) — target > 95%
- Average latency per stage (target < 500ms)
- Queue depth (tasks waiting)
- Error rate (%)

**How to Read It:**
```
OBSERVE (22 tasks)    → 5ms avg
UNDERSTAND (18 tasks) → 8ms avg
DISCOVER (15 tasks)   → 120ms avg (Neo4j queries)
PLAN (8 tasks)        → 15ms avg
DECOMPOSE (6 tasks)   → 10ms avg
...
SUCCESS (1,247 total)
FAILED (3 total)
```

**Red Flags:**
- ❌ Tasks stuck in one stage > 5 min → see [[ORCHESTRATOR-TASK-STALLED]]
- ❌ DISCOVER stage empty, only OBSERVE/UNDERSTAND busy → agent discovery broken → see [[NEO4J-DISCOVERY-BROKEN]]
- ❌ Database tasks hitting timeouts → see [[DATABASE-POOL-EXHAUSTED]]
- ❌ Success rate < 80% → systemic issue, escalate to L2

**Green Flags:**
- ✅ Smooth flow through all 13 stages
- ✅ Success rate > 95%
- ✅ No tasks stuck > 5 min
- ✅ Average latency < 500ms per stage
- ✅ Error rate < 2%

---

### Dashboard 2: Agent Capacity (The Workforce)
**What:** Real-time view of agent availability, utilization, performance, and ROI

**Why:** Understand workforce bottlenecks, spot underutilized agents, catch performance degradation

**Key Metrics:**
- Agents assigned (actively executing)
- Agents available (idle, ready)
- Agents at capacity (100% utilized)
- Success rate per agent (top 10, bottom 10)
- ROI multiple per agent (revenue/cost ratio)
- Revenue attribution lag (revenue recorded vs. task completion)

**How to Read It:**
```
AGENTS EXECUTION:
- Total agents: 318
- Actively executing: 42 (13%)
- Idle / available: 276 (87%)
- At capacity: 0 (healthy)

PERFORMANCE LEADERBOARD (top 5 this hour):
1. AGT-047 (Sales Discovery)      | Success: 96% | ROI: 3.2x
2. AGT-089 (Lead Generation)      | Success: 94% | ROI: 2.8x
3. AGT-012 (Email Outreach)       | Success: 91% | ROI: 2.5x
4. AGT-156 (Data Analysis)        | Success: 89% | ROI: 2.1x
5. AGT-201 (Capability Matching)  | Success: 88% | ROI: 1.9x

REVENUE ATTRIBUTION:
- Tasks completed: 157
- Revenue recorded: 151 (96% attribution rate)
- Attribution lag: 2.3 min (target < 5 min)
```

**Red Flags:**
- ❌ Many agents at capacity (> 20% at 100%) → need more agents or longer timeouts
- ❌ Revenue attribution lag > 5 min → see [[WEBHOOK-HANDLER-DOWN]]
- ❌ Agent success rate < 60% → possible misconfiguration or timeout too short → see [[ORCHESTRATOR-TASK-STALLED]]
- ❌ Zero revenue attributed for 10+ min → tracking broken → see [[WEBHOOK-HANDLER-DOWN]]

**Green Flags:**
- ✅ Most agents idle (high utilization headroom)
- ✅ Top agents maintaining > 90% success
- ✅ Revenue attributed within 2-3 min of task completion
- ✅ No agents at capacity
- ✅ ROI trending up month-over-month

---

### Dashboard 3: Brain Search (Knowledge Access)
**What:** Real-time search into Company Brain's Neo4j + Qdrant knowledge graph

**Why:** Verify knowledge graph is healthy, test context retrieval, understand what the Orchestrator "knows"

**Key Metrics:**
- Queries per minute (Cypher + vector)
- Query latency p50/p95/p99 (target: < 200ms p95)
- Neo4j node count (agents, capabilities, skills)
- Vector search accuracy (relevant documents returned)
- Discovery confidence scores

**How to Use It:**
```
Query Examples:

1. Find agents for "B2B sales discovery"
   → Returns: AGT-047 (96% match), AGT-089 (91% match), AGT-156 (78% match)
   → Latency: 145ms

2. Find capabilities for "medical facility outreach"
   → Returns: CAP-001 (Lead Gen), CAP-002 (Discovery), CAP-003 (Sales Strategy)
   → Coverage: 84% of ventures need this

3. Find similar agents to AGT-047
   → Returns: AGT-089 (89% similarity), AGT-156 (76% similarity)
   → Based on: skills, success rate, venture fit

4. Search "Can we handle a CPaaS integration?"
   → Returns: CAP-154 (API Integration), agents AGT-201, AGT-205
   → Confidence: 87% (we can do this)
```

**Red Flags:**
- ❌ Query latency > 2s → Neo4j degraded or missing indexes → see [[NEO4J-DISCOVERY-BROKEN]]
- ❌ Discovery returns 0 agents for common tasks → graph corrupted or agents missing → see [[NEO4J-DISCOVERY-BROKEN]]
- ❌ Confidence scores all < 0.5 → something fundamentally wrong with matching
- ❌ Vector search returning irrelevant results → embeddings model stale

**Green Flags:**
- ✅ Queries completing in < 200ms p95
- ✅ Discovery returning relevant agents with confidence > 0.8
- ✅ Neo4j has > 300 agent nodes + 300+ capability nodes
- ✅ Vector search returning semantically similar results

---

## Real-Time Status Page

**Where:** http://vex-hero-site-sigma.vercel.app/command-center (in development)

**Layout:**
```
┌────────────────────────────────────────────────────────────┐
│ COMMAND CENTER — Real-Time Orchestrator                    │
│ Last update: 14:32:45 UTC | Refresh: every 5s             │
├────────────────────────────────────────────────────────────┤
│                                                              │
│ 📊 TASK EXECUTION (Last Hour)                              │
│ ├─ Submitted: 1,247 | Success: 1,244 (99.8%) | Failed: 3  │
│ ├─ Avg Latency: 342ms | Current Queue: 12 tasks           │
│ └─ Critical Alert: None                                    │
│                                                              │
│ 👥 AGENT CAPACITY                                          │
│ ├─ Total Agents: 318 | Active: 42 (13%) | Idle: 276 (87%) │
│ ├─ Revenue (last hour): $4,250 | Attribution Lag: 2.1 min │
│ └─ Top Agent: AGT-047 (96% success, 3.2x ROI)              │
│                                                              │
│ 🧠 BRAIN HEALTH                                            │
│ ├─ Neo4j: ✅ OK | Agents: 318 | Capabilities: 307          │
│ ├─ Qdrant: ✅ OK | Vectors: 17,236 | Query Latency: 89ms   │
│ └─ Discovery Confidence: avg 0.87 (healthy)                │
│                                                              │
└────────────────────────────────────────────────────────────┘
```

---

## Monitoring by Role

### For On-Call Engineers
**Check every 5 minutes:**
1. Are tasks flowing through all 13 stages? (no stage stuck > 5 min)
2. Is success rate > 95%?
3. Is revenue attribution lag < 5 min?
4. Are any critical alerts showing?

**If something's wrong:**
1. Check which dashboard has the issue
2. Find matching runbook (Runbooks tab)
3. Follow immediate action steps

**Escalation path:**
- Issue unresolved after 5 min → Page L2 (domain specialist)
- Issue unresolved after 15 min → Page L3 (executive)

### For Executives
**Check daily (morning standoff):**
1. How many tasks executed yesterday? (target trend)
2. What was the revenue? (ROI per agent)
3. Which capabilities had the most work?
4. Any incidents or escalations?

**Check weekly (Friday review):**
1. Revenue trend (week-over-week growth)
2. Agent success rate trend (stable or improving?)
3. Discovery accuracy (confidence scores)
4. Incidents summary (what broke, why, how we fixed it)

### For Product Managers
**Check during feature release:**
1. Did new capability affect task success rate?
2. Which agents are using the new capability?
3. Is the new capability cheaper/faster than alternatives?
4. Any degradation in other capabilities?

---

## Common Patterns & What They Mean

### Pattern 1: Spiky Execution (Bursts)
**What You See:**
```
14:00 → 50 tasks active
14:01 → 120 tasks active (spike!)
14:02 → 95 tasks active
14:03 → 60 tasks active (back to normal)
```

**What It Means:**
- Batch job submitted (e.g., "cold email 100 leads")
- OR popular capability triggered multiple times
- OR external integration dumped tasks

**Is It Bad?** No, if:
- Tasks still completing successfully
- No stage getting stuck
- Success rate stays > 95%

**Is It Bad?** Yes, if:
- Tasks failing during spike (> 5% error rate)
- Queue backing up (tasks not starting)
- Database connections exhausted

**Action:** If good spike → nothing needed. If bad spike → see [[DATABASE-POOL-EXHAUSTED]] or [[ORCHESTRATOR-TASK-STALLED]]

---

### Pattern 2: High Revenue But Low Execution Count
**What You See:**
```
Tasks completed: 45
Revenue recorded: $8,500
Avg revenue per task: $189
```

**What It Means:**
- High-value deals closing (not just volume)
- Agent is picking expensive capabilities
- Good sales/revenue mix

**Is It Good?** Yes, likely means:
- Deal-focused work (not just lead gen)
- Strategic capability matching working
- ROI trending up

---

### Pattern 3: Capability X Always Fails
**What You See:**
```
CAP-042 (Email Outreach)
- Assigned to 15 agents
- Success rate: 34% (should be > 80%)
- Avg latency: 2,100ms (should be < 500ms)
```

**What It Means:**
- Capability timeout too short, OR
- Agents misconfigured for this capability, OR
- External API (email service) timing out

**Action:**
1. Check if timeout is configurable → increase by 2x
2. Check agent config for CAP-042 → verify parameters
3. Check email service health → is it responsive?
4. If still failing after #1-3 → see [[ORCHESTRATOR-TASK-STALLED]]

---

### Pattern 4: Discovery Finding No Agents
**What You See:**
```
Task: "Find an accountant for tax planning"
Discovery result: No agents found
Confidence: 0%
Fallback used: Yes (YAML registry)
```

**What It Means:**
- Neo4j doesn't have the skill/capability indexed, OR
- No agents marked with this capability, OR
- Query returned results but confidence was below threshold

**Action:** See [[NEO4J-DISCOVERY-BROKEN]] step 3 (check agent nodes and indexes)

---

### Pattern 5: Revenue Lag Growing
**What You See:**
```
14:00 → 2 min attribution lag
14:10 → 4 min attribution lag
14:20 → 8 min attribution lag (exceeds 5 min SLA)
```

**What It Means:**
- Webhook handler falling behind (queue backing up)
- Database slow (queries taking longer)
- High task volume with slow handler

**Action:** See [[WEBHOOK-HANDLER-DOWN]] (check handler process, database connections, queue depth)

---

## Key Dashboards & Commands

### Command-Line Status Checks

```bash
# 1. Check task flow (Supabase)
psql -h db.supabase.internal -U postgres -d company_brain -c "
SELECT 
  status,
  count(*) as count,
  ROUND(AVG(EXTRACT(EPOCH FROM (now() - created_at)))) as avg_age_seconds
FROM task_executions
WHERE created_at > NOW() - INTERVAL '1 hour'
GROUP BY status
ORDER BY count DESC;
"

# 2. Check agent utilization
curl -s http://100.87.214.70:20128/api/orchestrator/agent-stats?days=1 | jq '
.agents | map({
  name: .name,
  success_rate: .success_rate_percent,
  roi: .roi_multiple,
  tasks_last_hour: .recent_task_count
}) | sort_by(.success_rate) | reverse | .[0:5]
'

# 3. Check Neo4j health
curl -u neo4j:changeme -X POST http://100.87.214.70:7474/db/neo4j/tx \
  -H "Content-Type: application/json" \
  -d '{"statements":[{
    "statement": "CALL dbms.diagnostics.diagnosticQuery(\"systemConsistency\") YIELD data RETURN data.status"
  }]}'

# 4. Check discovery latency
curl -s -X POST http://100.87.214.70:20128/api/orchestrator/find-best-agents \
  -H "Content-Type: application/json" \
  -d '{
    "task_id": "HEALTH-CHECK",
    "description": "test query",
    "required_capabilities": ["CAP-001"],
    "venture": "OPS-001",
    "budget": 500
  }' | jq '.latency_ms'
```

---

## Setting Up Monitoring Alerts

### Critical Alerts (Page Immediately)

**Alert 1: Task Success Rate Drops**
```
IF (success_count / total_count) < 0.80 FOR 5 min
THEN page L2
```

**Alert 2: Revenue Attribution Lag**
```
IF (NOW() - last_revenue_recorded) > 5 min FOR 10 min
THEN page Revenue Team
```

**Alert 3: Database Connection Pool**
```
IF (active_connections / max_connections) > 0.95
THEN page Infrastructure Team
```

**Alert 4: Neo4j Query Latency**
```
IF query_latency_p95 > 2000 ms FOR 5 min
THEN page Knowledge Graph Team
```

### High Alerts (Page Within 5 min)

**Alert 5: Task Queue Depth**
```
IF queued_tasks > 100 FOR 10 min
THEN page Orchestrator Team
```

**Alert 6: Agent Success Rate Low**
```
IF any_agent.success_rate < 60% FOR 30 min
THEN create ticket, check in 30 min
```

### Medium Alerts (Create Ticket)

**Alert 7: API Latency**
```
IF api_response_time_p95 > 500ms FOR 15 min
THEN create ticket, review next day
```

---

## Dashboards (In Development)

### Current State (Tier 5)
- ✅ Command-Center.md (this document) — how to monitor
- 🟡 Orchestrator Dashboard (in progress) — visual interface
- 🟡 Revenue Leaderboard (planned)
- 🟡 Capability Heatmap (planned)

### Orchestrator Dashboard (Real-Time)
**Layout:**
```
Left Sidebar:
├─ Task Flow (13 stages with count)
├─ Error Log (last 10 errors)
├─ Alerts (critical/high/medium)
└─ Controls (pause, restart, reset)

Main Area (4-Quadrant View):
├─ Top-Left: Task Execution (timeline chart)
├─ Top-Right: Agent Capacity (utilization gauge)
├─ Bottom-Left: Revenue Attribution (lag trend)
└─ Bottom-Right: Brain Health (Neo4j + Qdrant status)

Right Sidebar:
├─ Quick Stats (success%, revenue/hour, avg latency)
├─ Top Agents (leaderboard)
└─ Recent Incidents (last 24h)
```

**Planned Features:**
- Real-time stage flow visualization (boxes showing task count per stage)
- Click to drill down into stuck tasks
- Agent detail view (click agent → see all tasks)
- Incident replay (click incident → replay the sequence)
- Custom alerts (create rules for your venture)

---

## Incident Response from Command Center

**Scenario 1: Success Rate Drops**
1. Look at Task Execution dashboard
2. Which stage has the most failures?
3. Are all agents in that stage failing, or just one?
4. Find matching runbook (Runbooks tab)
5. Follow immediate action steps

**Scenario 2: Revenue Lag Growing**
1. Check Agent Capacity dashboard → Revenue Attribution Lag
2. If lag > 5 min → see [[WEBHOOK-HANDLER-DOWN]]
3. If lag steady but task count high → normal (just busy)
4. If lag > 10 min → escalate to L2

**Scenario 3: No Agents Found for Task**
1. Check Brain Search dashboard
2. Run discovery query for the capability
3. If 0 agents returned → see [[NEO4J-DISCOVERY-BROKEN]]
4. If agents returned but low confidence → Neo4j query needs tuning

---

## FAQ

**Q: How often should I check the Command Center?**
A: On-call → every 5 min. Executives → daily morning. Product → during releases.

**Q: Why is my query latency > 500ms?**
A: Neo4j might be slow (see [[NEO4J-DISCOVERY-BROKEN]] step 4). Or database under load. Check database connections.

**Q: What's a "good" success rate?**
A: > 95% is healthy. 80-95% is acceptable (some failures expected). < 80% is a problem, escalate.

**Q: Why is revenue lag 4 minutes?**
A: Typical for high task volume. If < 5 min you're good. > 10 min is a problem.

**Q: Can I pause the Orchestrator from the dashboard?**
A: Not yet (Tier 5 planned feature). For now, contact @orchestrator-lead.

---

## Related Documentation

- [[ORCHESTRATOR-STATE-MACHINE]] — What happens at each of the 13 stages
- [[ORCHESTRATOR-API-REFERENCE]] — How to query the system programmatically
- [[RUNBOOKS]] — How to respond to incidents
- [[ESCALATION-POLICY]] — Severity matrix and escalation contacts
- [[REALITY|REALITY.md]] — Current system health status

---

**Status:** ✅ Command Center operational | **Last Updated:** 2026-09-18 | **Authority:** CP-033 (Execution) + CP-027 (Infrastructure)
