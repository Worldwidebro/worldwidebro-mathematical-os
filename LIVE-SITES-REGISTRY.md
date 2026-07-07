# Live Sites Registry

One place to find every real, deployed URL and what's actually left before each is client-ready.
Update this whenever a site is deployed, redeployed, or its readiness changes — this is meant to
replace re-discovering URLs from scratch each session.

| Site | URL | Repo | Status | What's left |
|------|-----|------|--------|-------------|
| Venture Hub (dashboard) | https://venture-hub-pi.vercel.app | (not yet located/cloned locally) | Live | Data is stale — shows `hasCode: false` for all 687 ventures incl. ones that are now real; no sync from real deployment state |
| VEX (holdings/studio site) | https://vex-hero-site-sigma.vercel.app | `github.com/Worldwidebro/vex-site` | Live | Missing pages per audit: Case Studies, Intake/Apply, Advisory Packages, Sector/OpCo pages, 404 (in progress, stashed — see `git stash list` in the repo) |
| CON-001 Ace Construction | https://con-001-ace-construction.vercel.app | `github.com/Worldwidebro/con-001-ace-construction` | Live | Stripe checkout code written, needs 3 secrets: `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `SUPABASE_SERVICE_ROLE_KEY`. Resend needs a real account + verified domain. |
| OPS-STAFF-001 Staffing | https://ops-staff-001-staffing.vercel.app | (not yet located/cloned locally) | Live (built by parallel session) | Not yet audited this session — needs the same kind of check con-001 got (real backend? real content? placeholder info?) |
| COMM-003 Ace Senior Care Connect | https://comm-003-ace-senior-care-connect.vercel.app | `github.com/Worldwidebro/comm-003-ace-senior-care-connect` | Live | Pure static/informational site, no backend wired — deployed clean, no blockers. First of 50 COMM ventures confirmed to have real Next.js apps (see `repo-site-scan-2026-07` memory) |
| Bloom (Community sector hub) | https://bloom-community-hub.vercel.app | `github.com/Worldwidebro/bloom-community-hub` | Live | Liquid-glass hero + `/ventures` directory linking to 48/50 real COMM venture sites. **Static build — no live API calls**, data baked in at build time from a one-off script run, not auto-synced |
| 48 individual COMM ventures | comm-001 through comm-050 (minus comm-014, comm-019) | `github.com/Worldwidebro/comm-NNN-*` | Live | All static/informational, no backend. comm-014 and comm-019 failed on transient Vercel network errors (`ECONNRESET`, `Not authorized`) — not code bugs, need a manual retry |

## Important: none of these sites call live tools at runtime
Bloom and vex-hero-site are static builds — `src/data/ventures.ts` / `portfolio.public.json` are
generated once from a script run and baked into the deploy. Neither site queries Supabase, Neo4j,
or GitHub live. If a venture goes live tomorrow, these sites won't reflect it until someone
re-runs the data generator and redeploys by hand — same manual loop used all session so far. No
scheduled/automatic sync exists yet.

## Other Vercel projects that exist but weren't part of this session's work
`quantum-brain-sync-website` (×3 variants), `genixbank-financial-system`, `arbitrage-nexus`,
`pitch-kit`, `bw-001-up-next-web`, `civilization-os`, `ps-012-website-build`, `00-dashboard`,
`iza-os-enterprise`, `simple-landing`, `v0-integrations-page` — listed in Vercel, not verified
real/stale/placeholder this session.

## How "what's left" gets tracked
There's no automated readiness tracker — this table is manually maintained. The closest thing to
an automated signal is `venture-completion-ledger.json` (Documents root, built by
`build_venture_completion_ledger.py`) which pulls each repo's own `venture.json` — but that field
data has been shown to be unreliable (con-002 shows `has_code: true` despite having no actual app
code) so treat it as a lead to verify, not a source of truth.
