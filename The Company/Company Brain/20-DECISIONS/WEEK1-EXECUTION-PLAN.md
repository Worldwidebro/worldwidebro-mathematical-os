[[STARTHERE]] | [[20-DECISIONS/README|Decisions Index]] | [[REALITY]]

# Week 1 Execution Plan — Agentic Engineering Framework

**Period:** Sep 10–15, 2026  
**Goal:** Revenue-ready state for 3 ventures + demo-ready for 2 others  
**Authority:** CP-033 (Execution)

---

## COMPLETION CRITERIA

| Venture | Completion Criteria | Success Proof |
|---------|---|---|
| **OPS-001** | 8 files committed + cold calls made | Git commit + 10 call logs |
| **LT-005** | Env vars deployed + calls made | Vercel dashboard + call logs |
| **CALLCENTER** | Twilio creds + backend live + inbound calls | Call recording + dashboard |
| **CON-001** | Marketing demo complete + calls made | Screenshots + call logs |
| **RE-001** | Holdings model demo + pitch ready | Screenshots + pitch deck |
| **LT-011** | Assessment complete (architecture candidate?) | Decision document |

---

## TASK DECOMPOSITION — 15-Minute Units

### OPS-001: Git Commit (1 unit = 30 min)

**Unit 1: Review & Stage Uncommitted Files**
- Model: Haiku (simple git operation)
- Time: 15 min
- Risk: None (read-only until final commit)
- Done condition: `git status` shows clean or all staged

```bash
cd repos/ops-staff-001-staffing
git status  # Review uncommitted files
git add .   # Stage all
git commit -m "chore: Production deployment artifacts"
```

**Eval:** Commit succeeds with no CI failures

---

### LT-005: Vercel Env Vars (1 unit = 30 min)

**Unit 1: Add 5 Environment Variables**
- Model: Haiku (config update)
- Time: 15 min
- Risk: Deployment restart needed
- Done condition: Vercel env vars saved + redeploy triggered

Variables to add:
```
VITE_SUPABASE_URL
VITE_SUPABASE_ANON_KEY
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
(+ 1 TBD from deployment logs)
```

**Eval:** Vercel redeploy completes + site loads without console errors

---

### CALLCENTER: Twilio Setup (2 units = 60 min)

**Unit 1: Add Twilio Credentials to Vercel**
- Model: Haiku (env vars)
- Time: 15 min
- Risk: None
- Done condition: Creds in Vercel dashboard

```
TWILIO_ACCOUNT_SID: <value>
TWILIO_AUTH_TOKEN: <value>
```

**Unit 2: Deploy Backend Python Service**
- Model: Sonnet (infrastructure)
- Time: 45 min
- Risk: Service routing
- Done condition: Backend responds on port 3000 + webhooks working

**Eval:** Inbound call test → backend receives webhook + logs call

---

### CON-001: Marketing Demo (1 unit = 45 min)

**Unit 1: Prepare Demo Flow**
- Model: Haiku (UI testing)
- Time: 30 min
- Risk: None (no code changes)
- Done condition: Screenshots captured + walkthrough scripted

Test flow:
1. Home page → Services → Gallery → Contact form
2. Fill form → Submit
3. Confirmation page

**Eval:** All pages load, forms submit, no broken links

---

### RE-001: Holdings Model Demo (1 unit = 60 min)

**Unit 1: Build Holdings Pitch Deck**
- Model: Sonnet (documentation)
- Time: 60 min
- Risk: None
- Done condition: 5-slide deck created + tested in browser

Deck structure:
1. What is Worldwidebro Holdings?
2. How we acquire ventures (CON-001 example)
3. How we generate returns (revenue + appreciation)
4. Current portfolio (6 ventures)
5. Capital needs (Q4 2026)

**Eval:** Deck loads + all images render + presenter notes complete

---

### LT-011: Assessment (1 unit = 60 min)

**Unit 1: Audit Code & Architecture**
- Model: Opus (architecture)
- Time: 60 min
- Risk: None
- Done condition: Assessment document written

Assessment questions:
1. Is this viable infrastructure?
2. Can it power LT-005 (HealthRoute)?
3. How many hours to production-ready?
4. Should we rebuild or buy/integrate?

**Eval:** Decision document has clear recommendation + 2-week roadmap if rebuild

---

## EXECUTION SCHEDULE

### Day 1 (Sep 10): Immediate Wins (90 min, Haiku + quick setup)

```
10:00 AM: OPS-001 git commit (30 min) — READY NOW
10:30 AM: LT-005 env vars (30 min) — READY NOW
11:00 AM: CALLCENTER Twilio creds (15 min) — READY NOW
11:15 AM: Confirm all 3 deployments live
```

**Outcome:** 3 ventures production-ready for revenue attempts

---

### Day 2–3 (Sep 11–12): Demo Readiness (150 min, Haiku + Sonnet)

```
Sep 11:
09:00 AM: CON-001 demo flow (30 min) — HAIKU
09:30 AM: RE-001 pitch deck (60 min) — SONNET
11:00 AM: Test both demos live

Sep 12:
09:00 AM: LT-011 assessment (60 min) — OPUS
10:00 AM: Decision meeting (30 min)
```

**Outcome:** Demo infrastructure ready + LT-011 decision made

---

### Day 4–5 (Sep 13–15): Revenue Execution (Parallel)

```
Sep 13–15:
- OPS-001: 10 cold calls + follow-ups
- LT-005: 5 facility demos + follow-ups
- CALLCENTER: Inbound call monitoring + manual routing
- CON-001: 20 contractor calls + demos
- RE-001: Investor outreach + pitch deck
```

