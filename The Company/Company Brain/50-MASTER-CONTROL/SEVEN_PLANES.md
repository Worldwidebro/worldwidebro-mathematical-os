---
id: CTRL-PLANES-007
title: Company Brain: 7-Plane Architecture
aliases: ["SEVEN_PLANES", "7-Plane Architecture", "50-MASTER-CONTROL/SEVEN_PLANES"]
tags: ["planes", "architecture", "planes-of-operation", "governance", "domains"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] | [[50-MASTER-CONTROL/HUNDRED_LAYERS|HUNDRED_LAYERS]] | [[50-MASTER-CONTROL/CONTROL_MATRIX|CONTROL_MATRIX]] | [[REALITY]]

# Company Brain: 7-Plane Architecture

> **Authority:** Master Control Plane (CP-050)  
> **Status:** ✅ Formalized & Reconciled (2026-09-06)  
> **Related:** [[50-MASTER-CONTROL/EXECUTION_STACK|EXECUTION_STACK]] | [[50-MASTER-CONTROL/HUNDRED_LAYERS|HUNDRED_LAYERS]] | [[50-MASTER-CONTROL/CONTROL_MATRIX|CONTROL_MATRIX]]

---

## The 7 Planes

```
┌──────────────────────────────────────────────────┐
│ Plane 1: COMPANY BRAIN                           │
│ Organizational intelligence, goals, decisions    │
└──────────────────────────────────────────────────┘
              ↓
┌──────────────────────────────────────────────────┐
│ Plane 2: ENGINEERING BRAIN (AST-100)             │
│ Architecture, testing, security, delivery        │
└──────────────────────────────────────────────────┘
              ↓
┌──────────────────────────────────────────────────┐
│ Plane 3: KNOWLEDGE FABRIC                        │
│ Neo4j, Qdrant, Graft, sources, memory, embeddings│
└──────────────────────────────────────────────────┘
              ↓
┌──────────────────────────────────────────────────┐
│ Plane 4: ORCHESTRATION FABRIC                    │
│ Loop Engine, Fractal, agents, skills, workflows  │
└──────────────────────────────────────────────────┘
              ↓
┌──────────────────────────────────────────────────┐
│ Plane 5: EXECUTION FABRIC                        │
│ herdr, terminals, worktrees, processes, sessions │
└──────────────────────────────────────────────────┘
              ↓
┌──────────────────────────────────────────────────┐
│ Plane 6: VERIFICATION FABRIC                     │
│ Tests, security scan, CI, code review, approval  │
└──────────────────────────────────────────────────┘
              ↓
┌──────────────────────────────────────────────────┐
│ Plane 7: OPERATIONS FABRIC                       │
│ Deploy, observe, incident response, recovery     │
└──────────────────────────────────────────────────┘
```

---

## Plane Definitions

### Plane 1: Company Brain
**Purpose:** Organizational intelligence and decision-making authority.

**Responsibilities:**
- Strategy and goals definition
- Decision-making and approval authority
- Policy setting and governance
- Risk management and compliance
- Portfolio oversight
- Financial planning and tracking

**Tools:** Neo4j, Qdrant, decision registries
**Bases:** 00-CONSTITUTION, 01-IDENTITY, 20-DECISIONS, 21-POLICY

---

### Plane 2: Engineering Brain (AST-100)
**Purpose:** Software delivery discipline and engineering governance.

**Responsibilities:**
- Architecture definition and validation
- Code quality standards
- Testing requirements and verification
- Security scanning and compliance
- Performance benchmarking
- Change management and release gating

**Tools:** Graft (TOL-000001), CI/CD systems
**Bases:** 13-REPOSITORIES, 18-TOOLS, 32-SECURITY, 33-COMPLIANCE

---

### Plane 3: Knowledge Fabric
**Purpose:** Unified organizational knowledge and semantic memory.

**Responsibilities:**
- Relationship graph (Neo4j)
- Semantic search (Qdrant)
- Code graph generation (Graft)
- Documentation and wikis
- Memory systems (episodic, semantic, procedural)
- Source attribution and evidence

**Tools:** Neo4j, Qdrant, Graft (TOL-000001)
**Bases:** 08-KNOWLEDGE-GRAPH, 09-KNOWLEDGE, 10-MEMORY, 11-INDEXING

---

### Plane 4: Orchestration Fabric
**Purpose:** Work discovery, planning, and agent coordination.

**Responsibilities:**
- Continuous work discovery (Loop Engine)
- Hierarchical task decomposition (Fractal)
- Agent orchestration and routing
- Skill composition and workflow definition
- Goal-to-action planning
- Work prioritization

**Tools:** Loop Engine, Fractal (TOL-000002)
**Bases:** 55-LOOP-ENGINEERING, 14-CAPABILITIES, 15-SKILLS, 16-AGENTS, 19-ORCHESTRATION

---

### Plane 5: Execution Fabric
**Purpose:** Persistent agent runtime and workspace management.

**Responsibilities:**
- Agent session management (herdr)
- Terminal and pane management
- Git worktree isolation
- Process lifecycle management
- Cost tracking (tokens, compute, time)
- State persistence across disconnects

**Tools:** herdr (TOL-000003), tmux, git
**Bases:** 22-EXECUTION, 49-SYSTEM, 41-OBSERVABILITY

---

### Plane 6: Verification Fabric
**Purpose:** Quality gates and confidence verification.

**Responsibilities:**
- Unit testing and integration testing
- Code review and approval gates
- Static analysis and linting
- Security scanning (SAST, DAST)
- Performance testing
- Regression detection
- Compliance verification

**Tools:** Test frameworks, scanners, CI gates
**Bases:** 31-LEGAL, 32-SECURITY, 33-COMPLIANCE, 42-EVALUATION

---

### Plane 7: Operations Fabric
**Purpose:** Deployment, monitoring, and incident response.

**Responsibilities:**
- Deployment orchestration and rollback
- Runtime observability (logs, traces, metrics)
- Incident detection and response
- Service health monitoring
- Capacity management
- Disaster recovery

**Tools:** Observability stack, deployment systems
**Bases:** 41-OBSERVABILITY, 43-OUTCOMES, 44-LEARNING, 45-EVOLUTION

---

## Control Flow

**Forward:** Goals → Constraints → Context → Work → Runtime → Verification → Deployment

**Feedback:** Outcomes → Metrics → Results → Lessons → Decision Memory

---

**See also:** [[EXECUTION_STACK]] | [[HUNDRED_LAYERS]] | [[CONTROL_MATRIX]]
