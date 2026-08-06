---
name: OLLAMA-REMOTE-SSH-CONFIG
title: Ollama Remote Operation via Mac Studio SSH
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Ollama Remote Operation via Mac Studio SSH

**Goal**: Run Ollama on Mac Studio, access from Mac Air via SSH tunnel  
**Status**: Ready to configure

---

## Setup (One-time)

### 1. Mac Studio: Allow SSH from Mac Air

```bash
# On Mac Studio
sudo systemsetup -setremotelogin on

# Verify SSH server is running
ssh -V
# Output: OpenSSH_9.x (or later)
```

### 2. Mac Air: Create SSH Tunnel

```bash
# On Mac Air (or any client)
# Persistent tunnel: Ollama at localhost:11434
ssh -N -L 11434:localhost:11434 acebless@macstudio.local

# Or: Background tunnel
ssh -f -N -L 11434:localhost:11434 acebless@macstudio.local
```

### 3. Test Connection

```bash
# On Mac Air
curl http://localhost:11434/api/tags

# Output: {"models": [{"name": "qwen3:8b"}, {"name": "llama3.1"}]}
```

---

## Usage: Python via Remote Ollama

```python
import requests
import json

# Points to Mac Air's SSH tunnel → Mac Studio's Ollama
def remote_ollama_embed(text):
    response = requests.post(
        "http://localhost:11434/api/embed",
        json={"model": "nomic-embed-text", "input": text},
        timeout=30
    )
    return response.json()["embeddings"]

# Or: LangChain/LlamaIndex integration
from langchain.llms import Ollama
llm = Ollama(base_url="http://localhost:11434", model="qwen3:8b")
```

---

## Continuous Operation

### Keep Tunnel Alive

```bash
# Option A: Screen/tmux session
screen -S ollama-tunnel
ssh -N -L 11434:localhost:11434 acebless@macstudio.local
# Detach: Ctrl+A, D

# Option B: LaunchAgent (auto-start on login)
cat > ~/Library/LaunchAgents/com.ollama.ssh-tunnel.plist << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.ollama.ssh-tunnel</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/bin/ssh</string>
    <string>-N</string>
    <string>-L</string>
    <string>11434:localhost:11434</string>
    <string>acebless@macstudio.local</string>
  </array>
  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>
  <key>StandardErrorPath</key>
  <string>/tmp/ollama-tunnel.err</string>
  <key>StandardOutPath</key>
  <string>/tmp/ollama-tunnel.log</string>
</dict>
</plist>

# Load it
launchctl load ~/Library/LaunchAgents/com.ollama.ssh-tunnel.plist
```

### Verify Tunnel Status

```bash
# Check if tunnel is alive
ps aux | grep "ssh -N -L"

# Check for errors
cat /tmp/ollama-tunnel.log
cat /tmp/ollama-tunnel.err
```

---

## For Continuous Work

**Agents + LightRAG can now:**
- Fetch embeddings from Mac Studio Ollama (via tunnel)
- Run inference on qwen3:8b (continuous)
- Store vectors in Qdrant
- Query Neo4j locally

**No changes needed** in existing code — just keep tunnel open.

---

## Status

- [ ] Enable SSH on Mac Studio
- [ ] Create SSH tunnel on Mac Air
- [ ] Test curl connection
- [ ] (Optional) Set up LaunchAgent for auto-start
- [ ] Verify Python can reach remote Ollama
- [ ] Keep tunnel open during development
