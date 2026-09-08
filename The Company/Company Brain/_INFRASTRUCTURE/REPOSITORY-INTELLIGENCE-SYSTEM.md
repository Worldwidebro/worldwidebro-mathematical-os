[[STARTHERE]] | [[REALITY]] | [[OMNIROUTE-STATUS]] | [[KNOWLEDGE-GRAPH-OMNIROUTE-INTEGRATION]] | [[_REGISTRIES/CANONICAL/EXTERNAL_CAPABILITY_UNIVERSE.yaml|EXTERNAL_CAPABILITY_UNIVERSE]] | [[14-CAPABILITIES]]

# Repository Intelligence System — 904 Starred Repos as External R&D

**Authority:** CP-006 [[Agents|16-AGENTS]] + CP-013 [[Knowledge Control Plane]] + CP-027 [[Infrastructure Control Plane|56-INFRASTRUCTURE]]

**Purpose:** Transform 904 external repositories into a strategic technology intelligence layer that feeds the Company Brain capability ontology, agent ecosystem, venture factory, and decision engine.

**Core principle:** Discover → classify → evaluate → connect → test → adopt → fork/build → monitor → archive.

---

## 1. INSTALLATION PHASES

### Phase 1: Inventory (904 → Canonical Registry)
**Duration:** 2 hours (automated)  
**Output:** `REPOSITORY_INGESTION_RAW.json` (all 904 repos + metadata)

```bash
# Automated GitHub API ingestion
github-starred-sync --user worldwidebro \
  --output /Volumes/LaCie/repositories/raw/github-starred.json \
  --include metadata,readme,topics,license,activity,dependencies
```

**Captures:**
- repo_id, owner, name, URL, stars, forks
- last_commit, contributors, releases
- languages, license, topics
- README content (first 2000 chars)
- activity metrics (commits/month, issues/month)
- dependency manifests (if available)

**Stores at:** `/Volumes/LaCie/repositories/raw/`

---

### Phase 2: Normalize (Dedup & Archive Check)
**Duration:** 30 minutes (automated)  
**Output:** `REPOSITORY_DEDUPLICATED.json` (880-900 valid repos)

**Remove:**
- Duplicate entries (same GitHub URL)
- Archived repositories (`archived: true`)
- Deleted repositories (404 on GitHub)
- Renamed repos (follow redirects, merge)
- Personal forks of company repositories (self-references)
- Empty/unmaintained stubs (<1 commit in 2 years)

**Decision:** Keep or purge?
- **KEEP:** Active, licensed, usable
- **ARCHIVE:** Interesting but dormant
- **PURGE:** Spam, malicious, irrelevant

**Stores at:** `/Volumes/LaCie/repositories/normalized/`

---

### Phase 3: Enrich (Deep Metadata Collection)
**Duration:** 4-6 hours (automated + sampling)  
**Output:** `REPOSITORY_ENRICHED.json` (per-repo metadata lake)

**Collect for each repo:**

```yaml
github:
  owner: string
  name: string
  url: string
  stars: int
  forks: int
  watchers: int
  issues_open: int
  issues_closed: int
  pull_requests: int
  contributors: int
  last_commit_date: ISO8601
  commit_activity_30d: int
  release_velocity: float
  
metadata:
  description: string
  topics: [string]
  license: string
  language_primary: string
  languages: {lang: percent}
  readme_length: int
  has_tests: bool
  has_ci: bool
  has_security_advisories: bool
  
dependencies:
  count: int
  direct: [string]
  transitive_estimated: int
  outdated_dependencies: int
  security_vulnerabilities: int
  
architecture:
  type: (monolith | microservices | library | framework | tool | plugin)
  entry_point: string
  estimated_size_lines: int
  
community:
  contributor_diversity: float
  issue_response_time_days: float
  pr_merge_time_days: float
  discussion_activity: bool
```

**Stores at:** `/Volumes/LaCie/repositories/enriched/` (one JSON per repo)

---

### Phase 4: Classify (Map to Company Ontology)
**Duration:** 8-12 hours (agent-driven)  
**Output:** `REPOSITORY_CLASSIFICATIONS.json`

**Agent:** `repo-classifier` (Claude Agent)

**Classify each repo against:**

