# Codebase Concerns

**Analysis Date:** 2026-09-05

## Critical Security Issues

### Plaintext Credentials in CLAUDE.md

**What happens:** Real production credentials and passwords are stored in plaintext in `CLAUDE.md`, a git-tracked file visible to anyone with repo access.

**Files:** `CLAUDE.md` (lines 107, 116, 120, 122)

**Exposed credentials:**
- OmniRoute password: `_.Thewave12` (line 107)
- SSH password: `_.Thewave12` (line 116)
- Neo4j default: `neo4j/changeme` (line 120)
- PostgreSQL default: `admin/changeme` (line 122)

**Why it's wrong:** 
- Git stores full history; removing later doesn't delete from commit logs
- Passwords are valid until manually rotated
- Anyone with clone access has production credentials
- Violates security standards (NIST, SOC 2, PCI-DSS)

**Do this instead:**
- Remove all credentials from CLAUDE.md immediately
- Rotate all exposed passwords (OmniRoute, SSH, Neo4j, PostgreSQL)
- Store credentials in `.env` (add to `.gitignore` if not already there)
- Use `git-filter-repo` to purge passwords from commit history
- Document credential retrieval via MCP authenticate flows or environment setup scripts
- Add pre-commit hooks to reject credential patterns

---

## Infrastructure & Deployment Concerns

### Duplicate Infrastructure Running Simultaneously

**What happens:** Four overlapping Docker Compose projects running on Mac Studio with duplicate services, confirmed by CLAUDE.md section "VERIFIED STATE."

**Files:** Mac Studio Docker daemon (external to repo)
- `civos_*` stack: Neo4j, Qdrant, Langfuse, Redis, PostgreSQL, LiteLLM, OmniRoute
- `t7shield-*` stack: Neo4j (crash-looping), Qdrant, Langfuse, Grafana, Redis
- `spinup-*` stack: Unknown (referenced but not documented)
- `buzz-*` stack: Unknown (referenced but not documented)
- `crm-postgres`: PostgreSQL

**Duplicates confirmed:**
- 2× Neo4j (one crash-looping: `t7shield-neo4j-1`)
- 2× Qdrant
- 2× Langfuse
- 3× Redis
- 3× Postgres

**Why it's wrong:**
- Violates WHAT I MUST NEVER DO #4 (duplicate infrastructure)
- Resources wasted on idle services
- Port conflicts and routing ambiguity
- Crash-looping services mask real issues
- No single source of truth for infrastructure state

**Do this instead:**
- Audit all four stacks; identify which is canonical
- Document the purpose of each non-canonical stack (dev/test/staging)
- Shut down 3 of 4 stacks, leaving only canonical production stack
- Update `_INFRASTRUCTURE/docker-compose.yml` to reflect single source of truth
- Add infrastructure audit script to CI/CD to prevent future duplication

---

### Crash-Looping Neo4j Container

**What happens:** `t7shield-neo4j-1` container fails to start due to invalid Neo4j 4.x configuration setting on newer image version.

**Symptom:** `Failed to read config: Unrecognized setting: dbms.connectors.default.advertised.address`

**File:** Docker configuration external to repo (likely `docker-compose.yml` in civos/t7shield stacks)

**Workaround:** Use `civos_neo4j` as canonical Neo4j instance (ports 7474/7687)

**Why it's wrong:**
- Dead container consumes resources and confuses deployments
- Hides real issue: version mismatch between compose config and pulled image
- No automated alerting or recovery

**Do this instead:**
- Remove `t7shield-neo4j-1` from active compose project
- Verify `civos_neo4j` configuration against Neo4j 5.x+ settings
- Add health checks to compose that alert on container restart loops
- Document required Neo4j image version in `_INFRASTRUCTURE/README.md`

---

### Observability Infrastructure Disconnected

