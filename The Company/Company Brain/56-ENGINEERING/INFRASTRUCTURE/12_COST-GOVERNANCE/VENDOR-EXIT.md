---
id: DOC-VEND-EXIT-001
aliases: ['VENDOR-EXIT']
tags: ['vendors', 'exit-strategy', 'sovereignty']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Vendor Exit Playbooks

> **Authority:** CP-027 & CP-001  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Exit Triggers & Actions
- **Trigger: Cloud LLM API Price Increase or Data Policy Shift:** Instantly shift 100% of subagent routing to Mac Studio local MLX cluster (`Qwen3.6-35B`).
- **Trigger: Vercel Service Disruption:** Reroute DNS to local edge instances via Cloudflare tunnels.

## 2. Connected Documents
- Vendor Risk: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/VENDOR-RISK|VENDOR-RISK.md]]
- Cloud Exit: [[56-ENGINEERING/INFRASTRUCTURE/05_CLOUD/CLOUD-EXIT|CLOUD-EXIT.md]]
- Multi-Cloud: [[56-ENGINEERING/INFRASTRUCTURE/05_CLOUD/MULTI-CLOUD|MULTI-CLOUD.md]]
