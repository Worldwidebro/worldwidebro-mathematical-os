#!/usr/bin/env bash
# Register Studio AirLLM bridge as OmniRoute OpenAI-compatible provider + refresh combo.
set -euo pipefail

BASE_URL="${AIRLLM_OR_BASE_URL:-http://100.87.214.70:8020/v1}"
MODEL="${AIRLLM_MODEL:-Qwen/Qwen2.5-Coder-7B-Instruct}"
NAME="${AIRLLM_OR_NAME:-Studio AirLLM}"

echo "==> health check $BASE_URL/../health"
curl -sf -m 8 "${BASE_URL%/v1}/health" | head -c 400 || {
  echo "Bridge not healthy at ${BASE_URL%/v1} — deploy first (scripts/deploy-studio.sh) or run mock locally."
  exit 1
}
echo

# Remove prior connection with same name if present (best-effort)
omniroute providers remove "$NAME" --yes 2>/dev/null || true

omniroute providers add openai \
  --name "$NAME" \
  --default-model "$MODEL" \
  --priority 40 \
  --credential "airllm-local" \
  --provider-specific-data "{\"baseUrl\":\"$BASE_URL\"}" \
  --yes

omniroute providers edit "$NAME" --active --default-model "$MODEL" 2>/dev/null || true

# Ensure continuous-coding combo exists and includes AirLLM model last
omniroute combo delete continuous-coding --yes 2>/dev/null || true
omniroute combo create continuous-coding \
  --strategy priority \
  --model qwen2.5-coder:14b \
  --model llama3.1:8b \
  --model "$MODEL" \
  --model mlx-community/Qwen3-Coder-480B-A35B-Instruct-4bit

omniroute combo switch continuous-coding

echo
echo "Active combo → continuous-coding"
echo "Clients should use OPENAI_BASE_URL=http://127.0.0.1:20128/v1 (OmniRoute), not :8020 directly."
omniroute providers list | rg -i 'ollama|airllm|exo' || omniroute providers list
