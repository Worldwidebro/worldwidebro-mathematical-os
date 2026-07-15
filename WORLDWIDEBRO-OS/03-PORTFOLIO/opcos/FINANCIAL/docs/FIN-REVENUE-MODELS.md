---
references:
  - [[VENTURE-MASTER]]
  - [[FIN-SECTOR-VERTICALS-MAP]]
  - [[FIN-036-ARBITRAGE-NEXUS]]
---

# FIN Sector — Real Revenue Models (replaces broken boilerplate)

**Why this exists:** Every `fin-*` repo's `VENTURE.json` has an identical, copy-pasted
`revenue.model` field — *"Credit repair service ($150-300/mo) + funding consultation
($500 flat)," monthly_target $8,000* — confirmed by directly reading 7 repos'
`VENTURE.json` (FIN-001, FIN-002, FIN-004, FIN-006, FIN-009, FIN-013, FIN-023, FIN-034,
FIN-036). A generation script templated the first venture and stamped it unchanged
across the rest. `has_revenue_model=True` in `VENTURE-READINESS-SCORECARD.csv` only
checks the field is non-empty — it does not mean the model is real or differentiated.
This doc proposes an actual, product-grounded monetization mechanism per venture,
based on how comparable real products in each category charge.

**Date:** 2026-07-06

---

## Banking
| Venture | Proposed model |
|---|---|
| FIN-001 GenixBank Lite | $99/mo subscription (cash flow dashboard + AI expense tagging + invoicing) — matches its own `PRODUCT_SPECIFICATION.md`, which is the one repo where a real price already exists |
| FIN-025 Escrow Automation | 0.5–1% fee per escrowed transaction |

## Lending
| Venture | Proposed model |
|---|---|
| FIN-002 Credit Repair Automation | $150–300/mo subscription + $500 flat funding-consultation upsell (this is the one venture the boilerplate accidentally fits) |
| FIN-007 Business Credit Building | $99–199/mo subscription + one-time credit-building report fee |
| FIN-012 Invoice Factoring AI | 2–5% discount rate per invoice factored, plus a flat platform fee |
| FIN-020 Debt Consolidation AI | 1–3% lender placement/referral fee on consolidated loan amount |

## Payments
| Venture | Proposed model |
|---|---|
| FIN-013 Charity Donation AI | 2.5–3% transaction fee on donations processed |
| FIN-017 Remittance AI | FX spread + flat fee per transfer |
| FIN-019 Payment Gateway AI | 2.9% + $0.30 per transaction (standard gateway pricing) |

## Wealth Management
| Venture | Proposed model |
|---|---|
| FIN-015 Financial Wellness Coach | $19–49/mo consumer subscription, or B2B2C via employer benefits contracts |
| FIN-018 Wealth Transfer AI | $299–999 flat fee per estate plan generated + attorney referral commission |
| FIN-022 Budget Forecasting AI | $9–29/mo consumer subscription |

## Asset Management
| Venture | Proposed model |
|---|---|
| FIN-023 Investment Portfolio AI | 0.25–0.5% AUM fee, or flat $29–99/mo subscription tier |

## Investment Banking / Capital Markets
| Venture | Proposed model |
|---|---|
| FIN-016 Trade Finance AI | 0.5–1.5% fee on trade finance facilitated |
| FIN-031 Investor Dashboard Builder | $49–199/mo per-seat SaaS for funds/firms |
| FIN-036 Arbitrage Nexus Platform | Performance fee (10–20% of arbitrage profit) + flat platform subscription — **highest priority to fix**, this is the only "active/growth" FIN venture and it's currently documented as selling credit repair |

## Venture Capital
| Venture | Proposed model |
|---|---|
| FIN-024 Crowdfunding AI | 5–8% fee on funds raised (standard crowdfunding platform cut) |

## Insurance
| Venture | Proposed model |
|---|---|
| FIN-035 Insurance Underwriting AI | B2B SaaS license to insurers (per-quote/API-call fee) or % of referred premium |

## FinTech / RegTech
| Venture | Proposed model |
|---|---|
| FIN-003 AI Boss Hub Lite | $49–99/mo SaaS subscription |
| FIN-026 Financial Compliance Scanner | $199–499/mo B2B SaaS, per institution monitored |
| FIN-029 Compliance Wallet SaaS | $49–149/mo per-seat SaaS |

## Accounting
| Venture | Proposed model |
|---|---|
| FIN-006 Tax Prep Filing Services | $49–199 per filing (already has a real landing page — one of only 6 FIN repos with actual site code) |
| FIN-008 Business Formation Services | $99–499 flat fee per entity formed + annual registered-agent renewal |
| FIN-009 Crypto Tax Optimizer | $49–149/yr subscription (CoinTracker/Koinly-style pricing) |
| FIN-011 Automated Bookkeeping | $49–149/mo subscription (Bench/Pilot-style tier) |
| FIN-014 Expense Tracker AI | $9–19/mo consumer, or per-seat B2B |
| FIN-021 Tax Deduction Finder | Freemium + $9.99 one-time or seasonal subscription |
| FIN-033 AI Tax Preparation Service | $79–249 per filing |

## Treasury
| Venture | Proposed model |
|---|---|
| FIN-004 GenixBanks AI Treasurer | 0.1–0.3% of AUM managed, or flat $199–999/mo for venture-studio treasury management |
| FIN-034 Payroll Automation | $5–10 per employee/month (standard payroll SaaS pricing) |

## Miscategorized (not finance, but still need a real model since they're active in the FIN-* range)
| Venture | Proposed model |
|---|---|
| FIN-005 U-Haul Rental Affiliate | Affiliate commission per referred rental |
| FIN-010 AI-Powered Garbage Collection | B2B SaaS, per-route/per-truck fee to waste haulers |
| FIN-027 Patent Writer AI | $29–79/mo subscription or per-document fee |
| FIN-028 Legal Analyzer AI | $29–79/mo subscription or per-document fee |
| FIN-030 Local SEO Ranker AI | $99–299/mo SaaS per local business |
| FIN-032 Legal Toolkit AI | $29–79/mo subscription or per-document fee |

---

## Next step

These are proposed, not yet written back into each repo's `VENTURE.json`. If you want
these live (so the readiness scorecard's `has_revenue_model` reflects reality instead of
the copy-paste bug), the fix is a script that walks all 36 `fin-*` repos and replaces the
`revenue.model` field with the row above — same pattern as the capability-backfill fix
described in `[[venture-readiness-audit-2026-07-06]]`.
