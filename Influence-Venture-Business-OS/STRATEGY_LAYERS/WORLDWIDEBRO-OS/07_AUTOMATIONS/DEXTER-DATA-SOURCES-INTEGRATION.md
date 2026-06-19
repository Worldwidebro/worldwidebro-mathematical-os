# Dexter Financial Orchestrator — Data Sources Integration Guide

**Purpose:** Wire all data sources (Supabase, Ollama, awesome-quant libraries, market data APIs) into Dexter  
**Updated:** 2026-05-16 | Ready to install and configure  

---

## Core Data Sources Map

```
Venture Data (Supabase)
    ↓
Financial Metrics (CFO Agent)
    ↓
Portfolio Analysis (PyPortfolioOpt + Riskfolio-Lib)
    ├─ Forecasting (Prophet + ARCH + statsmodels)
    ├─ Risk Analysis (Riskfolio-Lib)
    └─ Optimization (PyPortfolioOpt)
    ↓
Backtesting (Backtrader)
    ↓
Visualization (mplfinance + plotly)
    ↓
Execution (Composio → Capital Moves)
```

---

## Part 1: Core Data Layers

### Layer 1A: Venture Data (Supabase) ✅ LIVE

**URL:** https://iefnvvfxbnpxfcggzljq.supabase.co  
**Status:** 687 ventures, ready for financial schema extension  
**What you have:**
- venture_id, name, sector, stage, revenue, cost, description
- 64 repos with embeddings for tech stack mapping
- aoc_tasks audit trail

**What you're adding (from guide):**
- burn_rate, runway_months, growth_rate, risk_profile, allocation_target
- venture_financials (monthly history)
- portfolio_metrics (aggregates)
- allocation_decisions (audit trail)

**Connection code:**
```python
import supabase
from supabase import create_client

SUPABASE_URL = "https://iefnvvfxbnpxfcggzljq.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
db = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get all ventures with financials
ventures = db.table("ventures").select("*").execute().data
financials = db.table("venture_financials").select("*").execute().data
```

---

### Layer 1B: Knowledge Graph (LightRAG + Supabase) ✅ LIVE

**URL:** Not applicable (local + Supabase sync)  
**Status:** 7000+ nodes, 6000+ edges  
**What it provides:**
- Entity relationships: venture → founders → sector → metrics
- Can query: "Which ventures share founders?" or "Tech stack overlap?"

**Connection code:**
```python
from lightrag_agent_queries import AgentQueryInterface

kg = AgentQueryInterface()
# Query: ventures in fintech sector with >50% YoY growth
high_growth_fintech = kg.query(
    "fintech ventures growth_rate > 50"
)
```

---

### Layer 1C: Reasoning Engine (Ollama) ✅ LIVE

**URL:** http://100.87.214.70:11434  
**Model:** qwen2.5:32b  
**Status:** Running 24/7

**Connection code:**
```python
import requests

OLLAMA_URL = "http://100.87.214.70:11434"

def reason_about_portfolio(prompt: str) -> str:
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": "qwen2.5:32b",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

# Example: CFO reasoning about capital moves
analysis = reason_about_portfolio(
    f"Given venture metrics: {venture_metrics}, "
    f"should we move capital from A to B? Why?"
)
```

---

## Part 2: Financial Analysis Libraries (awesome-quant)

### Install All Dependencies

```bash
# Core data manipulation
pip install pandas numpy scipy

# Portfolio optimization
pip install pypfopt riskfolio-lib

# Time series forecasting
pip install prophet statsmodels arch

# Backtesting
pip install backtrader  # OR zipline-reloaded

# Technical indicators (for venture metric trends)
pip install ta

# Visualization
pip install plotly mplfinance matplotlib

# Market data (optional, for public securities)
pip install yfinance

# Supabase client
pip install supabase python-dateutil

# All at once:
pip install pandas numpy scipy pypfopt riskfolio-lib prophet statsmodels arch backtrader ta plotly mplfinance matplotlib yfinance supabase python-dateutil
```

---

### 2A: Portfolio Optimization (PyPortfolioOpt)

**GitHub:** https://github.com/robertmartin8/PyPortfolioOpt  
**Docs:** https://pyportfolioopt.readthedocs.io/  
**Use Case:** Suggest optimal capital allocation across ventures

**Integration Code:**

