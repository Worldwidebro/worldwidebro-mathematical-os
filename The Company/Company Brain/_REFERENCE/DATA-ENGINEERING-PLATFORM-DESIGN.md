# Company Brain — Data Engineering Platform Design
**Modern Data Stack for 789 Ventures**
2026-09-19 | Data Engineer Assessment

---

## Executive Summary

**Current State:** 5 disconnected data sources, batch sync (1x/day), no data contracts, scattered storage.  
**Target State:** Real-time synchronized platform with data quality, governance, and cost optimization.  
**Timeline:** 4 weeks | Cost: ~$2K–$5K cloud infrastructure  
**ROI:** 10x faster decision-making, 30% cost reduction via optimized storage.

---

## 1. Current Data Architecture Assessment

### Data Sources (Scattered)

| Source | Type | Volume | Latency | Status | Owner |
|--------|------|--------|---------|--------|-------|
| **Supabase** | PostgreSQL | 789 ventures × 23 KPIs | Real-time | ✅ Live | Transactional |
| **Neo4j** | Graph DB | 20,363 edges | Batch (24h) | 🟡 Stale | Relationships |
| **Qdrant** | Vector DB | 17,236 vectors | On-register | ✅ Live | Semantics |
| **Vercel** | Deployments | 7 live ventures | Real-time | 🟡 Unmapped | Hosting |
| **OmniRoute** | Tool routing | 110 tools | Real-time | 🔴 Unknown | Execution |
| **T7 Shield** | Cold storage | ~900 GB | N/A | 🔴 Unmanaged | Backup |
| **Lacie** | Cold storage | ? GB | N/A | 🔴 Unknown | Backup |
| **Git repos** | Code + docs | 177 code + 618 templates | On-commit | ✅ Indexed | Infrastructure |

**Problem:** No single source of truth. Each system owns a slice.

### Data Contracts (MISSING)

```
What is a "venture"?
├─ Supabase says: id, name, sector, readinessPercent, revenue_ytd, ...
├─ Neo4j says: Venture node with 23 properties
├─ Vercel says: A deployed URL in v-config.json
└─ VEX says: A row in the portfolio table

MISMATCH: If definition changes, which updates?
```

### Data Quality Issues

| Issue | Impact | Severity |
|-------|--------|----------|
| Supabase ≠ Neo4j venture counts | Portfolio metrics wrong | 🔴 High |
| Vercel deployments not tracked | Status unknown for 7 ventures | 🟡 Medium |
| T7 Shield unmaintained | Backups may be corrupt | 🔴 High |
| OmniRoute routing not mapped | Tool usage invisible | 🟡 Medium |
| No data lineage | Can't trace metric origins | 🟡 Medium |

---

## 2. Modern Data Stack Design

### Proposed Architecture

