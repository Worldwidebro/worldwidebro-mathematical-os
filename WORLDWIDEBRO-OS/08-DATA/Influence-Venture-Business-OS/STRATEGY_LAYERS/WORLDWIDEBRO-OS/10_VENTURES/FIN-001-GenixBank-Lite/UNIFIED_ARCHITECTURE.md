# GenixBank Unified Architecture

**Problem:** 4 repos (fin-001, fin-004, genixbank-financial-system, genixbank-insight-compass) causing confusion
**Solution:** ONE unified architecture clarity document

---

## 🏗️ The Architecture

```
PRODUCTS (Customer-Facing)
├── fin-001-genixbank-lite (SMB tier)
└── fin-004-genixbanks-ai-treasurer (Enterprise tier)
        ↓ (both use same backend)
SHARED BACKEND
└── genixbank-financial-system (transaction engine, integrations)
        ↓ (supplies data to)
ANALYTICS
├── genixbank-insight-compass (GenixBank analytics)
└── iza-os-analytics (cross-venture metrics)
```

---

## 📦 Repo Responsibilities

| Repo | Purpose | Used By | What's In It |
|------|---------|---------|------------|
| **fin-001-genixbank-lite** | SMB product frontend | Small teams ($25-100K ARR) | React/NextJS, landing page, basic dashboard |
| **fin-004-genixbanks-ai-treasurer** | Enterprise product frontend | Large companies ($500K+ ARR) | Advanced React app, compliance reporting, SSO |
| **genixbank-financial-system** | Core banking backend | BOTH products + FIN-002 through FIN-010 | Account APIs, transaction engine, Plaid/Stripe integration |
| **genixbank-insight-compass** | Analytics engine | GenixBank + internal dashboards | ML models, forecasting, spending patterns |

---

## 🎯 Key Clarity Points

### fin-001 vs fin-004
- **DIFFERENT PRODUCTS** (not versions of same thing)
- fin-001 = Consumer/SMB banking
- fin-004 = Enterprise treasury
- But **they use the SAME backend system** (genixbank-financial-system)

### genixbank-financial-system
- **THE SHARED CORE** that both products depend on
- Handles all banking operations
- Used by ALL FinTech ventures (FIN-001 through FIN-010)
- DO NOT DUPLICATE — use this for all FinTech products

### When to Create New Repos
- ✅ New **product** with different UI/UX = new product repo (fin-004)
- ❌ New **feature/service** = add to genixbank-financial-system
- ❌ New **analytics dashboard** = extend genixbank-insight-compass

---

## 🚀 Prevent This for All 629 Ventures

**Apply this architecture pattern to EVERY niche:**

```
NICHE CLUSTER (e.g., EdTech, Marketplace)
├── Product Repos (multiple, one per product tier)
├── Shared Backend Repo (ONE per niche)
└── Analytics Repo (ONE per niche)
```

**Example: EdTech with 69 ventures**
```
EdTech Cluster
├── edtech-course-platform-lite (basic courses)
├── edtech-academy-pro (premium courses)
├── edtech-lms-engine (shared backend)
└── edtech-analytics (learner insights)
```

All 69 EdTech ventures can use this same structure without recreating repos.

---

## ✅ Next Steps

1. **Document all 47 FinTech ventures** with this architecture
2. **Create REPO_MANIFEST.json** linking repos properly
3. **Set up CI/CD** so products auto-use latest backend
4. **Replicate pattern** for EdTech (69), Marketplace (195), etc.

**This one clarity document prevents repo fragmentation across all 629 ventures.**
