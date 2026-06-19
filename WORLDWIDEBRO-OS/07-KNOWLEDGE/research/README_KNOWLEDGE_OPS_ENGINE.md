# Knowledge Ops Engine

**Capture → Process → Index → Route intelligence across your portfolio.**

A production-ready system for ingesting ideas from Instagram, DMs, and social sources, extracting structured knowledge, deduplicating via semantic search, and routing to agents for execution across 712+ ventures.

**Status**: v0.1 (Option 1 complete, Options 2-3 in progress)  
**Core**: Claude Vision API, LightRAG, Supabase, Obsidian, n8n, Agent swarm

---

## What It Does

```
Instagram / DMs / Screenshots
    ↓ Option 1: Python Batch (Claude Vision OCR + routing)
    ↓ Option 2: n8n + Composio (hourly automation)
    ↓ Option 3: DM agents (network intelligence)
    ↓
Supabase + LightRAG (semantic indexing)
    ↓
Obsidian (atomic notes) → AI Agents (route to execution)
    ↓
Venture Metrics (sync across 712+ ventures)
```

---

## Features

### ✅ Option 1: Python Batch Processor (Complete)
- Claude Vision OCR from screenshots
- Venture type classification + routing
- Semantic deduplication (LightRAG)
- Obsidian atomic notes
- Supabase batch JSON

**Run it**:
```bash
bash 00_INTAKE_LAYER/Scripts/test_instagram_pipeline.sh
```

### 🔲 Option 2: n8n + Composio (In Progress)
- Instagram API hourly sync
- Automated pipeline execution
- Slack alerts on high-signal ideas
- Obsidian Dataview dashboard

### 🔲 Option 3: Multi-Source DM Agents (Planned)
- Telegram, Discord, X parsing
- People network graph
- Deal flow intelligence
- Agent decision loop

---

## Quick Start

### Prerequisites
```
Python 3.10+
Claude API key (ANTHROPIC_API_KEY)
Obsidian vault
LightRAG instance (http://localhost:8000)
Supabase project (optional)
```

### Installation
```bash
git clone https://github.com/Worldwidebro/knowledge-ops-engine.git
cd knowledge-ops-engine
python -m venv venv && source venv/bin/activate
pip install anthropic supabase-py
```

### Test Option 1
```bash
# Add screenshots
cp ~/Downloads/*.png 00_INTAKE_LAYER/Instagram_Screenshots/

# Run pipeline
bash 00_INTAKE_LAYER/Scripts/test_instagram_pipeline.sh

# Check Obsidian
open ~/Library/Mobile\ Documents/com~apple~CloudDocs/Documents/Obsidian\ Vault/Instagram_Ideas/
```

---

## Architecture

### Folder Structure
```
00_INTAKE_LAYER/             ← Raw captures
├── Instagram_Screenshots/
├── DM_Conversations/
├── Raw_Inputs/
└── Processed_Output/

01_PROCESSING/               ← Python scripts
├── ocr_vision_processor.py
├── extraction_agent.py
├── dedup_against_lightrag.py
└── push_to_obsidian.py

02_AUTOMATION/               ← n8n workflows (Option 2)
└── n8n/workflows/

03_DOCUMENTATION/            ← This file + guides
```

### Data Flow
```
Screenshot → OCR → Extraction → Dedup → Obsidian
                                          ↓
                                    LightRAG Index
                                          ↓
                                    Agent Query
```

---

## Scripts (Option 1)

| Script | Purpose | Input | Output |
|--------|---------|-------|--------|
| `ocr_vision_processor.py` | Vision OCR | PNG/JPG | JSON (extracted ideas) |
| `extraction_agent.py` | Venture routing | JSON | JSON (classified) |
| `dedup_against_lightrag.py` | Deduplication | JSON | JSON (filtered) |
| `push_to_obsidian.py` | Obsidian sync | JSON | Markdown + Supabase batch |

---

## Integration

### LightRAG
```bash
cd /path/to/iza-os-rag-system
python3 -m src.ingest --source=vault
```

### Agents
```python
from lightrag_agent_queries import query_lightrag
result = query_lightrag("AI opportunities", mode="hybrid")
```

### Obsidian
Notes auto-created at: `Obsidian Vault/Instagram_Ideas/YYYY-MM-DD-slug.md`

### Supabase
See `02_AUTOMATION/configs/supabase_schema.sql` for table setup

---

## Roadmap

- ✅ **v0.1**: Option 1 (Python batch processor)
- 🔲 **v0.2**: Option 2 (n8n + Composio) — 3-4 days
- 🔲 **v0.3**: Option 3 (DM agents) — 2-3 weeks
- 🔲 **v0.4**: Venture replication (scale to 712 ventures) — ongoing

---

## Related Repos

- [iza-os-rag-system](https://github.com/Worldwidebro/iza-os-rag-system) — Knowledge RAG
- [mission-control](https://github.com/Worldwidebro/mission-control) — Agent orchestration
- [venture-hub](https://github.com/Worldwidebro/venture-hub) — Venture management

---

**Author**: Worldwidebro | **Email**: winnerscirclewcllc@gmail.com | **Created**: 2026-06-04
