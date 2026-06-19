# AI Boss OS Implementation Guide for Cursor

## System Architecture

Read these files **FIRST** (in order):

1. `README.md` — 13-layer overview
2. `../agents-os/shared/CONTRACTS-SUMMARY.md` — Tech stack + boundaries
3. `../agents-os/shared/schemas/agent.schema.json` — Agent contract
4. `BUILD-STATUS.md` — What to build + order
5. `CURSOR-TASKS.md` — Phase checklist (start Phase 1)

## Core Principles

- **NO direct DB writes** — agents emit events; consumers write Postgres
- **Risk engine validates ALL decisions** before execution
- **Postgres** = source of truth (`event_log`, state history tables)
- **Neo4j** relationships = derived state (async sync from events)
- **Kafka** = event backbone (`{event_type}.v1` topics)
- **All agents** are state machines (LangGraph)

## Tech Stack (Fixed)

| Layer | Technology |
|-------|------------|
| Events | Apache Kafka |
| Orchestration | Temporal + n8n |
| Agents | LangGraph (Claude API) |
| Memory | Postgres + Neo4j + Qdrant + Redis |
| Observability | Grafana + Prometheus |
| API Gateway | FastAPI |
| Auth | Vault + Keycloak + OPA |

Config lives in `core/config/system_config.yaml` — **no hardcoded connection strings**.

## Implementation Order (Strict)

### Phase 1: Registries + Bootstrap (Week 1)

1. `registries/entity_registry/entities.json` — 712 ventures ✅
2. `core/config/system_config.yaml` — Connection strings ✅
3. `core/bootstrap/init_system.py` — Schema + Kafka topics ✅
4. `events/schemas/kafka_topics.yaml` — 25 Kafka topics

### Phase 2: Core Agents (Week 2)

1. `agents/agent_base.py` — Base class + LangGraph wrapper
2. `agents/orchestration_agents/master_orchestrator.py`
3. `agents/risk_agents/anomaly_detector.py`
4. `events/producers/agent_events.py` + `events/consumers/postgres_consumer.py`

### Phase 3: Venture Agent (Week 3)

1. `agents/execution_agents/venture_agent_template.py`
2. `execution/workflows/temporal_dags/venture_scale_workflow.py`
3. `memory/postgres/schema/` — extend migrations as needed

### Phase 4: Integration (Week 4+)

1. `observability/grafana_dashboards/`
2. `docker/docker-compose.yml`
3. Tests + documentation

## Each File Must Have

- JSON Schema validation where applicable
- Docstrings with contracts
- Type hints (Python)
- Error handling (no silent failures)
- Logging at every state transition

## Do NOT Implement Without Reviewing

- `../agents-os/shared/CONTRACTS-SUMMARY.md` — boundaries for the component
- `../agents-os/shared/schemas/` — data contracts
- Failure model in CONTRACTS-SUMMARY.md for that component

## When Stuck

1. Check if schema exists in `../agents-os/shared/schemas/`
2. Check event schema in `events/schemas/event_types.json`
3. Check state machine diagram in `BUILD-STATUS.md`
4. Ask: *"What are the system boundaries for this component?"*

## How Cursor Should Approach Each File

### 1. Registry files (JSON/YAML)

Load data from CSVs:

- `../venture-hub/ventures-master.csv` → `registries/entity_registry/entities.json`
- Sector mapping via `../venture-hub/registries/sector_code_mapping.json`
- Validate against `registries/entity_registry/schema.json` and `../agents-os/shared/schemas/`

### 2. Agent files (Python)

```python
from agents.agent_base import BaseAgent

class VentureAgent(BaseAgent):
    def state_machine(self):
        """IDLE → LOAD_CONTEXT → REASONING → RISK_VALIDATION → EXECUTION → IDLE"""

    async def reasoning_loop(self, event):
        """Claude API via LangGraph"""

    async def validate_with_risk_engine(self, decision):
        """Call risk engine before execution"""

    async def emit_event(self, event_type: str, payload: dict):
        """Emit to Kafka — NOT direct DB write"""
```

### 3. Workflow files (Temporal)

```python
from temporalio import workflow

@workflow.defn
class VentureScaleWorkflow:
    @workflow.run
    async def run(self, venture_id: str) -> dict:
        # 1. Validate constraints
        # 2. Transfer capital
        # 3. Emit event (consumer updates state)
        # 4. Return result
```

### 4. Schema files (SQL)

Immutable append-only tables:

- `event_log`
- `venture_state_history`
- `agent_state_history`

No `UPDATE` on event tables except bootstrap seed.

### 5. Consumer files (Python)

```python
# Kafka consumer → Postgres event_log → Redis cache → Prometheus metric
# Neo4j sync is async (separate consumer), not inline in agent
```

## Bootstrap Commands

```bash
python3 scripts/load_entity_registry.py
python3 core/bootstrap/init_system.py          # dry-run
python3 core/bootstrap/init_system.py --apply  # needs Postgres + Kafka
```

## Summary Prompt

> Build AI Boss OS following `CURSOR-TASKS.md` (Phase 1 first). Read `../agents-os/shared/CONTRACTS-SUMMARY.md` before any code. Use `system_config.yaml`. Events only. Risk engine before execution. Every agent is a state machine. Schema validation + type hints required.
