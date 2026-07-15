# Beauty Wellness — Sector CLAUDE.md

Scoped context for working inside this OPCO. Loaded automatically alongside the
global `~/.claude/CLAUDE.md` when you're working in this folder.

## Sector snapshot

- **OPCO:** OPCO-BeautyWellness
- **Ventures:** 40 (mvp: 16, validation: 15, planned: 9)
- **Readiness (v2, corrected, sector avg):** 24.5%
- **Site coverage:** 0/40 (0.0%)
- **Capital Layer 1 — Labor Income** (20-30 service ventures (CON, STA, BUS), target $5K-$15K/mo, 40-53% margin)

## Ventures in this sector
- `BW-001-Lash-Extension-Studio` — Lash Extension Studio — Membership / per-session fee ($29-99/month)
- `BW-002-Mobile-Lash-Service` — Mobile Lash Service — Membership / per-session fee ($29-99/month)
- `BW-003-Luxury-Lash-Bar` — Luxury Lash Bar — Membership / per-session fee ($29-99/month)
- `BW-004-Lash-Training-Academy` — Lash Training Academy — Course fee or subscription ($19-99 one-time or /month)
- `BW-005-Lash-Supply-Company` — Lash Supply Company — Membership / per-session fee ($29-99/month)
- `BW-006-Lash-Glue-Brand` — Lash Glue Brand — Membership / per-session fee ($29-99/month)
- `BW-007-Lash-Kits-&-Tools` — Lash Kits & Tools — Membership / per-session fee ($29-99/month)
- `BW-008-Private-Label-Lashes` — Private Label Lashes — Membership / per-session fee ($29-99/month)
- `BW-009-Franchise-Lash-Salons` — Franchise Lash Salons — Membership / per-session fee ($29-99/month membership or per-session)
- `BW-010-Online-Lash-Education` — Online Lash Education — Course fee or subscription ($19-99 one-time or /month)
- `BW-011-Nail-Salon` — Nail Salon — Membership / per-session fee ($29-99/month membership or per-session)
- `BW-012-Mobile-Nail-Tech` — Mobile Nail Tech — Subscription SaaS ($29-99/month)
- `BW-013-Luxury-Nail-Spa` — Luxury Nail Spa — Membership / per-session fee ($29-99/month membership or per-session)
- `BW-014-Press-On-Nail-Brand` — Press On Nail Brand — Subscription SaaS ($29-99/month)
- `BW-015-Nail-Art-Studio` — Nail Art Studio — Subscription SaaS ($29-99/month)

_...and 25 more — see `ventures.csv` filtered to `sector == beauty-wellness` for the full list._

## Revenue model mix (rule-based, see `VENTURE-REVENUE-MODELS.csv`)
- Membership / per-session fee: 25 ventures
- Subscription SaaS: 11 ventures
- Course fee or subscription: 2 ventures
- Marketplace take-rate: 2 ventures

## Assigned agents

`qwen-beauty-wellness` — 45 repos assigned (sector code `BW`).

## How this sector relates to others

Local-service sector; benefits from Community's reach and Financial's payment/booking infrastructure more than it needs bespoke tech of its own.

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

- Readiness: `grep ",beauty-wellness," VENTURE-READINESS-SCORECARD-V2.csv`
- Revenue models: `grep ",beauty-wellness," VENTURE-REVENUE-MODELS.csv`
- Before shipping any venture in this sector: run `/code-review`, `/security-review`,
  and `/verify` per the global CLAUDE.md workflow.
- Full portfolio dashboard: Sector Build-Out Registry artifact
  (https://claude.ai/code/artifact/9d66bb04-8613-403b-b1e3-4ebeb91ba9db) — filter to
  the "Beauty Wellness" tab for this sector's live-site status per venture.

## Next: dive into a specific venture

Each venture folder lives at
`WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/<venture-folder>/VENTURE.md` — read that
plus `docs/REPOSITORY-MANIFEST.md` and `docs/FORMATION-CREDENTIAL-TRACKER.md` before
doing venture-specific work.
