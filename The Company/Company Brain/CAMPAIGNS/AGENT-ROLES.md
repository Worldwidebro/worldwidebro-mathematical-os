# CAMPAIGN-AGENT-ROLES — Agent Capability & Boundary Matrix

> **Canonical Document ID:** `DOC-ROL-CAM-001`  
> **Authority:** Agent Governance (CP-016 / CP-046)  
> **Status:** ACTIVE SPECIFICATION  
> **Canonical Alias:** [[CAMPAIGNS/AGENT-ROLES.md]]

---

## 1. Capabilities and Boundaries Matrix

| Agent Code | Allowed Tools | Forbidden Actions | Escalation Trigger |
| :--- | :--- | :--- | :--- |
| **`AGT-ORC-001`** | Fractal CLI, Neo4j driver, OmniRoute | Cannot modify master budget without human signature | Budget variance > 10% |
| **`AGT-OUT-001`** | Outbound mailer, NeverBounce API, Apollo | Cannot send > 50 emails/hour; cannot bypass opt-outs | Bounce rate > 2.0% |
| **`AGT-CPY-001`** | LLM inference, grammar linter | Cannot make unsubstantiated technical claims | Factual claim without evidence |
| **`AGT-DEA-001`** | Cal.com API, SOW generator | Cannot offer discounts exceeding pre-approved bonuses | Client request for custom SLA |
| **`AGT-COM-001`** | Semgrep, regex compliance linter | Cannot approve copy containing spam triggers | CAN-SPAM disclosure missing |

---

## 2. Master Links

- AI Campaigns: [[CAMPAIGNS/AI-CAMPAIGNS]]
- Permissions: [[CAMPAIGNS/CAMPAIGN-AGENT-PERMISSIONS]]
