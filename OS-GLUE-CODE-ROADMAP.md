---
title: OS Glue Code Roadmap — Concrete Tasks to Wire 80% Solved Items
date: 2026-07-20
version: 1.0
---

# OS Glue Code Roadmap

**Goal:** Turn 80% solved items into operational by wiring existing tools together.

**Mindset:** Minimal code. Reuse everything. No new tools. Just connect what we have.

---

## Phase A: Quick Wins (4 hours, 1 day)

These unblock visibility + governance immediately.

### A1: Wire Otel-Collector to Prometheus
**Status:** 90% done (just needs config)  
**File:** `prometheus.yml`  
**Task:**
```yaml
# Add otel-collector as scrape target
scrape_configs:
  - job_name: 'otel-collector'
    static_configs:
      - targets: ['otel-collector:9464']
```
**Result:** Prometheus scrapes app metrics from otel-collector. Grafana can visualize.  
**Effort:** 5 minutes  
**Impact:** Phase 18 (Observability) jumps from 22% → 40%

---

### A2: Reconcile Hermes Schema
**Status:** 50% done (dashboard exists, queries wrong)  
**File:** `hermes-command-center/src/lib/supabase.ts`  
**Task:** Replace 4 table references:
- `aoc_agents` → `ventures`
- `agent_tasks` → `venture_decisions`
- `agent_decisions` → `venture_decisions` (filter by decision_type)
- `agent_assignments` → remove (use ventures.assigned_to)

**Result:** Hermes loads real venture data + shows health, readiness, MRR.  
**Effort:** 30 minutes  
**Impact:** Phase 20 (CEO Dashboard) jumps from 30% → 60%

---

### A3: Audit Log Instrumentation
**Status:** Schema exists (0 rows), needs hooks  
**Files:** Agent action code (venture creation, Slack posts, task creation)  
**Task:** Add 5 audit log calls:
```python
# When venture created
supabase.table('audit_logs').insert({
  'timestamp': datetime.now(),
  'agent_id': 'venture_classifier',
  'action': 'venture_created',
  'entity_id': venture_id,
  'metadata': {'name': venture_name}
})
```

**Result:** Complete audit trail. Compliance-ready.  
**Effort:** 1 hour  
**Impact:** Phase 12 (Security) + Phase 0 (Governance) jump from 33%/75% → 50%/85%

---

## Phase B: Foundation Wiring (20 hours, 1 week)

These enable agent coordination + venture infrastructure.

### B1: Finish AgentToolWiring Class
**Status:** 0% (started but incomplete)  
**File:** `agent_tool_wiring.py`  
**Task:** Implement permission checks + event publishing + error handling

**Result:** All agents can safely call tools with audit trail + coordination.  
**Effort:** 4 hours  
**Impact:** Phase 2 (Identity) + Phase 6 (Agent Runtime) jump from 44%/69% → 70%/85%

---

### B2: Wire venture_classifier to Slack + ClickUp
**Status:** Partially done (cadence-check.py works)  
**File:** Create `venture_classifier_agent.py`  
**Task:** Use AgentToolWiring to post Slack notifications + create ClickUp tasks

**Result:** venture_classifier automatically posts to Slack + creates tasks.  
**Effort:** 3 hours  
**Impact:** Phase 9 (Automation) + Phase 6 (Agent Runtime) jump from 40%/69% → 65%/80%

---

### B3: Venture OS Template
**Status:** 80% done (folder structure exists; not wired)  
**File:** Create `venture_os_template.py`  
**Task:** Generate per-venture config that provisions:
- Supabase schema (CRM tables)
- ClickUp list
- Grafana dashboard
- Webhooks (Stripe → Supabase)

**Result:** New ventures auto-provision CRM + dashboard + task management.  
**Effort:** 6 hours  
**Impact:** Phase 8 (Venture OS) jumps from 10% → 50%

---

### B4: Event Bus Wiring (Redis pubsub)
**Status:** 80% done (Redis running; not wired)  
**File:** Create `event_bus.py`  
**Task:** Wire agent actions → Redis pubsub events

