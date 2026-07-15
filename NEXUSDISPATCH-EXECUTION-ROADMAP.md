# NexusDispatch AI — Execution Roadmap

**Status:** Phase 1 MVP Planning → Development (Q2 2027)  
**Scope:** Unified dispatch OS for 30 logistics ventures  
**Team:** 6 parallel workstreams (9 FTE)  
**Launch Target:** 50 beta fleets by June 2027

---

## Phase 1: MVP (Q2 2027) — 12 Weeks

### Workstream 1: Backend — AI Agent Orchestration (8 agents)
**Owner:** Backend Lead | **FTE:** 3 | **Status:** Planning

**8 Autonomous Agents:**
1. **Load Finder** — DAT + Truckstop aggregation + profit scoring
2. **Rate Negotiation** — Market rate benchmarking + counter-offer generation
3. **Broker Communications** — Email + SMS automation
4. **Driver Scheduling** — HOS-aware routing + optimization
5. **Compliance** — CSA scores + FMCSA monitoring + violations prevention
6. **Invoice** — BOL/POD OCR + invoice generation + factoring submission
7. **Maintenance** — Predictive maintenance via telematics
8. **Safety** — Risk routing + weather alerts + fatigue detection

**Tech Stack:**
- **Framework:** FastAPI (Python)
- **Reasoning:** Claude API (autonomous decision-making)
- **Short-term Memory:** Redis (conversations, session state)
- **Long-term Storage:** PostgreSQL (loads, carriers, history, transactions)
- **Knowledge Graph:** Neo4j (relationships, decision trees, context)

**Code Reuse:**
- LT-003-Logistics-Dispatch-Service (dispatch foundation)
- LT-001-Truck-Dispatch-Company (carrier data model)
- LT-014-AI-Route-Optimization (route algorithms)
- LT-028-Freight-AI-Optimization (rate prediction models)
- LT-013-Logistics-Automation-System (workflow templates)

**Milestones:**
- **Week 4:** Load Finder MVP (single board, basic scoring)
- **Week 8:** All 8 agents stubbed + framework complete
- **Week 12:** Production-ready with HITL guardrails (>5% rate variance = human approval)

---

### Workstream 2: Frontend — Dispatch Dashboard + Driver App
**Owner:** Product Lead | **FTE:** 2 | **Status:** Design phase

**Dispatch Dashboard (Web)**
- **Routes:** `/dispatch` (main), `/crm`, `/analytics`, `/settings`
- **Key Components:**
  - LoadCardGrid: Top 5 loads by profit-per-mile
  - AgentStatusPanel: Real-time status of 8 agents (errors, last action)
  - CallCenterView: Active calls + sentiment analysis
  - QuickActions: Accept, Negotiate, Escalate
  - PerLoadPnL: Profit tracker by load + lane
  - CarrierCRM: Broker history, performance metrics

**Driver App (Mobile)**
- **Routes:** `/load` (current), `/history`, `/support`
- **3 Main Buttons:**
  1. Accept Load (swipe card interface)
  2. Upload POD (photo capture)
  3. Call Dispatcher (direct)
- **Offline Sync:** SQLite queue → server on reconnect

**Tech:**
- Dashboard: React 19 + Next.js 15 + Tailwind CSS
- Mobile: React Native (iOS/Android shared codebase)
- Real-time: WebSocket (agent updates), Redis pub/sub

**Milestones:**
- **Week 2:** Figma wireframes approved
- **Week 6:** Dashboard MVP on staging
- **Week 10:** Mobile alpha (TestFlight + Google Play)
- **Week 12:** Both production-ready

---

### Workstream 3: Integrations — Load Boards, ELDs, Factoring
**Owner:** Integration Lead | **FTE:** 1 | **Status:** Pre-development

**Phase 1 (MVP — Weeks 1-6):**
- [ ] DAT FreightWaves (load aggregation + RateView pricing)
- [ ] Truckstop.com (load aggregation + dual-board dedup)
- [ ] Samsara ELD (HOS data + compliance monitoring)
- [ ] Motive ELD (fleet telematics + maintenance forecasting)

**Phase 2 (Production-ready — Weeks 7-10):**
- [ ] RTS Financial (factoring invoice submission)
- [ ] TriumphPay (factoring portal API)
- [ ] QuickBooks (accounting sync)
- [ ] Geotab (backup telematics source)

**Integration Architecture:**
```
Standard Layer:
  - APIClient: Auth + retry + rate limiting
  - DataMapper: Normalize to canonical schemas
  - WebhookHandler: Inbound events (load updates, compliance alerts)
  - SyncScheduler: Backfill every 4 hours + real-time pubsub
  
Error Handling:
  - Dead-letter queue (failed submissions)
  - Retry with exponential backoff (max 3 attempts)
  - Admin dashboard (manual resubmission)
```

