---
name: airtable-dashboard-setup
type: Command Center Implementation Guide
date: 2026-06-18
data_source: VENTURE_INVENTORY_MASTER.csv
---

# Airtable Dashboard Setup Blueprint

**Purpose:** Single command center for tracking 704 ventures across 18 OPCOs

**Timeline:** 3-5 days to build
**Cost:** $120/month (Airtable Pro)
**Data source:** VENTURE_INVENTORY_MASTER.csv

---

## Step 1: Create Workspace

1. Go to airtable.com → Create workspace "Worldwidebro Portfolio"
2. Create base "Ventures"
3. Delete default table, import VENTURE_INVENTORY_MASTER.csv

---

## Step 2: Configure Fields

**Core Fields:**
- venture_id (text, primary)
- venture_name (text)
- opco (select: 18 options)
- owner (text)
- status (select: Idea, Research, Building, Launching, Operating, Scaling)
- revenue_ytd (currency, USD)
- monthly_burn (currency, USD)
- priority (select: HIGH, MEDIUM, LOW)
- 90day_potential (currency, formula)
- team_size (number, 0-10)
- last_updated (date)
- notes (long text)

---

## Step 3: Create 5 Views

**View 1: Executive Dashboard**
- Filter: status = Operating OR Scaling
- Sort: revenue_ytd DESC
- Summary: Count (ventures), Sum (revenue), Avg (burn)
- Show: top 20 ventures

**View 2: OPCO Summary**
- Grouped by: opco
- Summary per group: Count, Sum(revenue), Avg(burn)
- Purpose: Portfolio health by OPCO

**View 3: Status Funnel**
- Grouped by: status (in order)
- Summary: Count ventures, Sum revenue at each stage
- Purpose: Pipeline progression

**View 4: Revenue Leaders**
- Filter: revenue_ytd > 0
- Sort: revenue_ytd DESC
- Show: top 20 with growth potential

**View 5: Red Flags**
- Filter: monthly_burn > revenue_ytd
- Sort: burn DESC
- Purpose: Intervention targets

---

## Step 4: Automation

**Slack Alerts:**
- When: status changes → "Operating"
- Send: "{venture} now operating. Owner: {owner}, Revenue: {revenue}"

**Weekly Digest (Monday 9am):**
- Red flags, new launches, top performers, OPCO stats
- Send to: CEO, CFO, COO

**Data Maintenance:**
- Weekly: Update revenue/burn for Operating ventures
- Monthly: Review statuses, update forecasts
- Quarterly: Full portfolio review (Keep/Scale/Sell/Pause/Archive)

---

## Step 5: Integration

Link to:
- Supabase (weekly export)
- ClickUp (venture tasks)
- Notion (embed Revenue Leaders view)
- Slack (alerts)

---

## Success Criteria

✅ All 704 ventures imported by end Week 2
✅ 5 views operational and filtering correctly
✅ Real-time revenue tracking live
✅ Slack alerts working
✅ Weekly digest automated

---

**Action:** Build this dashboard in Airtable using VENTURE_INVENTORY_MASTER.csv as data source
