# Cursor Implementation Rules — AI Boss OS

## Before Writing Any Code

1. Check if schema exists in `../agents-os/shared/schemas/`
2. Read contracts in `../agents-os/shared/CONTRACTS-SUMMARY.md`
3. Verify event types in `events/schemas/event_types.json` (or CONTRACTS-SUMMARY § Event Types)
4. Ask: *"What are the state transitions for this component?"*

## Code Style

- Terse comments — explain **why**, not obvious **what**
- Type hints on all functions
- Docstring = contract + minimal example
- No abstractions beyond what the task requires
- JSON Schema validation on registry and event payloads

## Parallel Work (Safe to Do Concurrently)

- Multiple agent implementations (separate files, no shared mutable state)
- Kafka consumers (one per topic / consumer group)
- Registry loaders (independent JSON/YAML files)
- Grafana dashboard JSON files

## Do NOT Do

- ❌ Direct DB mutations from agents (only via Kafka → consumer → Postgres)
- ❌ Skip risk engine validation before execution
- ❌ Hardcode config (use `core/config/system_config.yaml` + env vars)
- ❌ Create abstractions "for future scaling"
- ❌ Error handling for impossible edge cases

## Every Agent File Must

1. Inherit from `agents/agent_base.py`
2. Implement `state_machine()` (or equivalent LangGraph graph builder)
3. Emit events to Kafka — not direct DB writes
4. Call `risk_engine.validate()` (or risk agent client) before execution
5. Emit structured logs; metrics via Prometheus consumer (not inline DB metrics tables)

## Repo Layout

```
ai-boss-os/          ← you are here (implementation)
agents-os/           ← contracts + schemas (read-only reference)
venture-hub/         ← ventures-master.csv, MAS/CrewAI router (sibling)
```

## Phase Gate

- Phase 1 complete → Phase 2 agents
- Event schemas + Kafka topics → producers/consumers
- Postgres schema → `postgres_consumer`
- Do not ship venture agents before `agent_base.py` + event pipeline exist
