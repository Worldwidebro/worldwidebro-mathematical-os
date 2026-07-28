# Operating Model: How Work Flows in the Delegation Network

## Core Principle
Work flows downstream. Margins flow upstream. Data flows everywhere.

---

## 1. The 15-Layer OS Architecture

The enterprise infrastructure is organized into 15 modular layers to ensure clear boundaries and ease of agentic traversal:

```text
Layer 01: Fiduciary & Ownership (WinnersCircleWCLLC)
Layer 02: Brand & Distribution (Worldwidebro Network)
Layer 03: Executive Command (AI Boss Holdings / Hermes)
Layer 04: Operating Companies (Sector OpCos)
Layer 05: Venture Factory (Spawner & Templates)
Layer 06: Knowledge Graph (Neo4j / GraphRAG)
Layer 07: Vector Memory (Qdrant / Semantic Cache)
Layer 08: Transactional Database (Supabase)
Layer 09: Orchestration Layer (Fractal / n8n Webhooks)
Layer 10: AI Models & Gateways (LiteLLM / Ollama)
Layer 11: Developer Tooling (Git Worktrees / VEX site builder)
Layer 12: Sales & CRM Engines (Twenty CRM)
Layer 13: Marketing Engines (Automated copy / newsletter compilers)
Layer 14: Analytics & Observability (Grafana / Prometheus / Langfuse)
Layer 15: Security & Guardrails (Metatron / Compliance Scrapers)
```

---

## 2. Progressive Monetization Model

To validate ventures with low capital risk, every business spawned by the Venture Factory follows a standardized three-phase maturation sequence:

```text
           [ v1: CONTENT ]                 [ v2: SERVICES ]                   [ v3: SAAS/PRODUCT ]
      - Landing pages & lead forms     - Manual ops backend by agents      - Full software automation
      - Audience building & SEO        - Invoicing & human approval        - Stripe checkout storefronts
      - Minimal TAM/SAM risk           - Cash-flow neutrality target       - Scaled multi-tenant apps
```

### 2.1 v1 (Content / Attention Acquisition)
- **Goal**: Generate interest and collect lead data.
- **Assets**: VEX frontend landing pages, static newsletters, search engine visibility (SEO).
- **Metric**: Cost per acquisition (CPA), visitor sign-ups.

### 2.2 v2 (Services / Agent-Assisted Operations)
- **Goal**: Deliver immediate value manually using agents to execute tasks.
- **Assets**: Invoicing tools, agentic lead routing, contractor workflows (e.g. automated matching).
- **Metric**: Monthly Recurring Revenue (MRR), delivery speed, customer satisfaction.

### 2.3 v3 (SaaS / Automated Product)
- **Goal**: Productize the service to scale without linear resource additions.
- **Assets**: Medusa commerce engines, self-service dashboard panels, structured APIs.
- **Metric**: Customer lifetime value (LTV), transaction counts, API uptime.

---

## 3. Separation of Concerns: OpCo vs. Venture

- **Operating Companies (OpCos)**: Function as strategic sector divisions (e.g., Construction OpCo, Staffing OpCo). They pool resources, define required capability maps, and report consolidated metrics.
- **Ventures**: Function as isolated startup entities under their parent OpCo (e.g., `con-001-ace-construction`). Each venture maintains separate transactional database records, localized workspace directories (git branches/worktrees), and product configurations to avoid cross-venture data pollution.

---

## 4. Agent Architecture & Autonomy Tiers

### 4.1 Executive & Specialist Personas
- **Hermes (Chief Coordinator)**: High-level strategy, OKR evaluation, and coordination. Routes calls using `auto/smart` (Claude 3.5 Sonnet / GPT-4o).
- **Dexter (CFO Agent)**: Financial auditor. Handles ledger updates and cash-flow projections. Routes calls using `auto/smart` (Claude 3.5 Sonnet).
- **Construction Estimator**: Performs takeoff calculations from blueprints. Routes calls using `auto/coding` (Claude 3.5 Sonnet / DeepSeek Coder).
- **Staffing Recruiter**: Candidate sourcing, vetting, and profile matching. Routes calls using `auto/fast` (GPT-4o-mini).
- **Copywriter (Writing Engine Node)**: Drafts sales copy, email sequences, and articles. Routes calls using `auto/cheap` (DeepSeek Chat / GPT-4o-mini).
- **Pen-Tester (Security Audit)**: Security compliance, vulnerability scanning. Routes calls using `auto/coding`.

