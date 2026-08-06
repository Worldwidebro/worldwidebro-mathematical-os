---
name: LIGHTRAG-SUPABASE-SETUP
title: LightRAG → Supabase Setup Guide
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# LightRAG → Supabase Setup Guide

**Status**: Ready to connect  
**Date**: May 14, 2026  
**Prerequisites**: Supabase project created with credentials

---

## Step 1: Get Supabase Credentials

From your Supabase project dashboard (https://supabase.com/dashboard):

1. Go to **Project Settings** → **API**
2. Copy **Project URL** (format: `https://[project-id].supabase.co`)
3. Copy **Anon Key** (public, can be shared in frontend code)

---

## Step 2: Set Environment Variables

```bash
export SUPABASE_URL="https://[your-project].supabase.co"
export SUPABASE_KEY="[your-anon-key]"
```

Or add to `.env`:
```
SUPABASE_URL=https://[your-project].supabase.co
SUPABASE_KEY=[your-anon-key]
```

Then load in shell:
```bash
source .env
```

Verify:
```bash
echo $SUPABASE_URL
echo $SUPABASE_KEY
```

---

## Step 3: Apply Database Migration

Run the migration to create tables:

```bash
supabase migration new add_lightrag_graph_tables
# Then copy contents of migrations/add_lightrag_graph_tables.sql into the new migration
```

Or if using Supabase console directly:
1. Go to **SQL Editor** in Supabase dashboard
2. Create new query
3. Paste contents of `migrations/add_lightrag_graph_tables.sql`
4. Run

---

## Step 4: Test Connection

Run the complete pipeline with real Supabase:

```bash
python3 /Users/acebless/Documents/lightrag_complete_pipeline.py
```

Expected output:
```
✅ Supabase ready: https://[project-id].supabase.co...
🚀 RAG Complete Pipeline Demo
📥 Processing: [document paths]
🔄 Syncing to Supabase...
✓ Entities Synced: [count]
✓ Relationships Synced: [count]
✓ Ventures Indexed: [count]
✅ RAG Pipeline Complete
```

---

## Step 5: Verify Data in Supabase

In Supabase dashboard **Table Editor**:
1. Check `graph_entities` table — should see extracted entities
2. Check `graph_relationships` table — should see entity connections
3. Verify venture mappings are correct

---

## Troubleshooting

### "Supabase credentials not set"
- Environment variables not found
- Solution: Run `export SUPABASE_URL=...` and `export SUPABASE_KEY=...`

### "Connection refused"
- Project URL incorrect or project paused
- Solution: Verify SUPABASE_URL in dashboard, ensure project is running

### "INSERT permission denied"
- Service role doesn't have write access
- Solution: Go to Supabase dashboard → **Auth** → **Policies** → set RLS policies

---

## Files Ready for Sync

Once Supabase is connected, these will automatically sync:

- **lightrag_complete_pipeline.py** — Master pipeline (preprocess → extract → sync → query)
- **lightrag_supabase_sync.py** — Handles entity/relationship persistence
- **lightrag_agent_queries.py** — Query interface for CEO/CFO/CTO agents

---

## Next: Phase 2 (May 20-21)

Document ingestion with real Week 0 data:

```bash
python3 /Users/acebless/Documents/lightrag_complete_pipeline.py
```

Will automatically:
1. Read documents from Week 0 (CSV, markdown, JSON)
2. Preprocess via RAG-Anything alternative
3. Extract entities via LightRAG
4. Sync to Supabase
5. Index by venture

---

**Ready to proceed once Supabase credentials are available.**
