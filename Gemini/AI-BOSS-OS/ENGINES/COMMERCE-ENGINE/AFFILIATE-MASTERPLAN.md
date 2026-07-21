# Affiliate Masterplan: Commission Engine & Databases

This document outlines the architecture for the **Affiliate Commission Engine**, mapping high-margin third-party tools to target content pillars.

---

## 1. Database Schema

The Affiliate database tracks active programs, payouts, links, and content matching hooks:

```text
AFFILIATE-DATABASE
├── Category: AI Tools, SaaS, Technology, Business, Education, Hardware
├── Program Name
├── Commission Rate (%)
├── Redirect Link
└── Content Opportunities (Target Hook Ideas)
```

---

## 2. Core Affiliate Programs Matrix

Our media network prioritizes SaaS and developer tools with recurring commission models:

| Category | Target Tool | Commission Model | Content Angle / Hook |
|:---|:---|:---|:---|
| **AI Software** | LiteLLM Enterprise / Ollama Cloud | 30% recurring | *"How we build local AI clusters for 50% cheaper"* |
| **CRM & DB** | Twenty CRM / Neon Serverless | 25% recurring | *"Stop paying Salesforce. Set up this open-source CRM in 10 mins"* |
| **Automation** | n8n Cloud | 20% recurring | *"The exact automation that runs our $200k/mo venture factory"* |
| **Hosting** | Vercel / Supabase | 15% recurring | *"Deploying 712 apps automatically without a dev team"* |
| **Education** | AI OS Masterclass | 50% one-off | *"The blueprint to run your company with 1,000 AI agents"* |

---

## 3. Agent Coordination (`Affiliate Agent`)

The `Affiliate Agent` is responsible for:
- Checking payout dashboards monthly and updating active payout metrics.
- Identifying expired link redirections and auto-updating target routing links.
- Scanning search trends to identify new high-payout SaaS affiliate opportunities and adding them to the dashboard registry.
