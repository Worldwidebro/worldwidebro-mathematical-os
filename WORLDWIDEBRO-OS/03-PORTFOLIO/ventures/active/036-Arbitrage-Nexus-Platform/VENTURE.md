# Arbitrage Nexus Platform

| Field | Value |
|-------|-------|
| Venture ID | FIN-036-Arbitrage-Nexus-Platform |
| Sector | financial |
| OPCO | FINANCIAL |
| Stage | building (was self-reported "growth" — corrected; no revenue, no live integration yet) |
| Status | active, stalled since 2026-04-16 |
| Entity | Arbitrage Nexus Platform LLC |
| State | WY |
| Formation Status | pending_formation |
| First Dollar Action | Run the documented 7-day Crucix deal-scoring test (27 OSINT feeds) → package 3-5 sample deal leads into a report → pitch 3 warm family-office/micro-PE contacts for a paid pilot |
| First Dollar Price | $5,000 |
| First Dollar Platform | Direct outreach + Stripe invoicing |
| Days to Revenue | 30 |
| Monthly Target | $15,000 (near-term milestone; doc's blue-sky target is $50K-$250K at 10 customers) |
| Revenue Model | Enterprise deal-flow subscription ($5K-$25K/month) to family offices and micro-PE firms, plus 1-5% commission on closed deals |

## ICP

- **Title:** Family office principal or micro-PE partner sourcing off-market M&A / distressed-asset deal flow
- **Pain Point:** Can't efficiently source pre-market or distressed deals; misses timing signals larger buyers get first
- **Platform:** Direct/warm intro, LinkedIn, M&A community forums
- **Opening Line:** "We surface pre-market M&A and distressed-asset leads from 27 live OSINT feeds — want to see this week's deal pipeline?"

## Repositories

- [`Worldwidebro/fin-036-arbitrage-nexus-platform`](https://github.com/Worldwidebro/fin-036-arbitrage-nexus-platform) — canonical venture repo: strategy docs (`CRUCIX_DEAL_MAPPING.md`, `FUNDING.md`, `PHASE_TRACKER.md`), `VENTURE.json`, `lib/shared` submodule. No deal-scoring or Crucix-integration code implemented yet.
- [`Worldwidebro/arbitrage-nexus`](https://github.com/Worldwidebro/arbitrage-nexus) — frontend MVP (React + TS + Vite + Supabase + shadcn/ui). Real multi-vertical marketplace: listing creation, messaging, admin approval flow, and test-mode Stripe payment link generation all built and deployed live at https://arbitrage-nexus.vercel.app (as of 2026-07-13). Backend now runs on a dedicated `arbitrage_nexus` schema inside the CivilizationOS Supabase project (`cyhzilqldouzgynacqpe`), migrated off the original Lovable-provisioned project this session had no admin access to.

## Capabilities

- Supabase auth + RLS-backed opportunity/messaging schema (real, live, in `arbitrage_nexus` schema)
- Real listing creation, messaging, admin approval, and Stripe payment-link generation (test mode) — all live on Vercel
- Deal-scoring methodology + feed-to-vertical mapping (documented only, in `CRUCIX_DEAL_MAPPING.md` — not yet code)
- Crucix OSINT feed access (live locally on :3117, per Finance Intelligence Stack — not yet wired to this venture)

## Known gaps (as of 2026-07-13)

- Core premise untested: whether Crucix's 27 feeds can actually surface a qualifying $5M+ deal lead. This is the highest-leverage next validation step.
- Admin grant + RLS self-admin security fix both require a manual Supabase SQL Editor visit (session has no DB-owner access to apply migrations directly).
- Stripe wired in test mode only — needs a live key swap when ready to actually collect a commission.
- No repo currently calls Crucix's API at all.

---
Generated from `08-DATA/registries/*` + `03-PORTFOLIO/ventures/active/036-Arbitrage-Nexus-Platform/VENTURE.json`. Manually corrected 2026-07-11, re-corrected 2026-07-13 after this file was found reverted to a blank auto-generated stub by an unidentified regeneration process (715 VENTURE.md files across the portfolio were touched in the same event) — root cause not yet found; see project memory. Don't trust this file's persistence across sessions without re-verifying against git history.