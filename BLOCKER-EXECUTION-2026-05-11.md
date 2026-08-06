---
name: BLOCKER-EXECUTION-2026-05-11
title: Blocker Execution Plan — May 11-13, 2026
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Blocker Execution Plan — May 11-13, 2026

## 🎯 Parallel Execution (Run All 4 in Parallel)

### Blocker 1: CPA Review (1-2 hours)
**Action**: Call/email CPA today for 2-hour consultation ($500-1K)

**Topics to Cover**:
1. Federal withholding: 2026 IRS tax tables (single/married/HOH)
2. State withholding: CA, TX, NY only (V1.0 scope)
3. FICA: 6.2% Social Security + 1.45% Medicare (fixed, no changes)
4. FUTA: 6.0% federal unemployment (standard, with SUTA credits state-specific)
5. State unemployment: CA (4.6% range), TX (0.42-3.96%), NY (3.9% range) — varies by new hire vs established
6. Out of scope V1.0: Local taxes, 1099 contractors, international, benefits/deductions, quarterly filing
7. Key question: "What's minimum compliance we must have to launch?"

**Deliverable**: Email from CPA confirming tax logic is sound, scope is realistic

**Owner**: Ace  
**Timeline**: Complete by Monday EOD (May 12)

---

### Blocker 2: Discovery Calls (4 calls, 1/day Mon-Thu)
**Action**: Email leads TODAY, schedule Mon-Thu

**OpenVolo Query** (run this Monday):
```
Industry: Construction OR Field Services OR Logistics
State: CA OR TX OR NY
Employee count: 20-150
Recent hires: Yes (hiring growth signal)
Contact info: Email + Phone available
Limit: Top 20
Sort by: Recently added (last 7 days)
```

**Discovery Call Script** (15 minutes):
```
OPENER: "Hi [Name], I'm building payroll software for construction/logistics crews 
getting too big for Excel/ADP. We're talking to Finance Directors like you to understand pain. 
Do you have 15 min to give us your two cents?"

IF YES:
1. "Walk me through how you handle payroll right now"
   → Listen: Manual? Software? Time spent?

2. "What's the biggest headache?"
   → Listen for: Tax complexity, multi-state, time, errors, costs

3. "We're thinking $199-$499/month depending on size. Does that fit your budget?"
   → Listen for: Price sensitivity

4. "Would you try a free 14-day trial of a payroll tool built for your size company?"
   → Listen for: Willingness to pilot

CLOSE: "Thanks [Name]. If this launches in June, can I send you the link?"
→ If YES: Add to trial list. If NO: Still get email link to share with peers.
```

**Leads to Call** (pull from OpenVolo Monday):
- Construction company (50 emp)
- Logistics company (30 emp)
- Field services company (80 emp)
- Construction company (100+ emp)

**Deliverable**: 4 call notes documenting pain points, pricing sensitivity, must-have features

**Owner**: Ace  
**Timeline**: Mon May 12 → Thu May 15 (1 call/day)

---

### Blocker 3: Sales Script (Draft + Polish)
**Action**: Draft today, finalize after discovery calls

**3-Call Sales Process**:

**Call 1: Discovery (15 min)**
- Opener: "We're solving [specific pain] for construction/logistics companies. Do you handle payroll for [Company]?"
- Questions: pain, current solution, switching cost, timeline
- Close: "If we had a product that solved this and cost $[X]/mo, would you trial it?"

**Call 2: Demo (30 min)**
- Show 3 key screens: Employee directory → Payroll run → Pay stub
- Demo scenario: "Let's add your 5 employees, calculate payroll, see the taxes auto-calculated"
- Highlight: "This takes 1 hour instead of 8, and compliance reports auto-generate"
- Close: "Want to start a free 14-day trial? All you do is add one employee to see it work."

