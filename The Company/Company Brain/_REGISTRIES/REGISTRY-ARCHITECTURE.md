# REGISTRY ARCHITECTURE
**Master Data & Indexing Blueprint for Company Brain**

**Date:** 2026-09-09  
**Authority:** CP-027 (Infrastructure), CP-013 (Knowledge), All 30 Control Planes

---

## OVERVIEW

**Registries** = authoritative source of truth (what exists)  
**Indexes** = optimized retrieval (how to find/reason over it)  
**Knowledge Graph** = relationships + reasoning (why things matter together)

```
MASTER DATA (PostgreSQL + YAML)
    ↓
REGISTRIES (authoritative inventory)
    ↓
INDEXING LAYER (PostgreSQL + Qdrant + Neo4j)
    ↓
SEARCH / GRAPH / RAG (agent queries)
    ↓
AGENT WORKFORCE (execution)
    ↓
RESULT → KPI → NEW GAP → RESEARCH LOOP
```

---

## 12 REGISTRY DOMAINS

### DOMAIN 1: ORGANIZATION

**Purpose:** Organizational structure, entities, roles, responsibilities

| Registry | Records | Source | Status | Owner |
|----------|---------|--------|--------|-------|
| **Venture Registry** | 789 ventures | `ventures-by-sector.yaml` | ✅ Live | CP-021 |
| **Entity Registry** | LLC, SPV, OpCo structures | Supabase + entity_registry.yaml | 🟡 Partial | CP-001 |
| **Department Registry** | 35 sectors + teams | `SECTOR-TAXONOMY-MASTER.md` | ✅ Live | CP-003 |
| **Role Registry** | Founder, manager, SDR, ops, etc. | role_registry.yaml | 🔴 TODO | CP-003 |
| **Responsibility Registry** | Every function/duty | `RESPONSIBILITY_REGISTRY.yaml` | 🟡 Started | CP-033 |

**Example schema:**

```yaml
# venture_registry.yaml
venture:
  id: OPS-001
  ref_id: "OPS-001"
  machine_id: "01ARZ3NDEKTSV4RRFFQ69G5FAV"  # ULID
  slug: "ops-001-careersops-staffing"
  
  name: "CareerOps Staffing"
  sector: SEC-014
  stage: DEPLOYED
  
  current_owner: founder
  future_owner_role: SDR (trigger: 1000 leads/month)
  
  metrics:
    revenue_mtd: 2500
    revenue_ytd: 2500
    leads_qualified: 8
    conversion_rate: 12.5%
  
  links:
    - repository: Worldwidebro/ops-001-staffing
    - deployment: ops-staff-001-staffing.vercel.app
    - crm: twenty.worldwidebro.local/accounts/OPS-001
    - clickup: worldwidebro.clickup.com/team/xxx/lists
    - neo4j: VENTURE {ref_id: 'OPS-001'}
```

---

### DOMAIN 2: WORKFORCE

**Purpose:** Humans + Agents + their capabilities, permissions, assignments

| Registry | Records | Source | Status | Owner |
|----------|---------|--------|--------|-------|
| **Person Registry** | Employees, contractors | HR system + crm | 🟡 Partial | CP-003 |
| **Agent Registry** | 26+ agents | Agent Roster | ✅ Live (26 agents) | CP-006 |
| **Agent Role Registry** | What each agent does | role_definitions.yaml | 🟡 Partial | CP-006 |
| **Agent Capability Registry** | Agent → Capability mapping | agent_capabilities.yaml | 🟡 Partial | CP-006 |
| **Agent Tool Registry** | 110 OmniRoute tools | OmniRoute API | ✅ Live | CP-007 |
| **Agent Permission Registry** | MCP access controls | permissions.yaml | 🟡 Partial | CP-027 |
| **Human-Agent Assignment Registry** | Responsibility → owner (human/agent) | RESPONSIBILITY_REGISTRY.yaml | 🟡 Started | CP-033 |
| **Delegation Registry** | Founder → Manager → Agent → Worker chains | delegation_registry.yaml | 🔴 TODO | CP-033 |
| **Escalation Registry** | When agent must escalate | escalation_rules.yaml | 🔴 TODO | CP-033 |
| **Agent Evaluation Registry** | Quality/performance metrics | agent_performance.yaml | 🔴 TODO | CP-006 |

