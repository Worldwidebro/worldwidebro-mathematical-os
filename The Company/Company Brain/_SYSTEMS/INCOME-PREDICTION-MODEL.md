# 🧮 INCOME-PREDICTION-MODEL: ML Revenue Forecasting for Ventures

**Date:** 2026-09-08 | **Version:** 1.0 | **Authority:** [[INTEGRATED-SYSTEM-ARCHITECTURE]] | [[CAPITAL-READINESS-ENGINE]]

**Purpose:** Predict venture revenue (Year 1-3) with confidence intervals, enabling capital allocation decisions

**Status:** READY TO TRAIN (Week 4, [[TRADING-INTEGRATION-PLAN]])

---

## EXECUTIVE SUMMARY

**What it predicts:** Year 1-3 revenue for each of 789 ventures  
**Input data:** TAM × market share × ARPU + sector-specific growth patterns + macro indicators  
**Output:** Revenue forecast ± confidence interval (e.g., "$590K ± 15%" for CON-001)  
**Update frequency:** Weekly (as customer data arrives in Supabase)  
**Accuracy target:** ±10% by week 4 of deployment

---

## THE MODEL: 3-STAGE PREDICTION

### Stage 1: Initial Projection (Top-Down)

**Formula:**
```
Year_1_Revenue = TAM × Market_Share × ARPU

Example (CON-001):
TAM = $85B (SE construction market)
Market_Share = 0.0007% (conservative estimate)
ARPU = $85,000 (average project value)
Year_1 = $85B × 0.0007% × $85K = $590K ✅
```

**By Sector (from [[SECTOR-TAXONOMY-MASTER]]):**

| Sector | TAM | Market Share Assumption | ARPU | Year 1 Revenue (Avg) |
|--------|-----|---|---|---|
| **SEC-013 (Construction)** | $85B | 0.0007% | $85K | $590K |
| **SEC-020 (Real Estate)** | $120B | 0.0015% | $250K | $1.8M |
| **SEC-031 (Finance)** | $180B | 0.001% | $500K | $2.1M |
| **SEC-006 (Logistics)** | $60B | 0.0008% | $45K | $780K |
| **SEC-004 (Technology)** | $200B | 0.0005% | $120K | $1.2M |

### Stage 2: Confidence Intervals (Historical Patterns)

**By Revenue Model Type:**

```
DIRECT REVENUE (e.g., CON-001 construction projects):
  Year 1: ± 15% CI (higher volatility, customer acquisition risk)
  Year 2: ± 10% CI (patterns emerge)
  Year 3: ± 8% CI (mature, predictable)

MARKETPLACE (e.g., LT-005 medical courier):
  Year 1: ± 18% CI (supply/demand balance uncertain)
  Year 2: ± 12% CI
  Year 3: ± 9% CI

SAAS SUBSCRIPTION (e.g., LT-011 fleet logistics):
  Year 1: ± 12% CI (churn risk lower, customer stickiness)
  Year 2: ± 8% CI
  Year 3: ± 6% CI

PORTFOLIO/RENTAL (e.g., RE-001 BRRRR):
  Year 1: ± 10% CI (asset-backed, more predictable)
  Year 2: ± 7% CI
  Year 3: ± 5% CI
```

### Stage 3: Actual Performance Tracking

**Weekly Update Logic:**
```python
def update_forecast(venture_id, week_actual_revenue):
    """
    Recalculate forecast as customer data arrives.
    Approach: exponential smoothing (momentum + projection weight)
    """
    
    prev_forecast = get_forecast(venture_id)
    momentum_weight = 0.7  # Recent data matters more
    projection_weight = 0.3  # Original estimate still valid
    
    if week_actual_revenue > 0:
        # Customer data arrived! Update the forecast
        new_forecast = (week_actual_revenue * momentum_weight +
                       prev_forecast * projection_weight)
        
        # Tighten confidence interval
        tracking_accuracy = week_actual_revenue / prev_forecast
        if 0.9 <= tracking_accuracy <= 1.1:
            ci_width = ci_width * 0.9  # Tighten by 10%
        elif tracking_accuracy < 0.5 or tracking_accuracy > 1.5:
            trigger_alert("Venture trending significantly off forecast")
        
        return new_forecast, ci_width
```

**Example (CON-001 Week 1-4):**

