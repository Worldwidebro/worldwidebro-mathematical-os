# Venture Media Factory — Architecture

Single control layer: **`MASTER_ORCHESTRATOR.py`**

---

## Five layers (one system)

```
┌─────────────────────────────────────────────────────────────┐
│  CONTROL: MASTER_ORCHESTRATOR.py + orchestrator-config.json │
└───────────────────────────────┬─────────────────────────────┘
                                │
     ┌──────────────────────────┼──────────────────────────┐
     ▼                          ▼                          ▼
 INTELLIGENCE              STRATEGY                  PRODUCTION
 content_brain             weekly_funnel_runner      venture_script_engine
 Supabase / SQLite         generate_funnel_content   venture_video_pipeline
                           batch_weekly_*            Higgsfield CLI (optional)
     │                          │                          │
     └──────────────────────────┼──────────────────────────┘
                                ▼
                          VIRAL ENGINE
                    Opus Clip (long → shorts)
                    publish_queue → Buffer/Later
                                │
                                ▼
                          ORCHESTRATION
                    n8n crons + webhooks
                    MASTER_ORCHESTRATOR cron
```

---

## Control flow (one run)

```text
MASTER_ORCHESTRATOR run --auto
        ↓
read orchestrator-config.json + content_brain state
        ↓
pick venture (round-robin or --venture-id)
        ↓
resolve goal from weekday → tof | mof | bof | weekly | batch
        ↓
generate_funnel_content.py (stage scripts)
        ↓
[optional] Higgsfield scene stills per scene JSON
        ↓
[optional] run_venture_video_pipeline.sh → output.mp4
        ↓
queue gf_publish_queue / SQLite publish_queue
        ↓
[optional] notify n8n webhook runner
        ↓
append orchestrator_runs.jsonl
```

---

## Commands

```bash
cd /Users/acebless/Documents/WORLDWIDEBRO-OS/11_GROWTH_FUNNEL

# Status
python3 MASTER_ORCHESTRATOR.py status

# Auto: next venture + today's funnel job
python3 MASTER_ORCHESTRATOR.py run --auto

# One venture, full cycle (script + render + opus clips + queue)
python3 MASTER_ORCHESTRATOR.py run --venture-id UUID --goal full_cycle --render --opus-clip

# With Higgsfield scene assets (composited in video pipeline)
HIGGSFIELD_ENABLED=1 python3 MASTER_ORCHESTRATOR.py run --venture-id UUID --stage tof --higgsfield --render

# Opus only (FFmpeg shorts → publish queue)
python3 SCRIPTS/opus_clip_runner.py --venture-id UUID --stage mof --mode local

# n8n Cloud entry (run runner + tunnel first)
python3 SCRIPTS/n8n_webhook_runner.py --port 8765

# Dry run (print plan only)
python3 MASTER_ORCHESTRATOR.py run --auto --dry-run
```

---

## Tool roles (canonical)

| Layer | Tools |
|-------|--------|
| Intelligence | `content_brain.py`, SQLite, Supabase `gf_*` |
| Strategy | `weekly_funnel_runner.py`, `generate_funnel_content.py`, `batch_weekly_all_ventures.py` |
| Production | `venture_script_engine.py`, `venture_video_pipeline.py`, FFmpeg, edge-tts, PIL, **Higgsfield** |
| Viral | **Opus Clip**, `gf_publish_queue`, TikTok/IG/YT |
| Orchestration | **MASTER_ORCHESTRATOR.py**, n8n, `n8n_webhook_runner.py` |

---

## Extension slots

| Tool | Status | How |
|------|--------|-----|
| Higgsfield | Wired | `--higgsfield` → `higgsfield_scenes.py` → PNG backgrounds in video pipeline |
| Opus Clip | Wired | `--opus-clip` or auto after MOF render; local FFmpeg or `OPUS_API_KEY` + public URL |
| MotionSites.ai | Manual | Landing motion between video → convert |
| Nano Banana prompts | Library | Curate into `PROMPTS/image/` |

---

## n8n single entry

Replace seven separate crons with one daily call:

```bash
python3 MASTER_ORCHESTRATOR.py run --auto --render
```

Or HTTP POST to webhook runner → shell out to orchestrator.

Import: `WORKFLOWS/n8n-orchestrator-cloud.json` (Cloud + tunnel) or `WORKFLOWS/n8n-master-orchestrator.json` (self-hosted Execute Command).

---

## Business output model

```
1 venture × 1 week
  → 7 scheduled jobs (weekly runner)
  → ~10 hooks, ~3 scripts/day class
  → optional 3–5 rendered MP4s
  → publish queue rows
  → Opus can multiply each long MOF into 20+ TOF clips
```

Scale: change `construction-batch.json` → 478 ventures same orchestrator.

---

## Files

| File | Purpose |
|------|---------|
| `MASTER_ORCHESTRATOR.py` | Control brain |
| `REGISTRY/orchestrator-config.json` | Paths, defaults, layer map |
| `DATA/orchestrator_state.json` | Round-robin + last runs |
| `DATA/orchestrator_runs.jsonl` | Audit log |
| `DATABASE/supabase-content-brain.sql` | Cloud memory |
| `N8N-WIRING-GUIDE.md` | Automation setup |
