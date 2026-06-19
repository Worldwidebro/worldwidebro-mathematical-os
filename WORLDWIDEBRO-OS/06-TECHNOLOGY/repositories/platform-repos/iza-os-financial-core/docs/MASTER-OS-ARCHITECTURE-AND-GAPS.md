# 🧠 MASTER OS ARCHITECTURE + GAPS + INSTALL ORDER

**Date:** 2026-06-06  
**Total System Size:** ~70-75 components  
**Current Completion:** ~78-82%  
**Gap to 100%:** ~18-22% (missing orchestration + integration layers)

---

# 🏗️ SECTION 1: FULL SYSTEM ARCHITECTURE DIAGRAM

## COMPLETE LAYER VIEW (All 70 Components)

```
╔════════════════════════════════════════════════════════════════════════════════╗
║                   🧠 CIVILIZATION OS TRADING ARCHITECTURE                      ║
║                            (MASTER BLUEPRINT)                                  ║
╚════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 0: DATA FEEDS & MARKET INPUT                                             │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  yfinance (equities)  ─┐                                                        │
│  finnhub (fundamentals)├─→ OpenBB Platform (data aggregation hub)               │
│  twelvedata (series)   ─┘         │                                            │
│                                   ├─→ Time-Series Database (OHLCV storage)     │
│  Forex Factory (news) ─→ News Filter Engine                                    │
│  TradingView (charts) ─→ Chart + Signal Layer                                  │
│                                                                                 │
│  CCXT (40+ crypto exchanges) → Crypto Market Data Feed                         │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 1: INTELLIGENCE BRAIN (IZA OS + FIN REPOS)                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─ IZA-Bot-Intelligence (CORE DECISION ENGINE)                                │
│  │   Inputs:                                                                   │
│  │   ├─ TradingView signals (ORB, reversals, liquidity)                        │
│  │   ├─ OpenBB market data                                                     │
│  │   ├─ Forex Factory macro context                                            │
│  │   ├─ fin-023 (Portfolio scoring)                                            │
│  │   ├─ fin-026 (Compliance gates)                                             │
│  │   ├─ Genixbank (Capital available?)                                         │
│  │   └─ ORB Strategy rules + Order Flow analysis                               │
│  │                                                                             │
│  │   Decision Output: BUY / SELL / SKIP TRADE                                  │
│  │                                                                             │
│  │   (Powered by 15 IZA sub-bots: forecasting, optimization, synthesis, etc.) │
│  │                                                                             │
│  └─→ ROUTE TO EXECUTION (MT5 OR Tradeovate OR Alpaca OR CCXT)                  │
│                                                                                 │
│  Supporting Intelligences:                                                      │
│  ├─ IZA-Bot-Forecasting (market predictions)                                   │
│  ├─ IZA-Bot-Optimization (strategy weighting)                                  │
│  ├─ IZA-Bot-Discovery (pattern recognition)                                    │
│  ├─ IZA-Bot-Synthesis (result aggregation)                                     │
│  ├─ IZA-Bot-Analytics (metrics + KPIs)                                         │
│  └─ IZA-Bot-Intelligence (final decision)                                      │
│                                                                                 │
│  Financial Core (Approval Gates):                                              │
│  ├─ fin-023-investment-portfolio-ai (strategy scoring 1-100)                   │
│  ├─ fin-026-financial-compliance-scanner (legal gate)                          │
│  ├─ fin-004-genixbanks-ai-treasurer (capital allocation check)                 │
│  └─ genixbank-financial-system (capital ledger)                                │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 2: ORCHESTRATION & ROUTING (n8n + MCP)                                   │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─ n8n Workflow Engine (SIGNAL ROUTER)                                        │
│  │  ├─ TradingView Webhook Listener (ORB signals)                              │
│  │  ├─ Route signal → IZA-Bot-Intelligence                                     │
│  │  ├─ Wait for decision response                                              │
│  │  ├─ If TRADE: Forward to Execution Layer                                    │
│  │  ├─ If SKIP: Log and wait for next signal                                   │
│  │  └─ If ERROR: Alert IZA-Bot-Alerting                                        │
│  │                                                                             │
│  └─ MCP Server (Agent Communication Protocol)                                  │
│     ├─ IZA bots talk to each other via MCP                                     │
│     ├─ Pass decision scores + confidence levels                                │
│     ├─ Route approvals/rejections                                              │
│     └─ Enable multi-bot consensus                                              │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 3: EXECUTION (BROKERS + PLATFORMS)                                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  IZA-Bot-Intelligence routes to:                                               │
│                                                                                 │
│  ┌─ MetaTrader 5 (MT5) [FX/CFD]                                                │
│  │  ├─ Alpaca (stocks/options) [Backup MT5 path]                               │
│  │  └─ Executes trade → returns fill + price                                   │
│  │                                                                             │
│  ├─ Tradeovate (Futures: NQ, ES, YM, etc.)                                     │
│  │  └─ Executes order → returns position info                                  │
│  │                                                                             │
│  ├─ Alpaca Brokerage (Stocks/ETFs/Options)                                     │
│  │  └─ Executes → returns fill data                                            │
│  │                                                                             │
│  └─ CCXT (40+ crypto exchanges)                                                │
│     └─ Executes crypto trade → returns position                                │
│                                                                                 │
│  [Optional Copy Trading Layer]                                                 │
│  ├─ Copygram (copy signal replication)                                         │
│  └─ Kinnobot (copy trading automation)                                         │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 4: TRADE MANAGEMENT & JOURNALING                                         │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─ IZA-Bot-Management                                                         │
│  │  ├─ Trailing stop logic                                                     │
│  │  ├─ Partial exit signals                                                    │
│  │  ├─ Breakeven adjustment                                                    │
│  │  └─ Time-based exits                                                        │
│  │                                                                             │
│  └─ IZA-Bot-Reporting (JOURNAL ENGINE)                                         │
│     ├─ Log every trade: entry, exit, P&L, reason                               │
│     ├─ Store in Time-Series Database                                           │
│     ├─ Send to fin-031 (Dashboard display)                                     │
│     ├─ Send to fin-004 (Allocation rebalance)                                  │
│     └─ Send to fin-023 (Portfolio update)                                      │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 5: PORTFOLIO OPTIMIZATION & CAPITAL MANAGEMENT                           │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─ fin-023-investment-portfolio-ai (PORTFOLIO AI)                             │
│  │  ├─ Receives trade journal from reporting bot                               │
│  │  ├─ Recalculates portfolio metrics                                          │
│  │  ├─ Updates strategy effectiveness scores                                   │
│  │  └─ Sends updated data to fin-031 (dashboards)                              │
│  │                                                                             │
│  └─ fin-004-genixbanks-ai-treasurer (CAPITAL ALLOCATOR)                        │
│     ├─ Receives P&L from reporting bot                                         │
│     ├─ Updates capital ledger in Genixbank                                     │
│     ├─ Rebalances allocation across ventures (if multi-trading)                │
│     └─ Sends constraints back to IZA-Bot-Intelligence                          │
│                                                                                 │
│  └─ Genixbank-Financial-System (CAPITAL LEDGER)                                │
│     ├─ Stores all capital transactions                                         │
│     ├─ Tracks available buying power                                           │
│     ├─ Updates in real-time as trades execute                                  │
│     └─ Sends capital checks to Intelligence bot                                │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 6: RISK MANAGEMENT & KILL SWITCH                                         │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─ fin-026-financial-compliance-scanner (RISK GATE #1)                        │
│  │  ├─ Pre-execution compliance checks                                         │
│  │  ├─ AML/KYC validation                                                      │
│  │  ├─ Regulatory rule enforcement                                             │
│  │  └─ Returns APPROVED / REJECTED                                             │
│  │                                                                             │
│  ├─ Risk Kernel (PORTFOLIO RISK ENGINE) ❌ MISSING                             │
│  │  ├─ VAR (Value at Risk) calculation                                         │
│  │  ├─ Leverage limits enforcement                                             │
│  │  ├─ Max drawdown tracking                                                   │
│  │  └─ HARD STOP if limits breached                                            │
│  │                                                                             │
│  └─ IZA-Bot-Alerting (NOTIFICATION SYSTEM)                                     │
│     ├─ Real-time trade alerts                                                  │
│     ├─ Risk threshold warnings                                                 │
│     ├─ System health status                                                    │
│     └─ Sends to user + dashboard                                               │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 7: ANALYTICS & LEARNING                                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─ IZA-Bot-Analytics (METRICS ENGINE)                                         │
│  │  ├─ Win rate tracking                                                       │
│  │  ├─ Sharpe ratio calculation                                                │
│  │  ├─ Drawdown analysis                                                       │
│  │  ├─ Strategy performance scoring                                            │
│  │  └─ Session-by-session rankings                                             │
│  │                                                                             │
│  ├─ IZA-Bot-Optimization (LEARNING ENGINE)                                     │
│  │  ├─ A/B test strategy variations                                            │
│  │  ├─ Weights trades based on success rate                                    │
│  │  ├─ Adjusts entry/exit rules dynamically                                    │
│  │  └─ Updates ORB thresholds based on win rate                                │
│  │                                                                             │
│  └─ fin-031-investor-dashboard-builder (REPORTING UI)                          │
│     ├─ Live P&L display                                                        │
│     ├─ Trade history + journal                                                 │
│     ├─ Performance charts                                                      │
│     ├─ Risk metrics dashboard                                                  │
│     └─ Accessible at: localhost:3000 (or cloud)                                │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 8: OPTIONAL INTELLIGENCE SYSTEMS                                         │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  [Can be integrated for advanced analysis]                                     │
│                                                                                 │
│  ├─ Chroma (semantic search, port 9022)                                        │
│  │  └─ General semantic search for market data                                 │
│  │                                                                             │
│  ├─ TurboVec (fast vector search - Rust + Python, 5.5K stars) ✅              │
│  │  └─ Find similar trading patterns historically                              │
│  │  └─ SIMD acceleration (AVX512/NEON) for fast pattern matching               │
│  │                                                                             │
│  ├─ Microsoft Qlib (backtesting + factor research)                             │
│  │  └─ Historical strategy validation                                          │
│  │                                                                             │
│  ├─ TradingAgents / ai-hedge-fund (multi-agent alternatives)                  │
│  │  └─ Secondary decision sources (for consensus)                              │
│  │                                                                             │
│  ├─ Nautilus Trader (alternative execution engine)                             │
│  │  └─ Fallback routing if brokers unavailable                                 │
│  │                                                                             │
│  └─ QuantMuse / Kronos (advanced analytics)                                    │
│     └─ Market microstructure analysis                                          │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ LAYER 9: OTHER FIN VENTURES (35 Repos)                                         │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  Parallel income streams + capital sources:                                    │
│  ├─ fin-001 (Genixbank Lite)                                                   │
│  ├─ fin-002 (Credit repair)                                                    │
│  ├─ fin-006 (Tax prep)                                                         │
│  ├─ fin-011 (Bookkeeping)                                                      │
│  ├─ ... (30+ more ventures)                                                    │
│  │                                                                             │
│  └─ Each feeds revenue → Genixbank → Available capital for trading              │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ INFRASTRUCTURE FOUNDATION                                                      │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ├─ Event-Driven Architecture (async message passing)                          │
│  ├─ Time-Series Database (OHLCV + trade results)                               │
│  ├─ Data Lake (raw market data storage)                                        │
│  ├─ Kafka-style Event Bus ❌ MISSING (needed for real-time coordination)       │
│  ├─ Tick Data Engine (real-time price feeds)                                   │
│  ├─ Order Book / DOM (market depth tracking) ❌ MISSING                        │
│  ├─ Feature Engineering Engine (signal generation) ❌ PARTIAL                   │
│  ├─ Strategy Registry (version control + A/B testing)                          │
│  ├─ VPS (always-on execution for MT5/bots)                                     │
│  └─ Risk Kernel (portfolio-wide kill switch) ❌ MISSING                        │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

# ❌ SECTION 2: MISSING COMPONENTS (18-22% GAP TO 100%)

## CRITICAL MISSING PIECES (System Won't Work Without These)

### 1. ❌ UNIFIED EVENT BUS (Kafka-style)

**What it is:** Real-time message broker coordinating all system events  
**Why missing:** All trades currently routed via n8n webhooks (not scalable)  
**Impact:** Can't handle 50+ trades/second reliably  
**Size:** ~500 lines (Kafka consumer/producer OR custom event queue)  
**Time to build:** 4-6 hours

```
Current: TradingView → n8n → IZA Bot (slow)
Need:    TradingView → Event Bus → IZA Bot → Execution (fast)
         Risk updates → Event Bus → All bots (broadcast)
         Trade execution → Event Bus → Reporting → All subscribers
