---
name: DEXTER-FINANCIAL-ORCHESTRATOR-GUIDE
title: Dexter Financial Orchestrator — Project Guide
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Dexter Financial Orchestrator — Project Guide

**Status:** Phase 0 (Framework Definition) | Ready to Execute  
**Owner:** Worldwidebro Holdings | Financial Systems  
**Built On:** agent_control_loop.py, LightRAG, Supabase, Ollama  
**Timeline:** 8 weeks from start → Live trading/capital moves  

---

## What You Already Have

### 1. **Agent Control Loop Foundation** ✓
- **File:** `agent_control_loop.py` (22K+ lines)
- **Authority Hierarchy:** CEO → CFO (metrics) → CTO (execution) → Sector PMs
- **CFO Already Calculates:** CAC, LTV, churn, margin, burn, health score, survival metrics
- **Decision Types:** KILL, OPTIMIZE, SCALE, COMPOUND
- **Execution via:** Composio tasks → aoc_tasks audit trail

**What you DON'T need to rebuild:** The decision hierarchy, the audit system, or the agent orchestration. You only extend CFO capabilities.

### 2. **Data Infrastructure** ✓
- **Supabase:** 687 ventures with revenue, cost, sector, description, stage
- **aoc_tasks table:** Work queue with status, assigned_agent, payload, result
- **LightRAG:** 7000+ nodes, 6000+ edges (ventures, founders, sectors, metrics relationships)
- **Ollama:** qwen2.5:32b reasoning engine running at 100.87.214.70:11434

**What you DON'T need to rebuild:** The database, task queue, or knowledge graph. Dexter will read from them.

### 3. **Financial Data Model** (Partial)
- **Ventures table columns:** venture_id, revenue, cost, sector, stage, market_size
- **Missing for portfolio level:** venture_type, growth_rate, burn_rate, runway_months, cash_position, allocation_target, risk_profile

---

## Scope: Building Dexter

### Phase 1: Data Model Extension (Week 1 — 2 days)

**What to add to Supabase:**

```sql
-- 1. Extend ventures table
ALTER TABLE ventures ADD COLUMN (
  burn_rate NUMERIC,         -- monthly cash burn
  runway_months INT,         -- months until cash-out
  growth_rate NUMERIC,       -- YoY revenue growth %
  risk_profile VARCHAR,      -- LOW, MEDIUM, HIGH
  allocation_target NUMERIC  -- $ assigned from portfolio
);

-- 2. Create portfolio_metrics table
CREATE TABLE portfolio_metrics (
  id UUID PRIMARY KEY,
  metric_date DATE,
  total_capital NUMERIC,
  allocated_capital NUMERIC,
  liquid_cash NUMERIC,
  total_portfolio_roi NUMERIC,
  avg_health_score INT,
  concentration_risk NUMERIC,
  portfolio_runway_months INT,
  venture_count INT
);

-- 3. Create venture_financials (historical)
CREATE TABLE venture_financials (
  id UUID PRIMARY KEY,
  venture_id UUID REFERENCES ventures(id),
  month DATE,
  revenue NUMERIC,
  cost NUMERIC,
  cac NUMERIC,
  ltv NUMERIC,
  churn NUMERIC,
  margin NUMERIC,
  recorded_at TIMESTAMP
);

-- 4. Create allocation_decisions (audit trail for Dexter)
CREATE TABLE allocation_decisions (
  id UUID PRIMARY KEY,
  decision_timestamp TIMESTAMP,
  venture_id UUID,
  old_allocation NUMERIC,
  new_allocation NUMERIC,
  reasoning TEXT,
  triggered_by VARCHAR,  -- e.g., "low_runway", "high_roi", "rebalance"
  status VARCHAR         -- PROPOSED, EXECUTED, REJECTED
);
```

**Reuse:** All metrics already calculated by CFO agent — just persist them to venture_financials.

---

### Phase 2: Extend CFO Agent (Week 1-2 — 3 days)

**What to add to agent_control_loop.py:**

```python
class FinancialAnalyst(Agent):
    """Extended CFO with portfolio capabilities"""
    
    # EXISTING (keep as-is)
    - calculate_venture_metrics(venture_id)  # per-venture: CAC, LTV, churn, etc.
    - health_score(venture_id)
    - survival_metric(venture_id)
    
    # NEW: Portfolio-level
    - portfolio_roi()                    # sum all ventures' ROI weighted by allocation
    - portfolio_runway()                 # min runway across all ventures
    - capital_concentration_risk()       # % in top 3 ventures
    - allocation_optimization()          # use PyPortfolioOpt to suggest rebalance
    - venture_forecast(venture_id, months)  # Prophet/ARCH model for revenue/burn
    - rebalancing_signals()              # which ventures need capital shift?
    - scenario_analysis(capital_increase, capital_decrease)  # "what if" modeling
    
    def portfolio_health_check(self):
        """Daily loop - called by CEO"""
        return {
            "total_capital": self.portfolio_roi(),
            "runway_months": self.portfolio_runway(),
            "concentration_risk": self.capital_concentration_risk(),
            "low_runway_ventures": self._ventures_under_6mo(),
            "high_roi_ventures": self._ventures_over_50pct_roi(),
            "rebalancing_needed": self.rebalancing_signals()
        }
```

