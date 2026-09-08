[[STARTHERE]] | [[REALITY]] | [[ARCHITECTURE]] | [[OPERATING-SYSTEM]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]

# ARCHITECTURE — System Overview & Tripartite Model

> **Canonical Document ID:** `DOC-ARCH-001`  
> **Authority:** System Architecture & Infrastructure Control Plane (CP-027)  
> **Status:** AUDITED LIVE  
> **Updated:** 2026-09-05

---

## 1. The Tripartite System Map
Company Brain is architecturally partitioned into three structural pillars converging through Data and Observability into Reality:

```text
                  COMPANY BRAIN
                        │
         ┌──────────────┼──────────────┐
         ↓              ↓              ↓
   ORGANIZATION      SOFTWARE    INFRASTRUCTURE
         │              │              │
         ↓              ↓              ↓
       ROLES          REPOS          HOSTS
       PEOPLE        SERVICES       NETWORK
       AGENTS          APIS         STORAGE
       TEAMS        DATABASES       COMPUTE
       OWNERS      DEPLOYMENTS      RUNTIME
         │              │              │
         └──────────────┼──────────────┘
                        ↓
                     SYSTEMS
                        ↓
                      DATA
                        ↓
                  OBSERVABILITY
                        ↓
                     REALITY
```

---

## 2. Infrastructure Layer
- **Physical Nodes:** Mac Studio M4 Max (Primary server & DB host) + MacBook Air (Mobile engineering node).
- **Network Mesh:** Tailscale WireGuard private encrypted overlay (`100.64.0.0/10`).
- **Data Substrate:** Neo4j (Graph), Qdrant (Vectors), PostgreSQL (Relational), Redis (Cache), MinIO (Object).
- **AI Inference:** Native Apple Silicon MLX via `exo` (`:52415`) + LiteLLM gateway (`:4000`) + OmniRoute (`:20128`).
- **Cloud Edge:** Vercel Global Edge Network (95 active sites).

---

## 3. NIST SP 800-204C Separation
- **Infrastructure-as-Code (IaC):** Compute, network, and storage provisioning declarations.
- **Policy-as-Code (PaC):** Open Policy Agent (OPA) / Conftest compliance guardrails.
- **Observability-as-Code (OaC):** Declarative Grafana dashboards and alerting rules.
