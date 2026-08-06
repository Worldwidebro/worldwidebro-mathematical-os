---
version: 1.0
created: 2026-08-06
---

# Skills Required — Phase 1 & 2 Execution

**Discovery Framework:** Understanding → Leaderboard → CLI Search → Verify → Present → Install  
**Operating Model:** Single LLC (Winners Circle WC LLC) — complete jobs, build infrastructure parallel

---

## PHASE 1: Revenue Ops (Week 1-4, Aug 6-12)

### Skills/Capabilities Required

| Skill | Category | Status | Blocker |
|-------|----------|--------|---------|
| **B004 Vercel Env Vars** | Deployment | READY | None |
| **B001 Supabase Schema** | Database | READY | None |
| **B002 SMS Dispatch** | Comms | READY | B001 |
| **B003 Stripe Webhooks** | Payments | READY | None |
| **B005 Project Tracking** | Data | READY | B001 |
| **Call Script Gen** | Sales | READY | None |
| **Ad Campaign Setup** | Marketing | READY | B003 |
| **Revenue Dashboard** | Analytics | Agent-built | B003 |

### Execution Checklist

**Day 1 (Aug 6):**
- [ ] `/vercel-deployment` — Set env vars (B004)
- [ ] Finalize call scripts

**Day 2-3 (Aug 7-8):**
- [ ] `/supabase-database` — Property/tenant model (B001)
- [ ] `supabase db` — Project schema (B005)
- [ ] `/stripe-setup` — Payment webhooks (B003)

**Day 3-4 (Aug 8-9):**
- [ ] Deploy OPS-001 to Vercel
- [ ] Deploy EC-112 to Vercel
- [ ] Deploy CON-001 to Vercel
- [ ] Launch paid campaigns

**Day 5 (Aug 10):**
- [ ] Revenue dashboard live
- [ ] First income confirmed

**Success:** $50K weekly revenue + all 5 blockers resolved

---

## PHASE 2: VEX Foundation (Week 5-12, Aug 13-Sep 30)

### Layers 0-4: Infrastructure + Orchestration

**Gating:** Blocked until Phase 1 revenue >$50K

| Layer | Component | Status | Timeline | Blocker |
|-------|-----------|--------|----------|---------|
| **0** | Event Store + WAL | TBD | Week 5-6 | None |
| **1** | Identity + Permissions | PARTIAL | Week 6-7 | Layer 0 |
| **2** | Event Fabric + Webhooks | TBD | Week 7-8 | Layer 1 |
| **3** | Knowledge Graph | PARTIAL | Week 8-10 | Layer 2 |
| **4** | Workflow Engine | TBD | Week 10-12 | Layer 3 |

### Custom Build Components

```
vex-foundation/
├── Layer 0: postgres-event-store/
├── Layer 1: identity-service/
├── Layer 2: event-fabric/
├── Layer 3: knowledge-graph/
└── Layer 4: orchestration-engine/
```

### Phase 2 Skill Discovery Sequence

**Week 5-6 (Layer 0):**
- Understanding: Event sourcing patterns
- Search: `npx skills find "event-sourcing"`
- Verify: 1000 events/sec throughput
- Install: Custom postgres-event-store

**Week 6-7 (Layer 1):**
- Understanding: Multi-tenant identity + agent auth
- Search: `npx skills find "identity-provider"`
- Verify: JWT + scope enforcement
- Install: Supabase Auth + agent provisioning

**Week 7-8 (Layer 2):**
- Understanding: Event-driven + webhooks
- Search: `npx skills find "event-bus"`
- Verify: Event ordering + audit trail
- Install: Redis pub/sub + event API

**Week 8-10 (Layer 3):**
- Understanding: Property graphs + Cypher
- Search: `npx skills find "graph-database"`
- Verify: Query p95 <100ms for 1000+ nodes
- Install: Neo4j + entity/relationship schema

**Week 10-12 (Layer 4):**
- Understanding: DAG executors + state machines + AI planning
- Search: `npx skills find "workflow-engine"`
- Verify: 99% workflow success
- Install: Custom DAG + Claude planner + router

---

## Success Criteria

**Phase 1:**
- [ ] 3 ventures live on Vercel
- [ ] $50K weekly revenue
- [ ] All 5 blockers resolved
- [ ] Revenue dashboard operational

**Phase 2:**
- [ ] Event throughput: 1000 events/sec
- [ ] Graph nodes: 1000+ entities
- [ ] Query p95: <100ms
- [ ] Workflows: 99% success

---

**Next Review:** 2026-08-12 (Phase 1 midpoint)
