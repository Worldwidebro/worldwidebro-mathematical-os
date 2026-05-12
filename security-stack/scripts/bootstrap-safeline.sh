#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SAFELINE_DIR="${ROOT}/safeline"
COMPOSE_URL="https://waf.chaitin.com/release/latest/compose.yaml"

mkdir -p "$SAFELINE_DIR"
cd "$SAFELINE_DIR"

if [[ ! -f compose.yaml ]]; then
  echo "Downloading official SafeLine compose.yaml → $SAFELINE_DIR/compose.yaml"
  curl -fsSL "$COMPOSE_URL" -o compose.yaml
else
  echo "compose.yaml already exists — skip download (delete to re-fetch)."
fi

echo ""
echo "Next:"
echo "  1. cd $SAFELINE_DIR"
echo "  2. Create .env per Chaitin docs (see safeline/.env.example in repo for variable names)."
echo "  3. docker compose -f compose.yaml up -d"
echo "Docs: https://docs.waf.chaitin.com/en/GetStarted/Deploy"
