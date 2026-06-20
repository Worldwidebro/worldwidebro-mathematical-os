# HRMS — Customer Acquisition Strategy (OpenVolo Integration)
**Status**: Ready to execute  
**Target Market**: Finance/HR directors at construction companies  
**Target List Size**: 500+ qualified leads  
**Conversion Goal**: 20-30% trial → paid conversion  
**Timeline**: Start Week 1 (parallel to coding)

---

## 🎯 Ideal Customer Profile (ICP)

### Company Characteristics
- **Industry**: Construction, field services, logistics, facility management
- **Size**: 20-150 employees (too small = DIY Excel, too large = already on ADP/Gusto)
- **Revenue**: $5M-$100M (typically $30K-$100K/month payroll)
- **Geography**: US (start: California, Texas, New York only)
- **Hiring Pattern**: Growing (4-6 new hires/quarter) — high payroll complexity

### Decision Maker Profile
- **Title**: Finance Director, HR Manager, Operations Manager, CEO (if <50 employees)
- **Pain Point**: Manual payroll + multiple tax filings + time-consuming compliance
- **Tech Comfort**: Moderate to high (uses Slack, QuickBooks, spreadsheets)
- **Budget Authority**: Yes (owns HR/Finance budget)
- **Decision Timeline**: 2-4 weeks (faster than enterprise)

---

## 📊 Target List from OpenVolo

### OpenVolo Query
**Goal**: Find construction companies in CA/TX/NY with 20-150 employees

**Data Available in OpenVolo**:
- Company name
- Location (state, city)
- Industry/vertical
- Employee count
- Decision makers (names, titles, emails, phones)
- LinkedIn profiles
- Recent hires (hiring momentum signal)
- Revenue estimates

### Top Sectors to Target (from Worldwidebro ventures)
1. **Construction**: 100 ventures in database
2. **Field Services**: 25 ventures
3. **Logistics & Supply Chain**: 45 ventures
4. **Facility Management**: 30 ventures
5. **Home Services**: 15 ventures

**Total**: ~215 opportunities from internal ventures

### Secondary Target (Cold Outreach)
- General construction companies in target geographies
- OpenVolo has ~50K construction companies in database
- Start with tier 1: CA/TX/NY with 20-150 employees (~2K companies)

---

## 🛠️ Lead Scoring & Prioritization

### High-Priority Leads (Contact First)
- ✅ Construction company
- ✅ 40-120 employees (high payroll complexity)
- ✅ Growing (recent hires or "hiring" status)
- ✅ CEO/Finance Director identified
- ✅ Email + phone available
- **Expected volume**: 300-500 leads
- **Expected response rate**: 5-10% (warm outreach)

### Medium-Priority Leads (Cold outreach Week 3+)
- ✅ Field services / logistics
- ✅ 20-80 employees
- ✅ Based in CA/TX/NY
- **Expected volume**: 1000+ leads
- **Expected response rate**: 1-2% (cold outreach)

### Low-Priority (Backlog)
- Construction companies with <20 or >150 employees
- Other industries (not construction/field services)
- No email/phone available

---

## 📞 Sales Process (OpenVolo → Close)

### Week 1: Discovery Calls (4 calls, 1/day)
**Goal**: Validate product-market fit before coding

1. **Call 1 (Mon)**: Construction company with 50 employees
   - Script: "Hi [Name], I'm building payroll software specifically for construction crews. Currently, how do you handle payroll for [Company]?"
   - Listen: Pain points, current solution, switching willingness
   - Success: "We're dealing with this exact problem" + "I'd trial it"

2. **Call 2 (Tue)**: Logistics company with 30 employees
   - Same script, different industry
   - Goal: Confirm problem is multi-industry, not construction-specific

3. **Call 3 (Wed)**: Field services company with 80 employees
   - Dig deeper: "If we could cut your payroll time in half, would you switch?"
   - Understand decision timeline: "How long would it take you to evaluate?"