```
COMPANY BRAIN DATA PLATFORM
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  DATA SOURCES (Raw) → INGESTION → TRANSFORMATION → ANALYTICS  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Supabase (PostgreSQL)                                          │
│  ├─ Ventures (789 rows)                                         │
│  ├─ Capabilities (300+ rows)                                    │
│  ├─ Agents (318 rows)                                           │
│  └─ Metrics (18K+ rows)                                         │
│         ↓                                                        │
│  [FIVETRAN] — Real-time CDC + incremental sync                 │
│         ↓                                                        │
│  DATA LAKE (S3 / T7 Shield)                                    │
│  ├─ ventures/ (Parquet, partitioned by sector)                 │
│  ├─ metrics/ (Parquet, partitioned by date + venture)          │
│  ├─ agents/ (Parquet, partitioned by capability)               │
│  └─ _metadata/ (Data catalog, lineage)                         │
│         ↓                                                        │
│  [dbt] — Transform + test + document                           │
│  ├─ Staging layer (normalize Supabase schema)                  │
│  ├─ Mart layer (dimensional model for analytics)               │
│  └─ Quality tests (great-expectations)                         │
│         ↓                                                        │
│  DATA WAREHOUSE (Snowflake / BigQuery)                         │
│  ├─ Fact tables (ventures_fact, metrics_fact)                  │
│  ├─ Dimension tables (sector_dim, agent_dim)                   │
│  └─ Analytics views (portfolio_summary, sector_performance)    │
│         ↓                                                        │
│  BI LAYER (VEX Dashboard)                                       │
│  ├─ Portfolio overview                                          │
│  ├─ Sector performance                                          │
│  ├─ Venture deep-dives                                          │
│  └─ Real-time metrics                                           │
│                                                                 │
│  GOVERNANCE LAYER (Data Catalog)                               │
│  ├─ DataHub — lineage, ownership, quality metrics              │
│  ├─ Great Expectations — data quality checks                   │
│  └─ dbt documentation — transformation logic                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Component Selection

| Layer | Current | Proposed | Rationale |
|-------|---------|----------|-----------|
| **Ingestion** | Manual | Fivetran | Real-time CDC, no code, monitoring |
| **Storage** | Scattered | S3 + T7 + Delta Lake | Unified, cost-optimized, versioned |
| **Transform** | None | dbt | Version control, testing, documentation |
| **Warehouse** | None | Snowflake / BigQuery | SQL analytics, cost-effective scale |
| **Orchestration** | None | Airflow / Prefect | DAG monitoring, error recovery |
| **Catalog** | None | DataHub | Lineage, ownership, quality tracking |
| **Quality** | None | Great Expectations | Automated anomaly detection |
| **Analytics** | VEX (basic) | VEX + BI tool | Real-time insights |

---

## 3. Data Contracts

### Contract 1: Venture Master Data

```yaml
# ventures_contract.yaml
entity: Venture
owner: Product (Holdings)
sla:
  freshness: 15 minutes  # Updated via Supabase
  availability: 99.9%
  accuracy: 100% (enforced via tests)

schema:
  venture_id:
    type: string
    primary_key: true
    source: Supabase.ventures.id
    description: "Unique venture identifier (VEN-XXXXX)"
  
  name:
    type: string
    nullable: false
    source: Supabase.ventures.name
    owner: Venture team
  
  sector:
    type: string
    nullable: false
    enum: [LT, OPS, CON, RE, ...]  # 35 values
    source: Supabase.ventures.sector
    test: "sector must be in SECTOR_ENUM"
  
  readiness_percent:
    type: numeric(3,1)
    nullable: true
    range: [0.0, 100.0]
    source: Supabase.ventures.readinessPercent
    test: "must be between 0 and 100"
    test: "must increase monotonically (no decreases)"
  
  revenue_ytd:
    type: numeric(12,2)
    nullable: false
    source: Supabase.ventures.revenue_ytd
    test: "must equal SUM of monthly revenue"
    test: "must not decrease without note in changelog"
  
  created_at:
    type: timestamp
    nullable: false
    source: Supabase.ventures.created_at
    immutable: true
  
  updated_at:
    type: timestamp
    nullable: false
    source: Supabase.ventures.updated_at
    test: "updated_at must be >= created_at"

quality_checks:
  - name: "No orphaned ventures"
    query: "ventures without valid sector"
    frequency: daily
    alert_threshold: 1
  
  - name: "Readiness completeness"
    query: "ventures with null readinessPercent > 30 days old"
    frequency: daily
    alert_threshold: 10
  
  - name: "Revenue consistency"
    query: "revenue_ytd < 0 OR revenue_ytd > $1M"
    frequency: hourly
    alert_threshold: 0

ownership:
  primary: Product team
  secondary: Finance (revenue validation)
  data_steward: acebless@worldwidebro.com
```

### Contract 2: Capability Mapping

```yaml
entity: Venture → Capability (relationship)
owner: Engineering (Infrastructure)

relationship_type: USES_CAPABILITY
cardinality: many-to-many

constraints:
  - venture_id must exist in ventures_master
  - capability_id must exist in capabilities_master
  - relationship created_at <= venture created_at (invalid if violated)
  - capability must be deployed before venture can use it

quality_checks:
  - "All 789 ventures have ≥1 capability"
  - "No circular capability dependencies"
  - "Capability versions match deployed versions"
