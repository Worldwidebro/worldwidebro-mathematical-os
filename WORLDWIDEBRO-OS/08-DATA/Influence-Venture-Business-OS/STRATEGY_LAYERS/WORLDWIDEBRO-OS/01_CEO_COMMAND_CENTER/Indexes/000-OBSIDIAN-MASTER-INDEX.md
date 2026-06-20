---
tags: [index, system, obsidian, master-catalog]
created: 2026-05-25
updated: 2026-05-25
---

# Obsidian Master Index — Worldwidebro Holdings

## Overview
Centralized semantic index for 150+ scattered files in ~/Documents. All files tagged by domain, venture, layer, and execution phase. Cross-links enable discovery via Dataview queries.

---

## 🏛️ DOMAIN TAXONOMY (8 Core Domains)

### [1. VENTURES & CLASSIFICATION](##ventures--classification)
- Venture definitions, tier systems, classification logic
- Taxonomy: venture_id, sector, tier (1-5), department, revenue_model
- **Files:** `VENTURE-*.md`, `VENTURE-DEFINITIONS.md`, `ventures_*.csv/json`

### [2. HRMS (Payroll SaaS)](##hrms-payroll-saas)
- HRMS venture execution: marketing, sales, tech stack, competitors
- Status: Phase 1 MVP (May 12-27), $3-5K MRR target
- **Files:** `HRMS-*.md`, `HRMS-*-integration.md`, `hrms.md`, `hrms-integrations-config.json`

### [3. AGENT SYSTEMS & AUTONOMY](##agent-systems--autonomy)
- Agent decision loops, conflict remediation, swarm runners
- Runtime repository manifest declaring dependencies, permissions, startup sequence
- 553 autonomous agents across 687 ventures, 7 core repos
- **Files:** `AGENT-*.md`, `AOC-*.md`, `*-AUTONOMY*.md`, `DEXTER-*.md`, `REPO_REGISTRY.json`

### [4. KNOWLEDGE GRAPH & INTELLIGENCE](##knowledge-graph--intelligence)
- LightRAG integration, Obsidian sync, semantic search, graph visualization
- Status: Phase 1B complete (Task 13), ready for agent integration
- **Files:** `*-GRAPH*.md`, `LIGHTRAG-*.md`, `IMPLEMENTATION-MAP-*.md`, `*-knowledge-graph*.json`

### [5. OPERATIONS & EXECUTION](##operations--execution)
- Daily execution, blockers, checklists, operational architecture
- Phase progression, readiness assessments, deployment guides
- **Files:** `*-EXECUTION*.md`, `BLOCKERS-*.md`, `OPERATIONS-*.md`, `PHASE-*.md`, `TASK-*.md`

### [6. INTEGRATIONS & TOOLS](##integrations--tools)
- ClickUp CRM, Composio, ClassBuild, Backstage, Paperclip, n8n
- Setup guides, configuration schemas, deployment plans
- **Files:** `*-INTEGRATION*.md`, `*-SETUP*.md`, `*CLICKUP*.md`, `*COMPOSIO*.md`

### [7. DATA & RESEARCH](##data--research)
- Starred repos, capabilities, contact extraction, sector analysis
- CSV/JSON: ventures, repos, contacts, sector gaps
- **Files:** `*-DATA*.md`, `starred*.csv/json`, `ventures*.csv/json`, `contacts*.csv`
- **AI Boss repo OS:** `AI-BOSS-HOLDINGS-REPO-OPERATING-SYSTEM.md`, `STARRED-REPOS-INSTALLATION-PRIORITY.csv`, `RAG-INGESTION-MANIFEST.csv`

### [8. STRATEGIC & PLANNING](##strategic--planning)
- Framework alignment, system architecture, decision trees, long-term strategy
- Business model docs, capital systems, financial logic
- **Files:** `*-FRAMEWORK*.md`, `*-STRATEGY*.md`, `*-ARCHITECTURE*.md`, `UNIFIED-*.md`, `REPO_REGISTRY.json`

---

## 🔗 CROSS-DOMAIN CONNECTIONS (Queries)

