---
name: _archive/mcp-browserclaw/README
title: [ARCHIVED]
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# [ARCHIVED]
This repository has been archived as part of Phase 2 OS consolidation.
All scaffolding templates have been moved to central template system.
Last archived: 2026-07-29
See: /Users/acebless/Documents/PHASE-2-COMPLETION.md

# BrowserClaw MCP Server

Expose BrowserClaw browser automation to Claude Code, Cursor, and other MCP-compatible AI tools.

## What This Does

Turns BrowserClaw's public HTTP endpoint into standardized MCP tools that agents can call:

```
User: "Book a meeting for next Thursday at 3pm"
  ↓
Claude/Cursor Agent
  ↓
BrowserClaw MCP Server
  ↓
BrowserClaw Public API
  ↓
Real browser automation
```

## Setup

### 1. Get BrowserClaw API Key

1. Install BrowserClaw: https://browseros.com/agents
2. Sign in to accounts (Gmail, Calendar, etc.)
3. Open BrowserClaw → MCP → Copy your API key + endpoint

### 2. Install MCP Server

```bash
cd /Users/acebless/Documents/mcp-browserclaw
cp .env.example .env
# Edit .env with your BrowserClaw endpoint and API key
pip install -r requirements.txt
```

### 3. Add to Claude Code

Edit `~/.claude/mcp-config.json`:

```json
{
  "mcpServers": {
    "browserclaw": {
      "command": "python",
      "args": ["/Users/acebless/Documents/mcp-browserclaw/server.py"],
      "env": {
        "BROWSERCLAW_ENDPOINT": "https://api.browseros.com/mcp",
        "BROWSERCLAW_API_KEY": "your-key-here"
      }
    }
  }
}
```

Restart Claude Code.

### 4. Add to Cursor

Edit `~/.cursor/mcp-config.json` (same structure as Claude Code):

```json
{
  "mcpServers": {
    "browserclaw": {
      "command": "python",
      "args": ["/Users/acebless/Documents/mcp-browserclaw/server.py"],
      "env": {
        "BROWSERCLAW_ENDPOINT": "https://api.browseros.com/mcp",
        "BROWSERCLAW_API_KEY": "your-key-here"
      }
    }
  }
}
```

Restart Cursor.

## Available Tools

| Tool | Purpose |
|------|---------|
| `browserclaw_navigate(url)` | Navigate to URL |
| `browserclaw_click(ref/selector)` | Click element |
| `browserclaw_fill(fields)` | Fill form |
| `browserclaw_screenshot()` | Capture page |
| `browserclaw_read()` | Extract as markdown |
| `browserclaw_wait(selector/text, timeout)` | Wait for element |
| `browserclaw_evaluate(js)` | Run JavaScript |
| `browserclaw_type(text)` | Type text |
| `browserclaw_press(key)` | Press key |
| `browserclaw_scroll(x, y)` | Scroll page |

## Example

```
User: "Find my calendar for next week and send me a summary"

Agent execution:
1. browserclaw_navigate("https://calendar.google.com")
2. browserclaw_wait(selector="[role='main']")
3. browserclaw_screenshot()
4. browserclaw_read()
5. Agent summarizes and sends email
```

## Troubleshooting

**"Connection refused"**
- Verify BROWSERCLAW_ENDPOINT (usually https://api.browseros.com/mcp)
- Check BROWSERCLAW_API_KEY is valid

**"Tool not found"**
- Restart Claude Code / Cursor after editing mcp-config.json
- Verify server process: `python server.py`

**"Element not found"**
- Use browserclaw_screenshot() first
- Use browserclaw_read() to see accessibility tree

## Standalone

```bash
export BROWSERCLAW_ENDPOINT=https://api.browseros.com/mcp
export BROWSERCLAW_API_KEY=your-key
python server.py
```

---

Status: ✅ Working
Date: 2026-07-24
