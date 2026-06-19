---
references:
  - [[VENTURE-MASTER]]
  - [[LOOP-FRAMEWORK]]
  - [[PLAN-WORKFLOW]]
  - [[FIN-036-ARBITRAGE-NEXUS]]
---

# Phase 7: Code Migration Plan — Complete Checklist

**Date:** 2026-06-05  
**Total Repos:** 44 (4 platform + 8 trading + 32 ventures)  
**Estimated Time:** 3 hours  
**Status:** Ready to execute

---

## PUSH ORDER (SEQUENTIAL + PARALLEL)

### Stage 0: GitHub Auth
- [ ] Unset: `unset GITHUB_TOKEN`
- [ ] Login: `gh auth login`
- [ ] Verify: `gh auth status`

### Stage 1: Platform Foundation (4 repos - SERIAL)
- [ ] **1.1 venture-hub** (verify existing)
- [ ] **1.2 iza-os-financial-core** (platform utilities)
- [ ] **1.3 genixbank-financial-system** (neobank shell)
- [ ] **1.4 genixbank-insight-compass** (analytics dashboards)

### Stage 2: Trading Stack (8 repos - SERIAL: FIN-023 first)
- [ ] **2.1 FIN-023: Investment Portfolio AI** ⭐ FIRST
- [ ] **2.2 FIN-026: Compliance Scanner** (depends on FIN-023)
- [ ] **2.3 FIN-004: Treasury** (depends on FIN-023)
- [ ] **2.4 FIN-031: Dashboards** (depends on FIN-023)
- [ ] **2.5 FIN-009: Crypto Tax**
- [ ] **2.6 FIN-022: Forecasting**
- [ ] **2.7 FIN-036: Arbitrage**
- [ ] **2.8 EM-015: Crypto** (optional)

### Stage 3: Non-Trading (32 repos - PARALLEL by tier)

**Tier 1 (Revenue-generating):**
- [ ] FIN-001: GenixBank Lite
- [ ] FIN-002: Credit Repair
- [ ] FIN-006: Tax Prep

**Tier 2 (Medium priority):**
- [ ] FIN-003, FIN-007, FIN-008
- [ ] FIN-011, FIN-021, FIN-033

**Tier 3 (Optional):**
- [ ] FIN-005, FIN-010, FIN-012-020
- [ ] FIN-024-025, FIN-027-032
- [ ] FIN-030, FIN-034-035

---

## PUSH COMMAND (Template for Each Repo)

```bash
# Clone
gh repo clone Worldwidebro/[REPO-NAME] ~/Documents/[PATH]/[REPO-NAME]
cd ~/Documents/[PATH]/[REPO-NAME]

# Copy code
cp -r ~/Documents/venture-hub/generated-books/[VENTURE-ID]/* src/

# Commit
git add .
git commit -m "scaffold: [venture description]"

# Push
git push -u origin main

# Verify
gh repo view Worldwidebro/[REPO-NAME]
```

---

## FILE MAPPING

```
venture-hub/generated-books/FIN-NNN/
├── business_model.md → docs/
├── roadmap.md → docs/
├── metrics.yaml → config/
└── assets/ → docs/

Each repo needs (NEW):
├── docs/integrations/ (OpenAPI specs)
├── .github/workflows/ (CI/CD)
├── .env.example
└── pyproject.toml
```

---

## VERIFICATION (Per Repo)

- [ ] Repo exists on GitHub
- [ ] Main branch has code (README, src/ folder)
- [ ] Register in venture-hub canonical_registry.json

```json
{
  "venture_id": "FIN-023",
  "repo_name": "fin-023-investment-portfolio-ai",
  "repo_url": "github.com/Worldwidebro/...",
  "has_code": true,
  "status": "live"
}
```

---

## TIME ESTIMATES

| Stage | Repos | Time |
|-------|-------|------|
| 0. Auth | 1 | 5 min |
| 1. Platform | 4 | 30 min |
| 2. Trading | 8 | 45 min |
| 3a. Tier 1 | 3 | 15 min |
| 3b. Tier 2 | 6 | 20 min |
| 3c. Tier 3 | 23 | 60 min |
| **Total** | **44** | **175 min (3 hrs)** |

---

## CHECKLIST

### Prerequisites
- [ ] GitHub auth fixed
- [ ] All venture code exists in venture-hub/
- [ ] venture-hub registry schema ready

### Execution
- [ ] Stage 0: Auth complete
- [ ] Stage 1: Platform 4/4 pushed
- [ ] Stage 2: Trading 8/8 pushed
- [ ] Stage 3: Tier 1 3/3 pushed
- [ ] Stage 3: Tier 2 6/6 pushed
- [ ] Stage 3: Tier 3 23/23 pushed

### Post-Push
- [ ] All 44 repos on GitHub
- [ ] All have src/, docs/, config/, tests/
- [ ] Integration docs created
- [ ] venture-hub registry updated
- [ ] CI/CD workflows active

---

## SUCCESS CRITERIA

✅ 44 repos pushed to Worldwidebro org  
✅ All repos self-contained (no code sharing)  
✅ All repos have integration docs  
✅ venture-hub registry updated (has_code=true)  
✅ CI/CD active (.github/workflows/)  

---

## Rollback Plan

- Repo deleted: Create new, repush
- Wrong code: Delete branch, repush
- Auth lost: `unset GITHUB_TOKEN`, login again
- All source in venture-hub backup
