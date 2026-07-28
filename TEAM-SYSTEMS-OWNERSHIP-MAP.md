# Team → Systems → Repos Ownership Map

**Scope:** 30-day OS-001 sprint + beyond  
**Date:** 2026-07-27  
**People:** 7 (you + 6 engineers) + 5 agents

---

## THE TEAM & WHAT THEY OWN

```
YOU (Founder/CEO)
├─ Role: Strategy, approval, coordination
├─ Hours: 15-20/week
├─ Owns: Decision-making, advisor calls, roadmap prioritization
└─ Reviews: All major changes before prod deploy
   
BACKEND ENGINEER A
├─ Role: Core Python services
├─ Hours: 40/week
├─ Owns: 
│  ├─ automation-agent.py (5 workflows)
│  ├─ sync-service.py (hourly pipeline)
│  └─ shared/libs/email (SendGrid wrapper)
├─ Repo: worldwidebro-holding (monorepo)
└─ PR pattern: feature/... → main → auto-deploy

BACKEND ENGINEER B
├─ Role: API & webhook services
├─ Hours: 40/week
├─ Owns:
│  ├─ webhook-receiver.py (FastAPI, real-time)
│  ├─ dashboard-api.py (4 REST endpoints)
│  └─ shared/libs/webhooks (verification logic)
├─ Repo: worldwidebro-holding (monorepo)
└─ PR pattern: feature/... → main → auto-deploy

DEVOPS ENGINEER
├─ Role: Infrastructure, CI/CD, monitoring, scaling
├─ Hours: 30/week
├─ Owns:
│  ├─ docker-compose.yml (local dev + staging)
│  ├─ .github/workflows/ (GitHub Actions CI/CD)
│  ├─ Nx configuration (build caching, remote caching)
│  ├─ Monitoring stack (Prometheus, Grafana, Langfuse)
│  ├─ Database backups & replication
│  └─ Production deployment & scaling
├─ Repos: worldwidebro-holding (CI/CD)
└─ Duty: Unblock team, keep prod green, manage secrets

DATA ENGINEER
├─ Role: Data layer, schemas, migrations, optimization
├─ Hours: 25/week
├─ Owns:
│  ├─ Supabase schema (tables, migrations, RLS)
│  ├─ Neo4j schema (nodes, edges, indexes)
│  ├─ Qdrant collections (vectors, embeddings)
│  ├─ Query optimization & indexing
│  └─ shared/libs/{supabase,neo4j,qdrant}-client
├─ Repos: worldwidebro-holding (shared/libs/)
└─ Duty: Data consistency, query performance, prod health

AI ENGINEER
├─ Role: Agent framework, reasoning, skills, memory
├─ Hours: 35/week
├─ Owns:
│  ├─ claude-agent.py (LangGraph reasoning loop)
│  ├─ Agent framework (lifecycle, state, coordination)
│  ├─ Skill registry (10 initial skills, extensible)
│  ├─ Memory layer (persistent context across calls)
│  ├─ Evaluation framework (score agent decisions)
│  ├─ shared/libs/anthropic-client (Claude wrapper)
│  ├─ shared/libs/types (Wealth, Person, Opportunity models)
│  └─ Prompt optimization (based on feedback)
├─ Repo: worldwidebro-holding (services/claude-agent/, shared/libs/)
└─ Duty: Agent reasoning quality, skill development

QA ENGINEER
├─ Role: Testing, integration validation, smoke tests
├─ Hours: 25/week
├─ Owns:
│  ├─ Unit tests (per service)
│  ├─ Integration tests (across services + databases)
│  ├─ Staging validation (before prod deploys)
│  ├─ Production smoke tests (hourly health checks)
│  ├─ Test automation (GitHub Actions)
│  └─ Bug triage & regression testing
├─ Repo: worldwidebro-holding (tests/ directory)
└─ Duty: Sign-off on prod deploys, catch regressions

SECURITY ENGINEER (Weeks 3-4 focus)
├─ Role: Auth, RBAC, audit logging, compliance, pen testing
├─ Hours: 20/week
├─ Owns:
│  ├─ API authentication (OAuth2/JWT)
│  ├─ RBAC (role-based access control)
│  ├─ Audit logging (all actions recorded)
│  ├─ Secrets management (encrypted .env, vault)
│  ├─ Rate limiting & DDoS protection
│  └─ Penetration testing (Weeks 3-4)
├─ Repo: worldwidebro-holding (security/, .github/secrets)
└─ Duty: Production security & compliance sign-off
```

---

## REPOS OWNED BY TEAM

