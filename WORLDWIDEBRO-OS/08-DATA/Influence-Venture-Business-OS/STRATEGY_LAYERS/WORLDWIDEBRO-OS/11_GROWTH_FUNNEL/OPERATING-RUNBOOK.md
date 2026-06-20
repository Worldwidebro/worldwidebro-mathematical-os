# Funnel Operating Runbook

Weekly loop for any venture with a live funnel folder.

## Phase 0 — Foundation (once per venture, refresh quarterly)

- [ ] Fill `00_FOUNDATION/audience.md` (who, pain, desire, trigger)
- [ ] Fill `00_FOUNDATION/brand_identity.md` (positioning, tone, visual, proof)
- [ ] Brand Agent review: one voice across TOF/MOF/BOF

## Phase 1 — TOF (weekly)

**Goal:** Attention at scale.

- [ ] Pick 3 hooks from `01_TOF/hooks.md` or generate via TOF Agent
- [ ] Produce 3–5 short videos (15–30s), hook-first, minimal explanation
- [ ] Post to Shorts / Reels / TikTok; track views, saves, profile CTR

**KPI targets:** views, shares, saves, CTR to profile

## Phase 2 — MOF (weekly)

**Goal:** Belief — “this might work for me.”

- [ ] One demo or walkthrough script from `02_MOF/demos.md`
- [ ] One proof asset (case study, before/after, dashboard screenshot)
- [ ] Retarget TOF engagers with MOF content (email or paid)

**KPI targets:** watch time, site visits, email signups

## Phase 3 — BOF (bi-weekly or per campaign)

**Goal:** Close — remove doubt.

- [ ] Update `03_BOF/offers.md` (pricing, guarantee, risk reversal)
- [ ] Stack proof: testimonials, numbers, comparisons
- [ ] Single clear CTA on landing page spec

**KPI targets:** conversion rate, close rate, CAC

## Phase 4 — Retention (monthly)

- [ ] Review `04_RETENTION/upsell_loop.md`
- [ ] Onboard → activate → expand → refer

## Agent dispatch (optional)

```json
{
  "tof": "tof-viral-agent",
  "mof": "mof-proof-agent",
  "bof": "bof-conversion-agent",
  "brand_check": "brand-agent"
}
```

Store overrides in `ventures/{CODE}/agents/routing.json`.

## n8n

Import `WORKFLOWS/n8n-tof-mof-bof.json`, set webhook + Supabase credentials, point `venture_id` at linkage CSV row.
