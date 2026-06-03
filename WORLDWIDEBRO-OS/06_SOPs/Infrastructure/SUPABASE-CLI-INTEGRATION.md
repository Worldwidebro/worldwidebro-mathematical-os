# Supabase CLI Integration for CRM Architecture

## Overview
The Supabase CLI enables local development, schema management, migrations, and edge function deployment for your CRM system. It bridges your local development environment with production infrastructure.

## 1. Local Development Workflow

```bash
# Start local Supabase stack (PostgreSQL + API + Auth + Storage)
supabase start

# Set environment variables for local development
export SUPABASE_URL="http://localhost:54321"
export SUPABASE_KEY="<local-anon-key-from-output>"

# Run dashboard locally
python dexter_dashboard.py
```

This gives you a full Supabase environment locally before deploying to production.

## 2. Schema Management & Migrations

### Create migration for CRM tables
```bash
# Auto-generate migration from your schema changes
supabase migration new add_crm_task_sync

# Edit the migration file in supabase/migrations/
# Example: add tasks table, task_blockers, deal_pipeline_status
```

### Apply migrations locally
```bash
supabase db push  # Push all pending migrations to local stack
```

### Deploy to production
```bash
supabase db push --project-ref <project-id>  # Uses SUPABASE_PROJECT_ID env var
```

## 3. Edge Functions for Real-Time Sync

Deploy ClickUp-to-Supabase sync as an edge function:

```bash
# Create edge function for ClickUp webhook listener
supabase functions new clickup_webhook_sync

# Deploy to production
supabase functions deploy clickup_webhook_sync --project-ref <project-id>
```

Edge functions enable:
- Real-time task updates from ClickUp
- Webhook ingestion from ClickUp API
- Automated sync without polling
- Serverless execution (free tier: 600k requests/month)

## 4. Environment Management

### Local vs. Production
```bash
# Development (local)
supabase start  # Runs on localhost:54321

# Staging (Supabase project)
supabase db push --project-ref staging-project

# Production
supabase db push --project-ref prod-project
```

### Secrets Management
```bash
# Set secrets for edge functions
supabase secrets set CLICKUP_API_TOKEN="<token>" --project-ref <project-id>

# Use in edge functions via Deno.env.get()
const token = Deno.env.get("CLICKUP_API_TOKEN");
```

## 5. Integration with Dashboard

The CRM dashboard workflow:
1. **Local Development**: `supabase start` → `python dexter_dashboard.py`
2. **Schema Evolution**: Create migrations → Test locally → Deploy to staging
3. **Real-Time Sync**: ClickUp webhook → Edge function → Supabase → Dashboard
4. **Monitoring**: Use Supabase dashboard logs to debug edge function issues

## 6. ClickUp-to-Supabase Schema Design

### New tables for CRM
```sql
-- Store ClickUp tasks synced in real-time
CREATE TABLE clickup_tasks (
  id TEXT PRIMARY KEY,
  list_id TEXT,
  name TEXT,
  status TEXT,
  priority TEXT,
  assignee_id TEXT,
  venture_id UUID,  -- FK to ventures table
  is_blocker BOOLEAN,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

-- Track deal pipeline stage per venture
CREATE TABLE deal_pipeline_status (
  id UUID PRIMARY KEY,
  venture_id UUID UNIQUE REFERENCES ventures(id),
  lead_count INTEGER,
  negotiation_count INTEGER,
  closed_count INTEGER,
  last_sync TIMESTAMP
);
```

## 7. Quick Start Commands

```bash
# Initialize Supabase in your project (if not done)
supabase init

# Start local development
supabase start

# Create and push migration
supabase migration new <name>
supabase db push

# Check local database
supabase db pull  # Export schema from production to track changes

# Deploy edge function
supabase functions deploy

# View logs
supabase functions logs <function-name> --project-ref <project-id>
```

## Benefits for Your CRM

1. **Local Testing**: Develop without impacting production
2. **Version Control**: Migrations stored in git for collaboration
3. **Real-Time Sync**: Edge functions auto-sync ClickUp → Dashboard
4. **Type Safety**: Generate TypeScript types from Supabase schema
5. **Reproducible Deployments**: Same schema everywhere (local→staging→prod)

## Next: Update dexter_dashboard.py to consume synced ClickUp data

Once migrations are deployed and webhook sync is live:
```python
# Dashboard will query clickup_tasks and deal_pipeline_status tables
# No more client-side API calls; everything flows through Supabase
```