```

### 2. ❌ ORDER BOOK / MARKET DEPTH ENGINE

**What it is:** Real-time DOM (depth of market) tracking  
**Why missing:** Can't identify true liquidity zones (only looking at charts)  
**Impact:** Missing "cleaner entries" identified in ORB strategy  
**Size:** ~800 lines (CCXT DOM feeder + caching)  
**Time to build:** 6-8 hours

```
Need: CCXT → orderbook_snapshot → Order Book Engine
      → Local cache updated 100ms
      → Signal to Intelligence bot: "Liquidity at $X with Y contracts"
```

### 3. ❌ UNIFIED RISK KERNEL

**What it is:** Portfolio-wide kill switch + constraint enforcement  
**Why missing:** No VAR/drawdown limits (only per-trade compliance checks)  
**Impact:** Can blow up entire account in cascade  
**Size:** ~600 lines (risk calculator + enforcement)  
**Time to build:** 4-5 hours

```
Need: Risk Kernel receives:
      ├─ Portfolio delta
      ├─ Leverage used
      ├─ Correlated exposure
      ├─ Drawdown %
      └─ Returns: APPROVE / BLOCK ALL TRADES (hard stop)
```

### 4. ❌ FEATURE ENGINEERING ENGINE (Complete)

**What it is:** Real-time signal pipeline (liquidity detection, volatility, reversals)  
**Why missing:** ORB logic is manual (hard-coded in bots)  
**Impact:** Can't add new signals without code changes  
**Size:** ~700 lines (feature factory + registry)  
**Time to build:** 5-6 hours

```
Need: Raw OHLCV → Feature Engine:
      ├─ ORB High/Low (automated)
      ├─ Liquidity Zones (DOM-based)
      ├─ Reversal Patterns (ML model)
      ├─ Volatility Score
      └─ Output: [signal_1, signal_2, confidence]