**Result:** Agents coordinate without polling. venture_classifier → risk_assessor → content_atomizer chain.  
**Effort:** 3 hours  
**Impact:** Phase 6 (Agent Runtime) + Phase 9 (Automation) jump from 69%/40% → 85%/70%

---

## Phase C: BI + Dashboards (16 hours, 1 week)

These provide visibility to run the OS.

### C1: Grafana Dashboard Templates
**Status:** 90% done (Grafana running; just needs JSON)  
**Files:** Create in `grafana/dashboards/`  
**Task:** Copy vendor templates + wire to Supabase queries:
- Revenue dashboard (MRR by venture, by sector)
- Venture health (readiness score, runway, risk)
- Agent execution (agent actions last 24h)

**Result:** Live dashboards. CEO sees venture health in real-time.  
**Effort:** 4 hours  
**Impact:** Phase 11 (BI) jumps from 10% → 40%

---

### C2: Venture Health Dashboard
**Status:** CSV only; needs interactive version  
**File:** Grafana dashboard + sync script  
**Task:** Wire VENTURE-READINESS-SCORECARD.csv to Grafana via Supabase

**Result:** Venture health visualized. Blockers surface automatically.  
**Effort:** 3 hours  
**Impact:** Phase 11 (BI) + Phase 20 (CEO Dashboard) jump from 10%/30% → 50%/50%

---

### C3: Agent Execution Dashboard
**Status:** Hermes UI built; not wired  
**File:** Grafana dashboard  
**Task:** Create panel showing agent activity (executions, success rate)

**Result:** See venture_classifier, risk_assessor running live.  
**Effort:** 2 hours  
**Impact:** Phase 20 (CEO Dashboard) jumps from 30% → 45%

---

## Phase D: Automation + Scaling (20 hours, 2 weeks)

These enable venture self-serve + scaling.

### D1: Deploy n8n
**Status:** Installed; not running  
**Task:** Start n8n + create 1 workflow (Stripe webhook → Supabase → Slack)

**Result:** Payments flow automated.  
**Effort:** 2 hours  
**Impact:** Phase 9 (Automation) jumps from 40% → 60%

---

### D2: Secrets Vault
**Status:** .env local; no vault  
**Task:** Install HashiCorp Vault. Migrate .env keys.

**Result:** API keys rotated automatically. Secrets not in git.  
**Effort:** 3 hours  
**Impact:** Phase 2 (Identity) + Phase 12 (Security) jump from 44%/33% → 60%/50%

---

## Execution Roadmap

### Week 1 (Phase A: Quick Wins)
- [ ] A1: Otel-collector wiring (5 min)
- [ ] A2: Hermes schema fix (30 min)
- [ ] A3: Audit log calls (1 hour)

**Total: 2 hours**

### Week 2-3 (Phase B: Foundation)
- [ ] B1: AgentToolWiring (4 hours)
- [ ] B2: venture_classifier integration (3 hours)
- [ ] B3: Venture OS template (6 hours)
- [ ] B4: Event bus (3 hours)

**Total: 16 hours**

### Week 4-5 (Phase C: Dashboards)
- [ ] C1: Grafana templates (4 hours)
- [ ] C2: Venture health dashboard (3 hours)
- [ ] C3: Agent execution dashboard (2 hours)

**Total: 9 hours**

### Week 6-7 (Phase D: Automation)
- [ ] D1: n8n deployment (2 hours)
- [ ] D2: Secrets vault (3 hours)

**Total: 5 hours**

---

## Success Metrics (End of Week 7)

**Operational Goals:**
- ✅ New venture auto-provisions CRM + dashboard
- ✅ venture_classifier posts to Slack + creates tasks
- ✅ CEO can see live venture health
- ✅ All agent actions audit-logged
- ✅ API keys rotated automatically

**OS Completion:**
- Phase 0: 75% → 85%
- Phase 2: 44% → 60%
- Phase 6: 69% → 85%
- Phase 8: 10% → 50%
- Phase 9: 40% → 65%
- Phase 11: 10% → 50%
- Phase 18: 22% → 40%
- Phase 20: 30% → 50%

**Overall:** 39% → 55% in 7 weeks

---

*Last Updated: 2026-07-20*
