# Revenue Blocker Audit: What's Blocking $1K/Month

**Status:** $0/month right now  
**Target:** $1K/month in 1 week  
**Blocker Level:** CRITICAL (5 major blockers)

---

## THE 5 REVENUE BLOCKERS (In Order of Impact)

### 🔴 BLOCKER #1: No Lead Capture Workflow
**Impact: 100% of revenue blocked**

**What's Missing:**
- Lead form on venture websites
- Form submission → Supabase insertion
- Slack notification to sales team

**To Fix (3.5 hours):**
1. Add `<LeadForm />` to vex-hero-site (1h)
   - Fields: company, job_title, budget, email, phone
   - onSubmit: POST to /api/leads

2. Build `/api/leads` endpoint (1h)
   - Insert into Supabase.lead_intake
   - Slack notify: "New {venture} lead: {company}"

3. Create Supabase table `lead_intake` (30min)
   - Columns: venture_id, company, job_title, budget, email, phone, status, created_at
   - Status enum: ['new', 'contacted', 'qualified', 'customer']

**Value Unlocked:** Can capture prospect info

---

### 🔴 BLOCKER #2: No Payment Processing  
**Impact: 100% of cash flow blocked**

**What's Missing:**
- Stripe webhook that processes payments
- Updates venture MRR
- Sends invoice

**To Fix (4.5 hours):**
1. Wire Stripe webhook (2h)
   - Listen: payment_intent.succeeded
   - Action: INSERT Supabase.payments
   - Update: ventures.mrr += amount
   - Email: Send invoice

2. Build `/api/pay` endpoint (1h)
   - Create Stripe PaymentIntent
   - Return clientSecret for checkout

3. Create Supabase tables (1.5h)
   - `payments`: id, venture_id, customer_id, amount, status, created_at, paid_at
   - `customers`: id, email, company, venture_id, last_payment_at

**Value Unlocked:** Customers can pay, you get cash

---

### 🔴 BLOCKER #3: No Revenue Dashboard
**Impact: 80% visibility loss**

**What's Missing:**
- Hermes tab showing MRR per venture
- Real-time customer count
- Revenue this month

**To Fix (4.5 hours):**
1. Add "Venture Performance" tab to Hermes (2h)
   - Display: venture_id, customers, MRR, growth%, runway
   - Sort by MRR descending
   - Chart: month-over-month revenue

2. Add "Deal Intake" tab (1.5h)
   - Show leads by status (new/contacted/qualified/customer)
   - Actions: mark as "Contacted", "Qualified", "Customer"

3. Add "Revenue Summary" card (1h)
   - Total MRR this month
   - Revenue this week
   - Top venture by MRR

**Value Unlocked:** See all revenue in real-time

---

### 🔴 BLOCKER #4: No Customer Relationship Database
**Impact: 60% operational loss**

**What's Missing:**
- Customer records linked to ventures
- Payment history per customer
- Churn tracking

**To Fix (3 hours):**
1. Create Supabase table `customers` (30min)
   - Fields: email, company, phone, venture_id, status, last_payment_at

2. Add "Customers" tab to Hermes (1.5h)
   - Show all customers by venture
   - Actions: mark as "Churned", "Send reminder"

3. Add customer detail modal (1h)
   - Show payment history, invoices, contact info

**Value Unlocked:** Manage and retain customers

---

### 🔴 BLOCKER #5: No Operational Automation
**Impact: 50% of revenue lost to manual work**

**What's Missing:**
- Auto-send invoice on payment
- Auto-update venture metrics
- Auto-notify sales team on lead

**To Fix (3 hours):**
1. Zapier: Payment → Invoice Email (1h)
   - Trigger: payment.status = 'succeeded'
   - Send invoice via Resend

2. Zapier: Lead → Slack (30min)
   - Trigger: lead.status = 'new'
   - Post to #sales-leads

3. Zapier: Payment → Update MRR (30min)
   - Update ventures.mrr on payment received

4. n8n: Qualified Lead → Contract (1h)
   - Generate PDF, send via email, notify sales

**Value Unlocked:** Zero manual work

---

## SUMMARY: 18.5 Hours to Revenue

| Task | Hours | Status | Impact |
|------|-------|--------|--------|
| Lead Capture Workflow | 3.5h | NOT BUILT | 100% |
| Payment Processing | 4.5h | 20% DONE | 100% |
| Revenue Dashboard | 4.5h | NOT BUILT | 80% |
| Customer Database | 3h | NOT BUILT | 60% |
| Automation | 3h | 20% DONE | 50% |
| **TOTAL** | **18.5h** | **20% BUILT** | |

---

## WEEK 1 EXECUTION PLAN

**Monday-Tuesday (8 hours):**
- ✓ Add lead form to vex-hero-site
- ✓ Wire Stripe webhook
- ✓ Build /api/leads and /api/pay endpoints
- ✓ Create lead_intake and payments tables
→ **Commit:** Can capture leads and process payments

**Wednesday (4.5 hours):**
- ✓ Build Venture Performance tab
- ✓ Build Deal Intake tab  
- ✓ Build Revenue Summary card
→ **Commit:** Real-time revenue visibility

**Thursday (3 hours):**
- ✓ Create customers table
- ✓ Build Customers tab in Hermes
- ✓ Add customer detail modal
→ **Commit:** Customer relationship management

**Friday (3 hours):**
- ✓ Wire Zapier automations (payment→invoice, lead→slack, payment→mrr)
- ✓ Build n8n workflow (qualified lead→contract)
→ **Commit:** Zero manual work on happy path

---

## WHAT YOU CAN DO TODAY

**Pick ONE (to validate the approach):**

**Option A: Task 1.1 + 1.2 only (3.5 hours)**
- Add lead form to /staffing page
- Build /api/leads endpoint
- Test: submit fake lead, see it in Supabase, get Slack notif
- **Validates:** Lead capture works

**Option B: Task 2.1 + 2.2 only (3 hours)**
- Wire Stripe webhook
- Build /api/pay endpoint
- Test: make $1 payment, see it update ventures.mrr
- **Validates:** Payment processing works

**Option C: Task 3.1 only (2 hours)**
- Add "Venture Performance" tab to Hermes
- Show hardcoded ventures with sample MRR data
- Test: can you see revenue in dashboard?
- **Validates:** Dashboard works

**Option D: All 18.5 hours (complete implementation)**
- Build everything
- Launch by Friday
- Revenue starts Monday

---

## SUCCESS CRITERIA BY 2026-07-28

✅ Customer visits STA-001 page  
✅ Fills lead form (company, budget)  
✅ Form → Supabase  
✅ Slack notifies sales  
✅ Sales marks "Qualified"  
✅ Contract auto-generated  
✅ Customer gets payment link  
✅ Stripe processes payment  
✅ Invoice auto-emailed  
✅ Hermes updates: "STA-001: 1 customer, $500 MRR"

**Revenue Generated:** $500-$1,000/month

---

## WHAT YOU NEED RIGHT NOW

- [ ] Stripe API keys (you have)
- [ ] Resend API key (for emails)
- [ ] Zapier account (free tier OK)
- [ ] n8n instance (running on Mac Studio)
- [ ] Slack webhook URL (#sales-leads channel)
- [ ] 18.5 hours of developer time

---

## YOUR CALL

**What do you want to do?**

A) I build all 18.5 hours (Wed-Fri, launch Monday)  
B) I build Option A: Lead capture only (validate first)  
C) I build Option B: Payment processing only (validate payment)  
D) I build Option D: Everything (start now)

**Pick one. Let's move.** 🚀
