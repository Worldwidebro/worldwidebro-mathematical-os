# CAMPAIGN-AUTOMATION — Automated Execution Engine

> **Canonical Document ID:** `DOC-AUT-CAM-001`  
> **Authority:** Infrastructure & Automation (CP-022 / CP-048)  
> **Status:** ACTIVE SPECIFICATION  
> **Canonical Alias:** [[CAMPAIGNS/AUTOMATION.md]]

---

## 1. Automation Infrastructure

Campaign automations run natively on Company Brain's local-first execution stack:
- **`trigger.dev` (`TOL-000016`):** Durable background execution for multi-day email sequence workflows.
- **`Graft` (`TOL-000001`):** Codebase graph generation engine powering Deliverable 2 of the audit.
- **`Fractal` (`TOL-000002`):** Multi-agent recursive task runner isolating agent worktrees.
- **`OmniRoute` (`:20128`):** Intelligent LLM inference router cascading prompts between local MLX and cloud models.

---

## 2. Master Links

- Master OS: [[CAMPAIGNS/CAMPAIGN-OS]]
- Workflows: [[CAMPAIGNS/CAMPAIGN-WORKFLOWS]]
- Triggers: [[CAMPAIGNS/TRIGGERS]]
