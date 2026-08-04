# Partner Ecosystem OS Build — Timeline & Tracker
**Started:** 2026-08-04  
**Target Complete:** 2026-08-07 (3 days parallel)  
**Status:** Planning → In Progress

---

## Timeline (Parallel Tracks)

```
DAY 1 (Aug 4)      DAY 2 (Aug 5)      DAY 3 (Aug 6)      DAY 4 (Aug 7)
├─ TRACK A         ├─ TRACK A ✅      ├─ TRACK B         ├─ TRACK D
├─ TRACK C         ├─ TRACK C         ├─ TRACK D         ├─ DEMO READY
└─ PREP            └─ PREP DONE       └─ INTEGRATION     └─ SHIP
```

---

## TRACK A: Supabase Schema + Functions
**Blocker for:** B, D  
**Est. Time:** 4 hours  
**Start:** Aug 4 morning  
**Target:** Aug 4 EOD  

### Checklist

- [ ] A1: Create `partners` table
  - [ ] id (UUID primary key)
  - [ ] name (text)
  - [ ] type (enum: reseller | service_provider | builder | referral)
  - [ ] tier (enum: affiliate | partner | strategic)
  - [ ] status (enum: pending | active | inactive)
  - [ ] capabilities (JSON array: ['dispatch', 'staffing', 'construction', 'ai'])
  - [ ] coverage_area (text: geography)
  - [ ] partner_score (float: 0-100)
  - [ ] commission_pct (float: default 20)
  - [ ] created_at, updated_at
  - [ ] RLS policy: Partners can view/edit own row

- [ ] A2: Create `deal_registration` table
  - [ ] id (UUID primary key)
  - [ ] partner_id (FK → partners.id)
  - [ ] customer_name (text)
  - [ ] customer_email (text)
  - [ ] industry (text)
  - [ ] opportunity_value (decimal)
  - [ ] products_needed (JSON array)
  - [ ] status (enum: registered | won | lost)
  - [ ] notes (text)
  - [ ] created_at, updated_at
  - [ ] RLS policy: Partners can view/edit own deals

- [ ] A3: Create `commissions` table
  - [ ] id (UUID primary key)
  - [ ] partner_id (FK → partners.id)
  - [ ] deal_id (FK → deal_registration.id)
  - [ ] revenue (decimal)
  - [ ] commission_pct (float)
  - [ ] commission_amount (decimal, calculated)
  - [ ] status (enum: calculated | pending_approval | paid)
  - [ ] payout_date (date nullable)
  - [ ] created_at
  - [ ] RLS policy: Partners can view own commissions (read-only)

- [ ] A4: Create `partner_certifications` table
  - [ ] id (UUID primary key)
  - [ ] partner_id (FK → partners.id)
  - [ ] certification (text: 'dispatch-ops' | 'staffing-aes' | 'construction-safety')
  - [ ] score (float: 0-100)
  - [ ] expires_at (date)
  - [ ] created_at
  - [ ] RLS policy: Partners can view own certifications

- [ ] A5: Create SQL functions
  - [ ] `calculate_commission(deal_id)` → returns commission_amount
  - [ ] `get_partner_score(partner_id)` → aggregates from deals + certs
  - [ ] `register_deal(partner_id, customer_name, value, products)` → creates row
  - [ ] `mark_deal_won(deal_id)` → creates commission + updates score
  - [ ] `get_partner_opportunities(partner_id)` → lists open deals

- [ ] A6: Enhance `customers` table
  - [ ] license_tier (enum: starter | professional | enterprise)
  - [ ] licenses (JSON array: SKUs)
  - [ ] partner_id (nullable FK)
  - [ ] referred_by (nullable text)

- [ ] A7: Create indexes for performance
  - [ ] deal_registration(partner_id, status)
  - [ ] commissions(partner_id, status)
  - [ ] partners(tier, status)

---

## TRACK B: vex UI Components
**Depends on:** A (schema ready)  
**Est. Time:** 8 hours  
**Start:** Aug 4 afternoon  
**Target:** Aug 6 afternoon  

### Checklist

- [ ] B1: Partner Registration Form (`/vex/pages/partner-onboard.tsx`)
  - [ ] Form: name, email, type, capabilities, coverage_area, phone
  - [ ] Validation & submit to API
  - [ ] Success message: "Pending approval"

- [ ] B2: Partner Dashboard (`/vex/pages/partner/dashboard.tsx`)
  - [ ] Stats: tier, commission rate, partner score
  - [ ] Deals summary (registered | won | lost counts)
  - [ ] Commission earnings (month/YTD)
  - [ ] Quick links to deal registration & opportunities

- [ ] B3: Deal Registration Form (`/vex/pages/partner/register-deal.tsx`)
  - [ ] Form: customer_name, email, industry, opportunity_value, products
  - [ ] Validation & submit
  - [ ] Success & redirect to tracker

