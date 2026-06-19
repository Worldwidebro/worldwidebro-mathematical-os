# Knowledge Ops

Operationalizes the Obsidian ↔ Graphify ↔ LightRAG ↔ SocratiCode stack with a weekly score and a fixed RAG eval set.

## Files

| File | Role |
|------|------|
| [rag-eval-questions.md](rag-eval-questions.md) | 20 grounded questions + pass criteria |
| [knowledge-ops-scorecard-template.csv](knowledge-ops-scorecard-template.csv) | Weekly score row template |
| `knowledge-ops-scorecard-*.csv` | Generated weekly snapshots (gitignored optional) |

## Weekly loop

```bash
bash WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/knowledge_ops_weekly_loop.sh
```

Or step by step:

1. `cd venture-hub && npm run hub:github-export` (optional if registries fresh)
2. `python3 WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/align_venture_repo_universe.py --skip-fetch`
3. `python3 WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/obsidian_graph_sync.py --local-only` (uses cached `.planning/graph-data.json` when Supabase env is absent; omit `--local-only` when credentials are in `.env` or `venture-hub/.env.mcp.local`)
4. `cd iza-os-rag-system && python3.11 -m src.ingest --source=alignment` (+ `--source=vault` when notes changed; requires RAG stack + network for tiktoken/Ollama)
5. `python3 WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/run_knowledge_ops_scorecard.py`
6. Optional automated RAG subset: `python3 WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/run_rag_eval.py --apply-scorecard`
7. Grade full set: [rag-eval-questions.md](rag-eval-questions.md) then `--rag-eval <pct>`
8. Append compounding rows: [venture-hub/registries/compounding_adoption_log.csv](../../venture-hub/registries/compounding_adoption_log.csv)

If `ventures_classification_final.csv` is missing, the weekly loop runs `regenerate_venture_catalog.py` first (from `VENTURE_STARRED_OWNED_REPOS.csv` + capabilities export).

**Current baseline (2026-06-04):** 629/629 ventures aligned, 0 `needs_attention`, graph connectivity 100%, Knowledge Ops Score ~67 until RAG eval + compounding log are graded.

## Agent execution template

Paste before venture work: [venture-hub/docs/prompts/VENTURE-KNOWLEDGE-OPS-EXECUTION.md](../../venture-hub/docs/prompts/VENTURE-KNOWLEDGE-OPS-EXECUTION.md)

## Target score

**Knowledge Ops Score ≥ 85** = production-ready for agentic venture tasks.

Components (weights in scorecard script): data 25%, graph 20%, RAG eval 25%, SocratiCode 15%, execution/compounding 15%.
