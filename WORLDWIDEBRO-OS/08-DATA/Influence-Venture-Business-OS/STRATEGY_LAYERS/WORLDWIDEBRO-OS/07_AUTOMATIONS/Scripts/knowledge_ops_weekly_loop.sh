#!/usr/bin/env bash
# Weekly Knowledge Ops loop — Obsidian graph, alignment, LightRAG ingest, scorecard.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$ROOT"

echo "== Knowledge Ops weekly loop =="
echo "Root: $ROOT"

if [[ ! -f "$ROOT/ventures_classification_final.csv" ]] && [[ ! -f "$ROOT/WORLDWIDEBRO-OS/08_RESEARCH/Ventures-Data/ventures_classification_final.csv" ]]; then
  echo ">> Regenerate venture catalog (classification + enriched)"
  python3 WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/regenerate_venture_catalog.py
fi

if [[ -d venture-hub ]] && command -v npm >/dev/null 2>&1; then
  echo ">> GitHub registry export (optional)"
  (cd venture-hub && npm run hub:github-export) || echo "   (skipped hub:github-export)"
fi

echo ">> Venture/repo alignment"
python3 WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/align_venture_repo_universe.py --skip-fetch

echo ">> Obsidian graph + alignment JSON"
python3 WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/obsidian_graph_sync.py --local-only

if [[ -d iza-os-rag-system ]]; then
  echo ">> LightRAG alignment ingest"
  (cd iza-os-rag-system && python3.11 -m src.ingest --source=alignment) || \
    (cd iza-os-rag-system && python3 -m src.ingest --source=alignment) || \
    echo "   (ingest failed — start RAG stack first)"
else
  echo ">> Skipping LightRAG ingest (iza-os-rag-system not found)"
fi

echo ">> Knowledge Ops scorecard"
python3 WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/run_knowledge_ops_scorecard.py

echo ">> Done. Grade RAG: WORLDWIDEBRO-OS/08_RESEARCH/Knowledge-Ops/rag-eval-questions.md"
echo "   Then: python3 WORLDWIDEBRO-OS/07_AUTOMATIONS/Scripts/run_knowledge_ops_scorecard.py --rag-eval <pct>"