- [ ] B4: Deal Tracker (`/vex/pages/partner/deals.tsx`)
  - [ ] Table: deal_id, customer, value, products, status, dates
  - [ ] Filters: status, sort: value/date
  - [ ] Detail view per deal (notes, email, timeline)

- [ ] B5: Commission Tracker (`/vex/pages/partner/commissions.tsx`)
  - [ ] Table: deal_id, revenue, commission_pct, commission_amount, status
  - [ ] Charts: trend (3mo), earnings by deal
  - [ ] Summary: YTD commission, pending, paid

- [ ] B6: Partner Profile (`/vex/pages/partner/profile.tsx`)
  - [ ] Edit: name, coverage_area, capabilities
  - [ ] View: tier, score, certifications
  - [ ] Read-only: join date, referrals, total revenue

- [ ] B7: Feature Gating Middleware (`/vex/lib/feature-gate.ts`)
  - [ ] `canAccess(user, feature)` checks licenses
  - [ ] Features: dispatch, staffing, construction, ai, analytics
  - [ ] Applied to route guards

- [ ] B8: Dynamic Pricing Page (`/vex/pages/pricing.tsx`)
  - [ ] Fetch SKUs from Supabase
  - [ ] Show: Core + modules (Dispatch, Staffing, Construction, AI)
  - [ ] CTA: "Buy Now" → Stripe or contact

---

## TRACK C: Neo4j Capability Graph + Matching
**Depends on:** Nothing (parallel to A)  
**Est. Time:** 5 hours  
**Start:** Aug 4 morning  
**Target:** Aug 5 EOD  

### Checklist

- [ ] C1: Define Neo4j nodes
  - [ ] Partner {id, name, capabilities[], tier, score}
  - [ ] Capability {name, category}
  - [ ] Opportunity {id, industry, value, products_needed[]}
  - [ ] Region {name, state}

- [ ] C2: Define relationships
  - [ ] (Partner)-[:HAS_CAPABILITY]->(Capability)
  - [ ] (Partner)-[:OPERATES_IN]->(Region)
  - [ ] (Opportunity)-[:REQUIRES_CAPABILITY]->(Capability)
  - [ ] (Opportunity)-[:IN_REGION]->(Region)
  - [ ] (Partner)-[:COMPLETED_DEAL]->(Opportunity)
  - [ ] (Partner)-[:CERTIFIED_IN]->(Capability)

- [ ] C3: Seed initial data (vex-api seed script)
  - [ ] Create capability nodes (dispatch, staffing, construction, ai, healthcare, compliance)
  - [ ] Create region nodes (Arizona, Carolina, Texas)
  - [ ] Create 5 sample partners with capability mixes

- [ ] C4: Build matchingEngine (`vex-api/src/matching/engine.ts`)
  - [ ] `findBestPartners(opportunity)` Neo4j query
  - [ ] Logic: find partners with matching capabilities + region
  - [ ] Rank by matching_caps DESC, partner_score DESC
  - [ ] Return top 5 with match scores

- [ ] C5: Expose `/api/vex/matching/find-partners` endpoint
  - [ ] POST { opportunity_id }
  - [ ] Returns: [{partner_id, name, score, reason}]

- [ ] C6: Implement partner scoring
  - [ ] Base: # of deals won
  - [ ] Boost: certifications (+5 ea)
  - [ ] Boost: recent wins (+2 ea)
  - [ ] Penalty: lost deals (-1 ea)
  - [ ] Range: 0-100

- [ ] C7: Capability discovery endpoint (`/api/vex/capabilities/list`)
  - [ ] Returns all capabilities
  - [ ] Used by signup form + opportunity filter

---

## TRACK D: Integration + Testing + Feature Gating
**Depends on:** A complete, B+C mostly done  
**Est. Time:** 4 hours  
**Start:** Aug 6 afternoon  
**Target:** Aug 7 EOD  

### Checklist

- [ ] D1: Wire feature gating
  - [ ] Apply to routes (dispatch, staffing, construction)
  - [ ] Test: customer with dispatch license sees UI
  - [ ] Test: customer without license sees "Upgrade" prompt

