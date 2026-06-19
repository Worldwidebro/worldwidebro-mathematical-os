# System Contracts Summary

**Real technology stack for CivilizationOS Agent OS**

---

## 🧠 Tech Stack (Open Source, Production-Ready)

| Layer | Technology | Role | Status |
|-------|-----------|------|--------|
| Events | **Apache Kafka** | Event bus, message streaming | Core dependency |
| Orchestration | **Temporal** or **n8n** | Workflow engine, retry logic, DAG execution | Core dependency |
| Agents | **LangGraph** | Agent loops, tool use, multi-agent coordination | Core dependency |
| Memory | **Neo4j** + **Weaviate** | Graph relationships, semantic embeddings | Core dependency |
| Storage | **Postgres** + **DuckDB** | Transactional truth + analytics | Core dependency |
| Observability | **Grafana** + **Prometheus** | Metrics, dashboards, alerting | Core dependency |
| Glue | **FastAPI** | Service-to-service API layer | Connector |
| State Cache | **Redis** | Agent state, session data | Accelerator |

---

## 📊 System Boundaries (What Can NOT Mix)

### 1. **Ontology ≠ Execution**
- **Ontology** (Neo4j): Relations between entities, taxonomy, knowledge graph
- **Execution** (Temporal/n8n): Workflows, decisions, actions
- **Boundary rule:** Agents read from ontology; write results as events, NOT directly to Neo4j

### 2. **Capital Logic ≠ Workflow Logic**
- **Capital Logic** (Risk Agent): ROI calculations, kill/scale decisions
- **Workflow Logic** (Venture Agent): Execution flows, task orchestration
- **Boundary rule:** Every workflow step must pass risk validation before execution

### 3. **Risk System Overrides Everything**
- **Source of truth:** Risk Engine constraints in `risk-agent/rules-engine/constraints.json`
- **Enforcement:** All decisions validated via Risk Agent before event emission
- **Boundary rule:** If risk threshold crossed → escalate, don't execute

### 4. **Cloud ≠ Source of Truth**
- **Source of truth:** Postgres (transactional events)
- **Derived state:** Elasticsearch, DuckDB, Redis caches
- **Boundary rule:** All mutations start in Postgres events table, propagate outward

### 5. **Agents ≠ Registries**
- **Agents** create decisions → emit events
- **Registries** (Neo4j) are read-only from agent perspective
- **Boundary rule:** Agents cannot directly mutate Neo4j; changes via event → Neo4j sync job

---

## 🔀 Data Flow Contracts

### Event → State → Action → Observation (Kafka → Postgres → Redis → Grafana)

```
1. Event Emitted
   ├─ Source: Agent, User, External System
   ├─ Schema: Kafka event schema (see event-system/event-taxonomy.md)
   └─ Kafka Topic: event.{type}.v1

2. Postgres Transactional Write
   ├─ Table: event_log
   ├─ Fields: event_id, type, source, payload, timestamp, correlation_id
   └─ Constraint: immutable append-only

3. Risk Engine Validation (Real-time)
   ├─ Reads: event payload
   ├─ Checks: constraints.json rules
   └─ Decision: ALLOW | REJECT | ESCALATE

4. State Update (Redis + Postgres)
   ├─ Redis: agent state cache (TTL: 1 hour)
   ├─ Postgres: historical state (permanent)
   └─ DuckDB: analytics materialization

5. Grafana Metric Emission
   ├─ Prometheus scrapes agent state
   ├─ Dashboard renders in real-time
   └─ Alerts trigger on thresholds

6. Neo4j Relationship Update (Async)
   ├─ Job: event → Neo4j sync (every 60 seconds)
   ├─ Creates: venture → sector, venture → metric, venture → risk relationships
   └─ Reads from: Postgres event_log

7. Obsidian Dataview Sync (Batch)
   ├─ Script: obsidian_graph_sync.py
   ├─ Exports: Neo4j → .planning/graph-data.json
   └─ Frequency: Every 6 hours (or manual trigger)
```

