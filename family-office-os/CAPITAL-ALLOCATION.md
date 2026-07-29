# Capital Allocation Framework

**Scope:** Formulas, thresholds, and decision criteria for capital deployment  
**Status:** Production-ready  
**Generated:** 2026-07-28

---

## Allocation Formula Overview

Capital allocation is formula-driven, auditable, and re-balanced weekly. The system allocates capital from the holding company pool to 38 OPCOs, then OPCOs deploy to ventures.

---

## Tier-Based Allocation Model

### Tier Classification

| Tier | OPCOs | Pool Share | Criteria | ROI Target |
|------|-------|-----------|----------|-----------|
| **1 (Mature)** | SaaS, Finance, Commerce, Investment | 27% | 90%+ deploy rate, 15%+ ROI | 18%+ |
| **2 (Growth)** | Education, Knowledge, Training, Data, Technology | 21% | 70%+ deploy rate, 10%+ ROI | 12%+ |
| **3 (Early)** | Environment, Gov, Consulting, Security, Healthcare | 18% | 50%+ deploy rate, any ROI | 8%+ |
| **Reserve** | All sectors (emergency/pivot fund) | 15% | Held idle until deployment spike | — |
| **Strategic** | Cross-OPCO initiatives, infrastructure | 19% | Board-approved initiatives | 20%+ |

---

## Allocation Formulas

### Tier 1: Mature OPCOs (27% = $135M at $500M pool)

**Base Formula:**
```
T1_Allocation = (Pool × 0.27) × (Realized_ROI / 0.15) × Velocity_Factor

Where:
  Realized_ROI = average of last 12 months actual ROI
  Velocity_Factor = (Deployments_This_Month / Target_Deployments_This_Month)
  Target_Deployments = (Allocated_Amount / Average_Deal_Size)
```

**Example Calculation:**

```
Given:
  Total Pool = $500M
  OPCO-SaaS Tier 1 base share = $500M × 0.27 = $135M
  OPCO-SaaS Realized ROI (12mo avg) = 18%
  OPCO-SaaS Velocity Factor = 0.92 (deployed 92% of target this month)

Result:
  OPCO-SaaS_Allocation = $135M × (0.18 / 0.15) × 0.92
                       = $135M × 1.2 × 0.92
                       = $148.46M
  
  Note: SaaS outperformed ROI target, so gets 10% bonus.
        Velocity slightly below 100%, so penalty of 8%.
        Net effect: +2% uplift from base.
```

**Guardrails:**
- Maximum allocation: base × 1.5 (50% upside cap)
- Minimum allocation: base × 0.75 (25% downside floor)
- Realized ROI below 10% → automatic review, possible reclassification

---

### Tier 2: Growth-Stage OPCOs (21% = $105M)

**Base Formula:**
```
T2_Allocation = (Pool × 0.21) × (Realized_ROI / 0.10) × min(Velocity_Factor, 1.2)

Where:
  Realized_ROI = average of last 12 months actual ROI (or forecast if < 12mo history)
  Velocity_Factor = (Deployments_This_Month / Target_Deployments_This_Month)
  Velocity cap = 1.2 (cannot exceed 20% above target even if high deployment)
```

**Example Calculation:**

```
Given:
  Pool = $500M
  OPCO-Education Tier 2 base share = $500M × 0.21 = $105M
  OPCO-Education Realized ROI (12mo avg) = 11%
  OPCO-Education Velocity Factor = 1.15 (deployed 115% of target)

Result:
  OPCO-Education_Allocation = $105M × (0.11 / 0.10) × min(1.15, 1.2)
                            = $105M × 1.1 × 1.15
                            = $131.81M
  
  Note: ROI above target (+10%), velocity above target (+15%).
        Velocity capped at 1.2 to prevent over-deployment.
        Net effect: +25.5% uplift from base.
```

**Guardrails:**
- Maximum allocation: base × 1.5 (50% upside cap)
- Minimum allocation: base × 0.6 (40% downside floor, more aggressive than T1)
- Realized ROI below 5% → automatic review and potential demotion to T3

---

### Tier 3: Early-Stage OPCOs (18% = $90M)

**Base Formula:**
```
T3_Allocation = (Pool × 0.18) × (1 + Growth_Rate_6mo) × min(Velocity_Factor, 1.0)

Where:
  Growth_Rate_6mo = (Current_Realized_ROI - Prior_6mo_ROI) / Prior_6mo_ROI
  Velocity_Factor = (Deployments_This_Month / Target_Deployments_This_Month)
  Velocity cap = 1.0 (conservative, cannot exceed target even if deployment surge)
```

**Example Calculation:**

```
Given:
  Pool = $500M
  OPCO-Environment Tier 3 base share = $500M × 0.18 = $90M
  OPCO-Environment Prior 6mo ROI = 4%
  OPCO-Environment Current ROI (12mo avg) = 7%
  OPCO-Environment Growth Rate = (0.07 - 0.04) / 0.04 = 0.75 (75% improvement!)
  OPCO-Environment Velocity Factor = 1.05 (deployed 105% of target)

Result:
  OPCO-Environment_Allocation = $90M × (1 + 0.75) × min(1.05, 1.0)
                              = $90M × 1.75 × 1.0
                              = $157.5M
  
  Note: Extraordinary growth trajectory (75%), so gets 75% uplift.
        Velocity above target but capped at 1.0 (conservative for early stage).
        Net effect: +75% uplift from base (justifies acceleration).
```

