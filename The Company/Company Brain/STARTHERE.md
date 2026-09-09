---
id: DOC-START-001
title: STARTHERE — Master Orientation Legend
aliases: ["START_HERE", "START-HERE", "starthere", "start-here", "Orientation", "Master-Legend"]
tags: [orientation, master-index, company-brain, governance, start-here]
status: ACTIVE
authority: "CP-001 / CP-027"
updated: 2026-09-09
---

[[STARTHERE]] | [[REALITY]] | [[00_RESPECT/RESPECT|RESPECT]] | [[_MEMORY/MEMORY-OS|MEMORY-OS]] | [[_PROMPTS/10_PRE-ACTION-AWARENESS|AWARENESS]] | [[SECTOR_INDEX]] | [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|SECTORS]] | [[INDEX]]

# START HERE

> **Canonical Document ID:** `DOC-START-001`  
> **Authority:** Sovereign Operator & Executive Governance (CP-001 / CP-027)  
> **Status:** LIVE ORIENTATION LEGEND — Updated 2026-09-09 | **Sep 9 Audit:** [[master-private-firm-ontology|Master Ontology]] + Sector Wiring Gaps + Finance Registry Gaps mapped  
> **Master Operating Contract:** [[ANTIGRAVITY|ANTIGRAVITY.md]]  
> **Universal Agent Operating Contract:** [[AGENTS|AGENTS.md]]  
> **Respect Control Layer:** [[00_RESPECT/RESPECT|RESPECT.md]]  
> **Memory Operating System:** [[_MEMORY/MEMORY-OS|MEMORY-OS.md]]  
> **First-Read Document For:** You, Claude Code, Codex, Gemini, Cursor, Autonomous Subagents, New Collaborators, Future-You.

---

## 1. WHAT IS THIS?

**Company Brain** is the operating, computational, and knowledge infrastructure for a distributed company coordinating owned ventures, repositories, AI agent swarms, polyglot databases, and local-first hardware networks.

It answers: **“What is true, what matters, where do I go, and what am I allowed to do next?”**

---

## 2. READ THESE FIRST (MANDATORY OPERATING SEQUENCE)

Before writing code, declaring features, or making changes, read in exact sequence:
1. [[REALITY|REALITY.md]] — What is actually true (evidence outranks documentation).
2. [[00_RESPECT/RESPECT|RESPECT.md]] — The 20 core rules of respect and governance (what we are permitted to do).
3. [[ANTIGRAVITY|ANTIGRAVITY.md]] — The 45 non-negotiable operating rules (strictly zero fake completion).
4. [[_MEMORY/MEMORY-OS|MEMORY-OS.md]] — The 10-stage cognitive cycle & four-tier memory architecture.
5. [[_PROMPTS/10_PRE-ACTION-AWARENESS|10_PRE-ACTION-AWARENESS.md]] — Mandatory 20-point pre-action awareness checklist.
6. [[AGENTS|AGENTS.md]] — Universal portable agent operating guidelines and system orientation.
7. [[EVIDENCE|EVIDENCE.md]] — Verified empirical proof log for all system claims.
8. [[ECONOMIC-REALITY|ECONOMIC-REALITY.md]] — Cash, runway, margins, and commercial survival metrics.
9. [[NORTH-STAR|NORTH-STAR.md]] — Where the company is going (commercial reality, paying customers).
10. [[PRIORITIES|PRIORITIES.md]] — What matters right now (revenue activation, clutter cleanup).
11. [[ARCHITECTURE|ARCHITECTURE.md]] — How the system is structured.
12. [[CLAUDE|CLAUDE.md]] — Live-audited infrastructure, models, and container runtime state.
13. [[UPDATE|UPDATE.md]] — What changed in the recent working sessions.