---

## 🤖 Agent Execution Contract (LangGraph + Temporal)

### Every agent must implement this state machine:

```
START
  ↓
LOAD_CONTEXT (Redis | Postgres)
  ├─ Agent ID, role, permissions
  ├─ Recent event history (last 100)
  └─ Current venture state snapshot
  ↓
RECEIVE_EVENT (Kafka consumer)
  ├─ Topic: event.{type}.v1
  ├─ Partition key: venture_id (ensures ordering)
  └─ Deserialize to event schema
  ↓
REASONING (LangGraph loop via Claude API)
  ├─ Input: event payload, agent state, available tools
  ├─ Tools available: query_neo4j, query_postgres, compute_roi, check_constraints
  ├─ Output: decision (structured JSON)
  └─ Chain-of-thought logging to stdout
  ↓
VALIDATE_WITH_RISK_ENGINE
  ├─ Call: risk-agent service (FastAPI)
  ├─ Input: decision payload
  ├─ Output: APPROVED | REJECTED | ESCALATE_TO_HUMAN
  └─ If REJECTED: emit event.decision.rejected
  ↓
EXECUTE (Temporal workflow if approved)
  ├─ Workflow: venture-execution-workflow.yaml
  ├─ Retries: 3 with exponential backoff (1s, 2s, 4s)
  ├─ Timeout: 30 minutes
  ├─ Dead letter queue: event.execution.failed
  └─ Execution logged to Postgres execution_log table
  ↓
EMIT_RESULT_EVENT (Kafka producer)
  ├─ Topic: agent.{agent_type}.executed.v1
  ├─ Event: { decision_id, decision, outcome, cost_usd, roi_impact_percent }
  ├─ Partition key: venture_id
  └─ Correlation ID: preserved from original event
  ↓
UPDATE_STATE (Redis + Postgres)
  ├─ Redis: agent state cache (SET agent:{id}:{timestamp} {...})
  ├─ Postgres: INSERT INTO agent_state_history (...)
  └─ Prometheus: emit venture_agent_decisions_total, venture_agent_execution_duration_ms
  ↓
END
```

---

## 📡 Event Types (Kafka Topic Schema)

25 core event types across 3 agent systems:

### Orchestrator Agent Events (Kafka Topic: `orchestrator.*`)
- `orchestrator.started` — Master orchestrator boots up
- `orchestrator.venture_agent.spawned` — New venture agent spawned
- `orchestrator.all_agents.spawned` — All N venture agents + risk agent ready
- `orchestrator.shutdown_requested` — Graceful shutdown initiated
- `orchestrator.health_check.passed` — All subsystems healthy
- `orchestrator.state_dump` — Full system state snapshot (hourly)

### Venture Agent Events (Kafka Topic: `venture.*`)
- `venture.initialized` — Venture agent loaded for venture_id
- `venture.decision.made` — Agent made a decision (SCALE, KILL, SUSTAIN, PIVOT)
- `venture.execution.started` — Decision execution began
- `venture.execution.succeeded` — Action completed successfully
- `venture.execution.failed` — Action failed with reason
- `venture.repo_synced` — GitHub repo synced + status updated
- `venture.contact_created` — New contact added to venture
- `venture.product_launched` — Product milestone reached
- `venture.milestone_reached` — Arbitrary milestone (custom)
- `venture.state_updated` — Venture state changed (IDEA → MVP → LIVE → SCALING)
- `venture.risk_triggered` — Risk threshold breached (e.g., MRR < threshold)
- `venture.escalated_to_human` — Decision escalated for manual review

### Risk Agent Events (Kafka Topic: `risk.*`)
- `risk.threshold_crossed` — KPI threshold (MRR, CAC, LTV) exceeded
- `risk.kill_decision` — Venture should be shut down
- `risk.scale_decision` — Venture should get more capital
- `risk.constraint_violated` — System constraint violated (max_agents, max_capital)
- `risk.capital_reallocated` — Capital moved from one venture to another
- `risk.warning_issued` — Soft constraint threshold approached
- `risk.all_constraints_ok` — System in healthy state

