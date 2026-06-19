# Phase-by-Phase Deep Dive: Operating System Roadmap

---

## PHASE 1: Venture Inventory (Week 1)

### What It Requires

**Input Data Needed:**
- venture_id (CON-001, FIN-002, etc.)
- venture_name (LocalRoof Co, GenixBank, etc.)
- opco (which OPCO owns it)
- owner (who manages it)
- status (Idea/Research/Building/Launching/Operating/Scaling/Archived)
- revenue_ytd (actual revenue this year)
- monthly_burn (monthly cash burn)
- priority (HIGH/MEDIUM/LOW)
- 90day_revenue_potential (realistic 90-day forecast)
- notes (context)

**Sources for This Data:**
1. venture-hub folder structure (we already have all 704 folders)
2. Supabase ventures table (if populated)
3. ClickUp tasks (if tracking ventures there)
4. Interview with owners (for revenue/burn/status)
5. GitHub commits (to infer if building/operating)

**Reality Check:**
- Do we have ACTUAL revenue data? (Probably not — most are ideas)
- Do we know WHO owns each venture? (Partially — need to interview)
- Do we have accurate burn rates? (Probably not — need estimates)
- Can we classify status without talking to owners? (No — requires interviews)

### The Blockers

**1. Information Gap**
Most ventures have:
- ❌ No revenue tracking
- ❌ No owner assigned
- ❌ No financial data
- ❌ No status

**2. Time to Interview**
- 704 ventures ÷ 5 per hour = 140 hours
- With 1 person: 4 weeks
- With 2 people: 2 weeks
- With 4 people: 1 week

**3. Definition of "Operating"**
What counts as operating?
- Has customers? ✓
- Making revenue? ✓
- Has a team? Maybe
- Has a product? Maybe
- Is live? Maybe

**Solution:**
Define status criteria FIRST:
- Idea: Concept only, no work started
- Research: 10+ hours work, market validation started
- Building: Active development, 50+ hours invested
- Launching: Product/service ready, going to market
- Operating: Live, has customers/revenue
- Scaling: Proven model, expanding
- Archived: Dead, not pursuing

### Realistic Timeline

**Week 1 Actual (not optimistic):**
- Day 1: Create CSV template
- Day 2: Script to extract 704 venture folders
- Day 3-5: Interview owners for operating ventures only (47 ventures × 30 min = 24 hours)
- Day 5: Classify remaining 657 as "Idea" with notes

**Output: VENTURE_INVENTORY_MASTER.csv with:**
- 47 ventures: Full data (revenue, burn, owner, status)
- 657 ventures: Minimal data (name, OPCO, status=Idea, notes=needs followup)

---

## PHASE 2: Command Center Dashboard (Week 2)

### Option A: Airtable (Recommended)

**Setup (1 day):**
1. Create Airtable workspace
2. Create base: "Worldwidebro Portfolio"
3. Create table: "Ventures" (704 records)
4. Link to OPCO table
5. Create 5 views

**Table Structure:**
```
Ventures
├── venture_id (text)
├── venture_name (text)
├── opco (link to OPCO table)
├── owner (text or link to People)
├── status (select: Idea/Research/Building/Launching/Operating/Scaling)
├── revenue_ytd (currency)
├── monthly_burn (currency)
├── priority (select: HIGH/MEDIUM/LOW)
├── 90day_potential (currency, formula)
├── last_updated (date)
└── notes (long text)
```

**5 Views:**

**View 1: Executive Dashboard**
- Filter: Operating + Scaling only
- Sort: revenue_ytd DESC
- Show: venture_name, revenue_ytd, owner, priority
- Count: Shows # operating ventures
- Sum: Shows total revenue

**View 2: OPCO Summary**
- Grouped by: opco
- Summary: Count, Sum(revenue_ytd), Avg(monthly_burn)
- Shows portfolio health per OPCO

**View 3: Status Funnel**
- Filter: All
- Grouped by: status
- Summary per group: Count, Sum(revenue_ytd)
- Shows progression

**View 4: Revenue Leaders**
- Sort: revenue_ytd DESC
- Filter: Operating OR Scaling
- Show top 20
- Shows quick wins

**View 5: Red Flags**
- Filter: monthly_burn > revenue_ytd (losing money)
- Sort: burn DESC
- Shows what needs intervention

**Automation (1 day):**
- Slack alerts when status changes
- Email when revenue_ytd drops
- Monthly summary report

**Cost:** $120/month (Airtable Pro)
**Time to build:** 2 days
**Time to populate:** 3 days (with data from Phase 1)

### Option B: Notion (Free but slower)

**Pros:**
- Free
- Pretty dashboards
- Integrates with other docs

**Cons:**
- Slower for 704 records
- Limited filtering/sorting
- No good automation

**Recommended:** Skip Notion, use Airtable

---