**Example schema:**

```yaml
# agent_registry.yaml
agent:
  id: AGT-013
  ref_id: "AGT-013"
  name: "Repository Classifier"
  
  role: capability_classifier
  
  capabilities:
    - repository_analysis
    - code_scanning
    - capability_extraction
    - github_api_queries
  
  tools:
    - mcp: graft_find_code
    - mcp: github_search
    - api: github_rest_v3
    - llm: claude-sonnet-5
  
  permissions:
    - repositories: read
    - github_api: read
    - neo4j: read, write (classifications only)
  
  runs:
    - count: 1247
    - success_rate: 94.2%
    - avg_latency_ms: 2341
  
  evaluation:
    - accuracy: 8.7/10
    - reliability: 9.1/10
    - coverage: 7.2/10
    - cost_efficiency: 9.5/10
    - score: 8.6/10
  
  status: PRODUCTION
  owner: CP-006 (Agent Control Plane)
```

---

### DOMAIN 3: CAPABILITY

**Purpose:** What the organization can do, what it cannot, what needs research

| Registry | Records | Source | Status | Owner |
|----------|---------|--------|--------|-------|
| **Capability Registry** | 300+ capabilities | `CAPABILITY_REGISTRY.yaml` | ✅ Live | CP-009 |
| **Tool Registry** | 110 OmniRoute tools + CLI + APIs | OmniRoute export | ✅ Live | CP-007 |
| **API Registry** | 95 Vercel + external APIs | `SITES_REGISTRY.yaml` + URLs | ✅ Live | CP-008 |
| **MCP Registry** | MCP servers + tools | MCP config | ✅ Live (32 MCPs) | CP-027 |
| **Skill Registry** | 296+ Claude Code skills | `/skills` directory | ✅ Live | CP-009 |
| **Gap Registry** | Missing capabilities | `gaps_detected` table | 🟡 Started (Phase 3) | CP-009 |

**Example schema:**

```yaml
# capability_registry.yaml
capability:
  id: CAP-042
  ref_id: "CAP-042"
  slug: workflow-orchestration
  
  name: "Workflow Orchestration"
  description: "Automate multi-step business processes"
  
  category: automation
  layer: execution
  
  current_status:
    owned: false
    external: true
    provider: n8n
    cost_monthly: 0  # self-hosted
    reliability: 99.9%
    maturity: production
  
  implementation:
    - option: n8n (self-hosted)
      status: ADOPTED
      cost_monthly: 0
      effort_to_adopt: 2 weeks
      maintenance_burden: medium
      reliability: 99.9%
      scalability: 500+ workflows
    
    - option: zapier
      status: REFERENCE
      cost_monthly: 50-500
      effort_to_adopt: 1 week
      maintenance_burden: low
      reliability: 99.95%
      scalability: limited
    
    - option: make.com
      status: REFERENCE
      cost_monthly: 12-500
      effort_to_adopt: 1 week
      maintenance_burden: low
      reliability: 99.9%
      scalability: good
  
  uses:
    - form_submission_to_clickup
    - stripe_payment_to_neo4j
    - task_completion_routing
    - daily_metrics_aggregation
  
  evaluation:
    - score: 8.4/10
    - evidence: [test_result_001, benchmark_034]
    - decision_date: 2026-09-14
    - decision_id: DEC-000127
  
  owner: CP-027 (Infrastructure)
  next_review: 2026-12-09
```

---

### DOMAIN 4: SOFTWARE

**Purpose:** Repository universe (1,740 owned + 904 external), software inventory, dependencies