```python
from pypfopt import EfficientFrontier, CLA, objective_functions
from pypfopt.discrete_allocation import DiscreteAllocation
import pandas as pd

class VenturePortfolioOptimizer:
    def __init__(self, ventures_df: pd.DataFrame):
        """
        ventures_df columns:
        - venture_id
        - current_allocation (current $)
        - expected_return (% YoY)
        - volatility (std_dev of returns, annualized)
        """
        self.ventures = ventures_df
        self.returns = ventures_df['expected_return'].values
        self.vols = ventures_df['volatility'].values
    
    def correlation_matrix(self) -> pd.DataFrame:
        """
        Estimate correlation between ventures
        (using sector similarity + founder network from LightRAG)
        """
        # Simple: ventures in same sector = 0.7 correlation
        # Different sector = 0.2 correlation
        sectors = self.ventures['sector'].values
        n = len(sectors)
        corr = pd.DataFrame(0.2, index=range(n), columns=range(n))
        for i in range(n):
            for j in range(n):
                if sectors[i] == sectors[j]:
                    corr.iloc[i, j] = 0.7
                if i == j:
                    corr.iloc[i, j] = 1.0
        return corr
    
    def covariance_matrix(self) -> pd.DataFrame:
        """Build covariance from volatility + correlation"""
        corr = self.correlation_matrix()
        cov = pd.DataFrame(
            index=self.ventures.index,
            columns=self.ventures.index
        )
        for i, v_i in enumerate(self.vols):
            for j, v_j in enumerate(self.vols):
                cov.iloc[i, j] = corr.iloc[i, j] * v_i * v_j
        return cov
    
    def optimize_max_sharpe(self, risk_free_rate=0.02):
        """Find allocation that maximizes Sharpe ratio"""
        cov = self.covariance_matrix()
        ef = EfficientFrontier(
            self.returns,
            cov,
            weight_bounds=(0.05, 0.5)  # 5%-50% per venture
        )
        ef.max_sharpe(risk_free_rate=risk_free_rate)
        weights = ef.clean_weights()
        perf = ef.portfolio_performance()
        
        return {
            'allocation': dict(zip(
                self.ventures['venture_id'],
                weights
            )),
            'expected_return': perf[0],
            'volatility': perf[1],
            'sharpe_ratio': perf[2]
        }
    
    def current_vs_optimal(self):
        """Show difference between current and optimal allocation"""
        optimal = self.optimize_max_sharpe()
        current = dict(zip(
            self.ventures['venture_id'],
            self.ventures['current_allocation']
        ))
        
        moves = {}
        for v_id in current:
            diff = optimal['allocation'][v_id] - (current[v_id] / sum(current.values()))
            if abs(diff) > 0.01:  # > 1% difference
                moves[v_id] = {
                    'current_pct': current[v_id] / sum(current.values()),
                    'optimal_pct': optimal['allocation'][v_id],
                    'move_amount': diff * sum(current.values())
                }
        
        return moves

# Usage
optimizer = VenturePortfolioOptimizer(ventures_df)
moves = optimizer.current_vs_optimal()
# Output: {"HRMS": {"current_pct": 0.4, "optimal_pct": 0.35, "move_amount": -50000}}
```

---

### 2B: Risk Analysis (Riskfolio-Lib)

**GitHub:** https://github.com/dcajasn/Riskfolio-Lib  
**Docs:** https://riskfolio-lib.readthedocs.io/  
**Use Case:** Advanced risk metrics (VaR, CVaR, Sharpe, Sortino)

```python
import riskfolio as rp
import pandas as pd

class VentureRiskAnalyzer:
    def __init__(self, returns_history: pd.DataFrame):
        """
        returns_history: DataFrame with venture returns by month
        Columns: venture_id, each row is monthly return %
        """
        self.returns = returns_history
    
    def value_at_risk(self, confidence=0.95):
        """What's the max portfolio loss at 95% confidence?"""
        portfolio = rp.Portfolio(returns=self.returns)
        portfolio.assets_stats(method_mu='hist', method_cov='hist')
        
        # Equal weight initially
        w = 1/len(self.returns.columns)
        weights = [w] * len(self.returns.columns)
        
        # Calculate VaR
        var = portfolio.Value_at_Risk(weights, confidence)
        return var
    
    def concentration_risk(self, weights: dict) -> float:
        """
        What % of portfolio is in top 3 ventures?
        Goal: < 60% (diversified)
        """
        sorted_weights = sorted(weights.values(), reverse=True)
        top_3_pct = sum(sorted_weights[:3])
        return top_3_pct
    
    def herfindahl_index(self, weights: dict) -> float:
        """
        Concentration metric: 0 = perfectly diversified, 1 = all in one
        """
        w_squared = [w**2 for w in weights.values()]
        return sum(w_squared)

# Usage
returns_df = db.table("venture_financials").select("venture_id, month, revenue_growth").execute().data
analyzer = VentureRiskAnalyzer(returns_df)
var_95 = analyzer.value_at_risk(confidence=0.95)
# "Portfolio has 5% chance of losing > $X in a month"
```

