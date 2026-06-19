# 00_INTAKE_LAYER — Instagram Intelligence Pipeline

**Purpose**: Capture → Process → Store → Route intelligence from Instagram and social media.

**Status**: Option 1 (Python processor) READY. Options 2-3 in progress.

---

## Folder Structure

```
00_INTAKE_LAYER/
├── Instagram_Screenshots/     # Raw screenshot images
├── DM_Conversations/          # DM text files (Telegram, Discord, X)
├── Raw_Inputs/                # Other raw sources
└── Processed_Output/          # JSON outputs from pipeline
```

---

## Option 1: Python Batch Processor

### Pipeline

```
Screenshot → ocr_vision_processor.py (Claude Vision)
  → extraction_agent.py (Venture routing)
  → dedup_against_lightrag.py (Semantic dedup)
  → push_to_obsidian.py (Atomic notes + Supabase batch)
```

### Quick Start

```bash
cd WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/

# Full pipeline
python ocr_vision_processor.py --batch-dir ../../../00_INTAKE_LAYER/Instagram_Screenshots/ --output /tmp/1.json
python extraction_agent.py --input /tmp/1.json --output /tmp/2.json
python dedup_against_lightrag.py --input /tmp/2.json --output /tmp/3.json
python push_to_obsidian.py --input /tmp/3.json --obsidian-vault /path/to/Obsidian --supabase-output /tmp/supabase_batch.json
```

### Scripts

| Script | Purpose |
|--------|---------|
| `ocr_vision_processor.py` | Claude Vision OCR → JSON |
| `extraction_agent.py` | Route by venture type |
| `dedup_against_lightrag.py` | Semantic dedup (0.95 threshold) |
| `push_to_obsidian.py` | Create atomic notes + Supabase batch |

### Output Formats

**Obsidian Note** (`Obsidian/Instagram_Ideas/YYYY-MM-DD-slug.md`):
- Frontmatter: source, category, venture_type, confidence, deal_flow_stage, tags
- Body: Idea, entities, routing, actions

**Supabase Batch** (`supabase_batch.json`):
- source, idea_text, category, people_mentioned, tools_mentioned, confidence, venture_type, deal_flow_stage, created_at

### Metrics

- **Speed**: 10 screenshots in <2 min
- **Dedup Accuracy**: Zero false positives
- **Latency**: <5 min screenshot → Obsidian note
- **Supabase Sync**: 100% within 5 min

---

## Option 2: n8n Automation (PLANNED)

Hourly Instagram API sync → pipeline → Obsidian + Slack alerts

**Timeline**: 2026-06-07

---

## Option 3: Multi-Source DM Agents (PLANNED)

Telegram + Discord + X → agent processing → network graph

**Timeline**: 2026-06-18

---

## Configuration

- **Claude Model**: claude-3-5-sonnet-20241022
- **Obsidian Path**: /Users/acebless/Documents/Obsidian (override via CLI flag)
- **Dedup Threshold**: 0.95 (cosine similarity)

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Claude timeout | Reduce image size |
| JSON parse error | Check API response format |
| Duplicate ideas | Tune similarity_threshold down |
| Obsidian not found | Verify path, use `--obsidian-vault` flag |

---

---

## Trend Discovery Pipeline (TrendRadar + Miro-Fish)

**Purpose**: Discover hot niches, validate products, predict next wave

### Quick Start

```bash
bash WORLDWIDEBRO-OS/09_AUTOMATION/RUN_DISCOVERY_PIPELINE.sh
```

### Output

- `trendradar_baseline_YYYYMMDD.json` — Niche momentum scores
- `miro_fish_forecast_YYYYMMDD.json` — 30/90-day trend predictions

### Top 5 Niches (Priority Ranked)

1. **FINTECH** — AI banking, crypto, payments
2. **AI_DEVTOOLS** — LLM APIs, prompt engineering
3. **SAAS** — B2B workflow automation
4. **HR_PAYROLL** — HRMS, talent management
5. **EDTECH** — AI tutoring, personalized learning

**Last Updated**: 2026-06-04
