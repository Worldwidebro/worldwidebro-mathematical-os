---
name: WORLDWIDEBRO-OS/09-GOVERNANCE/POLICIES
title: Governance Policies
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Governance Policies

## Venture Launch Checklist (5-Step)

1. **READINESS GATE:** Code deployed, Stripe live, Supabase ready (CTO + COO sign-off)
2. **EMAIL SEQUENCES:** 4 stages seeded, Resend configured, tracking ready (CMO sign-off)
3. **MARKETPLACE LISTING:** VEX page live, status="live" (not planned) (CMO sign-off)
4. **MONITORING:** Dashboard live, alerts configured, on-call assigned (CFO sign-off)
5. **LAUNCH:** Customer announcement, partner notification (CEO sign-off)

## Email Deployment Policy

**Required:**
- Resend API key + email_sequences table seeded
- Stripe webhook live + CTA links working
- trigger.dev workflow wired
- VP approval for >5000 emails/week

**Restrictions:**
- Must include unsubscribe link
- Compliance review required for healthcare/finance

## Partner Revenue Share Terms

**Standard:**
- Year 1: 30% of SaaS revenue (monthly payout)
- Year 2+: 25%
- Custom dev: 40%

**Auto-Promotion:**
- $50K annual → Tier 2 (35% commission)
- $250K annual → Tier 3 (40% commission)

**Payout:** Monthly via Stripe Connect, net 15

## Approval Gates

- Email campaign: VP Marketing
- Pricing change: CMO + CFO
- Partner tier: Auto if revenue threshold met
- Venture deactivation: COO + CFO
- New integration: CTO + VP Revenue
- Custom dev: CEO + CRO

**UPDATED: 2026-08-05**