| Week | Actual Revenue | Forecast | Tracking % | Confidence Interval | Action |
|------|---|---|---|---|---|
| Week 0 (initial) | — | $49K | — | ±15% | Projection set |
| Week 1 | $45K | $49K | 92% | ±14% | On track, tighten CI |
| Week 2 | $52K | $50K | 104% | ±12% | Exceeding slightly |
| Week 3 | $48K | $50K | 96% | ±10% | Converging on forecast |
| Week 4 | $51K | $50K | 102% | ±9% | HIGH CONFIDENCE |
| **Year 1 Update** | +$196K (4 wks) | $588K → $595K | 98% | ±10% | Forecast locked |

---

## SECTOR-SPECIFIC GROWTH PATTERNS

### Construction (SEC-013) — 22 Ventures

**Growth Driver:** Building permits, unemployment, interest rates

```
Baseline (Year 1): $590K
Growth trajectory:
  Year 2: $1.25M (+112%) — customer acquisition accelerates
  Year 3: $4.8M (+284%) — market penetration + project complexity ↑

Macro sensitivity:
  Interest rates ↑ 1%: Year 1 revenue -8% (permits ↓)
  Unemployment ↓ 0.5%: Year 1 revenue +5% (labor available)
  Recession signal: Year 1 revenue -20% (projects halt)

Sector Control Plane: [[CP-013-Construction]]
Ventures at risk: Any with <6mo cash runway + <$50K customer pipeline
```

### Real Estate (SEC-020) — 38 Ventures

**Growth Driver:** Cap rates, inventory, Section 8 demand

```
Baseline (Year 1): $1.8M
Growth trajectory:
  Year 2: $2.4M (+33%) — portfolio stabilizes
  Year 3: $3.2M (+78%) — exit + reinvestment cycle

Macro sensitivity:
  Recession signal: Year 1 revenue -15% (defaults ↑, BRRRR stalls)
  Section 8 rates ↓: Year 1 revenue -10% (margins compress)
  Mortgage rates ↓: Year 1 revenue +20% (liquidity ↑, refinancing)

Sector Control Plane: [[CP-020-Real-Estate]]
Defensive signal: All RE ventures have asset backing (low default risk)
```

### Finance/Trading (SEC-031) — 45 Ventures

**Growth Driver:** Volatility, Fed policy, credit spreads

```
Baseline (Year 1): $2.1M (management fees @ 2% AUM)
Growth trajectory:
  Year 2: $3.2M (+52%) — AUM grows with market
  Year 3: $5.1M (+144%) — compounding returns

Macro sensitivity (DAILY updates):
  VIX > 25: trading volume ↑ → Year 1 revenue +25%
  Fed rate cuts: volatility ↑ → Year 1 revenue +15%
  Credit spreads widen: high-yield demand ↑ → +12%
  Recession: volatility spikes (month 1), then normalizes

Sector Control Plane: [[CP-031-Financial-Services]]
Most volatile sector (macro-driven month-to-month)
```

### Logistics (SEC-006) — 31 Ventures

**Growth Driver:** Freight rates, shipping volumes, fuel prices

```
Baseline (Year 1): $780K
Growth trajectory:
  Year 2: $1.4M (+79%) — network effects
  Year 3: $2.8M (+259%) — market consolidation

Macro sensitivity:
  Fuel prices ↑: Year 1 revenue -8% (COGS pressure, pricing lag)
  Shipping volumes ↓ 20%: Year 1 revenue -18% (demand down)
  Supply chain normalized: Year 1 revenue +12% (stability premium)

Sector Control Plane: [[CP-006-Logistics]]
Counter-cyclical to recession (people still need goods)
```

### Technology/SaaS (SEC-004) — 67 Ventures

**Growth Driver:** Adoption curves, churn, ARPU expansion

```
Baseline (Year 1): $1.2M
Growth trajectory:
  Year 2: $2.1M (+75%) — strong churn-resistant growth
  Year 3: $4.5M (+275%) — market expansion

Churn Model:
  Month 1-3: 20% churn (customer fit learning)
  Month 4-12: 5% churn (product-market fit established)
  Year 2+: 2% churn (mature, sticky product)

Macro resilience: COUNTER-CYCLICAL (companies cut costs → need automation SaaS)
  Recession: Year 1 revenue -5% (deal closure delays, not demand destruction)

Sector Control Plane: [[CP-004-Technology]]
Lowest risk sector (least macro-sensitive)
```

---

## TRAINING DATA (From [[ventures-by-sector.yaml]])

