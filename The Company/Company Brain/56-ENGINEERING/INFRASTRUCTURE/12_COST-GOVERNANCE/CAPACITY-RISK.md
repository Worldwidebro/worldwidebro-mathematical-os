---
id: DOC-CAP-RSK-001
aliases: ['CAPACITY-RISK']
tags: ['capacity', 'risk', 'mitigation']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Capacity & Exhaustion Risks

> **Authority:** CP-027 & CP-028  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. High-Priority Capacity Risks
1. **MacBook Air Internal SSD Exhaustion:** Drive has only 34GB free space; aggressive Docker prune and artifact cleanup mandated.
2. **Unified Memory Saturation:** Running 32B+ models alongside Docker databases causes kernel memory pressure and swapping.

## 2. Connected Documents
- Risk Register: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-RISK-REGISTER|INFRASTRUCTURE-RISK-REGISTER.md]]
- Stress Testing: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/STRESS-TESTING|STRESS-TESTING.md]]
- Risk Control Plane: [[34-RISK/34-RISK|34-RISK]]
