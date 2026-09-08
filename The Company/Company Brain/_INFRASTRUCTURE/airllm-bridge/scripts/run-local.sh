#!/usr/bin/env bash
# Run AirLLM bridge locally (mock by default for wiring tests).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ ! -d .venv ]]; then
  python3 -m venv .venv
  # shellcheck disable=SC1091
  source .venv/bin/activate
  pip install -U pip
  pip install -r requirements.txt
else
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

export AIRLLM_MOCK="${AIRLLM_MOCK:-1}"
export AIRLLM_HOST="${AIRLLM_HOST:-127.0.0.1}"
export AIRLLM_PORT="${AIRLLM_PORT:-8020}"
[[ -f .env ]] && set -a && source .env && set +a

echo "AirLLM bridge → http://${AIRLLM_HOST}:${AIRLLM_PORT}/v1  (MOCK=${AIRLLM_MOCK})"
exec python server.py
