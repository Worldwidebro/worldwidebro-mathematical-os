#!/bin/bash
# Weekly RAG Re-Ingest — runs every Sunday
# Re-ingests vault + SKILL.md files into LightRAG

LOG_DIR="/tmp/iza-os-workflows"
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/rag-ingest.log"
DATE=$(date +%Y-%m-%d)
VAULT="/Users/acebless/Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault"
RAG_DIR="/Users/acebless/Documents/iza-os-rag-system"

echo "[$(date)] Starting weekly RAG re-ingest..." >> "$LOG"

# Activate venv and run vault ingest
cd "$RAG_DIR" && source .venv/bin/activate

echo "[$(date)] Ingesting vault..." >> "$LOG"
python3 -m src.ingest --source=vault >> "$LOG" 2>&1

echo "[$(date)] Ingesting SKILL.md files..." >> "$LOG"
python3 -m src.ingest --source=skills >> "$LOG" 2>&1

# Get doc count
DOC_COUNT=$(cat lightrag_data/kv_store_doc_status.json 2>/dev/null \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d))" 2>/dev/null || echo "unknown")

echo "[$(date)] Ingest complete. Docs indexed: $DOC_COUNT" >> "$LOG"

# Restart server if running
SERVER_PID=$(pgrep -f "src.serve" 2>/dev/null)
if [ -n "$SERVER_PID" ]; then
  echo "[$(date)] Restarting RAG server (PID $SERVER_PID)..." >> "$LOG"
  kill "$SERVER_PID" 2>/dev/null
  sleep 3
  python3 -m src.serve > /tmp/iza-rag-server.log 2>&1 &
  echo "[$(date)] RAG server restarted (PID $!)" >> "$LOG"
fi

# Write status note to vault inbox
NOTE="$VAULT/00-INBOX/rag-ingest-$DATE.md"
cat > "$NOTE" << EOF
---
type: system-status
date: $DATE
tags: [rag, ingest, system, automated]
---

# RAG Ingest Status — $DATE

**Docs indexed:** $DOC_COUNT
**Sources:** vault + SKILL.md files
**Server:** restarted

## Log
\`\`\`
$(tail -20 "$LOG")
\`\`\`
EOF

echo "[$(date)] Status note written to vault." >> "$LOG"