```yaml
PRIMARY_CAPABILITY:
  category: (AI | Infrastructure | Developer Tools | Knowledge | Business | Security)
  subcategory: string
  matches_existing_capability: bool
  capability_id: string or null

SECONDARY_CAPABILITIES:
  - category: string
    confidence: 0.0-1.0

ARCHITECTURE_LAYER:
  - layer: (Models | Routing | Orchestration | Memory | Compute | Storage | Observability | Control | Execution)
    confidence: 0.0-1.0

TECHNOLOGY_CLASSIFICATION:
  - tech: string
    category: string
    version: string

INDUSTRY_RELEVANCE:
  - sector: string
    relevance_score: 0-100
    venture_ids: [string]

AGENT_TYPE:
  - agent_family: string
    use_case: string
    compatibility: string
```

**Stores at:** `/Volumes/LaCie/repositories/classified/`

---

### Phase 5: Score (Strategic Evaluation)
**Duration:** 4-6 hours (agent-driven)  
**Output:** `REPOSITORY_SCORES.json`

**Agent:** `repo-scorer`

**Score each repo on 10 dimensions (0-100):**

```yaml
RELEVANCE_TO_COMPANY_BRAIN:
  description: "How well does this solve a problem we have?"
  score: 0-100

MAINTENANCE_HEALTH:
  description: "Is this actively maintained?"
  factors:
    - last_commit_age_days: int
    - commit_frequency_30d: int
    - maintainer_responsiveness_days: int
  score: 0-100

MATURITY:
  description: "Production-ready, stable, or experimental?"
  factors:
    - release_version: string
    - has_stable_api: bool
    - breaking_changes_frequency: int
  score: 0-100

SECURITY:
  description: "Known vulnerabilities, supply chain risk?"
  factors:
    - dependency_vulnerabilities: int
    - outdated_dependencies: int
    - secret_scanning_enabled: bool
    - signed_releases: bool
  score: 0-100

LICENSE_COMPATIBILITY:
  description: "Can we use this commercially?"
  score: 0-100
  flag: (🟢 Compatible | 🟡 Review | 🔴 Restricted)
  incompatibilities: [string]

COMMUNITY_STRENGTH:
  description: "Active community, good docs, responsive maintainers?"
  factors:
    - github_stars: int
    - contributor_count: int
    - issue_response_time: float
    - documentation_quality: 0-100
  score: 0-100

INTEGRATION_EASE:
  description: "How hard is it to adopt this?"
  factors:
    - api_clarity: 0-100
    - dependency_count: int
    - language_compatibility: bool
    - example_projects: int
  score: 0-100

PERFORMANCE:
  description: "Speed, efficiency, resource usage?"
  score: 0-100
  benchmark_data: object or null

DIFFERENTIATION_VALUE:
  description: "Is this a core competitive advantage or commodity?"
  score: 0-100
  strategic_importance: (core | valuable | useful | reference)

LONG_TERM_VIABILITY:
  description: "Will this project survive and evolve?"
  factors:
    - maintainer_commitment: 0-100
    - funding_status: string
    - adoption_rate: 0-100
    - competitive_landscape: string
  score: 0-100

VENTURE_VALUE:
  description: "How much could this accelerate our ventures?"
  ventures_enabled: [string]
  score: 0-100

STRATEGIC_SCORE:
  aggregate: (sum of above) / 11
  tier: (CRITICAL | HIGH | USEFUL | REFERENCE | LOW | ARCHIVE)
```

**Stores at:** `/Volumes/LaCie/repositories/scored/`

---

### Phase 6: Disposition (What to Do)
**Duration:** 4 hours (agent-driven + human review)  
**Output:** `REPOSITORY_DISPOSITIONS.json`

**Agent:** `repo-disposition` (Claude Agent)

**For each repo, decide:**

