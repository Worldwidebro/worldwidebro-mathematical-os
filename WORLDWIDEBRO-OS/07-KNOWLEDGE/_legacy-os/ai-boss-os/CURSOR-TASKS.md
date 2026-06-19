# Cursor Implementation Checklist

**Repo:** `Documents/ai-boss-os`  
**Contracts:** `Documents/agents-os/shared/`  
**Venture data:** `Documents/venture-hub/ventures-master.csv` (712 rows)

---

## PHASE 1: REGISTRIES + BOOTSTRAP (Start here)

### Registries (10 files)

- [x] `registries/entity_registry/entities.json` — 712 ventures from `venture-hub/ventures-master.csv`
- [x] `registries/entity_registry/relationships.graph` — 712 venture → sector edges
- [x] `registries/entity_registry/schema.json` — entity contract
- [ ] `registries/agent_registry/agents.yaml` — 6 agents: orchestrator, venture, risk, capital, intelligence, execution
- [ ] `registries/event_registry/event_schemas.json` — 25 event types from CONTRACTS-SUMMARY.md
- [ ] `registries/event_registry/topics.yaml` — Kafka topic config
- [ ] `registries/capital_registry/allocation_rules.json`
- [ ] `registries/risk_registry/failure_modes.yaml`
- [ ] `registries/kpi_registry/metrics.yaml`
- [ ] `registries/tool_registry/mcp_tools.yaml`
- [ ] `registries/model_registry/llm_models.yaml`

### Core System (5 files)

- [x] `core/config/system_config.yaml` — Kafka, Postgres, Neo4j, Redis URLs (env placeholders)
- [x] `core/config/system_config.yaml.example`
- [x] `core/config/feature_flags.yaml`
- [ ] `core/config/environment_vars.env` — template only (secrets in `~/.env`)
- [x] `core/bootstrap/init_system.py` — Postgres schema + Kafka topics + entity seed
- [ ] `core/bootstrap/start_services.sh` — docker-compose up
- [ ] `core/runtime/event_loop.py` — main orchestrator loop

### Events (Phase 1 tail)

- [ ] `events/schemas/kafka_topics.yaml` — 25 topics (mirror init_system.py list)
- [ ] `events/schemas/event_types.json` — canonical 25-type schema

### Loader

- [x] `scripts/load_entity_registry.py` — regenerate entities + relationships

---

## PHASE 2: AGENTS + EVENTS (Week 2)

### Agent Base + Orchestrator (3 files)

- [ ] `agents/agent_base.py` — LangGraph wrapper class
- [ ] `agents/orchestration_agents/master_orchestrator.py` — spawn / coordinate venture agents
- [ ] `agents/orchestration_agents/task_router.py`

### Risk Agent (2 files)

- [ ] `agents/risk_agents/anomaly_detector.py`
- [ ] `agents/risk_agents/rollback_agent.py`

### Event System (5 files)

- [ ] `events/producers/agent_events.py`
- [ ] `events/consumers/postgres_consumer.py` — write `event_log`
- [ ] `events/consumers/neograph_consumer.py` — update Neo4j (derived)
- [ ] `events/consumers/metrics_consumer.py` — Prometheus
- [ ] `events/consumers/slack_consumer.py` — notifications

### Memory (3 files)

- [x] `memory/postgres/schema/001_event_log.sql` — event_log + state history
- [x] `memory/postgres/schema/002_ventures.sql` — ventures + sectors
- [ ] `memory/graph_db/neo4j_models.cypher`
- [ ] `memory/cache/redis_config.yaml`

---

## PHASE 3: VENTURE AGENT + WORKFLOWS

- [ ] `agents/execution_agents/venture_agent_template.py` — IDLE → REASONING → EXECUTING
- [ ] `execution/workflows/temporal_dags/venture_scale_workflow.py`
- [ ] `execution/workflows/temporal_dags/venture_kill_workflow.py`

---

## PHASE 4: OBSERVABILITY + DEPLOYMENT

- [ ] `observability/grafana_dashboards/system_health.json`
- [ ] `observability/grafana_dashboards/venture_kpis.json`
- [ ] `observability/grafana_dashboards/risk_monitor.json`
- [ ] `docker/docker-compose.yml`
- [ ] `docker/Dockerfile.orchestrator`

---

## Dependencies

| Blocker | Blocked |
|---------|---------|
| Phase 1 registries + config | Phase 2 agents |
| `event_types.json` + Kafka topics | Producers / consumers |
| Postgres schema (`001`, `002`) | `postgres_consumer` |
| `agent_base.py` | All concrete agents |
| Event pipeline | Venture agent live execution |

---

## Progress

| Phase | Done | Total (listed) |
|-------|------|----------------|
| Phase 1 | 9 | ~18 |
| Phase 2 | 2 | 13 |
| Phase 3 | 0 | 3 |
| Phase 4 | 0 | 5 |

See `BUILD-STATUS.md` for full ~125-file breakdown.

---

## Cursor Entry Command

```
Build AI Boss OS following CURSOR-TASKS.md (Phase 1 remaining items first).
Read ../agents-os/shared/CONTRACTS-SUMMARY.md before any code.
Use core/config/system_config.yaml — no hardcoding.
Events only — no direct DB writes from agents.
Validate with risk engine before execution.
Every agent is a state machine.
Schema validation on all inputs.
Type hints + docstring contracts required.
Refer to ../agents-os/shared/schemas/ for contracts.
```
