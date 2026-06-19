# Product Growth Funnel System (TOF → MOF → BOF)

Reusable operating structure for **any venture**. Maps to existing `COMMERCIALS/` hubs and the Documents video pipeline (`venture_script_engine.py`, `venture_video_pipeline.py`).

## Control layer (master orchestrator)

All layers are coordinated by one entry point:

```bash
python3 MASTER_ORCHESTRATOR.py status
python3 MASTER_ORCHESTRATOR.py run --auto              # round-robin + today's stage
python3 MASTER_ORCHESTRATOR.py run --batch             # all ventures in registry
python3 MASTER_ORCHESTRATOR.py run --venture-id UUID --goal full_cycle --render --opus-clip
HIGGSFIELD_ENABLED=1 python3 MASTER_ORCHESTRATOR.py run --auto --render --higgsfield
```

See **`MEDIA-FACTORY-OS.md`** for the full five-layer architecture and n8n wiring.

## System flow

```
TARGET AUDIENCE (00_FOUNDATION/audience.md)
        ↓
BRAND IDENTITY (00_FOUNDATION/brand_identity.md)
        ↓
TOF — attention / viral hooks (01_TOF/)
        ↓
MOF — proof / demos / case studies (02_MOF/)
        ↓
BOF — trust / offers / conversion (03_BOF/)
        ↓
CUSTOMER / REVENUE
        ↓
RETENTION + UPSELL (04_RETENTION/)
```

## Folder layout (per venture)

Copy `_TEMPLATE/` → `ventures/{VENTURE_CODE}/` or run:

```bash
python3 WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/SCRIPTS/init_venture_funnel.py \
  --venture-id 1d84705c-8ebd-4c0c-83cf-cf383951b7bb
```

```
ventures/CON-004/
├── 00_FOUNDATION/
│   ├── audience.md          # who, pain, desire, trigger
│   └── brand_identity.md    # positioning, tone, visual, proof style
├── 01_TOF/                  # Top of funnel — viral / attention
│   ├── hooks.md
│   ├── content_calendar.csv
│   └── scripts/
├── 02_MOF/                  # Middle — showcase / belief
│   ├── demos.md
│   ├── case_studies.md
│   └── scripts/
├── 03_BOF/                  # Bottom — trust / close
│   ├── offers.md
│   ├── testimonials.md
│   └── scripts/
├── 04_RETENTION/
│   └── upsell_loop.md
├── agents/
│   └── routing.json         # which agent owns each stage
├── publish/
│   ├── landing_page.spec.md
│   └── channel_copy.json
└── funnel_manifest.json     # machine-readable stage config + KPIs
```

## Map to COMMERCIALS (media hub)

| Funnel | COMMERCIALS folder | Purpose |
|--------|-------------------|---------|
| Foundation | `00_STRATEGY`, `01_AVATARS` | Audience + brand |
| TOF | `02_HOOKS`, short `03_SCRIPTS` | Hooks, 15–30s viral |
| MOF | `03_SCRIPTS` (demo), `04_STORYBOARDS` | How it works, proof |
| BOF | `03_SCRIPTS` (close), `10_WINNERS` | Offers, social proof |
| Output | `07_EDITING`, `08_DISTRIBUTION` | Exports per channel |
| Metrics | `09_ANALYTICS` | Stage KPIs |

## Agents

See `REGISTRY/funnel-agents.json` and `PROMPTS/*.md`.

| Agent | Stage | Output |
|-------|-------|--------|
| Audience Agent | Foundation | `audience.md`, segments |
| Brand Agent | Foundation | `brand_identity.md`, consistency checks |
| TOF Agent | TOF | hooks, short scripts, reel concepts |
| MOF Agent | MOF | demos, walkthroughs, case studies |
| BOF Agent | BOF | offers, objection handlers, CTA copy |
| Distribution Agent | All | `publish/channel_copy.json` |

## Automation

| Tool | Role |
|------|------|
| `SCRIPTS/init_venture_funnel.py` | Scaffold venture funnel from linkage CSV |
| `SCRIPTS/generate_funnel_content.py` | Generate stage scripts + optional MP4 |
| `SCRIPTS/weekly_funnel_runner.py` | **Mon–Sun scheduled jobs** (hooks, MOF, BOF, analytics, prep) |
| `SCRIPTS/content_brain.py` | Supabase or local SQLite content brain |
| `WORKFLOWS/n8n-tof-mof-bof.json` | n8n import — intake → script → video → publish queue |
| `WORKFLOWS/n8n-weekly-growth-engine.json` | n8n import — 7 cron triggers → weekly runner |
| `WORKFLOWS/n8n-engagement-feedback-loop.json` | Daily analytics → MOF promotion |
| `DATABASE/supabase-content-brain.sql` | Postgres schema for hooks, assets, queue, reports |
| `Documents/venture_video_pipeline.py` | Render MP4 from stage script |

## Weekly operating system

Full schedule: **`WEEKLY-SCHEDULE.md`** · Triggers: **`REGISTRY/weekly-triggers.json`**

```bash
python3 WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/SCRIPTS/weekly_funnel_runner.py \
  --venture-id YOUR_UUID --day monday
```

## KPIs by stage

See `REGISTRY/kpis-by-stage.json`.

## Quick start (CON-004 example)

```bash
cd /Users/acebless/Documents

# 1. Scaffold funnel files
python3 WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/SCRIPTS/init_venture_funnel.py \
  --venture-id 1d84705c-8ebd-4c0c-83cf-cf383951b7bb

# 2. Generate TOF + MOF + BOF script packs
python3 WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/SCRIPTS/generate_funnel_content.py \
  --venture-id 1d84705c-8ebd-4c0c-83cf-cf383951b7bb --stages tof,mof,bof

# 3. Render TOF video (gold pipeline)
bash run_venture_video_pipeline.sh 1d84705c-8ebd-4c0c-83cf-cf383951b7bb single
```

## Related

- `OPERATING-RUNBOOK.md` — weekly ops checklist
- `Documents/EXECUTION-GUIDE.md` — video batch execution
- `10_VENTURES/.../COMMERCIALS/` — legacy media hub (compatible)
