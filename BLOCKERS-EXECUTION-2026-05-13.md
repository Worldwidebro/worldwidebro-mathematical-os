---
name: BLOCKERS-EXECUTION-2026-05-13
title: HRMS Pre-Launch Blockers — Execution Start
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# HRMS Pre-Launch Blockers — Execution Start

**Date**: May 13, 2026  
**Status**: IN EXECUTION (started now)  
**Critical Path**: All 4 must complete by May 15 for Task 9 to start May 16

---

## BLOCKER 1: Payroll Compliance Review ✅ IN PROGRESS

### What We Need
- CPA sign-off on tax calculation logic (federal + state)
- Compliance checklist for CA, TX, NY
- Documentation of what's NOT in MVP

### Action Items
- [ ] **TODAY**: Find CPA firm with payroll expertise
  - Search: "CPA payroll tax withholding [state]"
  - Look for: Multi-state experience, ADP/Gusto integrations
  - Estimated cost: $500-1K per consultation
  
- [ ] **Email template** (send today):
  ```
  Subject: Payroll Tax Logic Review Needed (30 min call)
  
  Hi [CPA Name],
  
  We're launching HRMS for small field service companies (30-150 employees).
  
  Need: 30-min review of our federal + CA/TX/NY tax calculation logic
  Scope: W2 withholding, FICA, state income tax, unemployment
  
  Can you fit a call tomorrow or Wednesday?
  
  Thanks,
  [Your Name]
  ```

- [ ] **Schedule call**: Target Mon-Tue (May 13-14)
  
- [ ] **Prepare for call**:
  - [ ] Pull financial_analyst_v2.py (tax calculation logic)
  - [ ] Document: tax formulas used
  - [ ] Ask: "Is this right for CA/TX/NY?"
  - [ ] Get: Sign-off or corrections needed

### Success Criteria
- ✅ CPA scheduled for Mon-Tue
- ✅ Tax logic reviewed
- ✅ Sign-off documented (email or call notes)

---

## BLOCKER 2: Product-Market Fit Validation ✅ IN PROGRESS

### What We Need
- 4 discovery calls (Mon-Thu)
- 3-5 pain points from each
- Pricing feedback ($199/mo tier validation)
- Feature prioritization

### Target Customers
1. **Call 1 (Mon 5/13 or 5/14)**: Construction, 50 employees
   - Pain: Field crew scheduling, GPS tracking, payroll accuracy
   - Tier feedback: $199/mo for 50 people = $4/person/mo?

2. **Call 2 (Tue 5/14 or 5/15)**: Logistics/Delivery, 30 employees
   - Pain: Multi-state employees, independent contractor complexity
   - Tier feedback: Does $199 feel right or too cheap?

3. **Call 3 (Wed 5/15)**: Field Services (HVAC/Plumbing), 80 employees
   - Pain: Subcontractor management, project-based pay
   - Tier feedback: Would they upgrade to $499 for more features?

4. **Call 4 (Thu 5/16)**: Construction, 100+ employees
   - Pain: Union requirements, prevailing wage tracking
   - Tier feedback: Enterprise needs? $999 tier?

### Discovery Call Script (15 min)

```
Opening (1 min):
"Hi [Name], thanks for jumping on. We're launching HRMS for field service companies. 
Quick questions about your payroll process?"

Section 1: Current Pain (5 min):
- "How many people on payroll?" → [count]
- "What's your biggest payroll headache right now?" → [pain]
- "How do you handle [multi-state/contractors/scheduling] today?" → [solution]
- "How much time does payroll take per month?" → [hours]

Section 2: Our Solution (5 min):
"We built HRMS for exactly this. $199/mo for unlimited employees, handles multi-state, 
tracks GPS, integrates with Stripe."
- "Does that sound useful?" → [yes/no/maybe]
- "Would you pay $199/mo for this?" → [yes/no/price point]
- "What one feature would make you switch today?" → [priority]

Closing (2 min):
"We're looking for early customers. Interested in a 2-week free trial?" → [Yes = beta lead]
"Thanks. I'll send you the trial link."
```

### Success Criteria
- ✅ All 4 calls scheduled (Mon-Thu)
- ✅ Call notes documented (pain points + tier feedback)
- ✅ 2+ customers interested in trial
- ✅ Pricing validated ($199 tier confidence)

