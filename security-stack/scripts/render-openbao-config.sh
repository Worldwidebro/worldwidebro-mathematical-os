#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

ENV_FILE="${ROOT}/docker/.env"
if [[ ! -f "$ENV_FILE" ]]; then
  echo "Missing $ENV_FILE — copy docker/.env.example to docker/.env" >&2
  exit 1
fi

set -a
# shellcheck disable=SC1091
source "$ENV_FILE"
set +a

: "${DB_USER:?}"
: "${DB_PASSWORD:?}"
: "${POSTGRES_DB:-openbao}"

export DB_USER DB_PASSWORD POSTGRES_DB

if ! command -v envsubst >/dev/null 2>&1; then
  echo "envsubst not found (macOS: brew install gettext)" >&2
  exit 1
fi

OUT="${ROOT}/config/openbao/config.hcl"
envsubst < "${ROOT}/config/openbao/config.hcl.template" > "$OUT"
echo "Wrote ${OUT}"
