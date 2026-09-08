---
id: DOC-PROV-001
aliases: ['PROVISIONING']
tags: ['provisioning', 'deployment', 'iac']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Automated Host Provisioning

> **Authority:** CP-027  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Provisioning Runbook
Automated onboarding of new macOS nodes into Company Brain:
1. Install Tailscale and authenticate with zero-trust credentials.
2. Configure SSH authorized keys and establish remote Docker context `macstudio`.
3. Clone canonical repositories and run bootstrap validation.

## 2. Connected Documents
- Lifecycle Management: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-LIFECYCLE|INFRASTRUCTURE-LIFECYCLE.md]]
- Runtime State: [[CLAUDE]]
- Deployment Domain: [[56-ENGINEERING/INFRASTRUCTURE/08_DEPLOYMENT/DEPLOYMENT|DEPLOYMENT.md]]