**Guardrails:**
- Maximum allocation: base × 2.0 (100% upside cap, aggressive for high-growth)
- Minimum allocation: base × 0.4 (60% downside floor, very conservative)
- Growth rate negative (declining ROI) → automatic review and possible reclassification
- Confidence scoring for all T3 decisions (must exceed 70%)

---

### Reserve Pool (15% = $75M)

**Allocation Rule:**
```
Reserve_Allocation = Pool × 0.15 (fixed, held idle)

Deployment triggers:
  - OPCO requests surge capital (unplanned deployment spike)
  - Emergency acquisition or pivot
  - Venture failure recovery (backstop for failed ventures)
  - Cross-OPCO opportunity (board approval required)

Recharge rule:
  Any month-end reserve drawdown > 20% auto-triggers recharge from ROI surplus
```

**Access Control:**
- < $5M: OPCO lead approval
- $5M–$25M: CFO approval
- > $25M: Board approval

---

### Strategic Pool (19% = $95M)

**Allocation Rule:**
```
Strategic_Allocation = Pool × 0.19 (reserved for initiatives)

Eligible uses:
  - Cross-OPCO ventures (venture serves multiple OPCOs)
  - Technology/infrastructure shared by 3+ OPCOs
  - New OPCO launch (bootstrapping capital)
  - M&A/consolidation fund
  - Hedge fund or secondary investment

Approval gate:
  All Strategic allocations require board approval (no autonomous deployment)
```

**Example:** Vex Engine platform serves 30+ ventures across 15 OPCOs → $2.5M from Strategic pool (board-approved)

---

## Deployment Decision Thresholds

### Per-Venture Deployment

| Amount | Approval Process | SLA | Auto-Escalate |
|--------|------------------|-----|----------------|
| < $50K | Auto-approved (log only) | 0 (immediate) | No |
| $50K–$100K | Auto-approved if confidence > 70% | 0–1h | Yes if confidence 60–70% |
| $100K–$500K | OPCO lead approval (async) | 2 hours | Yes if breached |
| $500K–$1M | OPCO lead + CFO approval (async) | 6 hours | Yes if breached |
| $1M+ | Board approval (sync) | 24 hours | Yes (board meeting required) |

**Confidence Scoring:**
- Agent computes confidence for each deployment decision (0–100%)
- Inputs: venture ROI history, sector performance, OPCO velocity, market conditions
- Threshold: > 70% auto-approved (up to limits); 60–70% escalates to human; < 60% rejected

---

## Deployment Log: Field Calculation

### predicted_roi_pct Calculation

```
predicted_roi_pct = (
  Historical_OPCO_ROI × 0.4 +           (40% weight: OPCO track record)
  Venture_Sector_Benchmark × 0.3 +      (30% weight: sector average)
  Venture_Stage_Adjustment × 0.2 +      (20% weight: seed/growth/mature)
  Market_Sentiment_Factor × 0.1         (10% weight: macro conditions)
)

Example:
  OPCO-SaaS historical ROI = 18%
  SaaS sector benchmark = 12%
  Venture stage (growth) adjustment = +2%
  Market sentiment (stable) = neutral (1.0x)
  
  predicted_roi = (18 × 0.4) + (12 × 0.3) + (2 × 0.2) + (1.0 × 0.1)
                = 7.2 + 3.6 + 0.4 + 0.1
                = 11.3%
```

### actual_roi_pct Calculation (post-deployment)

```
actual_roi = (Exit_Value - Deployed_Amount) / Deployed_Amount × 100

Examples:
  Deployed $100K, exited at $150K → +50%
  Deployed $100K, still operating (valuation $120K) → +20% (interim)
  Deployed $100K, failed (valued $0) → -100%
  Deployed $100K, still operating (valuation $85K) → -15% (interim)

Note: actual_roi_pct remains NULL until exit/failure/significant milestone.
      Dashboard shows interim valuations separately.
```

---

## Re-allocation Cadence

### Weekly Rebalance (Mondays 6am UTC)

```python
# Pseudocode
for each OPCO in Tier1, Tier2, Tier3:
  realized_roi = calculate_12mo_roi(OPCO)
  velocity_factor = deployments_this_week / target_deployments_this_week
  new_allocation = apply_formula(OPCO.tier, realized_roi, velocity_factor)
  
  if abs(new_allocation - current_allocation) > 5%:
    update opco_capital_allocations table
    create capital_decisions record (type='rebalance', reasoning=...)
    notify OPCO lead (Slack)
  else:
    # within variance tolerance, no action
    pass
```

### Monthly Rebalance (1st of month, 12am UTC)