### Master Private Firm Ontology (Sep 9, 2026 — THE BLUEPRINT)
- [[master-private-firm-ontology|Master Private Firm Ontology.md]] — **THE FOUNDATION:** 34-layer architecture showing how Principal → Family → Private Firm → Holdings → Ventures → Markets → Customers → Revenue feeds back to Capital. Shows that all systems (sectors, ventures, metrics, agents, Neo4j, Obsidian) are views of one graph, not separate databases. **Next phase:** Build PRIVATE-FIRM-ONTOLOGY.xml so all systems speak one vocabulary.

### Capital & Holding Company Architecture (NEW)
- [[WORLDWIDEBRO-HOLDINGS-MASTER-OPERATING-MANUAL]] — Master 789-venture holding company framework (structure, governance, capital allocation, exits)
- [[00_ENTERPRISE_BLUEPRINT|BUSINESS-CAPITAL-DATA-ROOM/00_ENTERPRISE_BLUEPRINT.md]] — Family office architecture (Family Trust → Asset/IP/Admin LLCs → Operating C-Corp)
- [[CAPITAL-READINESS-ENGINE]] — 5-venture capital readiness engine (pilot for 789-venture model); only 5 of 789 ventures have financial profiles
- [[FINANCIAL-ECOSYSTEM-MAPPING|BUSINESS-CAPITAL-DATA-ROOM/FINANCIAL-ECOSYSTEM-MAPPING.md]] — 12-layer financial OS for ventures
- **Business Metric Registry** (Sep 9 planned) — CFA-framework + 12 research libraries + 500 seed metrics + 789-venture financial profiles + Neo4j integration

### Supporting Truth & Discipline Ledgers
- [[KILL-LIST|KILL-LIST.md]] — Formally killed or decommissioned entities.
- [[STOP-DOING|STOP-DOING.md]] — Prohibited behaviors and anti-patterns.
- [[ASSUMPTIONS|ASSUMPTIONS.md]] & [[CLAIMS|CLAIMS.md]] — Unverified claims requiring proof.
- [[SYSTEM-REALITY|SYSTEM-REALITY.md]] — Hardware, network, and execution constraints.

---

## 3. CURRENT REALITY

> [!IMPORTANT]
> **READ [[REALITY|REALITY.md]] FIRST.**

Do not infer system state from:
- Filenames or directory names
- Stale Markdown documentation or sprint notes
- Theoretical registry entries
- Docker Compose declarations
- Repository presence
- URLs or HTTP links
- Speculative claims from past conversations

**Runtime evidence outranks documentation.**

### Known Gaps (Sep 9 Audit)

