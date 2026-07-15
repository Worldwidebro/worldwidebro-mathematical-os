# Technology — Sector CLAUDE.md

Scoped context for working inside this OPCO. Loaded automatically alongside the
global `~/.claude/CLAUDE.md` when you're working in this folder.

## Sector snapshot

- **OPCO:** OPCO-Technology
- **Ventures:** 61 (planned: 59, validation: 1, mvp: 1)
- **Readiness (v2, corrected, sector avg):** 34.9%
- **Site coverage:** 0/61 (0.0%)
- **Capital Layer 2 — Skill Monetization** (50-100 digital products (SaaS, content, templates), target $20K-$30K/mo, 60-80% margin)

## Ventures in this sector
- `TECH-001-Quantum-Algorithm-AI` — Quantum Algorithm Ai — Subscription SaaS ($29-99/month)
- `TECH-002-AI-Compliance-Scanner` — Ai Compliance Scanner — B2B compliance SaaS ($199-499/month per institution monitored)
- `TECH-003-Cloud-Management-AI` — Cloud Management Ai — Subscription SaaS ($29-99/month)
- `TECH-004-Robotics-Training-AI` — Robotics Training Ai — Course fee or subscription ($19-99 one-time or /month)
- `TECH-005-Customer-Insights-AI` — Customer Insights Ai — B2B SaaS subscription ($49-199/month per seat)
- `TECH-006-Voice-Assistant-AI` — Voice Assistant Ai — Subscription SaaS ($29-99/month)
- `TECH-007-Blockchain-Verifier-AI` — Blockchain Verifier Ai — Subscription SaaS ($29-99/month)
- `TECH-008-Cybersecurity-Shield` — Cybersecurity Shield — Subscription SaaS ($29-99/month)
- `TECH-009-Content-Studio-AI` — Content Studio Ai — Ad revenue + subscription (CPM/sponsorship + $5-15/month premium tier)
- `TECH-010-Smart-Home-AI` — Smart Home Ai — Subscription SaaS ($29-99/month)
- `TECH-011-Supply-Chain-Optimizer` — Supply Chain Optimizer — Subscription SaaS ($29-99/month)
- `TECH-012-Data-Visualization-AI` — Data Visualization Ai — Subscription SaaS ($29-99/month)
- `TECH-013-Workflow-Automation` — Workflow Automation — Subscription SaaS ($29-99/month)
- `TECH-014-Sentiment-Analyzer` — Sentiment Analyzer — Subscription SaaS ($29-99/month)
- `TECH-015-Image-Recognition-AI` — Image Recognition Ai — Subscription SaaS ($29-99/month)

_...and 46 more — see `ventures.csv` filtered to `sector == technology` for the full list._

## Revenue model mix (rule-based, see `VENTURE-REVENUE-MODELS.csv`)
- Subscription SaaS: 44 ventures
- B2B compliance SaaS: 4 ventures
- Course fee or subscription: 4 ventures
- B2B SaaS subscription: 4 ventures

## Assigned agents

`qwen-technology` — 56 repos assigned (sector code `TECH`).

## How this sector relates to others

Supplies platform/infrastructure capabilities other sectors consume (agents, automation, APIs). Highest-leverage sector to mine for reusable components before building sector-specific tools.

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

- Readiness: `grep ",technology," VENTURE-READINESS-SCORECARD-V2.csv`
- Revenue models: `grep ",technology," VENTURE-REVENUE-MODELS.csv`
- Before shipping any venture in this sector: run `/code-review`, `/security-review`,
  and `/verify` per the global CLAUDE.md workflow.
- Full portfolio dashboard: Sector Build-Out Registry artifact
  (https://claude.ai/code/artifact/9d66bb04-8613-403b-b1e3-4ebeb91ba9db) — filter to
  the "Technology" tab for this sector's live-site status per venture.

## Next: dive into a specific venture

Each venture folder lives at
`WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/<venture-folder>/VENTURE.md` — read that
plus `docs/REPOSITORY-MANIFEST.md` and `docs/FORMATION-CREDENTIAL-TRACKER.md` before
doing venture-specific work.
