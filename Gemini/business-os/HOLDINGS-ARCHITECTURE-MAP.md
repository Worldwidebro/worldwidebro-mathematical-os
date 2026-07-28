# IZA Holdings Architecture Map

This document maps the three-layer architectural blueprint of the **Worldwidebro Holdings AI Operating System (IZA OS)**, clarifying how the active ventures (`CON-001`, `STA-001`, `LT-005`, `EC-001`, `EC-112`, `RE-001`, and the `FIN` suites) coincide, where `OmniRoute` fits, how monetization and funding operate, and how we leverage reusable parts.

---

## 1. The Three-Layer IZA Architecture

We divide our system into three distinct layers to ensure reusable infrastructure, domain-specific business logic, and customer-facing operations are completely decoupled.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                      LAYER 1: PLATFORM OS                              │
│             (Shared Infrastructure & AI Routing Layer)                 │
│  [Identity] [Knowledge] [AI Agents] [OmniRoute] [Event Bus] [Finance]   │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                      LAYER 2: SECTOR OS                                │
│             (Domain-Specific Business Engines)                         │
│  [Construction OS] [Staffing OS] [Medical Courier OS] [Commerce OS]    │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                      LAYER 3: VENTURE REPOS                            │
│             (Customer-Facing Operating Companies)                      │
│   ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────┐│
│   │  CON-001  │  │  STA-001  │  │  LT-005   │  │  EC-112   │  │Tax/FIN││
│   │ (Const.)  │  │ (Staffing)│  │ (Courier) │  │ (Cosmic)  │  │Suites ││
│   └───────────┘  └───────────┘  └───────────┘  └───────────┘  └───────┘│
└────────────────────────────────────────────────────────────────────────┘
```

### Layer 1: Platform OS (Shared Infrastructure)
*   **Role**: Non-business, pure platform utility services. These route requests, store knowledge, manage vector models, authenticate users, and track system health.
*   **Core Services**:
    *   **OmniRoute**: Universal AI Routing Layer. Routes intelligence, determines LLM endpoints (Claude, GPT, local Llama), and failovers APIs.
    *   **Knowledge OS**: The global semantic network and graph layer (Neo4j / Qdrant).
    *   **Agent OS**: Running micro-agents (Lead Gen, Outreach, Compliance).
    *   **Event Bus / Notification OS**: Handles real-time events and multi-channel triggers.

### Layer 2: Sector OS (Domain Operating Systems)
*   **Role**: Houses the domain-specific business logic and APIs for each industry sector.
*   **Core Systems**:
    *   **Construction OS** (`worldwidebro-construction-os`): Estimating calculations, sub-contract formatting, change orders, site safety checks.
    *   **Staffing OS** (`iza-os-staffing-core`): Recruiter matching engine, compliance verification, credential tracking, time clocks.
    *   **Medical Courier OS** (Missing Backend): Courier route dispatch, HIPAA chain-of-custody, specimen logs.
    *   **Commerce OS** (`ec-112-cosmic-kitty/backend`): Headless inventory, multi-tenant catalogs, payments checkout (powered by Medusa).

### Layer 3: Venture Repos (Customer-Facing Brands)
*   **Role**: Customer-facing websites, storefronts, and marketing layouts.
*   **Active Brands**:
    *   **CON-001 Ace Construction**: Live Next.js client portal.
    *   **STA-001 Staffing**: Live static multipage placement site.
    *   **LT-005 Medical Courier**: Live route/driver files (missing frontend site).
    *   **EC-001 Angels in Daylight**: E-commerce catalog assets (missing storefront).
    *   **EC-112 Cosmic Kitty**: Live Next.js wellness storefront.

---

## 2. OmniRoute: Routing Intelligence, Not Trucks

As highlighted in the architecture, **OmniRoute is NOT a Logistics company**. It is a **Platform OS infrastructure router** that directs data and tasks to the correct models or microservices:

```text
[Venture Request] ──▶ [OmniRoute] ──▶ Route to: Claude-3.5-Sonnet (High complexity)
                                  ──▶ Route to: Google Maps API (Location request)
                                  ──▶ Route to: Llama-3 (Low cost translation)
```

*   **Logistics OS** (if built) is a Layer 2 Sector OS that manages physical vehicle assets, DOT compliance, and driver hours. It consumes **OmniRoute** as a dependency to route routing queries or coordinates, rather than OmniRoute managing trucks directly.

---

## 3. Monetization: Why We Aren't Bringing in Income (And How to Fix It)

Currently, the repositories are **skeletons or playbooks**—they have design files, code frameworks, and static pages, but they are not hooked to live pipelines:

1.  **No Traffic Sourcing**: The cold email outreach scripts are in the folder, but no automated agent is actively sending campaigns to Charlotte B2B prospects.
2.  **Disconnected Intake Forms**: The career and lead capture pages do not post submissions directly to n8n workflows that write to Supabase or Twenty CRM.
3.  **No Live Checkout Hooks**: Customers cannot click a link, receive a quote, sign a contract via Jotform Sign, and pay a deposit via Stripe.

### Direct Action Plan for Day 1 Income:
*   **Step 1**: Wire `STA-001` and `CON-001` contact forms directly to n8n webhook links.
*   **Step 2**: Trigger n8n to generate a Stripe Invoice Link upon client booking.
*   **Step 3**: Activate the lead discovery scripts to find Charlotte prospects and feed them into cold outreach campaigns.

---

## 4. How Funding Works in the Holdings Model

Worldwidebro Holdings operates on **Circular Capital Leverage** rather than isolated financing:

```text
               [Holdings Capital]
                       │
       ┌───────────────┴───────────────┐
       ▼                               ▼
