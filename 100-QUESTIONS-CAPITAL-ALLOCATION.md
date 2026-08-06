# 100 QUESTIONS: CAPITAL ALLOCATION INTELLIGENCE

**Framework:** Systems-level capital allocation for 712 ventures + 1,592 repos  
**Target:** $1M revenue via highest probability-adjusted path  
**Owner:** Autonomous Enterprise Loop (Agent + Human Approval Gates)  
**Generated:** 2026-08-05

---

## I. REALITY — What Actually Exists?

### Asset Inventory

```sql
-- Query 1-10: Asset classification
SELECT 
  asset_type,
  count(*) as count,
  avg(production_readiness) as avg_readiness,
  sum(annual_maintenance_cost) as total_cost
FROM asset_registry
WHERE asset_type IN ('software', 'tool', 'app', 'library', 'agent', 'model', 'dataset', 'infra', 'research')
GROUP BY asset_type
ORDER BY count DESC;

-- Follow-up: Which are duplicated?
SELECT 
  capability,
  count(distinct asset_id) as implementations,
  string_agg(asset_id, ', ') as repos
FROM asset_capabilities
GROUP BY capability
HAVING count(*) > 1
ORDER BY count DESC;

-- Follow-up: Which are abandoned?
SELECT 
  asset_id,
  last_commit,
  days_since_update,
  open_issues
FROM asset_registry
WHERE days_since_update > 180 AND open_issues > 0;

-- Follow-up: Which are commercial?
SELECT 
  asset_id,
  commercialization_path,
  potential_revenue_model,
  licenses_available
FROM asset_registry
WHERE commercialization_potential > 0.6;
```

### Capability Mapping

| Q# | Question | Source | Query | Threshold |
|----|----------|--------|-------|-----------|
| 1-10 | Asset inventory & classification | asset_registry | SQL above | — |
| 11 | What capabilities exist across all assets? | asset_capabilities + Neo4j | Graph traversal | — |
| 12 | Which capabilities are duplicated? | asset_capabilities | GROUP BY capability HAVING count > 1 | — |
| 13 | Which capabilities are missing? | capability_gap_analysis | LEFT JOIN ventures vs capabilities | Missing in >5% |
| 14 | Which assets are production-ready? | asset_registry.production_readiness | >= 0.8 | — |
| 15 | Which assets are abandoned? | asset_registry.days_since_update | > 180 days | — |
| 16 | Which assets are legally usable? | asset_registry.license | GPL/MIT/Apache/Commercial | — |
| 17-20 | Which can be combined/commercialized/white-labeled/become products? | venture_requirements × asset_capabilities | Cross-join + score | Score > 0.6 |

---

## II. MARKET — Where Is the Money?

### Market Sizing & Demand

```sql
-- Question 21-35: Market analysis
SELECT 
  sector,
  market_segment,
  market_size_usd,
  growth_rate_yoy,
  problem_urgency (1-10),
  problem_frequency_per_customer_year,
  price_willingness_usd,
  competition_fragmentation_score,
  customer_underserved_pct
FROM market_analysis
WHERE growth_rate_yoy > 0.15
  AND market_size_usd > 10000000
  AND problem_urgency >= 7
ORDER BY (market_size_usd * growth_rate_yoy * problem_urgency) DESC;

-- Question 36-40: Revenue potential
SELECT 
  market_segment,
  total_addressable_market,
  servable_addressable_market,
  servable_obtainable_market,
  revenue_potential_1m_horizon
FROM tam_sam_som
WHERE revenue_potential_1m_horizon >= 1000000
ORDER BY revenue_potential_1m_horizon DESC;
```