**What happens:** Langfuse service runs on port 3003 but receives zero traffic. Neither `civos_litellm` nor OmniRoute routes observability callbacks to Langfuse.

**Files:** 
- `_INFRASTRUCTURE/docker-compose.yml` (Langfuse service defined)
- LiteLLM configuration (external, not wired)
- OmniRoute configuration (external, not wired)

**Impact:** Observability layer is infrastructure-only; no tracing, no cost attribution, no performance metrics collected.

**Why it's wrong:**
- Cannot debug inference failures or routing decisions
- Cannot measure token usage or cost per model/provider
- Cannot identify performance bottlenecks in agent loops
- Defeats purpose of having observability infrastructure

**Do this instead:**
- Wire Langfuse callback in LiteLLM config: `success_callback: ["langfuse"]`
- Add Langfuse API credentials to LiteLLM deployment
- Add Langfuse callback routing to OmniRoute config
- Verify traces are flowing into Langfuse by checking dashboard
- Document Langfuse setup in `_INFRASTRUCTURE/OBSERVABILITY.md`
- Add tracing validation to e2e test suite

---

## Architectural & Design Concerns

### Incomplete Domain Structure

**What happens:** 67 domain folders organized in 00-50 numbering scheme, but extension range (51-67) has many that were created today without documentation.

**Missing README.md:** 
- `51-CONSTRUCTION`, `53-TEAMS`, `54-FINANCIAL`, `55-LOOP-ENGINEERING`, `56-ENGINEERING`, `57-CODE-INTELLIGENCE`, `58-LOGISTICS`, `59-MCP`, `60-APIS`, `61-KNOWLEDGE-SOURCES`, `62-TECHNOLOGY`, `63-CHANGE-MANAGEMENT`, `64-RELATIONSHIPS`, `65-SYNERGIES`, `66-OPPORTUNITIES-ALT`, `67-EVOLUTION-ALT`

**Shallow wikilinks:** Most existing READMEs (00-50) have 0-1 wikilinks; only `01-IDENTITY` and `52-PEOPLE` have meaningful cross-links (5 and 26 respectively).

**Why it's wrong:**
- New domains lack purpose statements, making them invisible to agents
- Shallow structure prevents serendipitous discovery and relationship mapping
- Architecture appears complete but lacks 25% of critical documentation
- Extended domains (51-67) feel like an afterthought, not deliberate architecture

**Do this instead:**
- Create README.md for all 16 missing domains with: purpose, key files, relationships, belongs-to parent
- Enrich all 50 base domain READMEs with 10+ wikilinks each (minimum)
- Establish cross-domain links (e.g., 54-FINANCIAL links to 20-DECISIONS, 24-FINANCE, 40-METRICS)
- Automate README generation via `_TEMPLATES/domain-readme.template.md`
- Add domain README validation to pre-commit hooks

---

### Duplicate Domains (66-OPPORTUNITIES-ALT, 67-EVOLUTION-ALT)

**What happens:** Two new domains exist as conceptual duplicates of existing canonical domains without clear merge strategy.

**Files:**
- `66-OPPORTUNITIES-ALT` (new, empty) duplicates `38-OPPORTUNITIES`
- `67-EVOLUTION-ALT` (new, empty) duplicates `45-EVOLUTION`

**Why it's wrong:**
- Creates branching in the domain graph when there should be one truth
- Agents querying opportunities/evolution will receive conflicting results
- No decision made on whether to merge, archive, or repurpose

**Do this instead:**
- Decide: merge into canonical domain, archive as alternate branch, or repurpose for different meaning
- If merging: copy content to canonical domain, delete ALT folder, update all wikilinks
- If archiving: move to `_ARCHIVE/domains/` with a README explaining relationship to canonical
- If repurposing: add clear README distinguishing it from the canonical domain
- Add a DOMAIN_MERGE_DECISIONS.md to document all such decisions

---

### Out-of-Scheme Folders (CAMPAIGNS, COMMERCIAL)

