# 💾 STORAGE & INFRASTRUCTURE SIZING

**Date:** 2026-06-06  
**System:** 70-75 component trading OS  
**Scope:** 2+ years historical data, live trading, 15 IZA bots

---

# 📊 STORAGE BREAKDOWN

## TIER 1: DATABASES (Largest Component)

### Time-Series Database (TimescaleDB)

**OHLCV Data (Main Driver)**

Symbols tracked:
- Forex: EURUSD, GBPUSD, NZDUSD, AUDUSD (4 pairs)
- Crypto: BTC, ETH, SOL, XRP, BNB (5 tokens)
- Stocks: SPY, QQQ, IWM, GLD, TLT (5 ETFs)
- Futures: NQ, ES, YM (3 contracts)
- **Total: ~17 instruments**

Data frequency:
- 1-minute candles: 2+ years
- 5-minute candles: 2+ years
- 1-hour candles: 2+ years
- Daily candles: 5-10 years

**Calculation:**

```
1-minute OHLCV per symbol per day:
- 1440 candles/day × 5 fields (O,H,L,C,V) × 8 bytes = 57.6 KB/day

Annual per symbol:
- 57.6 KB × 365 days = 21 MB/year

2 years for 17 symbols:
- 21 MB × 2 × 17 = 714 MB (just 1-min data)

Add 5-min, 1-hour, daily:
- 5-min: 200 MB (2 years, 17 symbols)
- 1-hour: 50 MB (2 years, 17 symbols)
- Daily: 5 MB (10 years, 17 symbols)

SUBTOTAL OHLCV: ~970 MB (≈ 1 GB)
```

**Trade Journal (Execution Data)**

Assumptions:
- 5 trades/day average
- 1,825 days (5 years of trading records)
- ~9,125 trades total

Per trade record:
```
Fields: timestamp, symbol, side, size, entry_price, exit_price, 
        pnl, strategy, duration, slippage, commission
Bytes: ~83 bytes per trade
```

Storage for 10,000 trades:
- 10,000 × 83 bytes = 830 KB (negligible)

**Risk/Compliance Data**

Per trade: ~170 bytes (VAR, correlation, leverage, compliance flags, audit)
- 10,000 trades: 1.7 MB (negligible)

**Total TimescaleDB:**
- OHLCV: 1 GB
- Trades: 1 MB
- Risk data: 2 MB
- Indexes + overhead: 200 MB
- **SUBTOTAL: ~1.2 GB**

---

### Backup & Snapshots

TimescaleDB backups:
- Daily full backup: 1.2 GB × 365 = 438 GB/year
- Keeping 1-week rolling backups: 438 × (7/365) = ~8.4 GB
- Keeping 1-month backups: ~36 GB

**Recommended:** Keep 1-week rolling backups = **8.4 GB**

---

## TIER 2: DATA LAKE (Parquet Files)

Raw market data stored as Parquet (compressed):

**Per asset per day:**
- CSV format: 150 KB
- Parquet (compressed): 40 KB

**2 years, 17 symbols:**
- 40 KB × 17 × 730 days = 500 MB

**Add alternative data feeds:**
- Forex Factory news archives: 50 MB
- Market sentiment data: 100 MB
- Correlation matrices (daily): 30 MB

**SUBTOTAL Data Lake: ~680 MB ≈ 0.7 GB**

---

## TIER 3: CODE & DEPENDENCIES

### Python Virtual Environment

Base packages:
- numpy, pandas, scipy, scikit-learn, requests: ~500 MB
- Data packages (yfinance, ccxt, finnhub): ~200 MB
- ML packages (XGBoost, LightGBM): ~400 MB
- Visualization (plotly, mplfinance, bokeh): ~300 MB
- Testing (pytest): ~100 MB
- **Subtotal venv: ~1.5 GB**

### Your 45-50 Repos (Git)

Clone all repos with history:
- Lean repos (fin-001–fin-035): 20 MB each × 35 = 700 MB
- IZA bot repos (15 bots): 30 MB each = 450 MB
- Core repos (genixbank, fin-023, etc.): 100 MB each × 5 = 500 MB
- Supporting (agents-os, ai-boss-os, etc.): 50 MB each × 5 = 250 MB

**Subtotal repos: ~1.9 GB**

### Node/npm Packages (fin-031 dashboard + n8n)

- React/Vue frontend: 500 MB - 1 GB
- n8n dependencies: 300 MB

**Subtotal Node: ~1 GB**

