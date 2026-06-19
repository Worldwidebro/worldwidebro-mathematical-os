# Platform Repos — Integration Matrix

**Platform Layer:** Shared infrastructure for all FIN ventures  
**Date:** 2026-06-05  
**Source:** venture-hub/docs/FIN_REPO_DELEGATION.md

---

## 4 Platform Repos & Ownership

### 1. genixbank-financial-system
**Owns:** Neobank shell (landing, auth, account views, calls venture APIs)  
**Calls:**
- FIN-023 (portfolio data)
- FIN-004 (treasury data)
- FIN-026 (compliance status)

### 2. genixbank-insight-compass
**Owns:** Analytics dashboards, insight UI  
**Calls:**
- FIN-023 (portfolio metrics)
- DuckDB (aggregations)

### 3. iza-os-financial-core
**Owns:** Forecasting, advisory orchestration, compliance utilities, investment APIs  
**Called by:** All FIN ventures for shared services

### 4. venture-hub
**Owns:** Registry, VBM, roadmaps, adoption log, delegation map  
**Called by:** All agents for venture reference data

---

## Integration Contracts (OpenAPI)

### genixbank-financial-system → FIN-023
**File:** `genixbank-financial-system/docs/integrations/fin-023-api.yaml`  
**Endpoints:**
- GET /portfolio/positions
- GET /portfolio/performance
- GET /portfolio/risk
- POST /portfolio/rebalance

### genixbank-financial-system → FIN-004
**File:** `genixbank-financial-system/docs/integrations/fin-004-api.yaml`  
**Endpoints:**
- GET /treasury/balance
- GET /treasury/allocation
- GET /treasury/cashflow

### genixbank-financial-system → FIN-026
**File:** `genixbank-financial-system/docs/integrations/fin-026-api.yaml`  
**Endpoints:**
- GET /compliance/status
- GET /compliance/violations

### All Ventures → venture-hub Registry
**File:** `venture-hub/docs/integrations/registry-api.yaml`  
**Endpoints:**
- GET /ventures/{venture_id}
- POST /ventures/{venture_id}/metrics

### All Ventures → iza-os-financial-core
**File:** `iza-os-financial-core/docs/integrations/advisory-api.yaml`  
**Endpoints:**
- POST /forecast
- GET /compliance-rules
- POST /risk-check

---

## Data Sync Points

| From | To | Frequency | Data |
|------|----|-----------| -----|
| Supabase | venture-hub | Real-time | Ventures, contacts |
| FIN-023 | genixbank | Every 1min | Portfolio metrics |
| FIN-023 | iza-os-core | Every 1h | Performance data |
| DuckDB | genixbank | Every 5min | Analytics |

---

## Deployment Order

1. venture-hub (registry)
2. iza-os-financial-core (shared utils)
3. genixbank-financial-system (shell)
4. genixbank-insight-compass (dashboards)
5. FIN-023 & FIN-004 (core trading/treasury)