| Registry | Records | Source | Status | Owner |
|----------|---------|--------|--------|-------|
| **Repository Registry** | 1,740 owned repos | GitHub API | ✅ Live | CP-008 |
| **Repository Fork Registry** | Which repos are forks | GitHub API | ✅ Live | CP-008 |
| **Repository Dependency Registry** | Package.json, requirements.txt, etc. | AST parsing | ✅ Live | CP-008 |
| **Repository Capability Registry** | Repo → Capability mapping | REPOSITORY_REGISTRY.yaml | 🟡 Partial (28 repos) | CP-008 |
| **Repository Architecture Registry** | Architecture patterns, layers | graft analysis | 🟡 Partial | CP-008 |
| **Repository Deployment Registry** | Repo → Vercel/Railway/etc | `REPO_TO_VERCEL_MAPPING.yaml` | ✅ 95 sites live | CP-008 |
| **Repository Source Registry** | 904 external repos from awesome lists | awesome_sources.yaml | 🟡 Started | CP-008 |
| **Repository Health Registry** | Maintenance, activity, security | GitHub API health checks | 🟡 Partial | CP-008 |
| **Package Registry** | npm, PyPI, gem, crate packages | Package managers | 🟡 Started | CP-008 |
| **Skill Registry** | 296 Claude Code skills | `/skills` directory | ✅ Live | CP-009 |
| **MCP Tool Registry** | 110 exposed OmniRoute tools | OmniRoute API | ✅ Live | CP-007 |

**Example schema:**

```yaml
# repository_registry.yaml
repository:
  id: REP-000247
  ref_id: "REP-000247"
  machine_id: "01ARZ3NDEKTSV4RRFFQ69G5FAV"
  
  name: "worldwidebro-vex"
  slug: "vex"
  
  github:
    url: "https://github.com/Worldwidebro/Worldwidebro-Vex"
    owner: Worldwidebro
    repo: Worldwidebro-Vex
    stars: 47
    forks: 2
    last_commit: 2026-09-08T14:32:00Z
    language: TypeScript
    license: MIT
  
  classification:
    primary_capability: venture_portal
    secondary_capabilities:
      - cap_table_management
      - portfolio_analytics
      - investor_dashboard
    
    architecture_layer: frontend
    tier: mission_critical
    maturity: production
  
  deployment:
    url: https://vex-hero-site-sigma.vercel.app
    status: live
    environment: production
    vercel_project_id: XXX
  
  relationships:
    ventures_using:
      - OPS-001
      - LT-005
      - LT-011
      - RE-001
      - EC-001
    
    dependencies:
      - next.js 14
      - supabase
      - stripe
      - twenty (crm)
    
    used_by:
      - AGT-006 (portfolio analyzer)
      - AGT-008 (investor reporter)
  
  metrics:
    health_score: 8.7/10
    security_score: 8.9/10
    activity_score: 9.1/10
    documentation_score: 7.8/10
  
  owner: CP-008 (Software Architecture)
  next_review: 2026-10-09
```

---

### DOMAIN 5: KNOWLEDGE

**Purpose:** Organizational memory, decisions, processes, SOPs, policies

| Registry | Records | Source | Status | Owner |
|----------|---------|--------|--------|-------|
| **Document Registry** | 1,000+ documents | Obsidian vault + Google Drive | ✅ Live | CP-013 |
| **Decision Registry** | Architectural decisions (ADRs) | `_REGISTRIES/decisions/` | 🟡 Started | CP-027 |
| **Process Registry** | Business processes | `_REGISTRIES/processes/` | 🔴 TODO | CP-033 |
| **SOP Registry** | Standard operating procedures | CLAUDE.md + runbooks | ✅ Live (partial) | CP-033 |
| **Policy Registry** | Operating rules, compliance | RESPECT + ANTIGRAVITY | ✅ Live | CP-027 |
| **Meeting Registry** | Meeting notes, decisions | Obsidian vault | 🟡 Partial | CP-013 |
| **Conversation Registry** | Important conversations | Claude session logs | 🟡 Partial (session-based) | CP-013 |

**Example schema:**

