#!/bin/bash
# Deploy a single venture repo to Vercel production, capture its clean
# production alias, wire it into deployment-urls.csv, then rebuild and
# redeploy vex-hero-site so the venture shows up as clickable at
# vex-hero-site-sigma.vercel.app/ventures.
#
# Usage:
#   ./deploy-and-link-venture.sh <venture-folder-name> <VENTURE-ID> [--dry-run]
#
# Example:
#   ./deploy-and-link-venture.sh con-001-ace-construction CON-001-ACE-CONSTRUCTION
#   ./deploy-and-link-venture.sh con-001-ace-construction CON-001-ACE-CONSTRUCTION --dry-run

set -euo pipefail

DOCS_ROOT="/Users/acebless/Documents"
CSV_PATH="$DOCS_ROOT/WORLDWIDEBRO-OS/08-DATA/registries/deployment-urls.csv"
VEX_PATH="$DOCS_ROOT/vex-hero-site"

FOLDER="${1:?Usage: $0 <venture-folder-name> <VENTURE-ID> [--dry-run]}"
VENTURE_ID="${2:?Usage: $0 <venture-folder-name> <VENTURE-ID> [--dry-run]}"
DRY_RUN="${3:-}"

REPO_PATH="$DOCS_ROOT/$FOLDER"
if [ ! -d "$REPO_PATH" ]; then
  echo "ERROR: $REPO_PATH does not exist" >&2
  exit 1
fi

echo "== 1/5: Deploying $FOLDER to Vercel production =="
if [ "$DRY_RUN" = "--dry-run" ]; then
  echo "(dry-run: skipping real vercel deploy, using existing csv value if present)"
  CLEAN_URL=$(grep "^$VENTURE_ID," "$CSV_PATH" | cut -d',' -f2- || true)
  if [ -z "$CLEAN_URL" ]; then
    CLEAN_URL="https://example-dry-run.vercel.app"
  fi
else
  cd "$REPO_PATH"
  DEPLOY_OUTPUT=$(vercel deploy --prod 2>&1)
  echo "$DEPLOY_OUTPUT"
  PROD_URL=$(echo "$DEPLOY_OUTPUT" | grep -oE 'https://[a-zA-Z0-9.-]+\.vercel\.app' | head -1)
  if [ -z "$PROD_URL" ]; then
    echo "ERROR: could not parse a production URL from vercel deploy output" >&2
    exit 1
  fi

  echo "== 2/5: Resolving clean production alias (no random hash) =="
  PROJECT_NAME=$(vercel inspect "$PROD_URL" 2>&1 | grep -E '^\s*name\s' | awk '{print $2}')
  CLEAN_URL="https://${PROJECT_NAME}.vercel.app"
  CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 8 "$CLEAN_URL")
  if [ "$CODE" != "200" ]; then
    echo "WARNING: $CLEAN_URL returned $CODE, falling back to deploy URL $PROD_URL" >&2
    CLEAN_URL="$PROD_URL"
  fi
  cd "$DOCS_ROOT"
fi

echo "Resolved live URL: $CLEAN_URL"

echo "== 3/5: Updating deployment-urls.csv for $VENTURE_ID =="
if grep -q "^$VENTURE_ID," "$CSV_PATH"; then
  # Update existing row in place
  TMP_FILE=$(mktemp)
  awk -F',' -v id="$VENTURE_ID" -v url="$CLEAN_URL" \
    'BEGIN{OFS=","} $1==id {$2=url} {print}' "$CSV_PATH" > "$TMP_FILE"
  mv "$TMP_FILE" "$CSV_PATH"
  echo "Updated existing row for $VENTURE_ID"
else
  echo "$VENTURE_ID,$CLEAN_URL" >> "$CSV_PATH"
  echo "Appended new row for $VENTURE_ID"
fi

echo "== 4/5: Regenerating and rebuilding vex-hero-site =="
cd "$VEX_PATH"
npm run generate:data
npm run build

if [ "$DRY_RUN" = "--dry-run" ]; then
  echo "(dry-run: skipping vex-hero-site deploy)"
else
  echo "== 5/5: Deploying vex-hero-site to production =="
  vercel deploy --prod
fi

echo "Done. $VENTURE_ID -> $CLEAN_URL"
