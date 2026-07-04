# Findings — Inventory & Migration Map (WORLDWIDEBRO-OS consolidation)

## Disposition codes
- **MOVE** = pure docs/markdown, physically relocate into canonical tree
- **REGISTER** = live git repo / running software → stays in place, gets a row in 08-DATA/registries (moving breaks .git + hardcoded paths)
- **FOLD** = competing OS/holdings doc-root → extract unique content into canonical layer, then retire husk
- **IGNORE** = build artifact (gitignored, left in place)
- **OUT** = not part of company OS → separate career/personal area
- **ARCHIVE** = stale/duplicate → ventures/archived

## Hard facts discovered
- 108 top-level dirs, ~384 loose root files (242 .md, 18 csv, 32 json, 44 py, 48 other)
- **41 embedded git repos** within 2 levels → those folders are live repos: REGISTER not MOVE
- No .gitignore existed (created); graphify-out=701M, node_modules=69M (IGNORE)
- Backup tag `backup-pre-os-migration` @ de982cf
- WORLDWIDEBRO-OS is part of main repo (safe build target); skeleton built = 164 dirs

## Competing OS / Holdings doc-roots → FOLD into canonical, then retire husk
| Folder | Folds into |
|--------|-----------|
| 00-OPERATING-SYSTEM .. 05-TEMP-AND-INBOX (numbered scheme) | split across 00–10 by content |
| OPERATING-SYSTEM, Worldwidebro-Operating-System, WORLDWIDEBRO-UNIFIED-OS | 00-DIRECTIVES + 02-GOVERNANCE |
| ai-boss-os, civilization-os-local, CON-OS-BUILD, staffing-os | 03-PORTFOLIO / 05-AGENTS |
| Influence-Venture-Business-OS | 02-GOVERNANCE + 07-KNOWLEDGE + 08-DATA (holds registries/venture-hub) |
| Worldwidebro-Holdings, worldwidebro-holdings-work, RE-001-Worldwidebro-Holdings | 02-GOVERNANCE/holdings |
| autonomous-venture-studio, ai-venture-studio-template, SecondBrain, The office, mission-control, MC-OPERATIONS | 04-OPERATIONS / 07-KNOWLEDGE |

## Live repos / infra → REGISTER in place (06-TECHNOLOGY/repositories + tools.csv)
supabase, grafana, nginx, migrations, LightRAG, RAG-Anything, composio, comfy, magika,
claude-code-proxy, vibetunnel, thunderbolt, omi, mcp-dashboard, portfolio-mcp,
MoneyPrinterTurbo, MoneyPrinterV2, TrendRadar, Miro-Fish, design-system x3, twenty-local-test,
iza-os, iza-os-marketing-core, iza-os-rag-system, agents-os, dexter, dexter-orchestrator

## Ventures → REGISTER (08-DATA/registries/ventures.csv); code stays as repo
ec-051-ai-email-marketing, edu-013-automated-empire-book, et-001-online-tutoring-platform,
fin-001-repo, fin-023-investment-portfolio-ai, fin-trading-stack, fin-ventures, genixbank-repo,
business-template-marketplace, marketplace-plumbing, marketplace-roofing, clip-farming-system,
STAFFING-AGENCY, pitch-kit, YES-LLC, YES-LLC-CONTRACTOR-DELIVERY-repo, Crucix, Azriel-Fathering-Content

## Knowledge/content → MOVE into 07-KNOWLEDGE (Obsidian vault registered, not moved)
books, docs, Knowledge Graph

## OUT (not company OS) → ~/Documents/_career/
antwuan-johns-job-search, career-ops, HIRING-PACKAGE-OPTION-D, WORKFORCE-PLANNING

## IGNORE (build artifacts, gitignored, left in place)
node_modules, __pycache__, integrations-venv, graphify-out (701M), moneyprinter-output,
lightrag_data, osint_results, generated-courses, backups

