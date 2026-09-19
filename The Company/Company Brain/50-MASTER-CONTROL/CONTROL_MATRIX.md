---
id: CTRL-MTX-001
title: Company Brain Control Matrix Guide
aliases: ["CONTROL_MATRIX", "Control Matrix Guide", "50-MASTER-CONTROL/CONTROL_MATRIX"]
tags: ["control-matrix", "planes", "layers", "governance", "neo4j", "qdrant"]
status: ACTIVE
updated: 2026-09-19
---

[[STARTHERE]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] | [[00-CONSTITUTION/CONTROL_PLANES_MASTER|Control Planes Master]] | [[_REGISTRIES/control-points/README|Control Points]] | [[50-MASTER-CONTROL/SEVEN_PLANES|SEVEN_PLANES]] | [[REALITY]]

# Control Matrix (50-MASTER-CONTROL)

> **Authority:** Master Control Plane ([[00-CONSTITUTION/control-planes/CP-050|CP-050]])  
> **Source Schema:** [[50-MASTER-CONTROL/CONTROL_MATRIX.yaml|CONTROL_MATRIX.yaml]]  
> **Dimensions:** 50 Domains × 7 Planes × 42 Control Points  
> **Status:** ACTIVE — Updated 2026-09-19

---

## 1. Overview
The **Control Matrix** specifies the operational and governance checkpoints across all 7 planes of the WorldwideBro / Company Brain architecture. It ties high-level constitutional mandates directly to machine-verifiable operational tools (Neo4j, Qdrant, Omniroute, Git, and automated CI).

---

## 2. Core Master Specifications

| Specification | Type | Scope | Target Reference |
|:---|:---|:---|:---|
| **Control Planes Master** | Architecture Directory | All 34 Control Planes | [[00-CONSTITUTION/CONTROL_PLANES_MASTER|CONTROL_PLANES_MASTER.md]] |
| **Control Points Registry** | Operational Matrix | Complete 42 Checkpoints | [[_REGISTRIES/control-points/README|Control Points Registry]] |
| **Control Matrix Source** | Structured YAML | Machine-readable definitions | [[50-MASTER-CONTROL/CONTROL_MATRIX.yaml|CONTROL_MATRIX.yaml]] |
| **Seven Planes** | Architectural Model | 7 horizontal/vertical operating tiers | [[50-MASTER-CONTROL/SEVEN_PLANES|SEVEN_PLANES.md]] |
| **Hundred Layers** | Layer Hierarchy | 100-layer checkpoint verification | [[50-MASTER-CONTROL/HUNDRED_LAYERS|HUNDRED_LAYERS.md]] |

---

## 3. Operational Control Points Matrix (42 Points)