4. **Call 4 (Thu)**: Construction company with 100+ employees
   - Test enterprise messaging: "Could benefits management help?"
   - Goal: Understand roadmap priorities

**Outcome**: 3-4 discovery conversations inform product roadmap, 1-2 commit to trial post-launch

---

### Week 2-3: Beta Customer Recruitment (During coding)
**Goal**: Get 3-5 paying customers at launch

**Approach**:
1. Email list from OpenVolo (top 50 prioritized leads)
   - Subject: "We're launching payroll software for construction"
   - Message: "Quick 15-min call to see if this solves your problem"
   - Link: Calendly for discovery call
   - CTA: "Join free trial (limited slots)"

2. Linkedin outreach (secondary, if email bounces)
   - Message: "Building payroll software for construction crews. Interested in free trial?"
   - Response rate: 2-5%

3. Referrals from Week 1 calls
   - "Know any other construction companies struggling with payroll? Refer + both get $100 credit"

**Expected funnel**:
- 50 outreach emails → 3-5 responses → 2-3 discovery calls → 1-2 beta customers

---

### Week 4+: Launch Sales (Post-coding, go-live)
**Goal**: Get 10-15 customers in first month

**Approach 1: Warm List (Week 1 calls + Email responders)**
- Follow up on Week 1 calls: "We launched! Here's the link to try free"
- Follow up on responders: "Demo scheduled for [Date], here's what you'll see"
- Expected conversion: 30-50% (warm, validated demand)

**Approach 2: Cold Email Campaign (Week 4+)**
- Segment OpenVolo list: "Construction, 30-100 employees, CA/TX/NY"
- 100 cold emails/week (spread out)
- Subject lines:
  - "Fix your payroll process [Company name]"
  - "Payroll + tax filing in 1 platform"
  - "Cut payroll time by 70%"
- Expected conversion: 5-10% to trial, 25% of trials to paid

**Approach 3: LinkedIn Campaign (Week 5+)**
- Target Finance/HR Directors in construction
- 20 connections/week + messages
- Message: "[Industry]-specific payroll software. See [competitor] pricing? We're 40% cheaper."
- Expected conversion: 2-5% to trial, 20% of trials to paid

**Approach 4: Referral Loop (Month 2+)**
- Customer 1 gets $100 credit for each referred customer who pays
- Referral rate in payroll software: 30-40% (word-of-mouth strong)
- Expected: 1 of 5 customers acquired via referral by month 2

---

## 📈 Expected Sales Funnel (8 weeks)

| Stage | Week 1-2 | Week 3-4 | Week 5-6 | Week 7-8 | Total |
|-------|----------|----------|----------|----------|-------|
| Discovery calls | 4 | 2 | — | — | 6 |
| Trial signups | 2 | 5 | 8 | 10 | 25 |
| Conversion rate | 50% | 40% | 30% | 25% | 32% |
| Paying customers | 1 | 2 | 2 | 2-3 | 7-8 |
| MRR | $199 | $600 | $1000 | $1500-1800 | $1500-1800 |

**By Week 8**: 7-8 paying customers, $1.5-1.8K MRR (on track for $3-4K by Month 3)

---

## 🤖 OpenVolo Integration via Composio

### Automated Lead Pull
```
Task: Every Monday, pull top 20 new leads from OpenVolo
Composio command: openvolo_search(
  industry: "construction",
  state: ["CA", "TX", "NY"],
  employees: 20-150,
  recently_added: true,  // Companies added in past 7 days
  limit: 20
)
Result: CSV list with name, location, contact, email, phone
Action: Send to Slack #sales for outreach
```

### Lead Enrichment
```
Task: When lead added to Worldwidebro CRM, enrich with OpenVolo data
Composio command: openvolo_company_detail(company_id)
Result: Valuation, funding, growth rate, recent hires
Action: Auto-calculate lead priority score
```

