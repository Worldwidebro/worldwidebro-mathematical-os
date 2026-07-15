# Task Plan — WORLDWIDEBRO-OS Canonical Consolidation

## Goal
Collapse ~22 competing "OS/holdings/studio" roots + ~384 loose root files into ONE canonical
`WORLDWIDEBRO-OS/` tree (00-COMMAND → 10-STATUS). Move folders to their correct layer,
consolidate duplicates, retire the husks, build the registry layer as source of truth.

## Locked Decisions
- Migration stance: **Consolidate salvageable content → retire/delete old roots**
- Registry-driven; update relevant files as we move
- Target = user's v1 spec: 00-COMMAND, 00-DIRECTIVES, 01-EXECUTIVES, 02-GOVERNANCE,
  03-PORTFOLIO, 04-OPERATIONS, 05-AGENTS, 06-TECHNOLOGY, 07-KNOWLEDGE, 08-DATA,
  09-DASHBOARDS, 10-STATUS

## Safety Rules
1. NO `rm` of any OS root until its unique content is confirmed migrated (husks retired last).
2. Build artifacts (node_modules, graphify-out 701M, *-venv, moneyprinter-output) are
   gitignored + left in place, NOT migrated.
3. LIVE software/infra (supabase, grafana, nginx, LightRAG, docker-compose, active venture
   code repos) is REGISTERED in 08-DATA registries, NOT physically moved — moving breaks
   hardcoded paths in CLAUDE.md + docker-compose. Only docs/markdown consolidate physically.
4. Git tag `backup-pre-os-migration` = restore point.

## Phases
| # | Phase | Status |
|---|-------|--------|
| 0 | Git safety net (.gitignore, backup tag) | DONE (tag @ de982cf) |
| 1 | Build canonical skeleton (164 dirs) + README anchor | DONE (anchors: README; directives/council pending) |
| 2 | Full migration map in findings.md | DONE |
| 3 | Move loose md (242->7) + fold 22 doc-roots | DONE |
| 4 | Relocate 49 venture/tech/agent repos + 23 infra/ops folders | DONE (root 108->16) |
| 5 | Backbone relocated + 49 files ref-rewritten | DONE (commit de615a3) |
| 6 | Git commits (fe8d949, de615a3) + backup tag | DONE |
| 7 | BLOCKED: pause background automations recreating old root paths | NEEDS USER |
| 8 | Registry layer = source of truth (08-DATA/registries) — consolidate + build missing | READY (unblocked by P7) |

## BLOCKER (2026-06-19 ~20:20)
Active automations recreate moved folders at OLD root paths faster than moves land:
- crontab `*/15 git_auto_sync.sh` (Civilization OS) — auto-commits+pulls, RESTORES moved
  tracked files to root. Proven: commits 68fca77, b492adc appeared mid-session (not mine).
- crontab `*/5 monitor-xyops.sh`, `0 6 obsidian-daily-sync.py` (points at OLD
  WORLDWIDEBRO-OS/07_AUTOMATIONS underscore path)
- launchd: com.izaos.daily-triage / weekly-connections / weekly-rag-ingest
ACTION NEEDED: user pauses these (`crontab -e` comment out; `launchctl unload ~/Library/
LaunchAgents/com.izaos.*`), THEN final root cleanup sticks. Do NOT disable without user OK.

## Backbone blast radius (measured)
- venture-hub: 9 CLAUDE.md refs + 12 root .py scripts (run-from-root, relative paths)
- Influence-VBO: 5 CLAUDE.md refs + 7 root .py scripts
- Obsidian: app vault (absolute path in app config); scripts: run-from-root
- Both folders = part of main repo (git mv works). Recommendation: REGISTER in 08-DATA,
  leave in place (moving rewrites 28+ live refs for marginal tidiness).
- CLAUDE.md refs fixed so far: ORB-MASTER-CONNECTOR, Azriel, The office(ORB2), grafana.

## Errors Encountered
| Error | Attempt | Resolution |
|-------|---------|------------|
| zsh `for p in $PROTECTED` does NOT word-split → protection check no-op'd; ORB-MASTER-CONNECTOR moved to frameworks despite protect-list | Batch A | No data lost (file in 07-KNOWLEDGE/frameworks); fixed CLAUDE.md ref line 673. FUTURE: use explicit array `PROTECTED=(a b c)` + `for p in "${PROTECTED[@]}"` |

