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

---

## 4. The Tripartite Knowledge Graph Architecture

Company Brain coordinates the enterprise not as a mere legal shell or flat list of tools, but as a unified tripartite knowledge graph:

$$\mathbf{Company\;Brain} = \mathbf{Ownership\;Graph} \;+\; \mathbf{Enterprise\;Graph} \;+\; \mathbf{Intelligence\;Graph}$$

```text
                                  COMPANY BRAIN
                                        │
           ┌────────────────────────────┼────────────────────────────┐
           ▼                            ▼                            ▼
   1. OWNERSHIP GRAPH           2. ENTERPRISE GRAPH         3. INTELLIGENCE GRAPH
      (The Estate)             (Commercial Ventures)          (Tool Substrate)
           │                            │                            │
  Family / Trust               36 Business Sectors           928 Starred Repos
  Holding Company (LLC)        12 Executive Divisions        Modular Capabilities
  People & Advisors            789 Operating Ventures        Agents & MCP Servers
  Assets & Real Estate         16-Step Money Flow Loop       Recurring Runbook Loops
  Deeds & Legal Docs           Customers, Deals & Invoices   Neo4j + gbrain + OmniRoute
```

### A. The Ownership Graph (Estate & Capital Preservation)
- **Primary Mission:** Coordinates who owns what, who controls what, how assets are shielded, and how wealth is preserved across generations.
- **Key Nodes:**
  - `Person`: Principal, Beneficiaries, Trustees, Executors, Family Members, Attorneys, CPAs, Bankers, Wealth Managers.
  - `Entity`: Family Trust, WorldwideBro Holdings LLC, Series LLCs, Operating LLCs, IP Holding Co, Foundations.
  - `Asset`: Real estate parcels, operating business equity, cash reserves, marketable securities, IP/patents, machinery, fleet vehicles.
  - `Document`: Trust indentures, Operating Agreements, Title Deeds, Insurance Binders, Form 1065/1120S Tax Returns, Wills.
  - `Advisory Network`: Fiduciary relationships mapping which advisor oversees which entity, asset, or tax strategy.
- **Core Edges:** `(Person)-[:CONTROLS]->(Entity)`, `(Trust)-[:OWNS_EQUITY]->(HoldCo)`, `(HoldCo)-[:HOLDS_ASSET]->(Asset)`, `(Document)-[:GOVERNS]->(Asset)`.

### B. The Enterprise Graph (Ventures & Commercial Production)
- **Primary Mission:** Models how the conglomerate acquires customers, delivers services, and generates gross margin.
- **Key Nodes:**
  - `Sector`: 36 Canonical Business Verticals (`SEC-001` through `SEC-035` + `SEC-037`).
  - `Venture`: The operating LLCs and front doors (e.g., `OPS-001`, `LT-005`, `CON-001`, `RE-001`, `CALLCENTER`).
  - `Division`: The 12 Executive Divisions (80 functional capabilities).
  - `Deal / Customer`: Enterprise clients, hospital labs, commercial general contractors, retail consumers.

### C. The Intelligence Graph (Tooling & Automation Substrate)
- **Primary Mission:** Automates execution across both the Estate and Enterprise without human friction.
- **Key Nodes:**
  - `Repository`: The 928 Starred GitHub Repositories.
  - `Capability`: Standardized business capabilities (Lead Scraping, OCR, ATS Ingestion, TMS Dispatch, CRM).
  - `Agent`: Specialized AI agents (`@architect`, `@qa`, `@deal-strategist`, `@outbound`).
  - `MCP Server`: Model Context Protocol servers (`company-brain`, `omniroute`, `browseros-neo`).
  - `Loop`: Scheduled recurring operations (Daily dispatch triage, monthly reconciliation, quarterly tax reviews).

---

## 5. The Enterprise Business Operating Model (12 Executive Divisions)

Rather than maintaining 80 isolated departments, Company Brain organizes corporate capabilities into **12 Executive Divisions**:

| # | Executive Division | Core Responsibility & Departmental Scope | Flagship Starred Tools |
|---|---|---|---|
| **01** | **Governance** | Board, CEO, Chief of Staff, Strategy, Internal Audit | `garrytan/gstack`, `Noisyxl/brier` |
| **02** | **Finance & Capital** | Treasury, FP&A, Tax, Accounting, Capital Markets, M&A | `firefly-iii`, `Open-Finance-Lab/AgenticTrading` |
| **03** | **Legal & Risk** | Contracts, Compliance, Risk, Insurance, IP, Regulatory | `opendatalab/MinerU`, `documenso/documenso` |
| **04** | **People** | Talent Acquisition, HR, Payroll, Workforce Planning | `ever-co/ever-gauzy`, `linkedin-agent-skill` |
| **05** | **Technology** | IT, Software, Infrastructure, Cybersecurity, AI/ML | `diegosouzapw/OmniRoute`, `openobserve`, `coolify` |
| **06** | **Product & Innovation** | Product Management, UI/UX, Design Systems, R&D | `shadcn-ui`, `v0`, `MengTo/threeui` |
| **07** | **Operations** | Supply Chain, Logistics, Fleet, Procurement, Facilities | `n8n-io/n8n`, `browser-use/browser-use` |
| **08** | **Revenue** | Sales, Deals, Account Management, Customer Success, CRM | `twentyhq/twenty`, `chatwoot/chatwoot` |
| **09** | **Marketing** | Demand Generation, Brand, SEO, Paid Media, Outbound | `google-maps-scraper-kit`, `crawl4ai`, `listmonk` |
| **10** | **Assets & Investments** | Real Estate, Property Management, Construction, Portfolio | `CloakHQ/CloakBrowser`, `typesense`, `Stirling-PDF` |
| **11** | **Public & Institutional** | Government Contracting, Grants, Civic & Community Impact | `self-hosted-ai-starter-kit`, `listmonk` |
| **12** | **Intelligence & Knowledge** | BI, Knowledge Graph, Docs, Decision Systems, Agent Ops | `garrytan/gbrain`, `neo4j`, `obsidian-cli` |

---

## 6. The Vital Center: The 16-Step Money Flow Reflex Arc

In accordance with [[REVENUE_GATE|REVENUE_GATE.md]], corporate departments and technical repositories do not exist to generate administrative meta-work. Every entity is designed to advance through the continuous cash-generation loop:

$$\text{Market} \rightarrow \text{Lead} \rightarrow \text{Marketing} \rightarrow \text{Sales} \rightarrow \text{Deal} \rightarrow \text{Contract} \rightarrow \text{Finance} \rightarrow \text{Operations} \rightarrow \text{Delivery} \rightarrow \text{Customer} \rightarrow \text{Invoice} \rightarrow \text{Collection} \rightarrow \text{Profit} \rightarrow \text{Capital} \rightarrow \text{Investment} \rightarrow \text{New Venture}$$

1. **Lead Generation:** `Marketing` uses `crawl4ai` and `google-maps-scraper-kit` to extract verified accounts.
2. **Sales & Qualification:** `Revenue` logs opportunities into `twenty` CRM and routes conversations via `chatwoot`.
3. **Contract & Compliance:** `Legal` parses requirements via `pdfplumber` and executes agreements with `documenso`.
4. **Operations & Delivery:** `Operations` dispatches jobs through `LT-011` / `HealthRoute` and monitors telemetry via `OpenObserve`.
5. **Invoicing & Collection:** `Finance` validates fulfillment and collects funds via Stripe/Plaid.
6. **Capital Reinvestment:** Profits are routed to `WorldwideBro Holdings LLC` for asset preservation, real estate acquisitions (`RE-001`), or venture seeding.

---

## 7. 36-Sector Top Anchor Ventures Crosswalk

Canonical mapping of the Top Operating Anchor for each sector:

| Sector ID | Sector Vertical | Flagship Venture | Status | Commercial Focus |
|---|---|---|:---:|---|
| **SEC-001** | Beauty & Wellness | **BEAUTY-001** | Active | Wellness and beauty studio memberships |
| **SEC-002** | Construction & Infrastructure | **CON-001** | 🟢 Live | ACE Construction commercial contracting |
| **SEC-003** | Consumer Hardware & IoT | **ELEC-001** | Staging | Cold-chain hardware transit telemetry |
| **SEC-004** | Content & Media | **MEDIA-001** | Staging | WorldwideBro Media Network podcasts & news |
| **SEC-005** | Education & Training | **ET-011** | 🟢 Active | Commercial dispatch & trade training academy |
| **SEC-006** | Energy & Utilities | **ENERGY-001** | Staging | EV fleet depot solar & charging infrastructure |
| **SEC-007** | Environmental Services | **ENV-001** | Staging | Regulated medical waste & biohazard handling |
| **SEC-008** | Financial Services | **FIN-001** | 🟢 Active | Genixbank corporate treasury & banking gateway |
| **SEC-009** | Food & Agriculture | **FOOD-001** | Staging | Vertical freight container organic farming |
| **SEC-010** | Food Service & Restaurants | **REST-001** | Staging | Cloud kitchen shared logistics & delivery |
| **SEC-011** | Gaming & Entertainment | **EC-111** | 🟢 Live | Miss Toys interactive physical-digital goods |
| **SEC-012** | Healthcare & Biotechnology | **HC-001** | Staging | CLIA diagnostic laboratory courier intake |
| **SEC-013** | Hospitality & Travel | **HOSP-001** | Staging | Executive corporate housing & extended stay |
| **SEC-014** | Human Resources & Staffing | **OPS-001** | 🟢 Live | WorldwideBro Staffing Ops light industrial |
| **SEC-015** | Insurance | **INS-001** | Staging | Commercial cargo & inland marine captive broker |
| **SEC-016** | Legal & Compliance | **LEGAL-001** | Staging | LexAutomata corporate entity governance |
| **SEC-017** | Logistics & Transportation | **LT-005** | 🟢 Live | HealthRoute Courier STAT medical logistics |
| **SEC-018** | Manufacturing & Engineering | **MFG-001** | Staging | Modular fleet enclosure fabrication |
| **SEC-019** | Marketing & Advertising | **MKTG-001** | Staging | B2B programmatic lead prospecting |
| **SEC-020** | Real Estate & Property | **RE-001** | 🟢 Live | WorldwideBro Holdings commercial & land |
| **SEC-021** | Retail & E-commerce | **COMM-001** | 🟢 Live | WorldwideBro multi-storefront network |
| **SEC-022** | Telecommunications | **TELECOM-001** | Staging | Private encrypted overlay mesh network |
| **SEC-023** | Professional Services | **PROF-001** | Staging | Executive turnaround & M&A advisory |
| **SEC-024** | Technology & Software | **TECH-040 / VEX** | 🟢 Live | WorldwideBro VEX Venture Operating System |
| **SEC-025** | Automotive & Mobility | **AUTO-001** | Staging | Commercial cargo van & box truck leasing |
| **SEC-026** | Utilities & Municipal | **UTIL-001** | Staging | Public works facility services |
| **SEC-027** | Venture Capital & Incubation | **VC-001** | Staging | WorldwideBro Ventures portfolio acceleration |
| **SEC-028** | B2B Enterprise Software | **ENT-001** | 🟢 Live | DispatchOS multi-tenant TMS platform |
| **SEC-029** | Marketplace & Platforms | **PLAT-001** | Staging | Medical courier on-demand shift exchange |
| **SEC-030** | Fintech & Payments | **FINTECH-001** | 🟢 Live | Arbitrage multi-currency settlement engine |
| **SEC-031** | Climate & Sustainability | **CLIMATE-001** | Staging | Logistics route emission reduction audits |
| **SEC-032** | Artificial Intelligence & ML | **AI-001** | 🟢 Live | Mac Studio Apple Silicon sovereign MLX node |
| **SEC-033** | Cybersecurity & Privacy | **CYBER-001** | Staging | Zero-trust secrets & identity management |
| **SEC-034** | Decentralized & Web3 | **WEB3-001** | Staging | Immutable private asset trust registry |
| **SEC-035** | [Discovery & Stealth] | **DISC-001** | Reserved | Opportunistic venture acquisition incubator |
| **SEC-037** | Quant Trading & Capital | **FIN-037** | 🟢 Live | High-frequency statistical arbitrage system |