| Q# | Question | Data Source | Decision Rule |
|----|----------|-------------|---------------|
| 21 | What markets are growing? | market_analysis.growth_rate_yoy | > 15% YoY |
| 22 | Which markets have urgent problems? | market_analysis.problem_urgency | >= 7/10 |
| 23-25 | Which customers spend money & how much? | customer_spend.annual_spend | > $10K/year |
| 26 | What causes them NOT to buy? | customer_research.objections | Score each objection |
| 27-30 | Which markets have poor solutions / weak competition / controlled distribution / underserved customers? | competitive_analysis | Dispersion score, CAC analysis |
| 31-35 | Which problems are expensive/frequent/mandatory/worsening/tech-solvable? | problem_severity_analysis | Multiply: cost × frequency × inevitability |
| 36-40 | Which markets can support $10K+ sales → realistic $1M path? | tam_sam_som | SOM >= $1M in 12 months |

---

## III. CUSTOMER — Who Will Actually Pay?

### Customer Persona & Willingness

```sql
-- Question 41-60: Customer segmentation
SELECT 
  customer_segment,
  persona_id,
  problem_experience_level (1-10),
  budget_control_score,
  decision_urgency,
  switching_cost_current_solution,
  current_spend_annual,
  expansion_potential,
  referral_coefficient,
  sales_cycle_days,
  gross_margin_by_segment
FROM customer_analysis
WHERE decision_urgency >= 7 AND current_spend_annual > 5000
ORDER BY expansion_potential DESC;

-- Question 56-60: Best segment for first revenue
SELECT 
  segment,
  sales_cycle_days,
  gross_margin_pct,
  customer_lifetime_value,
  referral_likelihood,
  identifiable_customers_today
FROM segment_ranking
ORDER BY (sales_cycle_days DESC) 
       * (gross_margin_pct DESC) 
       * (customer_lifetime_value DESC) DESC;
```

| Q# | Question | Source | Scoring |
|----|----------|--------|---------|
| 41-45 | Ideal customer, pain experience, budget control, purchasing decision | customer_survey + sales_data | Decision authority score |
| 46-50 | Current solution, cost, problem cost, urgency, switching barriers | competitive_analysis + customer_interviews | Switching willingness |
| 51-55 | Purchase frequency, adjacent problems, referral sources, best segment | sales_history + market_data | Expansion multiplier |
| 56-60 | Shortest cycle, highest margin, highest LTV, greatest expansion, identifiable today | segment_analysis | Weighted: (1/cycle_days) × margin × LTV × expansion |

---

## IV. PRODUCT — What Are We Actually Selling?

### Capability-to-Product Mapping

```sql
-- Question 61-80: Product definition
SELECT 
  product_idea_id,
  exact_outcome_sold,
  required_capabilities,
  assets_that_provide_capabilities,
  existing_asset_reuse_pct,
  build_vs_reuse_recommendation,
  mvp_deliverable,
  msp_deliverable,
  fastest_value_demo,
  delivery_speed_24h,
  delivery_speed_7d,
  recurring_revenue_potential,
  packaging_model,
  licensing_model,
  resale_potential,
  whitelabel_readiness,
  platform_potential
FROM product_strategy
WHERE existing_asset_reuse_pct > 0.6
ORDER BY delivery_speed_24h ASC;
```

| Q# | Question | Source | Requirement |
|----|----------|--------|-------------|
| 61-63 | Exact outcome, capability, repository | customer_need × asset_capabilities | 1:1 match |
| 64-66 | What must be built vs reused vs automated | asset_inventory × product_spec | Reuse > 60% |
| 67-69 | What agents can operate, what needs humans, what never automates | operational_model | Agent + Human approval gates |
| 70-72 | MVP, MSP, fastest value demo | development_roadmap | 24-hour demo |
| 73-80 | 7-day delivery, recurring revenue, packaging, licensing, resale, white-label, platform | business_model | Repeatable |

---

## V. MONEY — How Does It Become $1M?

### Revenue Path Analysis