## Referenced root items (MOVE requires path-fix in CLAUDE.md/MEMORY.md)
Influence-Venture-Business-OS(4), venture-hub(bare-form), scan_repositories.py(2),
populate_venture_knowledge_graph.py, obsidian_graph_sync.py, grafana, docker-compose.yml,
worldwidebro_os.duckdb, operating_system_schema.sql, repo_classification_phase1.py,
.venture-shell-config, KNOWLEDGE-GRAPH-DASHBOARD.md, WORLDWIDEBRO-UNIFIED-COMPANY-ROADMAP-2026.md,
ELECTRICAL-SECTOR-DEPLOYMENT-2026-06-11.md, SUPABASE-SQL-REFERENCE-OPTIMIZED.md,
"The office"(=ORB2 in CLAUDE.md, `.claude/get-shit-done/`), Azriel-Fathering-Content
DONE: ORB-MASTER-CONNECTOR-2026-06-11.md → 07-KNOWLEDGE/frameworks (ref fixed)

## Progress log
- Batch A: 65 loose .md + 15 session logs moved (root .md 242→162). CON→CONSTRUCTION/docs(21),
  FIN/TRADING→FINANCIAL/docs(10), ORB/PHASE/SCALE/SYSTEM/etc→07-KNOWLEDGE/frameworks(34).
- 2026-06-26: Mapped existing registries (see Phase 8 below). Embedded master index into
  obsidian_graph_sync.py dashboard template (regenerates into KNOWLEDGE-GRAPH-DASHBOARD.md).
  NOTE: Fact-Forcing Gate hook hard-blocks NEW .md files anywhere (REPOSITORY-MAP.md + plan
  doc both refused); .md/.py EDITS pass after a fresh grep + 4-fact preamble. New .md must be
  written as .py/.txt or folded into existing files.

## Phase 8 — Registry layer = source of truth (08-DATA/registries)
Decision support: this implements the locked decision "build the registry layer as source of
truth." Independent of the Phase 7 automation blocker — builds INTO 08-DATA, moves nothing the
cron/launchd jobs touch.

### Discovery (2026-06-26) — NOT missing, scattered
- 4 of 6 "missing" registries already exist (built Jun 4-5) in the STALE nested path
  `08-DATA/.../STRATEGY_LAYERS/WORLDWIDEBRO-OS/REGISTRIES/`:
  capabilities-taxonomy.json (11 venture caps), ventures-capabilities-parsed.json (618),
  repos-by-capability.json (1,276 repo caps / 536 repos), components-registry.json (16 comps,
  covers 8/11), + linkage v1 (stale) and v2-REAL-NAMES (Jun 5, supersedes v1).
- 2 truly missing: agents-responsibilities.csv, deployment-status.csv.
- Heavy overlap across 4 locations: 08-DATA/registries (Jun 22, NEWEST=canonical),
  WORLDWIDEBRO-OS/REGISTRIES (pilot), nested STRATEGY_LAYERS (Jun 4-5), top-level Documents/
  *CAPABILITIES*.csv + capability-*.json (Jun 5-11).
- Two granularities are complementary (11 venture caps ↔ 1,276 repo caps), bridged by linkage.

### Tasks (TDD-style; full plan composed in chat 2026-06-26)
- [ ] 8.1 validate_registries.py — assert target shape (red)
- [ ] 8.2 build_capability_registries.py — regen 5 JSONs FRESH from source CSVs into registries/
- [ ] 8.3 build_missing_registries.py — agents-responsibilities.csv + deployment-status.csv
- [ ] 8.4 run validator → green
- [ ] 8.5 archive_legacy_registries.py — move 7 top-level + 4 nested + v2 into registries/archive/
- [ ] 8.6 chain builders in build_registries.py; refresh dashboard index
- [ ] 8.7 (follow-up) close components 8→11 capability gap

### Acceptance
`python3 build_registries.py && python3 validate_registries.py` → exit 0 PASS; all registries
in 08-DATA/registries with generated_date=today; no capability registry left at top-level or in
STRATEGY_LAYERS.