**Call 3: Close (15 min)**
- If said YES to trial: "Great, here's the link. You'll get an email with credentials. Start by adding your first employee."
- If hesitant: "No pressure. I'm here if you have questions. When can I follow up?" (schedule call 4)
- If NO: "Totally understand. If you change your mind or know a peer, send them my way."

**Objection Handling**:
- "We use Gusto" → "Gusto is great, but they're $300/mo more expensive and built for offices. We're built for field crews, faster to set up, and half the cost."
- "Payroll is critical" → "Totally agree, which is why we had a CPA review our tax logic and we auto-calculate everything. We're built for accuracy."
- "Can't switch mid-cycle" → "No problem. Start next pay period. We'll help migrate your data. You'll be up and running in 1 hour."
- "Need to think about it" → "Smart. Happy to send you a [one-pager/demo video/pricing sheet]. When can I check in?"

**Deliverable**: Sales script doc (polish after first 2 calls)

**Owner**: Ace  
**Timeline**: Draft today (May 11), finalize Thu (May 15)

---

### Blocker 4: Billing Rules (Document Today)
**Action**: Write rules doc, test logic with Stripe sandbox

**Tier Pricing**:
- Starter: 1-10 employees → $199/month
- Professional: 11-50 employees → $499/month
- Enterprise: 51+ employees → $999/month

**Trial Flow**:
1. Customer signs up: Email + password only (no CC)
2. Day 1: Send "Welcome, add your first employee" email
3. Day 13: Send "Trial ends in 1 day, add payment method" email
4. Day 14, 11:59pm UTC: If no payment → disable account
5. Day 15: Send "Reactivate anytime, your data is safe for 30 days" email

**Billing Rules**:
- Charge on same day each month
- If upgrade mid-month (add 11th employee): Prorate charge
  - Example: Upgrade on May 20 (10 days left in May). Difference = ($499 - $199) / 30 × 10 = $100. Charge $100 on May 20, then $499 on June 1.
- Downgrade effective next billing cycle (no refunds)
- Cancellation: Customer marks "cancel", survey why, confirm data safe for 30 days, send final invoice

**Stripe Setup**:
- Create 3 products (Starter, Professional, Enterprise)
- Create 3 prices (monthly recurring)
- Create billing portal for customers to manage payment method
- Test trial → paid flow in sandbox

**Deliverable**: Billing rules doc + Stripe test results

**Owner**: Ace (or dev partner if they do Stripe integration)  
**Timeline**: Complete by Mon May 12

---

## 🚀 Parallel Timeline

| Day | Blocker 1 | Blocker 2 | Blocker 3 | Blocker 4 | Code Start |
|-----|-----------|-----------|-----------|-----------|-----------|
| Fri 5/11 | Email CPA | Draft script | Draft script | Draft rules | — |
| Mon 5/12 | CPA call | Pull leads, Call 1 | Review script | Review rules | Fork Mission Control |
| Tue 5/13 | ✅ Done | Call 2 | Polish script | Test Stripe | Schema design |
| Wed 5/14 | — | Call 3 | Close script | ✅ Done | Database migration |
| Thu 5/15 | — | Call 4 | ✅ Done | — | Employee CRUD |
| Fri 5/16 | — | ✅ Compile findings | — | — | Payroll calculation |

**Result**: All blockers done by Thu 5/15, code launches Fri 5/16-Thu 5/23 (Week 2), first beta customer trial starts Fri 5/23.

---

## 📋 What Needs Doing Right Now

1. **Email CPA** (today): Request 2-hour consultation, mention tax topics above
2. **Fork Mission Control** (Monday): Copy to `hrms-saas-mvp`, update README
3. **Create Calendly** (Monday): 30-min discovery call slots, post link in Slack
4. **Pull OpenVolo data** (Monday): Run query above, export to CSV
5. **Send first batch of emails** (Mon-Tue): "Hi [Name], we're building payroll software for field crews. Quick call about your payroll process?"

**Everything else flows from these 5 actions.**