**Milestones:**
- **Week 2:** DAT auth + load sync (stub scoring)
- **Week 4:** Truckstop dual aggregation + deduplication
- **Week 6:** Samsara + Motive HOS feeds live
- **Week 8:** Factoring layer architecture + RTS pre-prod
- **Week 10:** All 8 integrations pre-production

---

### Workstream 4: DevOps — Infrastructure, Monitoring, Deployment
**Owner:** Infrastructure Lead | **FTE:** 1 | **Status:** Design phase

**Infrastructure:**
```
Compute:
  - API Tier: FastAPI on ECS (auto-scaling, 99.9% SLA)
  - Agent Tier: Separate ECS cluster (GPU for embeddings)
  - Dashboard: Next.js on Vercel (CDN edge caching)

Data:
  - PostgreSQL: RDS Multi-AZ (automated backups, read replicas)
  - Redis: ElastiCache cluster (replication, Sentinel)
  - Neo4j: EC2 single-node → multi-node (Phase 2)

Monitoring:
  - CloudWatch logs (all services)
  - Prometheus metrics (custom agent dashboards)
  - Grafana (operations team view)
  - PagerDuty (on-call escalation)
```

**Security & Compliance:**
- [ ] SOC 2 Type II readiness (access logs, encryption at rest/transit)
- [ ] FMCSA data compliance (data residency US, retention policy)
- [ ] CCPA compliance (data export, deletion, portability)
- [ ] End-to-end encryption (AES-256 for driver data)
- [ ] Rate limiting + DDoS protection (CloudFront WAF)

**CI/CD Pipeline:**
```
On PR: Unit tests, linting, type-check, SAST scan
On Merge: Integration tests, Docker build
On Release tag: Deploy staging → smoke tests → manual approval → prod
Rollback: Automated if error rate >1% for 5 min
```

**Milestones:**
- **Week 2:** Base AWS (VPC, RDS, Redis, networking)
- **Week 4:** CI/CD live (GitHub Actions → Vercel)
- **Week 6:** Monitoring + alerting operational
- **Week 8:** Load testing (1000 concurrent WebSocket)
- **Week 12:** Production SLA validation (99.9% uptime)

---

### Workstream 5: Product — Beta Program + Onboarding
**Owner:** PM | **FTE:** 0.5 | **Status:** Recruitment starting

**Beta Fleet Selection (50 target):**
- 20 owner-operators (1-2 trucks, high engagement)
- 20 small carriers (5-50 trucks, regional)
- 10 freight brokers (integration feedback)
- Geographic mix: South (Charlotte anchor), Midwest, West Coast

**Onboarding Sequence:**
```
Week 1: Welcome + API key generation
Week 2: Load board auth (DAT + Truckstop)
Week 3: ELD connection (Samsara/Motive setup)
Week 4: First 3 loads automated (walk-through)
Week 5+: Weekly performance reports + bi-weekly group calls
```

**Support Structure:**
- 24/7 Slack channel (beta cohort only)
- Weekly 30-min group calls (Monday 10 AM PT)
- Google Form for feature requests (weekly synthesis)
- NPS survey (weeks 4, 8, 12)

**Success Metrics (End Q2 2027):**
- ✅ 40+ active users (of 50 invited)
- ✅ 15% average RPM improvement (validated via data export)
- ✅ <15 min time-to-book (vs 45 min manual)
- ✅ 90% retention rate
- ✅ 20+ validated feature requests
- ✅ 0 FMCSA violations in cohort

---

### Workstream 6: QA — Testing & Reliability
**Owner:** QA Lead | **FTE:** 1 | **Status:** Test framework building

**Test Layers:**
- **Unit:** 80%+ code coverage (agents, API routes)
- **Integration:** Agent→integration flows (load board → scoring → CRM)
- **E2E:** Dashboard workflows (accept load → driver notified → invoice generated)
- **Load Testing:** 1000 concurrent WebSocket connections

**Quality Gates:**
- All agents pass HITL test suite (100 test loads per agent)
- No integration data loss (delivery guarantee testing)
- Dashboard <1s response time (p95)
- Mobile app <500ms cold start

---

## Repo Structure

```
nexusdispatch/
├── backend/
│   ├── agents/
│   │   ├── load_finder.py
│   │   ├── rate_negotiation.py
│   │   ├── broker_comms.py
│   │   ├── driver_scheduler.py
│   │   ├── compliance.py
│   │   ├── invoice.py
│   │   ├── maintenance.py
│   │   └── safety.py
│   ├── integrations/
│   │   ├── dat_freightwaves.py
│   │   ├── truckstop.py
│   │   ├── samsara_eld.py
│   │   ├── motive_eld.py
│   │   └── factoring/
│   ├── models.py (Pydantic schemas)
│   ├── api.py (FastAPI routes)
│   ├── memory.py (Redis + Neo4j)
│   ├── requirements.txt
│   └── tests/
├── frontend/
│   ├── dashboard/ (Next.js)
│   ├── mobile/ (React Native)
│   └── package.json
├── devops/
│   ├── terraform/ (AWS infra)
│   ├── docker/ (Dockerfiles)
│   ├── github-workflows/ (CI/CD)
│   └── monitoring/ (Prometheus/Grafana)
├── docs/
│   ├── API.md
│   ├── AGENT-SPEC.md
│   ├── DEPLOYMENT.md
│   └── ONBOARDING.md
└── tests/
    ├── unit/
    ├── integration/
    └── e2e/
```