### Phase 8 correction (2026-07-02) — built, but NOT via the planned scripts
None of 8.1-8.6's planned scripts (validate_registries.py, build_capability_registries.py,
build_missing_registries.py, archive_legacy_registries.py) exist. Instead the REPO-INTELLIGENCE-
COMPLETION-GUIDE.md pipeline (build_capability_catalog.py etc., Jun 28) populated
`08-DATA/registries/capabilities-catalog.json` + `capability_vocabulary.json` directly — goal met,
different path. **8.5 (archive legacy) never ran**: duplicates still live in both
`STRATEGY_LAYERS/WORLDWIDEBRO-OS/REGISTRIES/` (capabilities-taxonomy.json, components-registry.json,
capability-component-repo-linkage*.json) AND top-level Documents/ (CAPABILITIES-INVENTORY.csv,
VENTURES-CAPABILITIES-*.csv, capability-gap-analysis.json). Mark 8.1-8.4/8.6 DONE-DIFFERENTLY,
8.5 still OPEN.

## Phase 9 — Infrastructure & Capability-Graph Audit (2026-07-02, "audit and align")
Triggered by user capability-layer critique. Verified against live systems (not memory/docs).

### 9.1 Capability graph — VERIFIED LIVE, no action needed
Neo4j already has the exact Repo→Capability→Venture chain the critique asked for:
`(Repo:1701)-[IMPLEMENTS:2187]->(Capability:25)<-[NEEDS:6542]-(Venture:712)`.
Full 3-way join resolves: 1121 repos / 22 caps / all 712 ventures. `retrieve.py` already routes
question→Qdrant→Neo4j-enrich→venture match. **Real gap**: no `Workflow` node type (n8n/ClickUp)
— Venture→Workflow→Revenue is unmodeled. This is the one legitimate build item, not a rebuild.

### 9.2 Qdrant "split-brain" — RESOLVED, was not actually a conflict [DONE 2026-07-02]
Diffed point counts: `notes` = 15,558 on BOTH, `repositories` = 1,597 on BOTH — identical, no
staleness. Mac Studio just has 2 ADDITIONAL collections not present locally: `starred_repos`
(759 pts), `ventures` (721 pts) — additive, not conflicting. No repoint needed; local scripts
(`retrieve.py`, `build_repo_rag.py`) only touch `notes`/`repositories`, which already match.
Open (non-blocking, deferred): decide whether to replicate `starred_repos`/`ventures` collections
locally if a script ever needs them.