### By Execution Phase
```
Phase 0 (Complete):
- Core architecture (UNIFIED-KNOWLEDGE-GRAPH-OS-v1.md)
- Knowledge graph (PHASE-1B-COMPLETE, Task 13)
- CRM integration (CRM-SYSTEM-INTEGRATED, May 16)

Phase 1A (Complete):
- Agent autonomy (Task 9-11, AGENT-AUTONOMY-READY-2026-05-11.md)
- HRMS MVP code (May 12-27)
- Obsidian sync (TASK-14-OBSIDIAN-SYNC-COMPLETE)

Phase 1B (In Progress):
- 25-layer framework application
- API route creation (/app/api/ventures/[id]/route.ts)
- Field population (Phase 1-3 per FRAMEWORK-ALIGNMENT-MAP.md)

Phase 2 (Planning):
- Scale to 712 ventures (complete)
- Full agent deployment
- Capital system execution
```

### By Venture Lifecycle
```
Discovery → Classification → Execution → Growth → Exit
├─ Ventures: VENTURE-DEFINITIONS.md, ventures_classification_final.csv
├─ HRMS: HRMS-EXECUTION-START.md → HRMS-ACQUISITION-PIPELINE.md → HRMS-30-DAY-MARKETING-PLAN.md
└─ All: See ventures_master_with_sectors.csv (712 ventures, 20 sector prefixes, complete)
```

### By Technical Stack
```
Frontend:     Obsidian, React (TSX), Vite
Backend:      Node.js, PostgreSQL (Supabase), LightRAG
Agents:       Composio, Paperclip, n8n, VAPI
Data:         SocratiCode, Graph DB (Neo4j), Chroma
```

---

## 📊 FILE INVENTORY BY DOMAIN

### Ventures & Classification
| File | Type | Records | Tags |
|------|------|---------|------|
| ventures_classification_final.csv | CSV | 712 ventures | tier, department, sector, revenue_model (reconciled) |
| ventures_with_capabilities.csv | CSV | - | capability_score, confidence |
| ventures_master_with_sectors.csv | CSV | 712 ventures | id, name, sector, stage, status, uuid (authoritative) |
| VENTURE-CLASSIFICATION-BRIDGE.csv | CSV | 712 ventures | bridge 629→712, legacy mapping, classification alignment |
| ventures_tier_classified_option_a.json | JSON | tiered | tier, complexity, roi |
| VENTURE-DEFINITIONS.md | Doc | conceptual | framework, vocabulary |
| VENTURE-OPERATIONS-FRAMEWORK.md | Doc | strategic | 7-tier system, 4-layer capital |

### HRMS (Payroll SaaS Venture)
| File | Type | Status | Key Metrics |
|------|------|--------|------------|
| HRMS-EXECUTION-START.md | Doc | May 12 start | blockers, timeline |
| HRMS-ACQUISITION-PIPELINE.md | Doc | pipeline | leads, conversion, pricing |
| HRMS-30-DAY-MARKETING-PLAN.md | Doc | marketing | channels, messaging, targets |
| HRMS-COMPETITOR-ANALYSIS.md | Doc | research | payroll competitors, positioning |
| HRMS-SALES-SCRIPT-*.md | Doc | scripts | discovery, qualification, closing |
| HRMS-TECH-STACK-INTEGRATION.md | Doc | architecture | Composio, APIs, workflows |
| HRMS-MARKETING-STRATEGY.md | Doc | strategic | brand, positioning, GTM |
| HRMS-BLOCKER-1-CPA-PREP.md | Doc | execution | CPA, payroll logic, regulations |
| HRMS-BLOCKER-2-DISCOVERY-CALLS.md | Doc | execution | outreach, qualification, leads |

### Agent Systems & Autonomy
| File | Type | Focus | References |
|------|------|-------|-----------|
| AGENT-REPO-RESPONSIBILITY.csv | CSV | mapping | 16 agents, 595 aligned repos, 20 sector prefixes |
| PRIVATE-REPOS-ACCESS-CONTROL.csv | CSV | governance | 853 repos, ownership matrix, access control |
| AGENT-DECISION-LOOPS.md | Doc | logic | revenue optimization, cost control |
| AGENT-SYSTEM-PROMPTS.md | Doc | prompts | decision framework, escalation |
| AGENT-CONFLICT-REMEDIATION.md | Doc | ops | dispute resolution, workflows |
| AOC-SWARM-RUNNER.md | Doc | execution | batch processing, task queues |
| DEXTER-*.md | Doc | orchestrator | financial, data sources |

