# Red Team: CON-001 Automation Plan

## Critical Assumptions (Unverified)

| Assumption | Risk | Impact |
|-----------|------|--------|
| CON-001 Supabase connected | If NOT connected, lead intake loop fails immediately | **BLOCKER** |
| Procore + QB APIs exposed | If behind auth walls, n8n can't reach them | **BLOCKER** |
| Stripe account ready | venture.json says "pending" — if not set up, payment loop dead on arrival | **BLOCKER** |
| PlanSwift API accessible | No evidence it has modern API (might be legacy) | **BLOCKER** |
| Houzz/Angi have webhooks | If no webhooks, lead intake requires polling (different architecture) | **BLOCKER** |

---

## What We Haven't Tested

| Component | Status | Risk | Contingency |
|-----------|--------|------|-------------|
| Supabase schema for leads | Unknown | Can't write to venture_leads if table doesn't exist | **MUST VERIFY** |
| Procore API authentication | Not tested | OAuth flow might be complex | Check Procore docs |
| QB API rate limits | Not tested | Could throttle invoice automation | Batch processing needed |
| n8n Docker deployment | Not tested | Render might have resource limits | Test locally first |
| Agency-agents webhook format | Assumed | Wrong JSON format = silent failures | Test with mock data |
| Vercel deployment status | Not verified | If prod environment different from local, loops won't work the same way | Check .vercel/project.json |

---

## Hidden Blockers

### 1. **Authentication Hell**
```
Procore needs: OAuth2 token refresh
QB needs: API key rotation  
PlanSwift needs: ???
Google Workspace needs: service account
```
**Risk:** Token expiration without auto-refresh = loop crashes silently  
**Mitigation:** Build token refresh into n8n workflow

### 2. **API Rate Limiting**
```
Houzz/Angi: Unknown limits (no public docs)
QB: 100 requests/min (tight for high-volume)
Procore: 60 requests/min (even tighter)
```
**Risk:** If we exceed limits, integrations fail silently or are throttled  
**Mitigation:** Batch operations, implement backoff logic

### 3. **Data Schema Mismatch**
```
Our loops expect:
  - venture_leads.email, budget, timeline, complexity
  
But Supabase might have:
  - leads.contact_email (different field name)
  - No complexity field
  - Budget as string not number
```
**Risk:** Loop runs but writes garbage data  
**Mitigation:** Audit Supabase schema BEFORE building loops

### 4. **Agency-Agents Aren't Out-of-Box**
```
Available agents are for software/SaaS (Classifier for code reviews, etc.)
CON-001 needs construction-specific agents
- "Lead Classifier" needs domain knowledge (residential vs commercial, etc.)
- "Estimator Agent" needs pricing logic ($/sqft for different trades)
- "Briefer" needs KPI dashboard format (different from SaaS metrics)
```
**Risk:** We copy-paste agents, they fail silently on construction data  
**Mitigation:** Custom agent development (not "adapt existing")

### 5. **Loop Orchestration Complexity**
```
8 loops, some dependent:
  Lead Intake → Classifier → Estimator → Bid Coordinator
  
If Lead Intake fails, everything downstream breaks
If Classifier hallucinates (gives wrong budget), Estimator prices wrong
```
**Risk:** Cascading failures across loops  
**Mitigation:** Circuit breaker pattern + fallback handlers

---

## Business Risks

| Risk | Scenario | Impact |
|------|----------|--------|
| **Bad lead scores** | Classifier marks $500K project as "low priority" → lost revenue | $50K+ per mistake |
| **Proposal with wrong pricing** | Curator generates $200K estimate for $100K project | Lose deal or margin |
| **Invoice never sent** | Payment loop crashes, customer never gets invoice → 90-day receivables | Cash flow crisis |
| **False anomaly alerts** | Monitor flags every overdue project, team ignores alerts | No one trusts system |
| **Automation breaks silently** | Loop runs but webhook fails → no leads intake for 48 hrs | Lost opportunities |

---

## What Needs Testing Before Phase 2

### Must-Do Before Loop Definition
1. [ ] **Read Supabase schema** — what tables exist? What fields?
2. [ ] **Test Procore API** — can we authenticate? Rate limits?
3. [ ] **Test QB API** — same as Procore
4. [ ] **Check Stripe account** — is it actually set up? Webhook configured?
5. [ ] **Verify Houzz/Angi integration** — do they send webhooks or need polling?
6. [ ] **Examine PlanSwift** — does it have a modern API or just desktop UI?
7. [ ] **Review Vercel deployment** — is the prod app serving real traffic?

