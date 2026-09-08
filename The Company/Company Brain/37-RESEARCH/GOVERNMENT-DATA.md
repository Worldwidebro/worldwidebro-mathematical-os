---
id: RES-GOV-001
title: "GOVERNMENT-DATA — Federal Economic & Business Intelligence"
tags: [research, government-data, macroeconomics, census, bls, bea, fred]
status: ACTIVE
updated: 2026-09-06
---

[[STARTHERE]] | [[37-RESEARCH/README|37-RESEARCH]] | [[37-RESEARCH/SOURCE-REGISTRY|Source Registry]] | [[23-VENTURES/23-VENTURES|Ventures]]

# GOVERNMENT-DATA.md — Federal Economic & Business Intelligence

> **Authority:** Economic Intelligence Control Plane (CP-020)  
> **Feeds:** Census Bureau (`SRC-CENSUS`), BLS (`SRC-BLS`), BEA (`SRC-BEA`), FRED (`SRC-FRED`), SEC (`SRC-SEC`)  
> **Purpose:** Grounding Company Brain venture models in macroeconomic and industrial reality rather than speculative TAM/SAM guesses.

---

## 1. Agency Mapping to Core Ventures

| Federal Agency | Primary Datasets | Direct Venture Application |
| :--- | :--- | :--- |
| **U.S. Census Bureau** | • Business Dynamics Statistics (BDS)<br>• Annual Integrated Economic Survey (AIES)<br>• County Business Patterns (CBP) | **`LT-005` & `LT-011`**: County-level density of hospitals, diagnostic labs, clinics, and manufacturing shippers.<br>**`CON-001`**: Establishments, payroll, and revenue for specialty trade contractors (NAICS 238). |
| **Bureau of Labor Statistics (BLS)** | • Occupational Employment & Wages (OEWS)<br>• Job Openings & Turnover (JOLTS)<br>• Producer Price Index (PPI) | **`OPS-001` (Staffing)**: Prevailing wage rates by MSA, unfilled job opening ratios, and worker churn metrics.<br>**`LT-005`**: Courier and messenger median hourly wages (SOC 53-7021). |
| **Bureau of Economic Analysis (BEA)** | • GDP by Industry<br>• Corporate Profits by Industry<br>• Personal Income & Outlays | **`FIN-037`**: Macro capital allocation, corporate profit margins by industry sector, economic inflection points. |
| **Federal Reserve (FRED)** | • Fed Funds Rate, SOFR, 10-Yr Treasury<br>• Delinquency Rates & Commercial Credit<br>• Housing Starts & Case-Shiller Index | **`RE-001` (Real Estate)**: Mortgage rate trajectories, regional cap rate pressures, and debt debt-service coverage.<br>**`FIN-037`**: Macro risk-on / risk-off liquidity signals. |
| **SEC EDGAR** | • Form 10-K (Annual audited reports)<br>• Form 10-Q (Quarterly financials)<br>• Form 8-K (Material unscheduled events) | **Competitive Intelligence**: Real gross margins, customer acquisition costs, churn disclosures, and risk factors of publicly traded incumbents. |

---

## 2. Census Bureau Automated Ingestion (`SRC-CENSUS`)

### Core API Endpoints
- **Business Dynamics Statistics (BDS):** `https://api.census.gov/data/timeseries/bds`  
  *Filters:* NAICS 2-6 digit, firm age, firm size, geography (State, Metro, County).  
  *Value:* Measures startup formation rate vs establishment death rate in target venture verticals.
- **County Business Patterns (CBP):** `https://api.census.gov/data/2023/cbp`  
  *Value:* Pinpoints exact business count and total payroll per zip code for local logistics dispatch (`LT-005`).

---

## 3. Bureau of Labor Statistics Automation (`SRC-BLS`)

### Series Keys for Core Ventures
- `OEUS0000000000000000053702100`: Light truck & delivery drivers hourly mean wage.
- `JTS000000000000000JOL`: Total nonfarm job openings rate (seasonal adjustment).
- `WPU101704`: Construction materials producer price index.

---

## 4. FRED Macroeconomic Ingestion (`SRC-FRED`)

### Macroeconomic Guardrails
- **SOFR30DAYAVG:** 30-Day Average SOFR (Base borrowing rate).
- **HOUST:** Housing Starts: Total New Privately Owned Units Started.
- **CSUSHPISA:** S&P/CoreLogic Case-Shiller U.S. National Home Price Index.
- **DRCCLACBS:** Delinquency Rate on Credit Card Loans, All Commercial Banks.

---

## 5. Automated Pipeline Integration

```bash
# Example invocation via Company Brain CLI
cb research pull --source census --naics 621511  # Medical Laboratories
cb research pull --source bls --series JOLTS     # Staffing labor demand
cb research pull --source fred --series SOFR     # Interest rate benchmark
```
All fetched time-series are stored canonically in `_REGISTRIES/CANONICAL/ECONOMIC_DATA/` and indexed into Qdrant for semantic agent querying.

---

## Connected Entities & Ventures
- **Master Research OS:** [[37-RESEARCH/RESEARCH-OS]]
- **Master Source Registry:** [[37-RESEARCH/SOURCE-REGISTRY]]
- **Operating Ventures Hub:** [[23-VENTURES/23-VENTURES]]
- **Economic Reality Ledger:** [[ECONOMIC-REALITY]]
