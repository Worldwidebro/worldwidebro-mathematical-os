---
id: DOC-SCALE-001
aliases: ['SCALING']
tags: ['scaling', 'architecture', 'growth']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Vertical & Horizontal Scaling Strategy

> **Authority:** CP-027  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Scaling Model
- **Vertical Scaling:** Apple Silicon Metal acceleration, memory compression, and model quantization.
- **Horizontal Scaling:** Peer-to-peer distributed inference across Mac Studio and MacBook Air via `exo` MLX over Tailscale.
- **Edge Scaling:** Serverless microservices on Vercel Edge.

## 2. Connected Documents
- Autoscaling: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/AUTOSCALING|AUTOSCALING.md]]
- Capacity Planning: [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/CAPACITY-PLANNING|CAPACITY-PLANNING.md]]
- Network Interconnect: [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/TAILSCALE|TAILSCALE.md]]
