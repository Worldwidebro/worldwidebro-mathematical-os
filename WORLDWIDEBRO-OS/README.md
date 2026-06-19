# WORLDWIDEBRO-OS

The single canonical operating system for Worldwidebro Holdings — a unified
**Holdings OS + Dynasty Trust OS + Venture Studio OS + Agent OS**.

> This folder is the **one root**. It replaces the ~22 competing "OS/holdings/studio"
> folders that previously lived at the root of `~/Documents`. See `findings.md` (repo root)
> for the migration map and `task_plan.md` for consolidation status.

## The hierarchy (authority flows downward)

```
00-COMMAND      → what matters RIGHT NOW (priorities, decisions, briefings)
00-DIRECTIVES   → the laws of the system (mission, principles, directives)
01-EXECUTIVES   → decision-makers & mandates (CEO/CFO/COO/CTO/CIO/CMO/CLO/CoS)
02-GOVERNANCE   → holdings charter, dynasty trust, committees
03-PORTFOLIO    → 18 OPCOs + ventures (active/incubating/acquired/archived)
04-OPERATIONS   → departments, workflows, SOPs
05-AGENTS       → agents + architecture/orchestration/memory/guardrails/evaluation
06-TECHNOLOGY   → repositories, infra, tools, apis, mcp, models, automations
07-KNOWLEDGE    → indexes, playbooks, frameworks, prompts, research, decisions
08-DATA         → registries (SOURCE OF TRUTH), analytics, crm, financials, graph
09-DASHBOARDS   → executive/holdings/opcos/ventures/agents/finance views
10-STATUS       → completion + status CSVs per entity
```

## How it actually connects (the part that was broken before)

Folders are a **tree** (one home per file). The business is a **graph** (a venture uses
many repos; a repo serves many ventures; an agent touches many ventures). The graph lives
in **`08-DATA/registries/`** — the `*_map.csv` files are the connective tissue. Folders just
store; **registries are the source of truth; Graphify renders the registries for navigation.**

## Rules
1. Live code repos and running infra are **registered** in `08-DATA`/`06-TECHNOLOGY`, not
   physically buried here (moving them breaks `.git` + hardcoded paths). Only docs consolidate.
2. New markdown links back to canonical references (`[[VENTURE-MASTER]]`, `[[LOOP-FRAMEWORK]]`).
3. Nothing is created at the `~/Documents` root anymore — it lands in a layer here.
