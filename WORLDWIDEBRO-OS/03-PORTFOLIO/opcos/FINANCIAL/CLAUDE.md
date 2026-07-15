# Financial — Sector CLAUDE.md

Scoped context for working inside this OPCO. Loaded automatically alongside the
global `~/.claude/CLAUDE.md` when you're working in this folder.

## Sector snapshot

- **OPCO:** OPCO-Financial
- **Ventures:** 36 (planned: 35, growth: 1)
- **Readiness (v2, corrected, sector avg):** 35.4%
- **Site coverage:** 4/36 (11.1%)
- **Capital Layer 2 — Skill Monetization** (50-100 digital products (SaaS, content, templates), target $20K-$30K/mo, 60-80% margin)

## Ventures in this sector
- `FIN-001-GenixBank-Lite` — Genixbank Lite — Subscription SaaS ($49-149/month)
- `FIN-002-Credit-Repair-Automation` — Credit Repair Automation — Subscription SaaS ($29-99/month)
- `FIN-003-AI-Boss-Hub-Lite` — Ai Boss Hub Lite — Subscription SaaS ($29-99/month)
- `FIN-004-GenixBanks-AI-Treasurer` — Genixbanks Ai Treasurer — Subscription SaaS ($29-99/month)
- `FIN-005-U-Haul-Rental-Affiliate` — U Haul Rental Affiliate — Affiliate commission (5-15% per referred transaction)
- `FIN-006-Tax-Prep-Filing-Services` — Tax Prep Filing Services — Per-filing fee ($49-249 per return)
- `FIN-007-Business-Credit-Building` — Business Credit Building — Subscription SaaS ($49-149/month)
- `FIN-008-Business-Formation-Services` — Business Formation Services — Flat formation fee ($99-499 one-time + annual renewal)
- `FIN-009-Crypto-Tax-Optimizer` — Crypto Tax Optimizer — Subscription SaaS ($29-99/month)
- `FIN-010-AI-Powered-Garbage-Collection` — Ai Powered Garbage Collection — Per-shipment / per-route fee (B2B SaaS, per-route or per-unit fee)
- `FIN-011-Automated-Bookkeeping` — Automated Bookkeeping — Subscription (accounting SaaS) ($49-149 / month)
- `FIN-012-Invoice-Factoring-AI` — Invoice Factoring Ai — Per-transaction fee (1-3% + flat fee per transaction)
- `FIN-013-Charity-Donation-AI` — Charity Donation Ai — Subscription SaaS ($29-99/month)
- `FIN-014-Expense-Tracker-AI` — Expense Tracker Ai — Subscription (accounting SaaS) ($49-149 / month)
- `FIN-015-Financial-Wellness-Coach` — Financial Wellness Coach — Course fee or subscription ($19-99 one-time or /month)

_...and 21 more — see `ventures.csv` filtered to `sector == financial` for the full list._

## Revenue model mix (rule-based, see `VENTURE-REVENUE-MODELS.csv`)
- Subscription SaaS: 12 ventures
- Per-transaction fee: 4 ventures
- Per-document fee or subscription: 3 ventures
- Per-filing fee: 2 ventures

## Assigned agents

**Overlapping coverage — 3 agents claim this sector, not resolved:**
- `qwen-finance` — 43 repos (sector code `FIN`)
- `qwen-financial-health` — 36 repos (sector code `FH`)
- `qwen-financial-services` — 25 repos (sector code `FS`)

Check which agent actually owns a given repo before assuming `qwen-finance` alone covers it.

## How this sector relates to others

Horizontal/enabling sector — payroll, bookkeeping, tax, and compliance ventures here are back-office inputs every other sector's ventures need. Financial ventures should be pitched *to* Construction, Beauty-Wellness, Food-Hospitality, etc. as vendors, not just built as standalone SaaS.

## Known data quality issues (don't trust blindly)

- `venture-capabilities-proposed.csv` assigns an **identical** capability set
  (api/authentication/database/dashboard/crm or similar) to every venture in this
  sector — the count always equals the venture count, meaning it's a stamped
  template, not real per-venture capability data. Don't cite "top capabilities"
  from that file as if they differentiate ventures within this sector.
- `development_stage` in `VENTURE.json` per repo is self-reported and was wrong for
  355/415 verified ventures portfolio-wide (see `[[venture-readiness-scorecard-v2]]`
  memory) — prefer `readiness_pct_v2` over the raw `stage` field.
- Revenue models above are rule-based (keyword match on venture name), not verified
  business plans — treat as a starting proposal, not fact.

## Audit & test

- Readiness: `grep ",financial," VENTURE-READINESS-SCORECARD-V2.csv`
- Revenue models: `grep ",financial," VENTURE-REVENUE-MODELS.csv`
- Before shipping any venture in this sector: run `/code-review`, `/security-review`,
  and `/verify` per the global CLAUDE.md workflow.
- Full portfolio dashboard: Sector Build-Out Registry artifact
  (https://claude.ai/code/artifact/9d66bb04-8613-403b-b1e3-4ebeb91ba9db) — filter to
  the "Financial" tab for this sector's live-site status per venture.

## Next: dive into a specific venture

Each venture folder lives at
`WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/<venture-folder>/VENTURE.md` — read that
plus `docs/REPOSITORY-MANIFEST.md` and `docs/FORMATION-CREDENTIAL-TRACKER.md` before
doing venture-specific work.
