#!/bin/bash
# Direct vault capture — no N8N required
# Usage: ./vault-capture.sh "Title" "Content" "tag1,tag2"

VAULT="/Users/acebless/Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault"
TITLE="${1:-capture}"
CONTENT="${2:-}"
TAGS="${3:-capture}"
DATE=$(date +%Y-%m-%d)
DATETIME=$(date +%Y-%m-%d-%H%M%S)
FILE="$VAULT/00-INBOX/capture-$DATETIME.md"

cat > "$FILE" << EOF
---
type: capture
date: $DATE
tags: [$TAGS]
source: cli
---

# $TITLE

$CONTENT
EOF

echo "✓ Captured to: $FILE"