```yaml
# decision_registry.yaml
decision:
  id: DEC-000127
  ref_id: "DEC-000127"
  date_decided: 2026-09-09
  
  question: "Which workflow orchestration system to use?"
  
  options_evaluated:
    - make.com
    - n8n
    - zapier
    - temporal
  
  evidence:
    - candidate_research_001
    - performance_benchmark_034
    - security_audit_089
  
  decision: "Adopt n8n (self-hosted)"
  
  rationale: |
    Best balance of:
    - Control (self-hosted vs. vendor lock-in)
    - Cost (free vs. $50-500/mo)
    - Community (active, 500+ integrations)
    - Maintenance burden (sustainable for current team)
  
  alternatives:
    - make.com: "Good for low-code, but higher cost"
    - zapier: "Most user-friendly, highest vendor lock-in"
    - temporal: "Overkill for current workflow complexity"
  
  owner: CP-027 (Infrastructure)
  approval: founder
  status: APPROVED
  
  implementation:
    owner: DevOps
    start_date: 2026-09-14
    target_date: 2026-09-28
    status: queued
  
  review_trigger: "2026-12-09 (90 days)"
  review_date: null
  
  tags:
    - infrastructure
    - automation
    - workflow
```

---

### DOMAIN 6: RESEARCH

**Purpose:** Gap detection, capability discovery, awesome lists, experiments, benchmarks

| Registry | Records | Source | Status | Owner |
|----------|---------|--------|--------|-------|
| **Gap Registry** | 50+ identified gaps | autonomous gap_detector | 🟡 Started (Phase 3) | CP-009 |
| **Research Question Registry** | Questions being investigated | research_questions.yaml | 🔴 TODO | CP-009 |
| **Awesome List Registry** | 20+ curated source lists | awesome_sources.yaml | 🟡 Started | CP-008 |
| **Research Candidate Registry** | 200+ evaluated projects | candidate_evaluation.yaml | 🟡 Partial | CP-008 |
| **Research Evidence Registry** | Evaluation scores, benchmarks | evidence_table | 🟡 Partial | CP-008 |
| **Research Finding Registry** | Conclusions from research | findings.yaml | 🔴 TODO | CP-009 |
| **Experiment Registry** | Tests, benchmarks, trials | experiment_registry.yaml | 🟡 Partial | CP-008 |

**Example schema:**

```yaml
# gap_registry.yaml
gap:
  id: GAP-000421
  ref_id: "GAP-000421"
  date_detected: 2026-09-08
  
  statement: "No reliable system for orchestrating multi-step workflows"
  
  type: missing_capability
  domain: automation
  severity: high
  
  business_impact_dollars: 50000  # estimated savings if fixed
  
  current_workaround: "Manual ClickUp + email follow-ups"
  
  required_for:
    - ventures:
      - OPS-001
      - CON-001
      - LT-005
      - LT-011
      - RE-001
      - EC-001
  
  target_state:
    coverage: 95%
    description: "Automated form → ClickUp → Stripe → Neo4j with <10s latency"
  
  research:
    status: in_progress
    awesome_lists:
      - awesome-workflow
      - awesome-automation
      - awesome-api-integration
    
    candidates_found: 47
    candidates_evaluated: 12
    finalists: 3
    
    decision_deadline: 2026-09-14
  
  decision:
    id: DEC-000127
    status: approved
    chosen_capability: workflow_orchestration
    chosen_tool: n8n
  
  implementation:
    phase: phase_2
    start_date: 2026-09-14
    target_date: 2026-09-28
    owner: DevOps
    status: queued
  
  owner: CP-009 (Capability Control Plane)
```

---

### DOMAIN 7: INFRASTRUCTURE

**Purpose:** Servers, containers, databases, deployments, environments

| Registry | Records | Source | Status | Owner |
|----------|---------|--------|--------|-------|
| **Machine Registry** | 2 Mac devices, services | hardware_inventory.yaml | ✅ Live | CP-027 |
| **Service Registry** | Neo4j, Qdrant, PostgreSQL, etc. | docker-compose.yml | ✅ Live | CP-027 |
| **Environment Registry** | Prod, staging, local | environment_config.yaml | ✅ Live | CP-027 |
| **Deployment Registry** | 95 Vercel projects | `SITES_REGISTRY.yaml` | ✅ Live | CP-008 |
| **Database Registry** | PostgreSQL, Neo4j, Qdrant | database_inventory.yaml | ✅ Live | CP-013 |
| **Storage Registry** | S3, local storage, LaCie | storage_inventory.yaml | ✅ Live | CP-027 |
| **Network Registry** | Tailscale, DNS, domains | network_config.yaml | ✅ Live | CP-027 |

---

### DOMAIN 8: DATA