| Repo | Owner | Purpose | Activity |
|------|-------|---------|----------|
| **worldwidebro-holding** | Backend A+B, DevOps, Data, AI | Monorepo (5 services + shared libs) | Daily commits |
| **wealth-optimization-platform** | You + Backend team | Phase 1 public deliverable | Weekly imports from monorepo |
| **vex-hero-site** | Frontend (outsourced) | Portfolio UI + venture directory | Calls dashboard-api |
| **venture-factory** | Backend + Builder Agent | Phase 2 (planned) | Month 2-3 |
| **ai-boss-os** | AI Engineer + CEO Agent | Phase 3 orchestrator (planned) | Month 4-6 |
| **[712 ventures]** | Distributed (1 per venture) | Individual business code | Template-based, separate |

---

## DAILY COORDINATION: WORKFLOW & DEPENDENCIES

### Daily Standup (15 min, 10am ET)

```
Backend A: "Completed auth-flow feature. Tests passing. Waiting for DevOps to merge. 
           Blocker: need Supabase role_based_access table. @Data?"

Data: "Can do in 30 min. Will migrate staging first. 10:30am ETA."

Backend B: "Dashboard v2 layout done. Integration tests passing. Ready for staging review. @QA?"

QA: "Running tests now. 15 min to completion."

DevOps: "CI/CD all green. All services deployed to staging. Monitoring nominal."

AI: "Refining agent reasoning. May need to adjust types if storage changes. @Backend?"

Backend A: "No planned changes for 2 weeks."

You: "All tracking well. Keep shipping. QA—sign off on prod Tuesday 2pm?"

QA: "Confirmed."
```

### Code Review & Merge Process

```
1. Backend A pushes feature/auto-workflows

2. GitHub Actions (DevOps CI/CD):
   ├─ Run: npm run lint
   ├─ Run: npm run test automation-agent
   ├─ Run: nx affected:build
   ├─ Build & push: Docker image
   └─ Deploy: Staging

3. Backend B code reviews (logic, security, perf)
   → Approve or request changes

4. QA reviews & manual test staging
   → Sign off or request retesting

5. DevOps verifies:
   - Staging health checks passing
   - No perf regressions
   - Secrets set correctly

6. Merge to main → Auto-deploy to prod
   - All checks pass = merge enabled
   - DevOps does final prod health check
   - Live within 5 min

7. Production monitoring:
   - QA runs smoke tests
   - DevOps watches Grafana
   - Auto-rollback if issues
```

### When Someone Hits a Blocker

```
Backend B: "Dashboard needs Neo4j data but sync hasn't run in 4 hours. Blocker."

Data: "Checking sync logs... Found: Twenty API rate limit. Fixing backoff. 30 min."

Backend B: "Can I test with mock data?"

Data: "Yes. shared/libs/fixtures/sample-opportunities.json"

Backend B: "Testing with mocks now. Will validate when real data ready."

[30 min later]

Data: "Backoff deployed. Sync catching up. Should be complete by 3pm."

Backend B: "Perfect. Staging validated."
```

---

## DEPENDENCY CONSTRAINTS (Monorepo Rules)

### What Each Service CAN Import

```
automation-agent:
  ✅ shared/libs/{types, config, logger, neo4j-client, supabase-client, 
                  email, constants, exceptions}
  ✅ External: anthropic, apscheduler, httpx, neo4j, supabase, sendgrid
  ❌ NO: other services (webhook-receiver, dashboard-api, claude-agent)

webhook-receiver:
  ✅ shared/libs/{types, config, logger, exceptions, validators, webhooks, constants}
  ✅ External: fastapi, httpx, supabase
  ❌ NO: other services

dashboard-api:
  ✅ shared/libs/{types, config, logger, exceptions, validators, constants}
  ✅ External: fastapi, supabase, pydantic
  ❌ NO: other services

claude-agent:
  ✅ shared/libs/{types, config, logger, exceptions, anthropic-client}
  ✅ External: anthropic, langchain, neo4j
  ❌ NO: other services

sync-service:
  ✅ shared/libs/{types, config, logger, exceptions, neo4j-client, supabase-client}
  ✅ External: httpx, neo4j, supabase
  ❌ NO: other services
```

**Why?** Services communicate via APIs, events, or shared data stores — not direct imports. Prevents circular dependencies.

---

## WEEK-BY-WEEK TEAM TASKS (30-Day Sprint)

### Week 1: Infrastructure & Deployment

**You:**
- Monday: Review plan, approve sprint
- Tue-Wed: Verify databases online
- Thu: Check containers running
- Fri: Go/no-go for Week 2

**Backend A:**
- Deploy automation-agent locally ✓
- Deploy sync-service locally ✓
- Write unit tests ✓
- Integration test (real Neo4j)