**TOTAL Code & Dependencies: ~4.5 GB**

---

## TIER 4: LOGS & MONITORING

### Application Logs

Per bot (15 IZA bots):
- 1 MB/day per bot × 15 = 15 MB/day total
- 30 days rolling retention: 450 MB

n8n workflow logs:
- 1,000 signal executions/day × 5 KB each = 5 MB/day
- 30 days rolling: 150 MB

Prometheus metrics (time-series):
- 500 metrics × 60 samples/hour × 24 hours × 30 days = 21.6 MB

Grafana dashboards & configs:
- 50 MB

**SUBTOTAL Logs: ~700 MB**

---

## TIER 5: DOCKER IMAGES & CONTAINERS

If dockerized (shared base image):
- Python base image: 900 MB
- PostgreSQL: 200 MB
- TimescaleDB extension: 100 MB
- Redis: 100 MB
- n8n image: 400 MB
- Prometheus: 150 MB
- Grafana: 200 MB
- Node image (dashboard): 300 MB

**SUBTOTAL Docker: ~2.3 GB (shared base, not duplicated)**

---

## TIER 6: MISC

- Config files (.env, YAML): 10 MB
- Documentation (markdown): 20 MB
- SSL certificates: 1 MB
- Temporary cache files: 100 MB

**SUBTOTAL Misc: ~130 MB**

---

# 📈 TOTAL STORAGE CALCULATION

| Component | Size | Notes |
|-----------|------|-------|
| **Databases** | 1.2 GB | TimescaleDB (OHLCV + trades + risk) |
| **Backups** | 8.4 GB | 1-week rolling backups |
| **Data Lake** | 0.7 GB | Parquet files + news + sentiment |
| **Code & Repos** | 1.9 GB | 45-50 repos + git history |
| **Dependencies** | 1.5 GB | Python venv |
| **Node Packages** | 1 GB | npm + n8n |
| **Logs & Monitoring** | 0.7 GB | 30-day rolling logs |
| **Docker Images** | 2.3 GB | Container images (shared base) |
| **Misc** | 0.2 GB | Configs, docs, certs |
| | | |
| **SUBTOTAL** | **~19.9 GB** | **~20 GB** |

---

# 🚀 SCALABLE SIZING BY SCENARIO

## SCENARIO 1: SMALL SETUP (MVP - Phase 0-4)

Just starting, minimal data:
- 5 symbols (3 forex, 2 crypto)
- 6 months historical data
- No backups
- Minimal logs (7 days)

**Size: 2-3 GB**

Suitable for:
- Laptop development
- Local machine
- Home VPS ($5-10/month)

---

## SCENARIO 2: MEDIUM SETUP (Phase 5-8)

Full system, 2 years data:
- 17 symbols (forex, crypto, stocks, futures)
- 2 years OHLCV + trade journal
- 1-week backups
- 30 days logs

**Size: 20-25 GB**

Suitable for:
- Mid-range VPS ($20-50/month)
- DigitalOcean Standard ($12/month for 50GB SSD)
- AWS EC2 t3.micro ($10/month)
- Linode Nanode ($5-17/month)

---

## SCENARIO 3: LARGE SETUP (Production - 100+ symbols)

Enterprise scale:
- 100+ symbols (all major forex, crypto, US stocks)
- 5+ years historical data
- 2-week backups
- 90 days logs + audit trail

**Size: 200-500 GB**

Suitable for:
- High-end VPS ($100-200/month)
- Dedicated server ($50-100/month)
- AWS RDS + S3 ($50-150/month)
- Google Cloud ($50-150/month)

---

# 💡 STORAGE OPTIMIZATION TIPS

## Reduce Database Size

1. **Enable TimescaleDB Compression**
   - Reduces size by 50%: 1 GB → 500 MB
   - Command: `SELECT compress_chunk(...)`

2. **Archive Old Data**
   - Keep 2 years hot (SSD): $0.10/GB/month
   - Move 3-5 years to S3 Glacier: $0.004/GB/month
   - Savings: 96% on cold storage

3. **Downsample Low-Priority Symbols**
   - High-frequency: 1-min + 5-min candles
   - Lower-frequency: Only daily/1-hour
   - Saves 40% storage

## Reduce Backup Size

1. **Incremental Backups**
   - Only changed data: 10% of full size
   - 8.4 GB → 840 MB/week

2. **Compress Backups**
   - gzip compression: 60% reduction
   - 8.4 GB → 3.4 GB