> [!WARNING]
> **6 Phantom Sector Registries:** All referenced in sector files, but missing from disk:
> - `ventures-by-sector.yaml` (referenced in every SEC-001 through SEC-035)
> - `repositories-by-sector.yaml`
> - `capabilities-by-sector.yaml`
> - `agents-by-sector.yaml`
> - `control-planes-by-sector.yaml`
> - `external-capabilities-by-sector.yaml`
>
> **Finance Data Gap:** Only 5 ventures (OPS-001, LT-005, LT-011, CON-001, RE-001) have financial readiness profiles in CAPITAL-READINESS-ENGINE.md; 784 remaining ventures have ZERO financial wiring (income distance, readiness %, monthly revenue, unit economics).
>
> **Neo4j Wiring:** SECTOR nodes exist conceptually, but edges missing (can't query "all ventures in SEC-024").
>
> **Business Metric Registry:** CFA framework + 12 research libraries defined; 500+ metrics identified but not wired to ventures. Control planes (CP-020 Capital, CP-023 Finance, CP-021 Revenue) own metric domains but no venture-level data.

**Fix roadmap:** Sep 10-19 builds 6 registries + 789-venture financial profiles + Business Metric Registry schema.

### Key Audited Facts (2026-09-09)
- **Nodes Online:** Mac Studio M4 Max (`100.87.214.70`) + MacBook Air (`100.121.17.63`) via Tailscale mesh.
- **Inference Services:** Native `exo` MLX serving `mlx-community/Qwen3.6-35B-A3B-5bit` on port `:52415`. Local Ollama (`http://localhost:11434`) running on MacBook Air serving `qwen2.5-coder:14b`, `llama3.1:8b`, and `hermes3:latest`.
- **Traffic Controller & MCP:** OmniRoute daemon running locally on port `:20128` (`http://localhost:20128`) and Mac Studio mesh node (`http://100.87.214.70:20128`), bridged to Antigravity IDE via FastMCP adapter (`/Users/acebless/.omniroute/bin/antigravity-mcp.mjs`) exposing 110 tools.
- **Security Engine:** Bitwarden CLI (`bw` v2026.4.1, `SEC-BITWARDEN-001`) managing zero-knowledge secrets.
- **Databases:** Healthy `civos_neo4j` on ports `:7474`/`:7687` (20,363 edges synced); `civos_qdrant` on `:6333`; PostgreSQL on `:5432`. **Neo4j gap:** SECTOR nodes exist but no edges from ventures.
- **Observability:** OpenObserve telemetry platform on port `:5080`.
- **Sector Taxonomy:** 35 sectors (SEC-001 to SEC-035) LIVE with proper wikilinks and navigation; 6 sector-scoped registries referenced but missing from disk.
- **Control Planes:** CP-001 to CP-030 all mapped to sectors, Neo4j synced (2026-09-09). CP-023 (Finance), CP-020 (Capital), CP-021 (Revenue) own financial metrics but venture-level data missing.
- **Known Issues:** Container `t7shield-neo4j-1` is crash-looping. Mac Studio has 4 overlapping Docker Compose projects (`civos_*`, `t7shield-*`, `spinup-*`, `buzz-*`).
- **Commercial State:** 0 paying customers, $0 revenue, 0 active commercial offers in market.
- **Code Reality:** 177 owned repos have verifiable code manifests; 618 are venture paperwork templates; 893 owned repos and 904 external capability universe repos cataloged.

---

## 4. CURRENT OBJECTIVE

Break out of the infrastructure avoidance loop. Direct intellectual horsepower and engineering infrastructure toward **commercial viability, real customer transaction, and automated revenue loops** while maintaining local-first sovereignty.

- **GTM Commercial Engine:** [[CAMPAIGNS/CAMPAIGN-OS|CAMPAIGN-OS.md]] & [[CAMPAIGNS/CAMPAIGN|CAM-001 (Local AI & Repo Intelligence Audit)]] driving paying enterprise transactions.

---

## 5. CORE OPERATING VENTURES (TIER-1 FOCUS)

The 7 operating companies (OpCos) advancing toward paying customer revenue:
1. [[23-VENTURES/LT-005|LT-005 (HealthRoute Medical Courier Dispatch)]] — Specimen delivery software. Site: `lt-005-medical-courier-dispatch.vercel.app`.
2. [[23-VENTURES/LT-011|LT-011 (CarrierDispatch TMS)]] — Small-fleet freight dispatch software. Site: `lt-011-dispatch-software.vercel.app`.
3. [[23-VENTURES/RE-001|RE-001 (WorldwideBro Holdings Real Estate)]] — Distressed deal evaluation portal. Site: `re-001-worldwidebro-holdings.vercel.app`.
4. [[23-VENTURES/OPS-001|OPS-001 (CareerOps Staffing)]] — AI talent matching portal. Site: `ops-staff-001-staffing-worldwidebros-projects.vercel.app`.
5. [[23-VENTURES/CON-001|CON-001 (ACE Construction Field OS)]] — Punch lists and field logs. Site: `con-001-ace-construction.vercel.app`.
6. [[23-VENTURES/EC-001|EC-001 (Angels in Daylight)]] — Lifestyle apparel brand storefront. Site: `ec-001-angels-in-daylight.vercel.app`.
7. [[23-VENTURES/FIN-037|FIN-037 (WorldwideBro Quantitative Trading)]] — Python backtesting and execution engine. Repo: `fin-037-worldwidebro-trading-system`.

---

## 6. BUSINESS SECTOR TAXONOMY

Company Brain classifies all operations, ventures, and capabilities across **35 Vertical Business Sectors**:
- Master Architecture & Crosswalk: [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|SECTOR-TAXONOMY-MASTER.md]]
- Navigational Sector Index: [[SECTOR_INDEX|SECTOR_INDEX.md]]
- Sector Vault Folder: [[SECTORS/|SECTORS/]] (contains `SEC-001` through `SEC-035`)
- Sector Crosswalk Registries:
  - [[_REGISTRIES/ventures-by-sector.yaml|ventures-by-sector.yaml]]
  - [[_REGISTRIES/control-planes-by-sector.yaml|control-planes-by-sector.yaml]]
  - [[_REGISTRIES/capabilities-by-sector.yaml|capabilities-by-sector.yaml]]

