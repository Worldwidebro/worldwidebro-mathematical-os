# VEX OPCO Engine — Roadmap to Completion

**Project:** Build live operations dashboard for Worldwidebro Holdings  
**Status:** MVP Dashboard Live + 3 Missing Components (Agency Agents, MCP Registry, Skills)  
**Goal:** Full real-time integration with Neo4j, Supabase, MCP Registry, Kafka  
**Timeline:** 4 weeks to production (2026-07-21 → 2026-08-18)

---

## EXECUTIVE SUMMARY

| Phase | Timeline | Deliverable | Status |
|-------|----------|-------------|--------|
| **0: MVP** | 2026-07-21 ✅ | Dashboard + 3 components | COMPLETE |
| **1: Connectors** | 2026-07-22 to 07-24 | Neo4j, Supabase, MCP, Kafka | NEXT (2-3 days) |
| **2: UI Components** | 2026-07-25 to 07-28 | 14 remaining routes | 3-4 days |
| **3: Real-Time Sync** | 2026-07-29 to 07-31 | Zustand, caching, subscriptions | 2-3 days |
| **4: Testing** | 2026-08-01 to 08-05 | Unit, integration, E2E, perf | 3-5 days |
| **5: Launch** | 2026-08-06 to 08-10 | Polish, docs, team training | 2-3 days |

**Total Effort:** ~4 weeks · 124 hours · 1 developer (or 2 weeks with 2 devs)

---

## PHASE 1: Data Connectors (YOUR IMMEDIATE NEXT STEP)

**Timeline:** 2026-07-22 → 2026-07-24 (2-3 days)  
**Effort:** 24 hours  
**Blockers:** None (all systems are live)  
**Success:** Dashboard data updates in real-time from all 4 backends

### Task 1.1: Neo4j Connector (8 hours)
**Purpose:** Fetch agents, org hierarchy, skill executions from graph database  
**Endpoint:** `bolt://localhost:7687` (neo4j/ventures2026)  
**Queries:**
```cypher
# Agents: name, role, status, CPU, memory, confidence
MATCH (a:Agent) RETURN a

# Org Hierarchy: CEO → Finance/Dev/Ops → Qwen specialists
MATCH (a1:Agent)-[:SUPERVISES]->(a2:Agent) RETURN a1, a2

# Skill Execution: progress, tokens, ETA
MATCH (s:SkillExecution)-[:EXECUTED_BY]->(a:Agent) RETURN s, a

# Pending Approvals: decision type, confidence scores
MATCH (p:Project {status: 'PENDING_APPROVAL'}) RETURN p
```
**Output:** `src/hooks/useNeo4j.ts` (React hook)  
**Integration:** Connect to Dashboard + Agents + Decisions tabs

### Task 1.2: Supabase Connector (6 hours)
**Purpose:** Fetch tasks, audit logs, decisions from transactional database  
**Endpoint:** `cyhzilqldouzgynacqpe.supabase.co`  
**Queries:**
```sql
-- Running tasks (status != 'completed')
SELECT * FROM aoc_tasks WHERE status != 'completed'

-- Audit log (last 100 entries)
SELECT * FROM audit_logs ORDER BY timestamp DESC LIMIT 100

-- Agent activity (past 7 days)
SELECT * FROM agent_activity WHERE created_at > now() - interval '7 days'

-- Venture decisions (reasoning traces)
SELECT * FROM venture_decisions ORDER BY created_at DESC
```
**Output:** `src/hooks/useSupabase.ts` (React hook with real-time subscriptions)  
**Integration:** Connect to Tasks + Audit + Decisions tabs

### Task 1.3: MCP Registry Loader (2 hours)
**Purpose:** Load 25 installed MCPs with live health status  
**Source:** `/Documents/MCP_REGISTRY.json`  
**Load:** On component mount  
**Extract Fields:** name, status, category, capabilities[], used_by[], last_verified  
**Output:** `src/loaders/loadMCPRegistry.ts`  
**Integration:** Connect to MCP Registry tab

### Task 1.4: Kafka WebSocket Consumer (8 hours)
**Purpose:** Stream real-time events (agent heartbeats, task updates, skill progress)  
**Endpoint:** `ws://localhost:3000/ws` (or SSE fallback)  
**Events:**
- `agent.heartbeat` (5s) → Update agent status
- `task.status_change` → Update kanban board
- `skill.execution_update` → Update progress bars
- `audit.action` → Append to log
- `mcp.health_check` → Update MCP indicators

**Output:** `src/hooks/useEventStream.ts`  
**Integration:** Real-time updates across all tabs

---

## PHASE 2: Complete UI Components (3-4 Days)

**Build these 14 routes in priority order:**

| Route | Component | Data Source | Est. Time |
|-------|-----------|-------------|-----------|
| `/tasks` | Kanban board | Supabase | 6h |
| `/decisions` | Timeline + traces | Neo4j + Qdrant | 5h |
| `/approvals` | Approval modals | Neo4j | 4h |
| `/organization` | D3 hierarchy graph | Neo4j | 8h |
| `/analytics` | Cost/token charts | Langfuse + Prometheus | 5h |
| `/audit` | Filterable log | Supabase | 3h |
| `/workflows` | Pipeline UI | n8n + Neo4j | 6h |
| `/memory` | Search notes | Neo4j + Qdrant | 5h |
| `/comms` | Message stream | Kafka | 4h |
| `/opcos` | OPCO grid | Neo4j | 3h |
| `/opcos/:id` | OPCO detail | Neo4j + Supabase | 3h |
| `/teams` | Team grid | Neo4j | 3h |
| `/teams/:id` | Team detail | Neo4j | 3h |
| `/bottlenecks` | Constraint ranking | Neo4j scoring | 4h |

