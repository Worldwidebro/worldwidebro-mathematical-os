#!/bin/bash
# Registers the Discord GitHub-webhook on all ACTIVE (non-archived) owned repos.
# Idempotent: skips repos that already have this exact Discord hook.
# Rollback: discord-webhook-rollout.sh remove
set -uo pipefail

DISCORD_BASE="https://discord.com/api/webhooks/1518792491569123409/bQFeEZyejfZn2njbO16TexwdllAv0alLvtJleYmiWw5ifNiRRh9UPfegjpMUlXYcZTYl"
HOOK_URL="${DISCORD_BASE}/github"
LOG=/tmp/discord-webhook-rollout.log
: > "$LOG"

# active (non-archived) repos
mapfile -t REPOS < <(awk -F'\t' '$2=="false"{print $1}' /tmp/all_repos.tsv)
echo "Mode=${1:-add}  Active repos=${#REPOS[@]}" | tee -a "$LOG"

added=0; skipped=0; failed=0; removed=0
for REPO in "${REPOS[@]}"; do
  # find existing hook id pointing at our discord webhook id
  existing=$(gh api "repos/$REPO/hooks" --jq \
    ".[] | select(.config.url // \"\" | contains(\"1518792491569123409\")) | .id" 2>/dev/null | head -1)

  if [ "${1:-add}" = "remove" ]; then
    if [ -n "$existing" ]; then
      gh api -X DELETE "repos/$REPO/hooks/$existing" >/dev/null 2>&1 && { removed=$((removed+1)); echo "REMOVED $REPO ($existing)" >>"$LOG"; }
    fi
    continue
  fi

  if [ -n "$existing" ]; then
    skipped=$((skipped+1)); echo "SKIP   $REPO (already has $existing)" >>"$LOG"; continue
  fi

  res=$(gh api -X POST "repos/$REPO/hooks" \
    -f "name=web" -F "active=true" \
    -f "config[url]=$HOOK_URL" -f "config[content_type]=json" \
    -f "events[]=push" -f "events[]=pull_request" -f "events[]=issues" -f "events[]=release" \
    --jq '.id' 2>>"$LOG")
  if [ -n "$res" ] && [ "$res" != "null" ]; then
    added=$((added+1)); echo "ADDED  $REPO ($res)" >>"$LOG"
  else
    failed=$((failed+1)); echo "FAIL   $REPO" >>"$LOG"
  fi
done

echo "DONE add=$added skip=$skipped fail=$failed removed=$removed" | tee -a "$LOG"