## PHASE 3: 90-Day Quick Wins ($365K/month)

### Realistic Assessment

**Can we hit $365K/month in 90 days?**

Currently operating:
- OPCO-Staffing: $28K/month (1 venture)
- OPCO-Construction: $32K/month (1 venture)
- OPCO-Operations: ~$18K/month (scattered)
- OPCO-Marketplace: $8K/month (1 venture)
- Other: ~$5K/month
- **Total: ~$91K/month**

To reach $365K/month, we need:
- +$274K/month additional revenue in 90 days

### The Venture Reality

**OPCO-Staffing (Current: $28K → Target: $100K)**
- Current: 1 recruiter, 5-10 placements/month
- To 10x: Need 5-10 recruiters, 50-100 placements/month
- Capital needed: $50K (recruiting tech, ads, payroll)
- Timeline: 90 days realistic? YES, but requires hiring NOW
- Blocker: Finding 5-10 good recruiters

**OPCO-Construction (Current: $32K → Target: $80K)**
- Current: 1 contractor, 3-5 jobs/month
- To 2.5x: 3-4 contractors, 10-15 jobs/month
- Capital needed: $10K (marketing, tools)
- Timeline: 90 days realistic? YES, repeatable model
- Blocker: Finding contractors + steady job flow

**OPCO-Operations (Current: $18K → Target: $75K)**
- Current: Several ventures, uncoordinated
- To 4x: Standardize process, scale BPO
- Capital needed: $20K (training, tools, marketing)
- Timeline: 90 days realistic? MAYBE, needs process standardization
- Blocker: Who standardizes? (needs ops lead)

**OPCO-Marketplace (Current: $8K → Target: $60K)**
- Current: Beta with 50 vendors
- To 7x: Scale to 500 vendors
- Capital needed: $30K (marketing, features, customer support)
- Timeline: 90 days realistic? RISKY, needs product + GTM
- Blocker: Network effects (hard to force)

**OPCO-Technology (Current: $0 → Target: $50K)**
- Current: Concepts only
- To generate revenue: Launch AI agency
- Capital needed: $15K (tools, marketing, payroll)
- Timeline: 90 days realistic? MAYBE, if team already exists
- Blocker: Do we have 2-3 engineers ready?

### Reality Check

**IF we execute perfectly on 3 out of 5:**
- Staffing: $60K/month
- Construction: $50K/month
- Operations: $40K/month
- **Total: $150K/month (not $365K)**

**Why the gap?**
- Hiring takes 4-6 weeks
- Sales take 2-4 weeks to show results
- Scaling compounds, not linear
- Unforeseen blockers (ops issues, team, market)

**More Realistic 90-Day Target: $150-200K/month**

---

## PHASE 4: Horizontal Teams (Month 2)

### Team Composition & Reality

**Finance (1 CFO + 1 Controller)**
- Salary: $150K CFO + $80K Controller = $230K/year
- Time to hire: 6-8 weeks
- Can you find someone part-time? Maybe $120K for both
- What they do: P&Ls, capital allocation, fundraising, tax

**Sales (1 VP Sales + 2 Account Managers)**
- Salary: $120K VP + $60K × 2 AMs = $240K/year
- Time to hire: 4-6 weeks
- Can you find experienced people? Hard in tight market
- What they do: Pipeline, customer acquisition, partnerships

**Operations (1 VP Ops + 1 Operations Manager)**
- Salary: $100K VP + $60K Manager = $160K/year
- Time to hire: 4-6 weeks
- What they do: SOP documentation, process automation, QA

**Technology (1 CTO + 2 Engineers)**
- Salary: $150K CTO + $100K × 2 Engineers = $350K/year
- Time to hire: 8-12 weeks (hard to find good engineers)
- What they do: CRM, AI agents, automation, infrastructure

**Marketing (1 CMO + 1 Marketing Manager)**
- Salary: $120K CMO + $60K Manager = $180K/year
- Time to hire: 4-6 weeks
- What they do: Brand, campaigns, lead gen, content

**HR (1 Head of People)**
- Salary: $80K/year
- Time to hire: 3-4 weeks
- Part-time initially? Yes
- What they do: Recruiting, contractor management, benefits

**Legal (1 General Counsel)**
- Salary: $150K/year
- Time to hire: 8+ weeks
- Can hire part-time/contract? YES, recommended
- What they do: Contracts, compliance, risk

**Data (1 Data Analyst)**
- Salary: $80K/year
- Time to hire: 4-6 weeks
- Part-time initially? YES
- What they do: Dashboards, KPIs, forecasting

### Total Cost (Year 1)
- Full team: $1.5M/year
- Part-time/contract approach: $700K/year

### Realistic Hiring Path

