# ClickUp Deal Pipeline Setup

**Workspace ID:** 9013677375  
**Timeline:** Create May 10, 2026 (during Phase 1 setup)  
**Owner:** Worldwidebro AI Systems  

---

## Lists to Create (5 Total)

### LIST 1: Leads—E-Commerce Tier 1
**Purpose:** Prospects we're calling from E-Commerce sector  
**Status:** 📋 Create May 10 at 9:30am  

**Custom Fields:**
- **warmth_score** (Number, 1-10) — Contact quality/relationship strength
  - 1-3: Cold (no prior connection)
  - 4-6: Warm (indirect connection, social signal)
  - 7-10: Hot (direct network, explicit interest)
- **venture_matched** (Text) — Which ECOM venture they need (ECOM-001, ECOM-020, etc.)
- **last_contacted** (Date) — When agent last called
- **demo_scheduled** (Date) — If booked, when is the demo
- **outcome** (Single Select: "interested", "not_interested", "demo_booked", "callback_scheduled", "do_not_call")
- **call_duration** (Number) — How long the call lasted in seconds
- **notes** (Text) — Agent observations, objections raised, next steps

**Initial Tasks (Sample - will populate from contacts):**
- Contact 1: [Name], [Phone], Company: [Company Name], warmth_score: 5
- Contact 2: [Name], [Phone], Company: [Company Name], warmth_score: 6
- (Add 8 more to reach 10 test prospects for May 11)

---

### LIST 2: Leads—Technology Tier 1
**Purpose:** Prospects from Technology sector (deploys May 15)  
**Status:** 📋 Create May 10 at 9:30am (same structure as LIST 1)  

**Same custom fields as LIST 1**

**Initial Tasks:**
- Empty until May 15 (when Swift agent deploys)
- Will be populated with 20+ tech prospects

---

### LIST 3: Leads—Beauty & Wellness Tier 1
**Purpose:** Prospects from Beauty & Wellness sector (deploys May 15)  
**Status:** 📋 Create May 10 at 9:30am (same structure as LIST 1)

**Same custom fields as LIST 1**

**Initial Tasks:**
- Empty until May 15 (when Bella agent deploys)
- Will be populated with 15+ beauty prospects

---

### LIST 4: Negotiations—Active Deals
**Purpose:** Prospects who booked demos, now in follow-up/negotiation phase  
**Status:** 📋 Create May 10 at 9:30am  

**Custom Fields:**
- **prospect_name** (Text) — Full name
- **company** (Text) — Company name
- **venture** (Text) — Which venture they're buying (ECOM-001, TECH-015, etc.)
- **deal_value** (Currency, $) — Estimated monthly or annual contract value
- **stage** (Single Select: "demo_scheduled", "demo_completed", "proposal_sent", "negotiating", "ready_to_close", "closed_won")
- **close_date** (Date) — Target close date
- **next_action** (Text) — What happens next (send proposal, schedule follow-up, etc.)
- **decision_maker** (Text) — Who has authority to sign
- **blockers** (Text) — Any objections or concerns still pending
- **contact_phone** (Text)
- **contact_email** (Text)

**Auto-populated by:** Webhook when call outcome = "demo_booked"  
**Manual updates by:** You or your sales team as deals progress

**Initial Tasks:**
- Alexus Johnson (Beauty By Nature, BW-001, $2K/month, demo_scheduled 2026-05-15)

---

### LIST 5: Closed Deals—Revenue
**Purpose:** Won deals, revenue tracking, success stories  
**Status:** 📋 Create May 10 at 9:30am  

**Custom Fields:**
- **prospect_name** (Text)
- **company** (Text)
- **venture_sold** (Text) — Which product they bought
- **deal_value** (Currency, $) — Monthly or annual contract value
- **close_date** (Date) — When deal closed
- **agent_closed_by** (Single Select: "Echo", "Swift", "Bella", "Manual")
- **revenue_tier** (Single Select: "Tier 1 ($1-2K)", "Tier 2 ($2-5K)", "Tier 3 ($5-10K)", "Tier 4 ($10K+)")
- **customer_notes** (Text) — What they said about the product, fit, etc.
- **integration_status** (Single Select: "onboarded", "in_implementation", "live", "churned")
- **monthly_revenue** (Currency, $) — Track recurring revenue

