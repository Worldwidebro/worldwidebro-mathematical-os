[[STARTHERE]] | [[REALITY]] | [[23-VENTURES]] | [[16-AGENTS]] | [[15-SKILLS]] | [[INDEX]]

# 23-VENTURES — Autonomous Venture Portfolio & Lifecycle

> **Canonical Domain ID:** `DOM-023`  
> **Authority:** Venture Control Plane (CP-005)  
> **Authoritative Public Portal:** [`Worldwidebro/worldwidebro-venture-portal`](https://github.com/Worldwidebro/worldwidebro-venture-portal) (`OWN-PRIV-0004` / `REP-001`)  
> **Flywheel Blueprint:** [[_INFRASTRUCTURE/VENTURE-PORTAL-FLYWHEEL|Autonomous Venturing Flywheel Architecture]]  
> **Master Registry:** [[_REGISTRIES/VENTURE_REGISTRY.yaml]]

---

## Overview

The `23-VENTURES` domain coordinates the lifecycle, portfolio allocation, sector assignment, repository mapping, and stage progression for **789 commercial ventures** across 35 sectors.

## Key Integration Points

1. **Public Showcase & Data Source:**
   - The authoritative source of truth for venture profiles is the **Venture Portal** (`src/data/portfolio.public.json`).
2. **Execution Flywheel:**
   - Detailed in [[_INFRASTRUCTURE/VENTURE-PORTAL-FLYWHEEL|VENTURE-PORTAL-FLYWHEEL.md]].
3. **Agent & Skill Allocation:**
   - Ventures are executed by swarms defined in [[_REGISTRIES/agents-by-sector.yaml]] utilizing playbooks in [[15-SKILLS/README|15-SKILLS]] and persistent actors in [[16-AGENTS/README|16-AGENTS]].

## Active Tier-1 Commercial Ventures

The following Tier-1 ventures have production-verified deployments and active monetization gateways:

| Venture ID | Brand Name | Sector | Commercial Status | Deployment & Links |
| :--- | :--- | :--- | :--- | :--- |
| [[23-VENTURES/RE-001\|RE-001]] | **WorldwideBro Holdings** | [[SECTORS/SEC-020-real-estate-property\|SEC-020 Real Estate]] | 🟢 **INCOME_READY** ($250 Underwriting / $499 Deal Room) | [re-001-worldwidebro-holdings.vercel.app](https://re-001-worldwidebro-holdings.vercel.app) |
| [[23-VENTURES/LT-005\|LT-005]] | **HealthRoute Courier** | [[SECTORS/SEC-017-logistics-transportation\|SEC-017 Logistics]] | 🟢 **INCOME_READY** ($45 Standard / $85 STAT / $1.2k Retainer) | [healthroute-courier.vercel.app](https://healthroute-courier.vercel.app) |
| [[23-VENTURES/CON-001\|CON-001]] | **ACE Construction** | [[SECTORS/SEC-002-construction-infrastructure\|SEC-002 Construction]] | 🟢 **INCOME_READY** ($299 Consultation / $1,500 Deposit) | [ace-construction.vercel.app](https://ace-construction.vercel.app) |
| [[23-VENTURES/OPS-001\|OPS-001]] | **WorldwideBro Staffing** | [[SECTORS/SEC-014-human-resources-staffing\|SEC-014 Staffing]] | 🟡 Operational Framework | [ops-staff-001-staffing.vercel.app](https://ops-staff-001-staffing.vercel.app) |
| [[23-VENTURES/LT-011\|LT-011]] | **CarrierDispatch / DispatchOS** | [[SECTORS/SEC-017-logistics-transportation\|SEC-017 Logistics]] | 🟢 **INCOME_READY** ($49/mo Starter / $149/mo Fleet Pro / $250 Escrow) | [lt-011-dispatch-software.vercel.app](https://lt-011-dispatch-software.vercel.app) |
| [[23-VENTURES/FIN-037\|FIN-037]] | **FinEngine Protocol** | [[SECTORS/SEC-008-financial-services\|SEC-008 Financial]] | 🟡 Validating | Institutional Models |
| [[23-VENTURES/EC-001\|EC-001]] | **DropCommerce OS** | [[SECTORS/SEC-021-retail-e-commerce\|SEC-021 E-Commerce]] | 🟡 Validating | Retail Storefronts |

## Status Distribution (789 Ventures)

- **Planned:** ~50%
- **Validating:** ~20%
- **Prototype:** ~15%
- **MVP:** ~10%
- **Operating / Income-Ready:** ~5%

