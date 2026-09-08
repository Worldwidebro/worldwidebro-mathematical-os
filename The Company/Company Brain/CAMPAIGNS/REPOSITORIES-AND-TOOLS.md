# REPOSITORIES-AND-TOOLS — Owned & Starred Repositories Powering Campaigns

> **Canonical Document ID:** `DOC-REP-CAM-003`  
> **Authority:** Systems Architecture & Capability Mapping (CP-014 / CP-027)  
> **Inventories:** [[_REGISTRIES/OWNED_REPOSITORIES_INVENTORY.md]] · [[_REGISTRIES/RECONCILIATION_2026_09_01/CAPABILITY_DEPENDENCY_MAP.md]]  
> **Status:** ACTIVE REPOSITORY & TOOL DEPENDENCY MAP

---

## 1. Executive Summary: The Technical Asset Foundation

The **Campaign Operating System** is not built from scratch. It is directly powered by **893 owned repositories** and **903 starred open-source repositories (31M+ stars)** cataloged across Company Brain's 10 capability layers.

---

## 2. Owned Repositories Powering Campaigns & Commercial Operations

| Repo Name | Identifier | Category | Role in Campaign Engine |
| :--- | :--- | :--- | :--- |
| **`iza-os-sales-core`** | REP-000559 | Sales & Revenue Core | Complete enterprise CRM, sales pipeline tracker, SOW contract manager, and revenue reconciliation engine. |
| **`iza-os-sales-automation-*-bot`** | REP-000803 to REP-000817 | Agentic Sales Bots | 15 specialized autonomous bots executing discovery, outreach synthesis, monitoring, reporting, and alerting. |
| **`clients`** | REP-000732 | Client Onboarding | Turnkey agreements, mutual NDA contracts, client portal, and automated escrow deposit onboarding. |
| **`omniroute`** | Core Infra | Inference Router | Multi-provider intelligent LLM router with provider fallback, token compression, and cost monitoring. |
| **`civos` / `Company Brain`** | REP-000887 | Knowledge Core | Neo4j knowledge graph (`:7687`), Qdrant semantic vectors (`:6333`), and universal registries. |
| **`graft`** | TOL-000001 | Code Intelligence | Codebase AST graph generation, symbol extraction, and blast-radius calculation (powers Audit Deliverable 2). |
| **`fractal`** | TOL-000002 | Agent Orchestration | Recursive agent decomposition, git worktree isolation, and multi-agent task execution. |
| **`ec-076-ai-sales-forecasting`**| REP-000255 | Commercial Modeling | Probabilistic deal closing velocity and cash flow forecasting. |

---

## 3. Starred Repositories (External Open-Source Dependencies)

The 903 starred repositories (31M+ stars) provide off-the-shelf capabilities that accelerate campaign execution without reinventing wheels (AntiGravity Rule #2):

### 1. Workflow Automation & Outbound Orchestration (28 repos, 1.1M★)
- **`n8n`** (48k★): Visual workflow automation connecting Apollo prospect scraping, email sequencing, CRM updates, and Slack war-room alerts.
- **`trigger.dev`** (`TOL-000016`): Durable execution engine for long-running multi-day email sequence workflows with automatic retry logic.
- **`Dify`** (45k★): Visual agent orchestration for conversational qualification bots.
- **`MoneyPrinterTurbo`** (25k★): Automated technical short video and screencast rendering engine.

### 2. Code Intelligence & Graph Construction (5 repos, 314k★)
- **`graphify`**: Turns complex codebases into structured AST relational knowledge graphs in minutes.
- **`CodeGraph`**: Deep semantic dependency mapping for monorepo architecture.
- **`graphiti`**: Dynamic memory graph for real-time tracking of code changes and agent edits.
- **`LangGraph`**: State-machine cyclic graph runtime for multi-agent reasoning.

### 3. Document Processing & Deliverable Generation (19 repos, 608k★)
- **`Docling`** (12k★): High-precision document parser converting PDFs, repos, and architectural docs into structured Markdown.
- **`Paperclip`**: Automated executive presentation and PDF report generation engine (renders the 48-Hour Audit deliverable).
- **`CLI-Anything`** (`TOL-000012`): Universal CLI wrapper enabling agents to invoke any terminal utility safely.

### 4. Telemetry, Observability & Analytics (3 repos, 228k★)
- **`Grafana` & `Prometheus`**: Real-time observability stack tracking campaign spend burn, conversion funnels, and UTM clicks.
- **`WorldMonitor`**: Global news and market signal tracking engine alerting on competitor moves.

### 5. Autonomous Coding & AI Foundations (130 repos, 3.9M★)
- **`claude-code`** (143k★): Terminal-native agentic coding tool executing audit scripts.
- **`ponytail`** (119k★): Token efficiency and lazy-loading execution patterns.
- **`awesome-llm-apps`** (135k★): Production-ready blueprints for agentic workflows.

---

## 4. Master Links

- Master OS: [[CAMPAIGNS/CAMPAIGN-OS]]
- Owned Repositories: [[_REGISTRIES/OWNED_REPOSITORIES_INVENTORY.md]]
- Starred Repositories: [[_REGISTRIES/RECONCILIATION_2026_09_01/CAPABILITY_DEPENDENCY_MAP.md]]
- Tools Registry: [[_REGISTRIES/ID_REGISTRY.yaml]]
