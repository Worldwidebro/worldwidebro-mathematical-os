---
name: CRM-QUICKSTART
title: CRM System Quick-Start Guide
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# CRM System Quick-Start Guide

## Goal
Unified visibility of remaining work across all ventures, contacts, and organizational structures. All systems (ClickUp, Supabase, Graphify) feeding into a single dashboard with real-time CRM pipeline status.

## Architecture
```
ClickUp Sales Pipeline          Supabase Ventures DB      GitHub Repos
  ├─ Lead Generation           ├─ 583 ventures           ├─ Owned repos
  ├─ Negotiations              ├─ 7 sectors              ├─ Capability matching
  └─ Closed Deals              └─ allocation targets     └─ Recommendation engine
         ↓                              ↓                       ↓
   ┌──────────────────────────────────────────────────────────────┐
   │         Dexter Dashboard (Plotly + HTML)                     │
   │  ├─ Allocation pie chart by sector                          │
   │  ├─ Risk heatmap (concentration + runway)                   │
   │  ├─ Deal stage visibility per venture                       │
   │  ├─ Task counts (leads → negotiations → closed)             │
   │  ├─ Ventures table with CRM + repos                         │
   │  └─ Stage control for portfolio management                  │
   └──────────────────────────────────────────────────────────────┘
           ↓
   Real-Time Outputs
   ├─ dexter_dashboard.html (interactive)
   ├─ Slack notifications (#hrms, #niche-mastery, etc)
   └─ Obsidian knowledge graph (via LightRAG)
```

## Setup (5 steps)

### 1. Set Environment Variables
```bash
export SUPABASE_URL="https://cyhzilqldouzgynacqpe.supabase.co"
export SUPABASE_KEY="<your-anon-key>"
export CLICKUP_API_TOKEN="<your-clickup-token>"
```

### 2. Install Dependencies
```bash
pip install requests pandas plotly numpy
```

### 3. Start Supabase Locally (Optional)
```bash
supabase start
# Then update SUPABASE_URL to http://localhost:54321 for local testing
```

### 4. Run Dashboard
```bash
python3 dexter_dashboard.py
```

### 5. Deploy Edge Function for Real-Time Sync
```bash
# Create ClickUp webhook listener to auto-sync tasks
supabase functions new clickup_webhook_sync

# Deploy to production
supabase functions deploy clickup_webhook_sync --project-ref <project-id>
```

## Dashboard Features

### Real-Time CRM Pipeline
Once ClickUp API token is set, dashboard automatically:
- Fetches 3 sales lists (Lead Gen, Negotiations, Closed Deals)
- Maps ClickUp tasks to ventures by sector/name
- Enriches ventures table with task counts
- Shows deal stage per venture (no_activity → lead_gen → negotiating → closed)

### Deal Stage Badges
| Badge | Color | Meaning |
|-------|-------|---------|
| closed | Green | Deal won, in closed_deals list |
| negotiating | Orange | Deal in negotiations |
| lead_gen | Blue | Prospect in lead generation |
| no_activity | Gray | No ClickUp tasks found |

### Interactive Features
- **Filter**: Search by name, sector, OR deal stage
- **Stage Control**: Update venture portfolio stage (ideation → mvp → beta → launch → growth)
- **Repos Panel**: View recommended owned repos per venture (GitHub-sourced, capability-matched)
- **Allocation**: Real-time capital allocation by sector

## Viewing Results

### HTML Dashboard
```bash
# After running dexter_dashboard.py, open in browser:
open dexter_dashboard.html
```

### Text Report
Dashboard prints summary to console:
- Portfolio overview (total ventures, capital, health)
- Sector breakdown (allocation %, venture counts, ROI)
- Backtest results (if backtest_results.json exists)
- Risk metrics

### Sample Output
```
📡 Loading ventures from Supabase...
✅ Loaded 583 ventures

📋 Loading ClickUp sales pipeline...
  ✓ lead_generation: 15 tasks
  ✓ negotiations: 8 tasks
  ✓ closed_deals: 12 tasks
✅ Loaded 35 CRM tasks
```

## Data Flow: ClickUp → Dashboard

### Current (Client-Side)
1. Dashboard queries ClickUp API directly
2. Maps tasks to ventures using sector + name matching
3. Stores in DataFrame for rendering