### Contact Sync
```
Task: Sync all contacted leads + outcomes to CRM
Composio command: crm_sync(
  lead_id, 
  status: "called|emailed|trial|customer",
  outcome: "interested|not_interested|call_back_later",
  notes: "..."
)
Action: Build sales pipeline, track conversion rates
```

---

## 📋 Sales Execution Checklist

### Week 1 (Planning)
- [ ] Pull top 50 leads from OpenVolo (construction, 20-150 emp, CA/TX/NY)
- [ ] Export to spreadsheet: Name, Title, Email, Phone, Company
- [ ] Schedule 4 discovery calls (aim for Mon-Thu)
- [ ] Prepare discovery call script
- [ ] Set up Calendly for demo bookings
- [ ] Create trial signup landing page (link in Pitch Kit)

### Week 2 (Recruiting)
- [ ] Complete 4 discovery calls, document findings
- [ ] Email top 50 leads: "Beta customer recruitment"
- [ ] Add calendar link to email for 15-min calls
- [ ] Target 5 demo calls this week
- [ ] Document feedback from calls → feed into product planning

### Week 3 (Validation)
- [ ] Finalize product spec based on discovery calls
- [ ] Continue cold emails (next 50 leads)
- [ ] Target 10 demo calls this week
- [ ] Document 1-2 beta customer commitments

### Week 4 (Launch)
- [ ] Product launches (production-ready)
- [ ] Send "We launched!" email to all demo call people
- [ ] Start conversion push: "Free 14-day trial available"
- [ ] Expected: 2-3 paid customers this week
- [ ] Begin weekly sales cadence (20 new outreach emails/week)

### Weeks 5-8 (Scale)
- [ ] Hit 10-15 customers by Week 8
- [ ] Track CAC (cost per customer acquired)
- [ ] Identify best-performing messaging (cold email, LinkedIn, referral?)
- [ ] Double down on what works
- [ ] Month-end analysis: "What should we double?" "What should we kill?"

---

## 💰 Economics

### CAC (Customer Acquisition Cost)
- **Cold Email**: $0-50/customer (time cost only, no paid ads)
- **Referral**: $100 credit/customer (paid out of margin)
- **Blended CAC by Week 8**: ~$200/customer

### LTV (Customer Lifetime Value)
- **Average tier**: Professional ($499/mo)
- **Average lifetime**: 24 months (assuming 50% annual churn)
- **LTV**: $499 × 24 = $11,976
- **Gross margin**: 60% (SaaS typical) = $7,186
- **LTV/CAC ratio**: $7,186 / $200 = **35.9x** (excellent, >3.0 is healthy)

### Payback Period
- **Monthly margin per customer**: $299 (at $499/mo with 60% margin)
- **Payback period**: $200 CAC / $299 margin = **0.67 months** (21 days)
- **Meaning**: Recovered acquisition cost in 3 weeks

---

## 📊 Weekly Metrics to Track

Every Monday, report to Paperclip:

| Metric | Target | Owner |
|--------|--------|-------|
| New leads pulled from OpenVolo | 20 | Sales ops |
| Emails sent this week | 20 | Sales |
| Demo calls completed | 3-5 | Sales |
| Trial signups from demos | 1-2 | Product |
| Trial-to-paid conversion | 30-40% | Sales/CS |
| Customers acquired | 0-2 | Sales |
| Cumulative MRR | Growing | CFO |
| CAC (this week) | <$300 | Marketing |
| Weekly churn | <5% | CS |

---

## 🎯 Success Milestones

- **Week 2**: First discovery call validates product-market fit
- **Week 4**: First paying customer (proves willingness to pay)
- **Week 6**: 5+ customers, $1K MRR (validates model)
- **Week 8**: 10+ customers, $2K+ MRR (ready to scale)
- **Month 3**: 20+ customers, $4K+ MRR (hire sales person)
- **Month 6**: 50+ customers, $10K+ MRR (profitability possible)