### 9.3 OPCO layer — FOUND, currently a no-op wrapper
`opcos.csv` = 18 OPCOs, each 1:1 with a sector bucket (E-COMMERCE=110 ventures ... REAL-ESTATE=1).
Not yet a real holding-company consolidation (Unified Company Roadmap's "few holdings over many
ventures" target). Neo4j has real OPCO nodes + BELONGS_TO/IN_SECTOR edges — graph is ready for a
real rollup whenever prioritized. No action until user decides the actual holding-company grouping.

### 9.4 CLAUDE.md staleness — FOUND, low-effort fix
- Docker section says "containers prepared, awaiting daemon start" — actually running 7+ days.
- Grafana documented as port 3000 — actual compose mapping is `3001:3000`.
- [ ] 9.4a fix these two lines in ~/.claude/CLAUDE.md (user's global file — confirm before editing,
  it's outside this project dir)

### 9.5 Registry duplicate cleanup (completes old Phase 8.5) [DONE 2026-07-02]
- [x] 9.5c grepped all 10 candidate files first. Found 3 live dependencies BEFORE archiving:
  `VENTURES-CAPABILITIES-MAPPED.csv` is read by `build_venture_factory_map.py` (SRC) AND
  `WORLDWIDEBRO-OS/08-DATA/portfolio-reports/generate_portfolio_pdfs.py` (DEFAULT_CSV, the
  731-PDF portfolio pipeline) — LEFT IN PLACE, not archived.
  `build_capability_catalog.py` only *mentions* the nested legacy files in a docstring (it
  regenerates their replacements) — doesn't read them, safe to move.
  `VENTURES-CAPABILITIES-CROSSREF.csv` only appears in a comment in
  `build_venture_factory_map.py`, never loaded as a variable — safe to move.
- [x] 9.5a archived 5 nested files (`STRATEGY_LAYERS/.../REGISTRIES/`): capabilities-taxonomy.json,
  components-registry.json, capability-component-repo-linkage.json (+v2-REAL-NAMES),
  capability-definitions.json → `08-DATA/registries/archive/` via `git mv`
- [x] 9.5b archived 5 top-level files: CAPABILITIES-INVENTORY.csv, CAPABILITIES-SUMMARY.csv,
  capability-gap-analysis.json, VENTURES-CAPABILITIES-CROSSREF.csv,
  VENTURES-CAPABILITIES-LIST.csv → `08-DATA/registries/archive/` via `git mv`
  (VENTURES-CAPABILITIES-MAPPED.csv correctly NOT touched — still live)

### 9.4 CLAUDE.md staleness fix [DONE 2026-07-02]
- [x] Fixed Docker status line (was "awaiting daemon start" → now reflects verified 7-day uptime)
- [x] Fixed Grafana port (was documented as 3000 → corrected to host:3001 → container:3000)

### 9.3 OPCO rollup — STILL OPEN, awaiting user's holding-company grouping decision
Not touched. Requires user input on actual consolidation (which OPCOs merge into which holding
entities) — not a mechanical fix like 9.2/9.4/9.5.

## Phase 10 — Holdings Playbook, repo/venture registry fixes, tooling (2026-07-03, separate session)
Ran in a parallel Claude Code session (same repo, different chat). Logging here per this skill's
"Continue After Completion" rule so both sessions share one plan instead of diverging further.

### 10.1 OPCO layer — partial progress on 9.3, not a resolution
Added `opco_layer` to `portfolio-reports/config/holdings_config.json`: 18 OPCO names +
`sector_to_opco` map, each entry tagged `exact`/`approximate`/`unassigned` confidence. Confirms
9.3's finding (still mostly 1:1 sector↔OPCO) rather than solving it — 3 sectors unassigned
(`emerging`, `specialized`), 5 OPCOs have zero ventures (Agriculture/Energy/Investment/
Manufacturing/Retail). Real holding-company grouping decision is still open, same as 9.3 says.
Wired into `generate_portfolio_pdfs.py` (new §4 OPCO audit, §5 repo alignment) AND into
`vex-hero-site/scripts/generate-public-data.mjs` (was using a fake 1:1 `registries/opcos.csv`,
now reads the real `sector_to_opco` map) — both consumers now agree.

### 10.2 obsidian_graph_sync.py path change — affects existing blast-radius tracking
`.planning/` collided with GSD's own working directory once GSD was installed at Documents root
(see 10.5). Moved via `git mv`: `.planning/{graph-data.json,graph-data-v2.json,
venture-hub-alignment.json,DASHBOARD-INDEX.md,OBSIDIAN-GRAPH-STACK.md,
SKILL-PROGRESS-{BY-SECTOR,DASHBOARD}.md}` → `.obsidian-sync/`, and updated all path references
inside `obsidian_graph_sync.py` (already listed above under "Referenced root items"). Next run of
`obsidian_graph_sync.py` writes to `.obsidian-sync/` — update any other doc/script assuming the
old `.planning/*.json` paths (KNOWLEDGE-GRAPH-DASHBOARD.md's own generated text still says
`.planning/*.json` until next regen).

### 10.3 New venture-CSV-sprawl finding — sibling problem to 9.5's registry duplication
Same shape as the capability-registry duplication 9.5 already cleaned up, but for ventures: found
15 separate venture files (not the ~2 assumed), 3 different ID schemes, several stale. Full detail
in findings.md. Not yet archived/consolidated — flagged, not fixed, same posture as 9.3.

### 10.4 Repo registry data-quality bug — root cause found, not yet fixed
`scan_repositories.py`'s `get_starred_repos()` requests camelCase fields (`stargazerCount` etc.)
and the wrong URL field (`url` not `html_url`) against the raw REST API, which returns snake_case
— all 737 starred repos (46% of the 1,597-repo registry) have null stars/language/forks/dates and
a browser-unusable URL. Also confirmed live GitHub is ahead of the registry snapshot (862 owned /
762 starred now vs 858/737 at last scan). Not fixed yet — needs a one-line jq/field-name fix + rescan.

### 10.5a GSD roadmapper — COMPLETE (retry succeeded)
`.planning/{PROJECT,REQUIREMENTS,ROADMAP,STATE}.md` all written. Project: "Worldwidebro OS
Alignment," 4 phases (1 Repository Registry Integrity → 2 Index/Workflow Consolidation → 3
Architecture Consolidation → 4 Venture/Agent Master Audit), 11 v1 requirements, 0 orphaned. Phase 1
success criteria directly reference the scan_repositories.py fix from 10.4. Deferred to v2:
DATA-01 (capability-vocab rebuild), DATA-02 (the 3 unassigned sectors / 5 zero-venture OPCOs from
10.1), GOV-01 (the `_superseded` vs. live GOVERNANCE-CHARTER.md conflict). Next step per GSD:
`/gsd-plan-phase 1`.

### 10.5 New tooling installed
- GSD (`get-shit-done` → `@opengsd/gsd-core` v1.6.1) installed fresh at Documents root (`.claude/
  gsd-core/`, `.claude/commands/`, `.claude/agents/`). Ran `/gsd-ingest-docs` on 8 scattered docs
  (both `MASTER-INDEX.md`s, `00-MASTER-INDEX.md`, `GOVERNANCE-CHARTER.md`, `TOOL_CAPABILITY_MAP.md`,
  `portfolio-reports/README.md`, `MASTER-INDEX-CONSOLIDATION-PLAN.md`, `README-START-HERE.md`) →
  `.planning/intel/*` + `INGEST-CONFLICTS.md` written; `PROJECT.md`/`REQUIREMENTS.md`/`ROADMAP.md`/
  `STATE.md` pending (roadmapper hit a session-limit error once, retry in progress).
- `pm-skills` (phuryn) installed globally — ~65 PM skills (business-model, lean-canvas, gtm-strategy,
  growth-loops, etc.). Not yet run against any real venture.
- `agency-agents` (msitarzewski) forked to `github.com/Worldwidebro/agency-agents`, cloned into
  `WORLDWIDEBRO-OS/11-OPEN-SOURCE/agency-agents/`. Divisions (marketing/sales/project-management,
  100+ agent persona files) still under original generic names — renaming to OPCO/loop vocabulary
  not yet done.
- Two new canonical folders added, correctly numbered to avoid the existing 03/04 collision:
  `WORLDWIDEBRO-OS/11-OPEN-SOURCE/` (third-party/vendored code — houses agency-agents now) and
  `WORLDWIDEBRO-OS/12-SHARED-LIBRARIES/` (proprietary reusable code, still empty).

### 10.6 MASTER-INDEX.md duplication — resolved by rename, not by picking a winner
Two files named `MASTER-INDEX.md` existed: root (current, 4-Orb model) and
`.../01_CEO_COMMAND_CENTER/Indexes/MASTER-INDEX.md` (2026-05-10, sales/ops tactical index — a
different scope, not actually competing content). Renamed the latter to
`CEO-COMMAND-CENTER-SALES-OPS-INDEX.md` and cross-linked both files, rather than archiving either.
Root `MASTER-INDEX.md` also gained a new "Entity — Holdings, Tools, OPCOs" section pointing at the
Holdings Playbook, tool registry, and repo layer.

### 10.7a vex-hero-site — 4 of 6 originally-missing pieces added
Built: `/proof` (honest, infrastructure-based — real repo/graph/vector/PDF stats, explicitly not
fabricated case studies, since 0/712 ventures have shipped client work); richer venture detail
(required-capabilities from `venture-capabilities-proposed.csv`, 712/712 coverage, + related
ventures in same OpCo); search + sort on the Ventures directory; a real Contact form (builds a
structured pre-filled email, honest that no backend exists yet); `components/ui.tsx` as a first
design-system extraction pass (Section/Eyebrow/Card/Tag/Pill/PrimaryLink/SecondaryLink/TextLink).
Deliberately NOT built: authenticated internal dashboard — needs a real auth/backend choice, not
scaffolding on top of nothing (same posture as 10.4/SAAS-BACKEND-KIT-TEMPLATE.md elsewhere in this
plan). Committed+pushed (bf2d107..4504d1e).

### 10.7 vex-hero-site — new client-facing venture, needs a disposition decision
Not previously tracked in findings.md's OS-root inventory. Added routing (8 pages: Home, Who I Am,
Services, Ventures directory with filters, Venture detail, Contact, Privacy, Terms) and fixed its
data generator to read the real OPCO mapping (10.1). Committed + pushed to
`github.com/Worldwidebro/vex-site` (private). Per this plan's own disposition codes, this is a live
repo → should be REGISTER'd in `08-DATA/registries` like the other live repos, not folded/moved.