**Backend B:**
- Deploy webhook-receiver locally ✓
- Deploy dashboard-api locally ✓
- Write unit tests ✓
- Integration test (real Supabase)

**DevOps:**
- Monday: Docker Compose wired up
- Tue-Wed: Database provisioning (Supabase, Neo4j, Qdrant)
- Thu: CI/CD pipeline skeleton
- Fri: Health checks passing

**Data:**
- Monday: Neo4j schema drafted
- Tue: Supabase migrations written
- Wed: Deploy to staging
- Thu-Fri: Seed test data (50 contacts)

**AI:**
- Review services
- Design agent framework skeleton
- Prepare for Week 2

**QA:**
- Setup test environment
- Write first test (birthday reminder)
- Test all services startup
- Document test plan

**Security:**
- Review .env template
- Design RBAC structure
- Identify compliance requirements

### Week 2: Data Layer & Integration

**Backend A+B:**
- Implement event bus (Redis Streams)
- Cross-service integration tests
- API rate limiting + retry
- Staging deployment & validation

**DevOps:**
- Setup event bus (Redis)
- Wire up service-to-service messaging
- Setup Prometheus + Grafana
- Create alerting rules
- Setup log aggregation

**Data:**
- Optimize all schema
- Create validation checks
- Setup automated backups
- Optimize indexes (query performance)

**AI:**
- Start agent framework build
- Design Wealth Agent state machine
- Prepare for Week 3 implementation

**QA:**
- Write integration tests
- Test event propagation
- Staging validation
- Identify edge cases

**Security:**
- Design audit logging
- Draft RBAC implementation
- Prepare security review checklist

### Week 3: Agents & Reasoning

**Backend A+B:**
- Implement skill execution pipeline
- Add telemetry to services
- Performance optimization
- Security hardening

**DevOps:**
- Setup agent deployment (containerized)
- Configure agent monitoring
- Setup rate limiting per agent
- Test horizontal scaling

**Data:**
- Build memory layer (persistent context)
- Create vector embeddings pipeline
- Optimize graph queries for reasoning

**AI:**
- Build Wealth Agent (relationship decisions)
- Implement 10 core skills
- Setup evaluation framework
- Create agent memory/context
- Test reasoning loop end-to-end

**QA:**
- Test agent reasoning (does it make sense?)
- Test skill execution (all 10)
- Test agent coordination
- Staging E2E workflow test

**Security:**
- Review agent decision logs
- Implement audit trail
- Setup compliance monitoring
- Begin penetration testing

### Week 4: Security, Scaling, Production Ready

**Backend:**
- Code security review (OWASP)
- Fix security findings
- Final optimizations

**DevOps:**
- Database replication & failover
- Backup testing (restore from backup)
- Load testing (10x traffic)
- Production rollout procedures
- On-call setup

**Data:**
- Verify data consistency (all stores)
- Test point-in-time recovery
- Optimize final queries
- Finalize backup strategy

**AI:**
- Evaluation framework complete
- Agent decision logs reviewed
- Prompt optimization (feedback)
- Finalize memory management

**QA:**
- Full E2E production readiness test
- Security validation
- Performance validation
- Sign-off for prod deployment

**Security:**
- Complete penetration testing
- RBAC implementation & validation
- Audit logging verification
- Compliance checklist (GDPR, SOC2)
- Security sign-off

**You:**
- Monday: Security review sign-off
- Wednesday: Final prod readiness review
- Friday: Production go/no-go decision

---

## SUMMARY TABLE

| Person | Role | Primary Repo | Daily Activity | Blocker Authority |
|--------|------|--------------|-----------------|-------------------|
| You | CEO/Strategy | All (approver) | Advisor calls, decisions | Go/no-go, approval |
| Backend A | Services | monorepo | Automation + sync coding | API changes, types |
| Backend B | API/Webhook | monorepo | Dashboard + webhook coding | Data schema, contracts |
| DevOps | Infrastructure | monorepo (CI/CD) | Service ops, deployment | Prod secrets, scaling |
| Data | Databases | monorepo (shared/libs) | Schema, migrations | Query perf, schema |
| AI | Agents | monorepo (services/) | Agent development | Reasoning, skills |
| QA | Testing | monorepo (tests/) | Test automation | Prod sign-off |
| Security | Compliance | monorepo (security/) | Auth, audit, pen test | Security sign-off |

---

## 3 CRITICAL QUESTIONS FOR YOU

1. **Do you have these 7 people?** Can you hire/outsource missing roles?
2. **Monorepo structure OK?** Confirms you want 5 services + shared libs in one repo?
3. **Start Week 1 now?** Can DevOps provision databases this week?