---

## 🧭 System Boundaries (Enforcement Points)

### Boundary 1: No Agent → Direct DB Writes
❌ WRONG:
```python
postgres.execute("UPDATE ventures SET status='LIVE' WHERE id=123")
```

✅ RIGHT:
```python
event = {
  "type": "venture.status_updated",
  "venture_id": "123",
  "new_status": "LIVE",
  "reason": "Agent decision: PMF threshold reached"
}
kafka_producer.send(topic="venture.status_updated.v1", value=event)
# Event handler in Postgres consumes Kafka, updates DB
```

### Boundary 2: Risk Engine is Gatekeeper
❌ WRONG:
```python
if agent_decision == "scale":
    venture.scale(2x_capital)  # Direct execution
```

✅ RIGHT:
```python
if agent_decision == "scale":
    event = {
        "type": "venture.scale_requested",
        "venture_id": venture_id,
        "capital_requested": 50000,
        "reason": agent_decision.reasoning
    }
    kafka_producer.send("venture.scale_requested.v1", value=event)
    
    # Risk agent consumes event, runs constraints check
    # If approved → risk agent emits venture.capital_allocated event
    # Temporal workflow listens for capital_allocated → executes transfer
```

### Boundary 3: Derived State is Read-Only
❌ WRONG:
```python
duckdb.execute("INSERT INTO ventures_aggregated ...")
```

✅ RIGHT:
```python
# DuckDB is materialized view from Postgres event_log
# Sync job runs every 15 minutes:
# SELECT venture_id, COUNT(*) as events, MAX(timestamp) as last_update
# FROM event_log
# WHERE type IN ('venture.executed', 'risk.threshold_crossed')
# GROUP BY venture_id
```

### Boundary 4: Neo4j is Append-Only From Agents
❌ WRONG:
```python
neo4j.run("UPDATE relationship SET weight=0.8 WHERE ...")
```

✅ RIGHT:
```python
# Neo4j relationships created from event_log via periodic job
# Sync job (every 60 seconds):
# FOR EACH event WHERE type = 'venture.initialized':
#   MATCH (v:Venture {id: event.venture_id})
#   MATCH (s:Sector {id: event.sector_id})
#   CREATE (v)-[:BELONGS_TO_SECTOR]->(s)
```

### Boundary 5: Agents Cannot Mutate Registries
❌ WRONG:
```python
capabilities_registry.add("new_capability", agent_id="bw-001")
```

✅ RIGHT:
```python
# Registries (capabilities, sector taxonomy) are static reference data
# Loaded once at startup from CLAUDE.md + CSV files
# Changes require human approval + code commit
# Agents only READ capabilities to understand constraints
```

---

## 🧯 Failure Model (Recovery Strategy)

| Scenario | Failure Point | Recovery | Data Loss Risk |
|----------|---------------|----------|-----------------|
| Agent crashes (LangGraph) | Agent process dies | Postgres event_log is immutable; agent restarts, replays from last checkpoint (Redis) | No loss; checkpoint preserved |
| Kafka broker down | Event emission fails | Kafka is replicated 3x; automatic failover | No loss if any broker alive |
| Postgres connection lost | Event storage fails | Agent halts gracefully; Redis keeps recent state (~1 hr); manual intervention | Yes, if Postgres unrecoverable |
| Risk engine rejects decision | Constraint violated | Emit `event.decision.rejected`; escalate to human via Slack | No; decision discarded before execution |
| Neo4j sync job fails | Graph outdated | Retry next cycle (60 sec); Postgres is source of truth | No; Neo4j is derived state |
| Grafana down | Visibility lost | Prometheus scrape continues; cache preserved; dashboard unavailable | No; metrics preserved 30 days |
| Redis memory full | State cache eviction | Postgres still has full history; Redis restarts | No; Redis is cache, not truth |
| DuckDB analytics stale | Reports delayed | Run manual refresh; next batch job updates | No; can be regenerated from Postgres |

