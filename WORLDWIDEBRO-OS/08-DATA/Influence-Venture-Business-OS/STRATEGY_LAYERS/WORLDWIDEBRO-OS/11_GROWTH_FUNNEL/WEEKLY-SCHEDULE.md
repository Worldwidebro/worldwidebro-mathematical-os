# Weekly Funnel Operating System

Semi-autonomous **TOF → MOF → BOF** cycle. Same rhythm every week; each day has a fixed funnel function.

## Core loop

```
Sunday prep → Monday TOF seed → Tuesday amplify → Wed MOF educate
→ Thu MOF proof → Friday BOF push → Saturday optimize → repeat
```

## Day map

| Day | Focus | Funnel | Agent(s) | Cron (local) |
|-----|-------|--------|----------|--------------|
| **Mon** | Strategy + viral seeding | TOF heavy | Hook + TOF | 9:00 AM |
| **Tue** | Amplify winners | TOF → MOF bridge | Analytics + TOF | 10:00 AM |
| **Wed** | Education + showcase | MOF | MOF | 9:00 AM |
| **Thu** | Proof + case studies | MOF | MOF + CRM hook | 10:00 AM |
| **Fri** | Trust + conversion | BOF | BOF | 9:00 AM |
| **Sat** | Optimization | All | Analytics | 12:00 PM |
| **Sun** | Reset + prep | Next week | Weekly prep | 6:00 PM |

Machine-readable config: `REGISTRY/weekly-triggers.json`

## Run manually

```bash
# Today’s job (auto-detect weekday)
python3 WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/SCRIPTS/weekly_funnel_runner.py \
  --venture-id 1d84705c-8ebd-4c0c-83cf-cf383951b7bb

# Specific day
python3 WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/SCRIPTS/weekly_funnel_runner.py \
  --venture-id 1d84705c-8ebd-4c0c-83cf-cf383951b7bb --day monday

# Dry run (no writes)
python3 .../weekly_funnel_runner.py --venture-id UUID --day friday --dry-run
```

## Automation stack

| Layer | Tool | Role |
|-------|------|------|
| Scheduler | n8n cron | `WORKFLOWS/n8n-weekly-growth-engine.json` |
| Content brain | Supabase | `DATABASE/supabase-content-brain.sql` |
| Local fallback | SQLite | `DATA/content_brain.db` (auto if no Supabase env) |
| Generation | Python + PROMPTS | Stage scripts + hooks |
| Video | `venture_video_pipeline.py` | Optional `--render` on Mon/Wed/Fri |
| Posting | Buffer / Later / native APIs | See `WORKFLOWS/auto-posting.md` |

## Event triggers (beyond schedule)

| Event | Threshold | Action |
|-------|-----------|--------|
| TOF post viral | views ≥ 5000 | Generate MOF expansion (`event: tof_viral`) |
| MOF engagement | watch_time / visits high | Trigger BOF sequence (`event: mof_warm`) |
| New user success | CRM webhook | Generate case study (`event: user_success`) |
| Comment objections | BOF agent input | Friday objection posts |

Configure thresholds in `REGISTRY/weekly-triggers.json` → `event_triggers`.

## Supabase setup

1. Apply migration: `DATABASE/supabase-content-brain.sql` (Dashboard SQL or MCP `apply_migration`)
2. Set env for runner:

```bash
export SUPABASE_URL=https://YOUR_PROJECT.supabase.co
export SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
```

3. n8n: import weekly workflow + Supabase credentials

## n8n import

1. `WORKFLOWS/n8n-weekly-growth-engine.json` — 7 cron nodes → `weekly_funnel_runner.py`
2. `WORKFLOWS/n8n-tof-mof-bof.json` — on-demand venture intake
3. `WORKFLOWS/n8n-engagement-feedback-loop.json` — daily analytics pull

Edit `venture_id` default in n8n Set node or pass from Supabase `ventures` table.

## Outputs per day (targets)

### Monday — TOF
- 10 hook variations (keep top 5)
- 3 short-form video scripts
- 5–10 post drafts → `content_assets` queue

### Tuesday — TOF + MOF bridge
- Repost top 20% from Mon analytics
- 2 explainer posts + 1 case study teaser

### Wednesday — MOF
- 1 demo video script (+ optional render)
- 2 breakdown posts + 1 thread outline

### Thursday — MOF proof
- 2 case study drafts
- 1 comparison post

### Friday — BOF
- Pricing/value breakdown
- 2 testimonial posts + 1 offer post
- Landing spec delta → `publish/landing_page.spec.md`

### Saturday — Analytics
- Weekly report → `weekly_reports`
- Update `content_hooks` viral scores
- Archive losers, tag winners for reuse

### Sunday — Prep
- 20 hooks + 10 ideas + 5 video scripts for next week
- Pre-queue Monday TOF in `publish_queue`

## Related

- `OPERATING-RUNBOOK.md` — checklist style
- `README.md` — funnel folder layout
- `PROMPTS/` — agent prompts per stage
