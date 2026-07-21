# DECISION RULES & RACI
## Capital Reallocation, Operational Clearances, and Agent Autonomy

---

## 1. Capital Allocation Gates
Fiduciary decisions inside the ecosystem are governed by strict capital thresholds to protect holding assets:

| Amount | Authority Level | Routing Process |
| :--- | :--- | :--- |
| **&lt; $50,000** | Level 1: Agent Autonomy | Automatically approved by the agent execution engine. logged to Postgres and Langfuse. |
| **$50,000 - $250,000** | Level 2: Executive AI | Requires AI Boss Holdings Command Center approval. Runs RACI check with Strategy and Risk agents. |
| **&gt; $250,000** | Level 3: Board Steering | Escalates to human board steering committee. Requires multi-signature cryptographic authorization. |

---

## 2. RACI Matrix for Venture Spawner Tasks

The creation and operation of new businesses follow a structured Responsibility Assignment matrix:

| Stage | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
| :--- | :--- | :--- | :--- | :--- |
| **Ideation & TAM** | Strategy Analyst Agent | Chief Executive Agent | Research Agent | Board / CFO |
| **Prerequisite Audit** | Risk Agent | Chief Operations Agent | Security Agent | Engineering |
| **Core Dev Spawning** | DevOps Agent / CLI Spawner | Chief Technology Agent | Backend / QA Agents | Project Manager |
| **Marketing Setup** | Brand Agent | Marketing Director | Content Scrapers | Sales / Support |
| **Capital Allocation** | Accountant Agent | CFO Agent | Board Steering | Strategy |

---

## 3. Decision Frameworks
All Level 2 decisions must employ one of the following structured cognitive frameworks:
- **RACI + Pre-Mortem**: Modeled risk profile, downside exposure mapping, and operational bottlenecks mitigation.
- **Weighted Scoring Matrix**: Mathematical trade-off scoring of multiple LLM providers or vendor options.
- **ROI Impact Assessment**: Financial projection testing against historical portfolio metrics.