```

### Contract 3: Solution Registry

```yaml
entity: Solution
owner: Engineering (Solution Finder)
sla:
  freshness: Real-time (on register)
  availability: 99.9%

schema:
  solution_id:
    type: string
    primary_key: true
    pattern: "SOL-[0-9]{6}"
  
  name:
    type: string
    nullable: false
    unique: true  # No duplicate solution names
  
  problem_solved:
    type: string
    nullable: false
    foreign_key: Problem.name
  
  code_path:
    type: string
    nullable: false
    validation: "file must exist in repos/"
  
  confidence:
    type: numeric(2,2)
    range: [0.0, 1.0]
    test: "confidence should be 0.75+ for production use"
  
  usage_count:
    type: integer
    nullable: false
    default: 0
    test: "usage_count >= 0"
    test: "usage_count only increases"

quality_checks:
  - "All referenced code paths must exist"
  - "Confidence scores must be justified (>1 usage or scored)"
  - "Solutions should not overlap (check for duplication)"
```

---

## 4. Data Pipeline Design

### Pipeline 1: Real-Time Supabase → Lake

**Frequency:** Continuous (CDC-based)  
**Tool:** Fivetran (managed) or Airbyte (self-hosted)

```
Supabase PostgreSQL
    ↓ (WAL / logical replication)
Fivetran Connector
    ↓ (incremental + full-refresh)
S3 data lake (Parquet files)
    ├─ ventures_raw/
    │  └─ 2026-09-19/ (date partitioned)
    │     ├─ ventures.parquet
    │     └─ _metadata (checksum, row count)
    ├─ metrics_raw/
    └─ ...

SLA: Data appears in S3 <5 min after write
Cost: ~$1K/month (Fivetran managed)
```

**Configuration (Fivetran):**
```json
{
  "connector_type": "postgres",
  "database": "company_brain",
  "source": "aipehhzlsmfxxzwceppd.supabase.co",
  "port": 5432,
  "tables": [
    "ventures",
    "capabilities", 
    "agents",
    "metrics",
    "call_logs",
    "orders",
    "projects",
    "properties"
  ],
  "sync_mode": "CDC",  // Change Data Capture
  "schedule": "continuous",
  "destination": "s3",
  "s3_bucket": "company-brain-datalake",
  "s3_prefix": "raw/",
  "file_format": "parquet",
  "partitioning": [
    {"column": "_fivetran_synced", "type": "date"}
  ]
}
```

### Pipeline 2: Lake → Warehouse (dbt)

**Frequency:** Hourly  
**Tool:** dbt Core (Git-based, CI/CD)

```yaml
# dbt/models/staging/stg_ventures.sql
{{ config(
  materialized='table',
  unique_id='venture_id'
) }}

SELECT
  id as venture_id,
  name,
  sector,
  readiness_percent,
  revenue_ytd,
  created_at,
  updated_at,
  _fivetran_synced as data_loaded_at
FROM {{ source('raw', 'ventures') }}
WHERE _fivetran_deleted = false

-- Tests
{% if execute %}
  {{ assert_unique('venture_id') }}
  {{ assert_not_null('venture_id') }}
  {{ assert_not_null('sector') }}
  {{ assert_accepted_values('sector', VALID_SECTORS) }}
{% endif %}
```

**Transformation Logic:**
```
Raw (Supabase) → Staging (normalize) → Marts (denormalize)

Staging layer:
├─ stg_ventures (normalize venture schema)
├─ stg_metrics (denormalize metrics)
└─ stg_agents (normalize agent metadata)

Mart layer (dimensional model):
├─ ventures_fact (fact table: venture metrics over time)
├─ sector_dim (dimension: sector details)
├─ agent_dim (dimension: agent capabilities)
└─ date_dim (dimension: time-based joins)
```

**Monitoring + Quality:**
```yaml
# dbt/tests/contracts/ventures_contract.sql
SELECT * FROM {{ ref('stg_ventures') }}
WHERE
  venture_id IS NULL OR
  sector NOT IN ('LT', 'OPS', 'CON', 'RE', ...) OR
  readiness_percent < 0 OR readiness_percent > 100 OR
  revenue_ytd < 0 OR revenue_ytd > 1000000