**Outcome:** $7.5K–$20K revenue or high-confidence pipeline

---

## MODEL ROUTING

| Task | Model | Reasoning | Complexity |
|------|-------|-----------|-----------|
| OPS-001 commit | Haiku | Simple git operation | Low |
| LT-005 env vars | Haiku | Config update, no logic | Low |
| CALLCENTER creds | Haiku | Env var copy-paste | Low |
| CALLCENTER backend | Sonnet | Python service + webhooks | Medium |
| CON-001 demo | Haiku | UI testing + screenshots | Low |
| RE-001 deck | Sonnet | Content creation + design | Medium |
| LT-011 assessment | Opus | Architecture + business decision | High |

---

## EVAL-FIRST LOOP

### Baseline Evals (Sep 10, 10 AM)

**OPS-001 Commit:**
```bash
# Baseline: uncommitted files exist
git status | grep "modified:\|new file:" | wc -l
# Expected: 8 uncommitted files

# After commit:
git status
# Expected: "working tree clean"
```

**LT-005 Env Vars:**
```bash
# Baseline: env vars missing
curl -s https://healthroute-courier.vercel.app/api/status | jq '.supabase_ready'
# Expected: false

# After deploy:
curl -s https://healthroute-courier.vercel.app/api/status | jq '.supabase_ready'
# Expected: true
```

**CALLCENTER Twilio:**
```bash
# Baseline: no inbound routing
curl -X POST https://callcenter-eosin.vercel.app/api/twilio/webhook \
  -H "Content-Type: application/json" \
  -d '{"CallSid": "test123", "From": "+1234567890"}'
# Expected: 404 or auth error

# After deploy:
# Same request
# Expected: 200 + log entry in backend
```

### Post-Implementation Evals (Sep 12, 2 PM)

Re-run all baseline evals + verify:
- No regressions in other systems
- Revenue pipeline ready to execute

---

## RISK ASSESSMENT

| Task | Risk | Mitigation |
|------|------|-----------|
| OPS-001 commit | Git merge conflict | Check git log first |
| LT-005 env vars | Vercel deployment fails | Have rollback plan (old vars saved) |
| CALLCENTER backend | Service doesn't start | Test locally first + check logs |
| CON-001 demo | Form doesn't submit | Use curl to verify API |
| RE-001 deck | Missing design assets | Use text + placeholders, upgrade later |
| LT-011 assessment | Wrong decision | Parallel review by ops lead |

---

## SUCCESS METRICS

By Sep 15, 2026:

| Metric | Target | Achieved |
|--------|--------|----------|
| Ventures in revenue-ready state | 3 | OPS-001, LT-005, CALLCENTER |
| Cold calls made | 35+ | OPS-001 (10) + CON-001 (20) + LT-005 (5) |
| Demo-ready ventures | 2 | CON-001, RE-001 |
| Pipeline value identified | $50K+ | From prospect calls |
| First revenue | $5K+ | Any venture, any amount |
| LT-011 decision | Made | Build, buy, or defer |

---

## DECISION GATES

### Gate 1: Sep 11, 2 PM
**Question:** Are OPS-001, LT-005, CALLCENTER all live and taking calls?  
**If YES:** Proceed to cold calls  
**If NO:** Fix blocker immediately

### Gate 2: Sep 13, 9 AM
**Question:** Do we have 10+ qualified leads?  
**If YES:** Proceed to closing  
**If NO:** Increase call volume 2x

### Gate 3: Sep 15, 5 PM
**Question:** Do we have $5K+ in pipeline or $1K+ in closed revenue?  
**If YES:** Week 2 plan: scale winners + fix losers  
**If NO:** Postmortem + adjust strategy

---

## COST & EFFORT TRACKING

| Task | Effort (hours) | Model | Cost | Status |
|------|---|---|---|---|
| OPS-001 commit | 0.5 | Haiku | $1 | READY |
| LT-005 env vars | 0.5 | Haiku | $1 | READY |
| CALLCENTER setup | 1.0 | Haiku+Sonnet | $15 | READY |
| CON-001 demo | 0.5 | Haiku | $1 | READY |
| RE-001 deck | 1.0 | Sonnet | $10 | READY |
| LT-011 assessment | 1.0 | Opus | $50 | READY |
| **TOTAL** | **4.5** | — | **$78** | — |

---

## EXECUTION CHECKLIST

### Sep 10 (Today)

- [ ] OPS-001: `git commit -m "chore: Production deployment artifacts"` + push
- [ ] LT-005: Add 5 Vercel env vars + trigger redeploy
- [ ] CALLCENTER: Add Twilio creds + confirm webhook routing works
- [ ] Verify: All 3 sites load + no console errors
- [ ] Commit audit results to GitHub

### Sep 11

- [ ] CON-001: Screenshot demo flow + create talking points
- [ ] RE-001: Draft pitch deck (5 slides minimum)
- [ ] Test: Both demos work in browser

### Sep 12

- [ ] LT-011: Write assessment document + decision memo
- [ ] Decision: Build, buy, or defer?
- [ ] All evals pass with no regressions

### Sep 13–15

- [ ] OPS-001: Make 10 calls + log outcomes
- [ ] LT-005: Make 5 calls + log outcomes
- [ ] CALLCENTER: Monitor inbound calls
- [ ] CON-001: Make 20 calls + demos
- [ ] RE-001: Send pitch deck to 3 investors
- [ ] Track pipeline value + closed revenue

---

**Owner:** Engineering + Sales  
**Authority:** CP-033 (Execution)  
**Next checkpoint:** Sep 11, 2 PM (Gate 1)
