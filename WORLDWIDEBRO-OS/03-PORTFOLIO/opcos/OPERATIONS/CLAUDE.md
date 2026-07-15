# Operations — Sector CLAUDE.md

Scoped context for working inside this OPCO. Loaded automatically alongside the
global `~/.claude/CLAUDE.md` when you're working in this folder.

## Sector snapshot

- **OPCO:** OPCO-Operations
- **Ventures:** 67 (planned: 66, mvp: 1)
- **Readiness (v2, corrected, sector avg):** 18.7%
- **Site coverage:** 0/67 (0.0%)
- **Capital Layer 1 — Labor Income** (20-30 service ventures (CON, STA, BUS), target $5K-$15K/mo, 40-53% margin)

## Ventures in this sector
- `OPS-001-Fractional-CTO-Agency` — Fractional Cto Agency — B2B SaaS subscription ($49-199/month per seat)
- `OPS-001-VENTURE-STAFFING` — Venture Staffing Operations — Placement fee (15-25% of first-year salary)
- `OPS-002-Supply-Chain-Optimizer` — Supply Chain Optimizer — Subscription SaaS ($29-99/month)
- `OPS-003-Event-Planning-AI` — Event Planning Ai — Subscription SaaS ($29-99/month)
- `OPS-004-Inventory-Management-AI` — Inventory Management Ai — Subscription SaaS ($29-99/month)
- `OPS-005-Project-Management-AI` — Project Management Ai — Subscription SaaS ($29-99/month)
- `OPS-006-Document-Automation-AI` — Document Automation Ai — Subscription SaaS ($29-99/month)
- `OPS-007-Meeting-Assistant-AI` — Meeting Assistant Ai — Subscription SaaS ($29-99/month)
- `OPS-008-Recruitment-AI` — Recruitment Ai — Placement fee (15-25% of first-year salary)
- `OPS-009-Onboarding-AI` — Onboarding Ai — Subscription SaaS ($29-99/month)
- `OPS-010-Training-Platform-AI` — Training Platform Ai — Course fee or subscription ($19-99 one-time or /month)
- `OPS-011-Performance-Review-AI` — Performance Review Ai — Subscription SaaS ($29-99/month)
- `OPS-012-IT-Support-AI` — It Support Ai — Subscription SaaS ($29-99/month)
- `OPS-013-Facilities-Management-AI` — Facilities Management Ai — Subscription SaaS ($29-99/month)
- `OPS-014-Travel-Booking-AI` — Travel Booking Ai — Subscription SaaS ($29-99/month)

_...and 52 more — see `ventures.csv` filtered to `sector == operations` for the full list._

## Revenue model mix (rule-based, see `VENTURE-REVENUE-MODELS.csv`)
- Subscription SaaS: 48 ventures
- B2B SaaS subscription: 4 ventures
- Per-document fee or subscription: 3 ventures
- B2B compliance SaaS: 3 ventures

## Assigned agents

`qwen-operations` — 18 repos assigned (sector code `OPS`).

## How this sector relates to others

Cross-cutting: these are internal tools (dashboards, automation, agents) other sectors' ventures could adopt directly rather than each building their own — check here before building bespoke ops tooling elsewhere.

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

- Readiness: `grep ",operations," VENTURE-READINESS-SCORECARD-V2.csv`
- Revenue models: `grep ",operations," VENTURE-REVENUE-MODELS.csv`
- Before shipping any venture in this sector: run `/code-review`, `/security-review`,
  and `/verify` per the global CLAUDE.md workflow.
- Full portfolio dashboard: Sector Build-Out Registry artifact
  (https://claude.ai/code/artifact/9d66bb04-8613-403b-b1e3-4ebeb91ba9db) — filter to
  the "Operations" tab for this sector's live-site status per venture.

## Next: dive into a specific venture

Each venture folder lives at
`WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/<venture-folder>/VENTURE.md` — read that
plus `docs/REPOSITORY-MANIFEST.md` and `docs/FORMATION-CREDENTIAL-TRACKER.md` before
doing venture-specific work.