---

### 2C: Time Series Forecasting (Prophet + ARCH)

**Prophet GitHub:** https://github.com/facebook/prophet  
**ARCH GitHub:** https://github.com/bashtage/arch  
**Use Case:** Forecast venture revenue, burn rate, runway

```python
from prophet import Prophet
from arch import arch_model
import pandas as pd

class VentureForecaster:
    def __init__(self, venture_id: str, historical_data: pd.DataFrame):
        """
        historical_data: DataFrame with columns:
        - ds (date)
        - y (revenue or burn rate)
        """
        self.venture_id = venture_id
        self.data = historical_data
    
    def forecast_revenue(self, periods=12):
        """12-month revenue forecast"""
        model = Prophet(yearly_seasonality=True, daily_seasonality=False)
        model.fit(self.data)
        
        future = model.make_future_dataframe(periods=periods, freq='MS')
        forecast = model.predict(future)
        
        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods)
    
    def forecast_volatility(self, periods=12):
        """Estimate revenue volatility using ARCH"""
        returns = self.data['y'].pct_change().dropna()
        
        model = arch_model(returns, vol='Garch', p=1, q=1)
        res = model.fit(disp='off')
        
        # Forecast next 12 months volatility
        forecast = res.forecast(horizon=periods)
        return forecast.variance.values[-1]
    
    def runway_forecast(self, current_cash: float, monthly_burn: float):
        """
        Given current cash and monthly burn,
        when does cash run out?
        """
        burn_forecast = self.forecast_revenue(periods=12)
        cumsum_burn = burn_forecast['yhat'].cumsum()
        
        # Find when cumsum > current_cash
        for month, burn in enumerate(cumsum_burn):
            if burn > current_cash:
                return month  # Months until cash-out
        return 12  # Has runway > 1 year

# Usage
revenue_history = db.table("venture_financials")\
    .select("month, revenue")\
    .eq("venture_id", "hrms-001")\
    .order("month", desc=False)\
    .execute().data

forecaster = VentureForecaster("hrms-001", revenue_history)
revenue_forecast = forecaster.forecast_revenue(periods=12)
runway_months = forecaster.runway_forecast(cash=500000, monthly_burn=50000)
# Output: runway_months = 10 (will need capital injection in 10 months)
```

---

### 2D: Backtesting (Backtrader)

**GitHub:** https://github.com/backtrader/backtrader  
**Docs:** https://www.backtrader.com/  
**Use Case:** Test capital allocation strategies on historical data

```python
import backtrader as bt
import pandas as pd

class VentureAllocationStrategy(bt.Strategy):
    def __init__(self):
        self.rebalance_days = 30
        self.days_since_rebalance = 0
    
    def next(self):
        # Every 30 days, rebalance to optimal allocation
        self.days_since_rebalance += 1
        
        if self.days_since_rebalance >= self.rebalance_days:
            # Get optimal weights from PyPortfolioOpt
            optimal_weights = self.get_optimal_allocation()
            
            # Rebalance
            for i, weight in enumerate(optimal_weights):
                target_size = self.broker.getvalue() * weight
                self.order_target_value(self.data[i], target_size)
            
            self.days_since_rebalance = 0
    
    def get_optimal_allocation(self):
        """Call optimizer to get weights"""
        # In real code: query PyPortfolioOpt
        return [0.35, 0.30, 0.20, 0.15]  # Dummy weights

# Run backtest
cerebro = bt.Cerebro()
cerebro.addstrategy(VentureAllocationStrategy)

# Add venture data as "stocks"
for venture in ventures:
    data = bt.feeds.PandasData(
        dataname=venture['historical_prices']  # venture growth % as "price"
    )
    cerebro.adddata(data)

cerebro.broker.setcash(1000000)  # $1M starting capital
results = cerebro.run()

print(f"Final Portfolio Value: ${cerebro.broker.getvalue()}")
# "Starting: $1M, Ending: $1.35M (35% gain over backtest period)"
```

---

### 2E: Visualization (Plotly + mplfinance)

**Plotly Docs:** https://plotly.com/python/  
**mplfinance GitHub:** https://github.com/matplotlib/mplfinance  
**Use Case:** Real-time dashboard for portfolio health

