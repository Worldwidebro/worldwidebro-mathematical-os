-- Growth Funnel Content Brain (Supabase / Postgres)
-- Apply via Supabase Dashboard SQL editor or: supabase db push / MCP apply_migration
-- RLS enabled; service_role bypasses for automation. Authenticated users scoped by venture membership.

-- Extensions
create extension if not exists "pgcrypto";

-- ─── Core ventures ─────────────────────────────────────────────
create table if not exists public.gf_ventures (
  id uuid primary key default gen_random_uuid(),
  venture_id text not null unique,
  venture_code text,
  venture_name text not null,
  sector text,
  config jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- ─── Hooks library (content brain) ───────────────────────────
create table if not exists public.gf_content_hooks (
  id uuid primary key default gen_random_uuid(),
  venture_id text not null references public.gf_ventures(venture_id) on delete cascade,
  hook_text text not null,
  funnel_stage text not null default 'tof' check (funnel_stage in ('tof', 'mof', 'bof', 'foundation')),
  source_day text,
  viral_score numeric(5,2) default 0,
  conversion_score numeric(5,2) default 0,
  used_count int not null default 0,
  status text not null default 'draft' check (status in ('draft', 'active', 'winner', 'archived')),
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create index if not exists idx_gf_hooks_venture on public.gf_content_hooks(venture_id);
create index if not exists idx_gf_hooks_status on public.gf_content_hooks(status, viral_score desc);

-- ─── Content assets (posts, scripts, videos) ─────────────────
create table if not exists public.gf_content_assets (
  id uuid primary key default gen_random_uuid(),
  venture_id text not null references public.gf_ventures(venture_id) on delete cascade,
  funnel_stage text not null check (funnel_stage in ('tof', 'mof', 'bof', 'foundation', 'prep')),
  format text not null default 'post' check (format in ('post', 'short_video', 'carousel', 'thread', 'case_study', 'landing_delta', 'script_json')),
  title text,
  hook text,
  body text,
  script_json jsonb,
  platform text,
  day_of_week text,
  status text not null default 'draft' check (status in (
    'draft', 'queued', 'scheduled', 'published', 'winner', 'archived'
  )),
  scheduled_for timestamptz,
  published_at timestamptz,
  parent_asset_id uuid references public.gf_content_assets(id),
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists idx_gf_assets_venture_stage on public.gf_content_assets(venture_id, funnel_stage, status);
create index if not exists idx_gf_assets_scheduled on public.gf_content_assets(scheduled_for) where status = 'scheduled';

-- ─── Analytics snapshots (24h feedback loop) ─────────────────
create table if not exists public.gf_analytics_snapshots (
  id uuid primary key default gen_random_uuid(),
  asset_id uuid not null references public.gf_content_assets(id) on delete cascade,
  venture_id text not null,
  platform text not null,
  views int default 0,
  shares int default 0,
  saves int default 0,
  comments int default 0,
  watch_time_sec int default 0,
  ctr numeric(8,4) default 0,
  site_visits int default 0,
  email_signups int default 0,
  viral_score numeric(5,2) default 0,
  conversion_score numeric(5,2) default 0,
  recorded_at timestamptz not null default now()
);

create index if not exists idx_gf_analytics_asset on public.gf_analytics_snapshots(asset_id, recorded_at desc);

-- ─── Publish queue (n8n / scheduler handoff) ─────────────────
create table if not exists public.gf_publish_queue (
  id uuid primary key default gen_random_uuid(),
  venture_id text not null references public.gf_ventures(venture_id) on delete cascade,
  asset_id uuid references public.gf_content_assets(id) on delete set null,
  funnel_stage text not null,
  platform text not null default 'youtube_shorts',
  payload jsonb not null default '{}'::jsonb,
  status text not null default 'ready_for_review' check (status in (
    'ready_for_review', 'approved', 'scheduled', 'posted', 'failed'
  )),
  scheduled_for timestamptz,
  posted_at timestamptz,
  error text,
  created_at timestamptz not null default now()
);

create index if not exists idx_gf_publish_status on public.gf_publish_queue(status, scheduled_for);

-- ─── Funnel events (CRM / webhooks) ──────────────────────────
create table if not exists public.gf_funnel_events (
  id uuid primary key default gen_random_uuid(),
  venture_id text not null,
  event_type text not null,
  payload jsonb not null default '{}'::jsonb,
  processed boolean not null default false,
  triggered_at timestamptz not null default now()
);

create index if not exists idx_gf_events_unprocessed on public.gf_funnel_events(processed, triggered_at) where not processed;

-- ─── Weekly reports (Saturday brain update) ──────────────────
create table if not exists public.gf_weekly_reports (
  id uuid primary key default gen_random_uuid(),
  venture_id text not null references public.gf_ventures(venture_id) on delete cascade,
  week_start date not null,
  report jsonb not null,
  created_at timestamptz not null default now(),
  unique (venture_id, week_start)
);

-- ─── Updated_at trigger ──────────────────────────────────────
create or replace function public.gf_set_updated_at()
returns trigger language plpgsql as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists gf_ventures_updated on public.gf_ventures;
create trigger gf_ventures_updated before update on public.gf_ventures
  for each row execute function public.gf_set_updated_at();

drop trigger if exists gf_assets_updated on public.gf_content_assets;
create trigger gf_assets_updated before update on public.gf_content_assets
  for each row execute function public.gf_set_updated_at();

-- ─── RLS ─────────────────────────────────────────────────────
alter table public.gf_ventures enable row level security;
alter table public.gf_content_hooks enable row level security;
alter table public.gf_content_assets enable row level security;
alter table public.gf_analytics_snapshots enable row level security;
alter table public.gf_publish_queue enable row level security;
alter table public.gf_funnel_events enable row level security;
alter table public.gf_weekly_reports enable row level security;

-- Service role (automation) — full access via bypass RLS when using service key
-- Authenticated: read own venture if app_metadata.venture_ids contains venture_id
create policy "gf_ventures_service_all" on public.gf_ventures
  for all using (auth.role() = 'service_role');

create policy "gf_hooks_service_all" on public.gf_content_hooks
  for all using (auth.role() = 'service_role');

create policy "gf_assets_service_all" on public.gf_content_assets
  for all using (auth.role() = 'service_role');

create policy "gf_analytics_service_all" on public.gf_analytics_snapshots
  for all using (auth.role() = 'service_role');

create policy "gf_publish_service_all" on public.gf_publish_queue
  for all using (auth.role() = 'service_role');

create policy "gf_events_service_all" on public.gf_funnel_events
  for all using (auth.role() = 'service_role');

create policy "gf_reports_service_all" on public.gf_weekly_reports
  for all using (auth.role() = 'service_role');

-- Optional: authenticated read if venture in JWT app_metadata.venture_ids array
create policy "gf_assets_auth_read" on public.gf_content_assets
  for select using (
    auth.role() = 'authenticated'
    and venture_id = any(
      coalesce(
        (auth.jwt() -> 'app_metadata' -> 'venture_ids')::jsonb,
        '[]'::jsonb
      )::text[]
    )
  );

comment on table public.gf_content_hooks is 'Viral hook library — content brain';
comment on table public.gf_content_assets is 'All funnel content assets by stage and format';
comment on table public.gf_publish_queue is 'Handoff to Buffer/Later/native schedulers';
