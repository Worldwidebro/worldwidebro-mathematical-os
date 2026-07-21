# CON-001 Infrastructure Blockers — Red Team Analysis

**Date:** 2026-07-16  
**Status:** Phase 2 PAUSED — 5 blockers must be resolved before Phase 2 planning can proceed  
**Timeline Impact:** Original 4-5 weeks → Realistic 8-10 weeks (including blocker resolution)

---

## Blocker #1: Supabase Schema — venture_leads Table

**Status:** ✅ FIXED (2026-07-16 14:35)

**Finding:**
- operating_system_schema.sql: NO venture_leads table
- CON-001 schema.sql: NO venture_leads table (uses contact_submissions instead)

**Resolution:**
- Migration created: `/Users/acebless/Documents/migrations/001_create_venture_leads_table.sql`
- Commit: `9ec52da` (2026-07-16)
- Fields: email, budget_min/max, timeline, complexity, source, lead_score, status
- RLS policies: Venture team access + agent write access
- Indexes: venture, status, source, lead_score, created_at

**Impact:** Loop 1 (Lead Intake) can now write captured leads to database

**Next Step:** Apply migration to CON-001 Supabase project via `supabase db push` or Vercel deploy pipeline

---

## Blocker #2: Stripe Account Status

**Status:** ⚠️ REQUIRES IMMEDIATE VERIFICATION

**Finding:**
- venture.json lists Stripe as "pending" (not activated)
- Code expects: `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET` environment variables in Vercel
- Cannot verify from CLI; requires manual Vercel dashboard check

**Required Actions:**
1. **Pull STRIPE_SECRET_KEY:**
   - Go to: https://dashboard.stripe.com/apikeys
   - Copy the Secret Key (live or test, depending on environment)
   - Add to Vercel: Settings → Environment Variables → `STRIPE_SECRET_KEY`

2. **Pull STRIPE_WEBHOOK_SECRET:**
   - Go to: https://dashboard.stripe.com/webhooks
   - Find webhook for your Vercel deployment URL (or create new one)
   - Copy the Signing Secret
   - Add to Vercel: Settings → Environment Variables → `STRIPE_WEBHOOK_SECRET`

3. **Test Connection:**
   - Run: `npm run dev` locally
   - Hit checkout endpoint: `POST /api/projects/[id]/checkout`
   - Verify Stripe session is created without errors

**Impact:** Loop 3 (Payment Processing) + project payment flow completely blocked without this

**Timeline:** 0.5 hours (manual step)

---

## Blocker #3: Procore API Integration

**Status:** ❌ UNKNOWN — Requires Research

**Finding:**
- No Procore code in CON-001 app
- No OAuth flow or API key storage configured
- Code does not reference Procore anywhere

**Required Actions:**
1. **Verify API Exists:**
   - Research: Procore Developer Portal
   - Check: Is there a REST API? (vs. UI-only)
   - Document: OAuth 2.0 flow, endpoints

2. **Measure Rate Limits:**
   - Default suspected: 60 requests/minute (very tight for automation)
   - Document: Batch strategy needed for high-volume operations

3. **Authentication Strategy:**
   - OAuth 2.0 token refresh mechanism (expires after ~2 hours)
   - Store refresh token securely in Supabase
   - Auto-refresh before expiry

**Impact:** 
- Loop 1 (Lead Intake): Cannot pull lead source data from Procore
- Loop 2 (Proposal Generation): Cannot pull project templates
- Loop 6 (Bid Coordination): Cannot pull job costing/scheduling
- Loop 8 (Accounting): Cannot pull cost tracking

**Timeline:** 2-3 days (research + design)

---

## Blocker #4: QuickBooks API Integration

**Status:** ❌ UNKNOWN — Requires Research

**Finding:**
- No QB code in CON-001 app
- No OAuth flow or API key storage
- Stripe payment events need to sync to QB for accounting

**Required Actions:**
1. **Verify Invoice Automation:**
   - Research: QB API invoice endpoints
   - Check: Real-time creation vs. batch-only
   - Document: Field mapping (project → invoice, labor → line items)

2. **Rate Limiting Strategy:**
   - QB rate limit: 100 requests/minute (tight)
   - Design: Batch processing for high volumes
   - Implement: Queueing system (n8n has built-in batching)

