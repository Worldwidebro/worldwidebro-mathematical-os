#!/usr/bin/env bash
# Apply Growth Funnel SQL to Supabase (Dashboard paste or psql with DATABASE_URL)
set -euo pipefail

ROOT="/Users/acebless/Documents/WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/DATABASE"
FILES=(
  "$ROOT/supabase-content-brain.sql"
  "$ROOT/supabase-orchestrator-runs.sql"
)

echo "Growth Funnel schema files (apply in order):"
for f in "${FILES[@]}"; do
  echo "  • $f"
done
echo ""
echo "Option A — Supabase Dashboard → SQL Editor → paste both files"
echo "Option B — psql: psql \"\$DATABASE_URL\" -f ... (service role connection string)"
echo ""
echo "After apply, source env and sync:"
echo "  source ~/.env.funnel.local"
echo "  python3 WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/SCRIPTS/sync_sqlite_to_supabase.py"
echo ""
if [[ -n "${DATABASE_URL:-}" ]]; then
  for f in "${FILES[@]}"; do
    echo "Applying $f ..."
    psql "$DATABASE_URL" -f "$f"
  done
  echo "Done."
else
  echo "DATABASE_URL not set — listing only."
fi
