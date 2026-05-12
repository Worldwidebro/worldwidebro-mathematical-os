# HRMS SaaS — Business Logic & Execution Plan
**Status**: Pre-launch planning  
**Target Launch**: May 25, 2026 (2 weeks)  
**Base Template**: Mission Control fork  
**Revenue Target**: $3-4K MRR by Week 8

---

## 🎯 Product Definition

### Target Customer
- **Persona**: Finance/HR Director at construction/field service companies
- **Company Size**: 10-100 employees
- **Problem**: Multi-location payroll, tax compliance, employee records scattered
- **Willingness to Pay**: $199-$499/month (proven by Gusto pricing)

### MVP Feature Set
- ✅ Employee directory (add/edit/delete)
- ✅ Payroll runs (calculate, review, approve)
- ✅ Tax withholding (US Fed + State, 2-3 states max)
- ✅ Pay stub generation & email
- ✅ Compliance reports (W-2, quarterly filings)
- ❌ Benefits management (post-MVP, Week 4+)
- ❌ Integrations (post-MVP, Week 3+)

### Pricing Strategy
| Tier | Employees | Price | Features |
|------|-----------|-------|----------|
| Starter | 1-10 | $199/mo | Basic payroll, tax filing |
| Professional | 11-50 | $499/mo | + Compliance reports, audit log |
| Enterprise | 51+ | $999/mo | + Custom workflows, API access |

---

## 🔴 CRITICAL BLOCKERS (Must Resolve Before Coding)

### Blocker 1: Payroll Compliance & Tax Law
**Status**: ⚠️ Not reviewed  
**Risk Level**: HIGH (payroll errors = legal liability)

