---
name: SecondBrain/CLAUDE
title: SecondBrain — Claude Code Session Context
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# SecondBrain — Claude Code Session Context

> This directory is the Claude Code working directory. The actual Obsidian vault is elsewhere.
> Read this file every session for full system context.

## Who You're Working With
Ace (winnerscirclewcllc@gmail.com) — building a sovereign multi-system ecosystem across AI, business automation, and knowledge management.

## The Actual Vault
```
/Users/acebless/Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault/
```
2,200+ notes. Always use this full path for vault file operations.
The vault also has its own CLAUDE.md with full structure detail.

## Active Systems

| System | Location | Status |
|--------|----------|--------|
| **Iza-OS RAG (LightRAG)** | `/Users/acebless/Documents/iza-os-rag-system/` | Ingesting vault — query at http://localhost:8000 |
| **Ollama** | http://localhost:11434 | Running — qwen2.5:32b + nomic-embed-text |
| **Iza-OS Docker stack** | `~/iza_os/` | Not running — start: `cd ~/iza_os && ./setup_izaos_warp.sh` |
| **The Office** | Convex→Supabase migration in progress | See `/Users/acebless/Documents/iza-os-rag-system/PROJECT.md` |

## RAG System — How to Use

**Query the knowledge graph** (when server is running):
```bash
curl -s -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"q":"YOUR QUESTION HERE", "mode":"hybrid"}'
```

**Start the RAG server:**
```bash
cd /Users/acebless/Documents/iza-os-rag-system && source .venv/bin/activate && python3 -m src.serve
```

**Re-ingest vault:**
```bash
cd /Users/acebless/Documents/iza-os-rag-system && source .venv/bin/activate && python3 -m src.ingest --source=vault
```

**Check ingest progress:**
```bash
cat /Users/acebless/Documents/iza-os-rag-system/lightrag_data/kv_store_doc_status.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(f'{len(d)} docs indexed')"
```

## Agent Memory
Located at: `~/.claude/projects/-Users-acebless-Documents-SecondBrain/memory/`
Read MEMORY.md there for full cross-session context.

## Key Vault Folders
```
00-INBOX/          ← capture target, triage daily
01-CORE-SYSTEMS/   ← Iza-OS, CivOS architecture
03-ACTIVE-PROJECTS/← current work
04-KNOWLEDGE-GRAPHS/← entity maps, canvas graphs
05-PROMPTS-LIBRARY/← prompt templates
07-BUSINESS-STRATEGY/← revenue, ventures
Iza-OS-Setup/      ← MASTER_CONTROL.md (full stack architecture)
```

## Available Claude Code Skills
- `knowledge-ops` — multi-layer knowledge sync
- `deep-research` — research workflows
- `iza-os-rag` — query LightRAG knowledge graph (custom skill)

## The Office Migration Context
Convex → Supabase migration in progress. 199 server action exports across 14 modules.
Supabase project: befitting-deer-732.
See PROJECT.md in iza-os-rag-system for full checklist.