---

## BLOCKER 3: Sales Script + 3-Call Sales Process ✅ TODO

### What We Need
- 3-call sales process (discovery → demo → close)
- Sales script with objections
- Trial structure documentation
- Email sequence for trial-to-paid

### Sales Process Design

**Call 1: Discovery (15 min)**
- Goal: Understand pain + fit
- Script: Use discovery call script above (from Blocker 2)
- Success: They want to see the product

**Call 2: Demo (30 min)**
- Goal: Show how we solve their #1 pain
- Prep: Record 2-min demo video OR live screen share
- Demo flow:
  1. Login (setup screen)
  2. Add employees (bulk import)
  3. Run payroll (show one paycheck calculation)
  4. Export pay stubs (PDF generation)
- Success: They're ready to try

**Call 3: Close (15 min)**
- Goal: Convert trial → paid
- Trigger: Day 10 of trial (if they're engaged)
- Message: "You've run 2 payrolls. Ready to go live?"
- Offer: $199/mo with 2-year discount ($150/mo if annual)
- Success: Credit card entered

### Objection Handling

| Objection | Response |
|-----------|----------|
| "We use ADP already" | "No switching cost. Trial is free. If you like us, you can migrate when the time is right." |
| "What about multi-state?" | "CA, TX, NY, all 50 states handled. Plus international employees." |
| "$199 is expensive" | "That's $4/employee/mo for 50 people. ADP is $6-8. We're cheaper AND easier." |
| "What about compliance?" | "[CPA name] reviewed our logic. We handle federal + state withholding." |
| "I need to see payroll data" | "Trial gives you full access. Run a real payroll with your actual employee count." |

### Trial Structure
- Duration: 14 days free
- No credit card required (to start)
- Credit card required (to go live after trial)
- Full feature access (no limitations)
- Bonus: First month 50% off ($99.50) if you sign up during trial

### Trial-to-Paid Email Sequence

**Day 1 (Trial Start)**
```
Subject: Your HRMS trial is live — add your first employees

Hi [Name],

Welcome! Here's how to get started in 5 minutes:
1. Login: [link]
2. Add employees (use CSV import or manual)
3. Run your first payroll (we'll calculate everything)
4. Download pay stubs (PDF ready to distribute)

Need help? Reply to this email. We're here.

— HRMS Team
```

**Day 5 (Mid-Trial Check-in)**
```
Subject: How's the trial going?

Hi [Name],

Just checking in. Have questions? Common issues:
- Multi-state employees → See docs [link]
- Independent contractors → Tutorial [link]
- Stripe integration → Step-by-step [link]

Want a quick call to walk through anything? Reply with times.

— HRMS Team
```

**Day 10 (Ready to Convert)**
```
Subject: You've run 2 payrolls. Ready to go live?

Hi [Name],

Looking at your trial: You've processed 2 payrolls, paid 47 employees, everything passed compliance.

Time to move from trial to production?

Sign up now: [link]
- $199/mo, billed monthly
- First month 50% off if you sign up this week
- Cancel anytime

Questions? We're here.

— HRMS Team
```

**Day 14 (Trial Expires)**
```
Subject: Trial ends tomorrow — here's what you're missing

Hi [Name],

Your 14-day trial expires tomorrow. 

You've seen:
✅ Multi-state payroll handling
✅ Automatic tax calculations
✅ Unlimited pay stubs
✅ Stripe integration

Ready to go live? $199/mo (first month $99.50).

[CTA Button: Go Live Now]

Questions? Call us.

— HRMS Team
```

### Success Criteria
- ✅ 3-call process documented (discovery/demo/close)
- ✅ Sales script written (with objection handling)
- ✅ Trial structure defined (14 days, no CC upfront, CC for live)
- ✅ Email sequence drafted (5 emails, days 1/5/10/14/expired)

---

## BLOCKER 4: Billing Rules ✅ TODO

### Subscription Tiers

| Tier | Price | Employees | Features |
|------|-------|-----------|----------|
| **Starter** | $199/mo | Unlimited | Multi-state, basic integrations |
| **Professional** | $499/mo | Unlimited | ↑ + API access, advanced reporting |
| **Enterprise** | $999/mo | Unlimited | ↑ + dedicated support, custom integrations |

### Trial Rules
- Duration: 14 days
- Cost: Free
- Credit card: NOT required to start
- Features: Full access (same as Starter)
- End behavior: Auto-expires, no charge if no CC provided

### Signup Flow
1. Email + password → Confirm email
2. Company name + employee count
3. Add first employee (optional)
4. Trial starts (14 days)
5. Day 10: "Ready to subscribe?" prompt
6. CC entry (only when subscribing)
7. Billing date: Charge on signup day, then monthly anniversary

### Upgrade/Downgrade Rules
- Mid-cycle changes: Prorate (daily rate)
- Example: Upgrade from Starter ($199) to Professional ($499) on day 15 of 30:
  - Starter cost for 15 days: $199 × (15/30) = $99.50
  - Professional cost for 15 days: $499 × (15/30) = $249.50
  - Charge: $249.50 - $99.50 = $150 (credit card)
  - Next billing: 15 days later, full $499

### Cancellation Rules
- Effective: End of current billing period
- No refunds: We won't prorate cancellations mid-cycle
- Surveyー: "Why did you cancel?" → Feedback
- Off-board: Day 30 after cancellation, data export available for 30 days

### Stripe Integration Checklist
- [ ] Create Stripe account (if not exists)
- [ ] Create 3 products in Stripe (Starter, Professional, Enterprise)
- [ ] Create 3 prices (recurring, monthly, USD)
- [ ] Create subscription webhook: `customer.subscription.created`, `customer.subscription.updated`, `customer.subscription.deleted`
- [ ] Setup retry rules: 4 retries over 15 days (decline recovery)
- [ ] Configure failed payment emails
- [ ] Test: Create subscription in test mode
- [ ] Deploy: Activate in production

### Code Implementation (Supabase)

```sql
-- Billing table structure
CREATE TABLE subscriptions (
  id UUID PRIMARY KEY,
  customer_id UUID REFERENCES customers(id),
  stripe_subscription_id TEXT UNIQUE,
  tier TEXT CHECK (tier IN ('starter', 'professional', 'enterprise')),
  status TEXT CHECK (status IN ('active', 'past_due', 'canceled', 'paused')),
  current_period_start TIMESTAMPTZ,
  current_period_end TIMESTAMPTZ,
  cancel_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Billing events (for audit trail)
CREATE TABLE billing_events (
  id UUID PRIMARY KEY,
  customer_id UUID REFERENCES customers(id),
  event_type TEXT CHECK (event_type IN ('trial_start', 'subscribed', 'upgraded', 'downgraded', 'canceled')),
  old_tier TEXT,
  new_tier TEXT,
  amount NUMERIC(10,2),
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Success Criteria
- ✅ Tiers defined ($199/$499/$999)
- ✅ Trial rules documented (14 days, no CC upfront, CC for paid)
- ✅ Upgrade/downgrade logic documented (prorating rules)
- ✅ Cancellation flow defined (survey + 30-day data export)
- ✅ Stripe integration checklist created
- ✅ SQL schema for subscriptions + billing_events

---

## TIMELINE

**Today (May 13, Tue)**
- [ ] Blocker 1: Email CPA + schedule call
- [ ] Blocker 2: Schedule all 4 discovery calls
- [ ] Blocker 3: Write sales script + 3-call process
- [ ] Blocker 4: Document billing rules

**May 14 (Wed)**
- [ ] Blocker 1: Attend CPA call + get sign-off
- [ ] Blocker 2: Call 1 (Construction, 50 people)
- [ ] Blocker 3: Record demo video (2 min)

**May 15 (Thu)**
- [ ] Blocker 2: Calls 2 & 3 (Logistics, Field Services)
- [ ] Blocker 4: Create Stripe products in test mode

**May 16 (Fri)**
- [ ] Blocker 2: Call 4 (Construction 100+)
- [ ] All blockers: Consolidate findings + mark COMPLETE

**May 17+ (Ready for Task 9)**
- ✅ Financial Analyst code starts

---

## GO / NO-GO Decision

**GO**: All 4 blockers must show ✅ checkmarks above before Task 9 starts.  
**NO-GO**: Any blocker missing = HALT, resolve first, then code.

Current status: IN EXECUTION (Tue May 13 start)