## Loose root .md (242) → MOVE by prefix
- CON-* (21) → 03-PORTFOLIO/opcos/CONSTRUCTION/
- SESSION-* (13), WAVE-* (3) → 10-STATUS/sessions/
- WORLDWIDEBRO-*, SYSTEM-*, OPERATING-* → 00-DIRECTIVES / 07-KNOWLEDGE
- FIN-*, TRADING-* → 03-PORTFOLIO/opcos/FINANCIAL/
- DUPLICATE-* (3) → delete after dedup confirm
- ORB-*, PHASE-*, SCALE-*, SKILLSLLM-* → 07-KNOWLEDGE/frameworks
- CAUTION: files referenced in CLAUDE.md/MEMORY.md (WORLDWIDEBRO-UNIFIED-COMPANY-ROADMAP-2026.md,
  ORB-MASTER-CONNECTOR-2026-06-11.md, SUPABASE-SQL-REFERENCE-OPTIMIZED.md) → moving requires
  updating those references in the same commit.

## Open risk
Hundreds of absolute /Users/acebless/Documents/X paths in CLAUDE.md + docker-compose.yml +
python scripts. Any MOVE of a referenced target must update the reference. This is why live
repos are REGISTER-in-place, not MOVE.

## Session 2026-07-02 — Infra & Capability-Graph Audit findings (verified live, not from docs)

**Docker (this Mac, `Mac.lan`):** neo4j, qdrant, redis, postgres, grafana all `Up 7 days (healthy)`
via `docker ps`. CLAUDE.md's "awaiting daemon start" line is stale.

**Neo4j graph (localhost:7474, auth neo4j/ventures2026) — populated:**
- Nodes: Repo 1701, Venture 712, Capability 25, Sector 18, OPCO 18, MCP 16, Skill 9, Entity 7
- Edges: NEEDS 6542 (Venture→Capability), IMPLEMENTS 2187 (Repo→Capability), BELONGS_TO 1008,
  IN_SECTOR 712, PROVIDES 22
- Full join `(Repo)-[IMPLEMENTS]->(Capability)<-[NEEDS]-(Venture)`: 1121 repos / 22 caps / 712
  ventures all resolve. This IS the "Repo→Capability→Venture" chain requested — already built.
- No `Workflow` node label exists — Venture→Workflow(n8n/ClickUp)→Revenue is the one real gap.

**Qdrant split-brain:**
- Local Docker (`localhost:6333`): collections = `notes`, `repositories` (2)
- Mac Studio (`100.87.214.70:6333`, Tailscale, reachable 9ms ping): collections = `notes`,
  `repositories`, `starred_repos`, `ventures` (4 — more complete)
- `os_env.py`/`retrieve.py`/`build_repo_rag.py` currently point at localhost — may be the stale copy.

**Tailscale:** aces-macbook-air-1 (this machine) + mac-studio (100.87.214.70, active/direct) online.
dexterslab, divines-imac, ipad-10th-gen offline (47-112d). No NAS/external volume mounted
(`/Volumes` = Macintosh HD only).

**OPCO structure (`registries/opcos.csv`):** 18 OPCOs, currently 1:1 with the 18 sectors
(E-COMMERCE=110 ventures ... REAL-ESTATE=1 venture). Not yet consolidated into fewer holding
companies — Neo4j has real OPCO nodes ready for a rollup pass whenever that's prioritized.

**Registry duplication (Phase 8.5 gap, confirmed still open):**
- Canonical: `WORLDWIDEBRO-OS/08-DATA/registries/` — capabilities-catalog.json (Jun 28, newest)
- Still-present duplicates (never archived):
  - `.../STRATEGY_LAYERS/WORLDWIDEBRO-OS/REGISTRIES/`: capabilities-taxonomy.json,
    components-registry.json, capability-component-repo-linkage.json (+ v2-REAL-NAMES),
    capability-definitions.json
  - Top-level `Documents/`: CAPABILITIES-INVENTORY.csv, CAPABILITIES-SUMMARY.csv,
    capability-gap-analysis.json, VENTURES-CAPABILITIES-CROSSREF.csv,
    VENTURES-CAPABILITIES-LIST.csv, VENTURES-CAPABILITIES-MAPPED.csv

**CLAUDE.md staleness found:** Docker "awaiting daemon start" (actually running); Grafana
documented as port 3000, actual compose mapping is `3001:3000`.

## Venture-file sprawl (2026-07-03, Phase 10.3) — sibling problem to registry duplication above

15 venture files exist at Documents root + `08-DATA/registries/`, not the ~2 assumed. Three
different ID schemes across them (`FIN-001`, `FIN-001-GenixBank-Lite`,
`TECH-001-Quantum-Algorithm-AI`), row counts drift (712/583/372/100) because each was
recomputed from scratch rather than extending one shared file.