**What happens:** Two folders exist at root level that don't fit the 00-67 numbering scheme with no documented owner or integration strategy.

**Files:**
- `CAMPAIGNS/` (223 files)
- `COMMERCIAL/` (2 files)

**Why it's wrong:**
- Orphaned from the domain structure; agents won't discover them
- No README describing relationship to other domains
- Navigation is unclear (should these be sub-domains? separate control planes?)

**Do this instead:**
- Create `CAMPAIGNS/README.md` documenting purpose and relationship to `26-MARKETING`, `25-SALES`, `40-METRICS`
- Create `COMMERCIAL/README.md` or merge into appropriate domain
- Add wikilinks from `26-MARKETING` and `25-SALES` to CAMPAIGNS
- Update `INDEX.md` to include out-of-scheme folders
- Add navigation tests ensuring all top-level folders are reachable from root

---

## Testing & Quality Concerns

### Complete Absence of Test Coverage

**What happens:** Codebase contains 192 code files (Python, JavaScript, TypeScript, Java) but 0 test files.

**Files:** 
- Code files: `scripts/**/*.py`, `_MCP/**/*.py`, `_CLI/**/*.py`, `fractal/**/*.py`, `fractal/**/*.ts`, etc.
- Test files: None found (no `*.test.*`, `*.spec.*`, or `*_test.*` patterns)

**Why it's wrong:**
- No automated validation of business logic
- No regression detection when refactoring
- Infrastructure changes (Docker, database migrations) have no safety net
- Critical scripts (`fastmcp_server.py`, MCP tools) operate untested in production
- Fragile ontology system (Neo4j wiring, capability routing) lacks validation

**Do this instead:**
- Set up test framework: `pytest` for Python, `jest`/`vitest` for TypeScript
- Create `tests/` directory with fixture-based structure
- Write tests for: all `_MCP/**/*.py` tools, `_CLI/**/*.py` commands, `fastmcp_server.py`, Neo4j wiring scripts
- Add pre-commit hook: `pytest --fail-fast` must pass before commit
- Add CI/CD workflow (`.github/workflows/test.yml`): run tests on push to main
- Set coverage target: 60% minimum for critical paths

---

### Stale Documentation in Model Inventory

**What happens:** CLAUDE.md section "Model Inventory" documents Ollama-based models as "RUNNING" even though Ollama was uninstalled 2026-07-17 and replaced by exo.

**Files:** `CLAUDE.md` lines 91-96

**Stale claims:**
- `qwen2.5-coder:14b` marked "RUNNING" on Ollama (actually dead)
- `nomic-embed-text` marked available for embeddings (actually broken; route still points to dead Ollama)
- Model status table predates infrastructure changes

**Why it's wrong:**
- Misleads operators about available inference capacity
- Hides that embeddings pipeline is broken (no replacement service for nomic-embed-text)
- No single source of truth for model/runtime state

**Do this instead:**
- Move runtime state from static CLAUDE.md to queryable source (Neo4j, Qdrant, or dedicated `_REGISTRIES/MODEL_RUNTIME_STATUS.yaml`)
- Update CLAUDE.md to reference the queryable registry with a query command
- Add `cb models status` CLI command to check live model state
- Remove all "RUNNING" from static documentation; replace with "See `cb models status`"
- Document exo configuration, aliases (`qwen-fast`, `qwen-heavy`), and current limitations (no embeddings)

---

## Architectural Debt Concerns

### LiteLLM Routing Strategy: Simple-Shuffle (No Intelligence)

**What happens:** LiteLLM `router_settings.routing_strategy` is set to `simple-shuffle`, which round-robins across deployments without quality, cost, or latency scoring.

**File:** LiteLLM config (external to repo)

**Impact:**
- Cannot optimize for cheapest provider when multiple options available
- Cannot route to lowest-latency endpoint
- Cannot learn from past performance (outcome-based routing)
- Caching is exact-match only (Redis), not semantic

