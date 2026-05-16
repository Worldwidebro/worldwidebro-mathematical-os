# All Tools & Integrations Mentioned

## MCP Servers & APIs
- **ClickUp API** — Sales pipeline task management (27 lists, 5 folders, 2 spaces)
  - Lead Generation (901327165574)
  - Negotiations (901327165575)
  - Closed Deals (901327165576)
- **Supabase REST API** — Ventures & contacts database (583 ventures, 7 sectors)
- **Graphify** — Graph database queries for entity relationships
- **LightRAG** — Knowledge graph ingestion + Supabase sync (17 entities, 3 relationships)
- **GitHub REST API** — Owned repos, capability matching
- **BrowserOS MCP** — ClickUp OAuth, automated interaction

## CLI Tools
- **Supabase CLI** — Local development, migrations, edge functions, secrets management
  - `supabase start` — Local stack (PostgreSQL + API + Auth + Storage)
  - `supabase db push` — Deploy migrations
  - `supabase functions deploy` — Edge function deployment
  - `supabase secrets set` — Environment secrets

## Skills Activated
- `/planning-with-files` — Multi-step workflow tracking (auto-generates task_plan.md, findings.md, progress.md)
- `/everything-claude-code` — 71-file workflow patterns (parallel execution, permission minimization, context management, git safety)

## Libraries & Frameworks
- **Plotly** — Interactive dashboards (pie charts, heatmaps, scatter plots, tables)
- **Pandas** — Data analysis & ventures DataFrame
- **Requests** — HTTP client for Supabase + ClickUp APIs
- **Deno** — Edge function runtime (supabase functions)
- **SQLAlchemy** (implied) — Database ORM for migrations

## Infrastructure
- **Supabase Project** — cyhzilqldouzgynacqpe.supabase.co
- **ClickUp Workspace** — Antwuan Johns's Workspace (ID 9013677375)
- **Slack** — Real-time updates (#hrms, #niche-mastery, #graphify, #pitch-kit channels)
- **Obsidian** — Knowledge graph visualization + Dataview

## Integration Patterns
1. **CRM Pipeline Flow**: ClickUp tasks → Supabase ClickUp_tasks table → Dashboard
2. **Real-Time Sync**: ClickUp webhook → Supabase edge function → Stored in DB
3. **Dashboard Display**: Supabase ventures + ClickUp task enrichment → Plotly HTML
4. **Knowledge Graph**: LightRAG entities → Supabase sync → Obsidian Dataview

## Environment Variables
```
SUPABASE_URL=https://cyhzilqldouzgynacqpe.supabase.co
SUPABASE_KEY=<your-anon-key>
CLICKUP_API_TOKEN=<your-clickup-token>
```

## Current Integration Status
- ✅ Supabase ventures table queryable
- ✅ ClickUp sales pipeline accessible via API
- ✅ GitHub owned repos matched to ventures
- ✅ LightRAG + Obsidian synced
- ⏳ Real-time ClickUp → Supabase sync (via edge function)
- ⏳ Slack automation for blockers/milestones