| Plane | Domain | Control Point | Status | Tool | Responsible Role | Control Plane |
|:---|:---|:---|:---:|:---|:---|:---:|
| Company Brain — Organizational Intelligence | [[00-CONSTITUTION/README|00-CONSTITUTION]] | **Define mission** | ✅ | `Neo4j` | CEO / Board | [[00-CONSTITUTION/control-planes/CP-001|CP-001]] |
| Company Brain — Organizational Intelligence | [[00-CONSTITUTION/README|00-CONSTITUTION]] | **Set principles** | ✅ | `Neo4j` | CEO / Board | [[00-CONSTITUTION/control-planes/CP-001|CP-001]] |
| Company Brain — Organizational Intelligence | [[01-IDENTITY/README|01-IDENTITY]] | **Define organizational structure** | ✅ | `Qdrant` | COO | [[00-CONSTITUTION/control-planes/CP-002|CP-002]] |
| Company Brain — Organizational Intelligence | [[20-DECISIONS/README|20-DECISIONS]] | **Record strategic decisions** | ✅ | `Neo4j` | CEO | [[00-CONSTITUTION/control-planes/CP-005|CP-005]] |
| Company Brain — Organizational Intelligence | [[21-POLICY/README|21-POLICY]] | **Define governance policies** | ✅ | `Neo4j` | Legal / Compliance | [[00-CONSTITUTION/control-planes/CP-030|CP-030]] |
| Company Brain — Organizational Intelligence | [[23-VENTURES/README|23-VENTURES]] | **Portfolio oversight** | ✅ | `Neo4j` | Portfolio Manager | [[00-CONSTITUTION/control-planes/CP-002|CP-002]] |
| Engineering Brain (AST-100) — Software Delivery Discipline | [[13-REPOSITORIES/README|13-REPOSITORIES]] | **Define architecture standards** | 🟡 | `Graft (TOL-000001)` | CTO | [[00-CONSTITUTION/control-planes/CP-028|CP-028]] |
| Engineering Brain (AST-100) — Software Delivery Discipline | [[13-REPOSITORIES/README|13-REPOSITORIES]] | **Repository health checks** | 🟡 | `Graft (TOL-000001)` | Engineering Manager | [[00-CONSTITUTION/control-planes/CP-028|CP-028]] |
| Engineering Brain (AST-100) — Software Delivery Discipline | [[15-SKILLS/README|15-SKILLS]] | **Code quality standards** | 🔴 | `—` | Engineering Manager | [[00-CONSTITUTION/control-planes/CP-006|CP-006]] |
| Engineering Brain (AST-100) — Software Delivery Discipline | [[18-TOOLS/README|18-TOOLS]] | **Tool integration requirements** | 🟡 | `TOL-000001` | Tech Lead | [[00-CONSTITUTION/control-planes/CP-008|CP-008]] |
| Engineering Brain (AST-100) — Software Delivery Discipline | [[32-SECURITY/README|32-SECURITY]] | **Security scanning gates** | 🟡 | `—` | Security Officer | [[00-CONSTITUTION/control-planes/CP-017|CP-017]] |
| Engineering Brain (AST-100) — Software Delivery Discipline | [[33-COMPLIANCE/README|33-COMPLIANCE]] | **Compliance verification** | 🟡 | `—` | Compliance Officer | [[00-CONSTITUTION/control-planes/CP-019|CP-019]] |
| Knowledge Fabric — Unified Organizational Knowledge | [[08-KNOWLEDGE-GRAPH/README|08-KNOWLEDGE-GRAPH]] | **Neo4j entity creation** | ✅ | `Neo4j` | Knowledge Engineer | [[00-CONSTITUTION/control-planes/CP-008|CP-008]] |
| Knowledge Fabric — Unified Organizational Knowledge | [[08-KNOWLEDGE-GRAPH/README|08-KNOWLEDGE-GRAPH]] | **Relationship mapping** | ✅ | `Neo4j` | Knowledge Engineer | [[00-CONSTITUTION/control-planes/CP-008|CP-008]] |
| Knowledge Fabric — Unified Organizational Knowledge | [[09-KNOWLEDGE/README|09-KNOWLEDGE]] | **Knowledge source ingestion** | 🟡 | `Qdrant` | Knowledge Manager | [[00-CONSTITUTION/control-planes/CP-013|CP-013]] |
| Knowledge Fabric — Unified Organizational Knowledge | [[10-MEMORY/README|10-MEMORY]] | **Semantic memory (embeddings)** | ✅ | `Qdrant` | ML Engineer | [[00-CONSTITUTION/control-planes/CP-013|CP-013]] |
| Knowledge Fabric — Unified Organizational Knowledge | [[11-INDEXING/README|11-INDEXING]] | **Full-text indexing** | 🟡 | `—` | Data Engineer | [[00-CONSTITUTION/control-planes/CP-013|CP-013]] |
| Knowledge Fabric — Unified Organizational Knowledge | [[13-REPOSITORIES/README|13-REPOSITORIES]] | **Code graph generation** | ✅ | `Graft (TOL-000001)` | Tech Lead | [[00-CONSTITUTION/control-planes/CP-028|CP-028]] |
| Orchestration Fabric — Work Discovery & Agent Coordination | [[55-LOOP-ENGINEERING/README|55-LOOP-ENGINEERING]] | **Work discovery loop** | ✅ | `Loop Engine` | Agent Architect | [[00-CONSTITUTION/control-planes/CP-010|CP-010]] |
| Orchestration Fabric — Work Discovery & Agent Coordination | [[55-LOOP-ENGINEERING/README|55-LOOP-ENGINEERING]] | **Loop execution (L1/L2/L3)** | ✅ | `Loop Engine` | Agent Architect | [[00-CONSTITUTION/control-planes/CP-010|CP-010]] |
| Orchestration Fabric — Work Discovery & Agent Coordination | [[14-CAPABILITIES/README|14-CAPABILITIES]] | **Capability routing** | ✅ | `Loop Engine` | Capability Manager | [[00-CONSTITUTION/control-planes/CP-004|CP-004]] |
| Orchestration Fabric — Work Discovery & Agent Coordination | [[15-SKILLS/README|15-SKILLS]] | **Skill composition** | 🟡 | `Fractal (TOL-000002)` | Skill Engineer | [[00-CONSTITUTION/control-planes/CP-006|CP-006]] |
| Orchestration Fabric — Work Discovery & Agent Coordination | [[16-AGENTS/README|16-AGENTS]] | **Agent spawning** | ✅ | `Fractal (TOL-000002)` | Agent Architect | [[00-CONSTITUTION/control-planes/CP-006|CP-006]] |
| Orchestration Fabric — Work Discovery & Agent Coordination | [[19-ORCHESTRATION/README|19-ORCHESTRATION]] | **Workflow orchestration** | ✅ | `Loop Engine` | Orchestration Engineer | [[00-CONSTITUTION/control-planes/CP-009|CP-009]] |
| Execution Fabric — Persistent Agent Runtime | [[22-EXECUTION/README|22-EXECUTION]] | **Agent session management** | ✅ | `herdr (TOL-000003)` | Runtime Engineer | [[00-CONSTITUTION/control-planes/CP-009|CP-009]] |
| Execution Fabric — Persistent Agent Runtime | [[22-EXECUTION/README|22-EXECUTION]] | **Terminal pane management** | ✅ | `herdr (TOL-000003)` | Runtime Engineer | [[00-CONSTITUTION/control-planes/CP-009|CP-009]] |
| Execution Fabric — Persistent Agent Runtime | [[22-EXECUTION/README|22-EXECUTION]] | **Git worktree isolation** | ✅ | `herdr (TOL-000003)` | Runtime Engineer | [[00-CONSTITUTION/control-planes/CP-009|CP-009]] |
| Execution Fabric — Persistent Agent Runtime | [[22-EXECUTION/README|22-EXECUTION]] | **Cost tracking** | 🟡 | `Fractal (TOL-000002)` | Finance Engineer | [[00-CONSTITUTION/control-planes/CP-009|CP-009]] |
| Execution Fabric — Persistent Agent Runtime | [[49-SYSTEM/README|49-SYSTEM]] | **Process lifecycle** | ✅ | `herdr (TOL-000003)` | Infra Engineer | [[00-CONSTITUTION/control-planes/CP-027|CP-027]] |
| Execution Fabric — Persistent Agent Runtime | [[41-OBSERVABILITY/README|41-OBSERVABILITY]] | **Runtime state visibility** | 🟡 | `—` | Observability Engineer | [[00-CONSTITUTION/control-planes/CP-029|CP-029]] |
| Verification Fabric — Quality Gates & Confidence | [[31-LEGAL/README|31-LEGAL]] | **Legal compliance gates** | 🟡 | `—` | Legal Officer | [[00-CONSTITUTION/control-planes/CP-016|CP-016]] |
| Verification Fabric — Quality Gates & Confidence | [[32-SECURITY/README|32-SECURITY]] | **Security scanning (SAST)** | 🟡 | `—` | Security Officer | [[00-CONSTITUTION/control-planes/CP-017|CP-017]] |
| Verification Fabric — Quality Gates & Confidence | [[32-SECURITY/README|32-SECURITY]] | **Security scanning (DAST)** | 🟡 | `—` | Security Officer | [[00-CONSTITUTION/control-planes/CP-017|CP-017]] |
| Verification Fabric — Quality Gates & Confidence | [[33-COMPLIANCE/README|33-COMPLIANCE]] | **Compliance verification** | 🟡 | `—` | Compliance Officer | [[00-CONSTITUTION/control-planes/CP-019|CP-019]] |
| Verification Fabric — Quality Gates & Confidence | [[42-EVALUATION/README|42-EVALUATION]] | **Code review gates** | 🟡 | `—` | Code Review Lead | [[00-CONSTITUTION/control-planes/CP-032|CP-032]] |
| Verification Fabric — Quality Gates & Confidence | [[42-EVALUATION/README|42-EVALUATION]] | **Test coverage validation** | 🟡 | `—` | QA Lead | [[00-CONSTITUTION/control-planes/CP-032|CP-032]] |
| Operations Fabric — Deployment & Incident Response | [[41-OBSERVABILITY/README|41-OBSERVABILITY]] | **Log aggregation** | 🟡 | `—` | Observability Engineer | [[00-CONSTITUTION/control-planes/CP-029|CP-029]] |
| Operations Fabric — Deployment & Incident Response | [[41-OBSERVABILITY/README|41-OBSERVABILITY]] | **Distributed tracing** | 🟡 | `—` | Observability Engineer | [[00-CONSTITUTION/control-planes/CP-029|CP-029]] |
| Operations Fabric — Deployment & Incident Response | [[41-OBSERVABILITY/README|41-OBSERVABILITY]] | **Metrics collection** | 🟡 | `—` | Observability Engineer | [[00-CONSTITUTION/control-planes/CP-029|CP-029]] |
| Operations Fabric — Deployment & Incident Response | [[43-OUTCOMES/README|43-OUTCOMES]] | **Outcome tracking** | 🟡 | `Neo4j` | Outcome Analyst | [[00-CONSTITUTION/control-planes/CP-029|CP-029]] |
| Operations Fabric — Deployment & Incident Response | [[44-LEARNING/README|44-LEARNING]] | **Lesson extraction** | 🟡 | `Qdrant` | Learning Engineer | [[00-CONSTITUTION/control-planes/CP-032|CP-032]] |
| Operations Fabric — Deployment & Incident Response | [[45-EVOLUTION/README|45-EVOLUTION]] | **Continuous improvement** | 🟡 | `—` | Evolution Engineer | [[00-CONSTITUTION/control-planes/CP-032|CP-032]] |