3. **Authentication & Token Refresh:**
   - OAuth 2.0 flow (QuickBooks Online)
   - Auto-refresh tokens (expires ~1 hour)
   - Secure storage in Supabase

**Impact:**
- Loop 3 (Payment Processing): Cannot write payments to QB
- Loop 8 (Accounting): Cannot export invoice data for reconciliation
- Financial reporting: No automated sync from CON-001 → QB → tax filing

**Timeline:** 2-3 days (research + design)

---

## Blocker #5: PlanSwift API Availability

**Status:** ❌ UNKNOWN — High Risk (May Not Exist)

**Finding:**
- No PlanSwift code in CON-001 app
- PlanSwift may be legacy desktop-only software (no public API)
- High risk that automation requires manual workaround

**Required Actions:**
1. **Research API Availability:**
   - Check: Does PlanSwift have a REST/GraphQL API?
   - Check: Is there a cloud version with integrations?
   - If no: Does it have a CSV/XML export capability?

2. **Fallback Strategy (if no API):**
   - Option A: Manual export + polling (user downloads CSV daily)
   - Option B: Scrape PlanSwift UI via Playwright (brittle, not recommended)
   - Option C: Replace with alternative estimating tool (Touchplan, Bridgit, etc.)

**Impact:**
- Loop 6 (Bid Coordination): Cannot automate bid estimation
- Estimators still manual; automation saves 2-3 hours/day per estimator

**Timeline:** 0.5 hours (research) + 1-2 days (redesign if no API)

---

## Go/No-Go Decision Matrix

| Blocker | Status | Go Criteria | Current | Decision |
|---------|--------|------------|---------|----------|
| #1 venture_leads | ✅ Fixed | Migration applied to Supabase | Pending Supabase apply | ✅ READY |
| #2 Stripe | ⚠️ Manual | Keys exist in Vercel env vars | Unverified | ⏳ VERIFY NOW |
| #3 Procore | ❌ Unknown | API + auth strategy documented | Not researched | ❌ BLOCKED |
| #4 QB | ❌ Unknown | API + rate limiting strategy documented | Not researched | ❌ BLOCKED |
| #5 PlanSwift | ❌ Unknown | API exists OR fallback strategy chosen | Not researched | ❌ BLOCKED |

**Phase 2 Go/No-Go:** **NO-GO** until all 5 blockers have action items complete.

---

## Execution Sequence

### This Week (Immediate)
- [ ] **Blocker #1:** Apply venture_leads migration to CON-001 Supabase
- [ ] **Blocker #2:** Pull Stripe keys from dashboard and add to Vercel environment
- [ ] **Blocker #3-5:** Research APIs (parallel, non-blocking)

### Next Week (After Blockers Resolved)
- [ ] Proceed to Phase 2: Customize LOOP.md for 8 construction loops
- [ ] Build 4 construction-specific agents (Classifier, Estimator, Bid, Accounting)
- [ ] Map domain knowledge (pricing model, complexity scoring, KPIs)

### Week 3-4 (Phase 3)
- [ ] Deploy Loop 1 (Lead Intake) + Classifier agent
- [ ] Deploy Loops 2-8 sequentially
- [ ] Full testing + production deployment

---

## Cost & Timeline Summary

**Implementation Cost (Scenario 1 — Open Source):**
- Year 1: $45,000 (n8n self-hosted, Playwright, LangGraph, Render VPS)
- Year 2+: $30,000/year (ongoing ops)

**Labor Savings:**
- Current: 15 hours/week manual work = $78,000/year
- Net Year 1: +$33,000 ROI

**Realistic Timeline:**
- Week 1-2: Blocker resolution + Phase 2 planning
- Week 3-8: Phase 3 execution + testing
- Total: 8 weeks to revenue (not original 4-5 weeks)

---

## References

- RED-TEAM-ANALYSIS.md (2026-07-16) — Full 5-blocker breakdown with hidden blockers and probability assessment
- CON-001-LOOPS.md — 8 construction automation loops design
- FRAMEWORK-ANALYSIS.md — Loop Engineering + Agency-Agents selection rationale
- TEST-RESULTS.md — Phase 1 testing results (all pass)