**Why it's wrong:**
- Wastes inference budget by not scoring provider quality
- Ignores fallback chains documented in CLAUDE.md
- No basis for cost attribution to ventures or projects

**Do this instead:**
- Enable LiteLLM's `usage-based-routing-v2` for cost optimization
- Enable `latency-based-routing` for performance optimization
- Wire Langfuse traces (see Observability concern above) to enable outcome-based routing
- Implement semantic caching in Redis (e.g., embedding-based clustering)
- Document routing strategy decisions in `_INFRASTRUCTURE/ROUTING_STRATEGY.md`

---

### No Capability Router (Layer 9)

**What happens:** System lacks a Layer 9 Capability Router to discover and invoke from ~300 capabilities based on agent intent.

**Files:** No implementation exists for `cap_router`, `search_capabilities`, or `execute_capability`

**Gap details:** Agents currently route to fixed endpoints; cannot dynamically discover capabilities.

**Why it's wrong:**
- Limits agent autonomy to pre-wired capabilities only
- Cannot add new capabilities without code changes
- Defeats purpose of modeling 300+ capabilities in Neo4j

**Do this instead:**
- Evaluate `different-ai/openwork` MCP (has `search_capabilities`, `execute_capability`)
- Or implement custom `CapabilityRouter` in `_MCP/fastmcp_server.py`
- Wire Neo4j queries: `MATCH (c:Capability) WHERE c.relevance_score > threshold RETURN c`
- Add capability router tests (see Testing concern above)
- Document capability discovery protocol in `14-CAPABILITIES/README.md`

---

### No Agent Router (Layer 6)

**What happens:** System lacks unified hub + per-task orchestrator for agent routing.

**Files:** No implementation exists; Antigravity/OmniRoute mentioned but not integrated

**Gap details:** 26 routing agents exist in theory but have no orchestration layer.

**Why it's wrong:**
- Agents cannot discover each other or coordinate
- No task queuing or priority system
- Cannot handle concurrent multi-agent workflows

**Do this instead:**
- Evaluate `agentlas-ai/Agentlas-OS` for agent routing
- Or design custom agent router in `16-AGENTS/AGENT_ROUTER.md`
- Implement agent registry in Neo4j: `CREATE (a:Agent {name, capabilities[], status})`
- Add task queue (use Trigger.dev or Redis Bull)
- Document agent lifecycle in `16-AGENTS/LIFECYCLE.md`

---

### No Policy Engine Enforcement

**What happens:** No enforcement layer for security, compliance, or governance policies.

**Files:** `21-POLICY/README.md` exists but contains no enforcement mechanism

**Gap details:** Policies are documented but not validated or blocked.

**Why it's wrong:**
- Agents can bypass security policies
- No audit trail of policy violations
- Compliance with ANTIGRAVITY rules is voluntary, not enforced

**Do this instead:**
- Evaluate `roboticforce/agent-guardrails` for policy enforcement
- Or implement custom `PolicyEngine` in `_MCP/fastmcp_server.py`
- Create policy interceptor: all agent actions route through policy check before execution
- Log all policy violations to Neo4j for audit trail
- Add policy tests (see Testing concern above)

---

### No Context Compiler (Neo4j+Qdrant Fan-Out)

**What happens:** System has Neo4j and Qdrant but no layer that ranks, compresses, or prioritizes context before passing to LLMs.

**Files:** No implementation of context ranking, deduplication, or compression

**Gap details:** Agents receive raw context dumps without optimization.

**Why it's wrong:**
- Wastes context window on low-relevance information
- Cannot distinguish signal from noise in large knowledge graphs
- Token budget used inefficiently

**Do this instead:**
- Design Context Compiler in `12-CONTEXT/COMPILER.md`
- Implement query → Neo4j (relationships) + Qdrant (semantics) → rank by relevance → compress → return
- Add relevance scoring: combine graph distance with embedding similarity
- Implement compression: abstractive summarization for low-ranking nodes
- Add context compiler tests with real queries