**Total:** 40 hours (5 days for 1 dev, 2-3 days for 2 devs)

---

## PHASE 3: Real-Time Sync & Performance (2-3 Days)

**Tasks:**
- [ ] Zustand store (agents, tasks, decisions, MCPs) — 4h
- [ ] WebSocket reconnection logic — 2h
- [ ] Optimistic updates — 3h
- [ ] Change detection (only re-render on actual changes) — 2h
- [ ] Caching strategy (1h TTL Neo4j, 5m TTL Supabase) — 3h
- [ ] Offline mode (graceful degradation) — 2h
- [ ] Error boundaries — 2h

**Performance targets:**
- Dashboard load: <1s
- Route transitions: <200ms
- WebSocket latency: <100ms
- Agent status propagation: <2s

**Total:** 20 hours (2-3 days)

---

## PHASE 4: Testing & Deployment (3-5 Days)

**Tests:**
- [ ] Unit tests for all 4 connectors — 6h
- [ ] Integration tests (mocked backends) — 6h
- [ ] E2E tests (against staging) — 8h
- [ ] Performance audit (Lighthouse, Core Web Vitals) — 2h
- [ ] Accessibility audit (WCAG 2.1 AA) — 2h

**Deployment:**
- [ ] Build optimization (code splitting, lazy loading) — 3h
- [ ] Docker containerization — 2h
- [ ] Environment config (dev/staging/prod) — 2h
- [ ] CI/CD pipeline wiring — 3h
- [ ] Monitoring (Sentry, Datadog) — 2h

**Total:** 24-32 hours (3-4 days)

---

## PHASE 5: Polish & Launch (2-3 Days)

**Final features:**
- [ ] Command palette (⌘K search) — 2h
- [ ] Keyboard shortcuts (g+d, g+a, etc) — 1h
- [ ] Dark/light theme toggle — 1h
- [ ] User preferences (sidebar, refresh rate) — 1h
- [ ] Export (CSV/JSON/SVG) — 2h
- [ ] Notifications (toast + center) — 1h

**Documentation:**
- [ ] API docs for connectors — 2h
- [ ] Runbooks + troubleshooting — 2h
- [ ] Team onboarding guide — 1h

**Launch:**
- [ ] Slack announcement
- [ ] Team training
- [ ] Feedback collection
- [ ] Initial monitoring

**Total:** 16 hours (2 days)

---

## DEPENDENCY GRAPH

```
Phase 0 (MVP) ✅
    ↓
Phase 1 (Connectors) — CRITICAL PATH
    ├─ Neo4j (agents, org, skills)
    ├─ Supabase (tasks, audit, decisions)
    ├─ MCP registry (MCPs)
    └─ Kafka (real-time events)
    ↓
Phase 2 (UI Components) — depends on connectors
    ├─ /tasks (uses Supabase)
    ├─ /decisions (uses Neo4j + Qdrant)
    ├─ /organization (uses Neo4j D3)
    └─ ... (14 routes total)
    ↓
Phase 3 (Real-Time Sync) — optimizes all phases
    ├─ Zustand state (all tabs)
    ├─ Caching (Neo4j 1h, Supabase 5m)
    └─ Subscriptions (Kafka events)
    ↓
Phase 4 (Testing) — verifies phases 1-3
    ├─ Unit (connectors)
    ├─ Integration (tabs)
    └─ E2E (full flows)
    ↓
Phase 5 (Launch) — polish + deploy
```

---

## RISK & MITIGATION

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Neo4j schema changes | Low | High | Pin schema version + add migration guards |
| Kafka connection loss | Medium | Medium | Auto-reconnect with exponential backoff + queue events |
| Supabase rate limits | Low | Medium | Implement request throttling + caching |
| Large dataset perf | Medium | High | Pagination + virtualization for 1,000+ rows |
| WebSocket memory leak | Low | High | Proper cleanup in useEffect + connection pooling |
| Security (exposed credentials) | Low | Critical | Use env vars + no secrets in code + rotate keys |

---

## RESOURCE ALLOCATION

**Recommended:** 2 developers (parallel work)

**Dev 1 (Backend integration):**
- Phase 1: All 4 connectors
- Phase 2: /tasks, /decisions, /workflows
- Phase 3: Zustand + subscriptions
- Phase 4: Integration tests

**Dev 2 (Frontend UI):**
- Phase 2: /organization, /analytics, /audit, /comms, /memory
- Phase 3: Caching + error boundaries
- Phase 4: Unit tests + E2E
- Phase 5: Polish + launch

**Both:** Pairing on critical paths (Phase 3 real-time sync)

---

## SUCCESS CRITERIA (Go/No-Go Gates)

**Phase 1:** All 4 connectors working + data flowing to dashboard  
**Phase 2:** 14 routes built + navigable + connected  
**Phase 3:** Real-time updates <2s propagation + no data loss on reconnect  
**Phase 4:** 100% connector test coverage + E2E passing + perf targets met  
**Phase 5:** Team trained + zero bugs in first week + ready for scale  

---

## ESTIMATED TIMELINE

```
Week 1 (Jul 22-28):  Phase 1 + Phase 2 (parallel)
Week 2 (Jul 29-Aug 4): Phase 3 + Phase 4 (parallel)
Week 3 (Aug 5-11):    Phase 5 + launch
Week 4 (Aug 12-18):   Stabilization + Phase 2 features (if time)
```

**Go-live target:** 2026-08-10  
**Stabilization window:** 2026-08-11 to 2026-08-18

---

**Ready to start? Build Phase 1 connectors now?**