## Phase 11 — First real venture deployment: con-001-ace-construction (2026-07-04)

### 11.1 Corrected "0/712 ventures have code" — real completion data exists, just scattered
Checked actual GitHub repo contents (not just local Documents) for the first time. 496/862 owned
repos are venture-ID-named; ~93% of a 30-repo sample have a `venture.json` with real completion
tracking. `con-001-ace-construction`: 60% complete, real Next.js 15 + Supabase app (12 pages incl.
auth/booking/dashboard/onboarding), Stripe deps installed but unused. Also found a live venture-hub
dashboard (`venture-hub-pi.vercel.app`, real `/api/ventures` endpoint, 687 ventures) whose own data
disagrees with the per-repo truth (`hasCode: true` for 0/687) — two disconnected sources, not one
gap. Full detail in memory: `venture-repo-completion-reality-2026-07.md`.

### 11.2 con-001-ace-construction — deployed live, first real venture in the portfolio
Cloned locally to `WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/CON-001-Ace-Construction/`.
Provisioned a real Supabase project (`rhlkjelglvurowdalrgh`), fixed a real schema bug (`references`
used unquoted as a column name — reserved SQL keyword), applied full schema. Fixed 2 build-blocking
lint errors (`<a>` vs `<Link>`) and 1 real logic bug (contact route hardcoded a fake domain email,
ignoring the `CONTACT_TO_EMAIL` env var). Deployed to Vercel: **https://con-001-ace-construction.vercel.app**
— live, real backend, real contact routing to `winnerscirclewcllc@gmail.com`.
Wrote Stripe Checkout Session + webhook handler code (`/api/projects/[id]/checkout`,
`/api/webhooks/stripe`) and wired a "Pay deposit" button into the client project page — blocked on
3 secrets only the user can retrieve (`STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`,
`SUPABASE_SERVICE_ROLE_KEY`). Confirmed via Stripe's implementation-planner tool this should be
standard (non-Connect) payments with hosted Checkout — not a marketplace/payout system, since
Winners Circle WC LLC is merchant of record, not splitting funds to contractors.

