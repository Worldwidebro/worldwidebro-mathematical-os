# Orchestrator Prime (AGT-001) — Product Requirements Document

**Version:** 1.0  
**Date:** 2026-09-18  
**Status:** Scaffolding Complete → Ready to Build  
**Owner:** Worldwidebro Holdings — Venture Operating System  
**Authority:** CP-033 (Execution) + CP-027 (Infrastructure)

---

## 1. OVERVIEW

### What Is Orchestrator Prime?

Orchestrator Prime (AGT-001) is the master routing agent that discovers, selects, and coordinates autonomous task execution across the Company Brain's 318-agent network. It answers the question: **"Given any task, who is the best agent to execute it?"**

### Problem It Solves

- **Agent Discovery:** Founders, executives, and systems don't know which of 318 agents can execute a task
- **Suboptimal Routing:** Tasks route to wrong agents, wasting cost and reducing revenue
- **Revenue Attribution:** Execution happens, but revenue and costs are never attributed to agents
- **No ROI Visibility:** We can't measure if agents are actually profitable
- **Manual Coordination:** System operators manually assign tasks instead of autonomous routing

### Vision & North Star

**By Dec 31, 2026:** Every task automatically routes to the agent that maximizes revenue, minimizes cost, and executes with >90% success rate. The system self-learns: low-performing agents are replaced, high-performing agents scale, and the system compounds profitability quarter-over-quarter.

---

## 2. BUSINESS GOALS

| Goal | Target | Owner | Success Metric |
|------|--------|-------|-----------------|
| **Discover best agent for any task** | 318 agents searchable + rankable | Orchestrator + Agent Registry | 95%+ of tasks route to correct agent (top 3) |
| **Execute tasks with minimum cost, maximum revenue** | Task → execution → revenue | OmniRoute + Agents | 10x avg ROI per agent, >90% execution success |
| **Track revenue attribution end-to-end** | Every dollar tied to agent | Supabase + Triggers | 100% revenue attributed, no orphaned records |
| **Enable autonomous task routing (L2/L3)** | No human-in-loop after week 1 | OrchestratorPrime + Agents | L3 autonomy for 30+ agents by Nov 15 |
| **Reduce task routing latency** | <2s from task → suggested agents | API + Caching | p95 latency <2s, p99 <5s |
| **Measurable agent performance** | Agent leaderboard by ROI | Agent Stats + Triggers | Top 10 agents visible, bottom 10 flagged for review |

---

## 3. KEY FEATURES

### Feature 1: Task Classification (Claude Haiku)
**What:** Parse any task description and extract: intent, required capabilities, logic layers, suggested autonomy level.

**How:** Submit task to Claude Haiku API with structured prompt → classify in <500ms → return JSON.

**Why:** Foundation for agent matching; teams need to understand what a task really requires before routing.

**Acceptance:** Task classification accuracy >85% (validated against LOGIC_LAYERS_REGISTRY).

---

### Feature 2: Agent Discovery & Matching
**What:** Search 318 agents by capability, category, and ROI; return ranked top 3.

**How:**
1. Load agent inventory from AGENTS_INVENTORY_318.yaml + Supabase
2. Filter by task intent + required capabilities
3. Score by: confidence match (0-100), estimated ROI, cost, venture fit
4. Rank top 3 by ROI/cost ratio

**Why:** Users don't know the agent ecosystem; they need instant, ranked suggestions.

**Acceptance:** Best agent lands in top 1 > 80% of the time.

---

### Feature 3: OmniRoute Execution
**What:** Execute selected task with best agent via OmniRoute, passing context (venture, budget, revenue target).

**How:**
1. Pack task + context into OmniRoute payload
2. Call OmniRoute API with agent ID + tool bindings
3. Monitor execution status
4. Handle failures, timeouts, retries

**Why:** Unified execution layer; agents don't need to know how to invoke each other.

**Acceptance:** Execution success rate >90%; timeouts <5min; retry logic recovers 80% of failures.

---

### Feature 4: Revenue Attribution & Logging
**What:** Track every task through its lifecycle: queued → executing → complete → revenue logged → agent stats updated.

**How:**
1. Create task_executions record when task queued
2. Update status as execution progresses
3. On completion, parse agent output for revenue (actual_revenue, cost_actual)
4. Insert revenue_log entry
5. Trigger updates agent_stats + venture_revenue_summary automatically

**Why:** No guessing; every dollar is tied to which agent earned it.

**Acceptance:** 100% of executed tasks have revenue_log entries; zero orphaned records.

---

### Feature 5: Agent Performance Analytics
**What:** Real-time leaderboard + dashboards showing agent ROI, cost, success rate, revenue trend.

**How:**
1. Build agent_leaderboard view: rank by avg ROI, filter by time window
2. Build venture_revenue_30d view: track revenue by venture + agent
3. Build task_execution_summary view: status distribution + success rates
4. Dashboard queries these views for live updates

**Why:** Transparency → accountability → performance improvement.

**Acceptance:** Dashboard loads <1s; data updates within 5min of task completion.