```sql
-- Question 81-95: Economic modeling
WITH paths AS (
  SELECT 
    'path_10x100k' AS model,
    10 AS customers,
    100000 AS unit_price,
    1000000 AS revenue
  UNION ALL
  SELECT 
    'path_100x10k',
    100,
    10000,
    1000000
  UNION ALL
  SELECT 
    'path_1000x1k',
    1000,
    1000,
    1000000
  UNION ALL
  SELECT 
    'path_10000x100',
    10000,
    100,
    1000000
)
SELECT 
  model,
  customers,
  unit_price,
  (SELECT avg(cac) FROM customer_acquisition) as cac,
  (SELECT avg(gross_margin_pct) FROM product_pricing) as margin_pct,
  (SELECT avg(delivery_cost) FROM operational_cost) as delivery_cost,
  (SELECT avg(ltv) FROM customer_lifetime) as ltv,
  customers * unit_price as gross_revenue,
  customers * (unit_price * (margin_pct / 100)) as gross_profit,
  customers * (SELECT avg(cac) FROM customer_acquisition) as acquisition_cost_total
FROM paths
ORDER BY acquisition_cost_total / gross_profit ASC;

-- Question 90-100: Fastest path to $1M
SELECT 
  opportunity_id,
  model_path,
  probability_success,
  months_to_1m,
  capital_required,
  probability_success * (1 / months_to_1m) * (1 / (capital_required / 100000)) as risk_adjusted_score,
  recommendation
FROM opportunity_modeling
ORDER BY risk_adjusted_score DESC
LIMIT 1;
```

| Q# | Question | Calculation |
|----|----------|-------------|
| 81-89 | Price, margin, CAC, delivery cost, LTV, payback, working capital | Revenue model |
| 90-95 | Customers needed, sales conversations, conversion rate, cost structure reduction | Path-specific math |
| 96-99 | Cross-sell, cross-venture, partner distribution, affiliate acquisition | Multiplier effects |
| 100 | **What should we do tomorrow with highest probability-adjusted path to cash?** | Rank all options |

---

## SECOND-ORDER THINKING LOOP

```
First Order: "Can we sell this?"
  ↓ Query: Does market demand exist? Is there budget?
  
Second Order: "Can we retain customers?"
  ↓ Query: What is churn? What creates stickiness?
  
Third Order: "What else can we sell them?"
  ↓ Query: What adjacent problems do customers have?
  
Fourth Order: "What distribution network develops?"
  ↓ Query: Which customers become advocates? Partners?
  
Fifth Order: "What additional businesses use that network?"
  ↓ Query: Can we white-label, resell, or partner?
  
Sixth Order: "What portfolio economics emerge?"
  ↓ Query: Cross-sell revenue? Affiliate upside? Strategic value?
```

---

## OPPORTUNITY SCORING ENGINE

Every opportunity produces:

```
MARKET_DEMAND           (0-100)
PAIN_SEVERITY           (0-100)
CUSTOMER_ABILITY_TO_PAY (0-100)
EXISTING_ASSET_FIT      (0-100)
MVP_SPEED               (0-100, inverted from days)
FIRST_SALE_SPEED        (0-100, inverted from days)
GROSS_MARGIN            (0-100)
RECURRING_REVENUE       (0-100)
DISTRIBUTION_POTENTIAL  (0-100)
CROSS_SELL_POTENTIAL    (0-100)
PARTNER_POTENTIAL       (0-100)
COMPETITIVE_MOAT        (0-100)
───────────────────────────────
EXECUTION_DIFFICULTY    (0-100, inverted for score)
CAPITAL_REQUIRED        (0-100, inverted for score)
REGULATORY_RISK         (0-100, inverted for score)
EVIDENCE_QUALITY        (0-100)
───────────────────────────────
COMPOSITE_SCORE         (0-100)
PROBABILITY_SUCCESS     (0-100)
EXPECTED_VALUE          ($)
```

**Composite = (Demand + Pain + Payability + AssetFit + Speed×3 + Margin + Recurring + Distribution + CrossSell + Partner + Moat) × (1 - ExecutionDifficulty/100) × (1 - Capital/100) × (1 - RegulatoryRisk/100) × EvidenceQuality/100**