**Required Actions**:
1. [ ] Confirm target states: US only, which states? (recommend: CA, TX, NY first — covers 30% of US population)
2. [ ] Get CPA review of tax withholding logic (don't code without this)
3. [ ] Document compliance checklist:
   - [ ] Federal income tax (IRS tables by year)
   - [ ] State income tax (varies by state, some have no income tax)
   - [ ] FICA/Social Security/Medicare (fixed %)
   - [ ] Unemployment insurance (FUTA/SUTA)
   - [ ] Local taxes (some cities charge local income tax)
4. [ ] Define scope: "What tax scenarios are NOT supported in MVP?"
   - Example: "We don't support 1099 contractors in v1.0"
   - Example: "We don't support international payroll in v1.0"

**Owner**: Hire CPA for 2-hour review ($500-1K)  
**Timeline**: 1 day  
**Block**: Cannot start database schema or payroll calculation code without this

---

### Blocker 2: Product-Market Fit Validation
**Status**: ⚠️ Not validated  
**Risk Level**: HIGH (could build wrong product)

**Required Actions**:
1. [ ] Schedule 4 discovery calls with construction company finance directors
   - Use OpenVolo to find contacts
   - Call script: "We're building payroll software for field service companies. What's your biggest pain point today?"
   - Goal: Understand top 3 problems, confirm pricing assumption
2. [ ] Ask specific questions:
   - [ ] How many employees? (validates our tier sizing)
   - [ ] Current payroll process? (understand workflow)
   - [ ] Switching cost from current solution? (Gusto, ADP, manual, Excel)
   - [ ] Must-have features? (benefits? time tracking? direct deposit?)
   - [ ] Price sensitivity? (would you pay $199/mo? $99/mo?)
3. [ ] Document findings in HRMS-CUSTOMER-ACQUISITION.md

**Owner**: Sales/CEO  
**Timeline**: 2-3 days (1 call/day)  
**Block**: Feature prioritization depends on feedback

---

### Blocker 3: Sales Process & Messaging
**Status**: ⚠️ Not defined  
**Risk Level**: MEDIUM (can't convert without clear pitch)

**Required Actions**:
1. [ ] Define 3-call sales process:
   - Call 1 (15 min): Discovery — understand their payroll pain
   - Call 2 (30 min): Demo — show how we solve it
   - Call 3 (15 min): Close — pricing, trial length, next steps
2. [ ] Create sales script:
   - Opening: "Hi [Name], we're solving [specific pain] for [industry]. Do you have 15 minutes?"
   - Pain discovery: "Walk me through how you handle payroll today"
   - Value prop: "Here's how we make that 10x faster and eliminate errors"
   - Close: "Want to try free for 14 days? Just add your first employee to see it work"
3. [ ] Define trial structure:
   - 14 days free (industry standard)
   - Auto-convert to paid on day 15 unless cancelled
   - Credit card required at signup (reduces flake)
4. [ ] Define objection handling:
   - "We use Gusto" → "We're $300/mo cheaper, plus designed for field crews"
   - "Payroll is too sensitive" → "We're payroll experts, built to US tax law, backed by [your credibility]"
   - "Can't switch mid-cycle" → "Start next pay period, we handle migration"

**Owner**: Sales/Marketing  
**Timeline**: 1-2 days  
**Block**: Can't launch without clear pitch

---

### Blocker 4: Billing & Subscription Logic
**Status**: ⚠️ Partially defined  
**Risk Level**: MEDIUM (bugs cost revenue)

**Required Actions**:
1. [ ] Define billing rules:
   - Monthly billing on same day each month
   - Prorated charges for mid-cycle upgrades (e.g., add 5 more employees = +$X for rest of month)
   - Downgrade effective next billing cycle (no refunds mid-cycle)
2. [ ] Define trial-to-paid flow:
   - Trial signup: collect email + password, no credit card (lower friction)
   - Day 13: Send email "Your trial ends in 1 day"
   - Day 14: Send email "Add payment method to keep using HRMS" (link to billing page)
   - Day 15 midnight: If no payment → disable account, send "reactivate" email
3. [ ] Define usage-based scaling:
   - Customer views "11 employees entered" → tier updates to Professional ($499/mo)
   - Charge difference prorated to current billing cycle
   - Send email: "Your plan upgraded to Professional ($300 more this month)"
4. [ ] Define cancellation flow:
   - Customer clicks "Cancel subscription"
   - 2-question survey: "Why cancel?" (required) + "Feedback?" (optional)
   - Confirm: "Account data preserved for 30 days, can reactivate anytime"
   - Last invoice generated, access disabled

**Owner**: Developer (Stripe integration)  
**Timeline**: 2-3 days (code + testing)  
**Block**: Cannot launch without this

---

## 📊 Financial Metrics & Monitoring

### Weekly Tracking (Every Monday)
| Metric | Target | Owner | Action if Red |
|--------|--------|-------|--------------|
| Trial signups | 2-3/week | Sales | Adjust messaging, increase outreach |
| Trial conversion rate | 20-30% | Product | Add feature, improve onboarding |
| CAC (Cost per customer) | <$500 | Sales | Lower ad spend, focus on organic |
| Average revenue per user (ARPU) | $250 | Product | Upsell to higher tiers |
| Churn rate | <5% / month | CS | Call churners, ask why, improve |
| NRR (Net revenue retention) | >100% | Product | Add features, increase stickiness |

### Daily Tracking (Ops Dashboard)
- Trial accounts created (shows demand)
- Trial accounts with ≥1 employee added (shows activation)
- Accounts on day 7+ (early churn signal)
- Failed payments (billing issue)

### Monthly Review (1st of month)
- Cohort analysis: "Customers acquired in Month 1 — how many still active in Month 2/3/4?"
- LTV calculation: Average customer lifetime value (based on current churn)
- CAC payback: How many months to recoup acquisition cost

---

## 🔧 Data Model & Schema

### Core Tables
```sql
-- Companies (customers)
CREATE TABLE companies (
  id uuid primary key,
  name text,
  industry text,
  state text (target state for tax withholding),
  subscription_tier text (starter|professional|enterprise),
  employee_count int,
  created_at timestamp,
  status text (trial|active|cancelled),
  trial_ends_at timestamp
);

-- Employees
CREATE TABLE employees (
  id uuid primary key,
  company_id uuid references companies,
  first_name text,
  last_name text,
  email text,
  ssn text (encrypted),
  date_of_birth date,
  hire_date date,
  salary numeric,
  pay_frequency text (weekly|biweekly|monthly),
  status text (active|inactive),
  created_at timestamp
);

-- Payroll Runs (monthly/biweekly)
CREATE TABLE payroll_runs (
  id uuid primary key,
  company_id uuid references companies,
  period_start date,
  period_end date,
  status text (draft|submitted|processed|paid),
  gross_payroll numeric,
  total_taxes numeric,
  net_payroll numeric,
  created_at timestamp,
  approved_by uuid references employees,
  approved_at timestamp
);

-- Payroll Details (per employee per run)
CREATE TABLE payroll_details (
  id uuid primary key,
  payroll_run_id uuid references payroll_runs,
  employee_id uuid references employees,
  gross_pay numeric,
  federal_tax numeric,
  state_tax numeric,
  fica_tax numeric,
  net_pay numeric,
  pay_stub_sent_at timestamp
);

-- Tax Settings
CREATE TABLE tax_settings (
  id uuid primary key,
  company_id uuid references companies,
  state_code text (CA, TX, NY, etc),
  fed_w4_allowances int,
  state_w4_allowances int,
  unemployment_rate numeric,
  filing_status text,
  created_at timestamp,
  updated_at timestamp
);

-- Compliance Reports
CREATE TABLE compliance_reports (
  id uuid primary key,
  company_id uuid references companies,
  report_type text (w2|941|unemployment|state_quarterly),
  period text (2026-Q1, etc),
  filed_date date,
  due_date date,
  status text (draft|filed),
  created_at timestamp
);
```

---

## 🚀 Launch Checklist

### Week 1: Planning & Validation
- [ ] Resolve 4 critical blockers (compliance, PMF, sales, billing)
- [ ] 4 discovery calls completed
- [ ] Legal review signed off
- [ ] Sales script finalized
- [ ] Feature list locked (no scope creep)

### Week 2: Development
- [ ] Database schema created + migrated
- [ ] Employee CRUD APIs working
- [ ] Payroll calculation engine working (federal + 1 state tax)
- [ ] Stripe integration working
- [ ] Onboarding flow functional
- [ ] Deployed to Vercel staging

### Week 3: Sales & Go-Live
- [ ] First 3 beta customers on trial
- [ ] Feedback incorporated (quick wins only)
- [ ] Deploy to production
- [ ] First customer paying
- [ ] Daily metric tracking active

---

## 🎁 Competitive Positioning

**vs. Gusto**:
- "We're $300/mo cheaper, built for field crews (construction, logistics, etc)"

**vs. ADP**:
- "We're simpler, faster to implement, no 30-day setup process"

**vs. Excel/Manual**:
- "1 click to calculate all taxes correctly, auto file compliance reports, employee sees pay stubs online"

**vs. Future Worldwidebro ventures**:
- "Integrated with Worldwidebro construction/logistics/service ventures — one platform for payroll + operations"

---

## 📝 Success Criteria

**Week 4 (First customer)**:
- 1 customer paying $199/mo
- 2-3 on trial
- 0 critical bugs reported

**Week 6 (Proof of concept)**:
- 5-10 customers paying
- $1K-2K MRR
- NRR >100% (customers adding employees)
- Churn <5%

**Week 8 (Validate model)**:
- 15-25 customers
- $3-5K MRR
- CAC <$500 (via organic/referral)
- Decision: Invest in sales & marketing or pivot