```

### 5. ❌ STRATEGY REGISTRY + VERSION CONTROL

**What it is:** Versioned strategy definitions with A/B testing support  
**Why missing:** Can't roll back bad strategy changes  
**Impact:** Accidental bad deployment breaks trading  
**Size:** ~400 lines (versioning + rollback)  
**Time to build:** 3-4 hours

```
Need: 
strategy_v1: ORB breakout + 2x liquidity
strategy_v2: ORB breakout + 3x liquidity + reversal filter
strategy_v3: Previous + order flow confirmation

Can A/B test: v1 on EURUSD, v2 on GBPUSD, v3 on NZDUSD
Rollback instantly if v2 wins/loses
```

---

## HIGH-PRIORITY MISSING PIECES (System Works but Degraded)

### 6. ❌ UNIFIED EXECUTION ADAPTER

**What it is:** Single interface for all brokers (MT5, Tradeovate, Alpaca, CCXT)  
**Why missing:** Each broker has different API (manual mapping)  
**Impact:** Adding new broker takes 2+ hours of integration  
**Size:** ~500 lines (unified order class + adapter pattern)  
**Time to build:** 3-4 hours

```
Current: 
if strategy == "MT5": send_to_mt5_api(order)
elif strategy == "Tradeovate": send_to_tradeovate_api(order)

