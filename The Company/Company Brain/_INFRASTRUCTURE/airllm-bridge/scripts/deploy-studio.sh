#!/usr/bin/env bash
# Deploy AirLLM bridge to Mac Studio over Tailscale SSH and start it.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REMOTE_HOST="${REMOTE_HOST:-mac-studio}"
REMOTE_DIR="${REMOTE_DIR:-/Volumes/LaCie/company-brain-services/airllm-bridge}"
SHARDS="${AIRLLM_SHARDS_PATH:-/Volumes/LaCie/airllm-shards}"

echo "==> sync → ${REMOTE_HOST}:${REMOTE_DIR}"
ssh -o BatchMode=yes -o ConnectTimeout=10 "$REMOTE_HOST" "mkdir -p '$REMOTE_DIR' '$SHARDS'"
rsync -az --delete \
  --exclude '.venv' --exclude '__pycache__' --exclude '.env' \
  "$ROOT/" "$REMOTE_HOST:$REMOTE_DIR/"

ssh -o BatchMode=yes "$REMOTE_HOST" bash -s <<REMOTE
set -euo pipefail
cd "$REMOTE_DIR"
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
# Real weights path — install AirLLM + MLX on Apple Silicon
pip install -U airllm mlx torch || true
if [[ ! -f .env ]]; then
  cp .env.example .env
  # Prefer real inference on Studio
  sed -i '' 's/^AIRLLM_MOCK=.*/AIRLLM_MOCK=0/' .env || true
fi
mkdir -p "$SHARDS" logs
# Stop prior instance
if [[ -f logs/airllm-bridge.pid ]]; then
  kill "\$(cat logs/airllm-bridge.pid)" 2>/dev/null || true
fi
source .venv/bin/activate
set -a; source .env; set +a
export AIRLLM_SHARDS_PATH="$SHARDS"
nohup python server.py > logs/airllm-bridge.log 2>&1 &
echo \$! > logs/airllm-bridge.pid
sleep 2
curl -sS -m 5 "http://127.0.0.1:\${AIRLLM_PORT:-8020}/health" || true
echo
echo "PID=\$(cat logs/airllm-bridge.pid)"
REMOTE

echo "==> probe from Air over Tailscale"
curl -sS -m 8 "http://100.87.214.70:8020/health" || echo "(not reachable yet — check Studio log)"
echo
echo "Next: scripts/register-omniroute.sh"
