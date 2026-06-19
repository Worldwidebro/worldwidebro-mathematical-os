# Phase 2 + MoneyPrinter + Instagram — Executable Scripts Guide

**Status**: All three workflows ready to execute
**Date**: 2026-06-05
**Branch**: 2026-05-22-figt

---

## ✅ Phase 2 Complete: Ventures Consolidated

```bash
bash phase-2-consolidate-ventures.sh
```

**What it does:**
- Moves `con-001-ace-construction` → `WORLDWIDEBRO-OS/10_VENTURES/Operations_Ventures/`
- Moves `bw-001-lash-extension-studio` → `WORLDWIDEBRO-OS/10_VENTURES/SaaS_Ventures/`
- Moves `venture-factory-core` → `WORLDWIDEBRO-OS/10_VENTURES/SaaS_Ventures/`
- Moves `YES-LLC-CONTRACTOR-DELIVERY` → `WORLDWIDEBRO-OS/00_CLIENT_WORK/YES-LLC-Wave-Rideshare/`
- Loads **venture-repo linkage**: `WORLDWIDEBRO-VENTURES-REPOS-ALIGNMENT.csv` (630 ventures)

**Status**: ✅ DONE (21 construction ventures found, 3 SaaS ventures organized)

---

## 🎬 MoneyPrinter V2: Generate Construction Videos

### Step 1: Prepare Metadata
```bash
python3 moneyprinter_v2_batch_generator.py
```

**What it does:**
- Finds 21 construction ventures from linkage CSV
- Generates video metadata for top 5 (adjustable with `--limit`)
- Creates output structure: `moneyprinter-output/{venture_id}/metadata.json`
- Generates promotional scripts per venture

**Output example:**
```
🏗️  Found 21 construction ventures:
   • CON-002 Permit Compliance Platform
   • CON-003 Contractor Network
   • CON-004 Building Supply Chain
   ...

✅ Metadata prepared: 5
📂 Output dir: /Users/acebless/Documents/moneyprinter-output
```

### Step 2: Gold-standard render (script + scenes + TTS + publish pack)

```bash
bash run_venture_video_pipeline.sh 1d84705c-8ebd-4c0c-83cf-cf383951b7bb single
# or batch (top 5):
bash run_venture_video_pipeline.sh _ all
```

**What it does:**
- `venture_script_engine.py` — trade-specific hooks, 5-line scripts, YouTube title/description/hashtags
- `venture_video_pipeline.py` — 5 scene cards, voice (edge-tts → macOS say → timed silent fallback), SRT sidecar, MP4

**Output per venture:**
- `metadata.json` (schema v2)
- `output.mp4` (multi-scene)
- `publish.json` (upload copy)
- `work/captions.srt` (caption file for platforms)

### Step 2b: Legacy simple render (static single frame)

```bash
/opt/homebrew/bin/python3.12 simple_video_generator.py --venture all
```

### Step 2c: Execute Video Generation (MoneyPrinter V2 native)
```bash
bash execute_moneyprinter_batch.sh
```

**What it does:**
- Runs `MoneyPrinterV2/src/main.py` with batch config
- Generates MP4s (1080p, YouTube Shorts optimized)
- Outputs to `moneyprinter-output/{venture_id}/output.mp4`

**Requirements:**
- MoneyPrinterV2 installed: `/Users/acebless/MoneyPrinterV2`
- Python 3.12
- FFmpeg, moviepy, assemblyai (per requirements.txt)

**Timeline**: ~2-5 min per video (parallel processing for 2 videos at a time)

---

## 📸 Instagram Content: Two Approaches

### Approach A: Automated Web Scraping (Selenium)

```bash
# First-time setup
python3 instagram_scraper_automated.py --mode selenium --account your_username

# Requires:
# - .env file with INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD
# - Selenium installed: pip install selenium undetected-chromedriver
```

**What it does:**
- Auto-scrapes Instagram profile for posts
- Extracts captions, images, engagement metrics
- Saves to `WORLDWIDEBRO-OS/00_INTAKE_LAYER/Instagram_Raw/`

**Status**: Ready (credentials not yet in .env)

---

### Approach B: Manual Webhook + Bookmarklet (Recommended)

**Setup** (one-time):
```bash
python3 instagram_scraper_automated.py --mode webhook
```

**What it creates:**
1. **Webhook receiver** (`instagram_webhook_receiver.py`) — listens on `http://localhost:5000`
2. **Browser bookmarklet** (`INSTAGRAM_CAPTURE_BOOKMARKLET.txt`) — one-click capture
3. **Import processor** (`process_instagram_captures.py`) — batch process captures

**Execution:**

Terminal 1 — Start webhook receiver:
```bash
python3 instagram_webhook_receiver.py
# Output: 🔌 Instagram webhook receiver listening on http://localhost:5000
```