Need:
unified_execute(order={symbol, size, side, tp, sl})
  ├─ Routes to MT5 / Tradeovate / Alpaca / CCXT via adapter
  └─ Returns standardized response: {order_id, fill_price, status}
```

### 7. ❌ TRADE CONFIRMATION + ACK SYSTEM

**What it is:** Waits for broker to confirm order before marking as "filled"  
**Why missing:** Assumes fills happen instantly (unreliable)  
**Impact:** Orphaned trades, wrong P&L calculations  
**Size:** ~300 lines (ACK queue + retry logic)  
**Time to build:** 2-3 hours

```
Need:
1. Send order to broker
2. Wait for broker ACK (max 5sec timeout)
3. If no ACK: retry or manual intervention
4. Log: order_id + timestamp + actual_fill_price
```

### 8. ❌ LIVE P&L UPDATE ENGINE

**What it is:** Real-time P&L tracking as prices move  
**Why missing:** P&L calculated only at exit (not live mid-trade)  
**Impact:** Dashboard can't show "you're up $500 right now"  
**Size:** ~300 lines (live quote subscriptions + calculator)  
**Time to build:** 2-3 hours

```
Need:
Open trade: {symbol: EURUSD, entry: 1.0850, size: 2.0}
Current price: 1.0865
→ Live P&L = (1.0865 - 1.0850) × 2.0 lots × $100K = $3,000
Update dashboard every 100ms
```

### 9. ❌ MULTI-TIMEFRAME CONFIRMATION SYSTEM

**What it is:** Confirms ORB breakout on multiple timeframes before executing  
**Why missing:** ORB rules only check current chart (no confluence)  
**Impact:** Fake breakouts → false signals → losses  
**Size:** ~400 lines (multi-TF logic + confidence weighting)  
**Time to build:** 3-4 hours

```
Need:
Signal on 5m chart: ORB breakout
Confirm on 15m: still above ORB? (confidence +25%)
Confirm on 1h: in uptrend? (confidence +25%)
Only trade if 2/3 confirmations → 75%+ confidence
```

### 10. ❌ SWAP/ROLLOVER AUTOMATION

**What it is:** Automatically closes/rolls positions at daily rollover (forex)  
**Why missing:** Manual rollover = missed trades at 5pm EST  
**Impact:** Overnight swap charges + missed entry opportunities  
**Size:** ~250 lines (scheduled task + position monitoring)  
**Time to build:** 2-3 hours

```
Need:
Daily 5pm EST: Check all open FX positions
If rollover fee > configured %: Close position
Wait 10 min for new daily candle
Re-enter if signal still valid
```

---

## MEDIUM-PRIORITY NICE-TO-HAVES

### 11. ⚠️ MACHINE LEARNING SIGNAL ENHANCER

**Status:** Partially implemented (fin-023 has some ML)  
**What's needed:** Train on 2+ years historical data  
**Size:** ~600 lines (ML pipeline + model serving)  
**Time:** 8-10 hours

### 12. ⚠️ NEWS SENTIMENT ANALYSIS

**Status:** Forex Factory feed exists, no NLP  
**What's needed:** Real-time sentiment scoring (bullish/bearish)  
**Size:** ~300 lines (API call to sentiment service)  
**Time:** 3-4 hours

### 13. ⚠️ MULTI-CURRENCY CORRELATION ENGINE

**Status:** Missing  
**What's needed:** Track EURUSD vs GBPUSD correlation, avoid conflicting trades  
**Size:** ~400 lines (correlation calculator + constraint checker)  
**Time:** 4-5 hours

---

## SUMMARY: MISSING COMPONENTS BY EFFORT

| # | Component | Critical? | Lines | Hours | Type |
|---|-----------|-----------|-------|-------|------|
| 1 | Event Bus | ⚠️ CRITICAL | 500 | 4-6 | Infrastructure |
| 2 | Order Book / DOM | ⚠️ CRITICAL | 800 | 6-8 | Data |
| 3 | Risk Kernel | ⚠️ CRITICAL | 600 | 4-5 | Risk |
| 4 | Feature Engine | ⚠️ CRITICAL | 700 | 5-6 | Signals |
| 5 | Strategy Registry | HIGH | 400 | 3-4 | Control |
| 6 | Execution Adapter | HIGH | 500 | 3-4 | Execution |
| 7 | Trade ACK System | HIGH | 300 | 2-3 | Execution |
| 8 | Live P&L Engine | HIGH | 300 | 2-3 | Display |
| 9 | Multi-TF Confirm | MEDIUM | 400 | 3-4 | Signals |
| 10 | Swap Automation | MEDIUM | 250 | 2-3 | Operations |
| 11 | ML Signal | MEDIUM | 600 | 8-10 | Intelligence |
| 12 | Sentiment Analysis | LOW | 300 | 3-4 | Intelligence |
| 13 | Correlation Engine | LOW | 400 | 4-5 | Risk |

**TOTAL TO REACH 100%:** ~5,900 lines | **40-50 hours of development**

---

# 🚀 SECTION 3: INSTALLATION & DEPLOYMENT ORDER

## INSTALL PHASES (Sequential + Parallel Where Possible)

### ⏱️ PHASE 0: PREREQUISITES (Day 1, 2-3 hours)

**DO FIRST — Everything else depends on this**

```bash
# 1. Install base infrastructure
sudo apt-get update && apt-get install -y \
  python3.11 \
  postgresql \
  redis-server \
  timescaledb \
  supervisor

