---
execution_metadata:
  venture_id: "TECH-051-Fraud-Prevention-AI"
  agent_completed: "AG-CEO"
  department: "Operations & Logistics"
  node: "HW-AIR-01"
  database_link: "DB-POSTGRES:PT-5433"
references:
  - [[TECH-051-Fraud-Prevention-AI-AGENT-COMMUNICATION]]
  - [[TECH-051-Fraud-Prevention-AI-FORMATION-CREDENTIAL-TRACKER]]
  - [[SECTOR-REGISTRY]]
---

# Departments & System Ecosystem — Fraud Prevention Ai

This document outlines the department boundary configurations and integration points to the central holding ecosystem.

---

## 1. THE 4 CORE DEPARTMENTS

### Department 1: Operations & Logistics
*   **Responsible Agent:** Operations Agent / CAO
*   **System Boundaries:** Coordinates the core execution loops (e.g. dispatch tracking, storefront catalog checks).

### Department 2: Marketing & Growth
*   **Responsible Agent:** Operations Agent (CRM automations) / Marketing Agent
*   **System Boundaries:** Runs landing page intakes, email lists, and conversion funnel scans.

### Department 3: Sales & Billing
*   **Responsible Agent:** Finance Agent / CFO
*   **System Boundaries:** Integrates Stripe billing nodes, manages client database pipelines, and reconciles invoicing ledgers.

### Department 4: HR & Onboarding
*   **Responsible Agent:** Operations Agent
*   **System Boundaries:** Subcontractor background check logs and internal workforce onboarding.

---

## 2. CENTRAL OS ECOSYSTEM INTEGRATION

Every active venture is interconnected with the centralized control plane:
- **Shared Memory (Qdrant Vector DB)**: Syncs planning notes and repository symbol graphs.
- **Ontology (Neo4j Graph)**: Joins `(Venture: TECH-051-Fraud-Prevention-AI)` to implementing code repositories.
- **State Database (PostgreSQL)**: Reconciles transactional customer objects.
- **Portals (VEX site)**: Automatically publishes metadata to the public portfolio directory.