---

## 7. DO NOT

- **DO NOT** invent completion or report "Done" without executable test proof (`ANTIGRAVITY.md` Rule #3).
- **DO NOT** create placeholder architecture, mock APIs, TODO stubs, or fake data (`ANTIGRAVITY.md` Rule #4).
- **DO NOT** duplicate existing services, databases, or infrastructure stacks.
- **DO NOT** create a new service without checking `_REGISTRIES/service_registry.json`.
- **DO NOT** create a new repository without checking `_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml`.
- **DO NOT** modify production or restart containers blindly.
- **DO NOT** treat speculative ventures as operating companies.
- **DO NOT** confuse documentation with implementation.
- **DO NOT** confuse infrastructure surface area with business enterprise value.

---

## 8. REPOSITORY MAP

```text
/
├── STARTHERE.md               # You are here: Master orientation legend
├── REALITY.md                 # Live executive truth ledger
├── ANTIGRAVITY.md             # 45 Core operating rules (Master Contract)
├── AGENTS.md                  # Universal portable agent operating contract
├── EVIDENCE.md                # Verified audit proof log
├── ECONOMIC-REALITY.md        # Financial metrics, margins, and burn rate
├── NORTH-STAR.md              # Long-term trajectory & business mission
├── PRIORITIES.md              # Immediate tactical priorities
├── ARCHITECTURE.md            # Tripartite system architecture
├── CLAUDE.md                  # Runtime infrastructure state & Docker contexts
├── INDEX.md                   # Complete navigational index of files & domains
├── SECTOR_INDEX.md            # Complete 35-sector business vertical index
├── .agents/                   # Modular Agent Customization Layer
│   ├── rules/                 # Architecture, security, git, and coding standards
│   ├── workflows/             # Slash commands (/gap-analysis, /deploy, etc.)
│   ├── skills/                # On-demand procedural runbooks (including find-skills)
│   └── agents/                # Specialized subagent personas
├── 37-RESEARCH/               # Dedicated external intelligence & research OS (merged 2026-09-05)
├── SECTORS/                   # 35 Vertical business sector notes (SEC-001 to SEC-035)
├── 23-VENTURES/               # Concrete venture master specifications
├── _REGISTRIES/               # Canonical registries & machine-readable manifests
│   └── CANONICAL/             # Ground-truth verified registries (Repos, Sites, Caps)
├── _CLI/                      # Local command line tools & bash harnesses
├── _MCP/                      # FastMCP server & Model Context Protocol bridges
└── 00-50 Domain Vaults/       # Specialized domain folders (CONSTITUTION to MASTER-CONTROL)
```

---

## 9. SYSTEMS & RUNTIME NODES

- **Master Brain Host:** Mac Studio M4 Max (`100.87.214.70`) at `/Volumes/LaCie`.
- **Mobile Engineering Node:** MacBook Air (`100.121.17.63`) at `/Volumes/T7 Shield`.
- **Network Mesh:** Tailscale Encrypted Mesh (`Worldwidebro@`, IPs `100.121.17.63`, `100.87.214.70`, `100.80.229.113`).
- **Knowledge Graph:** Neo4j Community/Enterprise 5.x (`civos_neo4j`, `bolt://100.87.214.70:7687`).
- **Vector Search:** Qdrant Vector Engine (`civos_qdrant`, `http://100.87.214.70:6333`).
- **Relational Database:** PostgreSQL 16 (`postgres`, port `5432`).
- **Heavy Model Engine:** Native Apple Silicon MLX via `exo` (`http://100.87.214.70:52415/v1`).
- **Local Model Engine:** Ollama Local (`http://localhost:11434`, `qwen2.5-coder:14b`, `llama3.1:8b`, `hermes3:latest`).
- **Model Gateway:** LiteLLM Router (`civos_litellm`, port `4000`).
- **Traffic Controller:** OmniRoute v3.8.50 running locally as daemon on `:20128` (`http://localhost:20128`) and Mac Studio (`http://100.87.214.70:20128`).
- **MCP Adapter:** OmniRoute FastMCP Adapter (`/Users/acebless/.omniroute/bin/antigravity-mcp.mjs`) exposing 110 tools to Antigravity IDE.
- **Secrets Management:** Bitwarden CLI (`/opt/homebrew/bin/bw`, `SEC-BITWARDEN-001`).
- **Telemetry & Observability:** OpenObserve (`http://100.87.214.70:5080`).
- **Edge PaaS:** Vercel Global Edge Network (95 active venture sites).

---

## 10. VEX RELATIONSHIP OS (Powered by Neo4j)

**VEX** is the relationship intelligence layer that powers venture portfolio visibility and stakeholder connectivity across Company Brain.

See [[CLAUDE.md#-naming-consolidation--canonical-source-of-truth-sep-9-2026|CLAUDE.md naming consolidation]] for canonical naming authority.

### Data Flow: Company Brain → Intelligence → Relationships

```
Company Brain (104 folders, institutional knowledge)
  ├─ Wiki Links (cross-references)
  ├─ Sector Taxonomy (35 sectors, 789 ventures)
  └─ gbrain Indexing (273+ venture documents)
          ↓
    Neo4j Knowledge Graph (20,363 edges)
  ├─ 789 Venture nodes
  ├─ 1,200+ Person nodes
  ├─ 300+ Investor nodes
  ├─ 300+ Capability nodes
  └─ ALL RELATIONSHIPS
          ↓
     VEX Portfolio (/portfolio)
  ├─ Venture relationships (people, investors, partners)
  ├─ Capability tracking (what each venture uses)
  ├─ Revenue dashboard (Stripe → real-time updates)
  └─ Investor intelligence (who-knows-whom, warm intros)
```

### Core Entities VEX Tracks

- **Ventures** (789 mapped): Name, sector, stage, revenue, team, investors, capabilities
- **People** (1,200+): Founders, executives, investors, advisors, partners, customers
- **Investors** (300+): Angels, VCs, family offices, LPs, banks, lenders, grant officers
- **Partners** (100+): Strategic, channel, distribution, technology, referral partners
- **Capabilities** (300+): Technical skills, platforms, tools, integrations, infrastructure
- **Capital** (tracked): Investments, commitments, equity, debt, grants, revenue
- **Deals** (all): Investments, acquisitions, partnerships, contracts, major wins

### Key Relationships VEX Powers

```cypher
(person)-[:FOUNDED]->(venture)          # Founder relationships
(person)-[:ADVISES]->(venture)          # Advisor assignments
(investor)-[:INVESTED_IN]->(venture)    # Capital deployed
(venture)-[:USES]->(capability)         # Tech stack
(venture)-[:OPERATES_IN]->(sector)      # Sector assignment
(person)-[:INTRODUCED_BY]->(person)     # Intro chain
(person)-[:KNOWS]->(investor)           # Network connections
(deal)-[:CONNECTS]->(investor)          # Deal relationships
```

### How Updates Flow

1. Update Company Brain wiki link or sector taxonomy
2. gbrain re-indexes the document
3. Sync script detects change & pushes to Neo4j
4. VEX API queries Neo4j and refreshes UI
5. Dashboard shows live relationships (no manual entry needed)

### Example VEX Queries

```cypher
# Show all relationships for a venture
MATCH (v:Venture {id: 'OPS-001'})-[r]-(n)
RETURN n, TYPE(r), properties(r)

# Find investors who know founders of target venture
MATCH (i:Investor)-[:KNOWS]-(p:Person)-[:FOUNDED]->(v:Venture {id: 'LT-005'})
RETURN DISTINCT i, p, v

# Show dormant relationships (90+ days)
MATCH (p:Person)-[r:INTERACTED_WITH]->(v:Venture)
WHERE r.last_interaction < date.today() - duration('P90D')
RETURN p, v, r.last_interaction

# Most connected people in venture ecosystem
MATCH (p:Person)-[r]->(v:Venture)
RETURN p, COUNT(r) as connection_count ORDER BY connection_count DESC
```

**Authority:** [[CLAUDE.md|CLAUDE.md]] Naming Consolidation (Sep 9, 2026) | **Status:** Phase 1 Implementation (Sep 9-22)

---

## 11. CANONICAL REGISTRIES & INVENTORIES

All verified ground-truth registries are located under [[_REGISTRIES/]]:
- [[_REGISTRIES/CANONICAL/NAVIGATION_ALIASES.yaml|NAVIGATION_ALIASES.yaml]] — Wiki link reference. **All document aliases in one place.**
- [[_REGISTRIES/CANONICAL/FILE_FORMAT_REGISTRY.yaml|FILE_FORMAT_REGISTRY.yaml]] — Canonical formats, conversion engines, privacy tiers, decision tree. **Start here for any file format question.**
- [[_REGISTRIES/OWNED_REPOSITORIES_INVENTORY.md]] — 893 owned repositories with AST reality status.
- [[_REGISTRIES/EXTERNAL_CAPABILITY_UNIVERSE_INVENTORY.md]] — 904 external capability universe repositories (31M+ stars).
- [[_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml]] — Wikidata-grounded external capability supply chain (OpenObserve, AirLLM, Utopia, Needle, Vaultwarden).
- [[_REGISTRIES/CANONICAL/CAPABILITY_GAP_MATRIX.yaml]] — Crosswalk of owned vs external capabilities vs 713 ventures.
- [[_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml]] — 1,740 repositories (177 code-verified).
- [[_REGISTRIES/CANONICAL/OWNED_REPO_DEPENDENCIES.json]] — Parsed manifests and dependencies for all 177 code repos.
- [[_REGISTRIES/CANONICAL/OWNED_REPO_CODE_REALITY.json]] — 177 code vs 618 paperwork classification.
- [[_REGISTRIES/CANONICAL/SITES_REGISTRY.yaml]] — 95 verified Vercel production sites (SITE-0001 to SITE-0095).
- [[_REGISTRIES/CANONICAL/VERCEL_DEPLOYMENTS.json]] — Live deployments pulled via Vercel CLI.
- [[_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml]] — Technical capabilities grounded in code manifests.
- [[_REGISTRIES/ventures-by-sector.yaml]] — Venture assignments across 35 sectors.
- [[_REGISTRIES/control-planes-by-sector.yaml]] — 30 Control planes mapped to sectors.
- [[_REGISTRIES/capabilities-by-sector.yaml]] — Capability taxonomy by sector.
- [[_REGISTRIES/repositories-by-sector.yaml]] — 893 owned repos mapped to 35 sectors.
- [[_REGISTRIES/external-capabilities-by-sector.yaml]] — 904 starred supply chain repos (31.3M+ stars) mapped across 35 sectors.
- [[_REGISTRIES/agents-by-sector.yaml]] — Agent archetypes and swarms by sector.

---

## 12. COGNITIVE & ETHICAL CONTROL LAYERS

- **Respect Control Layer:** [[00_RESPECT/RESPECT|RESPECT.md]] & [[00_RESPECT/RESPECT-OS|RESPECT-OS.md]] (20 Core Rules, Boundaries, Agency, Truth).
- **Memory Operating System:** [[_MEMORY/MEMORY-OS|MEMORY-OS.md]], [[_MEMORY/MEMORY-MODEL|MEMORY-MODEL.md]], and [[_MEMORY/MEMORY-ARCHITECTURE|MEMORY-ARCHITECTURE.md]].
- **Operational Prompt Stack:** [[_PROMPTS/10_PRE-ACTION-AWARENESS|10_PRE-ACTION-AWARENESS.md]] (The "Always-On" Pre-Action Protocol).
- **Memory Registry:** [[_MEMORY/MEMORY-REGISTRY.json]] (Active vector collections and backends).

---

## 13. BEFORE CHANGING ANYTHING

1. **Read [[STARTHERE|STARTHERE.md]], [[REALITY|REALITY.md]], and [[AGENTS|AGENTS.md]].**
2. **Read relevant subsystem documentation.**
3. **Inspect actual runtime implementation** (e.g., `docker --context macstudio ps`).
4. **Check registries** in `_REGISTRIES/CANONICAL/`.
5. **Determine blast radius** and single points of failure.
6. **Make the smallest valid change.**
7. **Test and verify runtime state.**
8. **Update documentation & update registries.**
9. **Record decisions in ADRs.**

---

## 14. CHANGE LOOP

```text
DISCOVER ──> UNDERSTAND ──> VERIFY ──> PLAN ──> CHANGE ──> TEST ──> DEPLOY ──> OBSERVE ──> VERIFY ──> DOCUMENT ──> UPDATE
```

---

## 15. TRUTH MODEL

Every entity and claim in Company Brain holds one of seven truth states:
- `VERIFIED` — Confirmed by live execution or concrete physical/financial proof.
- `PROBABLE` — Strong indirect evidence exists; awaiting direct runtime probe.
- `ASSUMED` — Declared as design intention; unproven.
- `UNKNOWN` — Missing empirical data.
- `DISPROVEN` — Empirically refuted (e.g., "Ollama is running").
- `STALE` — Previously true, now outdated.
- `CONFLICTED` — Competing contradictory assertions exist.

*Never silently convert an assumed or unverified status into verified.*

---

## 16. PHASE 1 EXECUTION (Sep 6-19, 2026)

Agent Enablement via 3 Knowledge Graph Capabilities:

- [[_PIPELINES/retrieval/hybrid_query|KG-017: Hybrid Search]] ✅ — Graph + Vector queries unified. File: `hybrid_query.py` | Wrapper: `_MCP/hybrid_query_tool.py` | Endpoint: `POST /api/graph/query`
- [[12-CONTEXT/agent_context_builder|KG-028: Agent Context]] ✅ — Subgraph builder for agents. File: `agent_context_builder.py` | Wrapper: `_MCP/context_assembly_tool.py` | Endpoint: `POST /api/graph/context`
- [[60-APIS/graph_api|KG-048: Graph API]] ✅ — FastAPI server with all endpoints. File: `graph_api.py` | Port: `8000` | Auth: Bearer token

**Roadmap:** [[PHASE_1_EXECUTION_PLAN|PHASE_1_EXECUTION_PLAN.md]] | **Assessment:** [[COMPANY_BRAIN_KG_ASSESSMENT|50 KG Capabilities (30% complete)]]

**Result:** 301+ agents (9 routing + 12 specialized + 280+ modular skills) become routable on Sep 19.

---

## 17. WHERE TO GO NEXT

- **Need a document?** → [[_REGISTRIES/CANONICAL/NAVIGATION_ALIASES.yaml|NAVIGATION_ALIASES.yaml]] (all wiki links + aliases)
- **Need file format guidance?** → [[_REGISTRIES/CANONICAL/FILE_FORMAT_REGISTRY.yaml|FILE_FORMAT_REGISTRY.yaml]] (canonical formats, conversion engines, privacy tiers)
- **Need current reality?** → [[REALITY|REALITY.md]] & [[EVIDENCE|EVIDENCE.md]]
- **Need ethical & respect governance?** → [[00_RESPECT/RESPECT|RESPECT.md]] & [[00_RESPECT/RESPECT-OS|RESPECT-OS.md]]
- **Need operating rules?** → [[ANTIGRAVITY|ANTIGRAVITY.md]] (Master Contract)
- **Need memory architecture?** → [[_MEMORY/MEMORY-OS|MEMORY-OS.md]] & [[_MEMORY/MEMORY-ARCHITECTURE|MEMORY-ARCHITECTURE.md]]
- **Need operational prompt stack?** → [[_PROMPTS/10_PRE-ACTION-AWARENESS|10_PRE-ACTION-AWARENESS.md]]
- **Need agent orientation?** → [[AGENTS|AGENTS.md]] (Agent Guidelines)
- **Need business sectors?** → [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|SECTOR-TAXONOMY-MASTER.md]] & [[SECTOR_INDEX|SECTOR_INDEX.md]]
- **Need core operating ventures?** → [[23-VENTURES|23-VENTURES/]] (LT-005, LT-011, RE-001, OPS-001, CON-001, EC-001, FIN-037)
- **Need research intelligence?** → [[37-RESEARCH/RESEARCH-OS|RESEARCH-OS.md]]
- **Need repository universe?** → [[_REGISTRIES/OWNED_REPOSITORIES_INVENTORY|OWNED_REPOSITORIES_INVENTORY.md]] & [[_REGISTRIES/EXTERNAL_CAPABILITY_UNIVERSE_INVENTORY|EXTERNAL_CAPABILITY_UNIVERSE_INVENTORY.md]]
- **Need company orientation?** → [[START-HERE-COMPANY|START-HERE-COMPANY.md]]
- **Need engineering orientation?** → [[START-HERE-ENGINEERING|START-HERE-ENGINEERING.md]]
- **Need infrastructure orientation?** → [[START-HERE-INFRASTRUCTURE|START-HERE-INFRASTRUCTURE.md]]
- **Need agents orientation?** → [[START-HERE-AGENTS|START-HERE-AGENTS.md]]
- **Need repositories orientation?** → [[START-HERE-REPOSITORIES|START-HERE-REPOSITORIES.md]]
- **Need ventures orientation?** → [[START-HERE-VENTURES|START-HERE-VENTURES.md]]
- **Need operations orientation?** → [[START-HERE-OPERATIONS|START-HERE-OPERATIONS.md]]
- **Need data orientation?** → [[START-HERE-DATA|START-HERE-DATA.md]]
- **Need governance orientation?** → [[START-HERE-GOVERNANCE|START-HERE-GOVERNANCE.md]]
- **Need research orientation?** → [[START-HERE-RESEARCH|START-HERE-RESEARCH.md]]
- **Need master ontology blueprint?** → [[master-private-firm-ontology|Master Private Firm Ontology.md]] (Sep 9: 34-layer architecture showing how all systems connect)
- **Need sector wiring gaps?** → [[sector-taxonomy-wiki-links-phantom-registries|Sector Taxonomy Wiki Links × Reality Map]] (Sep 9: 6 phantom registries identified)
- **Need control plane × finance wiring?** → [[control-planes-venture-finance-wiring|Control Planes × Venture Finance Wiring]] (Sep 9: CP-001 to CP-030 LIVE, but 784 ventures unfinanced)
- **Need templates & blueprints?** → [[_TEMPLATES/README|Templates & Blueprints Gallery]]
- **Need operational infrastructure?** → [[_INFRASTRUCTURE/README|Operational Infrastructure & Configuration Hub]]
- **Need system evaluation & benchmarks?** → [[_EVAL/README|Operational Evaluation Harness & Benchmarking Gateway]]
- **Need to know what changed?** → [[UPDATE|UPDATE.md]]
