# Codebase Structure

**Analysis Date:** 2026-09-05

## Directory Layout

```
Company Brain (repo root: /Users/acebless/Documents/The Company/Company Brain)
│
├── 00-CONSTITUTION/          # Mission, principles, governance
├── 01-IDENTITY/              # Company structure, holdings, brands
├── 02-SOURCES/               # Data sources, APIs, integrations
├── 03-INGESTION/             # ETL pipelines, connectors, data loading
├── 04-DATA/                  # Raw, normalized, canonical data
├── 05-METADATA/              # Schemas, lineage, provenance
├── 06-ENTITY-RESOLUTION/     # Deduplication, entity linking
├── 07-ONTOLOGY/              # Conceptual models, vocabularies
├── 08-KNOWLEDGE-GRAPH/       # Neo4j relationships, nodes, edges
├── 09-KNOWLEDGE/             # Policies, procedures, rules, IP
├── 10-MEMORY/                # Episodic, semantic, procedural memory
├── 11-INDEXING/              # Full-text, vector, semantic indexes
├── 12-CONTEXT/               # Task context, working memory
├── 13-REPOSITORIES/          # Repository metadata, code ownership
├── 14-CAPABILITIES/          # Capability registry, solutions/ (300+ implementations)
│   └── solutions/            # Generated capability docs (procedurally generated)
├── 15-SKILLS/                # Procedure library, examples
├── 16-AGENTS/                # Agent registry, personas, orchestration
├── 17-MODELS/                # Model registry, performance, costs
├── 18-TOOLS/                 # Tool/API registry, MCP servers
├── 19-ORCHESTRATION/         # Router, planner, scheduler
├── 20-DECISIONS/             # Decision requests, recommendations
├── 21-POLICY/                # Authority, permissions, escalation
├── 22-EXECUTION/             # Jobs, tasks, transactions, runs
├── 23-VENTURES/              # Venture registry, operations
├── 24-FINANCE/               # Accounting, budgets, forecasting
├── 25-SALES/                 # Sales pipeline, leads, deals
├── 26-MARKETING/             # Campaigns, analytics, content
├── 27-CUSTOMERS/             # Customer profiles, support, feedback
├── 28-PRODUCT/               # Product strategy, roadmap
├── 29-OPERATIONS/            # Processes, SOPs, logistics
├── 30-HR/                    # Workforce, recruiting, training
├── 31-LEGAL/                 # Contracts, IP, compliance
├── 32-SECURITY/              # Identity, access, vulnerabilities
├── 33-COMPLIANCE/            # Regulatory, certifications
├── 34-RISK/                  # Enterprise, financial, operational risk
├── 35-ASSETS/                # Real estate, equipment, IP
├── 36-PARTNERS/              # Investors, vendors, partners
├── 37-RESEARCH/              # Market research, trend analysis
├── 38-OPPORTUNITIES/         # Opportunities, market gaps
├── 39-EXPERIMENTS/           # Experimentation, A/B testing
├── 40-METRICS/               # KPIs, SLIs, SLOs, measurement
├── 41-OBSERVABILITY/         # Monitoring, logging, telemetry
├── 42-EVALUATION/            # Assessment, scoring
├── 43-OUTCOMES/              # Outcomes, results, achievements
├── 44-LEARNING/              # Lessons, knowledge synthesis
├── 45-EVOLUTION/             # Optimization, improvement
├── 46-GOVERNANCE/            # Change control, audits
├── 47-DOCUMENTS/             # Long-form documentation, guides
├── 48-AUTOMATION/            # Workflow automation, RPA
├── 49-SYSTEM/                # System architecture, infrastructure
├── 50-MASTER-CONTROL/        # Current state, objectives, blockers
│
├── 51-CONSTRUCTION/          # Extension: Construction domain (added 2026-09-05)
├── 52-PEOPLE/                # Extension: Workforce/talent (added 2026-09-05)
├── 53-TEAMS/                 # Extension: Team structures (added 2026-09-05)
├── 54-FINANCIAL/             # Extension: Financial services (added 2026-09-05)
├── 55-LOOP-ENGINEERING/      # Extension: Loop execution patterns (added 2026-09-05)
├── 56-ENGINEERING/           # Extension: Technical infrastructure (added 2026-09-05)
├── 57-CODE-INTELLIGENCE/     # Extension: Code graphs, symbol analysis (added 2026-09-05)
├── 58-LOGISTICS/             # Extension: Supply chain (added 2026-09-05)
├── 59-MCP/                   # Extension: MCP server registry (added 2026-09-05)
├── 60-APIS/                  # Extension: API registry (added 2026-09-05)
├── 61-KNOWLEDGE-SOURCES/     # Extension: External knowledge sources (added 2026-09-05)
├── 62-TECHNOLOGY/            # Extension: Technology stack (added 2026-09-05)
├── 63-CHANGE-MANAGEMENT/     # Extension: Change control (added 2026-09-05)
├── 64-RELATIONSHIPS/         # Extension: Entity relationships (added 2026-09-05)
├── 65-SYNERGIES/             # Extension: Cross-venture synergies (added 2026-09-05)
├── 66-OPPORTUNITIES-ALT/     # Extension: Alternative opportunities (added 2026-09-05)
├── 67-EVOLUTION-ALT/         # Extension: Alternative evolution paths (added 2026-09-05)
│
├── SECTORS/                  # Sector-specific files (35+ sectors: SEC-001 to SEC-034+)
│   ├── SEC-001-beauty-wellness.md
│   ├── SEC-002-construction-infrastructure.md
│   ├── ... (35+ sector definitions)
│
├── CAMPAIGNS/                # Marketing/growth campaigns
├── COMMERCIAL/               # Commercial/business operations
├── fractal/                  # Fractal agent system (hierarchical agents)
├── graft/                    # Code intelligence graphs
│
├── _CLI/                     # Command-line interface
│   ├── bin/cb                # Main CLI binary (hand-written bash)
│   ├── schema.yaml           # Command/domain mapping (reference, not generated)
│   └── README.md             # CLI documentation
│
├── _DOCS/                    # Documentation organized by type
│   ├── api/                  # API documentation
│   ├── architecture/         # Architecture guides
│   ├── guides/               # How-to guides
│   ├── procedures/           # Standard procedures
│   └── reference/            # Reference material
│
├── _INFRASTRUCTURE/          # Infrastructure setup & config
│   ├── docker-compose.yml    # Neo4j, Qdrant, PostgreSQL, LiteLLM, Langfuse
│   ├── DEPLOYMENT_PHASES.md  # 4-phase deployment roadmap
│   ├── agents/               # Agent deployment configs
│   ├── config/               # Service configs (Docker Compose projects)
│   ├── integrations/         # External service integrations
│   ├── memory/               # Memory layer configuration
│   ├── observability/        # Grafana, Langfuse setup
│   ├── omniroute/            # OmniRoute model router config
│   ├── storage/              # Storage topology (LaCie 4TB)
│   └── tools/                # Tool configurations
│
├── _MCP/                     # MCP server implementation
│   └── fastmcp_server.py     # 9 tools, 1 resource, 1 prompt (Python 3.12)
│
├── _MEMORY/                  # Persistent session memory
│
├── _ONTOLOGY/                # Core ontology definitions
│   ├── COGNITION_FLOW.yaml   # 22-stage cognitive pipeline
│   ├── FABRICS.yaml          # 9 cognitive fabrics
│   ├── OBJECT_TYPES.yaml     # 60+ entity types
│   ├── RELATIONSHIPS_EXTENDED.yaml  # 250+ predicates
│   ├── EVIDENCE_STANDARDS.md # Confidence scoring
│   └── STATUS_LIFECYCLE.md   # 8-state machine
│
├── _PIPELINES/               # Data processing pipelines (10 pipeline types)
│   ├── code-intelligence/    # Repository intelligence extraction
│   ├── execution/            # Execution tracking & auditing
│   ├── indexing/             # Qdrant/Neo4j indexing
│   ├── ingestion/            # ETL, source import
│   ├── learning/             # Lesson extraction
│   ├── observability/        # Telemetry collection
│   ├── processing/           # Data transformation
│   ├── reasoning/            # Agent reasoning workflows
│   ├── retrieval/            # Context assembly, RAG
│   └── transformation/       # Data format conversion
│
├── _PROMPTS/                 # Prompt templates for agents
│
├── _REGISTRIES/              # Canonical registries (single source of truth)
│   ├── CANONICAL/            # Canonical entity list
│   ├── agents/               # Agent registry (YAML)
│   ├── capabilities/         # Capability registry
│   ├── control-points/       # Control point (CBP) registry
│   ├── coverage/             # Coverage analysis
│   ├── integrations/         # Integration registry
│   ├── models/               # Model registry
│   ├── repositories/         # Repository registry
│   ├── services/             # Service registry
│   ├── skills/               # Skill registry
│   ├── tools/                # Tool registry
│   ├── ID_REGISTRY.yaml      # Machine ID → human ID mapping
│   ├── INFRASTRUCTURE_REGISTRY.yaml  # Device/storage inventory
│   ├── LLM_HARDWARE_COMPATIBILITY_REGISTRY.yaml  # Model-to-device matrix
│   ├── RECONCILIATION_2026_09_01/  # Audit results directory
│   │   ├── COMPANY_BRAIN_AUDIT_REPORT.md
│   │   ├── DELIVERY_SUMMARY.md
│   │   ├── CAPABILITY_DEPENDENCY_MAP.md
│   │   └── COMPANY_BRAIN_NEO4J_IMPORT.cypher
│   └── ventures-by-sector.yaml  # Venture registry by sector
│
├── _RELATIONSHIPS/           # Entity relationship definitions
│
├── _TEMPLATES/               # Reusable templates
│
├── _ARCHIVE/                 # Archive, cold storage
│   ├── COLD_STORAGE/         # Old versions, deprecated
│   └── session-artifacts/    # Previous session outputs
│
├── .agents/                  # Claude Code agent personalities
│   ├── agents/               # Agent persona definitions
│   ├── rules/                # Agent behavior rules
│   ├── skills/               # Agent skill links
│   └── workflows/            # Multi-step agent workflows
│
├── .claude/                  # Claude Code configuration
│   ├── CLAUDE.md             # Project-specific instructions
│   ├── settings.json         # MCP servers, settings
│   └── rules/                # Custom rules for Claude
│
├── .evolver/                 # Evolution/iteration tracking
│
├── .github/                  # GitHub Actions, workflows
│   └── workflows/            # CI/CD pipeline definitions
│
├── .obsidian/                # Obsidian vault configuration
│
├── .planning/                # GSD planning documents
│   └── codebase/             # This directory (ARCHITECTURE.md, STRUCTURE.md)
│
├── INDEX.md                  # Master index, all wikilinks
├── README.md                 # Architecture overview, 22-stage flow
├── NAVIGATION_GUIDE.md       # How to navigate Company Brain
├── STARTHERE.md              # Entry point for new users
│
├── neo4j-activation-queries.cypher  # Sample Neo4j queries
└── [various other metadata files]
```