---

## 4. The 7 Operational Planes Summary

1. **Plane 1: Company Brain** — Constitutional intelligence, identity, decisions, policies ([[00-CONSTITUTION/README|00-CONSTITUTION]], [[01-IDENTITY/README|01-IDENTITY]], [[20-DECISIONS/README|20-DECISIONS]], [[21-POLICY/README|21-POLICY]]).
2. **Plane 2: Engineering Brain** — Code intelligence, repositories, skills, CI/CD ([[13-REPOSITORIES/README|13-REPOSITORIES]], [[15-SKILLS/README|15-SKILLS]], [[56-ENGINEERING/README|56-ENGINEERING]], [[57-CODE-INTELLIGENCE/README|57-CODE-INTELLIGENCE]]).
3. **Plane 3: Knowledge Fabric** — Graph topology, memory, semantic indexing, ontologies ([[08-KNOWLEDGE-GRAPH/README|08-KNOWLEDGE-GRAPH]], [[09-KNOWLEDGE/README|09-KNOWLEDGE]], [[10-MEMORY/README|10-MEMORY]], [[11-INDEXING/README|11-INDEXING]]).
4. **Plane 4: Orchestration Fabric** — Work discovery, capabilities, agents, routing ([[14-CAPABILITIES/README|14-CAPABILITIES]], [[16-AGENTS/README|16-AGENTS]], [[19-ORCHESTRATION/README|19-ORCHESTRATION]], [[55-LOOP-ENGINEERING/README|55-LOOP-ENGINEERING]]).
5. **Plane 5: Execution Fabric** — Agent sessions, runtimes, terminal panes, isolation ([[22-EXECUTION/README|22-EXECUTION]], [[49-SYSTEM/README|49-SYSTEM]], [[41-OBSERVABILITY/README|41-OBSERVABILITY]]).
6. **Plane 6: Verification Fabric** — Security scanning, compliance verification, code review ([[31-LEGAL/README|31-LEGAL]], [[32-SECURITY/README|32-SECURITY]], [[33-COMPLIANCE/README|33-COMPLIANCE]], [[42-EVALUATION/README|42-EVALUATION]]).
7. **Plane 7: Operations & Evolution Fabric** — Telemetry, logging, continuous learning ([[40-METRICS/README|40-METRICS]], [[41-OBSERVABILITY/README|41-OBSERVABILITY]], [[43-OUTCOMES/README|43-OUTCOMES]], [[44-LEARNING/README|44-LEARNING]], [[45-EVOLUTION/README|45-EVOLUTION]]).

---
[[INDEX]] | [[00-CONSTITUTION/CONTROL_PLANES_MASTER|Control Planes Master]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]]