**Purpose:** Datasets, schemas, pipelines, lineage, quality

| Registry | Records | Source | Status | Owner |
|----------|---------|--------|--------|-------|
| **Dataset Registry** | Supabase tables, CSV exports | Supabase metadata | ✅ Live | CP-013 |
| **Data Schema Registry** | Table schemas, field definitions | schema_registry.yaml | 🟡 Partial | CP-013 |
| **Data Pipeline Registry** | ETL workflows, ingestion | pipeline_registry.yaml | 🟡 Partial | CP-013 |
| **Data Lineage Registry** | Source → transform → sink | data_lineage.yaml | 🔴 TODO | CP-013 |
| **Data Quality Registry** | Freshness, accuracy, completeness | quality_metrics.yaml | 🟡 Partial | CP-013 |

---

### DOMAIN 9: AI/ML

**Purpose:** Models, prompts, fine-tunes, evaluations, routing decisions

| Registry | Records | Source | Status | Owner |
|----------|---------|--------|--------|-------|
| **Model Registry** | 20+ LLMs available | model_inventory.yaml | ✅ Live | CP-007 |
| **Model Provider Registry** | OpenAI, Anthropic, exo, Ollama | provider_config.yaml | ✅ Live | CP-007 |
| **Model Capability Registry** | Model → task mapping | model_capability_matrix.yaml | ✅ Live | CP-007 |
| **Prompt Registry** | 100+ operational prompts | `_PROMPTS/` directory | ✅ Live | CP-009 |
| **Prompt Version Registry** | Version history of prompts | prompt_versions.yaml | 🟡 Partial | CP-009 |
| **Embedding Model Registry** | nomic-embed, ada, etc. | embedding_registry.yaml | ✅ Live | CP-013 |
| **Evaluation Registry** | Test results, benchmarks | evaluation_results.yaml | 🟡 Partial | CP-009 |

---

### DOMAIN 10: FINANCE

**Purpose:** Capital, deals, investors, revenue, costs

| Registry | Records | Source | Status | Owner |
|----------|---------|--------|--------|-------|
| **Customer Registry** | 12 customers across ventures | CRM (Twenty) | 🟡 Partial | CP-021 |
| **Deal Registry** | Open/closed deals, value | deal_payments table | ✅ Live | CP-021 |
| **Invoice Registry** | Sent and paid invoices | accounting system | 🟡 Partial | CP-020 |
| **Investment Registry** | Cap table, ownership, funding | cap_table.yaml | ✅ Live | CP-020 |
| **Expense Registry** | Operating costs, spend | accounting system | 🟡 Partial | CP-020 |
| **Revenue Registry** | MRR, ARR, customer value | revenue_tracking.yaml | ✅ Live (via Stripe) | CP-021 |

---

### DOMAIN 11: SECURITY

**Purpose:** Identity, permissions, secrets, vulnerabilities, audit trails

| Registry | Records | Source | Status | Owner |
|----------|---------|--------|--------|-------|
| **Identity Registry** | Users, service accounts | Bitwarden + Auth | ✅ Live | CP-030 |
| **Permission Registry** | Role-based access control | permission_matrix.yaml | 🟡 Partial | CP-030 |
| **Secret Reference Registry** | Pointers to Bitwarden/vault (not the secrets!) | secret_references.yaml | ✅ Live | CP-030 |
| **API Key Registry** | API key references (not keys themselves) | api_key_references.yaml | ✅ Live | CP-030 |
| **Vulnerability Registry** | Security issues, status | vulnerability_registry.yaml | 🔴 TODO | CP-030 |
| **Audit Log Registry** | Who did what when | PostgreSQL audit_logs table | ✅ Live | CP-030 |
| **Compliance Registry** | Regulatory requirements | compliance_checklist.yaml | 🟡 Partial | CP-030 |

---

### DOMAIN 12: OPERATIONS

**Purpose:** Workflows, automations, triggers, jobs, executions