```
Trigger: Realized ROI performance reconciliation
Actions:
  1. Calculate actual ROI for all deployments that matured in prior month
  2. Compare predicted vs actual (track forecast error)
  3. Reclassify any OPCO that crossed tier threshold:
     - T1 to T2 if ROI < 12% or deploy rate < 70%
     - T2 to T1 if ROI > 15% and deploy rate > 85%
     - T2 to T3 if ROI < 5%
     - T3 to T2 if ROI > 10% and growth rate positive
  4. Adjust Reserve and Strategic allocations based on drawdown
  5. Board notification of reclassifications
```

### Quarterly Strategic Review (1st of quarter, 2pm UTC)

```
Trigger: Tier reassessment, strategy update
Agenda:
  1. Review ROI forecast vs actual (identify systemic biases)
  2. Propose tier adjustments based on 12-month track record
  3. Reallocate Strategic pool based on approved initiatives
  4. Review Reserve pool adequacy (target: 15% undeployed)
  5. Board vote on any changes to tier definitions or percentages
```

---

## Guardrails & Constraints

### Hard Limits

| Constraint | Limit | Reason |
|-----------|-------|--------|
| Max weekly OPCO drawdown | 50% of quarterly allocation | Prevent boom-bust cycles |
| Max monthly pool drawdown | 70% of pool | Preserve emergency reserves |
| Max single deal | $5M | Concentration risk |
| Min OPCO allocation | 5% of tier base | Maintain minimum velocity |
| Confidence threshold | 60% | Prevent under-researched decisions |

### Soft Alerts (trigger review, not block)

| Alert | Threshold | Action |
|-------|-----------|--------|
| OPCO over-velocity | > 70% weekly drawdown | Slack alert to CFO |
| ROI forecast error | > 10% variance | Monthly review, adjust formula |
| Reserve pool low | < 10% undeployed | Auto-trigger recharge from ROI surplus |
| Approval SLA breach | > 2h for $100K–$1M | Escalate to board |
| Agent confidence decline | < 65% rolling avg | Review agent decision model |

---

## Examples & Scenarios

### Scenario 1: High-Growth OPCO

```
OPCO-Education starts at T2 (21% share = $105M)
  Month 1: ROI 8%, velocity 80% → allocation $105M
  Month 2: ROI 12%, velocity 90% → allocation $122M (+16%)
  Month 3: ROI 15%, velocity 95% → allocation $138M (+13%)
  Quarter end: Promoted to T1
  Next quarter: Assigned 27% share = $135M base
  Result: 28% total uplift from base tier share
```

### Scenario 2: Declining OPCO

```
OPCO-Consulting starts at T2 (21% share = $105M)
  Month 1: ROI 8%, velocity 70% → allocation $88M (-16%)
  Month 2: ROI 6%, velocity 60% → allocation $63M (-28%)
  Month 3: ROI 4%, velocity 50% → allocation $45M (-29%)
  Quarter end: Demoted to T3
  Next quarter: Assigned 18% share = $90M base
  Action: CFO reviews OPCO strategy, considers leadership change
  Result: Risk-managed, capital preserved
```

### Scenario 3: Emergency Drawdown

```
OPCO-SaaS has $50M allocated, requests $30M for acquisition
  Deployment SLA: $1M+ → requires board approval (24h)
  Confidence: 78% (high, acquisition of strategic competitor)
  Board decision: approved (next day)
  Reserve drawn: $20M (acquisition shortfall)
  Audit record: capital_decisions entry created
  Compliance: Reserve recharge triggered (75% of used reserve)
  Result: Acquisition proceeds, reserves replenished within 2 weeks
```

---

## Audit & Compliance

**Every decision creates a record in `capital_decisions` table:**

```json
{
  "id": "uuid",
  "decision_type": "deployment",
  "opco_name": "OPCO-SaaS",
  "amount": 250000,
  "decision_maker": "agent_opco_saas_01",
  "decision_date": "2026-07-28T14:32:00Z",
  "reasoning": {
    "formula_used": "Tier1",
    "confidence": 0.82,
    "predicted_roi_pct": 15.5,
    "venture_id": "SaaS-042",
    "supporting_data": {
      "opco_12mo_roi": 0.18,
      "sector_benchmark": 0.12,
      "venture_growth_rate": 0.35,
      "market_sentiment": "positive"
    }
  },
  "approval_status": "auto",
  "created_at": "2026-07-28T14:32:00Z"
}
```

---

## Testing & Validation

### Backtesting Allocation Model

```
Run all 2025 deployments through allocation formula:
  1. Did formulas correctly predict tier-based deployment?
  2. Did confidence scoring correlate with actual outcomes?
  3. Were ROI predictions within ±15% of actuals?
  4. Did guardrails prevent any concentrated risks?

Report: Allocation Accuracy Report (monthly)
  - Prediction error by tier
  - Tier reclassification accuracy
  - Guideline compliance violations (if any)
  - Recommendations for formula adjustment
```

---

## Version History

| Date | Version | Change |
|------|---------|--------|
| 2026-07-28 | 1.0 | Initial framework complete |

---

**Generated:** 2026-07-28  
**Status:** Production-ready for Supabase deployment