## Directory Purposes

**Core Domain Folders (00-50):**
- **Numbered 00-50:** Original 50-domain organizational structure mapping to 9 cognitive fabrics
- Purpose: Each folder represents one "organizational domain" — a coherent area of responsibility
- Structure: Each domain folder contains a README.md (description), possibly a domain-specific .md file, and often sub-folders for specific entity types (e.g., `14-CAPABILITIES/solutions/`)

**Extension Domain Folders (51-67):**
- **Numbered 51-67:** Added 2026-09-05 during structural cleanup to avoid renumbering conflicts
- Purpose: Specialized domains that didn't fit original 50; also duplicates merged from previous session artifacts
- Examples: `55-LOOP-ENGINEERING` (loop execution patterns), `59-MCP` (MCP servers), `60-APIS` (API contracts)

**Sector Folder (SECTORS/):**
- Purpose: 35+ sector definitions (SEC-001 to SEC-034+), each with OpCos, industries, venture counts
- Structure: Flat list of `SEC-NNN-sector-name.md` files
- Related: Ventures themselves live in `23-VENTURES/` (cross-indexed by sector)

**Cross-Cutting Folders:**
- **CAMPAIGNS/:** Marketing/growth campaigns (project-level, not venture-specific)
- **COMMERCIAL/:** Commercial/business operations (shared services, not venture-specific)
- **fractal/:** Fractal agent orchestration (hierarchical agent patterns)
- **graft/:** Code graph intelligence (Graft integration for repository analysis)