---

## AUTONOMOUS LOOP IMPLEMENTATION

```
┌─────────────────────────────────────┐
│  DISCOVER (Run 100 Questions)       │
│  → asset_registry + market_analysis │
│  → Generate 50-100 opportunities    │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ CLASSIFY (Tag by type)              │
│ → Software product, Service, IP...  │
│ → Venture + Infrastructure          │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ EVALUATE (Score each)               │
│ → Opportunity Scoring Engine        │
│ → Rank by composite score           │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ PRIORITIZE (Top 20, then Top 5)     │
│ → Filter by probability > 50%       │
│ → Filter by capital < $50K          │
│ → Filter by time < 90 days          │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ TEST (Run cheap experiment)         │
│ → Design 7-day proof of concept     │
│ → Cost: < $5K                       │
│ → Metric: Can we sell it?           │
│  ║                                  │
│  ╠→ FAIL? Kill it. Learn.           │
│  ╚→ WIN? Proceed.                   │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ [HUMAN APPROVAL GATE #1]            │
│ → "Should we invest capital?"       │
│ → $5K → $50K decision              │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ SELL (Get first customer)           │
│ → Outreach, negotiation, contract   │
│ → Target: First $10K in 30 days     │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ [HUMAN APPROVAL GATE #2]            │
│ → "Did we deliver on promise?"      │
│ → Customer satisfaction > 80%?      │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ DELIVER (Operate)                   │
│ → Production infrastructure         │
│ → Customer success                  │
│ → Repeat for next 9 customers       │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ MEASURE (Data collection)           │
│ → Revenue actual vs forecast        │
│ → CAC, LTV, churn, margin           │
│ → Profitability threshold?          │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ LEARN (Update models)               │
│ → What assumptions were wrong?      │
│ → What capabilities are missing?    │
│ → What adjacent market appeared?    │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ COMPOUND (Design next experiments)  │
│ → 10 customers → 100 customers      │
│ → Cross-sell to existing base       │
│ → Leverage distribution             │
└──────────────┬──────────────────────┘
               │
               └─→ DISCOVER (repeat)
```

---

## HUMAN APPROVAL GATES

| Gate | Triggered When | Decision | Cost | Timeline |
|------|---|---|---|---|
| **Gate 1: Capital Allocation** | Test wins; experiment shows PMF | "Invest capital (> $5K)?" | $5K-$50K | 24 hours |
| **Gate 2: Customer Promise** | First customer live | "Deliver? Renew? Kill?" | Revenue commitment | 48 hours |
| **Gate 3: Production Scale** | 10 customers profitable | "Scale to 100?" | $50K-$500K | 1 week |
| **Gate 4: Venture Launch** | 100 customers, $50K MRR | "Incorporate legally?" | Governance | 2 weeks |
| **Gate 5: Portfolio Strategy** | 5 ventures at $50K+ MRR | "Consolidate? Spin off? Sell?" | Strategic | Monthly |

---

## INTEGRATION WITH AGENT-PLATFORM-OS

Agent-platform-os runs this loop. Humans gate consequential decisions.

```
Agent submits: 
  "Opportunity #47 (Medical Dispatch) scored 78/100.
   Probability: 65%. Capital: $20K. Time: 60 days.
   Recommend: Run test."

Human reviews:
  ✓ Approve test (cost: $5K, duration: 7 days)
  OR
  ✗ Reject + provide guidance

Agent executes test:
  → Reach out to 50 customers
  → Measure willingness to pay
  → Log results

Test completes:
  → Results: 6/50 interested, 3 willing to commit
  → Probability updated: 65% → 72%
  → Recommend: Proceed to Gate 1 (capital allocation)

Human reviews Gate 1:
  ✓ Allocate $20K
  OR
  ✗ Reject + suggest adjustment
```

---

**Status:** Framework complete. Awaiting Opportunity Scoring Engine deployment.