```yaml
DISPOSITION:
  status: (ADOPT | INTEGRATE | FORK | EXTEND | REFERENCE | LEARN | MONITOR | CONTRIBUTE | REPLACE | COMPETE | ARCHIVE | IGNORE)
  
  rationale: string
  
  ADOPT:
    meaning: "Use this directly in production"
    action: "Integrate into Company Brain + vendor this capability"
    timeline: "Q4 2026"
    
  INTEGRATE:
    meaning: "Wrap this with our adapters/interfaces"
    action: "Build MCP server or shim layer"
    timeline: "TBD"
    
  FORK:
    meaning: "Clone, modify, maintain our own version"
    action: "Fork to GitHub, diverge for specific needs"
    dependencies: [string]
    
  EXTEND:
    meaning: "Contribute patches/features upstream"
    action: "Submit PRs to this project"
    features_wanted: [string]
    
  REFERENCE:
    meaning: "Study the architecture, don't adopt"
    action: "Add to research library"
    
  LEARN:
    meaning: "Understand patterns and techniques"
    action: "Code review, document lessons"
    
  MONITOR:
    meaning: "Watch for maturity before deciding"
    action: "Quarterly health checks"
    check_date: ISO8601
    
  CONTRIBUTE:
    meaning: "Add features Worldwidebro ventures need"
    action: "Become an active contributor"
    
  REPLACE:
    meaning: "This replaces an existing tool/lib we use"
    action: "Plan migration"
    deprecated_tool: string
    
  COMPETE:
    meaning: "We might build a competing solution"
    action: "Monitor, evaluate, decide to build or adopt"
    
  ARCHIVE:
    meaning: "Interesting but dormant, keep for reference"
    action: "Add to archive, quarterly review"
    
  IGNORE:
    meaning: "Not relevant to Company Brain"
    action: "Remove from active tracking"

OWNER:
  agent: string
  last_reviewed: ISO8601
  next_review: ISO8601
```

**Stores at:** `/Volumes/LaCie/repositories/dispositioned/`

---

### Phase 7: Graph Integration (Knowledge Graph Wiring)
**Duration:** 2-4 hours (automated)  
**Output:** Neo4j nodes and relationships

**Create nodes:**
```cypher
CREATE (repo:ExternalRepository {
  github_id: string,
  owner: string,
  name: string,
  url: string,
  stars: int,
  disposition: string,
  score: int,
  tier: string
})

CREATE (repo)-[:IMPLEMENTS]->(cap:Capability)
CREATE (repo)-[:ENABLES]->(ven:Venture)
CREATE (repo)-[:USED_BY]->(agt:Agent)
CREATE (repo)-[:DEPENDS_ON]->(dep:Dependency)
CREATE (repo)-[:COMPLEMENTS]->(other:ExternalRepository)
CREATE (repo)-[:COMPETES_WITH]->(other:ExternalRepository)
CREATE (repo)-[:REPLACES]->(lib:InternalLibrary)
CREATE (repo)-[:ARCH_LAYER]->(layer:ArchitectureLayer)
```