**Reuse:** All venture-level metrics already exist. Copy/paste the financial calculation logic, add portfolio aggregation.

---

### Phase 3: Portfolio Optimization Engine (Week 2-3 — 4 days)

**Build separately, wire to CFO:**

```python
# NEW FILE: portfolio_optimizer.py

from pypfopt import EfficientFrontier, portfolio_performance
from riskfolio import Portfolio
import numpy as np, pandas as pd

class PortfolioOptimizer:
    """Rebalancing suggestions for venture portfolio"""
    
    def __init__(self, ventures_data: pd.DataFrame):
        # ventures_data columns: 
        # venture_id, current_allocation, expected_return, risk (std_dev)
        self.ventures = ventures_data
    
    def efficient_frontier(self):
        """Given expected returns & risk, find optimal allocation"""
        returns = self.ventures['expected_return'].values
        cov_matrix = self._estimate_covariance()
        ef = EfficientFrontier(returns, cov_matrix)
        weights = ef.maximum_sharpe_ratio()
        return dict(zip(self.ventures.venture_id, weights))
    
    def rebalancing_recommendation(self):
        """Current allocation vs optimal → what to move"""
        current = dict(zip(self.ventures.venture_id, 
                          self.ventures['current_allocation']))
        optimal = self.efficient_frontier()
        moves = {v: optimal[v] - current[v] 
                for v in current.keys()}
        return {v: m for v, m in moves.items() if abs(m) > 0.01}
    
    def scenario_test(self, new_capital: float, scenario_name: str):
        """Backtest: if we add $X, how does portfolio health change?"""
        # Copy current + add capital
        # Rebalance
        # Return new metrics vs current
        pass
```

**Reuse:** PyPortfolioOpt is a package — no reimplementation needed. Just wire returns & risk data from CFO.

---

### Phase 4: Financial Dashboard/Terminal (Week 3-4 — 5 days)

**Option A: OpenBB Terminal (Lightweight)**
```bash
pip install openbb
# Create custom bundle in ~/.openbb/app/models/
# Extend with venture data feeds
```

**Option B: Custom Dashboard (Jupyter + Plotly)**
```python
# NEW FILE: dexter_dashboard.py
# Uses Supabase → portfolio_metrics → plotly charts
# Real-time venture P&L, runway, cash position
```

**Option C: Integrated into Paperclip**
- Paperclip already has org dashboards
- Wire Dexter metrics into Paperclip UI
- Single pane of glass

**Recommendation:** Start with **Option B** (Jupyter + custom) → wire to OpenBB for live trading terminal later.

---

### Phase 5: Trading Terminal Setup (Week 4-5 — 6 days)

**OpenBB vs Alternatives:**

| Tool | Venture Capital | Securities/Crypto | Setup | Notes |
|------|-----------------|-------------------|-------|-------|
| **OpenBB** | Limited | Excellent | 15 min | Free, extensible |
| **QuantConnect** | Limited | Excellent | 1 hour | Web-based, backtesting |
| **Alpaca** | Limited | Good | 30 min | API-first, good docs |
| **Custom (Backtrader)** | Native | Good | 2 days | Max flexibility |

**Build Dexter Terminal:**
```python
# NEW FILE: dexter_terminal.py
# Combines:
# 1. Portfolio dashboard (venture metrics)
# 2. Capital allocation controls (move $ between ventures)
# 3. Backtesting (test scenarios before executing)
# 4. Live execution hooks (trigger capital moves)
# 5. Risk monitoring (low runway alerts, concentration warnings)

class DexterTerminal:
    def __init__(self, cfo_agent: FinancialAnalyst):
        self.cfo = cfo_agent
        self.rebalancer = PortfolioOptimizer(...)
    
    def show_portfolio(self):
        """Current state: all ventures + metrics"""
        # Calls CFO.portfolio_health_check()
        # Renders in terminal or web UI
    
    def propose_rebalance(self):
        """Show CFO's suggested allocation changes"""
        # Calls rebalancer.rebalancing_recommendation()
        # Shows impact on portfolio metrics
    
    def execute_move(self, from_venture, to_venture, amount):
        """Execute capital move in Supabase + audit trail"""
        # Updates allocation_decisions table
        # Triggers CFO to recalculate
        # Sends alert if risks triggered
    
    def backtest_scenario(self, scenario_name, capital_add_or_remove):
        """Test: what if we add/remove $X?"""
        # Calls CFO.scenario_analysis()
        # Simulates for N months
        # Returns projected metrics
```

**Reuse:** All core logic is in CFO agent. Terminal is a UI wrapper.

---

## Weekly Timeline (8 weeks)

