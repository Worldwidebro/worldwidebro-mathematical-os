---
version: 1.0
created: 2026-08-06
status: reference (blocked until Phase 1 revenue >$50K)
phase: 2
duration_weeks: 8
timeline: Week 5-12 (Aug 13-30)
founder: whoiam
---

# Phase 2: VEX Foundation — Event/Graph Substrate (Layers 0-4)

**Gating Condition:** Phase 1 achieves $50K weekly revenue (all 3 ventures live)  
**Objective:** Build unified event/knowledge infrastructure for VEX OS surfaces (Room, CRM, CC, Work, Dev)  
**Outcome:** Canonical event log + knowledge graph queryable by all 5 surfaces  
**Operating Model:** Single LLC (Winners Circle WC LLC), hybrid human/agent execution

---

## Layer 0: Infrastructure (Week 5-6)

**Goal:** Centralized data layer for event store + knowledge graph

| Component | Tech | Status | Owner |
|-----------|------|--------|-------|
| Event Store DB | PostgreSQL WAL | TBD | Phase 1 |
| Knowledge Graph | Neo4j (local) | Live | Phase 1 |
| Vector DB | Qdrant (local) | Live | Phase 1 |
| Message Queue | Redis | Live | Phase 1 |
| Object Storage | S3-compatible | TBD | Phase 1 |
| Search | Elasticsearch | TBD | Phase 1 |

**Tasks:**
- [ ] Define event schema (Avro/Protobuf)
- [ ] Set up event store (append-only log)
- [ ] Configure WAL archival + snapshots
- [ ] Wire Redis pub/sub for fan-out
- [ ] Test 1000 events/sec throughput

**Timeline:** 2 weeks (Aug 13-20)  
**Blocker:** Phase 1 infrastructure must be stable

---

## Layer 1: Identity (Week 6-7)

**Goal:** Unified human + agent identity model

| Entity | Fields | Behavior |
|--------|--------|----------|
| Human | id, email, name, org, role, permissions | Manual creation, OAuth integration |
| Agent | id, name, type, org, role, capabilities, auth_key | Provisioned by system, MCP auth |
| Organization | id, name, slug, tier, settings | One: Winners Circle WC LLC (initial) |
| Role | id, name, permissions, scope | CEO, Agent, Executor, Viewer, Admin |
| Permission | resource, action, scope | Fine-grained: graph.read, task.write, etc. |

**Tasks:**
- [ ] Define identity schema
- [ ] Implement human registration (email-based)
- [ ] Implement agent provisioning (API key + MCP)
- [ ] Wire OAuth/Supabase Auth
- [ ] Create roles + permissions matrix
- [ ] Test identity verification (JWT + scope)

**Timeline:** 2 weeks (Aug 20-27)  
**Blocker:** Phase 1 staffing model must be stable

---

## Layer 2: Event Fabric (Week 7-8)

**Goal:** Immutable audit log + event-driven triggering

| Event Type | Schema | Subscribers |
|------------|--------|-------------|
| CALL.RECEIVED | caller, duration, transcript | CRM, Graph, Room, CC |
| TASK.CREATED | creator, venture, title, owner | Work, Graph, Room, Dev |
| ISSUE.OPENED | repo, title, assignee, labels | Dev, Work, Graph, Room |
| MESSAGE.SENT | channel, author, content, mentions | Room, Graph, Audit |
| PAYMENT.RECEIVED | venture, amount, customer, invoice_id | CRM, Work, Finance, Graph |
| DECISION.MADE | venture, outcome, approver, stakeholders | Graph, Room, Audit |
| WORKFLOW.TRIGGERED | trigger, workflow_id, inputs, outputs | Orchestration, Graph |

**Tasks:**
- [ ] Define canonical event schema
- [ ] Implement event store (append-only log)
- [ ] Build event publisher API
- [ ] Create event subscription system
- [ ] Wire webhook fan-out (Kafka-style)
- [ ] Implement audit trail (immutable)
- [ ] Test causality + event ordering

**Timeline:** 2 weeks (Aug 27-Sep 3)  
**Blocker:** Layer 1 identity must be stable

---

## Layer 3: Knowledge Graph (Week 8-10)

**Goal:** Queryable relationship model for all business entities

**Entities (Neo4j nodes):**

```
COMPANY
  ├── VENTURE (8 initial)
  ├── DEPARTMENT (36 domains)
  ├── PERSON (You + hired staff)
  ├── AGENT (Router, Specialists)
  ├── CUSTOMER (from CRM)
  ├── PRODUCT (venture outputs)
  ├── ORDER (revenue tracking)
  ├── CALL (from CC)
  ├── DECISION (governance)
  ├── WORKFLOW (automation)
  ├── TASK (ClickUp → graph)
  ├── ISSUE (GitHub → graph)
  ├── GOAL (strategy → graph)
  ├── KPI (measurement)
  └── EVENT (immutable log)
```

**Relationships:**

```
PERSON works_for COMPANY
PERSON manages DEPARTMENT
PERSON owns VENTURE
PERSON executes TASK
PERSON approves DECISION

AGENT belongs_to COMPANY
AGENT executes TASK
AGENT calls WORKFLOW

VENTURE has CUSTOMER
VENTURE produces PRODUCT
VENTURE generates KPI

TASK depends_on TASK
TASK blocks VENTURE_GOAL

CALL involves CUSTOMER
CALL creates TASK
CALL triggers DECISION

DECISION enables VENTURE
DECISION blocks VENTURE

WORKFLOW triggers TASK
WORKFLOW produces EVENT
```

**Tasks:**
- [ ] Define node + relationship schema
- [ ] Migrate Phase 1 entities to graph
- [ ] Wire event → graph listeners
- [ ] Implement query patterns (blast radius, critical path)
- [ ] Build Neo4j full-text search
- [ ] Create graph visualization
- [ ] Test query performance (1000+ nodes)

**Timeline:** 3 weeks  
**Blocker:** Layer 2 events must be flowing

---

## Layer 4: Orchestration (Week 10-12)

**Goal:** State machines + workflow engine for Phase 1 automation

| Primitive | Purpose | Example |
|-----------|---------|---------|
| Workflow | Sequence of steps | "Qualify Lead → Schedule Call → Create Task" |
| State Machine | Conditional routing | "Task: Pending→In Progress→Blocked→Done" |
| Trigger | Event-driven execution | "CALL.RECEIVED → Run Routing Workflow" |
| Planner | AI task decomposition | "Goal: $50K revenue → Parallel task graph" |
| Router | Agent dispatch | "Task type→Agent capability→Assignment" |

**Tasks:**
- [ ] Design workflow engine (DAG-based)
- [ ] Implement state machines (FSM + guards)
- [ ] Wire event triggers → workflows
- [ ] Build AI planner (Claude + task decomposition)
- [ ] Create agent router (capability matching)
- [ ] Implement workflow history + replay
- [ ] Test end-to-end: Goal → Tasks → Agents → Completion

**Timeline:** 3 weeks  
**Blocker:** Layer 3 graph must be queryable

---

## Phase 2 Success Criteria

| Metric | Target | Verification |
|--------|--------|--------------|
| Event throughput | 1000 events/sec | Load test |
| Graph nodes | 1000+ entities | Query count |
| Query latency (p95) | <100ms | Benchmark |
| Event ordering | 100% causal | Audit test |
| Workflow execution | 99% success | E2E tests |
| Layer coverage | All 4 complete | Checklist |

---

**Status:** Reference. Execution blocked until Phase 1 revenue >$50K.
