# Family Office Operating System

**Scope:** Capital allocation, OPCO governance, and venture funding orchestration across 38 sectors  
**Status:** Framework complete, ready for deployment  
**Generated:** 2026-07-28

---

## Overview

The Family Office Operating System (Family OS) provides capital routing, allocation formulas, and governance structures for Worldwidebro Holdings' portfolio of 1,200+ ventures organized across 38 operational companies (OPCOs).

**Core Principles:**
1. **Capital flows to ventures; ventures flow to OPCOs; OPCOs flow to the holding company**
2. **Allocation = formula-based, transparent, executable**
3. **Every allocation decision generates an audit trail**
4. **OPCOs are economic units; ventures are deployment units**

---

## Key Components

### 1. Capital Allocation Formula
- **Entry Point:** `CAPITAL-ALLOCATION.md`
- **Contains:** Allocation thresholds, decision criteria, ROI calculations
- **Updated:** Weekly via Supabase `capital_decisions` table

### 2. OPCO Structure
- **Entry Point:** `OPCO-STRUCTURE.md`
- **Contains:** 38 OPCOs, 7 economic layers, folder templates
- **References:** Source taxonomy in `/Documents/OPCO_SECTORS_38.md`

### 3. Database Schema
- **Location:** `supabase/migrations/`
- **Tables:**
  - `opco_capital_allocations` — Approved capital by OPCO (weekly snapshots)
  - `capital_deployment_log` — Actual venture deployments with ROI tracking
  - `capital_decisions` — Decision log with reasoning and audit trail

### 4. Agent Instructions
- **Entry Point:** `AGENTS.md`
- **Contains:** OPCO orchestrator agent prompts, approval workflows
- **Scope:** Autonomous capital decisions (< $100K), human approval ($100K–$1M+)

---

## Capital Routing Architecture

```
Holding Company Capital Pool ($500M)
        ↓
Weekly Allocation (Monday 6am UTC)
        ├→ Tier 1 OPCOs (27% = $135M) — SaaS, Finance, Commerce
        ├→ Tier 2 OPCOs (21% = $105M) — Education, Knowledge, Training
        ├→ Tier 3 OPCOs (18% = $90M)  — Environment, Government, Consulting
        ├→ Reserve Pool (15% = $75M)  — Emergencies, pivots, M&A
        └→ Strategic Pool (19% = $95M) — Cross-OPCO initiatives, infrastructure
        ↓
Per-OPCO Real-Time Deployment Decisions
        ├→ Auto-approve ($0–$100K) → Log only
        ├→ OPCO lead approval ($100K–$1M) → 2-hour SLA
        └→ Board approval ($1M+) → 24-hour SLA
        ↓
Venture Deployment (atomically)
        ├→ Stripe webhook (payment confirmation)
        ├→ Supabase insert (capital_deployment_log)
        ├→ Neo4j update (venture node, funded=true)
        └→ Audit log (complete trace)
```

---

## Data Flow & Audit Trail

**Field Definitions:**

### opco_capital_allocations
- `id` (UUID): Unique allocation record
- `opco_name` (TEXT): OPCO identifier (e.g., "OPCO-SaaS", "OPCO-Construction")
- `allocation_date` (DATE): When funds became available (YYYY-MM-DD)
- `approved_amount` (DECIMAL): Total allocated in USD
- `allocated_amount` (DECIMAL): Amount actually deployed (may be < approved_amount)
- `status` (TEXT): 'pending' | 'approved' | 'deployed' | 'returned'
- `approved_by` (TEXT): User or agent ID who approved
- `approval_date` (TIMESTAMP): When approval occurred (ISO8601)
- `created_at` (TIMESTAMP): Record creation time (DEFAULT NOW())

### capital_deployment_log
- `id` (UUID): Unique deployment record
- `opco_name` (TEXT): OPCO deploying capital
- `venture_id` (TEXT): Venture ID in format {SECTOR}-{NUMBER} (e.g., "SaaS-042")
- `amount_deployed` (DECIMAL): Funds deployed in USD
- `deployment_date` (DATE): Deployment date (YYYY-MM-DD)
- `predicted_roi_pct` (DECIMAL): Expected ROI % (0–100)
- `actual_roi_pct` (DECIMAL): Observed ROI % after outcome (NULL until final)
- `formula_used` (TEXT): Which allocation formula generated this deployment
- `created_at` (TIMESTAMP): When deployment was recorded

### capital_decisions
- `id` (UUID): Unique decision record
- `decision_type` (TEXT): 'allocation' | 'deployment' | 'rebalance'
- `opco_name` (TEXT): OPCO affected
- `amount` (DECIMAL): Amount in USD
- `decision_maker` (TEXT): Agent ID or user ID
- `decision_date` (TIMESTAMP): When decision was made (ISO8601)
- `reasoning` (TEXT): JSON-serialized decision reasoning trace
- `approval_status` (TEXT): 'auto' | 'pending' | 'approved' | 'rejected'
- `created_at` (TIMESTAMP): Record creation time