# 2. Python virtual environment
python3.11 -m venv /opt/trading-os
source /opt/trading-os/bin/activate
pip install --upgrade pip setuptools wheel

# 3. Clone all repos
mkdir -p /opt/trading-repos
cd /opt/trading-repos
git clone https://github.com/yourusername/genixbank-financial-system.git
git clone https://github.com/yourusername/iza-os-financial-core.git
git clone https://github.com/yourusername/fin-023-investment-portfolio-ai.git
# ... (all 45+ repos)

# 4. Start databases
systemctl start postgresql
systemctl start redis-server
systemctl start supervisor

# 5. Create database
createdb civilization_os
psql civilization_os < schema/operating_system_schema.sql
```

**Status Check:**
```bash
$ python3 --version  # Python 3.11+
$ psql --version     # PostgreSQL 14+
$ redis-cli ping     # PONG
```

---

### ⏱️ PHASE 1: DATA LAYER (Day 1-2, 3-4 hours)

**PARALLEL TASKS**

```
1a. Time-Series Database Setup
    ├─ Create TimescaleDB hypertable (trades, OHLCV)
    ├─ Create indexes on timestamp + symbol
    └─ Load historical OHLCV (2+ years)
    
1b. API Connections
    ├─ yfinance integration
    ├─ finnhub client setup
    ├─ twelvedata client setup
    └─ Test data flows
```

**Commands:**

```bash
# 1a. TimescaleDB
psql civilization_os <<EOF
CREATE TABLE trades (
  time TIMESTAMPTZ NOT NULL,
  symbol TEXT NOT NULL,
  side TEXT,
  size FLOAT,
  entry_price FLOAT,
  exit_price FLOAT,
  pnl FLOAT,
  strategy TEXT
);
SELECT create_hypertable('trades', 'time', if_not_exists => TRUE);
CREATE INDEX ON trades (time DESC, symbol);
EOF

# 1b. Data feeds
pip install yfinance finnhub-python twelvedata
python3 scripts/test_data_feeds.py
```

**Status Check:**
```bash
$ psql civilization_os -c "SELECT COUNT(*) FROM trades;"  # Should show loaded rows
$ python3 -c "import yfinance; print(yfinance.download('EURUSD=X', period='1d'))"
```

---

### ⏱️ PHASE 2: IZA OS CORE (Day 2-3, 4-5 hours)

**SEQUENTIAL** — Must complete before bots can run

```
iza-os-core
  ├─ Database connection pool
  ├─ Config loader
  ├─ Event logger
  └─ Status endpoint (HTTP)

iza-bot-orchestration
  ├─ Bot registry
  ├─ Dispatch queue
  ├─ Health monitor
  └─ Graceful shutdown
```

**Commands:**

```bash
cd /opt/trading-repos/iza-os-financial-core

# Install dependencies
pip install -r requirements.txt

# Initialize
python3 setup.py install

# Test core
python3 -m pytest tests/test_core.py -v
python3 scripts/health_check.py

# Start orchestration
supervisord -c conf/supervisord.conf
```

**Status Check:**
```bash
$ curl http://localhost:9000/health
# Response: {"status": "running", "bots": 15, "ready": true}

$ supervisorctl status
# All 15 bots should show RUNNING
```

---

### ⏱️ PHASE 3: IZA BOTS (Day 3-4, 8-10 hours)

**PARALLEL BOOT** — All 15 bots initialize together

```
GROUP A: Core Bots (Start first)
├─ iza-bot-processing (data ETL)
├─ iza-bot-monitoring (health)
├─ iza-bot-integration (API bridges)
└─ iza-bot-orchestration (already running)

