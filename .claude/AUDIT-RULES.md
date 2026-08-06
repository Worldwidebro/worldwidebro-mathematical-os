# Venture Audit Rules

Scan ventures like a code-review team: find gaps, awareness, blockers.

## Checklist (per venture)

- [ ] Repo exists (GitHub)
- [ ] Has code (src/ or app/ or lib/)
- [ ] Has package.json (dependencies declared)
- [ ] Has Vercel config (vercel.json or .vercel/)
- [ ] Deployed to Vercel (URL accessible)
- [ ] Stripe configured (grep: stripe in package.json + API routes)
- [ ] Stripe webhook wired (n8n or manual handler)
- [ ] Customer funnel exists (landing page + signup)
- [ ] n8n workflows connected (if applicable)
- [ ] Supabase tables exist (ventures, invoices, deal_payments)
- [ ] Environment secrets set (STRIPE_KEY, SUPABASE_URL)
- [ ] Ready for revenue ✅ (all above pass)

## Gap Detection

Scan all ventures for:
- Missing Stripe integration (payment gap)
- Deployed but no funnel (discovery gap)
- Stripe + no webhook (automation gap)
- No Vercel config (deployment gap)
- n8n installed but workflows empty (orchestration gap)

## Extrapolation (712 ventures)

Sample 30 thoroughly, extrapolate to full 712:
- If 10% have Stripe: ~71 ventures ready for payment
- If 20% deployed to Vercel: ~142 ventures have live URLs
- If 5% have both: ~36 ventures can go live TODAY

## Report Format

```
VENTURE AUDIT REPORT
====================

READY NOW (Vercel + Stripe + Code):
- CON-001: ✅ https://con-001.vercel.app → Stripe connected → $5K/mo potential
- EC-111: ✅ https://ec-111.vercel.app → Stripe connected → $8K/mo potential
- OPS-001: ✅ https://ops-001.vercel.app → Stripe connected → $12K/mo potential

READY IN 2 HOURS (need Stripe or Vercel):
- captable: has Stripe, needs Vercel deploy
- +14 more

BLOCKERS (missing payment or deployment):
- 674 ventures: need Stripe + deployment + funnel wiring

NEXT ACTIONS:
1. Wire 3 pilots → $25K/mo revenue potential
2. Automate with /venture-ready skill
3. Deploy remaining 9 ready-in-2-hours
4. Target: $100K/mo in 30 days if all wired
```

## Intelligence Signals

Search ventures for:
- TODO/FIXME/BLOCKED comments
- Stripe key missing (grep: stripe_key, STRIPE_KEY)
- n8n workflows marked "draft" or "disabled"
- Vercel deployment failed (check deploy logs)
- Supabase connection errors in logs