**Stores at:** Neo4j (bolt://100.87.214.70:7687)

---

### Phase 8: Operationalize (Adoption Pipeline)
**Duration:** Ongoing  
**Output:** Adoption candidates → production

**For repos with disposition = ADOPT or INTEGRATE:**

```
SCREENED (already done in Phase 6)
   ↓
LICENSE CHECK (automated)
   ↓
SECURITY SCAN (automated)
   ├─ Dependency vulnerabilities
   ├─ Secret scanning
   ├─ Supply chain risk
   └─ Abandonment risk
   ↓
ARCHITECTURE REVIEW (agent-driven)
   ├─ API contract verification
   ├─ Integration points
   ├─ Performance requirements
   └─ Compatibility matrix
   ↓
SANDBOX TEST (dev environment)
   ├─ Build verification
   ├─ Basic functionality test
   ├─ Dependency resolution
   └─ Integration with OmniRoute / Neo4j
   ↓
BENCHMARK (performance & reliability)
   ├─ Latency measurement
   ├─ Resource usage (CPU/memory)
   ├─ Concurrency limits
   └─ Failure modes
   ↓
INTEGRATION TEST (Mac Studio environment)
   ├─ Test against real Neo4j
   ├─ Test against real Qdrant
   ├─ Test against real OmniRoute
   └─ Test against real venture data
   ↓
PRODUCTION CANDIDATE
   ├─ Risk assessment
   ├─ Rollback plan
   ├─ Monitoring setup
   └─ Runbook creation
   ↓
ADOPTED (monitoring ongoing)
   ├─ Health checks (weekly)
   ├─ Update tracking (continuous)
   ├─ Vulnerability tracking (continuous)
   └─ Usage metrics (continuous)
```

**Stores adoption pipeline state in:** `/Volumes/LaCie/repositories/adoption/`

---

## 2. STORAGE ARCHITECTURE

### Directory Structure

```
/Volumes/LaCie/
├── repositories/
│   ├── raw/                          # Phase 1 output
│   │   ├── github-starred.json       # All 904 repos, raw metadata
│   │   └── ingestion-log.json        # Errors, timestamp
│   │
│   ├── normalized/                   # Phase 2 output
│   │   ├── deduplicated.json         # 880-900 valid repos
│   │   ├── archived.json             # Repos to keep but not active
│   │   └── purged.json               # Repos removed (reasons)
│   │
│   ├── enriched/                     # Phase 3 output
│   │   ├── {repo_id}.json            # Per-repo deep metadata
│   │   ├── enrichment-log.json
│   │   └── enrichment-errors.json
│   │
│   ├── classified/                   # Phase 4 output
│   │   ├── classifications.json      # All repos + classifications
│   │   ├── by-capability/            # Grouped by capability
│   │   │   ├── AI-Agents.json
│   │   │   ├── Infrastructure.json
│   │   │   └── ...
│   │   ├── by-sector/                # Grouped by venture sector
│   │   │   ├── LT-Medical.json
│   │   │   ├── CON-Construction.json
│   │   │   └── ...
│   │   └── classification-log.json
│   │
│   ├── scored/                       # Phase 5 output
│   │   ├── scores.json               # All repos + scores
│   │   ├── by-tier/
│   │   │   ├── CRITICAL.json         # 90-100 score
│   │   │   ├── HIGH.json             # 80-89 score
│   │   │   ├── USEFUL.json           # 70-79 score
│   │   │   ├── REFERENCE.json        # 50-69 score
│   │   │   ├── LOW.json              # 30-49 score
│   │   │   └── ARCHIVE.json          # 0-29 score
│   │   ├── scoring-log.json
│   │   └── scoring-errors.json
│   │
│   ├── dispositioned/                # Phase 6 output
│   │   ├── dispositions.json         # All repos + decisions
│   │   ├── by-disposition/
│   │   │   ├── ADOPT.json
│   │   │   ├── INTEGRATE.json
│   │   │   ├── FORK.json
│   │   │   ├── REFERENCE.json
│   │   │   ├── MONITOR.json
│   │   │   ├── ARCHIVE.json
│   │   │   └── IGNORE.json
│   │   └── disposition-log.json
│   │
│   ├── adoption/                     # Phase 8 tracking
│   │   ├── pipeline.json             # Current adoption pipeline state
│   │   ├── candidates/
│   │   │   ├── {repo_id}-sandbox.md  # Sandbox test report
│   │   │   ├── {repo_id}-benchmark.md
│   │   │   ├── {repo_id}-security.md
│   │   │   └── {repo_id}-integration.md
│   │   ├── deployed/                 # Adopted repos
│   │   │   ├── {repo_id}-status.json # Deployment status
│   │   │   └── {repo_id}-metrics.json # Performance metrics
│   │   └── adoption-log.json
│   │
│   ├── mirrors/                      # Optional local mirrors
│   │   ├── {repo_id}/
│   │   │   └── ... (clone of repo)
│   │   └── mirror-manifest.json
│   │
│   └── metadata/
       ├── REPOSITORY_INTELLIGENCE_REGISTRY.yaml  # Master index
       ├── CAPABILITY_DEPENDENCY_MAP.yaml         # Capability <- Repo mapping
       ├── TECHNOLOGY_RADAR.yaml                  # ADOPT/TRIAL/ASSESS/HOLD
       ├── DUPLICATE_CAPABILITIES.yaml            # Which repos implement same thing
       ├── DO_NOT_BUILD.yaml                      # Capabilities we won't build
       ├── ADOPTION_PIPELINE_STATUS.yaml          # Current pipeline state
       └── REPOSITORY_HEALTH_TIMELINE.json        # Weekly health snapshots
```

---

## 3. CANONICAL REGISTRIES

### `REPOSITORY_INTELLIGENCE_REGISTRY.yaml`

Master index of all 904 repositories with minimal record.

```yaml
registry_version: "1.0.0"
total_repositories: 904
last_ingested: ISO8601
ingestion_agent: "github-starred-sync"

repositories:
  - repo_id: "EXT-REPO-000001"
    github_id: int
    owner: string
    name: string
    url: string
    
    # Quick lookup
    tier: string                    # CRITICAL | HIGH | USEFUL | REFERENCE | LOW | ARCHIVE
    disposition: string             # ADOPT | INTEGRATE | FORK | REFERENCE | MONITOR | ARCHIVE | IGNORE
    
    # Key metrics
    stars: int
    score: int                      # 0-100
    maintenance_health: 0-100       # Quick indicator
    
    # Relationships
    implements_capability: string or null
    enables_ventures: [string]
    used_by_agents: [string]
    replaces_internal: string or null
    
    # Tracking
    first_starred: ISO8601
    last_classified: ISO8601
    next_review: ISO8601
    owner_agent: string

indices:
  by_capability: ...
  by_venture: ...
  by_tier: ...
  by_disposition: ...
  by_architecture_layer: ...
```

---

### `CAPABILITY_DEPENDENCY_MAP.yaml`

Maps capabilities to repository implementations.

```yaml
capabilities:
  AI_AGENTS:
    implementations:
      - repo_id: "EXT-REPO-000001"
        repo_name: "autogen"
        maturity: "PRODUCTION_READY"
        score: 92
        recommendation: "ADOPT"
        
      - repo_id: "EXT-REPO-000002"
        repo_name: "langgraph"
        maturity: "PRODUCTION_READY"
        score: 89
        recommendation: "TRIAL"
        
      - repo_id: "EXT-REPO-000003"
        repo_name: "metagpt"
        maturity: "STABLE"
        score: 81
        recommendation: "REFERENCE"
    
    selected: "EXT-REPO-000001"
    selection_date: ISO8601
    selection_rationale: "Best community, active maintenance, proven at scale"

  KNOWLEDGE_GRAPH:
    implementations:
      - repo_id: "EXT-REPO-000010"
        repo_name: "neo4j"
        recommendation: "ADOPTED"
      - repo_id: "EXT-REPO-000011"
        repo_name: "duckdb"
        recommendation: "REFERENCE"
    
    selected: "EXT-REPO-000010"
    internal_implementation: "Neo4j Community Edition"
```

---

### `TECHNOLOGY_RADAR.yaml`

Gartner-style technology radar.

```yaml
ADOPT:
  - name: "OmniRoute"
    reason: "Traffic controller for all model routing"
    since: "2026-09-06"
    venues: [ventures, agents, infrastructure]
    
  - name: "exo"
    reason: "Distributed MLX inference on Apple Silicon"
    since: "2026-09-01"
    
TRIAL:
  - name: "LangGraph"
    reason: "Agent orchestration framework"
    status: "Sandbox testing"
    target_decision: "2026-10-01"
    
ASSESS:
  - name: "Repository A"
    reason: "Promising but immature"
    target_decision: "2026-12-01"
    
HOLD:
  - name: "Repository B"
    reason: "Over-engineered for our use case"
    since: "2026-08-01"
```

---

### `DO_NOT_BUILD.yaml`

Explicit record of capabilities we decided NOT to build.

```yaml
decisions:
  - capability: "Secrets Management"
    decision: "DO NOT BUILD"
    date: "2026-09-06"
    reason: "Mature OSS implementations exist (Vault, 1Password)"
    selected_solution: "EXT-REPO-000042"
    selected_solution_name: "Vault"
    owner: "agent-infrastructure"
    
  - capability: "Observability Dashboards"
    decision: "DO NOT BUILD"
    date: "2026-09-06"
    reason: "OpenObserve + Grafana sufficiently mature"
    selected_solutions: ["EXT-REPO-000001", "EXT-REPO-000002"]
    
  - capability: "Vector Search Engine"
    decision: "DO NOT BUILD"
    date: "2026-08-15"
    reason: "Qdrant is production-ready, 21k+ stars"
    selected_solution: "EXT-REPO-000078"
```

---

## 4. AGENTS & WORKFLOWS

### Agent: `repo-classifier`

**Responsibility:** Classify each repository into your ontology

**Inputs:**
- Repository enriched metadata
- Your capability taxonomy
- Your architecture layers
- Your sector definitions

**Outputs:**
- Primary capability
- Secondary capabilities
- Architecture layers
- Sector relevance
- Agent compatibility

**Scale:** 5-10 repos/minute (batched)

---

### Agent: `repo-scorer`

**Responsibility:** Score repository on 10 strategic dimensions

**Inputs:**
- Repository classification
- Dependency analysis
- Activity metrics
- Community signals
- License compatibility
- Security scan results

**Outputs:**
- 10 dimensional scores
- Strategic aggregate score
- Tier classification (CRITICAL → ARCHIVE)

**Scale:** 5-10 repos/minute (batched)

---

### Agent: `repo-disposition`

**Responsibility:** Decide what to do with each repository

**Inputs:**
- Repository score
- Classification
- Your current technology stack
- Your venture roadmap
- Capability gaps

**Outputs:**
- Disposition (ADOPT | INTEGRATE | FORK | etc.)
- Rationale
- Owner assignment
- Timeline

**Scale:** 3-5 repos/minute (requires reasoning)

---

### Agent: `repo-monitor`

**Responsibility:** Track health of ADOPT repos weekly

**Runs:** Weekly (Mondays)

**Checks:**
- Last commit date
- Release velocity
- Open security vulnerabilities
- Contributor activity
- Breaking changes

**Outputs:**
- Health report
- Alerts for concerning trends
- Upgrade recommendations

---

### Workflow: `repository-intelligence-pipeline`

```
GitHub Starred Repos
        ↓
    Phase 1: INVENTORY
        ↓
    Phase 2: NORMALIZE
        ↓
    Phase 3: ENRICH
        ↓
    Phase 4: CLASSIFY (repo-classifier agent)
        ↓
    Phase 5: SCORE (repo-scorer agent)
        ↓
    Phase 6: DISPOSITION (repo-disposition agent)
        ↓
    Phase 7: GRAPH (Neo4j integration)
        ↓
    Phase 8: OPERATIONALIZE
        ↓
    Weekly: MONITOR (repo-monitor agent)
```

**Cadence:**
- Full pipeline: Quarterly (Sep, Dec, Mar, Jun)
- Quick update: Monthly
- Health check: Weekly

---

## 5. INTEGRATION WITH COMPANY BRAIN

### Neo4j Graph Structure

```cypher
// Repository node
CREATE (repo:ExternalRepository {
  repo_id: string,
  github_id: int,
  owner: string,
  name: string,
  url: string,
  stars: int,
  disposition: string,
  score: int,
  tier: string,
  last_verified: timestamp
})

// Relationships to Company Brain
repo -[:IMPLEMENTS]-> (cap:Capability)
repo -[:ENABLES]-> (ven:Venture)
repo -[:ENABLES_VENTURE_CATEGORY]-> (cat:VentureCategory)
repo -[:USES]-> (tech:Technology)
repo -[:USED_BY]-> (agent:Agent)
repo -[:COMPLEMENTS]-> (repo2:ExternalRepository)
repo -[:DEPENDS_ON]-> (dep:Dependency)
repo -[:REPLACES]-> (internal:InternalLibrary)
repo -[:FILLS_GAP]-> (gap:CapabilityGap)
repo -[:ARCH_LAYER]-> (layer:ArchitectureLayer)
```

### Queries

**"Which repos could accelerate medical courier venture?"**
```cypher
MATCH (ven:Venture {sector: "LT"})-[:REQUIRES]->(cap:Capability)
MATCH (repo:ExternalRepository)-[:IMPLEMENTS]->(cap)
WHERE repo.disposition IN ["ADOPT", "INTEGRATE", "FORK"]
RETURN repo.name, cap.name, repo.score ORDER BY repo.score DESC
```

**"Which capabilities are missing?"**
```cypher
MATCH (ven:Venture)-[:REQUIRES]->(cap:Capability)
WHERE NOT EXISTS((repo:ExternalRepository)-[:IMPLEMENTS]->(cap))
RETURN cap.name, COUNT(ven) as venture_count ORDER BY venture_count DESC
```

**"What could reduce build time for next venture?"**
```cypher
MATCH (repo:ExternalRepository {disposition: "ADOPT"})
RETURN repo.name, repo.score, repo.enables_ventures ORDER BY repo.score DESC LIMIT 10
```

---

## 6. IMMEDIATE ACTIONS

### Week 1: Phases 1-3

**Phase 1: Inventory**
```bash
./scripts/ingest-github-starred.sh \
  --user worldwidebro \
  --output /Volumes/LaCie/repositories/raw/github-starred.json
```

**Phase 2: Normalize**
```bash
python3 scripts/normalize_repositories.py \
  --input /Volumes/LaCie/repositories/raw/github-starred.json \
  --output /Volumes/LaCie/repositories/normalized/deduplicated.json
```

**Phase 3: Enrich**
```bash
# For each repo, fetch deep metadata
python3 scripts/enrich_repositories.py \
  --input /Volumes/LaCie/repositories/normalized/deduplicated.json \
  --output-dir /Volumes/LaCie/repositories/enriched/ \
  --parallel 10
```

### Week 2-3: Phases 4-7

**Phase 4: Classify (agent-driven)**
```
Launch: repo-classifier agent
Input: /Volumes/LaCie/repositories/enriched/*.json
Output: /Volumes/LaCie/repositories/classified/
Batches: 10 repos/batch
Duration: ~8-12 hours
```

**Phase 5: Score (agent-driven)**
```
Launch: repo-scorer agent
Input: /Volumes/LaCie/repositories/classified/classifications.json
Output: /Volumes/LaCie/repositories/scored/
Duration: ~4-6 hours
```

**Phase 6: Disposition (agent-driven + review)**
```
Launch: repo-disposition agent
Input: /Volumes/LaCie/repositories/scored/scores.json
Output: /Volumes/LaCie/repositories/dispositioned/
Duration: ~4 hours
Review: 1-2 hours (human spot-check)
```

**Phase 7: Graph Integration**
```bash
# Ingest into Neo4j
python3 scripts/graph_ingest_repositories.py \
  --input /Volumes/LaCie/repositories/dispositioned/dispositions.json \
  --neo4j bolt://100.87.214.70:7687 \
  --user neo4j \
  --password $(bw get password neo4j_default)
```

---

## 7. DECISION ENGINE OUTPUT

After full pipeline:

**Questions you can answer:**
- ✅ Which 10 repos are CRITICAL to adopt?
- ✅ Which capabilities are already solved by OSS?
- ✅ Which capabilities should we build ourselves?
- ✅ Which repos could accelerate [venture name]?
- ✅ What's the total maintenance burden of adopted repos?
- ✅ Which repos have security vulnerabilities we need to address?
- ✅ Which repos will we fork?
- ✅ Which repos will we contribute to?
- ✅ Which repos should we monitor but not adopt yet?

---

## 8. SUCCESS CRITERIA

By end of Month 1:

- ✅ 904 repos ingested, normalized, deduplicated (880-900 remain)
- ✅ All 880+ repos enriched with metadata
- ✅ All 880+ repos classified into capability ontology
- ✅ All 880+ repos scored on 10 dimensions
- ✅ All 880+ repos dispositioned (ADOPT | INTEGRATE | FORK | etc.)
- ✅ Top 50 repos (CRITICAL + HIGH tiers) ready for adoption pipeline
- ✅ Neo4j relationships created (repo → capability → venture → agent)
- ✅ Technology radar published
- ✅ DO_NOT_BUILD registry completed
- ✅ 3-5 repos entered adoption pipeline (sandbox/benchmark/security)

By end of Quarter 1:

- ✅ 5-10 repos ADOPTED and deployed
- ✅ 3-5 repos FORKED and under our control
- ✅ Repository intelligence system operational (weekly monitoring)
- ✅ All ventures have access to capability dependency map
- ✅ All agents can query "which repos enable this capability?"

---

**This is not a project backlog.**

**This is an external R&D and technology intelligence system that feeds your Company Brain.**

The question is never "Should we build this?"

The question is: **"What already exists in the open-source world that we can intelligently incorporate?"**

Your 904 starred repos should become the answer engine for that question.
