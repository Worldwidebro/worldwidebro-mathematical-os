# Construction — Sector CLAUDE.md

Scoped context for working inside this OPCO. Loaded automatically alongside the
global `~/.claude/CLAUDE.md` when you're working in this folder.

## Sector snapshot

- **OPCO:** OPCO-Construction
- **Ventures:** 20 (planned: 20)
- **Readiness (v2, corrected, sector avg):** 13.5%
- **Site coverage:** 20/20 (100.0%)
- Capital layer: unassigned

## Ventures in this sector
- `CON-001-ACE-CONSTRUCTION` — Ace Construction — Project fee / margin (10-20% margin on job value)
- `CON-002-RESIDENTIAL-CONSTRUCTION` — Residential Construction — Project fee / margin (10-20% margin on job value)
- `CON-003-COMMERCIAL-CONSTRUCTION` — Commercial Construction — Project fee / margin (10-20% margin on job value)
- `CON-004-INDUSTRIAL-CONSTRUCTION` — Industrial Construction — Project fee / margin (10-20% margin on job value)
- `CON-005-CONSTRUCTION-EQUIPMENT-RENTAL` — Construction Equipment Rental — Project fee / margin (10-20% margin on job value)
- `CON-006-CONSTRUCTION-PROJECT-MANAGEMENT` — Construction Project Management — Project fee / margin (10-20% margin on job value)
- `CON-007-GREEN-BUILDING-SERVICES` — Green Building Services — Project fee / margin (10-20% margin on job value)
- `CON-008-HOME-RENOVATION-SERVICES` — Home Renovation Services — Project fee / margin (10-20% margin on job value)
- `CON-009-ROOFING-COMPANY` — Roofing Company — Project fee / margin (10-20% margin on job value)
- `CON-010-PLUMBING-SERVICES` — Plumbing Services — Project fee / margin (10-20% margin on job value)
- `CON-011-ELECTRICAL-SERVICES` — Electrical Services — Project fee / margin (10-20% margin on job value)
- `CON-012-HVAC-SERVICES` — HVAC Services — Project fee / margin (10-20% margin on job value)
- `CON-013-PAINTING-SERVICES` — Painting Services — Subscription SaaS ($29-99/month)
- `CON-014-FLOORING-SERVICES` — Flooring Services — Project fee / margin (10-20% margin on job value)
- `CON-015-LANDSCAPING-SERVICES` — Landscaping Services — Project fee / margin (10-20% margin on job value)

_...and 5 more — see `ventures.csv` filtered to `sector == construction` for the full list._

## Revenue model mix (rule-based, see `VENTURE-REVENUE-MODELS.csv`)
- Project fee / margin: 19 ventures
- Subscription SaaS: 1 ventures

## Assigned agents

`qwen-construction` — 24 repos assigned (sector code `CON`).

## How this sector relates to others

Lowest readiness tier (13.5%) alongside Real-Estate. 100% site coverage (20/20) but that's necessary, not sufficient — needs Financial (invoice factoring, payroll) and Logistics (materials/equipment) most.

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

- Readiness: `grep ",construction," VENTURE-READINESS-SCORECARD-V2.csv`
- Revenue models: `grep ",construction," VENTURE-REVENUE-MODELS.csv`
- Before shipping any venture in this sector: run `/code-review`, `/security-review`,
  and `/verify` per the global CLAUDE.md workflow.
- Full portfolio dashboard: Sector Build-Out Registry artifact
  (https://claude.ai/code/artifact/9d66bb04-8613-403b-b1e3-4ebeb91ba9db) — filter to
  the "Construction" tab for this sector's live-site status per venture.

## Next: dive into a specific venture

Each venture folder lives at
`WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/<venture-folder>/VENTURE.md` — read that
plus `docs/REPOSITORY-MANIFEST.md` and `docs/FORMATION-CREDENTIAL-TRACKER.md` before
doing venture-specific work.
