#!/bin/bash
# Daily INBOX Triage — runs every morning
# Routes notes from 00-INBOX/ to correct vault folders

VAULT="/Users/acebless/Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault"
LOG_DIR="/tmp/iza-os-workflows"
mkdir -p "$LOG_DIR"

echo "[$(date)] Starting daily inbox triage..." >> "$LOG_DIR/triage.log"

/Users/acebless/.local/bin/claude \
  --dangerously-skip-permissions \
  -p "You are Claude Code running a daily INBOX triage for Ace (Antwuan Johns).

VAULT PATH: /Users/acebless/Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault

TODAY: $(date +%Y-%m-%d)

TASK:
1. List all files in 00-INBOX/ using Glob
2. For each file older than 24 hours, read its content
3. For each file, determine which folder it belongs in:
   - 01-CORE-SYSTEMS/ — architecture, integration docs, Iza-OS technical notes
   - 03-ACTIVE-PROJECTS/ — active work, in-progress builds
   - 04-KNOWLEDGE-GRAPHS/ — entity maps, relationship notes, graph data
   - 05-PROMPTS-LIBRARY/ — prompt templates, AI instructions
   - 06-WORKFLOWS/ — automation patterns, process docs
   - 07-BUSINESS-STRATEGY/ — revenue, ventures, business models
   - 08-ARCHIVE/ — done/resolved items, imported content, old notes
   - 00-INBOX/ — KEEP HERE if it needs Ace's attention before routing

4. Write a triage report to: 00-INBOX/triage-$(date +%Y-%m-%d).md
   Format:
   - List each file with recommended destination and one-line reason
   - Flag any items that need Ace's direct attention
   - Count: X items triaged, Y need attention, Z moved to archive

5. Move files that are clearly archivable (imported content, completed items, old notes)
   to 08-ARCHIVE/ using Bash mv command

Do NOT move files that are recent (< 24 hours) or flagged as needing attention.
Use direct, no-fluff language. No summaries at the end." \
  --allowedTools "Glob,Read,Write,Bash" \
  --cwd "/Users/acebless/Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault" \
  >> "$LOG_DIR/triage.log" 2>&1

echo "[$(date)] Inbox triage complete." >> "$LOG_DIR/triage.log"
