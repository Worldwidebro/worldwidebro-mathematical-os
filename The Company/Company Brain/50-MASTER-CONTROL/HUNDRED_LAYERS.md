---
id: CTRL-LAYERS-100
title: Company Brain: 100-Layer Control Framework
aliases: ["HUNDRED_LAYERS", "100-Layer Control Framework", "50-MASTER-CONTROL/HUNDRED_LAYERS"]
tags: ["layers", "planes", "checkpoints", "verification", "governance"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] | [[50-MASTER-CONTROL/SEVEN_PLANES|SEVEN_PLANES]] | [[50-MASTER-CONTROL/CONTROL_MATRIX|CONTROL_MATRIX]] | [[REALITY]]

# Company Brain: 100-Layer Control Framework

> **Authority:** Master Control Plane (CP-050)  
> **Status:** ✅ Framework Defined & Reconciled (2026-09-06)  
> **Related:** [[50-MASTER-CONTROL/SEVEN_PLANES|SEVEN_PLANES]] | [[50-MASTER-CONTROL/CONTROL_MATRIX|CONTROL_MATRIX]] | [[50-MASTER-CONTROL/EXECUTION_STACK|EXECUTION_STACK]]

---

## Architecture: 50 Domains × 7 Planes × ~100 Control Points

```
Each of 50 domains (00-50) is present in each of 7 planes.
That creates ~350 domain-plane intersections.
Within each intersection are 2-4 control points.
Total: ~100-150 distinct control points mapped.
```

---

## Layer Hierarchy (Sample Structure)

### Plane 1: Company Brain

| Layer | Domain | Control Point | Status | Tool |
|-------|--------|---|---|---|
| 1.1 | 00-CONSTITUTION | Define mission | ✅ | Neo4j |
| 1.2 | 00-CONSTITUTION | Set principles | ✅ | Neo4j |
| 1.3 | 01-IDENTITY | Define organizational structure | ✅ | Qdrant |
| 1.4 | 20-DECISIONS | Record strategic decisions | ✅ | Neo4j |
| 1.5 | 21-POLICY | Define governance policies | ✅ | Neo4j |
| 1.6 | 23-VENTURES | Portfolio oversight | ✅ | Neo4j |

---

### Plane 2: Engineering Brain

| Layer | Domain | Control Point | Status | Tool |
|-------|--------|---|---|---|
| 2.1 | 13-REPOSITORIES | Define architecture standards | 🟡 | Graft |
| 2.2 | 13-REPOSITORIES | Repository health checks | 🟡 | Graft |
| 2.3 | 15-SKILLS | Code quality standards | 🔴 | — |
| 2.4 | 18-TOOLS | Tool integration requirements | 🟡 | TOL-000001 |
| 2.5 | 32-SECURITY | Security scanning gates | 🟡 | — |
| 2.6 | 33-COMPLIANCE | Compliance verification | 🟡 | — |

---

### Plane 3: Knowledge Fabric

| Layer | Domain | Control Point | Status | Tool |
|-------|--------|---|---|---|
| 3.1 | 08-KNOWLEDGE-GRAPH | Neo4j entity creation | ✅ | Neo4j |
| 3.2 | 08-KNOWLEDGE-GRAPH | Relationship mapping | ✅ | Neo4j |
| 3.3 | 09-KNOWLEDGE | Knowledge source ingestion | 🟡 | Qdrant |
| 3.4 | 10-MEMORY | Semantic memory (embeddings) | ✅ | Qdrant |
| 3.5 | 11-INDEXING | Full-text indexing | 🟡 | — |
| 3.6 | 13-REPOSITORIES | Code graph generation | ✅ | Graft (TOL-000001) |

---

### Plane 4: Orchestration Fabric