**Infrastructure Prefixes (underscore):**
- **_CLI/:** Command-line interface for Company Brain operations
- **_DOCS/:** Documentation organized by purpose (API, architecture, guides, procedures, reference)
- **_INFRASTRUCTURE/:** Infrastructure setup (Docker Compose, deployment phases, service configs)
- **_MCP/:** MCP (Model Context Protocol) server implementation
- **_MEMORY/:** Persistent session memory (not entity data; execution/session state)
- **_ONTOLOGY/:** Core ontology (schema definitions, not instances)
- **_PIPELINES/:** Data pipelines (ingestion, transformation, retrieval, learning)
- **_PROMPTS/:** Prompt templates for agents
- **_REGISTRIES/:** Canonical registries (single source of truth per entity type)
- **_RELATIONSHIPS/:** Entity relationship definitions
- **_TEMPLATES/:** Reusable templates for new entities
- **_ARCHIVE/:** Archive and deprecated versions

**Configuration Prefixes (dot):**
- **.agents/:** Claude Code agent persona configuration
- **.claude/:** Claude Code project settings and instructions
- **.evolver/:** Evolution/iteration tracking
- **.github/:** GitHub Actions workflows
- **.obsidian/:** Obsidian vault configuration (graph, settings, plugins)
- **.planning/:** GSD (Get Stuff Done) planning documents