### Knowledge Graph & Intelligence
| File | Type | Status | Integration |
|------|------|--------|------------|
| IMPLEMENTATION-MAP-RAG-OBSIDIAN-GRAPH.md | Doc | complete | LightRAG + Obsidian + Supabase |
| LIGHTRAG-INTEGRATION-PLAN.md | Doc | deployed | 17 entities, 3 relationships |
| LIGHTRAG-SUPABASE-SETUP.md | Doc | live | sync pipeline, graph export |
| KNOWLEDGE-GRAPH-DASHBOARD.md | Doc | live | Dataview queries, Obsidian UI |
| KNOWLEDGE-GRAPH-VISUAL.md | Doc | visual | graph viz, entity connections |
| VENTURE-SHARED-SERVICES-MAPPING.csv | CSV | live | 712 ventures→4-12 shared services, cost allocation |
| VENTURE-RESOURCE-DEPENDENCIES.csv | CSV | live | 712 ventures linked to shared services + infrastructure |

### Operations & Execution
| File | Type | Scope | Phase |
|------|------|-------|-------|
| BLOCKERS-EXECUTION-2026-05-13.md | Doc | 4 parallel blockers | May 12-15 |
| EXECUTION-CHECKLIST-MAY-11.md | Checklist | go-live | Phase 0 closure |
| PHASE-1-DEPLOYMENT-GUIDE.md | Doc | deploy steps | Phase 1 |
| PHASE-1-READY-TO-DEPLOY.md | Doc | readiness | go-no-go |
| SYSTEM-LAUNCH-QUICKSTART.md | Doc | launch | day-1 operations |
| MAY-14-EXECUTION-BRIEFING.md | Doc | briefing | status, next steps |

### Integrations & Tools
| File | Type | Tool | Status |
|------|------|------|--------|
| CLICKUP-SETUP-GUIDE.md | Doc | ClickUp | configured |
| CLICKUP-PIPELINE-SETUP.md | Doc | ClickUp CRM | pipeline live |
| COMPOSIO-SETUP-GUIDE.md | Doc | Composio | agents ready |
| COMPOSIO-TASK-EXECUTION-STATUS.md | Doc | Composio | task mapping |
| CLASSBUILD-SETUP-COMPLETE.md | Doc | ClassBuild | vendor training |
| PAPERCLIP-DEPLOYMENT-PLAN.md | Doc | Paperclip | email automation |
| OPENVOLO-INTEGRATION-GUIDE.md | Doc | OpenVolo | outreach system |
| BACKSTAGE-INTEGRATION-SETUP.md | Doc | Backstage | service mesh |

### Data & Research
| File | Type | Records | Tags |
|------|------|---------|------|
| starred_repos_664.csv | CSV | 664 repos | language, stars, topics |
| STARRED-REPOS-INSTALLATION-PRIORITY.csv | CSV | 664 repos | install priority, phase, governance, repo OS |
| STARRED-REPOS-GOVERNANCE.csv | CSV | 664 repos | sectors, managers, venture relationships |
| STARRED-REPOS-MONITORING-WORKFLOW.md | Doc | workflow | upstream monitoring, alerts, review cadence |
| AI-BOSS-HOLDINGS-REPO-OPERATING-SYSTEM.md | Doc | architecture | Warp workspaces, repo groups, install backbone |
| RAG-INGESTION-MANIFEST.csv | CSV | 4 sources | authoritative RAG ingestion registry |
| starred_repos_with_capabilities.csv | CSV | capability map | language, capabilities |
| starred-repos-full.json | JSON | 664 repos | full metadata |
| socraticode_profiles.json | JSON | semantic | 18 repos, 13 capabilities |
| contacts-extracted.csv | CSV | contact records | names, titles, companies |
| sector_gaps_and_recommendations.csv | CSV | 16 sectors | coverage, gaps, recs |
| UNALIGNED-REPOS-CATEGORIZATION.csv | CSV | 258 repos | infrastructure, shared_services, templates, experimental |
| sector_repo_mapping.csv | CSV | sector→repos | domain mapping |

### Strategic & Planning
| File | Type | Scope | Framework |
|------|------|-------|-----------|
| UNIFIED-KNOWLEDGE-GRAPH-OS-v1.md | Doc | OS architecture | 7-layer system |
| VENTURE-OPERATIONS-FRAMEWORK.md | Doc | vocabulary | 7-tier classification |
| PERSONAL-VENTURES-UNIFIED-PLAN.md | Doc | life + ventures | integrated planning |
| SYSTEM-INTEGRATION-MAP.md | Doc | architecture | dependencies, dataflow |
| OPERATIONAL-ARCHITECTURE.md | Doc | ops design | roles, responsibilities |