```python
import plotly.graph_objects as go
import plotly.subplots as sp
from plotly.subplots import make_subplots

class DexterDashboard:
    def __init__(self, portfolio_metrics: dict):
        self.metrics = portfolio_metrics
    
    def create_dashboard(self):
        """Create 4-panel dashboard"""
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=(
                "Portfolio Value Trend",
                "Venture Allocation",
                "Runway by Venture",
                "Risk Metrics"
            )
        )
        
        # Panel 1: Portfolio value over time
        fig.add_trace(
            go.Scatter(
                x=self.metrics['dates'],
                y=self.metrics['portfolio_value'],
                mode='lines',
                name='Portfolio Value'
            ),
            row=1, col=1
        )
        
        # Panel 2: Pie chart of allocation
        fig.add_trace(
            go.Pie(
                labels=self.metrics['venture_names'],
                values=self.metrics['allocations'],
                name='Allocation'
            ),
            row=1, col=2
        )
        
        # Panel 3: Runway bar chart
        fig.add_trace(
            go.Bar(
                x=self.metrics['venture_names'],
                y=self.metrics['runway_months'],
                name='Runway (months)'
            ),
            row=2, col=1
        )
        
        # Panel 4: Risk heatmap
        fig.add_trace(
            go.Heatmap(
                z=self.metrics['risk_correlation'],
                name='Risk Correlation'
            ),
            row=2, col=2
        )
        
        fig.update_layout(height=800, showlegend=True)
        fig.write_html("dexter_dashboard.html")
        return fig

# Usage
dashboard = DexterDashboard(portfolio_metrics)
dashboard.create_dashboard()
# Opens dexter_dashboard.html in browser
```

---

## Part 3: Integration Wiring

### CFO Agent → Data Sources

```python
# FILE: agent_control_loop.py (extend existing FinancialAnalyst class)

from portfolio_optimizer import VenturePortfolioOptimizer
from venture_forecasting import VentureForecaster
from dexter_dashboard import DexterDashboard
import supabase

class FinancialAnalyst(Agent):
    """Extended CFO with portfolio capabilities"""
    
    def __init__(self, cfo_name="Dexter CFO"):
        super().__init__(cfo_name)
        self.db = supabase.create_client(
            "https://iefnvvfxbnpxfcggzljq.supabase.co",
            os.getenv("SUPABASE_KEY")
        )
        self.kg = AgentQueryInterface()
        self.ollama = OllamaReasoner("http://100.87.214.70:11434")
    
    def portfolio_health_check(self) -> dict:
        """Daily loop called by CEO"""
        # 1. Get all venture metrics from Supabase
        ventures = self.db.table("ventures").select("*").execute().data
        financials = self.db.table("venture_financials").select("*").execute().data
        
        # 2. Calculate per-venture metrics
        venture_metrics = {}
        for v in ventures:
            metrics = self._calculate_venture_metrics(v, financials)
            venture_metrics[v['id']] = metrics
        
        # 3. Portfolio-level analysis
        portfolio_roi = self._portfolio_roi(venture_metrics)
        concentration_risk = self._concentration_risk(venture_metrics)
        portfolio_runway = self._portfolio_runway(venture_metrics)
        
        # 4. Get optimization suggestions
        optimizer = VenturePortfolioOptimizer(ventures)
        rebalancing = optimizer.current_vs_optimal()
        
        # 5. Forecast 12 months out
        forecasts = {}
        for v_id in ventures:
            forecaster = VentureForecaster(v_id, financials)
            forecasts[v_id] = {
                'revenue_12m': forecaster.forecast_revenue(12),
                'runway': forecaster.runway_forecast(...)
            }
        
        # 6. Return complete picture for CEO decision-making
        return {
            'venture_metrics': venture_metrics,
            'portfolio_roi': portfolio_roi,
            'concentration_risk': concentration_risk,
            'portfolio_runway': portfolio_runway,
            'rebalancing_needed': rebalancing,
            'forecasts': forecasts,
            'timestamp': datetime.now()
        }
    
    def _calculate_venture_metrics(self, venture: dict, financials: list):
        """Existing logic - already in agent_control_loop.py"""
        # Calculate CAC, LTV, churn, margin, health_score
        # ...
        pass
    
    def _portfolio_roi(self, metrics: dict) -> float:
        """Aggregate ROI across all ventures"""
        total_allocation = sum([m['allocation'] for m in metrics.values()])
        total_roi = sum([m['roi'] * m['allocation'] for m in metrics.values()])
        return total_roi / total_allocation if total_allocation > 0 else 0
    
    def _concentration_risk(self, metrics: dict) -> float:
        """Top 3 ventures = what % of portfolio?"""
        allocations = sorted(
            [m['allocation'] for m in metrics.values()],
            reverse=True
        )
        return sum(allocations[:3]) / sum(allocations)
    
    def _portfolio_runway(self, metrics: dict) -> int:
        """Minimum runway across all ventures"""
        runways = [m['runway_months'] for m in metrics.values()]
        return min(runways) if runways else 0
```