---

## 📊 State Model (Where Data Lives)

| Data | Storage | Owner | TTL | Mutability | Replication |
|------|---------|-------|-----|------------|-------------|
| Events (immutable log) | Postgres `event_log` | System of record | Permanent | Append-only | 3x async replica |
| Agent state (snapshot) | Redis `agent:{id}:{ts}` | Each agent | 1 hour | Read/write | No (recreatable) |
| Agent state (history) | Postgres `agent_state_history` | System of record | Permanent | Append-only | 3x async replica |
| Venture state (current) | Redis `venture:{id}:state` | Last agent to update | 1 hour | Overwrite | No |
| Venture state (history) | Postgres `venture_state_history` | System of record | Permanent | Append-only | 3x async replica |
| Neo4j graph relationships | Neo4j `graph.db` | Neo4j cluster | Permanent | Append-only | 3x RAFT cluster |
| Analytics (DuckDB views) | DuckDB `analytics.duckdb` | Computed nightly | 7 days | Materialized | No (regeneratable) |
| Observability metrics | Prometheus TSDB | Prometheus | 30 days | Time-series append | No (query-time aggregation) |
| Cached reads (Weaviate) | Weaviate `vectors.db` | Weaviate cluster | 1 day | Overwrite | 3x replication |

---

## 🚀 Implementation Phases

### Phase 1: Contracts & Schemas (Week 1)
- [ ] Define 10 JSON Schemas (agent, event, venture state, risk constraint)
- [ ] Configure 25 Kafka topics with retention policies
- [ ] Design Postgres schema (event_log, agent_state_history, venture_state_history)
- [ ] Setup Neo4j schema (Venture, Sector, Metric, Risk nodes + relationships)

### Phase 2: Master Orchestrator (Week 2)
- [ ] Build orchestrator agent (LangGraph)
- [ ] Setup Kafka consumer for orchestrator events
- [ ] Implement Temporal workflows for venture agent spawning
- [ ] Wire Redis state cache

### Phase 3: Venture Agent Template (Week 3)
- [ ] Build single venture agent (LangGraph)
- [ ] State machine implementation (IDLE → REASONING → EXECUTING → IDLE)
- [ ] Risk engine integration (FastAPI sync call before execution)
- [ ] Event emission (venture.* Kafka topics)

### Phase 4: Risk Agent & Constraints (Week 3)
- [ ] Build risk monitor agent (LangGraph)
- [ ] Implement rules engine (constraints.json evaluation)
- [ ] Capital allocation logic
- [ ] Escalation workflow

### Phase 5: Integration & Observability (Week 4)
- [ ] Postgres event_log schema + sync handlers
- [ ] DuckDB materialized views for analytics
- [ ] Neo4j sync job (event_log → relationships)
- [ ] Grafana dashboards (venture KPIs, agent health, event throughput)
- [ ] Prometheus metrics (agent_decisions_total, execution_duration_ms, risk_checks_passed)
- [ ] Slack notifications for escalations

### Phase 6: Production Readiness (Week 5)
- [ ] Docker/Kubernetes manifests
- [ ] Load test (712 venture agents on single Kafka cluster)
- [ ] Failure recovery tests (Postgres/Kafka failover)
- [ ] Go/no-go decision

---

## 📞 Common Questions for Implementation

**Q: "What's the Kafka partition strategy?"**
A: `partition_key = venture_id` — ensures all events for one venture go to same partition, preserving order

**Q: "How do we handle agent state recovery?"**
A: Postgres event_log is immutable; last checkpoint stored in Redis; agent restarts, replays from checkpoint

**Q: "What's the max event payload size?"**
A: 1MB (Kafka default); use compression for larger events

**Q: "How do we scale to 712 venture agents?"**
A: Temporal handles orchestration + scheduling; Kafka partitions by venture_id (712 partitions); each agent is a separate Temporal worker

**Q: "What's the observability contract?"**
A: Prometheus metrics → Grafana dashboards + Slack alerts on threshold breach

