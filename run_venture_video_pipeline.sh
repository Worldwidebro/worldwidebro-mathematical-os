#!/bin/bash
# Gold-standard venture video pipeline: scripts + TTS + scenes + captions
set -euo pipefail

DOCS="/Users/acebless/Documents"
PY="${DOCS}/.venv-venture-video/bin/python"
if [[ ! -x "$PY" ]]; then
  /opt/homebrew/bin/python3.12 -m venv "${DOCS}/.venv-venture-video"
  "${DOCS}/.venv-venture-video/bin/pip" install -q edge-tts pillow
  PY="${DOCS}/.venv-venture-video/bin/python"
fi

cd "$DOCS"

VENTURE="${1:-1d84705c-8ebd-4c0c-83cf-cf383951b7bb}"
MODE="${2:-single}"
HF_FLAG=""
if [[ "${USE_HIGGSFIELD:-}" == "1" ]] || [[ "${HIGGSFIELD_ENABLED:-}" == "1" ]]; then
  HF_FLAG="--use-higgsfield"
fi

if [[ "$MODE" == "all" ]]; then
  "$PY" venture_script_engine.py --all-con --limit 5
  "$PY" venture_video_pipeline.py --all --limit 5 --regenerate-script $HF_FLAG
else
  "$PY" venture_script_engine.py --venture "$VENTURE"
  "$PY" venture_video_pipeline.py --venture "$VENTURE" --regenerate-script $HF_FLAG
fi

echo ""
echo "Done. Open: ${DOCS}/moneyprinter-output/${VENTURE}/output.mp4"