[RE-001 (Real Estate)]      [FIN-Core (Financial)]
 (SBA 504 / Collateral)      (SPV Debt Structuring)
       │                               │
 (Asset Purchase)             (Inventory RBF Credit)
       ▼                               ▼
[CON-001 (Construction)]    [EC-001 / EC-112 (Commerce)]
```

1.  **Debt & Asset Leverage**: The Financial Sector (`FIN`) structures SPVs (Special Purpose Vehicles) to raise debt. Real Estate (`RE-001`) leverages this debt to secure SBA 504 loans, buying land and physical assets (datacenters, warehouses).
2.  **Revenue-Based Financing (RBF)**: Capital raised in funding rounds is deployed as revolving inventory lines directly to Commerce ventures (`Angels in Daylight`, `Cosmic Kitty`). High-margin retail sales repay the credit lines dynamically.
3.  **Arbitrage Handoff Yields**: Every operational delegation cycle between ventures captures a contract margin (Construction GCs capture 25-35%, Staffing captures 30-40% markup, Real Estate captures 8-12% lease fees). These margins are siphoned back up to the holding company.

---

## 5. Comprehensive Multi-Venture Mapping & Funding Loop

The following table maps the 14 active ventures, showing their Sector classification, directory path, and how they hook into the credit, loan, and tax-offset pipeline:

| Venture ID | Venture Name / Scope | Sector | Local Repo / Directory | Funding & Loan Alignment Role |
| :--- | :--- | :--- | :--- | :--- |
| **`FUND-001`** | Funding Hub / SPVs | Funding | *Central Registry* | **Primary Capital Aggregator**: Deployer of RBF and venture equity lines. |
| **`FIN-007`** | Business Credit Building | Financial | *Registry / Config* | **Credit Architect**: Builds credit scores for all opcos to secure bank loans. |
| **`FIN-002`** | Credit Repair Automation | Financial | *Registry / Config* | **Personal Guarantee Shield**: Optimizes personal scores of executive guarantors. |
| **`RE-001`** | Property Holdings | Real Estate | [/RE-001-Worldwidebro-Holdings](file:///Users/acebless/Documents/RE-001-Worldwidebro-Holdings) | **Asset / Mortgage Holder**: Leverages `FIN-007` credit to secure SBA 504 loans to lease properties. |
| **`CON-001`** | Ace Construction | Construction| [/con-001-ace-construction](file:///Users/acebless/Documents/con-001-ace-construction) | **Renovation Engine**: Builds assets, secures heavy equipment leasing loans via `FIN-007`. |
| **`LT-005`** | Medical Courier Dispatch | Logistics | [/lt-005-medical-courier-dispatch](file:///Users/acebless/Documents/lt-005-medical-courier-dispatch) | **Fleet / Route Operator**: Secures commercial vehicle auto loans using built credit lines. |
| **`OPS-001`** | Venture Staffing | Staffing | [/ops-staff-001-staffing](file:///Users/acebless/Documents/ops-staff-001-staffing) | **Labor Provider / Float Manager**: Leverages credit lines for payroll accounts receivable floats. |
| **`EC-112`** | Cosmic Kitty storefront | Commerce | [/ec-112-cosmic-kitty](file:///Users/acebless/Documents/ec-112-cosmic-kitty) | **RBF Consumer**: Receives inventory lines from `FUND-001` to capture retail margin. |
| **`EC-001`** | Angels in Daylight | Commerce | [/ec-001-angels-in-daylight](file:///Users/acebless/Documents/ec-001-angels-in-daylight) | **RBF Consumer**: Receives wholesale inventory financing to purchase retail stock. |
| **`FIN-006`** | Tax Prep & Filing | Financial | [/fin-006-tax-prep-filing-services](file:///Users/acebless/Documents/fin-006-tax-prep-filing-services) | **Tax Architect**: Files partnership and corporate tax returns (1065 / 1120-S). |
| **`FIN-009`** | Crypto Tax Optimizer | Financial | [/fin-009-crypto-tax-optimizer](file:///Users/acebless/Documents/fin-009-crypto-tax-optimizer) | **Crypto Shield**: Optimizes digital asset transaction gains and deducts losses. |
| **`FIN-021`** | Tax Deduction Finder | Financial | [/fin-021-tax-deduction-finder](file:///Users/acebless/Documents/fin-021-tax-deduction-finder) | **Expense Auditor**: Automatically crawls ledger receipts to maximize deductions. |
| **`FIN-033`** | AI Tax Prep Service | Financial | [/fin-033-ai-tax-preparation-service](file:///Users/acebless/Documents/fin-033-ai-tax-preparation-service) | **Tax Automation Engine**: Generates automated IRS filings and matches deduction criteria. |
| **`PS-010`** | Tax Preparation Service | Financial | *Registry / Config* | **Client-Facing CPA Services**: Captures direct B2B accounting and compliance retainer revenues. |

---

## 6. Overlapping Duplicates & Replicas

We identified duplicate repositories on the drive that represent the same holdings logic:
1.  **Property Holdings**:
    *   `/Users/acebless/Documents/re-001-property-holdings` (stale origin)
    *   `/Users/acebless/Documents/RE-001-Worldwidebro-Holdings` (primary vercel connected)
    *   *Action*: We keep `RE-001-Worldwidebro-Holdings` as the active development directory.
2.  **Tax Prep Services**:
    *   `fin-006-tax-prep-filing-services`
    *   `fin-033-ai-tax-preparation-service`
    *   *Alignment*: `FIN-006` handles manual filing and workflows, while `FIN-033` develops the underlying AI parsing code. They are connected in parallel.