**Month 2 (Immediate hire):**
- Finance: 1 part-time CFO ($120K/year)
- Operations: 1 VP Ops ($100K/year)
- Sales: 1 VP Sales ($120K/year)
- **Cost: $340K/year**
- **Can cover with $365K/month revenue target**

**Month 3-4 (Add to team):**
- Technology: 1 CTO + 1 Engineer ($250K/year)
- Marketing: 1 CMO ($120K/year)
- **Add cost: $370K/year**
- **Total: $710K/year**

**Blocker: Finding good people**
- In this market, a strong CFO takes 8-10 weeks to hire
- A strong CTO takes 10-12 weeks
- Need to start recruiting NOW

---

## PHASE 5: 18-PDF Master Template (Month 2)

### What Goes In It

**Document 1: Business Profile**
- Company name, DBA, formation date
- Industry, niche, market size
- Mission, vision, target customer
- 1-2 page summary

**Document 2: Formation Documents**
- Articles of organization (LLC/Corp)
- EIN letter
- State registration
- 5-10 pages

**Document 3: Financial Model**
- Startup costs (equipment, marketing, team)
- 3-year revenue projection
- Monthly P&L model
- Break-even analysis
- 3-5 pages with spreadsheets

**Document 4: Marketing Plan**
- Customer acquisition strategy
- Target customer profile
- Lead generation channels
- Marketing budget
- 2-3 pages

**Document 5: Sales Process**
- Sales pipeline
- Average deal size (ACV)
- Sales cycle length
- Conversion rates
- 2-3 pages

**Document 6: Operations Manual**
- Daily/weekly procedures
- Quality checklist
- Vendor relationships
- Contingency plans
- 3-5 pages

**Document 7: Technology Stack**
- Software/tools used
- Infrastructure (cloud, hosting)
- Integrations
- Data security
- 2 pages

**Document 8: Org Chart**
- Current team structure
- Roles & responsibilities
- Key person risk
- Hiring plan
- 1 page

**Document 9: Customer Contracts**
- Standard agreement template
- Payment terms
- Cancellation policy
- 2-3 pages

**Document 10: Supplier Agreements**
- Key suppliers/vendors
- Contract terms
- Pricing
- 2-3 pages

**Document 11: KPI Dashboard**
- Monthly revenue target
- Profitability target
- CAC/LTV
- Churn rate
- Growth rate
- 1-2 pages

**Document 12: 90-Day Plan**
- Q1 priorities
- Key milestones
- Team goals
- Budget allocation
- 1-2 pages

**Document 13: Quarterly Review Template**
- Revenue vs. plan
- Expense vs. budget
- Team updates
- Risks & blockers
- 1-2 pages

**Document 14: Risk Assessment**
- Key risks identified
- Mitigation strategies
- Contingency plans
- 2-3 pages

**Document 15: Competitive Analysis**
- Direct competitors
- Competitive advantages
- Market positioning
- 2-3 pages

**Document 16: Scaling Strategy**
- How to 2x, 5x, 10x revenue
- Bottlenecks & solutions
- Expansion timeline
- 2-3 pages

**Document 17: Acquisition Plan** (if applicable)
- Acquisition targets
- Integration plan
- Timeline
- 1-2 pages

**Document 18: Annual Review**
- Year summary
- What worked/didn't
- Lessons learned
- Next year plan
- 2-3 pages

### Total Length: 40-60 pages

**Production:**
- Template design: 1 day
- Example filled: 1-2 days
- Ready to duplicate for all OPCOs

---

## PHASE 6: Governance (Month 3)

### Board Meetings (Monthly)

**Attendees:**
- CEO (you)
- CFO (Finance lead)
- COO (Operations lead)
- CTO (Technology lead)
- External advisor (1 person)

**Agenda (90 minutes):**
1. Portfolio health (15 min) — Revenue, burn, runway
2. Red flags (15 min) — Which ventures are struggling
3. Green lights (15 min) — Which ventures should scale
4. Capital allocation (15 min) — Where to deploy next $50K
5. Hiring (15 min) — Team gaps, recruiting status
6. Strategic (15 min) — Long-term positioning

**Decisions Made:**
- Capital >$50K deployed
- Ventures to SCALE/PAUSE/ARCHIVE
- OPCO president candidates
- Quarterly review schedule

### OPCO Presidents (Quarterly Reviews)

**Each OPCO has 1 president who:**
- Owns P&L for their OPCO
- Manages top 3-5 ventures in OPCO
- Reports KPIs quarterly
- Hires/fires within budget

**Quarterly Review Meeting (60 min):**
1. Revenue vs. plan (15 min)
2. Margin analysis (10 min)
3. Team updates (15 min)
4. Risk/blockers (10 min)
5. Next quarter plan (10 min)

**Decision: Keep / Scale / Sell / Merge / Pause / Archive**

---

## PHASE 7: Real Estate & Investment (Month 4-6)

### Real Estate OPCO Build-Out