### Future (Real-Time via Supabase)
1. ClickUp webhook fires on task changes
2. Edge function processes webhook payload
3. Supabase stores in `clickup_tasks` table
4. Dashboard queries Supabase (faster, cached)

### Migration Path
```sql
-- Create table for synced ClickUp data
CREATE TABLE clickup_tasks (
  id TEXT PRIMARY KEY,
  list_id TEXT,
  name TEXT,
  status TEXT,
  venture_id UUID REFERENCES ventures(id),
  is_blocker BOOLEAN,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

-- Create deal pipeline status view
CREATE TABLE deal_pipeline_status (
  id UUID PRIMARY KEY,
  venture_id UUID UNIQUE,
  lead_count INTEGER,
  negotiation_count INTEGER,
  closed_count INTEGER,
  last_sync TIMESTAMP
);
```

## Supabase CLI Integration

### Local Development
```bash
# Start local PostgreSQL + API server
supabase start

# Set local URL
export SUPABASE_URL="http://localhost:54321"
export SUPABASE_KEY="<local-anon-key>"

# Run dashboard against local DB
python3 dexter_dashboard.py
```

### Deploy Changes
```bash
# Push new migrations to production
supabase db push --project-ref cyhzilqldouzgynacqpe

# Deploy edge functions
supabase functions deploy clickup_webhook_sync --project-ref cyhzilqldouzgynacqpe

# Set secrets for edge functions
supabase secrets set CLICKUP_API_TOKEN="<token>" --project-ref cyhzilqldouzgynacqpe
```

### Monitor Edge Function
```bash
supabase functions logs clickup_webhook_sync --project-ref cyhzilqldouzgynacqpe

# Example log output:
# 2026-05-16T12:45:23 Synced 3 new tasks from ClickUp
# 2026-05-16T12:45:24 Updated deal_pipeline_status for venture_id=xyz123
```

## Slack Integration

Dashboard sends real-time updates to Slack channels based on venture priority:

```python
# Auto-posts to venture channels
slack_send_message(
    channel="#hrms",  # Venture name mapped to channel
    message="HRMS | Task 42 | lead_generation | 15 total leads"
)
```

See `/Users/acebless/.claude/CLAUDE.md` for Slack configuration.

## ClickUp List Structure

### Sales Pipeline (Automated by Webhook)
- **Lead Generation** (901327165574) — Initial prospects, research phase
- **Negotiations** (901327165575) — Active discussions, demo scheduled
- **Closed Deals** (901327165576) — Won deals, revenue tracking

### Sector Lists (Manual Organization)
- Leads—Technology Tier 1, Leads—E-Commerce Tier 1, etc.
- Negotiations—Active Deals
- Closed Deals—Revenue

## Troubleshooting

### No ClickUp data showing?
1. Check `CLICKUP_API_TOKEN` is set: `echo $CLICKUP_API_TOKEN`
2. Verify token has access to workspace 9013677375
3. Check list IDs match your workspace (IDs shift if lists are recreated)
4. Look for "⚠️  ClickUp fetch error" in dashboard output

### Dashboard won't run?
```bash
# Check Python version
python3 --version  # Should be 3.9+

# Check dependencies
pip list | grep -E "pandas|plotly|requests"

# Verify Supabase connectivity
curl -H "apikey: $SUPABASE_KEY" $SUPABASE_URL/rest/v1/ventures?select=count
```

### Supabase migrations failing?
```bash
# Check local database state
supabase db ls  # List tables

# Reset to clean state (dev only!)
supabase db reset

# View migration logs
supabase db logs
```

## Next Steps

1. **Activate Slack Channel Posting** — Configure SLACK_BOT_TOKEN in edge function
2. **Enable Webhook Sync** — Deploy clickup_webhook_sync edge function
3. **Add Contacts Table** — Map ClickUp assignees to contacts in Supabase
4. **Real-Time Obs Dashboard** — Link dashboard to Obsidian via dataview
5. **Forecasting** — Integrate backtest results with ClickUp pipeline

## Files Reference
- **dexter_dashboard.py** — Main dashboard (854 lines, ClickUp integrated)
- **SUPABASE-CLI-INTEGRATION.md** — Supabase setup guide
- **TOOLS-REFERENCE.md** — Complete tool inventory
- **/.claude/CLAUDE.md** — Project-level instructions (Slack config, skills)

---

**Status**: CRM MVP ready. Dashboard pulls live data from Supabase + ClickUp. Real-time sync via edge function pending activation.
