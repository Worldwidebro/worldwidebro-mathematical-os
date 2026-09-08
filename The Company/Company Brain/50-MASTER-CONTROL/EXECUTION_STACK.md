---
id: CTRL-EXEC-001
title: Company Brain Execution Stack
aliases: ["EXECUTION_STACK", "Company Brain Execution Stack", "50-MASTER-CONTROL/EXECUTION_STACK"]
tags: ["execution-stack", "graft", "fractal", "herdr", "multi-agent", "runtime"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] | [[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING|55-LOOP-ENGINEERING]] | [[57-CODE-INTELLIGENCE/57-CODE-INTELLIGENCE|57-CODE-INTELLIGENCE]] | [[REALITY]]

# Company Brain Execution Stack

> **Authority:** Master Control Plane (CP-050) & Execution Architecture  
> **Status:** ✅ Architecture Integrated & Reconciled (2026-09-06)  
> **Related:** [[50-MASTER-CONTROL/SEVEN_PLANES|SEVEN_PLANES]] | [[50-MASTER-CONTROL/HUNDRED_LAYERS|HUNDRED_LAYERS]] | [[50-MASTER-CONTROL/CONTROL_MATRIX|CONTROL_MATRIX]] | [[57-CODE-INTELLIGENCE/GRAFT_INTEGRATION|GRAFT_INTEGRATION]] | [[55-LOOP-ENGINEERING/FRACTAL_INTEGRATION|FRACTAL_INTEGRATION]] | [[55-LOOP-ENGINEERING/LOOP_ENGINEERING|LOOP_ENGINEERING]] | [[09-KNOWLEDGE/Utopia-World-Model|Utopia World Model]]

---

## The Complete Autonomous Execution Stack

```
                  COMPANY BRAIN
              Organizational intelligence
                        │
           ┌────────────┴────────────┐
           │                         │
    GOAL / DECISION             KNOWLEDGE LAYER
    (What should happen?)       [[Neo4j]] | [[Qdrant]]
           │                         │
           └────────────┬────────────┘
                        ▼
                  WORK DISCOVERY
            (Identify autonomous opportunities)
                        │
        ┌───────────────┴───────────────┐
        │                               │
  [[LOOP_ENGINEERING]]            [[FRACTAL_INTEGRATION]]
  (Continuous loops)         (Recursive decomposition)
        │                               │
        └───────────────┬───────────────┘
                        ▼
              AGENT ORCHESTRATOR
                        │
        ┌───────────────┼───────────────┐
        │               │               │
    [[SKILLS]]      [[GRAFT]]       [[MODELS]]
    (How-to)     (Code Context)  (Reasoning)
        │               │               │
        └───────────────┼───────────────┘
                        ▼
            [[HERDR_INTEGRATION]]
              (Persistent Runtime)
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
         Claude            Codex / Other
              │                   │
              └─────────┬─────────┘
                        ▼
              MCP / APIs / Tools
                        │
                        ▼
                      CODE
                        │
            ┌───────────┼───────────┐
            ▼           ▼           ▼
         TEST        RUN        VERIFY
                        │
                   APPROVAL
                        │
            ┌───────────┴───────────┐
            ▼                       ▼
         MERGE                   DEPLOY
            │                       │
            └───────────┬───────────┘
                        ▼
                    METRICS
                        │
                    OUTCOME
                        │
                    LEARNING
                        │
                        ▼
                  COMPANY BRAIN
             (Updated knowledge base)
```

---

## The Four Layers

### 1. **Work Discovery** (`L1: Report Only`)

[[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING|Loop Engineering]] continuously discovers work that should happen.

**Examples:**
- "Audit all repositories"
- "Classify ventures by risk"
- "Find reusable code components"

**Autonomy:** Loop proposes work to human, human confirms.

---

### 2. **Work Decomposition** (`Fractal`)

If work is large, [[FRACTAL_INTEGRATION]] recursively decomposes it into a hierarchy of agents.

**Example: Audit all repositories**

```
                  ROOT: Audit 1600 repos
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
     LT Auditor        CON Auditor        FIN Auditor
        │                  │                  │
    ┌───┼───┐          ┌───┼───┐         ┌───┼───┐
    ▼   ▼   ▼          ▼   ▼   ▼         ▼   ▼   ▼
   R1  R2  R3         R4  R5  R6         R7  R8  R9
```

**Fractal provides:**
- Hierarchical decomposition
- Worktree isolation (Git branches per agent)
- Execution state tracking
- Budget limits (cost, time, depth)
- Iteration control
- Signal passing between agents

**Autonomy:** L1 (report) → L2 (assisted, after verification) → L3 (autonomous, within policy)

---

### 3. **Code Understanding** (`Graft`)

Each agent needs to understand the code it's working with. [[GRAFT_INTEGRATION]] provides persistent code context.

**Graft generates:**
- `CODE_GRAPH` — Symbols, functions, classes
- `CODE_NODE` — Individual symbols
- `CODE_EDGE` — Call relationships
- `DEPENDENCY` — External/internal deps
- `BLAST_RADIUS` — Impact analysis

**Instead of:**
```
Audit Agent
  → "What's in this repo?"
  → Read README
  → Grep for patterns
  → (50 tool calls to understand repo)
  → NOW start actual work
```

**With Graft:**
```
Audit Agent
  → Load code graph (2s)
  → Understand architecture (1 tool call)
  → Start work
```

**Autonomy:** Agents don't rediscover code every session.

---

### 4. **Agent Execution** (`herdr`)

Where do agents actually run? [[HERDR_INTEGRATION]] owns that.