---

## Allocation Formulas

### Tier 1 OPCOs (27% of pool)
**Eligibility:** Mature OPCOs with 90%+ deployment rate and 15%+ ROI track record

**OPCOs:** SaaS, Finance, Commerce, Investment

**Formula:**
```
Tier1_Allocation = (Total_Pool × 0.27) × (AVG_ROI / 0.15) × Deployment_Velocity
```

### Tier 2 OPCOs (21% of pool)
**Eligibility:** Growth-stage OPCOs with 70%+ deployment rate and 10%+ ROI

**OPCOs:** Education, Knowledge, Training, Data, Technology

**Formula:**
```
Tier2_Allocation = (Total_Pool × 0.21) × (AVG_ROI / 0.10) × min(Deployment_Velocity, 1.2)
```

### Tier 3 OPCOs (18% of pool)
**Eligibility:** Early-stage OPCOs with 50%+ deployment rate

**OPCOs:** Environment, Government, Consulting, Security, Healthcare

**Formula:**
```
Tier3_Allocation = (Total_Pool × 0.18) × (1 + Growth_Rate) × min(Deployment_Velocity, 1.0)
```

---

## Governance & Approval Workflows

**Approval Thresholds (per deployment):**
- **< $100K:** Auto-approved (logged, no human required)
- **$100K–$1M:** OPCO lead approval (async, 2-hour SLA)
- **$1M+:** Board approval (sync, 24-hour SLA)

**Re-allocation Cadence:**
- **Weekly (Mondays 6am UTC):** Adjust allocations based on deployment velocity
- **Monthly (1st of month):** Rebalance based on realized ROI performance
- **Quarterly (1st of quarter):** Strategic review, tier adjustments

**Guardrails:**
- No OPCO may deploy > 50% of its quarterly allocation in one week
- Total pool drawdown capped at 70% per month (reserve 30% for emergencies)
- Agent approval confidence must be > 60% (else escalate to human)

---

## Integration Points

### Neo4j (Graph Database)
- Stores OPCO hierarchy, agent relationships, venture nodes
- Queries: OPCO → ventures → deployment outcomes
- Updated real-time on deployment confirmation

### Supabase (Transactional)
- Records: `opco_capital_allocations`, `capital_deployment_log`, `capital_decisions`
- Real-time subscriptions for dashboard updates
- Audit-trail immutable (no updates, only inserts)

### Stripe (Payments)
- Webhooks trigger on deployment confirmation
- Payment receipts logged to `capital_decisions` reasoning field
- Failed payments block venture deployment

### Langfuse (Observability)
- Tracks agent decision reasoning in `capital_decisions.reasoning`
- Compares `predicted_roi_pct` vs `actual_roi_pct` for continuous improvement

---

## Dashboards & Observability

### Key Metrics
- **OPCO Capital Velocity:** $/week per OPCO (target: 80%+ of allocated)
- **Approval Queue Time:** avg 2h, 95th percentile < 6h
- **Deployment Success Rate:** target 95%+ (payment confirmed + Neo4j updated)
- **ROI Forecast vs Actual:** monthly reconciliation, forecast error tracking

### Alerts
- Capital pool running low (< 15% remain)
- Approval SLA breach (2h or 24h depending on tier)
- Deployment failure (Stripe webhook timeout or payment decline)
- Anomalous decision (agent confidence < 60%)
- OPCO over-velocity (> 50% quarterly allocation in one week)

---

## Quick Start

### 1. Initialize Database
```bash
supabase db push --linked
```

### 2. Load OPCO Allocations
```bash
node scripts/seed-opco-allocations.js
```

### 3. Deploy Dashboard
```bash
npm run deploy:family-office-os
```

### 4. Configure Agents
```bash
node scripts/register-opco-agents.js
```

---

## Files in This Directory

| File | Purpose |
|------|---------|
| `README.md` | This file — overview, data schema, governance |
| `CAPITAL-ALLOCATION.md` | Detailed allocation formulas, thresholds, decision trees |
| `OPCO-STRUCTURE.md` | 38 OPCOs, economic layers, folder templates, governance |
| `AGENTS.md` | Agent instructions, approval workflows, decision prompts |
| `supabase/migrations/001_opco_capital_allocations.sql` | Create capital allocations table |
| `supabase/migrations/002_capital_deployment_log.sql` | Create deployment log table |
| `supabase/migrations/003_capital_decisions.sql` | Create decisions table with audit trail |

---

## Support & Documentation

- **Governance & OPCO Hierarchy:** See `OPCO-STRUCTURE.md`
- **Agent Decision Logic:** See `AGENTS.md`
- **Database Schemas:** See `supabase/migrations/`
- **Allocation Mathematics:** See `CAPITAL-ALLOCATION.md`
- **Source Sector Taxonomy:** `/Documents/OPCO_SECTORS_38.md`

---

**Version:** 1.0 (Framework Ready)  
**Generated:** 2026-07-28  
**Status:** Ready for Supabase deployment and agent integration
