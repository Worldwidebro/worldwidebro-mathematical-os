---
id: DOC-ASSET-RET-001
aliases: ['ASSET-RETIREMENT']
tags: ['lifecycle', 'retirement', 'containers']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Software & Container Retirement

> **Authority:** CP-027  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Container & Software Retirement Policy
- Containers marked for retirement enter a 14-day staging period with DNS disabled before hard deletion.
- All code manifests and Dockerfile configurations archived in `_ARCHIVE/` prior to purge.

## 2. Connected Documents
- Decommissioning: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/DECOMMISSIONING|DECOMMISSIONING.md]]
- Kill List: [[KILL-LIST]]
- Technical Debt: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/TECHNICAL-DEBT|TECHNICAL-DEBT.md]]