**Timeline:**
- Weeks 1-4: Scout 20-50 distressed properties
- Weeks 5-8: Analyze deals, negotiate
- Weeks 9-12: Close 2-3 acquisitions

**Capital needed:** $200K
- Acquisition: $150K
- Renovation budget: $50K

**Revenue model:**
- Rental: $3-5K/month per property ($30-50K/year)
- Flips: $20-50K per deal
- Property mgmt: $1-2K/month per managed property

**To hit $100K/month:**
- 20-30 rental properties, OR
- 3-5 flips per month

**Blockers:**
- Finding capital
- Finding deal flow
- Finding contractors (rehab)

### Investment OPCO Build-Out

**Timeline:**
- Weeks 1-4: Source 10-20 targets
- Weeks 5-8: Analyze, pitch to investors
- Weeks 9-12: Close 1-2 deals

**Capital needed:** $500K initial
- Investment vehicle setup: $50K
- Deal capital: $450K

**Revenue model:**
- Equity returns: 10-30% per year
- Management fees: 2% per year
- Dividend income: 5-8% annually

---

## PHASE 8: Quarterly Reviews (Ongoing)

### Decision Framework

**KEEP**
- Criteria: $10K+/month revenue, positive unit economics, good team
- Action: Support, don't interfere
- Review: Every quarter

**SCALE**
- Criteria: $20K+/month, proven model, team capacity
- Action: More capital, hire, marketing
- Investment: $10-50K per venture
- Target: 2-3x revenue in 12 months

**SELL**
- Criteria: Operating but stalled, not core to strategy, good buyer available
- Action: Find buyer, negotiate, transition
- Timeline: 60-90 days
- Target price: 1-2x annual revenue

**MERGE**
- Criteria: Overlaps with another venture, combined form stronger
- Action: Consolidate teams, eliminate duplication
- Savings: 20-30% cost reduction
- Timeline: 30 days

**PAUSE**
- Criteria: Not ready yet, team issue, market not ready
- Action: Freeze, reassess in 90 days
- Timeline: Revisit Q4
- Cost: Minimal (retain IP, documentation)

**ARCHIVE**
- Criteria: No traction, wrong market, wrong team, no path to revenue
- Action: Shut down, preserve IP/docs, kill burn
- Timeline: Immediate
- Savings: Stop monthly burn

### Example: Q3 Review

**EC-001 (Marketplace)**
```
Revenue: $45K/month (target: $30K) ✓✓
Margin: 35%
Team: 5 people (need +2)
Capital spent: $50K
Capital needed: +$50K
Risks: Competitor entering, churn rising
Decision: SCALE
→ Hire 2 more, allocate $50K marketing
```

**FIN-002 (Fintech)**
```
Revenue: $0
Spend: $15K/month
Team: 2 engineers, low morale
Capital spent: $80K total
Product: MVP delayed 2 months
Risks: Team burnout, market validation unclear
Decision: PAUSE
→ Freeze for 90 days, revisit Q4, find new tech lead
```

**TECH-045 (Random AI Tool)**
```
Revenue: $0
Spend: $0
Team: None
Capital spent: $0
Market: Dozens of competitors
Risks: Not differentiated, nobody assigned
Decision: ARCHIVE
→ Kill it, delete repo, document learnings
```

---

## Critical Path (What Must Happen First)

1. **Create VENTURE_INVENTORY_MASTER.csv** (Week 1)
   - Without this, you can't make any other decision
   - Takes 1 week with team effort
   - Blocks: Everything

2. **Set up Airtable dashboard** (Week 2)
   - Visualize the inventory
   - Blocks: Command center readiness

3. **Hire Finance lead** (Month 2)
   - Can't scale without financial oversight
   - Takes 4-6 weeks
   - Blocks: Capital allocation, fundraising

4. **Identify 3-5 quick-win ventures** (Week 3)
   - Not the 704 — just the 3-5 that can hit $365K
   - From dashboard view
   - Blocks: Nothing, can start immediately

5. **Hire operational leads** (Month 2-3)
   - CTO, VP Sales, VP Ops
   - Takes 4-12 weeks
   - Blocks: Scaling ventures

---

## Bottom Line

**Realistic 90-Day Outcome (not optimistic):**
- Inventory: ✅ Complete
- Dashboard: ✅ Live
- Revenue: $150-200K/month (not $365K)
- Ventures operating: 80-100 (not 150)
- Teams hired: Finance + Ops only (not full 8)
- Governance: Monthly board only (not full structure)

**Why less than planned?**
- Hiring timeline (takes 6-8 weeks per person)
- Revenue growth compounds, not linear
- Unexpected blockers (team issues, market)

**What's possible:**
- Turn off 30% of cash burn (archive zombies)
- 2-3x revenue in 6 months with right team
- Foundation for $1M/month by month 12

