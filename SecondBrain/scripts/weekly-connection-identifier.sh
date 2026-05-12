#!/bin/bash
# Weekly Connection Identifier — runs every Monday
# Finds non-obvious patterns across vault folders

VAULT="/Users/acebless/Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault"
LOG_DIR="/tmp/iza-os-workflows"
mkdir -p "$LOG_DIR"

echo "[$(date)] Starting weekly connection identifier..." >> "$LOG_DIR/connections.log"

/Users/acebless/.local/bin/claude \
  --dangerously-skip-permissions \
  -p "You are Claude Code running a weekly vault synthesis for Ace (Antwuan Johns).

VAULT PATH: /Users/acebless/Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault

TODAY: $(date +%Y-%m-%d)

TASK:
1. List files in these folders and read the 3 most recently modified from each:
   - 00-INBOX/
   - 03-ACTIVE-PROJECTS/
   - 07-BUSINESS-STRATEGY/

2. After reading them, identify:
   a) Non-obvious patterns connecting ideas across the folders
   b) Contradictions between strategies or plans
   c) Cross-domain synthesis opportunities (where one idea from one folder unlocks another)
   d) One high-leverage insight that Ace might be missing

3. Write your findings to: 00-INBOX/connections-$(date +%Y-%m-%d).md

FORMAT for the output note:
- Direct, confident voice. Numbers-first. Short sentences.
- No AI buzzwords (no 'delve', 'tapestry', 'leverage' as verb, 'seamlessly')
- Lead with the most surprising finding
- End with 1-2 concrete next actions

Use Glob, Read, and Write tools to complete this task." \
  --allowedTools "Glob,Read,Write,Bash" \
  --cwd "/Users/acebless/Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault" \
  >> "$LOG_DIR/connections.log" 2>&1

echo "[$(date)] Connection identifier complete." >> "$LOG_DIR/connections.log"