---

## Data & Registry Concerns

### Venture Registry Integrity (700+ Speculative Records)

**What happens:** 700+ ventures documented in Supabase and registries but marked as "speculative registry records with zero revenue" in REALITY.md.

**Files:** 
- `_REGISTRIES/ventures-by-sector.yaml`
- Supabase ventures table (external)
- VENTURE-READINESS-SCORECARD.csv

**Metadata conflicts:** 
- venture.json status disagrees with live venture-hub dashboard
- 96/864 owned repos have real site code, but venture.json may say "planned"
- Readiness scorecard shows 27.7% average completion, 0 ventures past MVP

**Why it's wrong:**
- Single founder cannot distinguish signal (real ventures) from noise (template records)
- Capital allocation decisions based on unreliable metadata
- Time spent on "active" ventures that are actually templates
- No clear path to monetization validation

**Do this instead:**
- Establish venture staging gates: Template → Validation → Prototype → MVP → Scaling
- Only count ventures with external revenue in metrics
- Mark template records with `status: template` explicitly
- Run weekly audit: compare venture.json + git commit history + Supabase revenue to identify real operating ventures
- Generate "REAL VENTURES" registry pulling only from observed revenue, customer signups, deployed code
- Document single source of truth per venture (which system wins in conflicts: GitHub, Supabase, or CSV)

---

### Registry Gaps: MCP Tools Metadata

**What happens:** FastMCP server (`_MCP/fastmcp_server.py`) defines 9 tools but they are not indexed in `_REGISTRIES/tools.yaml` or linked in Neo4j.

**Files:**
- `_MCP/fastmcp_server.py` (tools defined)
- `_REGISTRIES/tools.yaml` (not updated)
- Neo4j (no Tool nodes with MCP metadata)

**Why it's wrong:**
- Agents cannot discover available MCP tools via knowledge graph
- No way to route to correct MCP based on intent
- Dead gap between tool definition and tool discovery

**Do this instead:**
- Auto-generate `_REGISTRIES/tools.yaml` from `_MCP/fastmcp_server.py` docstrings
- Create Neo4j nodes for each tool: `CREATE (t:Tool {name, description, inputs, outputs, mcp})`
- Add tool discovery query: `MATCH (t:Tool) WHERE t.capability_tags CONTAINS $intent RETURN t`
- Run this on MCP server startup to sync registry
- Add tool registry validation test

---

## Navigation & Discoverability Concerns

### Multiple Root Navigation Files (START-HERE Sprawl)

**What happens:** 12+ navigation stub files at root level with unclear hierarchy and overlapping purposes.

**Files:**
- `START-HERE.md`
- `STARTHERE.md`
- `START-HERE-AGENTS.md`
- `START-HERE-COMPANY.md`
- `START-HERE-DATA.md`
- `START-HERE-ENGINEERING.md`
- `START-HERE-GOVERNANCE.md`
- `START-HERE-INFRASTRUCTURE.md`
- `START-HERE-OPERATIONS.md`
- `START-HERE-REPOSITORIES.md`
- `START-HERE-RESEARCH.md`
- `START-HERE-VENTURES.md`

**Why it's wrong:**
- New user doesn't know which to read first
- No clear relationships between files
- Duplicate information likely spread across multiple files
- No single source of truth for navigation

**Do this instead:**
- Consolidate into single `START-HERE.md` with role-based branches
- Format as: "Are you a [Founder / Developer / Researcher / Operator]? Start here → `path`"
- Delete `STARTHERE.md` (duplicate name of `START-HERE.md`)
- Merge role-specific content into appropriate base domains (e.g., START-HERE-ENGINEERING → `56-ENGINEERING/README.md`)
- Link role-specific entry points from single START-HERE.md
- Test navigation flow: new user should find answer in ≤2 clicks

