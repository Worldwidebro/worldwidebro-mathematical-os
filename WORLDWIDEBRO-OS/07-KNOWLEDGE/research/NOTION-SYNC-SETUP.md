# Notion Sync Setup Guide

## Overview
The `sync_ventures_to_notion.py` script syncs all ventures from Supabase into your Notion Venture Portfolio database in real-time.

---

## Prerequisites

### 1. Ensure .env Has Real Credentials

Your `.env` file needs actual values:

```bash
# Required for Supabase
SUPABASE_URL=https://cyhzilqldouzgynacqpe.supabase.co
SUPABASE_KEY=<your_real_service_key>

# Required for Notion
NOTION_TOKEN=<your_real_notion_api_token>
```

**Get Supabase Service Key:**
1. Go to Supabase dashboard (cyhzilqldouzgynacqpe.supabase.co)
2. Settings → API
3. Copy "service_role" key (not anon key)

**Get Notion API Token:**
1. Go to https://www.notion.so/my-integrations
2. Create new integration named "AI Boss Holdings"
3. Copy the API token
4. Add to `.env` as `NOTION_TOKEN=ntn_...`

---

## Running the Sync

### Option 1: Direct Run
```bash
cd /Users/acebless/Documents
python3 sync_ventures_to_notion.py
```

### Option 2: Scheduled (Every 6 Hours)
```bash
# Add to crontab (crontab -e)
0 */6 * * * cd /Users/acebless/Documents && python3 sync_ventures_to_notion.py >> /tmp/notion_sync.log 2>&1
```

### Option 3: Manual from Terminal
```bash
! python3 /Users/acebless/Documents/sync_ventures_to_notion.py
```

---

## What It Does

| Step | Details |
|------|---------|
| **1. Connect** | Connects to Supabase and fetches all ventures |
| **2. Check Notion** | Queries existing entries in Notion portfolio |
| **3. Compare** | Matches ventures by name (create new / update existing) |
| **4. Sync** | Creates new entries or updates fields |
| **5. Report** | Shows created/updated/total counts |

---

## Field Mapping

| Supabase | Notion | Type |
|----------|--------|------|
| `name` | Venture Name | Title |
| `status` | Status | Select (Idea/Validation/MVP/Revenue/Growth) |
| `stage` | Stage | Select (Pre-Launch/MVP/Beta/Launch/Scale) |
| `revenue_ytd` | Revenue | Number (dollars) |
| `costs_mom` | Costs | Number (dollars) |
| `owner_id` | Owner | Text |
| `sector` | Sector | Text |
| `business_model` | ICP | Text |

---

## Expected Output

```
🔄 Starting Supabase → Notion sync...
📅 2026-06-10T00:45:00.123456

📥 Fetching ventures from Supabase...
✅ Found 712 ventures

🔍 Checking existing Notion entries...
✅ Found 0 existing Notion entries

  ✨ Created: Venture 001
  ✨ Created: Venture 002
  ✨ Created: Venture 003
  ...

==================================================
✅ Sync Complete!
   Created: 712
   Updated: 0
   Total: 712/712
==================================================
```

---

## Troubleshooting

### "supabase_url is required"
**Fix:** `.env` file not loaded or missing SUPABASE_URL

```bash
# Verify .env exists and has values
cat /Users/acebless/.env | grep SUPABASE
```

### "Invalid token" from Notion
**Fix:** NOTION_TOKEN is incorrect or expired

1. Check `.env` has correct token
2. Regenerate from https://www.notion.so/my-integrations
3. Update `.env` and try again

### "Sync Complete! Created: 0, Updated: 0"
**Possible causes:**
- Supabase ventures table is empty
- No ventures match the name in Notion
- All ventures already synced on previous run

---

## Next Steps

### Automate With Make.com
1. Create a webhook that calls this script every 6 hours
2. Post results to Slack with metrics

### Add More Databases
- **Deal Flow DB** ← from venture_decisions table
- **KPI Center DB** ← calculate from ventures metrics
- **Agent Registry DB** ← from agent assignments

### Monitor Syncs
Create a "Sync Logs" database in Notion to track:
- Last sync timestamp
- Ventures created
- Ventures updated
- Errors (if any)

---

## Database IDs (Reference)

```
NOTION_VENTURES_DB_ID = "c7c533f2c9824b80b6c0d1bba77a920d"
NOTION_DATA_SOURCE_ID = "3030288e-8138-4de4-8077-2618d4da44b2"
```

If you need to update these, find them in:
- Notion URL: `https://app.notion.com/p/{DATABASE_ID}`
- Data source URLs: `collection://{DATA_SOURCE_ID}`