---

## Part 4: Execution Flow (End-to-End)

```
1. CFO.portfolio_health_check() runs every 6 hours
   ↓
2. Collects data from:
   - Supabase (venture financials)
   - LightRAG (relationships, sector clustering)
   - Forecasting models (runway, growth)
   - Portfolio optimizer (rebalancing)
   ↓
3. Returns complete portfolio picture to CEO
   ↓
4. CEO decides: KILL, OPTIMIZE, SCALE, or COMPOUND
   ↓
5. If decision = "SCALE HRMS", CFO suggests:
   - Move $X from venture A to HRMS
   - Expected ROI impact: +Y%
   - Risk increase: Z%
   ↓
6. CEO approves → creates task in aoc_tasks
   ↓
7. Composio executes capital move in Supabase
   ↓
8. Audit trail logged to allocation_decisions table
   ↓
9. Dashboard updates in real-time
```

---

## Installation Checklist

- [ ] Run: `pip install pandas numpy scipy pypfopt riskfolio-lib prophet statsmodels arch backtrader ta plotly mplfinance matplotlib yfinance supabase python-dateutil`
- [ ] Verify Supabase connection: `python -c "import supabase; print('OK')"`
- [ ] Verify Ollama connection: `curl http://100.87.214.70:11434/api/tags`
- [ ] Verify LightRAG: `from lightrag_agent_queries import AgentQueryInterface`
- [ ] Create `portfolio_optimizer.py` (copy code from 2A above)
- [ ] Create `venture_forecasting.py` (copy code from 2C above)
- [ ] Create `dexter_dashboard.py` (copy code from 2E above)
- [ ] Extend `agent_control_loop.py` (copy CFO methods from Part 3)
- [ ] Test end-to-end: `python agent_control_loop.py`

---

## Quick Test (Run This First)

```bash
# Test all connections
python3 << 'EOF'
import os
import requests
import supabase
from lightrag_agent_queries import AgentQueryInterface

# 1. Supabase
db = supabase.create_client(
    "https://iefnvvfxbnpxfcggzljq.supabase.co",
    os.getenv("SUPABASE_KEY")
)
ventures = db.table("ventures").select("count").execute()
print(f"✓ Supabase: {ventures.data[0]['count']} ventures")

# 2. Ollama
ollama = requests.get("http://100.87.214.70:11434/api/tags").json()
print(f"✓ Ollama: {ollama['models'][0]['name']} model loaded")

# 3. LightRAG
kg = AgentQueryInterface()
entities = kg.query("ventures sector fintech")
print(f"✓ LightRAG: {len(entities)} entities found")

# 4. Libraries
import pypfopt, prophet, arch, backtrader
print("✓ All libraries imported successfully")

print("\n🟢 All systems ready for Dexter deployment!")
EOF
```

---

## URLs Reference Card

| Source | URL | Purpose |
|--------|-----|---------|
| **Supabase** | https://iefnvvfxbnpxfcggzljq.supabase.co | Venture data |
| **Ollama** | http://100.87.214.70:11434 | Reasoning engine |
| **PyPortfolioOpt** | https://github.com/robertmartin8/PyPortfolioOpt | Portfolio optimization |
| **Riskfolio-Lib** | https://github.com/dcajasn/Riskfolio-Lib | Risk analysis |
| **Prophet** | https://github.com/facebook/prophet | Revenue forecasting |
| **ARCH** | https://github.com/bashtage/arch | Volatility modeling |
| **Backtrader** | https://github.com/backtrader/backtrader | Strategy backtesting |
| **Plotly** | https://plotly.com/python/ | Dashboard visualization |

---

## Next Steps

1. **Install all libraries** (5 min): Run pip install command above
2. **Test connections** (5 min): Run quick test script
3. **Create portfolio_optimizer.py** (30 min): Copy code from 2A
4. **Create venture_forecasting.py** (30 min): Copy code from 2C
5. **Extend agent_control_loop.py** (1 hour): Add CFO portfolio methods
6. **Test end-to-end** (30 min): Run portfolio_health_check()
7. **Build dashboard** (2 hours): Copy code from 2E

**Total:** 5 hours to full integration

Ready to start?
