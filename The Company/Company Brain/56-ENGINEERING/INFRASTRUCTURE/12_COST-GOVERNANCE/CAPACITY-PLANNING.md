---
id: DOC-CAP-PLAN-001
aliases: ['CAPACITY-PLANNING']
tags: ['capacity', 'planning', 'scaling']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Capacity Planning & Growth Projections

> **Authority:** CP-027  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Bottleneck Thresholds & Planning
- Primary constraint is **36GB Unified Memory** on the Mac Studio inference server.
- Maximum supported single local model: ~24GB VRAM footprint (`Qwen3.6-35B` 5-bit or `qwen2.5-coder:14b`).
- Secondary constraint is internal SSD free space on MacBook Air (34GB free).

## 2. Connected Documents
- Capacity Overview: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/CAPACITY|CAPACITY.md]]
- Scaling Strategy: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/SCALING|SCALING.md]]
- Mac Hardware Specs: [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/MACS|MACS.md]]
- Resource Planning: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/RESOURCE-PLANNING|RESOURCE-PLANNING.md]]