---

### Broken/Dangling Wikilinks

**What happens:** Many wikilinks reference non-existent files or use inconsistent naming.

**Example:** CLAUDE.md references `[[INFRASTRUCTURE]]` but actual file is `56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE.md` (nested 2 levels)

**Files:** Scattered across domain READMEs and markdown files

**Why it's wrong:**
- Obsidian vault shows "broken link" warnings
- Agents trying to follow wikilinks receive 404s
- Navigation intent is unclear (relative path? domain? file?)

**Do this instead:**
- Standardize wikilink format: `[[Domain-Name|Display Text]]` where Domain-Name is the folder name
- Audit all wikilinks: `grep -r "\[\[" . --include="*.md" | grep -v "^#"`
- For each broken link: fix the target file path or delete the link
- Add wikilink validation to pre-commit: must resolve to existing file
- Document wikilink conventions in `_TEMPLATES/WIKILINK_GUIDE.md`

---

## Performance & Capacity Concerns

### Limited Headroom for Concurrent Inference

**What happens:** Mac Studio M4 Max has 36GB unified RAM; single large LLM instance (`Qwen3.6-35B-A3B-5bit`) consumes ~24GB, leaving only 12GB for OS, databases, and concurrent requests.

**Files:** `_REGISTRIES/LLM_HARDWARE_COMPATIBILITY_REGISTRY.yaml`

**Bottleneck:** Cannot run two inference workloads simultaneously; must queue or fail-over to fallback provider (Claude API).

**Why it's wrong:**
- Single point of failure for inference
- Agents have no graceful degradation (must block or fail)
- Cannot validate multi-model fallback chains under load

**Do this instead:**
- Document memory budget in `_INFRASTRUCTURE/CAPACITY_PLANNING.md`
- Set hard limit: reserve 12GB for system, allocate 24GB per inference model
- Implement aggressive model quantization: target 8-bit or 4-bit variants if available
- Add memory monitoring: `cb health memory` should alert when headroom < 5GB
- Test fallback chain: when local model hits memory limit, does it fallback to Claude API gracefully?
- Plan MacBook Air secondary deployment for inference load balancing

---

### Unverified Claims About Distributed Inference

**What happens:** REALITY.md lists as unverified: "exo can reliably split tensor layers between Mac Studio and MacBook Air under concurrent agent workloads without crashing."

**Files:** `REALITY.md` line 45, and implicit in exo configuration

**Why it's wrong:**
- Distributed inference is a core feature of the system but untested
- No benchmark under production load
- Single failure of MacBook Air network or power could crash inference

**Do this instead:**
- Run load test: 10 concurrent agent requests to local model
- Measure: latency, memory usage on both machines, network bandwidth
- Document results in `_INFRASTRUCTURE/LOAD_TEST_RESULTS.md`
- Set latency SLA: max 2s per token at 10 concurrent
- Add automated load test to CI/CD (weekly)
- Define fallback if MacBook Air is offline: must gracefully degrade to Mac Studio only

---

## Operational Concerns

### Single Founder Bottleneck (Bus Factor = 1)

**What happens:** REALITY.md states: "Solo operator structure. Zero full-time employees, zero contractors with recurring deliverables. The entire bus factor of the enterprise is 1."

**Files:** `REALITY.md` line 94

**Risk:** If founder is unavailable, all infrastructure, deployment, and strategic decisions halt.

**Why it's wrong:**
- No redundancy for critical knowledge
- Onboarding new person requires months of reverse-engineering
- Cannot parallelize work
- Technical debt accumulates while founder is overloaded