## Key File Locations

**Entry Points:**

| File | Purpose |
|------|---------|
| `INDEX.md` | Master index with all wikilinks; start here for navigation |
| `README.md` | Architecture overview; 22-stage pipeline diagram |
| `NAVIGATION_GUIDE.md` | 5-30 minute reading flows by audience |
| `START_HERE.md` | Quick onboarding (~5 minutes) |
| `STARTHERE.md` | Same as above (duplicate for Obsidian) |
| `START-HERE-*.md` | Topic-specific entry points (agents, company, data, engineering, etc.) |

**Configuration:**

| File | Purpose |
|------|---------|
| `.planning/codebase/ARCHITECTURE.md` | This architecture analysis |
| `.planning/codebase/STRUCTURE.md` | This structure analysis |
| `.claude/CLAUDE.md` | Project-specific Claude Code instructions |
| `.claude/settings.json` | Claude Code config (MCP servers, permissions) |
| `_REGISTRIES/ID_REGISTRY.yaml` | Machine ID ↔ Human ID mapping (authoritative) |
| `_ONTOLOGY/COGNITION_FLOW.yaml` | 22-stage pipeline definition |
| `_ONTOLOGY/FABRICS.yaml` | 9 cognitive fabrics definition |

**Core Logic:**

| Directory | Purpose |
|-----------|---------|
| `08-KNOWLEDGE-GRAPH/` | Neo4j relationships (relationships are the schema) |
| `11-INDEXING/` | Qdrant vector indexes (semantic search) |
| `14-CAPABILITIES/solutions/` | 300+ capability implementations (generated) |
| `16-AGENTS/` | 26+ routing agents, personas |
| `17-MODELS/` | Model registry (Claude, Qwen, local models) |
| `20-DECISIONS/` | Decision request log (auditable decisions) |
| `22-EXECUTION/` | Execution log (tasks, jobs, outcomes) |

**Testing:**

| Directory | Purpose |
|-----------|---------|
| `_PIPELINES/ingestion/` | Ingestion tests, validation |
| `_PIPELINES/retrieval/` | Context assembly tests |
| `_PIPELINES/execution/` | Execution tracking tests |