---

## 🔍 DISCOVERY PATTERNS

### By Tag (Dataview Queries)
```
#hrms → All HRMS-related documents
#phase-1-a → Phase 1A execution files  
#venture-id-bw-001 → BW-001 Lash Extension studio files
#blocker → Current blockers
#integration → Third-party tool integrations
#csv/json → Raw data files
```

### By Relationship
```
HRMS (venture)
├─ Execution: HRMS-EXECUTION-START.md
├─ Blockers: HRMS-BLOCKER-1-*.md, HRMS-BLOCKER-2-*.md
├─ Sales: HRMS-ACQUISITION-PIPELINE.md, HRMS-SALES-SCRIPT-*.md
├─ Marketing: HRMS-MARKETING-STRATEGY.md, HRMS-30-DAY-MARKETING-PLAN.md
├─ Tech: HRMS-TECH-STACK-INTEGRATION.md, hrms-integrations-config.json
├─ Competitors: HRMS-COMPETITOR-ANALYSIS.md
└─ Research: sector_gaps_and_recommendations.csv

Agent System
├─ Assignments: AGENT-REPO-RESPONSIBILITY.csv (16 agents→595 repos by sector)
├─ Governance: PRIVATE-REPOS-ACCESS-CONTROL.csv (853 repos ownership)
├─ Autonomy: AGENT-AUTONOMY-READY-*.md
├─ Decision: AGENT-DECISION-LOOPS.md
├─ Prompts: AGENT-SYSTEM-PROMPTS.md
├─ Swarms: AOC-SWARM-RUNNER.md
└─ Orchestration: DEXTER-*.md

Knowledge Graph
├─ Graph: ventures_master_with_sectors.csv (712 entities + connections to 853 repos)
├─ Bridge: VENTURE-CLASSIFICATION-BRIDGE.csv (legacy 629→712 mapping)
├─ Services: VENTURE-SHARED-SERVICES-MAPPING.csv (712 ventures→shared services)
├─ Resources: VENTURE-RESOURCE-DEPENDENCIES.csv (ventures→infrastructure repos)
├─ Governance: PRIVATE-REPOS-ACCESS-CONTROL.csv (853 repos ownership matrix)
├─ Integration: LIGHTRAG-*.md
├─ Obsidian: IMPLEMENTATION-MAP-RAG-*.md
└─ Dashboard: KNOWLEDGE-GRAPH-DASHBOARD.md
```

---

## 📋 NEXT ACTIONS

### Phase 4 (Index & Integration) — Complete ✅
1. ✅ **Index new 6 CSV files**: Updated 000-OBSIDIAN-MASTER-INDEX.md
2. ✅ **Supabase schema integration**: Repo entities ready for graph_entities table
3. ✅ **Retire stale MASTER-INDEX.md**: 000-OBSIDIAN-MASTER-INDEX.md is authoritative

### Phase 5 (REPO_REGISTRY Wiring) — In Progress
1. 🔄 **Consolidate REPO_REGISTRY.json**: 7 repos + agent_name_map + local_path/github_repo fields
2. 🔄 **Populate ventures_served**: PRIVATE-REPOS-ACCESS-CONTROL.csv updated with repo→venture mappings
3. 🔄 **Add Repo entities to Supabase**: Insert 7 Repo nodes + Repo→Venture edges
4. 🔄 **Sync to Obsidian**: Repo entities now queryable in KNOWLEDGE-GRAPH-DASHBOARD.md
5. ⏳ **Commit to Documents + civilization-os-local**: Registry wiring complete, files committed

### Phase 6 (Agent Activation) — Pending
1. **Wire agent assignments**: Load AGENT-REPO-RESPONSIBILITY.csv into agent decision loop
2. **Cost allocation**: Use VENTURE-SHARED-SERVICES-MAPPING.csv in P&L calculation
3. **Access control sync**: Push PRIVATE-REPOS-ACCESS-CONTROL.csv to GitHub teams
4. **Repository monitoring**: Enable automated checks for UNALIGNED-REPOS-CATEGORIZATION.csv

**Target**: Supabase sync + agent activation by **June 5**.
