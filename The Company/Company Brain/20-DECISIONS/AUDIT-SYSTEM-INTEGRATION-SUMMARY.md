[[STARTHERE]] | [[20-DECISIONS/README|Decisions Index]] | [[REALITY]]

# Audit System Integration — How To Use Across Operations & Portfolio

**Question:** How should the audit framework be used for our companies and with them as well?

**Answer:** Three integrated systems working together.

---

## SYSTEM 1: REALITY LEDGER (Single Source of Truth)

**What it is:** [[REALITY|00-CONSTITUTION/REALITY.md]]

**What it does:**
- Documents what's actually working (not what we assume)
- Prevents fake-completion claims
- Drives decision-making

**Who uses it:**
- Founders → decide where to invest time
- Engineers → know what to prioritize
- Investors → assess capital allocation

**Updated by:**
- Weekly audits of Tier-0 ventures (Monday)
- Monthly audits of top 50 (1st Monday)
- Quarterly board audits (quarterly)

**Example entries:**
```
OPS-001: ✅ READY for revenue (8 files to commit, then cold calls)
LT-005: ✅ READY for revenue (add 5 env vars, then calls)
CALLCENTER: ✅ READY for revenue (Twilio creds + backend)
CON-001: 🟡 6 hours from revenue (build API endpoints)
RE-001: 🟡 25 hours from revenue (build deal engine)
LT-011: 🔴 30+ hours, DEFER for now
```

---

## SYSTEM 2: VENTURE-AUDIT-FRAMEWORK (How To Test)

**What it is:** [[VENTURE-AUDIT-FRAMEWORK|20-DECISIONS/VENTURE-AUDIT-FRAMEWORK.md]]

**What it does:**
- Defines the 12-layer audit methodology
- Specifies scoring rubric (0–5)
- Lists transaction spines for each venture type
- Provides critical-test checklist

**Who uses it:**
- QA teams → test complete transactions
- Engineers → verify API/DB/integration functionality
- Product managers → assess product completeness

**How it works:**

1. **Pick a venture** (e.g., OPS-001)
2. **Follow the transaction spine:**
   ```
   Employer → Request workers → Create job → Quote → 
   Agreement → Placement → Worker deployed → Hours verified → 
   Invoice → Payment
   ```
3. **Score each layer (0–5):**
   - Layer 1 (Identity): Can customer explain what we do? [Score: 5]
   - Layer 2 (UX): Can employer navigate site? [Score: 4]
   - Layer 3 (Lead capture): Can they submit a job? [Score: 5]
   - ...
   - Layer 12 (Business proof): Can we complete employer→payment? [Score: 3]
4. **Calculate composite score:**
   ```
   Product Score = Layers 1–3 average
   Technical Score = Layers 4–7 average
   Operations Score = Layer 8 average
   Commercial Score = Layers 9–12 average
   ```
5. **Document blockers** (if any)
6. **Update REALITY.md**

---

## SYSTEM 3: AUDIT-SYSTEM-IMPLEMENTATION (How To Operationalize)

**What it is:** [[AUDIT-SYSTEM-IMPLEMENTATION|20-DECISIONS/AUDIT-SYSTEM-IMPLEMENTATION.md]]

**What it does:**
- Defines weekly/monthly/quarterly cadence
- Integrates with ClickUp, Neo4j, Supabase
- Shows how to use audit data for capital decisions
- Ties audit results to engineering priorities

**Who uses it:**
- Operations manager → runs weekly audits
- CFO → uses audit data for capital allocation
- Engineering leads → prioritizes work based on blockers
- Executive team → makes quarterly strategic decisions

**How it works:**

### Level 1: Weekly (Tier-0 only — 5 ventures)

**Time:** 3–5 hours  
**Cadence:** Every Monday  
**Output:** Updated REALITY.md

```
Example: Week of Sep 9

Monday 9 AM: Audit kickoff
├── OPS-001: Test employer→job→placement→payment (90 min)
├── LT-005: Test facility→request→dispatch→delivery→payment (90 min)
├── CALLCENTER: Test inbound call → handling → billing (60 min)
├── CON-001: Test lead→quote→contract (60 min)
└── RE-001: Test venture registry → ownership (60 min)

Monday 4 PM: Document findings
├── Update REALITY.md
├── Create blockers list
├── Commit to GitHub
└── Notify team

Result: 
- OPS-001: Still ready (commit files)
- LT-005: Still ready (add env vars)
- CALLCENTER: Still ready (add creds)
- CON-001: Needs API work (6 hrs)
- RE-001: Needs deal engine (25 hrs)
```

### Level 2: Monthly (Top 50 ventures)

