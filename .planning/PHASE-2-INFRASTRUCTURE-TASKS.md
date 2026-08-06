---
version: 1.0
created: 2026-08-06
phase: 2
status: Planning (blocked until Phase 1 >$50K)
tech_stack: Temporal, Apicurio, @cflow/core, steadykey, Prosody, human-in-the-loop, Clockwork, Agent Analytics
---

# Phase 2 Infrastructure Tasks — Layer 0-4 + Observability

**Gating:** Blocked until Phase 1 revenue >$50K (target: Aug 12)  
**Duration:** 8 weeks (Aug 13 - Oct 8)  
**Founder/CEO:** [[whoiam]]

---

## PHASE 2 TASK HIERARCHY

### TASK 1: Layer 0 Infrastructure (Week 5-6)
**Status:** Planned | **Owner:** You + Contractor | **Blocker:** None

#### Subtask 1.1: PostgreSQL Event Store
- [ ] Design event schema (Avro/Protobuf)
- [ ] Create append-only log table
- [ ] Configure WAL + snapshots
- [ ] Load test: 1000 events/sec
- **Effort:** 3 days

#### Subtask 1.2: Redis Pub/Sub
- [ ] Configure persistence (RDB + AOF)
- [ ] Set up Streams for fanout
- [ ] Test message ordering
- **Effort:** 2 days

#### Subtask 1.3: Schema Registry (Apicurio)
- [ ] Deploy Apicurio Registry
- [ ] Register all event types
- [ ] Set up compatibility rules
- [ ] Wire schema validation
- **Effort:** 3 days

#### Subtask 1.4: Verify Layer 0
- [ ] Throughput test
- [ ] Failover test
- [ ] Schema registry responding
- **Effort:** 1 day | **Blocker:** 1.1-1.3 complete

---

### TASK 2: Layer 1 Identity (Week 6-7)
**Status:** Planned | **Owner:** You | **Blocker:** None

#### Subtask 2.1: Human Identity
- [ ] Design identity schema
- [ ] Wire Supabase Auth
- [ ] Create roles + RLS policies
- [ ] Test JWT validation
- **Effort:** 3 days

#### Subtask 2.2: Agent Identity
- [ ] Design agent schema
- [ ] Create provisioning API
- [ ] Implement agent authentication
- [ ] Test key rotation
- **Effort:** 3 days

#### Subtask 2.3: Permissions Matrix
- [ ] Define resources + actions
- [ ] Create permissions table
- [ ] Implement permission checker
- [ ] Test scope enforcement
- **Effort:** 2 days

#### Subtask 2.4: Verify Layer 1
- [ ] Human registration + login
- [ ] Agent provisioning + auth
- [ ] RLS enforcement
- **Effort:** 1 day | **Blocker:** 2.1-2.3 complete

---

### TASK 3: Layer 2 Event Fabric (Week 7-8)
**Status:** Planned | **Owner:** You + Contractor | **Blocker:** Layer 0 + 1

#### Subtask 3.1: Idempotency (steadykey + Prosody)
- [ ] Install steadykey
- [ ] Design idempotency key strategy
- [ ] Create idempotency cache
- [ ] Wire into event publisher
- **Effort:** 2 days

#### Subtask 3.2: Event Publisher API
- [ ] Design event API
- [ ] Implement schema validation
- [ ] Implement idempotency checking
- [ ] Create event logging
- **Effort:** 3 days

#### Subtask 3.3: Event Subscription
- [ ] Create subscription registry
- [ ] Implement Redis Streams consumer
- [ ] Implement webhook delivery
- [ ] Test retry + dead-letter queue
- **Effort:** 3 days

#### Subtask 3.4: Audit Trail
- [ ] Design audit schema
- [ ] Create write-once table
- [ ] Implement tamper detection
- **Effort:** 2 days

#### Subtask 3.5: Verify Layer 2
- [ ] Event published → stored
- [ ] Idempotency works
- [ ] All subscribers receive events
- [ ] Audit trail immutable
- **Effort:** 1 day | **Blocker:** 3.1-3.4 complete

---

### TASK 4: Layer 3 Knowledge Graph (Week 8-10)
**Status:** Planned | **Owner:** You + Agent | **Blocker:** Layer 2

#### Subtask 4.1: Neo4j Schema Design
- [ ] Define node labels (16 types)
- [ ] Define relationships (10+ types)
- [ ] Create property constraints
- [ ] Design indexing strategy
- **Effort:** 2 days

#### Subtask 4.2: Entity Sync from Events
- [ ] Design event → node mapper
- [ ] Implement event listeners
- [ ] Create sync job (idempotent)
- [ ] Test: event → node
- **Effort:** 3 days

#### Subtask 4.3: Relationship Sync
- [ ] Create relationship mapper
- [ ] Implement cascade deletes
- [ ] Test consistency
- **Effort:** 2 days

