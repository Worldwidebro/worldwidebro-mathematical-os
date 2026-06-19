# DATA-FLOW-ARCHITECTURE.md
## How Data Moves Through Your System

**Purpose:** Complete data pipelines from sources through MCPs to outputs.

---

## THE MASTER FLOW

```
External Sources → MCPs (transform) → Supabase (store) → Agents (read/write) → Actions
```

---

## FINANCIAL DATA FLOW

```
Stripe API payments
    ↓ [Webhook]
Supabase.spending_transaction
    ↓ [KPI MCP, daily 6 AM]
Calculate: MRR = SUM(revenue) WHERE date > NOW() - INTERVAL '1 month'
    ↓
metrics_weekly table
    ↓ [Dashboard]
Financial Controller Agent reads
```

---

## DEAL SOURCING FLOW

```
Tavily web search → deal_research table
Crunchbase research → deal_research (enriched)
Deal-Flow MCP scoring → scored_deals table
HubSpot contact match → operator_assignment
Slack notification → Team sees opportunity
```

---

## CONTENT DISTRIBUTION FLOW

```
Raw video
    ↓ [Media MCP]
├─ Transcribe
├─ Extract clips
└─ Auto-subtitle
    ↓
content_pieces table (20+ pieces from 1 video)
    ↓
Buffer/Beehiiv/Twitter MCPs post
    ↓ [48-72 hours]
audience_metrics (engagement tracked)
    ↓ [KPI MCP daily]
Dashboard shows performance
```

---

## KNOWLEDGE FLOW

```
Research created
    ↓ [Stored in Supabase]
Qdrant MCP weekly reindex
    ↓
Vector embeddings created
    ↓
Research Agent queries semantically
    ↓
Returns: Top 5 relevant docs
```

---

## PORTFOLIO HEALTH FLOW

```
Company submits metrics (monthly)
    ↓
Supabase.portfolio_companies
    ↓ [Portfolio MCP, real-time]
Health score calculated
    ↓ [KPI MCP, daily]
metrics_weekly updated
    ↓
Portfolio Manager Agent reads
    ├─ If health < 6 months → Flag
    └─ If critical → Slack alert
```

---

## KEY TABLES (Supabase Schema)

```
spending_transaction
├─ id, date, amount, currency, customer_id
├─ indexed: date, amount

metrics_weekly
├─ week_of, revenue_mrr, followers, deals, agents_deployed
├─ indexed: week_of

content_pieces
├─ id, original_video_id, piece_type (clip, post, newsletter)
├─ platform, engagement_metrics
├─ indexed: original_video_id, platform

scored_deals
├─ id, company_name, score, operator_match, pipeline_stage
├─ indexed: score, operator_match

portfolio_companies
├─ id, name, revenue, burn_rate, runway_months, health_score
├─ indexed: health_score, runway_months

audience_metrics
├─ date, followers, open_rate, click_rate, reach, engagement
├─ indexed: date
```

---

## MCP DATA FLOW SUMMARY

| MCP | Source | Destination | Frequency | Criticality |
|-----|--------|-------------|-----------|------------|
| **Stripe** | Stripe API | spending_transaction | Real-time | Critical |
| **KPI** | Supabase tables | metrics_weekly | Daily 6 AM | Critical |
| **Portfolio** | portfolio_companies | Health scores | Real-time | Critical |
| **HubSpot** | HubSpot API | hubspot_contacts/deals | Hourly | Critical |
| **Deal-Flow** | scored_deals | Pipeline stages | Per deal | Critical |
| **Media** | Raw video | content_pieces | Per video | High |
| **Buffer/Beehiiv** | Scheduled posts | audience_metrics | Hourly | High |
| **Tavily** | Web search | deal_research | Continuous | Medium |
| **Qdrant** | knowledge docs | Vector embeddings | Weekly | Medium |
| **Slack** | All agents | Notifications | Real-time | High |

---

## VALIDATION & INTEGRITY

**Real-time checks:**
- Revenue amounts ≥ 0
- Scores 1-100
- Operators exist in HubSpot

**Weekly audits:**
- Data completeness
- Stripe ↔ Ledger reconciliation
- Outlier detection

**Failed validations → audit_log table → alert**

---

## SCALING (1M+ records/month by Year 1)

- Partition by date (metrics_weekly, content_pieces)
- Index on: venture_id, date, status
- Archive: >12 months → cold storage
- Cache: KPI dashboard via Redis (5-min TTL)

---

**Complete visibility = Data-driven decisions**