| File | Rows | Verdict |
|------|------|---------|
| `VENTURES-CAPABILITIES-MAPPED.csv` | 712 | live — Holdings Playbook + vex-site source |
| `08-DATA/registries/ventures.csv` | 712 | live — vex-site source (opco column now fixed, 10.1) |
| `VENTURE-FACTORY-MAP.csv` | 712 | unused — `integration_pct` is NOT measured per venture, it's a fixed constant per archetype (fintech=83, market=80, infra/devtools/ai=100, con/re=60 — only 8 distinct values across 712 rows) |
| `venture-capabilities-proposed.csv` | 6,542 pairs | unused — real venture_id→capability pairs, never joined anywhere |
| `tech_ventures_registry.csv` | 61 | **unused, but 57/61 `repo_id` values are real repos already in REPOSITORY-REGISTRY.json** — a working venture↔repo link sitting idle, never merged into `related_ventures` |
| `ventures_updated_2026-05-15.csv` | 583 | stale — pre-dates current ID scheme |
| `ventures_16sector_classification.csv` | 372 | stale — superseded `Sector_7`/`Sector_16` dual taxonomy |
| `ALL-100-SCALE-VENTURES.csv` | 100 | misleading — "Repo 1-4" columns are generic category placeholders (only 7 distinct combos across 100 rows), not real repos |
| `MOBILE-VENTURES-CLASSIFIED.csv` | 182 | unused — orphaned mobile-specific slice |
| `VENTURES-ASSET-CLASSIFICATION.csv` | 30 | unused — investment scoring, never referenced elsewhere |
| `ventures_sector_summary/alignment_matrix/UNIT-ECONOMICS` csvs | 8-17 | fine — small rollup summaries |
| `VENTURE_INVENTORY_MASTER.csv` (`_superseded/`) | 704 | superseded |

Related: `duplicates-report.json` (root, generated 2026-06-28) already scored 1,597 repos and found
51 clusters / 305 repos (19%) as near-duplicates ≥90% similarity, with explicit keep/archive picks
— never executed. `execution-readiness.csv` (root) already scored 357 repos on dockerized/
has_license/mcp_compatible/production_ready (35 pass, 16 MCP-compatible) — never read downstream.
Both are the same pattern as the capability-registry duplication above: real analysis computed,
sitting unused, no "apply" step ever run.

## Venture completion — actual state (2026-07-03, Phase 10)

Checked directly, not assumed: **0 of 712 ventures have real frontend/backend code.** Only
`vex-hero-site` exists as an actual coded site/app anywhere in Documents, and it's the parent
Holdings brand site, not a venture. Stage breakdown: 542 `planned` (76%, name+sector only), 93
`mvp`/`development`, 72 `validation`, 5 `growth`/`active` (`FIN-036-Arbitrage-Nexus-Platform`,
`EC-044-Live-Commerce-Platform`, `EC-046-3D-Product-Viewer`, `EDU-017-AI-Coding-Tutor`,
`SPEC-032-AI-Game-Designer`). `SAAS-BACKEND-KIT-TEMPLATE.md` (04-OPERATIONS, built same day by the
parallel session) has zero proven instances — HRMS flagged as first candidate, not yet built.

## Two separate "playbook" outputs now exist — do not conflate

1. **`00-HOLDINGS-MASTER.pdf`** (`WORLDWIDEBRO-OS/08-DATA/portfolio-reports/output/`) — pre-existing,
   29 pages, OPCO layer + repo alignment, built via `generate_portfolio_pdfs.py` (reportlab, reads
   `VENTURES-CAPABILITIES-MAPPED.csv`). Zipped as `WORLDWIDEBRO-HOLDINGS-PLAYBOOK-2026-07-03.zip`.
   This is the polished, distributable deliverable. Not touched or regenerated by anything below.
2. **`03-PORTFOLIO/opcos/<OPCO>/PLAYBOOK.md` + `MASTER-PLAYBOOK.md`** (2026-07-02) — new, markdown,
   built via `generate_opco_playbooks.py` (reads `registries/ventures.csv` + live Neo4j capability
   graph). Working/analytical view (capability-coverage ranking per venture), not a replacement for
   the PDF pipeline — different source data, different purpose, different format.