Terminal 2 — Use browser bookmarklet:
```bash
# 1. Open INSTAGRAM_CAPTURE_BOOKMARKLET.txt
cat INSTAGRAM_CAPTURE_BOOKMARKLET.txt

# 2. Create new browser bookmark with the JavaScript code
# 3. Visit any Instagram post
# 4. Click the bookmark — it captures the post to webhook

# Watch Terminal 1 for: ✅ Webhook capture saved: ...
```

Terminal 3 — Process captured posts:
```bash
python3 process_instagram_captures.py

# Output:
# 📊 Found 5 captures
# 📸 https://instagram.com/p/ABC123
#    Caption: New product launch...
```

**Why this approach:**
- ✅ No auto-login complexity
- ✅ Selective capture (you choose which posts)
- ✅ Works with private accounts
- ✅ Respects Instagram's ToS
- ✅ Webhook can be extended to Slack, Discord, Telegram

---

## 🚀 Master Execution Flow

### Sequential (Safest):
```bash
# 1. Phase 2 consolidation
bash phase-2-consolidate-ventures.sh

# 2. MoneyPrinter preparation
python3 moneyprinter_v2_batch_generator.py

# 3. MoneyPrinter execution
bash execute_moneyprinter_batch.sh
# (wait for videos to finish, ~10-30 min for 5 videos)

# 4. Instagram setup (choose A or B)
python3 instagram_scraper_automated.py --mode webhook
# OR
python3 instagram_scraper_automated.py --mode selenium --account myaccount
```

### Parallel (Faster, Instagram separate session):
```bash
# In main session:
bash phase-2-consolidate-ventures.sh
python3 moneyprinter_v2_batch_generator.py
bash execute_moneyprinter_batch.sh  # background job

# In separate terminal session (dispatch center):
python3 instagram_scraper_automated.py --mode webhook
# ... use bookmarklet to capture Instagram posts
python3 process_instagram_captures.py
```

---

## 📊 Status Checklist

| Task | Status | Command |
|------|--------|---------|
| Phase 2: Consolidate ventures | ✅ DONE | `bash phase-2-consolidate-ventures.sh` |
| MoneyPrinter: Prepare metadata | ✅ READY | `python3 moneyprinter_v2_batch_generator.py` |
| MoneyPrinter: Generate videos | ⏳ PENDING | `bash execute_moneyprinter_batch.sh` |
| Instagram: Webhook setup | ✅ READY | `python3 instagram_scraper_automated.py --mode webhook` |
| Instagram: Bookmarklet use | ⏳ MANUAL | Cat & copy `INSTAGRAM_CAPTURE_BOOKMARKLET.txt` |
| Instagram: Process captures | ✅ READY | `python3 process_instagram_captures.py` |

---

## 🔍 Verification

**Phase 2 output:**
```bash
ls -la /Users/acebless/Documents/WORLDWIDEBRO-OS/10_VENTURES/{Operations_Ventures,SaaS_Ventures}/
# Should show: con-001-*, bw-001-*, venture-factory-core
```

**MoneyPrinter metadata:**
```bash
find /Users/acebless/Documents/moneyprinter-output -name "metadata.json" | wc -l
# Should show: 5 (or limit specified)
```

**Instagram captures:**
```bash
ls /Users/acebless/Documents/WORLDWIDEBRO-OS/00_INTAKE_LAYER/Instagram_Raw/
# Should show: webhook_*.json files (after bookmarklet clicks)
```

---

## Growth funnel (TOF → MOF → BOF)

System root: `WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/README.md`

```bash
# Scaffold per venture
python3 WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/SCRIPTS/init_venture_funnel.py \
  --venture-id 1d84705c-8ebd-4c0c-83cf-cf383951b7bb

# Generate stage scripts (metadata_tof.json, metadata_mof.json, metadata_bof.json)
python3 WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/SCRIPTS/generate_funnel_content.py \
  --venture-id 1d84705c-8ebd-4c0c-83cf-cf383951b7bb --stages tof,mof,bof

# Render TOF video: copy stage metadata then run pipeline
cp moneyprinter-output/{venture_id}/metadata_tof.json moneyprinter-output/{venture_id}/metadata.json
bash run_venture_video_pipeline.sh {venture_id} single
```

n8n: import `11_GROWTH_FUNNEL/WORKFLOWS/n8n-tof-mof-bof.json`

**Weekly engine:** `WEEKLY-SCHEDULE.md` + `weekly_funnel_runner.py --day auto`

---

## 🎯 Next Phase (Phase 3)

Once MoneyPrinter videos complete:
1. Verify video quality in `moneyprinter-output/{venture_id}/output.mp4`
2. Upload to YouTube via automation (Post Bridge integration)
3. Extract Instagram ideas → feed into venture agents via LightRAG
4. Create unified dashboard in Obsidian