### Input Features (Per Venture)

```yaml
venture:
  id: CON-001
  sector_id: SEC-013
  revenue_model: DIRECT
  market_size: TAM_85B
  competitive_positioning: STRONG  # defensibility
  team_experience: 15y_construction
  customer_pipeline_value: $590K
  arpu_estimate: $85000
  market_share_target: 0.0007%
  
macro_context:
  interest_rate_environment: RISING  # affects construction
  sector_health: HEALTHY  # permits up
  competitive_intensity: MODERATE
  regulatory_risk: LOW
  supply_chain_risk: LOW
```

### Output Target (Per Venture)

```yaml
forecast:
  year_1_revenue: $590000
  year_1_confidence_interval: ±15%
  year_2_revenue: $1250000
  year_2_confidence_interval: ±10%
  year_3_revenue: $4800000
  year_3_confidence_interval: ±8%
```

---

## MODEL TRAINING PIPELINE

### Phase 1: Historical Calibration (Week 1-2)

**Data source:** BUSINESS-CAPITAL-DATA-ROOM/*/08_REVENUE/ (5 ventures with detailed models)

```python
# Train on 5 ventures with known Year 1 outcomes (or conservative projections)
training_ventures = [
  "CON-001",  # $590K baseline
  "LT-005",   # $780K baseline
  "LT-011",   # $3.2M baseline
  "OPS-001",  # $2.7M baseline
  "RE-001"    # $2.0M baseline
]

# Extract features:
features = []
for v in training_ventures:
  f = extract_tam_arpu_marketshare(v)  # Core TAM formula
  features.append({
    'tam': f['tam'],
    'market_share': f['market_share'],
    'arpu': f['arpu'],
    'sector_growth_rate': get_sector_growth(v['sector']),
    'team_experience_years': v['team_experience'],
    'competitive_moat': score_defensibility(v),
  })

# Train model
model = LinearRegression()  # Start simple
model.fit(features, targets=[v['year_1_revenue'] for v in training_ventures])
```

### Phase 2: Live Deployment (Week 3-4)

**Data source:** Supabase ventures table + weekly actuals

```python
def forecast_all_ventures():
    """Run weekly to update all 789 venture forecasts"""
    
    for venture in get_all_ventures():
        # Stage 1: Top-down projection
        projection = model.predict(venture.features)
        
        # Stage 2: Confidence interval (by revenue model type)
        ci = get_ci_by_model_type(venture.revenue_model)
        
        # Stage 3: Update if actuals available
        if venture.actual_revenue_this_week:
            projection = update_with_actuals(
                projection,
                venture.actual_revenue_this_week,
                momentum_weight=0.7
            )
            ci = tighten_ci(ci, tracking_accuracy)
        
        # Store in Neo4j + Supabase
        save_forecast(venture.id, {
            'projection': projection,
            'confidence_interval': ci,
            'confidence_level': 'HIGH' if ci < 10 else 'MEDIUM' if ci < 15 else 'LOW',
            'last_updated': now(),
            'based_on_actuals': venture.actual_revenue_this_week > 0
        })
```

---

## INTEGRATION: Neo4j + Supabase + iza-os-finance-advisor-bot

### Neo4j Schema (Forecast Nodes)

```cypher
(Venture)-[:HAS_FORECAST]->(Forecast {
  year_1_revenue: 590000,
  year_1_ci: 0.15,
  year_2_revenue: 1250000,
  year_2_ci: 0.10,
  year_3_revenue: 4800000,
  year_3_ci: 0.08,
  confidence_level: "HIGH",
  last_updated: "2026-09-15",
  tracking_vs_actual: 0.98,
  macro_adjustments: {
    interest_rates: -0.08,
    unemployment: +0.05
  }
})

(Forecast)-[:DRIVES]->(AllocationSignal {
  venture_id: "CON-001",
  allocate_pct: 12.5,
  capital_amount: $562500,
  rationale: "High readiness + tracking 98% of forecast"
})
```

### Supabase Tables

```sql
-- venture_forecasts (updated weekly)
CREATE TABLE venture_forecasts (
  venture_id UUID PRIMARY KEY,
  week_of DATE,
  year_1_forecast DECIMAL,
  year_1_ci DECIMAL,
  year_1_actual DECIMAL,
  tracking_pct DECIMAL,
  confidence_level TEXT,
  based_on_actuals BOOLEAN,
  macro_adjustments JSONB,
  updated_at TIMESTAMP
);

-- forecast_history (audit trail)
CREATE TABLE forecast_history (
  venture_id UUID,
  week_of DATE,
  forecast_previous DECIMAL,
  forecast_new DECIMAL,
  reason TEXT,  -- e.g., "actual +$45K", "interest rates ↑"
  created_at TIMESTAMP
);
```

---

## ACCURACY BENCHMARKS

### Target Accuracy by Week

| Week | Ventures with Actuals | Mean Absolute Error | Confidence Interval |
|---|---|---|---|
| Week 1 | 5-10 | ±20% | ±15% (initial) |
| Week 2 | 20-30 | ±15% | ±12% (tightening) |
| Week 3 | 50-70 | ±12% | ±10% (good) |
| Week 4 | 100+ | ±10% | ±8% (high) |

### Success Criteria

```
✅ ACHIEVED when:
- 80%+ of ventures within confidence interval
- Mean forecast error < ±10% after 4 weeks
- Sector growth patterns validated (construc. +100%, real estate +30%, etc.)
- Model updates weekly with zero errors
- Alerts fire when venture drifts >10% from forecast
```

---

## SECTOR-SPECIFIC FEATURES

### Construction (SEC-013)

```
Feature: Building Permits (from OpenBB)
  ↑ permits → ↑ demand for construction services
  lag: 1 month (permits approved → projects start)

Feature: Interest Rates (Fed rate from OpenBB)
  ↑ rates → ↓ construction demand (financing costs)
  lag: 2-3 weeks (fed announcements → builder decisions)

Feature: Unemployment (from Census via OpenBB)
  ↓ unemployment → ↑ construction labor availability
  lag: 1 month
```

### Real Estate (SEC-020)

```
Feature: Section 8 Rent Limits (HUD data)
  ↑ S8 rates → ↑ rental income potential
  lag: 1 month (new fiscal year)

Feature: Cap Rates (commercial real estate indices)
  ↓ cap rates → ↓ property valuations (squeeze margins)
  lag: immediate

Feature: Inventory (from MLS data)
  ↓ inventory → ↑ deal flow (BRRRR model)
  lag: 2 weeks
```

### Finance (SEC-031)

```
Feature: Volatility Index (VIX)
  ↑ VIX → ↑ trading volume → ↑ fee revenue
  lag: 1 day (immediate)

Feature: Credit Spreads (Fed data)
  ↑ spreads → ↑ high-yield trading activity
  lag: immediate
```

---

## MONITORING & ALERTING

### Weekly Report Template

```
VENTURE FORECAST ACCURACY REPORT — Week of 2026-09-15

Summary:
  Total ventures forecasted: 789
  Ventures with actual data: 45 (5.7%)
  Mean tracking accuracy: 98% ± 12%
  Confidence intervals tightened: 15% → 12% (avg)

Outliers (require intervention):
  ❌ LT-005: Tracking 5% vs 65% forecast (alert sent 2026-09-14)
    Root cause: Low driver incentive (market dynamics, not execution)
    Recommendation: Operational review + pricing adjustment
  
  ✅ CON-001: Tracking 98% vs 92% forecast (on target)
    Update: Raise Year 1 from $590K → $598K
  
  ✅ RE-001: Tracking 102% vs 95% forecast (exceeding)
    Update: Raise Year 1 from $2.0M → $2.1M

Macro Adjustments Applied:
  Interest rates ↑ 0.25%: Construction ventures adjusted -8%
  Fed rate hold: Finance ventures neutral
  Section 8 rates announced: RE ventures +2%

Capital Allocation Recommendation:
  Based on updated forecasts, reallocate from LT-005 (underperforming)
  to CON-001 (outperforming) and RE-001 (growth signal).
```

---

## REFERENCES

- [[TRADING-INTEGRATION-PLAN]] — Week 4 (forecasting activation)
- [[INTEGRATED-SYSTEM-ARCHITECTURE]] — Layer 3 (capital readiness model)
- [[SECTOR-TAXONOMY-MASTER]] — 35 sectors + growth patterns
- [[ventures-by-sector.yaml]] — 789 ventures + initial projections
- [[CAPITAL-READINESS-ENGINE]] — Readiness scoring methodology

---

**Status:** READY TO TRAIN | **Start:** Week 2 ([[TRADING-INTEGRATION-PLAN]]) | **Owned by:** iza-os-finance-advisor-bot