## Naming Conventions

**Files:**

| Pattern | Example | Use |
|---------|---------|-----|
| `NN-DOMAIN-NAME/` | `14-CAPABILITIES/` | Domain folders (00-67 numbered) |
| `NN-DOMAIN-NAME.md` | `14-CAPABILITIES.md` | Domain summary file (inside domain folder) |
| `SEC-NNN-sector.md` | `SEC-001-beauty-wellness.md` | Sector definitions (in SECTORS/ or 00-CONSTITUTION/) |
| `VEN-NNN-venture.md` | `VEN-000001-venture-name.md` | Venture definition (in 23-VENTURES/ or sector folders) |
| `CAP-NNN-capability.md` | `CAP-000247-entity-resolution.md` | Capability definition (in 14-CAPABILITIES/solutions/) |
| `AGT-NNN-agent.md` | `AGT-000042-routing-agent.md` | Agent definition (in 16-AGENTS/) |
| `README.md` | `14-CAPABILITIES/README.md` | Domain folder overview |
| `_REGISTRY.yaml` | `_REGISTRIES/capability_registry.yaml` | Canonical entity registry |

**Directories:**

| Pattern | Example | Use |
|---------|---------|-----|
| `NN-DOMAIN/` | `14-CAPABILITIES/` | Main domain folder |
| `NN-DOMAIN/solutions/` | `14-CAPABILITIES/solutions/` | Generated implementations |
| `_TYPE/` | `_REGISTRIES/`, `_PIPELINES/`, `_INFRASTRUCTURE/` | Infrastructure/utility |
| `.TYPE/` | `.agents/`, `.claude/`, `.github/` | Configuration/dotfiles |

**Identifiers (in YAML/JSON):**

| Prefix | Range | Example | Usage |
|--------|-------|---------|-------|
| `CB-` | All compound IDs | `CB-RECON-2026-09-01` | Audit/operation IDs |
| `CB-REPO-` | 000001–000893 | `CB-REPO-000001` | Repository reference |
| `VEN-` | 000001–999999 | `VEN-000001` | Venture (internal ID) |
| `SEC-` | 001–034+ | `SEC-001` | Sector |
| `CAP-` | 000001–999999 | `CAP-000247` | Capability |
| `AGT-` | 000001–999999 | `AGT-000042` | Agent |
| `SKL-` | 000001–999999 | `SKL-000042` | Skill |
| `MOD-` | 000001–999999 | `MOD-000001` | Model |
| `TOL-` | 000001–999999 | `TOL-000016` | Tool/API |
| `MCP-` | 000001–999999 | `MCP-000001` | MCP Server |
| `DEC-` | 000001–999999 | `DEC-001567` | Decision |
| `CBP-` | 000001–999999 | `CBP-000247` | Control Point |

**Wikilinks (Obsidian):**

| Pattern | Example | Use |
|---------|---------|-----|
| `[[NN-DOMAIN]]` | `[[14-CAPABILITIES]]` | Link to domain folder |
| `[[NN-DOMAIN/file]]` | `[[14-CAPABILITIES/README]]` | Link to file in domain |
| `[[_TYPE/file]]` | `[[_ONTOLOGY/COGNITION_FLOW.yaml]]` | Link to infrastructure file |
| `[[file.md]]` | `[[INDEX.md]]` | Link to root-level file |

## Where to Add New Code

**New Capability (what can the org do):**
- Definition file: `14-CAPABILITIES/solutions/CAP-NNNNNN-capability-name.md`
- Implementation reference: `14-CAPABILITIES/CAPABILITY_SOLUTION_MATRIX.json`
- Link to skill: `15-SKILLS/SKL-NNNNNN-procedure.md`
- Link to tool: `18-TOOLS/` or `59-MCP/`
- Register in: `_REGISTRIES/capabilities/` (YAML)

**New Skill (how to do something):**
- File: `15-SKILLS/SKL-NNNNNN-skill-name.md`
- Register in: `_REGISTRIES/skills/` (YAML)
- Reference in: `14-CAPABILITIES/solutions/` (which capability uses this skill)

