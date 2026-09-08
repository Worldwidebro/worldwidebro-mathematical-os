#!/usr/bin/env bash
# deploy-ventures.sh — spread venture-template's 3-file Phase 1 context package
# (docs/ONTOLOGY.md symlink, venture.json, src/lib/ontology.ts) to every venture
# folder under Documents that is (a) findable from ventures_index.csv and (b) a
# real git repo.
#
# Usage:
#   ./deploy-ventures.sh          # dry run — shows what would happen, no git writes
#   ./deploy-ventures.sh --apply  # actually copies files + commits + pushes
#
# ponytail: bash+find+sed instead of a whole node/python tool — this is a
# straight-line file copy across a folder list, stdlib shell covers it.

set -uo pipefail

ROOT="/Users/acebless/Documents"
TEMPLATE="$ROOT/venture-template"
CSV="$ROOT/ventures_index.csv"
LOGDIR="$ROOT/.deploy-logs"
TS="$(date +%Y%m%d-%H%M%S)"
LOG="$LOGDIR/deploy-$TS.log"
REPORT="$LOGDIR/deploy-report-$TS.md"

APPLY=0
[[ "${1:-}" == "--apply" ]] && APPLY=1

mkdir -p "$LOGDIR"
: > "$LOG"

log() { echo "$1" | tee -a "$LOG"; }

deployed=()
not_found=()
not_git=()
skip_existing=()
push_errors=()
already_current=()

total=0

log "=== deploy-ventures.sh run $TS (apply=$APPLY) ==="

while IFS=, read -r id name sector stage rev owner repo_id created status; do
  [[ "$id" == "id" ]] && continue   # header
  [[ -z "$id" ]] && continue
  total=$((total+1))

  id_lower=$(echo "$id" | tr '[:upper:]' '[:lower:]')

  # Find candidate folder: top-level first, then up to 4 levels deep.
  match=$(find "$ROOT" -maxdepth 1 -iname "${id_lower}-*" -type d 2>/dev/null | head -1)
  if [[ -z "$match" ]]; then
    match=$(find "$ROOT" -maxdepth 4 -iname "${id_lower}-*" -type d \
      -not -path "*/node_modules/*" -not -path "*/.git/*" 2>/dev/null | head -1)
  fi

  if [[ -z "$match" ]]; then
    not_found+=("$id")
    log "[NOT FOUND] $id"
    continue
  fi

  if [[ ! -d "$match/.git" ]]; then
    not_git+=("$id -> $match")
    log "[NOT GIT] $id -> $match"
    continue
  fi

  log "[MATCH] $id -> $match"

  if [[ $APPLY -eq 0 ]]; then
    deployed+=("$id -> $match (dry-run)")
    continue
  fi

  mkdir -p "$match/docs" "$match/src/lib"

  # docs/ONTOLOGY.md as symlink to the canonical file (matches template pattern)
  ln -sf "$ROOT/ONTOLOGY.md" "$match/docs/ONTOLOGY.md"

  # src/lib/ontology.ts — straight copy from template
  cp "$TEMPLATE/src/lib/ontology.ts" "$match/src/lib/ontology.ts"

  # venture.json — only create if missing, never clobber a real one
  if [[ -f "$match/venture.json" ]]; then
    skip_existing+=("$id (venture.json already exists)")
    log "[SKIP venture.json] $id already has one, left untouched"
  else
    sed \
      -e "s/VENTURE-XXX/$id/" \
      -e "s/Unnamed Venture/${name:-Unnamed Venture}/" \
      -e "s/sector-name/${sector:-unknown}/" \
      "$TEMPLATE/venture.json" > "$match/venture.json"
  fi

  # Scope git add to only the 3 target paths — do NOT git add -A, these repos
  # have unrelated dirty state (receipts.jsonl, untracked dirs) that must not
  # get swept into this commit.
  ( cd "$match" && git add docs/ONTOLOGY.md src/lib/ontology.ts venture.json 2>>"$LOG" )

  if ( cd "$match" && git diff --cached --quiet ); then
    already_current+=("$id")
    log "[NO CHANGE] $id — files already match, nothing to commit"
    continue
  fi

  if ! ( cd "$match" && git commit -m "chore: add Phase 1 context system" >>"$LOG" 2>&1 ); then
    push_errors+=("$id (commit failed)")
    log "[COMMIT FAILED] $id"
    continue
  fi

  branch=$(cd "$match" && git branch --show-current)
  if ( cd "$match" && git push origin "HEAD:$branch" >>"$LOG" 2>&1 ); then
    deployed+=("$id -> $match")
    log "[PUSHED] $id -> $match ($branch)"
  else
    push_errors+=("$id (push failed, see log)")
    log "[PUSH FAILED] $id"
  fi

done < "$CSV"

{
  echo "# Bulk Deploy Report — $TS"
  echo
  echo "Mode: $([[ $APPLY -eq 1 ]] && echo APPLY || echo DRY-RUN)"
  echo
  echo "## Summary"
  echo "- Total CSV rows processed: $total"
  echo "- Deployed/pushed: ${#deployed[@]}"
  echo "- Not found (no matching folder): ${#not_found[@]}"
  echo "- Found but not a git repo: ${#not_git[@]}"
  echo "- venture.json already existed (skipped): ${#skip_existing[@]}"
  echo "- Already current (nothing to commit): ${#already_current[@]}"
  echo "- Git errors: ${#push_errors[@]}"
  echo
  echo "## Deployed"
  for v in "${deployed[@]:-}"; do [[ -n "$v" ]] && echo "- $v"; done
  echo
  echo "## Git errors"
  for v in "${push_errors[@]:-}"; do [[ -n "$v" ]] && echo "- $v"; done
  echo
  echo "## Not found (sample, first 30 of ${#not_found[@]})"
  for v in "${not_found[@]:0:30}"; do echo "- $v"; done
  echo
  echo "## Not git (all)"
  for v in "${not_git[@]:-}"; do [[ -n "$v" ]] && echo "- $v"; done
} > "$REPORT"

log ""
log "=== DONE: deployed=${#deployed[@]} not_found=${#not_found[@]} not_git=${#not_git[@]} errors=${#push_errors[@]} ==="
log "Full log: $LOG"
log "Report:   $REPORT"
