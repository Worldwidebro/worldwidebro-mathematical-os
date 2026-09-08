---
id: CP-027-INFRA-CONTROL
title: Infrastructure Control Plane (CP-027)
aliases: ["Infrastructure Control Plane", "CP-027", "Infrastructure Control Plane (CP-027)", "50-MASTER-CONTROL/Infrastructure Control Plane"]
tags: ["infrastructure", "control-plane", "cp-027", "macstudio", "databases", "tailscale"]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[50-MASTER-CONTROL/50-MASTER-CONTROL|50-MASTER-CONTROL]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]] | [[CLAUDE]] | [[REALITY]]

# Infrastructure Control Plane (CP-027)

The core hardware, network, database, container, and model routing control plane for Company Brain.

## Master Hubs & Navigation
- Canonical Control Plane: [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE.md]]
- Subsystem Orientation: [[56-ENGINEERING/INFRASTRUCTURE/START-HERE|START-HERE.md]]
- Directives Gateway: [[DIRECTIVES]]
- AI Brain Subsystem: [[AI-BRAIN]]
- Runtime State & Docker Contexts: [[CLAUDE.md]]
- Operating Rules: [[ANTIGRAVITY.md]]

## The 12 Engineering Subsystems
1. [[56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE|01_CORE]] — System OS, models, and metamodel.
2. [[56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE/COMPUTE|02_COMPUTE]] — Mac Studio M4 Max, MacBook Air, Metal GPU, virtual machines.
3. [[56-ENGINEERING/INFRASTRUCTURE/03_STORAGE/STORAGE|03_STORAGE]] — Internal SSDs, LaCie 4TB HDD, Samsung T7 Shield 2TB NVMe SSD.
4. [[56-ENGINEERING/INFRASTRUCTURE/04_NETWORK/NETWORK|04_NETWORK]] — Tailscale WireGuard mesh (`100.64.0.0/10`), MagicDNS, strict ports.
5. [[56-ENGINEERING/INFRASTRUCTURE/05_CLOUD/CLOUD|05_CLOUD]] — Hybrid cloud edge, 95 Vercel sites, multi-cloud exit strategy.
6. [[56-ENGINEERING/INFRASTRUCTURE/06_DATA/DATABASES|06_DATA]] — Polyglot databases (Neo4j, Qdrant, PostgreSQL 16, Redis, MinIO).
7. [[56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME/RUNTIME|07_RUNTIME]] — Remote Docker context `macstudio`, LiteLLM, OmniRoute, native MLX.
8. [[56-ENGINEERING/INFRASTRUCTURE/08_DEPLOYMENT/DEPLOYMENT|08_DEPLOYMENT]] — NIST SP 800-204C DevSecOps: IaC, PaC, OaC separation.
9. [[56-ENGINEERING/INFRASTRUCTURE/09_OBSERVABILITY/OBSERVABILITY|09_OBSERVABILITY]] — Grafana dashboards (:3011), Langfuse (:3003), telemetry.
10. [[56-ENGINEERING/INFRASTRUCTURE/10_SECURITY/SECURITY-INFRASTRUCTURE|10_SECURITY]] — NIST SP 800-207 Zero Trust multi-subject, Bitwarden JIT secrets.
11. [[56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE/RESILIENCE|11_RESILIENCE]] — High availability, 3-2-1 backup architecture, DR runbooks, RTO/RPO.
12. [[56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE/INFRASTRUCTURE-COST|12_COST-GOVERNANCE]] — FinOps ($309/mo TCO), capacity limits, SOP runbooks, ADRs.