| Week | Phase | Deliverables | Status |
|------|-------|--------------|--------|
| 1 | **Data + CFO extension** | Supabase schema + portfolio metrics in agent_control_loop.py | Ready now |
| 2 | **Portfolio optimizer** | PyPortfolioOpt wired to CFO | Parallel |
| 3 | **Forecasting** | Prophet/ARCH models for venture growth/burn | Parallel |
| 4 | **Dashboard** | Jupyter notebook or Paperclip integration | Parallel |
| 5 | **Terminal setup** | OpenBB instance with venture feeds | Sequential |
| 6 | **Backtesting** | Scenario testing framework | Parallel |
| 7 | **Execution layer** | Capital move triggers + alerts | Sequential |
| 8 | **Live testing** | Run 2 weeks of backtest → go live | Sequential |

---

## Architecture: What Connects Where

```
Supabase (ventures, financials, decisions)
    ↓
LightRAG Knowledge Graph (entity relationships)
    ↓
CFO Agent (in agent_control_loop.py)
    ├─ Calculate venture metrics
    ├─ Portfolio health check
    └─ Call PortfolioOptimizer for suggestions
    ↓
PortfolioOptimizer (PyPortfolioOpt)
    └─ Suggest rebalancing
    ↓
DexterTerminal (UI)
    ├─ Show portfolio state
    ├─ Propose moves
    ├─ Backtest scenarios
    └─ Execute capital moves
    ↓
Composio Tasks (execute trades, send alerts)
    ↓
aoc_tasks audit trail (every decision logged)
```

---

## What You DON'T Need to Build

1. **Decision hierarchy** — CEO/CFO/CTO already exist
2. **Task queuing** — aoc_tasks already handles it
3. **Data storage** — Supabase already live
4. **Knowledge graph** — LightRAG already indexed
5. **Reasoning engine** — Ollama already running
6. **Execution framework** — Composio already hooked
7. **Audit trail** — Already in place
8. **Agent autonomy** — Already implemented

---

## What You Need to Build

1. **Supabase schema extension** (2 hours) — 4 new tables
2. **CFO portfolio methods** (3 hours) — extend existing class
3. **PortfolioOptimizer class** (4 hours) — PyPortfolioOpt wrapper
4. **Forecasting models** (4 hours) — Prophet + ARCH
5. **DexterTerminal UI** (6 hours) — dashboard + controls
6. **Backtesting framework** (4 hours) — scenario testing
7. **Execution hooks** (3 hours) — wire capital moves to Composio
8. **Testing & tuning** (1 week) — live backtest

**Total: ~40 hours of actual coding**

---

## Files to Create/Modify

**Modify:**
- `agent_control_loop.py` — Add CFO portfolio methods

**Create:**
- `supabase_migrations/004_dexter_financial_schema.sql` — Schema extension
- `portfolio_optimizer.py` — PyPortfolioOpt wrapper
- `venture_forecasting.py` — Prophet + ARCH models
- `dexter_terminal.py` — UI + controls
- `dexter_backtester.py` — Scenario testing
- `dexter_executor.py` — Capital move execution
- `dexter_dashboard.py` — Web UI (Jupyter or Plotly)

---

## Dependencies to Install

```bash
pip install pypfopt riskfolio-lib pandas numpy scipy statsmodels prophet arch yfinance plotly jupyter
```

**Total:** 11 packages, all open-source, zero proprietary costs.

---

## Success Criteria

- [ ] Portfolio metrics visible in real-time (CFO health check output)
- [ ] Capital allocation suggestions generated by optimizer
- [ ] Backtesting shows 2 weeks of simulated decisions
- [ ] Zero uncaught errors in execution
- [ ] All decisions audit-logged in aoc_tasks
- [ ] Terminal shows live venture P&L + runway
- [ ] Test 1 real capital move (small amount) → audit trail confirms

---

## Next Steps (Start Tomorrow)

1. **Week 1:** Run the Supabase migration + add CFO methods (2 days)
2. **Week 1:** Build PortfolioOptimizer (1 day) 
3. **Week 1:** Test with mock data (1 day)
4. **Week 2:** Add forecasting (2 days)
5. **Week 2:** Build terminal + backtest (3 days)

**Parallel:** Can start terminal UI while optimizer is being built.

---

## Questions Before You Start

1. **Venture data completeness:** Do all 687 ventures have revenue/cost/stage data, or just top 50?
2. **Capital sources:** Where does capital come from? (Your wallet, investors, venture revenue?)
3. **Risk tolerance:** What's acceptable portfolio concentration in one venture? (e.g., max 30% in HRMS?)
4. **Execution frequency:** Rebalance daily? Weekly? Monthly?
5. **Real trading:** Start with simulated (backtest only) or run live capital moves immediately?

---

## Green Light? 

If this looks right, start with:
```bash
# 1. Run Supabase migration
supabase migration new dexter_financial_schema

# 2. Extend agent_control_loop.py with CFO portfolio methods
# 3. Build portfolio_optimizer.py
# 4. Create dexter_terminal.py stub
# 5. Wire up a simple dashboard

python3 dexter_terminal.py  # Start here
```

Ready to execute?
