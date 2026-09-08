---
id: GUIDE-INFRA-START
aliases: ['INFRASTRUCTURE/START-HERE']
tags: ['infrastructure', 'orientation', 'guide']
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[REALITY]] | [[CLAUDE]] | [[56-ENGINEERING/56-ENGINEERING|56-ENGINEERING]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]

# START HERE — Infrastructure Subsystem Orientation

> **Scope:** 56-ENGINEERING / INFRASTRUCTURE Navigation  
> **Master Legend:** [`STARTHERE.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/STARTHERE.md)  
> **Subsystem Control Plane:** [`INFRASTRUCTURE.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE.md)  
> **Authority:** CP-027  
> **Status:** ACTIVE — Updated 2026-09-05

---

## 1. Welcome to Infrastructure
You are in the canonical **56-ENGINEERING/INFRASTRUCTURE** subsystem. This subsystem contains 265 structured markdown documents organized into 12 engineering domains and backed by 23 machine-readable JSON registries in `_REGISTRIES/`.

---

## 2. The 12 Domains At a Glance
1. [`01_CORE/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/01_CORE) — System OS, models, metamodel, and [`INFRASTRUCTURE-REALITY.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE-REALITY.md).
2. [`02_COMPUTE/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/02_COMPUTE) — Mac Studio M4 Max, MacBook Air, Metal GPU, UMA memory limits.
3. [`03_STORAGE/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/03_STORAGE) — Internal SSDs, LaCie 4TB HDD, Samsung T7 Shield 2TB NVMe SSD.
4. [`04_NETWORK/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/04_NETWORK) — Tailscale WireGuard mesh (`100.64.0.0/10`), MagicDNS, strict ports.
5. [`05_CLOUD/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/05_CLOUD) — Hybrid cloud edge, 95 Vercel sites, multi-cloud exit strategy.
6. [`06_DATA/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/06_DATA) — Polyglot databases (Neo4j, Qdrant, PostgreSQL 16, Redis, MinIO).
7. [`07_RUNTIME/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/07_RUNTIME) — Remote Docker context `macstudio`, LiteLLM, OmniRoute, native MLX.
8. [`08_DEPLOYMENT/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/08_DEPLOYMENT) — NIST SP 800-204C DevSecOps: IaC, PaC, OaC separation.
9. [`09_OBSERVABILITY/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/09_OBSERVABILITY) — Grafana dashboards (:3011), Langfuse (:3003), telemetry.
10. [`10_SECURITY/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/10_SECURITY) — NIST SP 800-207 Zero Trust multi-subject, Bitwarden JIT secrets.
11. [`11_RESILIENCE/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/11_RESILIENCE) — High availability, 3-2-1 backup architecture, DR runbooks, RTO/RPO.
12. [`12_COST-GOVERNANCE/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/12_COST-GOVERNANCE) — FinOps ($309/mo TCO), capacity limits, SOP runbooks, ADRs 001–005.

---

## 3. What To Do First
- Read the master control plane: [`INFRASTRUCTURE.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE.md).
- Verify running components: [`01_CORE/INFRASTRUCTURE-REALITY.md`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/56-ENGINEERING/INFRASTRUCTURE/01_CORE/INFRASTRUCTURE-REALITY.md).
- Check machine-readable registries in [`_REGISTRIES/`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_REGISTRIES).