**Time:** Full day (parallel teams)  
**Cadence:** 1st Monday of each month  
**Output:** Venture readiness matrix + priority queue

```
Task assignment (10 engineers × 5 ventures each):
- Engineer 1: Ventures 1–5 (assigned batch)
- Engineer 2: Ventures 6–10 (assigned batch)
- ... (divide 50 ventures across team)

Each engineer:
1. Runs 12-layer audit on 5 ventures
2. Tests transactions end-to-end
3. Documents blockers
4. Updates spreadsheet

Consolidation:
- Combine all audits into master CSV
- Sort by commercial_score DESC
- Identify top 10 "ready to accelerate"
- Identify top 10 "needs pivots"
- Present to executive team
```

### Level 3: Quarterly (Capital Review)

**Time:** 1 week  
**Cadence:** Every Q  
**Output:** Capital allocation plan + board presentation

```
Week 1:
- Run Level 2 audit on all 789 ventures
- Categorize by maturity stage
- Score each for capital deployment

Week 2:
- Build P&L forecasts for top 50
- Assess ownership/cap tables
- Model scenarios (accelerate / pivot / wind-down)
- Calculate total capital needed

Week 3:
- Present findings to board
- Make capital allocation decisions
- Update 5-year plan

Output:
"Q4 capital plan: $2M to Tier-0 (revenue accelerators),
 $500K to Tier-1 (32 ventures approaching revenue),
 $200K to Tier-2 (contingency/pivots)"
```

---

## HOW AUDIT DATA FLOWS THROUGH OPERATIONS

### Daily (No formal audit, informal check-ins)

**OPS team:**
```
Each day, check:
- Did we close any deals? (sales)
- Any delivery rejections? (operations)
- Any payment failures? (billing)

If yes → investigate → update blocker list
If no → continue as planned
```

**Example (LT-005):**
```
Day 1 (Mon): No deliveries booked yet (expected, calls started)
Day 2 (Tue): 3 demo calls completed, 1 facility interested
Day 3 (Wed): First delivery request! ($85) — test end-to-end
  ✓ Order created in system
  ✓ Dispatcher saw assignment
  ✓ Driver assigned
  ✓ GPS tracking worked
  ✓ Proof of delivery photo uploaded
  ✓ Invoice generated
  ✓ Payment processed
→ Layer 12 score = 5 (proven end-to-end)
→ Update REALITY.md
```

### Weekly (Formal audit)

**Operations meeting (Monday 9 AM):**

```
Attendees: Ops manager, 2 engineers, 1 sales lead

Agenda:
1. Tier-0 status (5 ventures)
   - OPS-001: Still blocked on git commit? Yes/No
   - LT-005: Env vars added yet? Yes/No
   - CALLCENTER: Twilio live yet? Yes/No
   - CON-001: How many API hours done? (Progress: 2/6)
   - RE-001: How many deal-engine hours? (Progress: 3/25)

2. Blockers preventing revenue (top 3)
   - OPS-001: git commit (0.5 hr fix)
   - LT-005: Vercel env vars (0.5 hr fix)
   - CALLCENTER: Twilio credentials (1 hr fix)

3. This week's engineering allocation (40 hrs total)
   - Allocate 8 hrs to OPS-001 (commit + test)
   - Allocate 2 hrs to LT-005 (env vars + test)
   - Allocate 8 hrs to CALLCENTER (creds + backend test)
   - Allocate 12 hrs to CON-001 (continue API build)
   - Allocate 10 hrs to RE-001 (continue deal engine)

4. Revenue status this week
   - OPS-001: 5 cold calls scheduled
   - LT-005: 3 facility demos scheduled
   - CALLCENTER: Live inbound routing enabled
   - Expected: $0 (but "ready" state means can close this week if calls work)

5. Next Monday's priority
   - Will OPS-001 close a deal? (decision point)
   - Will LT-005 close a delivery? (decision point)
   - Will CALLCENTER take a call? (decision point)
```

### Monthly (Portfolio review)

**First Monday of each month (Full-day session):**

```
Morning: Audit parallel team testing
- 10 engineers each test 5 ventures
- Document all 50 in spreadsheet

Afternoon: Consolidation + analysis
- Sort by commercial_score
- Identify patterns (e.g., 12/50 blocked on payments)
- Calculate portfolio "readiness average" (currently 38%)
- Spot opportunities (e.g., 6 ventures 80%+ ready)

Output: Spreadsheet to board + updated REALITY.md

Example: "Sep 1 audit shows:
- 3 ventures ready for revenue (OPS-001, LT-005, CALLCENTER)
- 8 ventures 80%+ ready, need 2–3 days of work
- 15 ventures 50–80%, need 1–2 weeks
- 24 ventures <50%, defer or pivot

Total capital needed to get top 26 to revenue: $400K
Payback period (avg): 8–12 weeks
Expected Sep–Dec revenue: $200–500K"
```