#### Subtask 4.4: Graph Queries
- [ ] Implement blast radius query
- [ ] Implement critical path query
- [ ] Implement capability search
- [ ] Create GraphQL API
- [ ] Test performance (p95 <100ms)
- **Effort:** 3 days

#### Subtask 4.5: Full-Text Search
- [ ] Enable Neo4j Lucene
- [ ] Create search indexes
- [ ] Test search functionality
- **Effort:** 1 day

#### Subtask 4.6: Verify Layer 3
- [ ] Events sync to graph
- [ ] Query performance < 100ms
- [ ] Blast radius + critical path work
- **Effort:** 1 day | **Blocker:** 4.1-4.5 complete

---

### TASK 5: Layer 4 Orchestration (Week 10-12)
**Status:** Planned | **Owner:** You + Contractor | **Blocker:** Layer 3

#### Subtask 5.1: Temporal Setup
- [ ] Deploy Temporal
- [ ] Configure server
- [ ] Create worker pool
- [ ] Test simple workflow
- **Effort:** 2 days

#### Subtask 5.2: Workflow DSL (@cflow/core)
- [ ] Design workflow YAML format
- [ ] Create workflow parser
- [ ] Implement state handlers
- [ ] Test YAML → execution
- **Effort:** 3 days

#### Subtask 5.3: Agent Router (@reaatech/agent-handoff-routing)
- [ ] Design capability metadata
- [ ] Implement weighted scoring
- [ ] Create fallback logic
- [ ] Wire into workflow
- **Effort:** 2 days

#### Subtask 5.4: State Machine (FSM)
- [ ] Define formal FSM
- [ ] Implement state transitions
- [ ] Create state serialization
- [ ] Implement resume logic
- **Effort:** 2 days

#### Subtask 5.5: Human Approval (human-in-the-loop)
- [ ] Design approval schema
- [ ] Implement approval tasks
- [ ] Implement timeout + escalation
- [ ] Create approval UI
- **Effort:** 3 days

#### Subtask 5.6: Distributed Scheduler (Clockwork)
- [ ] Deploy scheduler
- [ ] Define schedule DSL
- [ ] Create job handlers
- [ ] Test scheduled execution
- **Effort:** 2 days

#### Subtask 5.7: Event → Workflow Triggering
- [ ] Create trigger registry
- [ ] Implement event listeners
- [ ] Wire Temporal client
- [ ] Test event → workflow
- **Effort:** 2 days

#### Subtask 5.8: Verify Layer 4
- [ ] End-to-end workflow execution
- [ ] State persistence
- [ ] Agent routing
- [ ] Human approvals + timeouts
- [ ] Scheduled jobs
- [ ] Event → workflow triggering
- **Effort:** 1 day | **Blocker:** 5.1-5.7 complete

---

### TASK 6: Observability + Intelligence (Week 10-12, parallel)
**Status:** Planned | **Owner:** You + Agent | **Blocker:** Layer 3 + 4 in progress

#### Subtask 6.1: Agent Analytics
- [ ] Deploy Agent Analytics
- [ ] Instrument agent executions
- [ ] Create KPI tracking
- [ ] Wire into Supabase
- **Effort:** 2 days

#### Subtask 6.2: Workflow Metrics
- [ ] Track execution time
- [ ] Track approval time
- [ ] Track error rates
- [ ] Create dashboards
- **Effort:** 2 days

#### Subtask 6.3: Revenue Feedback Loop
- [ ] Wire KPIs into Neo4j
- [ ] Create daily aggregates
- [ ] Implement replan trigger
- [ ] Create CEO dashboard
- **Effort:** 2 days

#### Subtask 6.4: Verify Observability
- [ ] Agent performance visible
- [ ] Workflow SLAs tracked
- [ ] Revenue KPIs live
- [ ] Dashboards render
- **Effort:** 1 day | **Blocker:** 6.1-6.3 complete

---

## PHASE 2 TIMELINE

```
Week 5-6 (Aug 13-27):  Layer 0 + Layer 1
Week 7-8 (Aug 27-Sep 3):  Layer 2 (+ Layer 1 wrap)
Week 8-10 (Sep 3-24):  Layer 3 (+ Layer 2 wrap)
Week 10-12 (Sep 24-Oct 15):  Layer 4 + Observability (parallel)

Oct 15: Phase 2 COMPLETE ✓
```

---

## SUCCESS CRITERIA (Phase 2 Complete)

- [ ] Event throughput: 1000 events/sec
- [ ] Graph nodes: 1000+ entities
- [ ] Query p95: <100ms
- [ ] Workflow success rate: 99%
- [ ] All layers tested + integrated
- [ ] KPI dashboard live
- [ ] Revenue feedback loop active

---

**Status:** Planned | **Blocked until:** Phase 1 revenue >$50K | **Target:** Oct 15, 2026
