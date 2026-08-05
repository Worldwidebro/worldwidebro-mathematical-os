# Worldwidebro Holding Estate: Subsidiary & Capabilities Dependency Map

This document defines the dependency architecture of the Worldwidebro Holding Estate. It maps our parent company, operating companies (OpCos), individual service ventures, and how they leverage our starred open-source repository toolsets.

---

## 1. Corporate & Technical Hierarchy

```text
                  WORLDWIDEBRO HOLDINGS (Parent Estate)
                                   │
         ┌─────────────────────────┴─────────────────────────┐
         ▼ (Sectors / OpCos)                                 ▼
       LOG-OS                                              FIN-OS
 (Logistics & Trans)                                     (Financials)
   │             │                                         │
   ├─ LT-001 (Trucking)                                    ├─ FIN-001 (GenixBank)
   ├─ LT-005 (Medical Courier)                             ├─ FIN-011 (Bookkeeping)
   └─ LT-011 (DispatchOS Core Middleware) ◄────────────────┴─ FIN-012 (Invoice Factoring)
         ▲
         │ (Shared dispatch routing/GPS engine)
   ┌─────┴─────────────────────────┐
   ▼                               ▼
 BW-OS (Beauty-Wellness)        FH-OS (Food-Hospitality)
   ├─ BW-002 (Mobile Lash)         ├─ FH-001 (Personal Chef)
   └─ BW-012 (Mobile Nail)         └─ FH-002 (Meal Prep Delivery)
```

1.  **Worldwidebro Holdings (Parent Estate):** Sets global compliance, security guidelines, and oversees shared infrastructure.
2.  **Operating Companies (OpCos / Sectors):** Grouped by business domain (`LOG-OS`, `FIN-OS`, `BW-OS`, `FH-OS`) as mapped in `OPCO-STRUCTURE.md`.
3.  **Core Middleware (LT-011 / DispatchOS):** Serves as the central operational dispatch platform. Every mobile-service venture (like `BW-002` mobile lashes, `FH-001` personal chefs, or `LT-005` medical courier) routes its booking, driver matching, and GPS tracking requests directly through `LT-011` APIs.

---

## 2. Open-Source Starred Repository Integrations

Based on the audit of your `starred_repos_664.csv`, we map specific open-source tools to satisfy capabilities across the estate:

| Starred Repository | Venture / Sector | Capability Provided |
| :--- | :--- | :--- |
| **`decolua/9router`** | Shared (All OpCos) | local AI gateway supporting multi-provider pooling, auto-fallback, and token compression to run local LLMs. |
| **`a2aproject/A2A`** | LOG-OS & FIN-OS | Open protocol to let our dispatch agents (like `BillingAgent`) communicate securely with financial agents (like `GenixBank`). |
| **`Panniantong/Agent-Reach`** | LOG-OS (Tendering) | Scrapes and gathers freight market rates and shipper leads from directories with zero API fees. |
| **`coleam00/Archon`** | Shared (Agents) | Deterministic yaml-based harness builder to version and parse our Markdown prompts. |
| **`iOfficeAI/AionUi`** | Shared (Management) | Local, open-source 24/7 Web UI to monitor multiple agent logs in real time. |

---

## 3. Dependency Pipeline Phases

| Phase | Milestone | Dependency Requirements |
| :--- | :--- | :--- |
| **Phase 1** | Local Infrastructure | Docker networks for Postgres and Neo4j on the Mac Studio. |
| **Phase 2** | Local AI Routing | Running `9router` locally to serve as the unified API base. |
| **Phase 3** | CRM Webhook Binding | Connect outbound lead webhooks from **Buzz CRM** to automatically inject new cargo orders. |
| **Phase 4** | Cross-Venture Scaling | Inherit tracking APIs from `LT-011` to match appointments for beauty (`BW-002`) and food (`FH-001`) ventures. |
