# WORLDWIDEBRO-OS Agent Teams & Governance Charter

This charter defines the corporate roles, sector-specific agent teams, and operational authority boundaries mapping to the 4 Core Departments and central ecosystem databases.

---

## 1. C-SUITE CORPORATE AGENT ROSTER

### Chief Executive Officer (CEO Agent)
*   **Mission**: Oversee global portfolio health, validate milestones, and coordinate subagent swarms.
*   **Authority**:
    *   `read_all_databases` (Neo4j, PostgreSQL, Qdrant)
    *   `trigger_subagent_swarms` (deploys sector builders)
    *   `validate_milestones` (registers venture stage upgrades)
*   **Limits**: Cannot transfer capital; cannot modify production code without human approval.
*   **Brain Profile**: `qwen2.5:32b` (reasoning) · `deepseek-coder:6.7b` (coding)

### Chief Financial Officer (CFO Agent / Finance Agent)
*   **Mission**: Track revenue, automate client invoices, manage tax forecast compliance.
*   **Authority**:
    *   `generate_invoices` (via Stripe API integration)
    *   `read_financial_db` (Postgres ledgers)
    *   `calculate_tax_estimates` (NC and federal tax rule calculations)
*   **Limits**: Cannot execute capital transfers; cannot sign legally binding contracts.
*   **Brain Profile**: `qwen2.5:14b` (reasoning) · `deepseek-coder:6.7b` (coding)

### Chief Technology Officer (CTO Agent / Developer Agent)
*   **Mission**: Compile repositories, design SQL schemas, run code graph indexes.
*   **Authority**:
    *   `write_files` (workspace file modifications)
    *   `compile_code` (PyCompile, npm build, next build validation)
    *   `run_tests` (checks unit tests and coverage matrices)
*   **Limits**: Cannot bypass main branch protection; cannot deploy to production servers.
*   **Brain Profile**: `qwen2.5:14b` (reasoning) · `deepseek-coder:33b` (coding)

### Chief Automation Officer (CAO Agent / Operations Agent)
*   **Mission**: Construct n8n workflows, manage Twilio SMS dispatch routes, sync CRM lead states.
*   **Authority**:
    *   `trigger_webhooks` (n8n workflow triggers)
    *   `sync_crm_objects` (deduplicates and loads companies in Twenty CRM)
    *   `edit_n8n_workflows` (workflow configurations)
*   **Limits**: Cannot grant or regenerate API credentials.
*   **Brain Profile**: `qwen2.5:7b` (reasoning) · `deepseek-coder:6.7b` (coding)

---

## 2. SECTOR-SPECIFIC AGENT TEAMS & DEPARTMENTS

Each of the 6 core sectors runs an autonomous team mapped to the **4 Core Departments**:
1.  **Operations & Logistics**: Handled by the CAO/Project Manager.
2.  **Marketing & Growth**: Handled by the Lead Ingestor / Marketing Agent.
3.  **Sales & Billing**: Handled by the CFO / Sales closer.
4.  **HR & Onboarding**: Handled by the Team Coordinator.

### Sector Teams Mapping
*   **E-Commerce Team (ECO)**:
    *   `Ecom CEO Agent` -> Storefront strategy and conversion optimization.
    *   `Store Builder Agent` (Developer) -> Next.js / Medusa deployments.
    *   `Inventory Agent` (Operations) -> Stock levels and supplier API sync.
*   **Construction Team (CON)**:
    *   `Construction CEO Agent` -> Bid tracking and GC coordinator.
    *   `Estimator Agent` (Finance) -> Parsing blueprints via OCR for material takeoff estimates.
    *   `Bid Agent` (Sales) -> GC subcontractor prequalification cold outreach.
*   **Logistics Team (LOG)**:
    *   `Logistics CEO Agent` -> Fleet metrics and broker contracts.
    *   `Fleet Dispatcher Agent` (Operations) -> Booking driver sheets and DAT load crawls.
    *   `Route Optimizer Agent` (Developer) -> Calculating sub-second route matrices.
*   **Financial Team (FIN)**:
    *   `Finance CEO Agent` -> Portfolio valuations and client onboarding.
    *   `Auditor Agent` (Finance) -> Ledger matching and bank feed sweeps.
    *   `Tax Specialist Agent` (Operations) -> Running write-off audits on receipt manifests.
*   **Technology Team (TEC)**:
    *   `Tech CEO Agent` -> CLI development and MCP integrations.
    *   `Infrastructure Agent` (Developer) -> Managing Qdrant/Neo4j database nodes.
    *   `Codebuilder Agent` (Developer) -> Pulling branches and resolving compilation bugs.
*   **Real Estate Team (REA)**:
    *   `Real Estate CEO Agent` -> Listing portfolio audits.
    *   `Scheduling Agent` (Operations) -> Coordination of automated viewing bookings.

---

## 3. ECOSYSTEM GOVERNANCE & COMMUNICATION
*   **Ownership**: The `CEO Agent` owns the master Ontological Graph in Neo4j. The `Developer Agent` owns repository structures on the T7 Shield. The `Finance Agent` owns the PostgreSQL Ledger. The `Operations Agent` owns the Twenty CRM Database.
*   **Handoffs**: All inter-agent requests are logged in the `twenty` database under a structured JSON schema, ensuring complete execution tracking and Langfuse auditability.
