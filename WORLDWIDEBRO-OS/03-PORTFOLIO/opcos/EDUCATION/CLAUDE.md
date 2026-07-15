# Education — Sector CLAUDE.md

Scoped context for working inside this OPCO. Loaded automatically alongside the
global `~/.claude/CLAUDE.md` when you're working in this folder.

## Sector snapshot

- **OPCO:** OPCO-Education
- **Ventures:** 40 (planned: 39, growth: 1)
- **Readiness (v2, corrected, sector avg):** 34.5%
- **Site coverage:** 0/40 (0.0%)
- **Capital Layer 2 — Skill Monetization** (50-100 digital products (SaaS, content, templates), target $20K-$30K/mo, 60-80% margin)

## Ventures in this sector
- `EDU-001-Youth-Entrepreneurship-Curriculum` — Youth Entrepreneurship Curriculum — Course fee or subscription ($19-99 one-time or /month)
- `EDU-002-AI-Literacy-Program` — Ai Literacy Program — Subscription SaaS ($29-99/month)
- `EDU-003-Coding-Mentor-Certification` — Coding Mentor Certification — Course fee or subscription ($19-99 one-time or /month)
- `EDU-004-Real-Estate-Licensing-Prep` — Real Estate Licensing Prep — Transaction commission (1-3% of transaction value)
- `EDU-005-Coding-Bootcamp` — Coding Bootcamp — Course fee or subscription ($19-99 one-time or /month)
- `EDU-006-Homeschooling-Content-AI` — Homeschooling Content Ai — Ad revenue + subscription (CPM/sponsorship + $5-15/month premium tier)
- `EDU-007-AI-Tutoring-Platform` — Ai Tutoring Platform — Course fee or subscription ($19-99 one-time or /month)
- `EDU-008-Branding-Templates-Marketplace` — Branding Templates Marketplace — Marketplace take-rate (8-20% of GMV)
- `EDU-009-Voiceover-Script-Library` — Voiceover Script Library — Course fee or subscription ($19-99 one-time or /month)
- `EDU-010-Trade-Skills-Bootcamp` — Trade Skills Bootcamp — Course fee or subscription ($19-99 one-time or /month)
- `EDU-011-Franchise-Blueprint-System` — Franchise Blueprint System — Course fee or subscription ($19-99 one-time or /month)
- `EDU-012-Low-Income-Housing-Blueprint` — Low Income Housing Blueprint — Course fee or subscription ($19-99 one-time or /month)
- `EDU-013-Automated-Empire-Book` — Automated Empire Book — Course fee or subscription ($19-99 one-time or /month)
- `EDU-014-BIPOC-Creator-Incubator` — Bipoc Creator Incubator — Course fee or subscription ($19-99 one-time or /month)
- `EDU-015-AI-Legal-Doc-Generator` — Ai Legal Doc Generator — Per-document fee or subscription ($29-79 / month or per-document)

_...and 25 more — see `ventures.csv` filtered to `sector == education` for the full list._

## Revenue model mix (rule-based, see `VENTURE-REVENUE-MODELS.csv`)
- Course fee or subscription: 25 ventures
- Subscription SaaS: 10 ventures
- Per-document fee or subscription: 2 ventures
- Transaction commission: 1 ventures

## Assigned agents

`qwen-education` — 58 repos assigned (sector code `EDU`).

## How this sector relates to others

Feeds labor into Professional-Services and Staffing-type ventures across every other sector — training/upskilling is the actual product of this sector, not just courses sold direct to consumers.

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

- Readiness: `grep ",education," VENTURE-READINESS-SCORECARD-V2.csv`
- Revenue models: `grep ",education," VENTURE-REVENUE-MODELS.csv`
- Before shipping any venture in this sector: run `/code-review`, `/security-review`,
  and `/verify` per the global CLAUDE.md workflow.
- Full portfolio dashboard: Sector Build-Out Registry artifact
  (https://claude.ai/code/artifact/9d66bb04-8613-403b-b1e3-4ebeb91ba9db) — filter to
  the "Education" tab for this sector's live-site status per venture.

## Next: dive into a specific venture

Each venture folder lives at
`WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/<venture-folder>/VENTURE.md` — read that
plus `docs/REPOSITORY-MANIFEST.md` and `docs/FORMATION-CREDENTIAL-TRACKER.md` before
doing venture-specific work.