**Auto-populated by:** Manual entry once deal is closed  
**Monthly revenue tracking:** Sum all monthly_revenue fields for Month 1, Month 2, etc.

**Initial Tasks:**
- (Empty until first deal closes, expected May 18-22)

---

## Status Workflow

### List 1-3: Leads
```
New Lead
  ↓ (Created from contact list or CSV import)
Called by Agent
  ↓ (Webhook updates outcome field)
If Demo Booked:
  → Move task to LIST 4 (Negotiations)
If Not Interested:
  → Mark outcome = "not_interested", leave in list
If Callback Requested:
  → Mark outcome = "callback_scheduled", set follow-up date
```

### List 4: Negotiations
```
Demo Scheduled
  ↓ (Agent booked via call)
Demo Completed
  ↓ (You or agent updates after demo)
Proposal Sent
  ↓ (Send contract/pricing)
Negotiating
  ↓ (Back-and-forth on terms)
Ready to Close
  ↓ (Just waiting for signature)
Closed Won
  → Move task to LIST 5 (Closed Deals)
```

### List 5: Closed Deals
```
Closed Won (final list, historical record)
  ↓ Monthly reconciliation
  → Sum revenue, calculate commission, update forecasts
```

---

## ClickUp Setup Instructions

1. **Create workspace or use existing (9013677375)**

2. **Create Lists** (May 10, 9:30am):
   - Open ClickUp → Space
   - Click "+ List"
   - Name: "Leads—E-Commerce Tier 1"
   - Repeat for all 5 lists

3. **Add Custom Fields** (May 10, 10:00am):
   - Open each list
   - Settings → Custom Fields
   - Add fields listed above (warmth_score, venture_matched, etc.)
   - Copy field IDs to .env file (for webhook automation)

4. **Configure Webhooks** (May 10, 1:30pm):
   - Use field IDs from step 3
   - Update `CLICKUP_LIST_ECOM`, `CLICKUP_LIST_TECH`, `CLICKUP_LIST_BEAUTY` in .env
   - Test: Make test call, verify task created in list

5. **Populate Initial Contacts** (May 11, 9:00am):
   - Import 10 E-Commerce prospects as tasks in LIST 1
   - Set warmth_score (5-7 for unknowns)
   - Set venture_matched (ECOM-001, ECOM-020, etc.)
   - Ready to call

---

## Revenue Tracking (Monthly)

At end of each month, run this query in ClickUp:

```
List 5: Closed Deals
Filter: close_date >= [Month Start] AND close_date <= [Month End]
Group By: revenue_tier
Sum: deal_value (total revenue)
Sum: monthly_revenue (recurring revenue forecast)
```

**Expected May 18-31 Results:**
- 1-2 deals closed
- $2K-$7K total revenue
- $2K-$7K monthly recurring revenue (MRR)

---

## Integration with Supabase

All tasks created in ClickUp are **also** logged to Supabase `ai_calls` table:
- When webhook fires (call complete)
- Creates task in ClickUp AND
- Inserts record in Supabase with outcome, warmth_score, transcript, agent_type

**Result:** Single source of truth splits into two systems:
- **ClickUp:** Sales team interface, deal pipeline tracking
- **Supabase:** Automation/analytics backend, RAG context for future calls

---

## Files Generated From This List Structure

**From LIST 1 + 2 + 3:**
- Weekly calling targets (20 calls/day × 5 days = 100 calls/week by Week 2)
- Demo booking rate tracking (target 15-20%)
- Warmth score distribution analysis

**From LIST 4:**
- Active negotiations pipeline (deals in progress)
- Close probability forecasting
- Revenue forecast

**From LIST 5:**
- Monthly revenue report
- Customer acquisition cost (CAC) = cost of calls / number of closed deals
- Lifetime value (LTV) = recurring revenue × months active

---

## Status: ✅ READY TO CREATE

All 5 lists are documented and ready to set up during Phase 1 deployment (May 10).

**Next file:** DEAL-SCRIPTS-BY-SECTOR.md (what agents say on calls)