---

## Team Structure (9 FTE)

| Role | Workstream | FTE | Skills |
|------|-----------|-----|--------|
| Backend Lead | Agents + orchestration | 1 | FastAPI, LLMs, Python |
| Agent Engineer (2×) | Individual agents | 2 | Claude API, domain knowledge |
| Frontend Lead | Dashboard + mobile | 1 | React, TypeScript, real-time |
| Mobile Engineer | Driver App | 1 | React Native, UX |
| Integration Engineer | APIs + connectors | 1 | REST/GraphQL, error handling |
| DevOps/SRE | Infrastructure | 1 | AWS, Terraform, monitoring |
| PM/Product | Beta + metrics | 0.5 | GTM, user research |
| QA | Testing + reliability | 1 | Test automation, load testing |

---

## Critical Dependencies

**Blocking Load Finder (Week 2):**
1. DAT FreightWaves enterprise API access
2. Truckstop API credentials + rate limits
3. Basic scoring logic (profit-per-mile formula)

**Blocking Dashboard (Week 6):**
1. Load Finder API stable
2. Agent framework (stubs OK)
3. WebSocket authentication

**Blocking Mobile (Week 10):**
1. Driver sync protocol
2. Photo upload infrastructure
3. Notification system

---

## Known Risks + Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **Load Board API Restrictions** — DAT/Truckstop may limit scraping or charge premium fees | Blocks MVP | Secure enterprise partnerships Week 1; build OCR fallback by Week 6 |
| **AI Hallucination** — Agent agrees to unprofitable rates | Revenue loss | HITL approval gate (>5% variance); strict guardrails + test suite |
| **Driver Adoption Friction** — Drivers resist new app | Low adoption | Keep UI to 3 buttons; $50 adoption incentive; compare to manual workflow |
| **ELD API Downtime** — Samsara/Motive outage blocks compliance checks | Compliance risk | Dual ELD integration (Motive backup); local cache of HOS data |
| **Scale: 1000 WebSocket connections** — Dashboard melts under load | Ops incident | Load test Week 8; implement connection pooling + backpressure |

---

## Launch Checklist (Week 12)

**Engineering:**
- [ ] All 8 agents pass 100-load test suite
- [ ] Dashboard + Driver App in production
- [ ] All integrations functional (load boards, ELDs, factoring prep)
- [ ] 99.9% uptime for 48 hours

**Product:**
- [ ] 50 beta fleets recruited + contracts signed
- [ ] Onboarding flow tested end-to-end
- [ ] Support Slack + weekly call calendar scheduled
- [ ] NPS baseline (target: 40+)

**Security:**
- [ ] SOC 2 audit started (attestation in Q3)
- [ ] FMCSA data compliance verified
- [ ] Pentest completed (no critical findings)
- [ ] Encryption enabled (at rest + in transit)

---

## Success Metrics by Phase

**Phase 1 (Q2 2027):**
- 40+ active fleets
- 15% avg RPM improvement
- <15 min time-to-book
- 90% retention
- 99.9% uptime
- 0 FMCSA violations

**Phase 2 (Q4 2027):**
- 200 fleets
- $50K MRR
- Full automation layer
- Broker integration live

**Phase 3 (Q2 2028):**
- 500 fleets
- $150K MRR
- Financial OS complete
- 30 logistics ventures unified

**Phase 4 (Q4 2028):**
- 1000+ fleets
- $300K+ MRR
- Ecosystem play
- Open API + partnerships

---

## Next Steps (Week 1)

**This Week:**
- [ ] Secure DAT/Truckstop enterprise partnerships (PM)
- [ ] Backend team kickoff: agent architecture (Backend Lead)
- [ ] Frontend wireframes: Figma (Product Lead)
- [ ] DevOps: AWS account + CI/CD setup (Infrastructure Lead)
- [ ] Beta recruitment emails sent (PM)

**Ongoing Cadence:**
- Weekly sync: 30 min (workstream leads)
- Daily standup: 15 min (engineering teams)
- Bi-weekly demos: Progress reviews

---

**Created:** 2026-07-16  
**Owner:** Engineering Lead + PM  
**Last Updated:** 2026-07-16  
**Review Frequency:** Weekly
