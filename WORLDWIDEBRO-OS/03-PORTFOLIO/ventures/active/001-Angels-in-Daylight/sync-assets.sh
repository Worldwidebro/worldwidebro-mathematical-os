#!/bin/bash
# Sync Angels in Daylight asset-manifest.json counts/timestamps against the real files on disk.
# No Convex step — venture-hub <-> real assets only, per 2026-07-04 session decision.
set -euo pipefail
cd "$(dirname "$0")"

MANIFEST="asset-manifest.json"
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

for key in product_images_clean product_images_clean_transparent; do
  path=$(jq -r ".asset_locations.${key}.path" "$MANIFEST")
  if [ ! -d "$path" ]; then
    echo "ERROR: $key path not found: $path" >&2
    exit 1
  fi
  count=$(find "$path" -type f -name "*.png" | wc -l | tr -d ' ')
  jq --arg c "$count" --arg ts "$TS" \
    ".asset_locations.${key}.count = (\$c | tonumber) | .asset_locations.${key}.last_synced = \$ts" \
    "$MANIFEST" > tmp.json && mv tmp.json "$MANIFEST"
done

csv_path=$(jq -r '.asset_locations.catalog_csv.path' "$MANIFEST")
if [ ! -f "$csv_path" ]; then
  echo "ERROR: catalog_csv path not found: $csv_path" >&2
  exit 1
fi
rows=$(tail -n +2 "$csv_path" | wc -l | tr -d ' ')
jq --arg c "$rows" --arg ts "$TS" \
  '.asset_locations.catalog_csv.count = ($c | tonumber) | .asset_locations.catalog_csv.last_synced = $ts' \
  "$MANIFEST" > tmp.json && mv tmp.json "$MANIFEST"

html_path=$(jq -r '.asset_locations.catalog_html.path' "$MANIFEST")
if [ ! -f "$html_path" ]; then
  echo "ERROR: catalog_html path not found: $html_path" >&2
  exit 1
fi
jq --arg ts "$TS" '.asset_locations.catalog_html.last_synced = $ts' "$MANIFEST" > tmp.json && mv tmp.json "$MANIFEST"

echo "Synced $(jq -r .venture_id "$MANIFEST"): $(jq -r '.asset_locations.product_images_clean.count' "$MANIFEST") clean images, $(jq -r '.asset_locations.catalog_csv.count' "$MANIFEST") SKUs"