3. **Cloud Backups to S3**
   - S3 Glacier: $0.004/GB/month
   - 8.4 GB: $0.03/month

## Reduce Code Size

1. **Docker Slim**
   - Reduces image size: 30-50%
   - 2.3 GB → 1.2 GB

2. **Shallow Clone Repos**
   - No git history: 50% reduction
   - 1.9 GB → 950 MB

3. **Serverless (Lambda)**
   - Don't store code on machine
   - Saves 2-3 GB

---

# 🎯 RECOMMENDED CONFIG FOR YOUR SYSTEM

**Phase 0-4 (Development):**
- Storage: **5-10 GB**
- Host: Laptop or $5 VPS
- Backups: Git only
- Cost: Free or $5/month

**Phase 5-9 (Live Trading):**
- Storage: **25-50 GB SSD**
- Host: $20-50/month VPS (DigitalOcean, Linode, AWS)
- Backups: 1-week rolling to S3
- Monitoring: Prometheus + Grafana
- Cost: **$25-50/month**

**Example VPS Setup:**
```
DigitalOcean Standard Droplet
├─ CPU: 2 vCPU
├─ RAM: 4 GB
├─ Storage: 80 GB SSD
├─ Transfer: 4 TB/month
└─ Cost: $24/month

OR

Linode 4GB
├─ CPU: 2 vCPU
├─ RAM: 4 GB
├─ Storage: 80 GB SSD
└─ Cost: $20/month
```

**Production (100+ symbols):**
- AWS RDS (managed PostgreSQL): $50-100/month
- S3 for data lake: $20-50/month
- S3 Glacier backups: $10/month
- EC2 compute: $30-100/month
- **TOTAL: $110-260/month**

---

# 📊 STORAGE GROWTH OVER TIME

As you trade longer, storage grows linearly:

| Timeframe | OHLCV | Trades | Logs | Backups | **TOTAL** |
|-----------|-------|--------|------|---------|-----------|
| Month 1 | 50 MB | 10 KB | 50 MB | 1 GB | **~1.1 GB** |
| Year 1 | 600 MB | 100 KB | 100 MB | 4 GB | **~4.8 GB** |
| Year 2 | 1.2 GB | 500 KB | 150 MB | 8.4 GB | **~9.7 GB** |
| Year 5 | 3 GB | 2 MB | 200 MB | 20 GB | **~23 GB** |

**Linear growth:** +5 GB per year

---

# 🔧 MONITORING DISK USAGE

```bash
# Check current usage
du -sh /opt/trading-os
df -h /

# Monitor growth
du -sh /opt/trading-os/data/*
du -sh /var/lib/postgresql/

# Set alerts
# If > 80% full, trigger warning
# If > 90% full, stop trading (safety)

# Clean old logs (keep 30 days)
find /var/log -name "*.log" -mtime +30 -delete

# Compress old trades
tar -czf trades_2024.tar.gz /var/lib/postgresql/trades_2024/
```

---

# 💰 ANNUAL COST BREAKDOWN

| Component | Monthly | Annual | Notes |
|-----------|---------|--------|-------|
| **VPS** | $20-50 | $240-600 | DigitalOcean/Linode |
| **Backups (S3)** | $3 | $36 | S3 storage for backups |
| **Database** | $0 | $0 | Self-hosted (included) |
| **Monitoring** | $0 | $0 | Prometheus/Grafana free |
| **Brokers** | TBD | TBD | Commissions on trades |
| | | |
| **TOTAL** | **$23-53** | **$276-636** |

**Payoff:** Breaks even after 1-2 profitable trading days (assuming $500-2000 profit per trade)

---

# ⚡ QUICK REFERENCE TABLE

| Use Case | Storage | VPS Cost | Backups | Notes |
|----------|---------|----------|---------|-------|
| **Dev/Test** | 5 GB | Free-$5 | None | Laptop or micro VPS |
| **Phase 0-7** | 10 GB | $5-10 | Git only | Development phase |
| **Phase 8-9 (Live)** | 25 GB | $20-50 | 1-week rolling | Production ready |
| **100+ Symbols** | 200+ GB | $100-200 | 2-week rolling | Enterprise scale |

---

**TLDR:**
- **MVP:** 5-10 GB, $0-10/month
- **Live Trading:** 20-25 GB, $20-50/month  
- **Enterprise:** 200+ GB, $100-200/month
- **Payoff:** 1-2 profitable trading days covers all annual costs