```

### Pipeline 3: Warehouse → Analytics (VEX)

**Frequency:** Real-time (via Snowflake or BigQuery API)  
**Tool:** Native SQL querying + caching

```typescript
// vex/src/api/analytics/portfolio.ts
import { createClient } from '@supabase/supabase-js';

export async function getPortfolioMetrics() {
  // Query Snowflake via SQL + cache 1h
  const { data } = await snowflake.query(`
    SELECT
      COUNT(*) as total_ventures,
      AVG(readiness_percent) as avg_readiness,
      SUM(revenue_ytd) as total_revenue,
      COUNT(CASE WHEN readiness_percent >= 75 THEN 1 END) as ready_count,
      ARRAY_AGG(DISTINCT sector) as sectors
    FROM ventures_mart
    WHERE is_current = true
  `);
  
  return data[0];
}
```

---

## 5. Data Quality Framework

### Great Expectations Configuration

```yaml
# data_quality/suites/ventures_quality.yml

expectations:
  - expectation_type: "table.row_count.between"
    kwargs:
      min_value: 780
      max_value: 800
    meta:
      reason: "Should have 789 ± 11 ventures"

  - expectation_type: "column.values.match_regex"
    column: venture_id
    kwargs:
      regex: "^[A-Z]{1,3}-\\d{3,6}$"
    meta:
      reason: "Venture IDs must match pattern (LT-005, OPS-001, etc.)"

  - expectation_type: "column.values.in_set"
    column: sector
    kwargs:
      value_set: ["LT", "OPS", "CON", "RE", ...]  # 35 values
    meta:
      reason: "Sector must be in approved list"

  - expectation_type: "column.values.between"
    column: readiness_percent
    kwargs:
      min_value: 0.0
      max_value: 100.0
    meta:
      reason: "Readiness must be 0-100%"

  - expectation_type: "table.row_count.to_be_between"
    table: metrics
    kwargs:
      min_value: 18000  # 789 ventures × 23 KPIs
    meta:
      reason: "Should have complete metric set"

  - expectation_type: "table.columns_to_exist"
    kwargs:
      column_list: ["venture_id", "name", "sector", "readiness_percent", "revenue_ytd"]
    meta:
      reason: "Critical columns must always exist"
```

**Monitoring + Alerting:**
```python
# Great Expectations checkpoint
def run_quality_checks():
  suite = context.get_expectation_suite("ventures_quality")
  validation = context.run_validation_operator(
    "action_list_operator",
    assets_to_validate=[df],
    expectation_suite_name="ventures_quality"
  )
  
  if not validation['success']:
    send_alert({
      'channel': 'slack',
      'severity': 'high',
      'message': f"Data quality check failed: {validation['results']}"
    })
```

---

## 6. Data Governance

### Data Catalog (DataHub)

```yaml
# datahub/ingest.yml

entities:
  - type: "dataset"
    name: "ventures_mart"
    source: "snowflake://company_brain.public.ventures_mart"
    owner: "Product Team"
    domain: "Holdings"
    description: "Master venture dimension with current attributes"
    
    fields:
      - name: venture_id
        type: string
        description: "Unique venture ID"
        
      - name: readiness_percent
        type: numeric
        description: "Calculated readiness score (0-100)"
        lineage: "computed from 12 sub-scores"
        
    quality_metrics:
      freshness: "< 1 hour"
      completeness: "100% non-null"
      accuracy: "validated by contracts"
    
    usage_stats:
      accessed_by: ["VEX", "BI tool", "Reports"]
      weekly_queries: 1250

  - type: "lineage"
    upstream: ["supabase://ventures"]
    transform: "dbt stg_ventures → ventures_mart"
    downstream: ["analytics.portfolio_overview"]
    
  - type: "policy"
    pii_fields: ["name", "email"]  # Mark PII
    access_level: "internal"
    compliance: ["GDPR", "SOC2"]
