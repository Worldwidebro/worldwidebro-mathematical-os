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