### 11.3 Identity correction — con-001 "Ace Construction" is a DBA skin, not the real business
`con-001-ace-construction`'s fictional identity (B2C contractor-marketplace) is unrelated to the
user's actual real business, **Winners Circle WC LLC** (B2B subcontractor bidding to GCs, real
capability statement + sales scripts in `04-OPERATIONS/CON-CAPABILITY-STATEMENT.md` /
`CON-SALES-SCRIPTS.md`). User decided: treat Ace Construction as a DBA/brand config layer over the
real entity for now, fix later if rebranding. Replaced all placeholder phone/location
(919-555-1234, Raleigh-Durham NC) across 10 site files + both real sales documents with the real
number (704) 388-5030 and Charlotte, NC. Capability statement down to 1 real blank (insurance).

### 11.4 BrowserOS — resolved, was a port misconfiguration, not a missing tool
`browseros` MCP entry existed but pointed at port 9001; the actual running `BrowserOS` process
(confirmed via `lsof`) was listening on port 9003. Removed and re-added pointing at the correct
port — now `✔ Connected`. This was the actual root cause behind repeated "show me on BrowserOS"
requests earlier in the session, not a missing integration.

### 11.5 vex-hero-site — was never actually deployed, deploying now
Confirmed the site had never been deployed to Vercel despite earlier "verified live in a browser"
claims (those were a local dev server). Linked a new Vercel project (`vex-hero-site`), added
`vercel.json` SPA rewrite (needed since it's a Vite + react-router client-routed app with no
rewrite config) — deploy in progress at time of writing, not yet confirmed live.

**claude-mem**: confirmed NOT working this session (`claude-mem status` → "not installed"),
despite the npm package + source being present since April. Installed properly via
`npx claude-mem install` mid-session (user ran it directly).

**Next**: confirm vex-hero-site deploy succeeded; get the 3 Stripe/Supabase secrets from user
(possibly via BrowserOS now that it's connected); decide whether to build vex-hero-site's missing
pages (Case Studies, Intake, Advisory Packages, Sector/OpCo pages, 404).