| Registry | Records | Source | Status | Owner |
|----------|---------|--------|--------|-------|
| **Workflow Registry** | 4 core n8n workflows (Phase 2) | n8n export | 🟡 Started | CP-033 |
| **Automation Registry** | Trigger → action mappings | automation_rules.yaml | 🟡 Partial | CP-033 |
| **Schedule Registry** | Recurring jobs, cron times | schedule_registry.yaml | 🟡 Partial | CP-033 |
| **Job Registry** | Execution history | job_executions table | ✅ Live (via Langfuse) | CP-033 |
| **Test Registry** | Test cases, suites, results | test_registry.yaml | 🟡 Partial | CP-009 |
| **Incident Registry** | Bugs, failures, resolutions | incident_registry.yaml | 🟡 Partial | CP-030 |

---

## INDEXING LAYER

Registries live in PostgreSQL + YAML. Indexes optimize retrieval:

| Index Type | Technology | Purpose | Current Status |
|---|---|---|---|
| **Full-text search** | PostgreSQL FTS | Find documents, code, decisions | ✅ Live |
| **Semantic search** | Qdrant vectors | Find by meaning, not keywords | ✅ Live (17,236 vectors) |
| **Graph traversal** | Neo4j | Relationships and dependencies | ✅ Live (20,363 edges) |
| **Global search** | Meilisearch or Typesense | Fast cross-registry search | 🔴 TODO |
| **Code search** | graft / Qdrant | Find code patterns, functions | ✅ Live (via graft) |

---

## NEO4J RELATIONSHIP SCHEMA

All registries connect in Neo4j:

```cypher
(VENTURE)-[:HAS_RESPONSIBILITY]->(RESPONSIBILITY)
(RESPONSIBILITY)-[:OWNED_BY]->(PERSON|AGENT)
(PERSON|AGENT)-[:HAS_CAPABILITY]->(CAPABILITY)
(CAPABILITY)-[:USES_TOOL]->(TOOL)
(TOOL)-[:EXPOSED_BY]->(MCP_SERVER)
(CAPABILITY)-[:IMPLEMENTED_BY]->(REPOSITORY)
(REPOSITORY)-[:CREATED_FROM]->(RESEARCH)
(RESEARCH)-[:RESOLVES]->(GAP)
(GAP)-[:BLOCKS]->(GOAL)
(GOAL)-[:BELONGS_TO]->(VENTURE)
(RESPONSIBILITY)-[:TRACKED_BY]->(WORKFLOW)
(WORKFLOW)-[:MEASURES]->(KPI)
(KPI)-[:REVEALS]->(NEW_GAP)
```

This closes the loop: **Goal → Gap → Research → Agent → Action → Result → New Gap**

---

## TIER 1 REGISTRIES TO BUILD IMMEDIATELY

**Critical path for Phase 2-3:**

1. ✅ **Responsibility Registry** — human + agent ownership (started)
2. ✅ **Agent Registry** — 26 agents listed (live)
3. ✅ **Capability Registry** — 300+ capabilities (live)
4. ✅ **Tool Registry** — 110 OmniRoute tools (live)
5. ✅ **Repository Registry** — 1,740 repos (live)
6. 🟡 **Gap Registry** — autonomous detection (Phase 3)
7. 🟡 **Research Registry** — awesome lists + candidates (Phase 3)
8. 🟡 **Decision Registry** — ADRs and choices (Phase 2)
9. 🟡 **Workflow Registry** — n8n workflows (Phase 2)
10. 🟡 **Test Registry** — verification framework (Phase 2)
11. ✅ **Deployment Registry** — 95 Vercel sites (live)
12. 🟡 **Agent Evaluation Registry** — quality metrics (Phase 3)
13. 🟡 **Agent Assignment Registry** — human-agent pairs (Phase 2-3)
14. 🟡 **SOP Registry** — operational procedures (Phase 2)
15. 🟡 **Awesome List Registry** — research sources (Phase 3)

---

## IMPLEMENTATION PHASES

### Phase 2 (Sep 14-28): Wire Core Registries
- [ ] Deploy Decision Registry (ADRs in Neo4j)
- [ ] Deploy Workflow Registry (n8n workflows)
- [ ] Deploy Responsibility Registry (finalize human-agent pairs)
- [ ] Deploy Test Registry (verification framework)
- [ ] Wire all 4 domains via Neo4j relationships

