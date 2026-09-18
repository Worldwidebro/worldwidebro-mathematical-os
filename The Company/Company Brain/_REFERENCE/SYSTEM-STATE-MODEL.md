---
title: System State Model (Continuous Truth)
id: SYSTEM-STATE-MODEL
phase: Phase 2 (Local Autonomy)
updated: 2026-09-17
---

[[STARTHERE]] | [[REALITY]] | [[20-DECISIONS/PHASE-2-RESEARCH-TO-REVENUE-ROADMAP]]

# System State Model

**Authority:** [[_REGISTRIES/CANONICAL/LOGIC_LAYERS_REGISTRY.yaml|LOGIC-007 through LOGIC-012]] (Observation layer)  
**Part of:** [[20-DECISIONS/PHASE-2-RESEARCH-TO-REVENUE-ROADMAP|Phase 2 Research-to-Revenue Engine]] → Graph Infrastructure (Dec 2026)

**Goal:** "What is true right now?" queryable in <100ms via [[_PIPELINES/GRAPH-INGESTION-PIPELINE.md|graph ingestion]] and [[CLAUDE.md#Infrastructure Status|live infrastructure queries]].

## Core State Queries

```sql
-- Cash Position
SELECT SUM(revenue_today) FROM invoices WHERE created_today;

-- Open Opportunities  
SELECT COUNT(*) FROM opportunities WHERE status='open';

-- Unanswered Leads
SELECT COUNT(*) FROM leads WHERE last_contact < NOW() - interval '24h';

-- Failed Workflows
SELECT * FROM workflows WHERE status='failed' ORDER BY created DESC;

-- Agent Health
SELECT agent_id, last_success, failure_count FROM agents;

-- Next Due Actions
SELECT * FROM scheduled_actions WHERE due_time <= NOW();

-- System Health
SELECT uptime, error_rate, avg_latency FROM observability;
```

## Postgres View

```sql
CREATE VIEW system_state_current AS
  SELECT
    (SELECT SUM(revenue_today) FROM invoices WHERE created_today) as daily_revenue,
    (SELECT COUNT(*) FROM opportunities WHERE status='open') as open_opportunities,
    (SELECT COUNT(*) FROM leads WHERE last_contact < NOW() - interval '24h') as unanswered_leads,
    (SELECT COUNT(*) FROM workflows WHERE status='failed') as failed_workflows,
    NOW() as captured_at;
```

## Usage

Agents query before deciding:
- "What's our cash position?" → instant answer
- "How many open deals?" → instant answer
- "What failed since last loop?" → instant answer

## Update Frequency

- Real-time updates from event stream (Kafka/RabbitMQ)
- Every 5 min full refresh from databases
- Eventual consistency within 5 seconds