```

### Access Control (Least Privilege)

```yaml
# Access policies
roles:
  - name: "data_analyst"
    permissions:
      - SELECT on ventures_mart
      - SELECT on metrics_mart
      - DENY on customer_pii
  
  - name: "data_engineer"
    permissions:
      - SELECT/INSERT/UPDATE on all raw tables
      - MODIFY dbt models
      - RUN Fivetran sync
  
  - name: "founder"
    permissions:
      - SELECT on ventures_mart
      - SELECT on analytics views
      - EXPORT reports
      - DENY on operational tables
```

---

## 7. Cost Optimization

### Storage Strategy

| Storage | Use Case | Cost | Retention |
|---------|----------|------|-----------|
| **S3 Standard** | Hot data (< 30d) | $0.023/GB | 30 days |
| **S3 Intelligent-Tiering** | Warm data (30–90d) | $0.0125/GB | 90 days |
| **S3 Glacier** | Cold backups (> 90d) | $0.004/GB | 1 year |
| **T7 Shield** | Local backup | One-time $180 | On-site |
| **Lacie** | Offsite backup | One-time $200 | Offsite |

**Estimated Monthly Cost:**
```
Raw data lake (S3):      800 GB × $0.023 = $18.40
Transformed (S3):       300 GB × $0.0125 = $3.75
Warehouse (Snowflake):  ~$500–$1,000 (compute + storage)
Fivetran (CDC):         ~$1,000
DataHub (catalog):      ~$200 (self-hosted)

TOTAL: ~$1,700–$2,200/month
SAVINGS vs. manual:     $5K+/month (reduced overhead)
```

### Cost Reduction Opportunities

1. **Partition data by time + sector** (reduce scan costs)
2. **Archive metrics > 1 year** to Glacier
3. **Use spot instances** for dbt transformations
4. **Implement query caching** in BI layer
5. **Compress Parquet files** (50%+ reduction)

---

## 8. Implementation Roadmap

### Week 1: Foundation
- [ ] Set up data contracts in YAML
- [ ] Deploy Fivetran connector (Supabase → S3)
- [ ] Create S3 bucket structure
- [ ] Cost: ~$1.2K (Fivetran setup + S3)

### Week 2: Transformation
- [ ] Set up dbt project
- [ ] Write staging layer models
- [ ] Implement Great Expectations
- [ ] Set up quality checks
- [ ] Cost: ~$300 (dbt CI/CD)

### Week 3: Warehouse
- [ ] Provision Snowflake account (or BigQuery)
- [ ] Load transformed data
- [ ] Create dimensional model
- [ ] Cost: ~$500 (first month warehouse)

### Week 4: Governance + Analytics
- [ ] Deploy DataHub catalog
- [ ] Wire VEX to warehouse
- [ ] Implement alerting
- [ ] Documentation + runbooks
- [ ] Cost: ~$200 (DataHub self-hosted)

**Total 4-week cost: ~$2.2K**

---

## 9. Success Metrics

| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| **Data freshness** | 24h (batch) | <5 min (real-time) | Week 1 |
| **Data quality** | Unknown | 100% contract compliance | Week 2 |
| **Query latency** | >10s | <1s | Week 3 |
| **Cost per query** | $0.25+ | <$0.01 | Week 3 |
| **Data lineage** | None | 100% tracked | Week 4 |
| **Analyst velocity** | Manual → 2h | Automated → 30 min | Week 4 |
| **Portfolio visibility** | 40% (VEX basic) | 100% (warehouse + BI) | Week 4 |

---

## 10. Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **Fivetran sync fails** | Data stale | Daily validation checks + Slack alerts |
| **dbt transformation breaks** | Bad data in warehouse | Comprehensive test coverage + CI/CD |
| **Schema changes** | Upstream breaks | Version control all schemas + backward compat tests |
| **Cost overruns** | Budget exceeded | Reserved instances + query monitoring + alerts |
| **Data breach (PII)** | Compliance violation | Row-level security + encryption + audit logs |

---

## Conclusion

**This is a professional data engineering platform ready to scale 789 ventures from manual data wrangling to real-time analytics.**

The foundation is 90% there (Supabase, Neo4j, Qdrant). This design connects the dots and adds governance, quality, and cost optimization.

**Next step:** Approve the design or modify it, then execute Week 1 (Fivetran + S3 setup).