**herdr provides:**
- Persistent terminals/sessions
- Pane management
- Session reattachment (if interrupted)
- Agent-to-agent interaction (tmux escape sequences)
- Runtime visibility (which agent is blocked?)

**Important:** herdr is **not** the hierarchy (that's Fractal). It's the **substrate**.

Think of it like:
- **Fractal** = organizational chart (who reports to whom)
- **herdr** = office building (where people work)
- **Graft** = shared knowledge base (what you know about the code)

---

## IDs and Registration

### Tools Registered

| ID | Tool | Type | Purpose | Base |
|---|---|---|---|---|
| `TOL-000001` | [[GRAFT_INTEGRATION]] | Code Intelligence | Understand code | 57-CODE-INTELLIGENCE |
| `TOL-000002` | [[FRACTAL_INTEGRATION]] | Agent Orchestration | Recursive decomposition | 55-LOOP-ENGINEERING |
| `TOL-000003` | [[HERDR_INTEGRATION]] | Agent Runtime | Persistent sessions | 22-EXECUTION |

### Object Types

**Execution Runtime Objects:**
- `ANO` — Agent Node (single agent in hierarchy)
- `ATR` — Agent Tree (whole Fractal tree)
- `ARN` — Agent Run (single execution)
- `AIT` — Agent Iteration (loop within run)
- `AST` — Agent Step (individual action)
- `ASG` — Agent Signal (parent/child comm)
- `WRT` — Worktree (Git isolation)
- `EBD` — Execution Budget (cost/time limits)
- `EXP` — Execution Policy (autonomy level)

**Code Intelligence Objects:**
- `CBD` — Codebase (repository)
- `CGP` — Code Graph (Graft output)
- `CND` — Code Node (symbol/function)
- `CED` — Code Edge (call/dependency)
- `MOD` — Module (code module)
- `SYM` — Symbol (extractable identifier)
- `DEP` — Dependency (external lib)
- `BLR` — Blast Radius (impact analysis)

---

## Execution Policies (Autonomy Levels)

Fractal respects these policies:

### L0: Read-Only Intelligence

```yaml
filesystem: read_only
network: restricted
git_write: false
auto_execute: true
approval_required: false
examples:
  - Code analysis
  - Repository audits
  - Report generation
```

### L1: Assisted Execution

```yaml
filesystem: worktree_only
network: restricted
git_write: branch_only
auto_execute: true
approval_required: false
merge_required: true
examples:
  - Dependency updates
  - Security patches
  - Code refactoring
```

### L2: Bounded Autonomous

```yaml
filesystem: sandbox
network: allowlist
git_write: branch_only
auto_execute: true
max_cost_usd: 10
max_depth: 3
max_children: 5
max_iterations: 20
approval_required: false
merge_required: true
examples:
  - Feature development
  - Bug fixes (limited scope)
  - Performance optimization
```

### L3: Production Automation

```yaml
filesystem: sandbox
network: allowlist
git_write: branch_only
approval_required: true
deployment_approval_required: true
examples:
  - Release automation
  - Emergency incident response
  - Critical infrastructure changes
```

**Key principle:** [[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING|Loop Engineering]] starts at L1. Graduate to L2/L3 **only after verification proves reliable**.

---

## Key Relationships

**Agent Hierarchy:**
```
[[FRACTAL_INTEGRATION]]: ANO PARENT_OF ANO (tree structure)
                          ANO SPAWNS_AGENT ANO (recursive)
                          ANO PART_OF_TREE ATR
```

**Execution:**
```
ANO EXECUTES_RUN ARN
ARN HAS_ITERATION AIT
AIT HAS_STEP AST
ANO SIGNALS ANO (parent/child communication)
```

**Constraints:**
```
ANO HAS_BUDGET EBD (cost, time, depth)
ANO GOVERNED_BY EXP (autonomy policy)
```

**Code Intelligence:**
```
CBD HAS_CODE_GRAPH CGP
CGP CONTAINS_CODE_NODE CND
CND CALLS CND (call graph)
CND DEPENDS_ON_CODE DEP
CND IMPLEMENTS_CODE CAP
```

**Impact:**
```
ANO HAS_BLAST_RADIUS BLR
BLR AFFECTS_REPOSITORY REP
BLR AFFECTS_REPOSITORY VEN
BLR AFFECTS_REPOSITORY CAP
```

---

## Deployment Checklist

- [ ] Graft 0.16.0+ installed (`npm install -g @nanonets/graft`)
- [ ] Fractal 1.1.0+ installed (Apache-2.0 license)
- [ ] herdr installed (persistent runtime)
- [ ] Neo4j graph initialized with object types
- [ ] Execution policies documented in governance base
- [ ] Cost accounting integrated (Fractal tracks model usage)
- [ ] Sandbox/worktree isolation verified
- [ ] L1 (report-only) loops operational
- [ ] L2 budget limits configured
- [ ] Verification gates in place before L3 deployment

---

## Next Steps

1. **Test L1 discovery loop** — Does [[55-LOOP-ENGINEERING/55-LOOP-ENGINEERING|Loop Engineering]] find real work?
2. **Integrate Graft** — Can agents understand repos in <2s?
3. **Deploy Fractal** — Can we decompose a 100-item task into agents?
4. **Add herdr** — Can agents persist across interruptions?
5. **Graduate autonomy** — Move from L1 to L2 as verification proves reliable
6. **Production readiness** — Before L3, ensure approval gates work

---

**See also:**
- [[INDEX]] — Wiki index
- [[10-MEMORY]] — Knowledge graph
- [[55-LOOP-ENGINEERING]] — Continuous work loops
- [[57-CODE-INTELLIGENCE]] — Code analysis
- [[22-EXECUTION]] — Execution layer
- [[32-SECURITY]] — Security policies
