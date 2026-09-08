---
id: DOC-SEC-RSK-001
aliases: ['SECURITY-RISK']
tags: ['security', 'risk', 'zero-trust']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Security & Intrusion Risks

> **Authority:** CP-027 & CP-028  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Security Threats & Hardening
- Threat: Public port exposure -> Enforce zero public ingress ports via Tailscale WireGuard only.
- Threat: Plaintext secrets in Git -> Enforce Bitwarden CLI ephemeral secret injection.

## 2. Connected Documents
- Security Subsystem: [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/SECURITY-INFRASTRUCTURE|SECURITY-INFRASTRUCTURE.md]]
- Secrets Management: [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/SECRETS|SECRETS.md]]
- Risk Register: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-RISK-REGISTER|INFRASTRUCTURE-RISK-REGISTER.md]]
