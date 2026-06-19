-- Orchestrator run audit (apply after supabase-content-brain.sql)

create table if not exists public.gf_orchestrator_runs (
  id uuid primary key default gen_random_uuid(),
  venture_id text not null references public.gf_ventures(venture_id) on delete cascade,
  goal text not null,
  funnel_stage text,
  ok boolean not null default false,
  steps jsonb not null default '[]'::jsonb,
  outputs jsonb not null default '{}'::jsonb,
  errors jsonb not null default '[]'::jsonb,
  started_at timestamptz,
  finished_at timestamptz,
  created_at timestamptz not null default now()
);

create index if not exists idx_gf_orchestrator_venture on public.gf_orchestrator_runs(venture_id, created_at desc);

alter table public.gf_orchestrator_runs enable row level security;

create policy "gf_orchestrator_service_all" on public.gf_orchestrator_runs
  for all using (auth.role() = 'service_role');

comment on table public.gf_orchestrator_runs is 'Master orchestrator audit trail';
