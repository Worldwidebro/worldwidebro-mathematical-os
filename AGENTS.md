# Agent Instructions: OS-001 Mathematical Operating System

## Overview
Decision engine that queries existing formulas from 1,600+ repos + stdlib, chains them into agent-executable workflows, and learns from outcomes.

**Not** a formula library. **Query + execute + learn.**

## Package Manager
Use **Python 3.12+ with uv**: `uv sync`, `uv run python`

## File-Scoped Commands
| Task | Command |
|------|---------|
| Type check | `uv run pyright path/to/file.py` |
| Lint | `uv run ruff check path/to/file.py` |
| Test | `uv run pytest path/to/file.py -v` |
| Format | `uv run ruff format path/to/file.py` |

## Commit Attribution
AI commits MUST include:
```
Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

## Architecture
- `formula_retriever.py` — Query Neo4j: "which repos implement X?"
- `decision_executor.py` — Run formula with inputs, log outcome
- `learning_loop.py` — Compare predictions vs actuals, update playbooks
- `supabase/migrations/` — Schema for formulas, results, decisions

## Key Conventions
1. **Never implement** what a starred repo already does. Query it first.
2. **Every formula execution** logs: query → repo choice → inputs → output → outcome
3. **Decisions are auditable**: who asked, which formula, why, what happened
4. **Learning loop runs weekly**: formula accuracy vs actuals, cascade updates to playbooks

## Dependencies
- `supabase-py` — Supabase sync
- `neo4j` — Repo graph queries
- `pydantic` — Formula schemas
- `pytest` — Testing

## Success Criteria
- ✅ Agents can ask "calculate X" → system finds best repo + formula + executes
- ✅ Every decision logged with outcome (for learning)
- ✅ Weekly playbook updates based on actual results
- ✅ Zero custom reimplementation of existing formulas