- [ ] D2: License table integration
  - [ ] GET /api/vex/licenses/list (customer's active licenses)
  - [ ] Show expiry dates + renewal
  - [ ] Link to upgrade

- [ ] D3: Dynamic pricing
  - [ ] Pull SKUs from Supabase
  - [ ] Show tiers: Starter ($499) | Pro ($999) | Enterprise (custom)
  - [ ] Show modules: +Dispatch | +Staffing | +Construction | +AI
  - [ ] CTA: "Upgrade Now"

- [ ] D4: Partner registration → Supabase
  - [ ] Form validation
  - [ ] Create partners row (status='pending')
  - [ ] Send admin notification
  - [ ] Partner gets dashboard link

- [ ] D5: Deal → Commission flow
  - [ ] Register deal → partners.deal_registration row
  - [ ] Mark "won" → commissions row created
  - [ ] Commission = revenue × commission_pct
  - [ ] Partner sees in dashboard

- [ ] D6: End-to-end scenario test
  - [ ] Partner registers $100k opportunity
  - [ ] Status: registered → won
  - [ ] Commission $20k (20%) created
  - [ ] Partner dashboard shows earnings
  - [ ] Customer buys "Professional + Dispatch"
  - [ ] Dispatch UI unlocks

- [ ] D7: Admin panel (basic)
  - [ ] View all partners
  - [ ] Approve/reject pending partners
  - [ ] View all deals
  - [ ] Mark deals won/lost
  - [ ] View commission payouts

- [ ] D8: Security review
  - [ ] RLS policies enforced
  - [ ] API requires auth + partner_id match
  - [ ] Parameterized queries (no SQL injection)
  - [ ] Webhook handling (if Stripe)

- [ ] D9: Documentation
  - [ ] Partner API quickstart
  - [ ] Admin guide (approve, view commissions)
  - [ ] Schema ER diagrams

- [ ] D10: Smoke tests
  - [ ] Partner registration success
  - [ ] Deal registration success
  - [ ] Commission calculation correct
  - [ ] Feature gating works
  - [ ] Neo4j matching returns results

---

## Status Summary

| Track | Checklist Items | Status | Est. Hours |
|-------|-----------------|--------|-----------|
| **A** | A1-A7 (7 items) | ⏳ Pending | 4h |
| **B** | B1-B8 (8 items) | ⏳ Pending | 8h |
| **C** | C1-C7 (7 items) | ⏳ Pending | 5h |
| **D** | D1-D10 (10 items) | ⏳ Pending | 4h |
| **TOTAL** | 32 checklist items | 0% | ~21h sequential / ~10h parallel |

---

## Critical Path

```
Aug 4 morning:
  ├─ Start TRACK A (schema) — BLOCKS B+D
  └─ Start TRACK C (Neo4j) — INDEPENDENT

Aug 4 afternoon:
  ├─ A1-A4 done?
  └─ Start TRACK B (UI) if A ready

Aug 5:
  ├─ Finish C (Neo4j matching)
  └─ Continue B (UI)

Aug 6:
  ├─ Finish B (UI components)
  └─ Start D (integration)

Aug 7:
  ├─ Finish D (testing + go-live)
  └─ SHIP
```

**Parallelism saves:** ~6 hours vs sequential.

---

## Files to Create

**New:**
- `PARTNER-ECOSYSTEM-SCHEMA.sql` (Supabase migrations)
- `vex/pages/partner-onboard.tsx` (registration form)
- `vex/pages/partner/dashboard.tsx` (partner home)
- `vex/pages/partner/deals.tsx` (deal tracker)
- `vex/pages/partner/commissions.tsx` (earnings dashboard)
- `vex/pages/partner/profile.tsx` (partner profile edit)
- `vex-api/src/matching/engine.ts` (matching logic)

**Edit:**
- `vex-api/src/db.ts` (Neo4j connection)
- `vex/pages/pricing.tsx` (dynamic pricing)
- `vex/lib/middleware.ts` (feature gating)
- `vex/lib/feature-gate.ts` (NEW file)

---

## Success Criteria (Must Have)

- ✅ Partner can register
- ✅ Partner can register deal
- ✅ Deal → commission when won
- ✅ Partner dashboard shows earnings
- ✅ Customer sees active licenses
- ✅ Feature gating blocks unauthorized access
- ✅ Pricing page shows all SKUs
- ✅ Neo4j matching works
- ✅ Admin can manage partners + deals
- ✅ RLS isolation working

---

## Deployment

**Env:** Supabase staging (or local with Docker)  
**Testing:** Manual scenario test + Jest smoke tests  
**Go-live:** After all Track D passes  
**Monitor:** Commission accuracy, RLS, performance  

---

## Known Questions

- **Partner approval:** Manual or auto? → Default: **manual** (quick review, prevent spam)
- **Commission payout:** Monthly or per-deal? → Default: **per-deal** (real-time visibility)
- **Commission type:** % or fixed? → Default: **% per tier** (scalable)
- **Stripe integration:** Now or later? → Default: **later** (Supabase tracking first, Stripe payout v2)

---

## Linked Tasks

- Task #1: Parent (Partner Ecosystem OS — Full Stack Build)
- Task #2: Track A (Supabase Schema)
- Task #3-6: Subtasks for Track A
- Task #7: Track B (vex UI)
- Task #8: Track C (Neo4j)
- Task #9: Track D (Integration)

---

**Last Updated:** 2026-08-04 16:00 UTC  
**Next Review:** When Track A is 50% complete
