---
id: TOL-000002
aliases: ['FRACTAL_INTEGRATION', 'FRACTAL']
tags: ['fractal', 'loop-engineering', 'multi-agent', 'tool-integration']
status: LIVE_REGISTERED
updated: 2026-09-06
---

[[STARTHERE]] | [[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING|55-LOOP-ENGINEERING]] | [[55-LOOP-ENGINEERING/README|README]] | [[fractal/README|fractal/README.md]] | [[fractal/wiki/_index|fractal/wiki/_index.md]] | [[22-EXECUTION]]

# Fractal Integration (TOL-000002)

> **Tool ID:** `TOL-000002`  
> **Status:** ✅ Registered  
> **License:** Apache-2.0  
> **Version:** 1.1.0+  
> **Company Brain Base:** [[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING|55-LOOP-ENGINEERING]], [[22-EXECUTION]]  
> **Related:** [[50-MASTER-CONTROL/EXECUTION_STACK|EXECUTION_STACK]] | [[57-CODE-INTELLIGENCE/GRAFT_INTEGRATION|GRAFT_INTEGRATION]]

---

## What Fractal Does

Recursive multi-agent decomposition. Break large tasks into hierarchical agent trees.

**Example:** Audit 1600 repositories in parallel

```text
                  ROOT: Audit All
                        │
    ┌───────────────────┼───────────────────┐
    ▼                   ▼                   ▼
  LT Auditor        CON Auditor        FIN Auditor
    │                   │                   │
  R1-R50             R51-R100            R101-R150
```

---

## Key Capabilities

- Hierarchical task decomposition
- Git worktree isolation per agent
- Cost limits ($25/agent, $10/subtask)
- Depth limits (max 4 levels)
- Iteration control (max 20 per agent)
- State tracking (running/blocked/done)
- Signal passing (parent↔child communication)
- Cost accounting (model usage tracking)

---

## Object Types

| Type | ID |
|---|---|
| Agent Node | ANO |
| Agent Tree | ATR |
| Agent Run | ARN |
| Agent Iteration | AIT |
| Agent Step | AST |
| Worktree | WRT |
| Execution Budget | EBD |
| Execution Policy | EXP |

---

## Autonomy Levels (L0-L3)

```text
L0: Read-only (no approval needed)
L1: Assisted (default, no approval)
L2: Bounded autonomous (cost limits)
L3: Production (approval required)
```

**Rule:** Start L1. Graduate to L2/L3 only after verification.

---

## Key Relationships

```text
ANO PARENT_OF ANO           (hierarchy)
ANO SPAWNS_AGENT ANO        (recursive)
ANO EXECUTES_RUN ARN        (execution)
ANO HAS_BUDGET EBD          (constraints)
ANO GOVERNED_BY EXP         (autonomy)
ANO REPORTS_TO ANO | DEC    (communication)
```

---

## Connected Engine Documents
- Fractal Master Engine: [[fractal/README|fractal/README.md]]
- Fractal Wiki: [[fractal/wiki/_index|fractal/wiki/_index.md]]
- Node Charter: [[fractal/fractal/_node/NODE|NODE.md]]
- Company Brain Integration: [[fractal/wiki/architecture/company_brain_integration|company_brain_integration.md]]
- Execution Stack: [[50-MASTER-CONTROL/EXECUTION_STACK|EXECUTION_STACK]]
- Graft Integration: [[57-CODE-INTELLIGENCE/GRAFT_INTEGRATION|GRAFT_INTEGRATION]]
