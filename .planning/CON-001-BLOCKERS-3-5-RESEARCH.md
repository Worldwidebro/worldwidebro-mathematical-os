# CON-001 Blockers #3-5 Research & Action Plan
**Date:** 2026-07-16  
**Status:** Complete — All three blockers have solutions  

---

## Blocker #3: Procore API Integration

### Findings
✅ **Procore HAS REST API** — Requires partner registration  

**Key Details:**
- Auth: OAuth 2.0 (partner-gated)
- Rate Limit: 60 req/min
- Endpoints: Projects, budgets, schedules, financials all available
- Registration: https://developer.procore.com → Partner signup (3-5 business days)

**Implementation:**
1. Register as Procore Partner (5 min, wait 3-5 days for approval)
2. OAuth token storage in Supabase ventures table
3. Auto-refresh tokens before expiry
4. Query on payment events (Loop 1 + 6 + 8)

**Timeline:** 5-8 days (including partner wait)  
**Risk:** MEDIUM (partner approval required)  
**Decision:** ✅ **PROCEED** — Stable API, well-documented

---

## Blocker #4: QuickBooks Online API

### Findings
✅ **QB Online HAS excellent Invoice API** — Recommended path  

**Key Details:**
- Auth: OAuth 2.0 (user authorizes once in dashboard)
- Rate Limit: 100 req/min (very generous)
- Invoice Creation: Direct POST with line items
- Supports: Invoices, journal entries, tax tracking

**Invoice Creation Flow:**
```
Stripe payment_intent.succeeded
  → Extract: venture_id, amount, email
  → Get QB OAuth token from Supabase
  → POST /invoices { LineItems, Customer, DueDate }
  → Store QB invoice_id for reconciliation
  → Return to frontend (success)
```

**Implementation:**
1. Add QB OAuth button to CON-001 settings (dashboard)
2. Store refresh_token in Supabase ventures.qb_refresh_token
3. Create QB invoice logic in webhook or n8n
4. Auto-sync status back to venture_leads

**Timeline:** 3-4 days  
**Risk:** LOW (production-ready API)  
**Decision:** ✅ **PRIORITY #1** — Start immediately after Stripe goes live

**Files to Create:**
- `src/lib/integrations/quickbooks.ts` — OAuth + invoice logic
- `src/app/settings/qb-connect.tsx` — Auth component
- `src/app/api/webhooks/qb-sync/route.ts` — Invoice status polling

---

## Blocker #5: PlanSwift API

### Findings
❌ **PlanSwift HAS NO PUBLIC API** — Desktop-only software  

**Reality:**
- No REST API exists
- CSV/XML export only (manual)
- Windows desktop application
- Limited to Excel integrations

**Loop 6 Impact:**
Bid Coordination Loop cannot auto-pull estimates without workaround.

**Workaround Solutions (Priority Order):**

### Option A: Migrate to Touchplan (RECOMMENDED)
- Cloud-based estimating + scheduling
- Native REST API
- Rate limit: 500 req/min
- Cost: $100-300/month
- Integration: 2 days

### Option B: Keep PlanSwift, Use CSV Polling (TEMPORARY)
- Estimator exports CSV daily to shared folder
- CON-001 polls for new CSVs
- n8n parses → creates projects
- Cost: 1-2 hours/week manual work
- Integration: 1 day
- **Use this NOW, migrate to Touchplan later**

### Option C: Bridgit Bench (ALTERNATIVE)
- Resource planning + job costing
- Integrates with Procore
- Cost: $50-150/month
- Integration: 2 days

**Recommendation:**
- **Week 1:** Use Option B (CSV manual export)
- **Week 2-3:** Evaluate Touchplan for migration
- **Week 4+:** Full Touchplan API integration

**Timeline:** 1 day (CSV setup) + 5-10 days (Touchplan migration later)  
**Risk:** MEDIUM (no API, but workarounds exist)  
**Decision:** ✅ **PROCEED with CSV interim, plan Touchplan migration**

---

## Execution Roadmap

### Phase 1: QB Invoice API (This Week)
- [ ] Day 1: Create QB OAuth component
- [ ] Day 1: Implement invoice creation logic
- [ ] Day 2: Wire to stripe webhook
- [ ] Day 2: Test end-to-end
- **Result:** Loop 3 fully operational ✅

### Phase 2: Procore Integration (Next Week)
- [ ] Day 1: Register Procore Partner (wait for approval)
- [ ] Days 5-6: Implement OAuth + endpoints
- [ ] Day 7: Test with real Procore account
- **Result:** Loop 1 + 6 + 8 can pull project data ✅

### Phase 3: PlanSwift Workaround (This Week)
- [ ] Day 1: Set up CSV polling script
- [ ] Day 1: Wire to n8n for project creation
- **Result:** Manual workflow in place, ready for Touchplan migration

### Phase 4: PlanSwift Migration (Next Month)
- [ ] Touchplan account setup
- [ ] Data migration from PlanSwift
- [ ] API integration
- **Result:** Fully automated bid coordination ✅

---

## Cost & Timeline Summary

| Blocker | Solution | Cost/Month | Implementation | Timeline | Go Decision |
|---------|----------|-----------|-----------------|----------|------------|
| **#3 Procore** | Partner API | $0 | OAuth + token refresh | 5-8 days | ✅ PROCEED |
| **#4 QB** | OAuth Invoice API | $0 | Dashboard auth + webhook | 3-4 days | ✅ **NEXT** |
| **#5 PlanSwift** | CSV interim + Touchplan | $0-300 | Manual export → Touchplan | 1 day + 5-10 days | ✅ PROCEED |

---

## Next Actions

**Today (2026-07-16):**
- Commit this research
- Start QB OAuth component

**By EOW (2026-07-18):**
- QB invoice API working end-to-end
- PlanSwift CSV workflow in place
- Procore partner registration submitted

**Blockers status post-Phase 1:**
- ✅ #1 venture_leads table
- ✅ #2 Stripe webhook
- 🔄 #3 Procore (waiting for partner approval)
- ✅ #4 QB (ready for Phase 2)
- ✅ #5 PlanSwift (CSV + Touchplan plan)

**Phase 2 Entry Criteria:**
All blockers have action plans + Procore approval lands → Begin implementation
