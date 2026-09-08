---
id: DOC-DECOMM-001
aliases: ['DECOMMISSIONING']
tags: ['decommissioning', 'pruning', 'cleanup']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Service Decommissioning Runbook

> **Authority:** CP-027  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Decommissioning Procedure
1. Verify service presence on [[KILL-LIST]].
2. Capture final snapshot / export to LaCie external archive.
3. Stop container, remove Docker volumes, and revoke Tailscale certs.
4. Update machine-readable registry in [[_REGISTRIES/service_registry.json|service_registry.json]].

## 2. Connected Documents
- Kill List: [[KILL-LIST]]
- Prohibited Actions: [[STOP-DOING]]
- Asset Retirement: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/ASSET-RETIREMENT|ASSET-RETIREMENT.md]]
- Asset Disposal: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/ASSET-DISPOSAL|ASSET-DISPOSAL.md]]