GROUP B: Intelligence Bots (Depend on Group A)
├─ iza-bot-forecasting (market predictions)
├─ iza-bot-analytics (metrics)
├─ iza-bot-optimization (learning)
├─ iza-bot-discovery (patterns)
└─ iza-bot-synthesis (aggregation)

GROUP C: Decision Bots (Depend on Groups A+B)
├─ iza-bot-intelligence (MAIN DECISION ENGINE)
├─ iza-bot-compliance (rule checks)
├─ iza-bot-security (auth)
└─ iza-bot-reporting (journaling)

GROUP D: Support Bots (Depend on Groups A-C)
├─ iza-bot-alerting (notifications)
├─ iza-bot-management (control)
└─ iza-bot-automation (workflow)
```

**Commands:**

```bash
# Boot all IZA bots
supervisorctl start iza-bot-processing
supervisorctl start iza-bot-monitoring
supervisorctl start iza-bot-integration
sleep 5

supervisorctl start iza-bot-forecasting
supervisorctl start iza-bot-analytics
supervisorctl start iza-bot-optimization
supervisorctl start iza-bot-discovery
supervisorctl start iza-bot-synthesis
sleep 5

supervisorctl start iza-bot-intelligence
supervisorctl start iza-bot-compliance
supervisorctl start iza-bot-security
supervisorctl start iza-bot-reporting
sleep 5

supervisorctl start iza-bot-alerting
supervisorctl start iza-bot-management
supervisorctl start iza-bot-automation

# Verify all running
supervisorctl status | grep RUNNING
```

**Status Check:**
```bash
$ curl http://localhost:9000/bots/status
# Response: {
#   "iza-bot-intelligence": "ready",
#   "iza-bot-compliance": "ready",
#   ... (all 15 should be ready)
# }
```

---

### ⏱️ PHASE 4: FINANCIAL CORE (Day 4, 3-4 hours)

**SEQUENTIAL** — Order matters

```
4a. Genixbank-Financial-System
    ├─ Capital ledger initialization
    ├─ Account balance sync
    └─ Transaction history import

4b. fin-023-investment-portfolio-ai
    ├─ Portfolio initialization
    ├─ Strategy registry load
    └─ Historical backtesting data

4c. fin-026-financial-compliance-scanner
    ├─ Rule engine load
    ├─ Compliance rules DB
    └─ Test compliance gates

4d. fin-004-genixbanks-ai-treasurer
    ├─ Allocation rules load
    ├─ Connect to Genixbank
    └─ Rebalancing logic
```

**Commands:**

```bash
# 4a. Genixbank
cd /opt/trading-repos/genixbank-financial-system
pip install -r requirements.txt
python3 setup.py install
python3 scripts/init_accounts.py --capital 100000  # Placeholder amount

# 4b. fin-023
cd /opt/trading-repos/fin-023-investment-portfolio-ai
pip install -r requirements.txt
python3 scripts/load_historical_data.py --years 2
python3 -m pytest tests/test_portfolio.py -v

# 4c. fin-026
cd /opt/trading-repos/fin-026-financial-compliance-scanner
pip install -r requirements.txt
python3 scripts/load_compliance_rules.py
python3 scripts/test_gates.py

# 4d. fin-004
cd /opt/trading-repos/fin-004-genixbanks-ai-treasurer
pip install -r requirements.txt
python3 scripts/connect_to_genixbank.py
python3 scripts/init_allocation_rules.py
```

**Status Check:**
```bash
$ curl http://localhost:8080/genixbank/balance
# Response: {"total_capital": 100000, "available": 100000, "deployed": 0}

$ curl http://localhost:8081/portfolio/strategies
# Response: [{"strategy": "ORB", "score": 85, "win_rate": 0.62}, ...]
```

---

### ⏱️ PHASE 5: BROKER CONNECTIONS (Day 4-5, 4-5 hours)

**PARALLEL** — All can initialize at same time

```
5a. MetaTrader 5 (MT5)
    ├─ Install MT5 terminal
    ├─ Configure Python integration
    ├─ Test connection + sample trade
    └─ Set account balance hook

5b. Tradeovate
    ├─ API credentials setup
    ├─ Account initialization
    ├─ Test order submission
    └─ Check margin requirements

5c. Alpaca Brokerage
    ├─ API keys setup
    ├─ Paper trading mode (FIRST)
    ├─ Test order flow
    └─ Set account parameters

5d. CCXT (Crypto)
    ├─ Install CCXT
    ├─ Configure exchanges (Binance, Coinbase, Kraken)
    ├─ Test market data feeds
    └─ (Paper trading only initially)
```

**Commands:**

```bash
# 5a. MT5
pip install MetaTrader5
python3 <<'EOF'
import MetaTrader5 as mt5
mt5.initialize(login=PLACEHOLDER_LOGIN, password=PLACEHOLDER_PASSWORD, server="PLACEHOLDER_SERVER")
print(f"Connected: {mt5.terminal_info()}")
mt5.shutdown()
EOF