---

### Feature 6: REST API Endpoint
**What:** HTTP POST `/api/orchestrate` accepts task, returns suggested agents + execution status.

**Request:**
```json
{
  "description": "Send cold emails to 20 prospects",
  "venture": "LT-005",
  "urgency": "high",
  "budget": 50,
  "revenue_target": 1500
}
```

**Response:**
```json
{
  "success": true,
  "task_id": "TASK-2026-09-18-001",
  "suggested_agents": [
    {
      "agent_id": "agent-revenue-cold-email-writer-001",
      "confidence_score": 95,
      "cost": 0.25,
      "estimated_revenue": 1500,
      "rationale": "Matches outreach + [write-emails, personalize, track-opens]"
    }
  ],
  "status": "queued"
}
```

**Why:** Other systems (Make.com, VEX dashboard, internal tools) need a unified interface.

**Acceptance:** API available 24/7; response time <2s; error rate <0.1%.

---

## 4. SUCCESS METRICS

| Metric | Target | Measurement Method | Cadence |
|--------|--------|-------------------|---------|
| **Agent Discovery Accuracy** | Best agent in top 3: >80% | Validate classifications vs. LOGIC_LAYERS_REGISTRY | Weekly |
| **Execution Success Rate** | >90% | (tasks_completed / tasks_executed) | Daily |
| **Average ROI per Agent** | >10x | revenue_actual / cost_actual per agent | Daily |
| **Revenue Attribution Completeness** | 100% | tasks_with_revenue_log / tasks_completed | Daily |
| **Task Routing Latency (p95)** | <2s | API response time measurement | Hourly |
| **Dashboard Uptime** | >99.9% | Continuous monitoring | Daily |
| **Agent Leaderboard Accuracy** | 100% | Views match source tables | Automated |
| **Cost per Classification** | <$0.003 | Track Claude Haiku API usage | Monthly |
| **Venture Revenue Tracking** | 100% clean attribution | Audit revenue_log vs. Make.com + Stripe | Weekly |

---

## 5. USER STORIES

### Story 1: Founder Sends Task
**As a** founder (e.g., building LT-005),  
**I want to** send a task in natural language and get instant agent suggestions,  
**So that** I don't need to know the 318-agent ecosystem; the system finds the best one.

**Acceptance Criteria:**
- POST /api/orchestrate with task description
- Returns top 3 agents in <2 seconds
- Agent includes confidence_score, cost, estimated_revenue

---

### Story 2: Agent Discovers Tasks
**As an** agent (e.g., Cold Email Writer),  
**I want to** be discoverable when tasks match my capabilities,  
**So that** I execute high-value tasks and build a strong performance record.

**Acceptance Criteria:**
- Agent indexed in AGENTS_INVENTORY_318.yaml
- When task intent + capabilities match, agent ranked in top 3
- Agent receives task execution request via OmniRoute

---

### Story 3: System Tracks Revenue
**As the** Company Brain (operating system),  
**I want to** track revenue end-to-end from task → execution → payment,  
**So that** we know which agents are profitable and which need improvement.

**Acceptance Criteria:**
- Every executed task creates task_executions record
- Completion triggers revenue_log entry
- Agent stats updated automatically via trigger
- No manual revenue entry needed

---

### Story 4: Executive Reviews Agent Performance
**As an** executive (e.g., CEO, VP Growth),  
**I want to** see agent leaderboard ranked by ROI and revenue,  
**So that** I can scale high-performers, replace low-performers, and optimize cost.

**Acceptance Criteria:**
- agent_leaderboard view shows top 10 + bottom 10
- Sortable by: ROI, total_revenue, success_rate, cost
- Filters by: venture, time_window (7d/30d/90d)
- Updates within 5 minutes of task completion

---

### Story 5: Autonomous Execution
**As the** system (L2/L3 autonomy),  
**I want to** route tasks without human approval after verification,  
**So that** the 789-venture portfolio executes in parallel without bottlenecks.

**Acceptance Criteria:**
- L2 autonomy: system selects agent, human confirms before execution
- L3 autonomy: system selects agent and executes automatically (with guardrails)
- Rollback available if execution fails
- Human oversight via dashboard + alerts

---

## 6. SCOPE

### In Scope
✅ Task classification (Claude Haiku)  
✅ Agent discovery + matching (capability-based)  
✅ OmniRoute execution routing  
✅ Revenue attribution + logging  
✅ Agent performance analytics (leaderboard)  
✅ REST API endpoint (`/api/orchestrate`)  
✅ Supabase schema + views + triggers  
✅ Dashboard (basic agent stats)  
✅ Error handling + fallback logic  
✅ Cost tracking per task + agent

### Out of Scope
❌ Individual agent UI/interface (agents handle their own)  
❌ Agent development (agent teams build; Orchestrator just routes)  
❌ Human orchestration interface (beyond dashboard)  
❌ Real-time agent communication (handled by OmniRoute)  
❌ Financial settlement (handled by billing system)  
❌ Agent training (handled by agent teams)

---

## 7. TIMELINE