### 4.2 Autonomy Levels
Autonomy is graded in five explicit levels based on the risk profile of the task:

| Tier | Name | Description | Fiduciary Boundary |
|---|---|---|---|
| **Level 0** | Ad-Hoc/Manual | Fully controlled by human prompts. No self-triggering. | No capital power. |
| **Level 1** | Read-Only | Runs research/queries. Can draft but cannot write modifications. | No write permissions on main branches. |
| **Level 2** | Reversible Write | Can deploy code drafts, compile VEX, write records, log runs. | Can edit staging; cannot push production. |
| **Level 3** | Semi-Autonomous | Can perform actions, issue invoices, run campaigns < $1K limit. | Auto-approvals for standard SOP events. |
| **Level 4** | Autonomous | Full process execution within set budgets (limit up to $10K). | Capital > $10K requires human review. |

---

## 5. Agent-to-Agent (A2A) Protocols

Agents communicate using JSON-RPC 2.0 payloads.

### 5.1 Request Format
```json
{
  "jsonrpc": "2.0",
  "method": "request_estimate",
  "params": {
    "venture_id": "CON-001",
    "project_scope": "Concrete foundation pour",
    "blueprint_file": "/path/to/blueprint.pdf"
  },
  "id": "req-98745-con"
}
```

### 5.2 Handshake & Retry Logic
1. **Timeout**: The default request timeout limit is **15 seconds** for standard operations and **90 seconds** for complex database updates.
2. **Retry Protocol**: On timeout or network drop, the requesting agent executes up to **3 retries** with exponential backoff (2s, 4s, 8s).
3. **Escalation**: If all retries fail, the requesting agent marks the execution as `blocked` and alerts the director agent.

---

## 6. The 14-Phase Execution Framework

Each venture runs inside a structured lifecycle executor that sequences 14 milestones:

```text
  [Parallel Ingestion]  ──→  [System Integration]  ──→  [Operational Rollout]  ──→  [Scale & Audit]
    - Phase 01: Profile        - Phase 05: Data Match     - Phase 09: SOP Deploy      - Phase 13: Audit
    - Phase 02: Strategy       - Phase 06: APIs Sync      - Phase 10: Launch          - Phase 14: Report
    - Phase 03: Product        - Phase 07: CRM Setup      - Phase 11: Growth Run
    - Phase 04: Market         - Phase 08: Workflows      - Phase 12: Finance Invoicing
```

### 6.1 Status Tracker Inheritance (`STATUS.md` & `venture.json`)
Spawned ventures inherit a root `STATUS.md` tracking development progress (14-phase checklist status: completed `[x]`, in-progress `[/]`, or pending `[ ]`) and a `venture.json` file specifying basic metadata, required capabilities, and funding levels.

---

## 7. Venture Spawner CLI (`create_venture.py`)

The **Venture Factory** spawner CLI automates the creation of new venture folders:

```bash
python3 /Users/acebless/Documents/WORLDWIDEBRO-OS/05-AGENTS/create_venture.py \
  --name "Downtown Builders" \
  --sector "construction" \
  --location "Florida, US" \
  --revenue 150000
```

- **Folder Generation**: Seeds 11 standard directories (`00_IDENTITY` through `14_ANALYTICS`) in `/Users/acebless/Documents/`.
- **Database Logging**: Inserts records into PostgreSQL, merges sector nodes in Neo4j, and logs metadata to `registries/ventures.csv`.
- **VEX Sync**: Updates `portfolio.public.json` inside the VEX project folder and triggers Vercel deployment.