# 5b. Tradeovate
pip install tradeovate-api
python3 scripts/setup_tradeovate.py --api-key PLACEHOLDER_KEY

# 5c. Alpaca
pip install alpaca-trade-api
python3 scripts/setup_alpaca.py --api-key PLACEHOLDER_KEY --paper True

# 5d. CCXT
pip install ccxt
python3 scripts/setup_ccxt.py --exchanges binance,coinbase,kraken
```

**Status Check:**
```bash
$ python3 -c "from alpaca_trade_api import REST; api = REST(); print(api.get_account())"
# Response: Account(account_type='paper', ...)

$ python3 -c "import ccxt; ex = ccxt.binance(); print(ex.fetch_ticker('BTC/USDT')['last'])"
# Response: 45000.50
```

---

### ⏱️ PHASE 6: ORCHESTRATION (n8n + MCP) (Day 5, 3-4 hours)

**SEQUENTIAL** — n8n must come before MCP server

```
6a. n8n Setup
    ├─ Docker or local install
    ├─ Create webhook listener (TradingView)
    ├─ Create routing workflows
    └─ Load 3 initial workflows

6b. MCP Server
    ├─ Start MCP server
    ├─ Register all IZA bots
    ├─ Test inter-bot communication
    └─ Load protocol definitions
```

**Commands:**

```bash
# 6a. n8n (Docker)
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -e DB_TYPE=postgres \
  -e DB_POSTGRESDB_CONNECTION_URL='postgresql://user:pass@localhost/n8n' \
  n8nio/n8n

# Or local
npm install -g n8n
n8n start

# Then import workflows
python3 scripts/import_n8n_workflows.py \
  --tradingview-webhook \
  --route-to-intelligence \
  --execute-trade

# 6b. MCP
cd /opt/trading-repos/mcp-server
pip install -r requirements.txt
python3 mcp_server.py --port 9100
```

**Status Check:**
```bash
$ curl http://localhost:5678/api/workflows
# Response: [{id: "...", name: "TradingView Webhook", ...}, ...]

$ curl http://localhost:9100/health
# Response: {"status": "running", "bots_registered": 15}
```

---

### ⏱️ PHASE 7: SIGNAL TESTING (Day 6, 2-3 hours)

**END-TO-END TESTING** — Before live trading

```
7a. TradingView Integration
    ├─ Create test alert
    ├─ Send webhook to n8n
    ├─ Verify routing to IZA-bot-intelligence
    └─ Check decision output

7b. Decision Flow Test
    ├─ ORB signal arrives
    ├─ Intelligence bot evaluates (capital check)
    ├─ Compliance checks (passes)
    ├─ Portfolio scoring (85/100)
    └─ Decision: BUY or SKIP

7c. Execution Test (PAPER TRADING ONLY)
    ├─ Signal routed to MT5/Tradeovate/Alpaca
    ├─ Order placed in paper account
    ├─ Verify fill + reporting
    └─ Check dashboard update
```

**Commands:**

```bash
# 7a. Test webhook
python3 scripts/test_tradingview_webhook.py

# 7b. Simulate signal
python3 <<'EOF'
import requests
import json

signal = {
    "symbol": "EURUSD",
    "side": "BUY",
    "pattern": "ORB_BREAKOUT",
    "confidence": 0.85
}

response = requests.post(
    "http://localhost:9000/signal",
    json=signal
)

print(f"Decision: {response.json()['decision']}")
EOF

# 7c. Paper trade test
python3 scripts/test_paper_trading.py --symbol EURUSD --side BUY
```

**Status Check:**
```bash
$ curl http://localhost:8080/trades/last
# Response: {
#   "symbol": "EURUSD",
#   "entry": 1.0850,
#   "pnl": 150.00,
#   "status": "open"
# }
```

---

### ⏱️ PHASE 8: DASHBOARD & MONITORING (Day 6-7, 2-3 hours)

**PARALLEL** — UI and monitoring can run independently

```
8a. fin-031 Dashboard
    ├─ Start frontend (React/Vue)
    ├─ Connect to APIs
    ├─ Load live P&L display
    └─ Load trade journal

8b. Monitoring + Alerting
    ├─ Prometheus metrics setup
    ├─ Grafana dashboard
    ├─ Alert rules (down trades, high losses, errors)
    └─ Slack/email notifications
```

**Commands:**

```bash
# 8a. Dashboard
cd /opt/trading-repos/fin-031-investor-dashboard-builder
npm install
npm run build
npm start  # Starts on http://localhost:3000

# 8b. Monitoring
pip install prometheus-client grafana-api
supervisorctl start prometheus
supervisorctl start grafana
# Grafana: http://localhost:3001 (admin/admin)

# Load dashboard
python3 scripts/setup_grafana_dashboards.py
```

**Status Check:**
```bash
$ curl http://localhost:3000/api/health
# Response: {"status": "ok", "trades": 42, "pnl": 1250.50}