### Phase 1: Complete Scaffolding (Sep 18–19, 0.5h)
- Deploy Supabase schema (6 tables, 3 views, 2 triggers)
- Seed agent_registry with AGENTS_INVENTORY_318.yaml data
- Verify all tables exist + initial data loaded

### Phase 2: Task Classification (Sep 19–20, 2h)
- Wire classifyTask() to Claude Haiku API
- Implement keyword fallback if API fails
- Test with 10 sample tasks; verify 85%+ accuracy
- Commit: "feat: Task classification via Claude Haiku"

### Phase 3: Agent Matching (Sep 20–21, 2h)
- Implement capability-based scoring algorithm
- Test matching: ("send emails" → "Cold Email Writer")
- Verify top agent correct >80% of the time
- Commit: "feat: Agent matching by capability + ROI"

### Phase 4: OmniRoute Execution (Sep 21–22, 2h)
- Wire executeTask() to OmniRoute API
- Test invocation: task → OmniRoute → agent execution
- Implement retry + timeout handling
- Commit: "feat: OmniRoute execution + failure recovery"

### Phase 5: Revenue Attribution (Sep 22–23, 1h)
- Implement attributeRevenue() end-to-end
- Test trigger: revenue_log entry → agent_stats update
- Verify ROI calculation accuracy
- Commit: "feat: Revenue attribution + agent stats triggers"

### Phase 6: API + Dashboard (Sep 23–25, 1.5h)
- Deploy `/api/orchestrate` endpoint
- Create dashboard: agent leaderboard + venture revenue + task summary
- Wire Make.com trigger (optional; post-MVP)
- Commit: "feat: /api/orchestrate endpoint + dashboard"

### Phase 7: Testing + Optimization (Sep 25–30, 1.5h)
- Unit tests: agent loading, classification, scoring, ROI calc
- Integration tests: full task lifecycle
- End-to-end tests: 5 real ventures with real agents
- Performance optimization: p95 latency <2s
- Commit: "test: Complete unit + integration + E2E test suite"

### Phase 8: Launch + Monitoring (Oct 1, 0.5h)
- Deploy to production
- Enable alerting: failed classifications, high error rates
- Monitor API uptime + dashboard performance
- Activate first 10 autonomous agents (L2)

---

## 8. DEPENDENCIES & RISKS

### Critical Dependencies
- **AGENTS_INVENTORY_318.yaml:** Must be current + accurate
- **Claude Haiku API:** Classification endpoint must be available
- **OmniRoute:** Execution routing must be live + accessible
- **Supabase:** Database schema + triggers must be deployed
- **LOGIC_LAYERS_REGISTRY:** Mapping capabilities to logic layers must exist

### Key Risks
| Risk | Impact | Mitigation |
|------|--------|-----------|
| Classification accuracy <80% | Wrong agents selected | Fallback to keyword matching; weekly review |
| OmniRoute unavailable | Tasks can't execute | Cache last-known agent list; graceful degradation |
| Revenue tracking orphaned records | No ROI visibility | Daily audit; manual reconciliation if needed |
| High API latency (>2s) | Poor user experience | Implement caching; fallback to cached agents |
| Agent not in inventory | Agent undiscoverable | Weekly sync AGENTS_INVENTORY_318.yaml with Supabase |

---

## 9. DEFINITION OF DONE

✅ All 6 Supabase tables created + seeded  
✅ Task classification working (Claude Haiku + fallback)  
✅ Agent matching algorithm implemented + tested  
✅ OmniRoute execution wired + failure handling in place  
✅ Revenue attribution end-to-end working  
✅ `/api/orchestrate` endpoint live + responding <2s  
✅ Dashboard showing agent leaderboard + metrics  
✅ Unit tests: >80% coverage  
✅ Integration tests: full task lifecycle  
✅ E2E tests: 5 real ventures executed successfully  
✅ Error handling: all edge cases documented + handled  
✅ Monitoring: alerts set up for failures + latency  
✅ Documentation: README, API docs, architecture diagram  
✅ Team trained: founders + agents understand how to use  

---

## 10. MEASURES OF SUCCESS (90-DAY)

By Nov 18, 2026:
- ✅ 500+ tasks routed + executed
- ✅ $50K+ revenue attributed to agents
- ✅ Top 10 agents with >10x ROI
- ✅ 30+ agents operating autonomously (L2+)
- ✅ <1% task routing failure rate
- ✅ Dashboard used daily by 5+ executives
- ✅ Agent leaderboard guides resource allocation

---

**Prepared by:** Claude Haiku 4.5  
**Reviewed by:** [CP-033 Execution Owner]  
**Approved by:** [CEO/Founder]  

---

**Next:** Phase 1 Deployment (Sep 18–19) → Phase 2–7 (Sep 19–30) → Production Launch (Oct 1)

See also: `OMNIROUTE-ORCHESTRATOR-PRIME-BUILD-PLAN.md`, `ORCHESTRATOR-PRIME-SUPABASE-SCHEMA.sql`, `src/services/orchestrator-prime.ts`
