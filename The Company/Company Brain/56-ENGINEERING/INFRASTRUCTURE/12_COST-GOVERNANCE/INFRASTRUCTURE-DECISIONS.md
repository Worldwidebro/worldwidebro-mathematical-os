---
id: DOC-INFRA-ADR-001
aliases: ['INFRASTRUCTURE-DECISIONS', 'Infrastructure ADRs']
tags: ['adr', 'architecture', 'decisions']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|INFRASTRUCTURE-COST]] | [[24-FINANCE]] | [[46-GOVERNANCE]]

# Architecture Decision Records (ADRs)

> **Authority:** CP-027  
> **Status:** ACTIVE — Audited 2026-09-06

## 1. Master ADR Register
- `ADR-001`: Adopt Mac Studio M4 Max as primary inference server and database host.
- `ADR-002`: Consolidate multi-project Docker compose stacks into single canonical `macstudio` context.
- `ADR-003`: Deploy `exo` MLX cluster on port `:52415` for native Apple Silicon acceleration.
- `ADR-004`: Enforce Zero Public Ingress Ports using Tailscale WireGuard overlay.
- `ADR-005`: Implement Bitwarden JIT credential injection to eliminate plaintext secrets.

## 2. Connected Documents
- Decisions Domain: [[20-DECISIONS/20-DECISIONS|20-DECISIONS]]
- Directives Hub: [[DIRECTIVES]]
- System Principles: [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE-PRINCIPLES|INFRASTRUCTURE-PRINCIPLES.md]]
