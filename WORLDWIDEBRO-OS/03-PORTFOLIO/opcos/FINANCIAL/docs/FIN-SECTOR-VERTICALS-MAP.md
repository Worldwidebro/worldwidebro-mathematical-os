---
references:
  - [[VENTURE-MASTER]]
  - [[LOOP-FRAMEWORK]]
  - [[FIN-036-ARBITRAGE-NEXUS]]
---

# FIN Sector — Verticals & Business-Type Map

**Purpose:** Classify all 36 FIN-* ventures into the finance-industry vertical taxonomy
(Banking, Lending, Payments, Wealth Management, Asset Management, Investment Banking,
Venture Capital, Private Equity, Insurance, FinTech, Accounting, Treasury, Capital Markets)
so the finance-sector site (Home → Verticals → Business Types → Companies → Software →
Jobs → Workflows) has a real content map instead of a flat venture list.

**Halo (USD Halo) is the front door.** It sits above this structure as the sector
landing/hero page — GenixBank's premium marketing front end — before a visitor drops
into the deeper per-vertical pages described below. It is not itself a vertical page.

**Date:** 2026-07-06
**Source:** `VENTURES-CAPABILITIES-MAPPED.csv` (36 FIN-* rows, current canonical names),
cross-checked against live GitHub repo contents. Supersedes the ad-hoc 5-category
grouping in `FIN-PHASE-5-ORGANIZATION-GUIDE.md`, which uses stale venture names from
before a venture-ID renaming pass (e.g. its FIN-005 "Digital Treasury Pro" is now
"U-Haul Rental Affiliate" in the current CSV).

---

## Verticals (Business Type this vertical primarily equips)

### Banking — serves Banks, GenixBank itself
| Venture | Repo | Notes |
|---|---|---|
| FIN-001 GenixBank Lite | `fin-001-genixbank-lite` (validated, PMF 0.83) + backend `genixbank-financial-system` | Front door = Halo landing page |
| FIN-025 Escrow Automation | unmapped | Banking-adjacent settlement |

### Lending — serves Banks, FinTech Companies
| Venture | Repo |
|---|---|
| FIN-002 Credit Repair Automation | unmapped |
| FIN-007 Business Credit Building | unmapped |
| FIN-012 Invoice Factoring AI | unmapped |
| FIN-020 Debt Consolidation AI | unmapped |

### Payments — serves FinTech Companies, Banks
| Venture | Repo |
|---|---|
| FIN-013 Charity Donation AI | unmapped |
| FIN-017 Remittance AI | unmapped |
| FIN-019 Payment Gateway AI | unmapped |

### Wealth Management — serves Family Offices, individuals
| Venture | Repo |
|---|---|
| FIN-015 Financial Wellness Coach | unmapped |
| FIN-018 Wealth Transfer AI | unmapped |
| FIN-022 Budget Forecasting AI | unmapped |

### Asset Management — serves Family Offices, Hedge Funds
| Venture | Repo |
|---|---|
| FIN-023 Investment Portfolio AI | `fin-023-investment-portfolio-ai` (trading stack, has PROJECT_GUIDE.md) |

### Investment Banking / Capital Markets — serves Banks, Hedge Funds, VC Firms
| Venture | Repo |
|---|---|
| FIN-016 Trade Finance AI | unmapped |
| FIN-031 Investor Dashboard Builder | trading stack, read-only client of FIN-023 |
| FIN-036 Arbitrage Nexus Platform | **only active/growth-stage FIN venture** — see `FIN-036-ARBITRAGE-NEXUS-REFERENCE.md` |

### Venture Capital — serves VC Firms
| Venture | Repo |
|---|---|
| FIN-024 Crowdfunding AI | unmapped |

### Insurance — serves Insurance Companies
| Venture | Repo |
|---|---|
| FIN-035 Insurance Underwriting AI | unmapped |

### FinTech / RegTech (horizontal — compliance & infra, not a single business type)
| Venture | Repo |
|---|---|
| FIN-003 AI Boss Hub Lite | unmapped |
| FIN-026 Financial Compliance Scanner | trading stack, KYC/AML |
| FIN-029 Compliance Wallet SaaS | unmapped |

### Accounting — serves Conglomerates, FinTech Companies, SMBs
| Venture | Repo |
|---|---|
| FIN-006 Tax Prep Filing Services | unmapped |
| FIN-008 Business Formation Services | unmapped |
| FIN-009 Crypto Tax Optimizer | unmapped |
| FIN-011 Automated Bookkeeping | unmapped |
| FIN-014 Expense Tracker AI | unmapped |
| FIN-021 Tax Deduction Finder | unmapped |
| FIN-033 AI Tax Preparation Service | unmapped |

### Treasury — serves Conglomerates, GenixBank
| Venture | Repo |
|---|---|
| FIN-004 GenixBanks AI Treasurer | trading stack, treasury allocation engine |
| FIN-034 Payroll Automation | unmapped |

*(No FIN-* venture currently maps to Private Equity — noted gap.)*

---

## ⚠️ Miscategorized (tagged `financial` but not actually finance)

These 6 ventures sit in the FIN-* numbering range but belong to other sectors. Flagging
so they don't get forced into a finance vertical page:

| Venture | Actual domain |
|---|---|
| FIN-005 U-Haul Rental Affiliate | Logistics / affiliate commerce |
| FIN-010 AI-Powered Garbage Collection | Logistics / waste management |
| FIN-027 Patent Writer AI | Legal |
| FIN-028 Legal Analyzer AI | Legal |
| FIN-030 Local SEO Ranker AI | Marketing |
| FIN-032 Legal Toolkit AI | Legal |

---

## Summary

- 36 FIN-* ventures total → 30 genuinely finance, 6 miscategorized (legal/logistics/marketing).
- Only **FIN-036** is active/growth stage; everything else is `planned`.
- **GenixBank (FIN-001 + FIN-004 + platform repos) is the most-built cluster** — real
  product code exists across 4 repos even though local venture folders still say
  "planned, no repos mapped" (stale metadata — same pattern as the repo-site-scan finding).

### Correction (2026-07-06, later same day)

The "unmapped" labels above were wrong. Every `fin-001` through `fin-036` repo **exists**
on GitHub (confirmed via `gh repo list Worldwidebro --limit 900`, 38 relevant repos found
including a `fin-033` name collision — `fin-033-ai-tax-preparation-service` and
`fin-033-legal-toolkit-ai` both exist, needs de-duplication). So "unmapped" was never
accurate — repos exist, they just have no site/frontend code in most cases.

Cross-checked against `repos-with-sites.json` (96/864 owned repos have any site signal):
only **6 of the 38 FIN/GenixBank repos have site code at all**:
`fin-006-tax-prep-filing-services`, `fin-009-crypto-tax-optimizer`,
`fin-021-tax-deduction-finder`, `fin-033-ai-tax-preparation-service`,
`genixbank-financial-system`, `genixbank-insight-compass`. The other 32 repos are
formation/docs-stage only (`FORMATION.md`/`FUNDING.md`/`GRANTS.md`/`PRODUCT_SPECIFICATION.md`
pattern, no frontend).

**No proven frontend template exists for these ventures.** The only reusable-template
doc in the system, `SAAS-BACKEND-KIT-TEMPLATE.md`, is backend-only and says
"Proven instance: none built yet." `genixbank-hero-site` (this session, Vite + React +
TS + Tailwind + lucide-react, Navbar/Hero/Info/BackedBy/UseCases + a per-vertical
wireframe page) is the first landing-page template of this kind for the FIN sector —
nothing preceded it.
