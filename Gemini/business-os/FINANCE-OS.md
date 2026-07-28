# Finance OS: Capital Allocation & Financial Intelligence

This document defines the architecture, data models, and agent capabilities of the **Finance OS (Dexter)** within **Worldwidebro Holdings**.

---

## 1. Capital Hierarchy & Monetization Layers

The Finance OS manages treasury operations and aggregates yield across four corporate capital layers:

```text
                               WinnersCircleWCLLC (Capital Pool)
                                              │
            ┌──────────────────────┬──────────┴──────────┬──────────────────────┐
            ▼                      ▼                     ▼                      ▼
    [ Layer 1: Labor ]     [ Layer 2: SaaS ]     [ Layer 3: Services ]  [ Layer 4: Equity ]
     STA commissions &      Digital products,     Acquisitions of        Deal spread & carry
     labor markups (30-40%) courses, subscriptions. brick-and-mortar firms. on exits (15-20%).
```

We minimize infrastructure expenditures by enforcing a strict **open-source first** policy: all databases (Postgres, Neo4j, Qdrant), route gateways (LiteLLM), models (Ollama), and software cores (MedusaJS) are hosted locally or on self-managed infrastructure. We can always find a solution that doesn't cost.

---

## 2. Database Schema Extensions

To track consolidated portfolio ROI and run capital rebalancing optimizations, the transactional database implements the following tables:

```sql
-- 1. portfolio_metrics (Daily snapshots of consolidated holdings)
CREATE TABLE portfolio_metrics (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  metric_date DATE NOT NULL,
  total_capital NUMERIC(15,2),
  allocated_capital NUMERIC(15,2),
  liquid_cash NUMERIC(15,2),
  total_portfolio_roi NUMERIC(5,2),
  avg_health_score INT,
  concentration_risk NUMERIC(5,2),
  portfolio_runway_months INT,
  venture_count INT
);

-- 2. venture_financials (Historical monthly metrics per venture)
CREATE TABLE venture_financials (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id UUID REFERENCES ventures(id),
  month DATE NOT NULL,
  revenue NUMERIC(12,2) NOT NULL,
  cost NUMERIC(12,2) NOT NULL,
  cac NUMERIC(10,2),
  ltv NUMERIC(10,2),
  churn NUMERIC(5,2),
  margin NUMERIC(5,2),
  recorded_at TIMESTAMP DEFAULT NOW()
);

-- 3. allocation_decisions (Fiduciary audit trail of Dexter's moves)
CREATE TABLE allocation_decisions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  decision_timestamp TIMESTAMP DEFAULT NOW(),
  venture_id UUID,
  old_allocation NUMERIC(12,2),
  new_allocation NUMERIC(12,2),
  reasoning TEXT,
  triggered_by VARCHAR(50), -- e.g., "low_runway", "high_roi", "rebalance"
  status VARCHAR(20)        -- PROPOSED, EXECUTED, REJECTED
);
```

---

## 3. CFO Agent Portfolio Capabilities

The CFO Agent (**Dexter**) extends `agent_control_loop.py` to calculate portfolio health and output allocation signals:

```python
class FinancialAnalyst(Agent):
    """Extended CFO with portfolio management capabilities"""

    def portfolio_roi(self):
        """Sum of all ventures' ROI weighted by capital allocation"""
        pass

    def portfolio_runway(self):
        """Calculates the minimum runway in months across active ventures"""
        pass

    def capital_concentration_risk(self):
        """Measures portfolio risk concentration in top 3 ventures"""
        pass

    def allocation_optimization(self):
        """Uses PyPortfolioOpt to suggest optimal capital distributions"""
        pass

    def portfolio_health_check(self):
        """Runs daily loop reporting metrics to Hermes and the human principal"""
        return {
            "total_capital_roi": self.portfolio_roi(),
            "runway_months": self.portfolio_runway(),
            "concentration_risk": self.capital_concentration_risk(),
            "rebalancing_needed": self.allocation_optimization()
        }
```

---

## 4. Integration Triggers & Protections

1. **Invoicing Triggers**:
   - **STA Matches**: Triggered when a contractor is placed. The Staffing Placement Agent invokes `CFO.generate_invoice` to bill the client.
   - **CON Milestones**: Triggered when the Project Manager logs a milestone as `completed`. The Construction Agent invokes the billing loop.
2. **Runaway Cost circuit breaker**:
   - If an agent pipeline exceeds **$5.00** in API expenses within a single hour, the loop is frozen, and an alert is sent.

---

## 5. Treasury Status & Deficit Recovery Plan

### Current Cash Outflow
- **Subscriptions**: $20.00/mo (Antigravity IDE) + $20.00/mo (Claude Pro) = **$40.00/mo total overhead**.
- **Current Income**: **$0.00/mo (Pre-revenue)**.
- **Runway Status**: Burning $40.00/mo with zero margin capture.

### Immediate Action Plan (Monday Launch Target)
To clear this deficit and reach cash-flow neutrality immediately, the system initiates the **Wave 1 Labor Dispatch Loop**:
1. **CON-001 Electrician Handoff**: Post the 5 contractor roles on Monday morning (bypassing expensive external listing channels by scraping local CDL/General Contractor databases).
2. **STA-001 Placement**: Match and deploy the first electrician at a base rate of $25/hr.
3. **Margin Arbitrage**: STA-001 invoices CON-001 at a **30% markup** ($32.50/hr), capturing a **$7.50/hr margin** ($60/day profit).
4. **Deficit Clearance**: A single 8-hour placement captures **$60.00 in margin**, clearing the entire monthly subscription overhead ($40.00) in **less than 6 hours of operation**.