| Layer | Domain | Control Point | Status | Tool |
|-------|--------|---|---|---|
| 4.1 | 55-LOOP-ENGINEERING | Work discovery loop | ✅ | Loop Engine |
| 4.2 | 55-LOOP-ENGINEERING | Loop execution (L1/L2/L3) | ✅ | Loop Engine |
| 4.3 | 14-CAPABILITIES | Capability routing | ✅ | Loop Engine |
| 4.4 | 15-SKILLS | Skill composition | 🟡 | Fractal (TOL-000002) |
| 4.5 | 16-AGENTS | Agent spawning | ✅ | Fractal (TOL-000002) |
| 4.6 | 19-ORCHESTRATION | Workflow orchestration | ✅ | Loop Engine |

---

### Plane 5: Execution Fabric

| Layer | Domain | Control Point | Status | Tool |
|-------|--------|---|---|---|
| 5.1 | 22-EXECUTION | Agent session management | ✅ | herdr (TOL-000003) |
| 5.2 | 22-EXECUTION | Terminal pane management | ✅ | herdr (TOL-000003) |
| 5.3 | 22-EXECUTION | Git worktree isolation | ✅ | herdr (TOL-000003) |
| 5.4 | 22-EXECUTION | Cost tracking | 🟡 | Fractal (TOL-000002) |
| 5.5 | 49-SYSTEM | Process lifecycle | ✅ | herdr (TOL-000003) |
| 5.6 | 41-OBSERVABILITY | Runtime state visibility | 🟡 | — |

---

### Plane 6: Verification Fabric

| Layer | Domain | Control Point | Status | Tool |
|-------|--------|---|---|---|
| 6.1 | 31-LEGAL | Legal compliance gates | 🟡 | — |
| 6.2 | 32-SECURITY | Security scanning (SAST) | 🟡 | — |
| 6.3 | 32-SECURITY | Security scanning (DAST) | 🟡 | — |
| 6.4 | 33-COMPLIANCE | Compliance verification | 🟡 | — |
| 6.5 | 42-EVALUATION | Code review gates | 🟡 | — |
| 6.6 | 42-EVALUATION | Test coverage validation | 🟡 | — |

---

### Plane 7: Operations Fabric

| Layer | Domain | Control Point | Status | Tool |
|-------|--------|---|---|---|
| 7.1 | 41-OBSERVABILITY | Log aggregation | 🟡 | — |
| 7.2 | 41-OBSERVABILITY | Distributed tracing | 🟡 | — |
| 7.3 | 41-OBSERVABILITY | Metrics collection | 🟡 | — |
| 7.4 | 43-OUTCOMES | Outcome tracking | 🟡 | Neo4j |
| 7.5 | 44-LEARNING | Lesson extraction | 🟡 | Qdrant |
| 7.6 | 45-EVOLUTION | Continuous improvement | 🟡 | — |

---

## Status Legend

| Icon | Meaning |
|---|---|
| ✅ | Implemented |
| 🟡 | Planned / Partial |
| 🔴 | Missing / Gap |

---

## Tool Coverage

| Tool | Layers | Domains |
|---|---|---|
| **Graft** (TOL-000001) | 2.1, 2.2, 3.6 | 13-REPOSITORIES, 13-REPOSITORIES, 13-REPOSITORIES |
| **Fractal** (TOL-000002) | 4.4, 4.5, 5.4 | 15-SKILLS, 16-AGENTS, 22-EXECUTION |
| **herdr** (TOL-000003) | 5.1-5.3, 5.5 | 22-EXECUTION, 22-EXECUTION, 49-SYSTEM |
| **Neo4j** | 1.1, 1.2, 1.4, 1.5, 3.1, 3.2, 7.4 | Multiple |
| **Qdrant** | 1.3, 3.3, 3.4, 7.5 | Multiple |
| **Loop Engine** | 4.1-4.3, 4.6 | 55-LOOP-ENGINEERING, 14-CAPABILITIES, 19-ORCHESTRATION |

---

**See also:** [[SEVEN_PLANES]] | [[CONTROL_MATRIX]]
