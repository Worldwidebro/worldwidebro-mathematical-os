# 👥 JOBS AND ROLES: HUMAN-AGENT SYSTEM DIRECTORY

This document details the mapping of **Human Leadership Roles**, **AI Agent Roles**, and **System Intelligence Capabilities** across the AVS holding company.

```
┌─────────────────────────────────────────────────────────┐
│              TIER 1: HUMAN EXECUTIVE LEADERSHIP         │
│                 (CEO, COO, CFO, Head of Sales)          │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│              TIER 2: HUMAN SECTOR MANAGERS              │
│         (Tech Manager, Construction Manager, etc.)      │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│                 TIER 3: AI AGENT WORKFORCE              │
│      (Venture CEO Agents, Estimator Agents, PM Agents)   │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│              SYSTEM INTELLIGENCE CAPABILITIES           │
│        (Descriptive, Relational, Predictive, Meta)      │
└─────────────────────────────────────────────────────────┘
```

---

## 🏛️ TIER 1: HUMAN EXECUTIVE LEADERSHIP (Authority 10-8)

Executive leaders set strategic direction, establish capital parameters, and handle final authorization thresholds.

| Position | Position Code | Authority | Approval Limit | Core Focus |
|---|---|---|---|---|
| **CEO / Founder** | `POS-CEO-001` | 10 | $999,999 | Portfolio vision, strategic partnerships, major capital allocation. |
| **COO / Operations** | `POS-COO-001` | 9 | $500,000 | Project coordination across sectors, quality assurance, daily operations. |
| **CFO / Finance** | `POS-CFO-001` | 9 | $500,000 | Financial close, cash flow, revenue forecasting, vendor payables. |
| **Head of Sales** | `POS-SALES-HEAD` | 8 | $200,000 | Lead generation strategy, deal closing, sector messaging. |

---

## 🏗️ TIER 2: HUMAN SECTOR MANAGERS (Authority 6-5)

Sector managers coordinate vendor networks, handle client onboarding, and oversee group-level performance KPIs.

| Sector | Position Code | Authority | Scope | Core Focus |
|---|---|---|---|---|
| **Tech & Software** | `POS-TECH-MANAGER` | 6 | `TECH-001` to `TECH-120` | Tech stack selection, API integrations, SaaS rollout. |
| **Beauty & Wellness** | `POS-BEAUTY-MANAGER` | 6 | `BW-001` to `BW-087` | Booking systems, inventory, local store logistics. |
| **Construction** | `POS-CON-MANAGER` | 6 | `CON-001` to `CON-050` | Sub-contractor management, job site safety, bidding. |
| **Courier & Logistics** | `POS-LOG-MANAGER` | 6 | `LT-001` to `LT-030` | Dispatch routing, driver onboarding, billing compliance. |

---

## 🤖 TIER 3: AI AGENT WORKFORCE (Autonomous Execution)

AI agents handle high-velocity, repetitive operational tasks. They operate under strict sandbox and database limits.

### A. Venture-Level Agents (Dynamic Workflows)
*   **Venture CEO Agent**: Orchestrates daily venture tasks, coordinates sub-agents, logs decisions.
    *   *Tools*: Database read/write, clickup-integration.
    *   *Model*: Qwen 2.5 (7B/32B).
*   **Estimator Agent**: Parses customer job blueprints/forms and generates material cost estimates.
    *   *Tools*: PDF parser, calculator.
    *   *Model*: Qwen 2.5.
*   **Bidding Agent (Sales)**: Compiles bids, submits proposals to prospects, drafts contract templates.
    *   *Tools*: Email client, docuseal-api.
    *   *Model*: Qwen 2.5 / Claude.
*   **Project Manager Agent (Operations)**: Tracks project tasks, alerts human managers on delays, coordinates driver/builder availability.
    *   *Tools*: Telemetry logs, task manager.

### B. Global System Utility Agents
*   **CTO Agent**: Manages codebase files, runs sandbox checks, and tests code integration.
    *   *Tools*: git-mcp, filesystem-mcp, terminal sandbox.
    *   *Model*: Claude Code.
*   **CFO Agent**: Analyzes transaction sheets, generates tax optimization logs, and executes spreadsheet ledger tasks.
    *   *Tools*: database-mcp, python-calc.
    *   *Model*: Claude 3.5 Sonnet.
*   **Research Agent**: Scrapes the web for contact info, competitor analysis, and industry datasets.
    *   *Tools*: firecrawl, tavily-search.
    *   *Model*: Gemini 3.5 Flash / Claude.

---

## 🧠 TIER 4: SYSTEM INTELLIGENCE DOMAINS (The Control Layer)

Rather than standalone agents, these are system-wide capabilities operating over the graphs to assist humans and agents:

1.  **Descriptive (Inventory)**: Knows what repositories, ventures, and assets exist.
2.  **Structural**: Understands module-level dependencies and required capability schemas.
3.  **Relational (Neo4j)**: Discovers cross-file, cross-venture, and cross-contact relationships.
4.  **Causal (Langfuse)**: Identifies the mechanism behind operational failures or revenue gains.
5.  **Predictive**: Computes success rates, churn rates, and code reusability indexes.
6.  **Prescriptive (Decisions)**: Advises human executives on capacity routing and capital allocation.
7.  **Compounding (Memory)**: Stores valid playbooks to ensure previous mistakes are never repeated.