**New Agent (autonomous executor):**
- File: `16-AGENTS/AGT-NNNNNN-agent-name.md` or `.agents/agents/agent-name.yaml`
- Register in: `_REGISTRIES/agents/` (YAML)
- Define policies in: `21-POLICY/` (what this agent is authorized to do)

**New Tool/API:**
- If MCP: `59-MCP/MNNNNNN-server-name/` with fastmcp implementation
- If REST API: `60-APIS/ANNNNNN-api-name.md`
- Register in: `_REGISTRIES/tools/` (YAML)

**New Decision (authorization/approval point):**
- File: `20-DECISIONS/DEC-NNNNNN-decision-name.md`
- Policy reference: `21-POLICY/` (what criteria to evaluate)
- Register in: `_REGISTRIES/control-points/` (map to domain + layer)

**New Execution/Loop (work to be done):**
- Template file: `22-EXECUTION/LOP-NNNNNN-loop-name.md`
- Monitoring/tracking: `43-OUTCOMES/` (record results)
- Register in: `_REGISTRIES/loops/` or `55-LOOP-ENGINEERING/` (L1/L2/L3 autonomy level)

**New Venture (business unit):**
- File: `23-VENTURES/VEN-NNNNNN-venture-name.md` or sector-specific folder
- Register in: `_REGISTRIES/ventures-by-sector.yaml`
- Mapping: Add to `SECTOR_INDEX.md` and sector `.md` file (e.g., `SECTORS/SEC-008-financial.md`)

## Special Directories

**`_REGISTRIES/RECONCILIATION_2026_09_01/`:**
- Purpose: Output from universal portfolio audit (893 repos, 789 ventures, 903 dependencies)
- Generated: 2026-09-01
- Contents: Neo4j import scripts, capability dependency map, delivery summary
- Do not edit: Regenerate via `cb reconcile` (if CLI implemented)

**`_REGISTRIES/CANONICAL/`:**
- Purpose: Single source of truth for each entity type (one row per entity, no duplicates)
- Generated: From `_REGISTRIES/*.yaml` consolidated view
- Usage: Primary source for Neo4j inserts, agent queries, graph analysis
- Do not edit: Edit source YAML files instead, regenerate CANONICAL/

**`14-CAPABILITIES/solutions/`:**
- Purpose: 300+ generated capability implementation docs (procedurally created)
- Generated: By Python script `phase3-generate-solution-docs.py`
- Do not edit by hand: Files are regenerated on each run; edit source matrix instead
- Consumed by: Agents when looking up "how to do X"

**`_ARCHIVE/session-artifacts/`:**
- Purpose: Previous session outputs, one-off analysis, deprecated documentation
- Not part of canonical state
- Safe to delete after review

**`_ARCHIVE/COLD_STORAGE/`:**
- Purpose: Old versions of files, deprecated approaches, historical reference
- Not actively used
- Cleaned up annually

## Committed vs Generated

**Committed to Git:**
- All `.md` documentation files
- All domain folders and their README.md files
- All `.yaml` registry definitions (source of truth)
- Configuration files (`_INFRASTRUCTURE/docker-compose.yml`, `_CLI/schema.yaml`)
- Python pipeline scripts (`_PIPELINES/*/`)
- Ontology definitions (`_ONTOLOGY/*.yaml`)

**Generated (do not commit):**
- `14-CAPABILITIES/solutions/` (entire directory; regenerate with Python script)
- `_REGISTRIES/CANONICAL/` (consolidated view; regenerate from source `.yaml` files)
- `.planning/codebase/ARCHITECTURE.md`, `.planning/codebase/STRUCTURE.md` (this analysis; regenerated by `/gsd-map-codebase`)
- `_ARCHIVE/session-artifacts/` (session outputs; safe to delete)
- `.gitignore` excludes: `*.pyc`, `__pycache__/`, `.env`, `.env.local`, `*.log`, `node_modules/`

---

*Structure analysis: 2026-09-05*