**Do this instead:**
- Document all critical procedures: `_INFRASTRUCTURE/RUNBOOKS/` with step-by-step playbooks
- Create operations dashboard: `cb health` should show all critical service status in one view
- Hire first contractor: focus on observability/monitoring automation
- Establish on-call rotation (even if founder is primary, need backup procedures)
- Automate deployments: `cb infrastructure deploy` should be one command, not manual steps
- Add audit trail: all changes must be logged and reversible (`git revert`)

---

### Unmonetized System with Negative Cash Flow

**What happens:** REALITY.md documents: "30-Day External Cash Collected: $0.00" and "This violates [[00-CONSTITUTION|WHAT I MUST NEVER DO #4]]."

**Files:** `REALITY.md` lines 68, 75-77

**Cost drivers:** Electricity, hardware depreciation, domain registrations, cloud API fallback

**Why it's wrong:**
- Burning capital without revenue to offset
- System is a research lab, not a business
- Risk of running out of runway before finding product-market fit

**Do this instead:**
- Identify 1-3 ventures with >$5K MRR potential in next 90 days
- Allocate 80% of founder time to revenue, 20% to infrastructure
- Set unit economics targets: cost per venture must be <30% of revenue
- Implement cost tracking: `cb finance venture-cost LT-005` to see all costs attributed to a venture
- Quarterly revenue target: Month 1: $0 → Month 3: $5K MRR → Month 6: $25K MRR

---

## Documentation Concerns

### Stale Claims in CLAUDE.md

**What happens:** CLAUDE.md documents infrastructure as current but acknowledges multiple stale claims in "VERIFIED STATE" section (lines 11-20).

**Examples:**
- Ollama still listed as running but actually dead since 2026-07-17
- Port 3010 documented as Grafana but actually Open WebUI
- Neo4j container t7shield-neo4j-1 crash-looping but still in compose files
- Ollama routes still configured in LiteLLM

**Why it's wrong:**
- Operators follow stale documentation and run into 404s
- Newcomers waste time debugging "broken" setup
- Hides that multiple infrastructure components need refresh

**Do this instead:**
- Move all verified state to queryable source (`_REGISTRIES/INFRASTRUCTURE_STATUS.yaml`)
- CLAUDE.md becomes reference to the registry, not source of truth
- Add `cb infrastructure verify` command that checks all claims
- Document drift detection: weekly audit comparing documentation vs actual state
- Mark all stale sections with `<!-- STALE: see _REGISTRIES/INFRASTRUCTURE_STATUS.yaml -->`

---

### Empty Architecture File

**What happens:** `./_DOCS/architecture.md` exists but is completely empty (0 bytes).

**Files:** `./_DOCS/architecture.md`

**Why it's wrong:**
- Suggests architecture is documented when it's not
- New developer looking for system architecture finds nothing
- No reference point for architectural decisions

**Do this instead:**
- Either delete the empty file, or fill it with:
  - System overview (20 layers, control planes, domains)
  - Data flow diagrams (ingestion → knowledge graph → agents → execution)
  - Technology stack
  - Links to detailed documentation in domains
- Make it the authoritative architecture reference
- Link from START-HERE.md

---

## Compliance & Governance Concerns

### No Audit Trail for Infrastructure Changes

**What happens:** Docker services, database schemas, and configuration changes are not tracked in version control or audit logs.

**Files:** 
- Docker daemon state (external)
- LiteLLM config (external)
- OmniRoute config (external)

**Why it's wrong:**
- Cannot answer "who changed what and when?"
- Cannot rollback configuration errors
- Violates compliance requirements (HIPAA, SOC 2, PCI)

**Do this instead:**
- Check all infrastructure config into version control
- For Docker: commit `docker-compose.yml` with all service configs
- For external systems (LiteLLM, OmniRoute): export config to `_INFRASTRUCTURE/config/` and track in git
- Add pre-commit hook: `git diff` must review config changes before commit
- Implement audit log: all deployments logged to Neo4j with timestamp, actor, change
- Add `cb audit infrastructure` command to query change history

---

---

*Concerns audit: 2026-09-05*