### Phase 3 (Oct 1-31): Autonomous Discovery
- [ ] Deploy Gap Registry (autonomous detection)
- [ ] Deploy Research Registry (awesome lists)
- [ ] Deploy Research Candidate Registry (scoring results)
- [ ] Deploy Agent Evaluation Registry (quality metrics)
- [ ] Activate gap → research → decision loop

### Phase 4 (Nov 1-Dec 31): Scale
- [ ] Deploy remaining Tier 2 registries (models, APIs, processes)
- [ ] Wire all 12 registry domains
- [ ] Activate full Neo4j relationship graph
- [ ] Enable AI-native queries across all registries

---

## HOW REGISTRIES FEED THE LOOP

```
RESPONSIBILITY
    ↓
"I own sales research"
    ↓
AGENT_ASSIGNMENT_REGISTRY
    ↓
"Research Agent handles discovery"
    ↓
AGENT_REGISTRY
    ↓
AGT-017 (research_executor)
    ↓
AGENT_CAPABILITY_REGISTRY
    ↓
"Can query awesome lists"
    ↓
AWESOME_LIST_REGISTRY
    ↓
[20 curated lists]
    ↓
RESEARCH_CANDIDATE_REGISTRY
    ↓
[200+ evaluated projects]
    ↓
RESEARCH_EVIDENCE_REGISTRY
    ↓
[scored by evidence_scorer]
    ↓
DECISION_REGISTRY
    ↓
"ADOPT n8n"
    ↓
CAPABILITY_REGISTRY
    ↓
"workflow_orchestration = implemented"
    ↓
REPOSITORY_REGISTRY
    ↓
"Worldwidebro/n8n-orchestrator deployed"
    ↓
DEPLOYMENT_REGISTRY
    ↓
"n8n running on Mac Studio"
    ↓
WORKFLOW_REGISTRY
    ↓
[4 core workflows executing]
    ↓
JOB_REGISTRY
    ↓
[traced via Langfuse]
    ↓
KPI_REGISTRY
    ↓
"Form-to-dashboard latency: 7 seconds"
    ↓
METRIC_ALERT
    ↓
NEW_GAP: "Latency > 10 seconds"
    ↓
(loop closes, research starts again)
```

---

## WIKI LINKS & SECTOR TAXONOMY INTEGRATION

All registries reference wiki links for navigation:

```yaml
capability_registry:
  entry:
    id: CAP-042
    links:
      - wiki: "[[workflow-orchestration]]"
      - sector: "[[SEC-001]] to [[SEC-035]]"
      - venture: "[[OPS-001]], [[LT-005]], [[CON-001]]"
      - repository: "[[Worldwidebro/worldwidebro-vex]]"
      - agent: "[[AGT-017]] (research), [[AGT-019]] (orchestration)"
      - decision: "[[DEC-000127]]"
      - awesome_list: "[[awesome-workflow]], [[awesome-automation]]"
```

Every registry entry is **machine-readable** (YAML/JSON) + **human-navigable** (Obsidian wiki links).

---

## WHO OWNS WHAT

| Registry Domain | Control Plane | Owner |
|---|---|---|
| Organization | CP-001, CP-003 | Chief of Staff |
| Workforce | CP-006, CP-033 | Agent / Operations lead |
| Capability | CP-009 | CTO |
| Software | CP-008 | Software architect |
| Knowledge | CP-013 | Chief Knowledge Officer |
| Research | CP-009 | Research lead |
| Infrastructure | CP-027 | Infrastructure lead |
| Data | CP-013 | Data architect |
| AI/ML | CP-007 | AI lead |
| Finance | CP-020, CP-021 | CFO / RevOps |
| Security | CP-030 | Security lead |
| Operations | CP-033 | Operations lead |

---

## STATUS SUMMARY

**Live (✅):** 5 domains + foundation registries (35% complete)

**In Progress (🟡):** 7 domains + most registries started (35% complete)

**TODO (🔴):** 4 domains + critical research automation (30% complete)

**By end of Phase 3:** 95% of Tier 1 registries operational

**By end of Phase 4:** All 12 domains wired, full graph operational

---

**Next:** Integrate registries into Phase 2 implementation roadmap