### Quarterly (Board & capital)

**Board meeting (Quarterly):**

```
Presentation deck:

Slide 1: Portfolio overview
- 789 ventures total
- 3 revenue-generating (OPS-001, LT-005, CALLCENTER)
- 26 80%+ ready
- 150 50–80% ready
- 610 <50% (mostly templates)

Slide 2: Tier-0 deep dive
- OPS-001: $X revenue YTD, margin %, blockers
- LT-005: $X revenue YTD, margin %, blockers
- CALLCENTER: $X revenue YTD, margin %, blockers
- CON-001: Ready? Days to first deal?
- RE-001: Ready? Can it model holdings yet?

Slide 3: Capital deployment (Q3–Q4 plan)
- Allocate $500K to Tier-0 (marketing + sales)
- Allocate $300K to Tier-1 (26 ventures, engineering)
- Allocate $100K to Tier-2 (100 ventures, engineering)
- Allocate $50K to contingency

Slide 4: Expected outcome (by Dec 31)
- Tier-0: $500K–$1M cumulative revenue
- Tier-1: 5–10 ventures generating revenue
- Tier-2: 20+ ventures 80%+ ready
- Portfolio value: $10M–$20M

Slide 5: Risks
- Top blocker: [from audit data]
- Ventures requiring pivot: [from audit data]
- Capital runway: 14 months at current burn
```

---

## WHAT TO LOOK FOR IN AUDIT DATA

### Green Flags (Accelerate Funding)

```
✅ Revenue ready (all 4 scores ≥ 80)
✅ First customer acquisition proof
✅ Unit economics positive
✅ No blockers OR blockers <4 hrs to fix
✅ Founder engaged + executing
```

### Yellow Flags (Continue Carefully)

```
🟡 3 composite scores ≥ 70, one <70
🟡 1–3 blockers, fixable in days
🟡 Customer interest but no conversions yet
🟡 Founder engaged but execution slow
🟡 Unit economics uncertain (not proven yet)
```

### Red Flags (Prepare to Pivot)

```
🔴 Any composite score <40
🔴 >5 blockers OR blockers >40 hrs to fix
🔴 No customer interest after 10+ outreach attempts
🔴 Founder engagement < 50%
🔴 Technology fundamentally broken
```

---

## INTEGRATION CHECKLIST

**Week 1 (Sep 9–15):**
- [ ] Run Level 1 audit manually on 5 Tier-0 ventures
- [ ] Update REALITY.md with findings
- [ ] Commit to GitHub
- [ ] Use findings to guide cold calls + fixes

**Week 2 (Sep 16–22):**
- [ ] Build Supabase `ventures_audits` table
- [ ] Set up ClickUp audit task template
- [ ] Run Level 2 audit on top 50 (manual)
- [ ] Populate Supabase + ClickUp

**Month 2 (Oct):**
- [ ] Wire Neo4j audit node connections
- [ ] Set up automated audit queries
- [ ] Run first monthly portfolio audit
- [ ] Present findings to board

**Quarter 2 (Oct–Dec):**
- [ ] Use audit data for all capital decisions
- [ ] Track revenue correlation to audit scores
- [ ] Refine audit methodology based on real data
- [ ] Plan Q4 portfolio strategy based on audits

---

## SUCCESS METRICS

**The audit system is working when:**

1. **Accuracy:** Audit predictions match actual outcomes
   - Example: "Venture scored 70% likely to close first deal in 2 weeks"
   - Reality: 80% of ventures that scored 70+ closed in 2–3 weeks ✅

2. **Speed:** Investment decisions made faster
   - Before: "Is OPS-001 ready for capital?" → 2 weeks to answer
   - After: "Is OPS-001 ready?" → Answer in audit data, 1 day ✅

3. **Confidence:** Capital deployment more profitable
   - Ventures funded post-audit show 30% higher revenue in Month 1
   - ROI on audit infrastructure pays back in 2–3 weeks ✅

4. **Scale:** Can audit 789 ventures monthly
   - 10 engineers × 5 ventures each = 50/month
   - Automate to 100+/month via Supabase queries ✅

---

**Owner:** Operations + Engineering  
**Authority:** CP-033 (Execution) + CP-021 (Revenue)  
**Start date:** 2026-09-09  
**Target:** 100% of Tier-0 (5 ventures) audited weekly by Sep 30

