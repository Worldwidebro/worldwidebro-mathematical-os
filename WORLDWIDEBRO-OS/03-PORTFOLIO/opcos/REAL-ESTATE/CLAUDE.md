# Real Estate — Sector CLAUDE.md

Scoped context for working inside this OPCO. Loaded automatically alongside the
global `~/.claude/CLAUDE.md` when you're working in this folder.

## Sector snapshot

- **OPCO:** OPCO-RealEstate
- **Ventures:** 1 (planned: 1)
- **Readiness (v2, corrected, sector avg):** 13.5%
- **Site coverage:** 0/1 (0.0%)
- Capital layer: unassigned

## Ventures in this sector
- `RE-001-PROPERTY-HOLDINGS` — Property Holdings — Transaction commission (1-3% of transaction value)

## Revenue model mix (rule-based, see `VENTURE-REVENUE-MODELS.csv`)
- Transaction commission: 1 ventures

## Assigned agents

`qwen-real-estate` — 2 repos assigned (sector code `RE`).

## How this sector relates to others

Only 1 venture — essentially unbuilt as a sector. Lowest readiness tier alongside Construction; not worth independent tooling investment until more ventures exist here.

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

- Readiness: `grep ",real-estate," VENTURE-READINESS-SCORECARD-V2.csv`
- Revenue models: `grep ",real-estate," VENTURE-REVENUE-MODELS.csv`
- Before shipping any venture in this sector: run `/code-review`, `/security-review`,
  and `/verify` per the global CLAUDE.md workflow.
- Full portfolio dashboard: Sector Build-Out Registry artifact
  (https://claude.ai/code/artifact/9d66bb04-8613-403b-b1e3-4ebeb91ba9db) — filter to
  the "Real Estate" tab for this sector's live-site status per venture.

## Next: dive into a specific venture

Each venture folder lives at
`WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/<venture-folder>/VENTURE.md` — read that
plus `docs/REPOSITORY-MANIFEST.md` and `docs/FORMATION-CREDENTIAL-TRACKER.md` before
doing venture-specific work.
