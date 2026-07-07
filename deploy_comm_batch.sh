#!/bin/bash
# deploy_comm_batch.sh — clone, link, and deploy the remaining COMM ventures to Vercel.
# Continues past individual failures; logs results to comm_batch_results.log.

set -u
VENTURES_DIR="/Users/acebless/Documents/WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active"
LOG="/Users/acebless/Documents/comm_batch_results.log"
LIST="/tmp/comm_ventures_remaining2.txt"

while IFS= read -r repo; do
  [ -z "$repo" ] && continue
  echo "=== $repo ===" | tee -a "$LOG"

  # PascalCase-ish local folder name (python, since macOS sed has no \U support)
  folder=$(python3 -c "import sys,re; print(re.sub(r'(^|-)([a-z])', lambda m: m.group(2).upper(), sys.argv[1]))" "$repo")
  target="$VENTURES_DIR/$folder"

  if [ ! -d "$target" ]; then
    git clone "https://github.com/Worldwidebro/$repo.git" "$target" >> "$LOG" 2>&1
  fi

  if [ ! -d "$target" ]; then
    echo "CLONE FAILED: $repo" | tee -a "$LOG"
    continue
  fi

  cd "$target" || continue

  vercel link --yes --project "$repo" --scope worldwidebros-projects >> "$LOG" 2>&1

  deploy_output=$(vercel deploy --prod 2>&1)
  echo "$deploy_output" >> "$LOG"

  url=$(echo "$deploy_output" | grep -Eo 'https://[a-zA-Z0-9.-]+\.vercel\.app' | tail -1)
  if [ -n "$url" ]; then
    echo "SUCCESS: $repo -> $url" | tee -a "$LOG"
  else
    echo "DEPLOY FAILED: $repo" | tee -a "$LOG"
  fi

  cd "$VENTURES_DIR" || true
done < "$LIST"

echo "=== BATCH COMPLETE ===" | tee -a "$LOG"