### Must-Do Before Agent Development
8. [ ] **Define domain knowledge** — what makes a "good lead" for construction?
9. [ ] **Pricing logic** — how do we estimate? What's the formula?
10. [ ] **KPI definitions** — what metrics matter for CON-001? (revenue, job count, profitability, crew utilization?)
11. [ ] **Error handling** — what if AI agent hallucinates? Fallback to human review?

### Must-Do Before N8n Deployment
12. [ ] **Test locally first** — Docker on local machine, not Render
13. [ ] **Mock all APIs** — test with fake data before hitting real systems
14. [ ] **Set up monitoring** — how do we know if a loop crashes? (Slack alerts? Grafana?)
15. [ ] **Load test** — what if 100 leads come in same hour? Does n8n handle it?

---

## Probability Assessment

| Outcome | Confidence | Why |
|---------|------------|-----|
| Phase 1 tests pass | 95% | ✅ Already verified |
| Phase 2 plan without blockers | 40% | ⚠️ Lots of unknowns (APIs, schema, config) |
| Phase 2 → Phase 3 execution succeeds | 20% | ❌ Cascading risks, hidden API issues |
| CON-001 live with 8 loops by Week 4 | 10% | ❌ Too many untested dependencies |

---

## Revised Timeline (Realistic)

| Phase | Original | Realistic | Buffer |
|-------|----------|-----------|--------|
| Phase 1: Test | 30 min | 30 min | ✅ |
| Phase 2: Plan | 30 min | **4-6 hrs** | API schema audit, domain modeling |
| Phase 3: Execute Loop 1 | 1 week | **2-3 weeks** | Debugging API integrations, schema mismatches |
| Phase 3: Loops 2-8 | 2 weeks | **4-6 weeks** | Each loop reveals new issues |
| **TOTAL** | **4-5 weeks** | **6-10 weeks** | Realistically: **8 weeks to revenue** |

---

## Stop/Go Decision Points

**STOP if:**
- [ ] Supabase schema doesn't have venture_leads table → rebuild Supabase first
- [ ] Procore API requires manual OAuth → delays 1+ week
- [ ] PlanSwift has no API → need manual workaround or scraping
- [ ] Stripe account not activated → pause until ready
- [ ] QB API rate limits prevent real-time invoicing → redesign for batching

**GO if:**
- [ ] All APIs documented and accessible
- [ ] Supabase schema matches loop requirements
- [ ] We build domain-specific agents (not copy-paste existing)
- [ ] We have fallback handlers for loop failures
- [ ] We test locally before deploying to Render

---

## Recommendations

### High Priority (Do Before Phase 2)
1. **Audit CON-001's actual infrastructure**
   - What's actually deployed? Supabase tables? Stripe config? APIs?
   - 1-2 hours reading code + vendor dashboards

2. **Define domain expertise**
   - What pricing model? Complexity scoring? KPI definitions?
   - Requires input from CON-001 operations (30 min call)

3. **Check vendor API capabilities**
   - Can Procore, QB, PlanSwift do what we need?
   - Read their API docs (2-3 hours)

### Medium Priority (Do During Phase 2)
4. **Build construction-specific agents**
   - Don't copy-paste agency-agents
   - Custom training data (construction terminology, pricing, trade skills)

5. **Implement error handling**
   - Circuit breakers, fallbacks, dead-letter queues
   - Slack notifications for all failures

### Defer (Phase 3)
6. Load testing, optimization, scaling

---

## Current Red Team Verdict

| Status | Evidence |
|--------|----------|
| **Framework Tests** | ✅ PASS (CON-001 app builds, Loop Engineering works, agency-agents available) |
| **Infrastructure Tests** | ❌ FAIL (Supabase schema unknown, APIs untested, Stripe pending) |
| **Domain Readiness** | ❓ UNKNOWN (No construction-specific agents, pricing model undefined) |

**Overall:** Frameworks are solid, but **execution is blocked by infrastructure unknowns**.

**Recommendation:** 
- ✅ Phase 1: COMPLETE
- ⚠️ Phase 2: PAUSE for 1-2 day infrastructure audit
- ❌ Phase 3: Don't start until Phase 2 blocker-check passes

**Go/No-Go for Phase 2:** 
**NO-GO** until we verify:
1. Supabase schema (venture_leads table exists)
2. API access (Procore, QB, PlanSwift working)
3. Stripe account (activated + webhook configured)
4. Domain knowledge (pricing logic, complexity scoring defined)

Without these, Phase 2 creates technical debt that Phase 3 can't recover from.