$ curl http://localhost:9090/api/v1/targets
# Prometheus should show all targets as "up"
```

---

### ⏱️ PHASE 9: LIVE TRADING DEPLOYMENT (Day 7+, CAUTION)

**⚠️ DO NOT SKIP PHASES 1-8**

```
9a. Real Account Setup (MICRO FIRST)
    ├─ Switch MT5 to live micro account
    ├─ Set position size: 0.01 lot (micro)
    ├─ Set daily loss limit: -$50
    ├─ Start with $500 capital

9b. Live Signal Routing (Limited)
    ├─ Enable TradingView alerts (1-3 trades/day only)
    ├─ Route ONLY to MT5 (other brokers off)
    ├─ Monitor every single trade
    └─ Check for unexpected behavior

9c. Gradual Scale
    ├─ Week 1: 0.01 lot, $500 capital
    ├─ Week 2: If profitable, 0.05 lot, $2,000 capital
    ├─ Week 3: 0.1 lot, $5,000 capital
    └─ Month 2: Full capital (if consistent profits)
```

**Commands:**

```bash
# 9a. Switch to live (CAREFUL!)
python3 scripts/switch_mt5_to_live.py \
  --login PLACEHOLDER_LOGIN \
  --position-size 0.01 \
  --daily-loss-limit -50 \
  --max-capital 500

# 9b. Enable live signals
curl -X POST http://localhost:5678/workflows/WORKFLOW_ID/activate
curl -X POST http://localhost:9000/trading/enable \
  --data '{"mode": "live", "brokers": ["MT5"], "max_trades_per_day": 3}'

# 9c. Scale up (after 1 week of profits)
python3 scripts/increase_position_size.py --new-size 0.05 --new-capital 2000
```

**Status Check:**
```bash
$ curl http://localhost:8080/account/live/balance
# Response: {"balance": 450.00, "equity": 505.50, "pnl": 5.50}

$ curl http://localhost:8080/trades/live/count
# Response: {"trades_today": 2, "wins": 1, "losses": 1}
```

---

## INSTALLATION TIMELINE SUMMARY

| Phase | Name | Duration | Day | Cumulative |
|-------|------|----------|-----|-----------|
| 0 | Prerequisites | 2-3h | 1 | 2-3h |
| 1 | Data Layer | 3-4h | 1-2 | 5-7h |
| 2 | IZA Core | 4-5h | 2-3 | 9-12h |
| 3 | IZA Bots | 8-10h | 3-4 | 17-22h |
| 4 | Financial Core | 3-4h | 4 | 20-26h |
| 5 | Brokers | 4-5h | 4-5 | 24-31h |
| 6 | Orchestration | 3-4h | 5 | 27-35h |
| 7 | Signal Testing | 2-3h | 6 | 29-38h |
| 8 | Dashboard | 2-3h | 6-7 | 31-41h |
| 9 | Live Trading | (Ongoing) | 7+ | 31-41h + |

**TOTAL TIME TO LIVE:** ~31-41 hours (4-5 days if working full-time)

---

## CRITICAL CHECKPOINTS (Don't Skip!)

| Checkpoint | Must Pass Before | Action if Fail |
|-----------|---|---|
| Phase 0 test | Moving to Phase 1 | Re-install dependencies |
| Phase 1 data load | Moving to Phase 2 | Check DB connection + API keys |
| Phase 3 all bots running | Moving to Phase 4 | Check logs: `supervisorctl tail -f` |
| Phase 5 paper trade test | Moving to Phase 6 | Verify broker API connection |
| Phase 7 signal routing | Moving to Phase 9 | Check n8n webhook logs |
| Phase 8 dashboard loads | Moving to Phase 9 | Check frontend connection to APIs |
| Paper trading 1 week | Switching to Phase 9 live | Ensure win rate > 45% |

---

## ROLLBACK STRATEGY (If Something Breaks)

```bash
# Pause everything
supervisorctl stop all

# Check logs
tail -f /var/log/iza-bots/*.log
journalctl -u supervisor -f

# Roll back last change
git log --oneline -5  # See recent commits
git revert HEAD       # Undo last change

# Restart
supervisorctl start all
curl http://localhost:9000/health  # Verify
```

---

## POST-INSTALLATION CHECKLIST

- [ ] Phase 0: All dependencies installed + verified
- [ ] Phase 1: Time-series DB has 2+ years OHLCV data
- [ ] Phase 2: IZA-OS-core running, endpoint responds
- [ ] Phase 3: All 15 IZA bots show RUNNING in supervisorctl
- [ ] Phase 4: Genixbank balance = $100K, fin-023 strategies loaded
- [ ] Phase 5: Can place paper trades on all 4 brokers
- [ ] Phase 6: n8n webhook receives test signal, MCP server responds
- [ ] Phase 7: End-to-end signal → decision → execution works
- [ ] Phase 8: Dashboard shows live trades + P&L
- [ ] Phase 9: Paper trading 1 week, win rate documented

---

**Ready to deploy? Run Phase 0 first.**
