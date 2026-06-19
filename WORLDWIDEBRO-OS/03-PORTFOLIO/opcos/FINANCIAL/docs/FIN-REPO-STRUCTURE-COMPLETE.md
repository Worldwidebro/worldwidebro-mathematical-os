---
references:
  - [[VENTURE-MASTER]]
  - [[LOOP-FRAMEWORK]]
  - [[PLAN-WORKFLOW]]
  - [[FIN-036-ARBITRAGE-NEXUS]]
---

# FIN Sector Repo Structure — Complete Implementation

**Date:** 2026-06-05  
**Status:** ✅ Phase 2 Complete — Folder Structure Ready  
**Canonical Reference:** venture-hub/docs/FIN_REPO_DELEGATION.md

---

## Folder Hierarchy

```
~/Documents/
├── platform-repos/                           (4 platform repos)
│   ├── genixbank-financial-system/
│   ├── genixbank-insight-compass/
│   ├── iza-os-financial-core/
│   └── [Each: src/, docs/integrations/, config/, tests/, README.md]
│
├── fin-trading-stack/                        (8 trading repos)
│   ├── fin-004-genixbanks-ai-treasurer/
│   ├── fin-023-investment-portfolio-ai/
│   ├── fin-026-financial-compliance-scanner/
│   ├── fin-031-investor-dashboard-builder/
│   └── [Each: src/, config/, scripts/, docs/, tests/, README.md]
│
├── fin-ventures/                             (32 venture repos)
│   ├── fin-001-genixbank-lite/
│   ├── fin-002-credit-repair-automation/
│   ├── ... (FIN-003 through FIN-036)
│   └── [Each: src/, docs/, config/, tests/, README.md]
│
└── venture-hub/                              (existing, canonical registry)
```

---

## Platform Layer Repos

| Repo | Owns | Does NOT Own |
|------|------|------------|
| genixbank-financial-system | Landing, auth, accounts, neobank shell | Tax, portfolio engine, credit workflows |
| genixbank-insight-compass | Dashboards, insight UI | Raw data pipelines |
| iza-os-financial-core | Forecasting, advisory, compliance utils, investment APIs | Single-product tax, escrow |

---

## Trading Stack Repos

| Repo | Concern | Key Files |
|------|---------|-----------|
| fin-023 | Event bus, strategies, risk, journal, Alpaca | trading_os/, strategies.yaml, risk.yaml |
| fin-031 | Portfolio dashboards (read-only) | Dashboard code, FIN-023 client |
| fin-004 | Treasury, post-trade allocation | Allocation YAML, treasury cron |
| fin-026 | Trade compliance, KYC/AML | Audit rules, AML adapters |

---

## Venture Structure (Per Repo)

```
fin-ventures/fin-NNN-*/
├── src/              → Application code
├── docs/             → Documentation
├── config/           → Configuration files
├── tests/            → Test suite
└── README.md         → Venture overview
```

---

## Next Steps

1. ✅ Phase 1: Audit complete
2. ✅ Phase 2: Folder structure created
3. ⏳ Phase 3: Organize platform repos + docs
4. ⏳ Phase 4: Organize trading stack
5. ⏳ Phase 5: Organize non-trading ventures
6. ⏳ Phase 6: Integration documentation
7. ⏳ Phase 7: Code migration plan

---

## Priority Clones (Ready for GitHub Auth + Push)

1. FIN-023 (investment-portfolio-ai) — Has PROJECT_GUIDE.md
2. genixbank-financial-system — Platform repo
3. FIN-036 (arbitrage-nexus-platform) — Active venture
4. FIN-004 (ai-treasurer) — Treasury automation
