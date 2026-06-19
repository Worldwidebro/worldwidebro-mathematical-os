# MCP Config Cleanup — 2026-06-09

## ✅ Completed

### MCP Config Simplified (`/Users/acebless/.mcp.json`)

**Kept (8 active servers):**
- `github` — repo access & automation
- `filesystem` — file operations across `/Users/acebless`, `/Volumes/T7 Shield`, `/Volumes/LaCie`
- `context7` — documentation lookup & code examples
- `memory` — agent memory persistence (`/Users/acebless/.claude/projects/-Users-acebless-Documents/memory/graph.json`)
- `puppeteer` — browser automation
- `clickup` — CRM integration (fixed: now uses `${CLICKUP_API_KEY}` env var instead of hardcoded token)
- `browseros` — GUI automation (port 9001)
- `openclaw` — Internal agent gateway to Mac Studio Qwen (100.87.214.70:3333)

**Removed (6 unused servers):**
- `supabase` ❌ (not using MCP; using Supabase SDK directly in Python)
- `brave-search` ❌ (redundant; using context7 instead)
- `dart` ❌ (not in your tech stack)
- `sqlite` ❌ (using DuckDB instead; path was also broken)
- `notion` ❌ (using Obsidian instead)
- `linear` ❌ (using ClickUp instead)
- `resend` ❌ (hardcoded API key = security risk; removed entirely)

### `.env` File Updated

**Added required API keys (placeholders to fill in):**
```
ANTHROPIC_API_KEY=your_anthropic_api_key
SUPABASE_URL=https://cyhzilqldouzgynacqpe.supabase.co
SUPABASE_KEY=your_supabase_service_key
GITHUB_TOKEN=your_github_personal_access_token
CLICKUP_API_KEY=126203176_86WLS7DNKWGZEF3S2Z5I0C1PF8H05V2N
```

## ⚠️ Still Needs Action

### Step 1: Fill in Your .env File
```bash
# Edit ~/.env and set actual values for:
ANTHROPIC_API_KEY=sk_...
GITHUB_TOKEN=ghp_...
SUPABASE_KEY=eyJhbGc...
```

### Step 2: Remove Duplicate Claude Installation
```bash
npm -g uninstall @anthropic-ai/claude-code
which claude  # Should return: /Users/acebless/.local/bin/claude
```

### Step 3: Fix BrowserOS Endpoint Conflict
You currently have BrowserOS on **both**:
- User scope: `http://127.0.0.1:9002/mcp` (old)
- Project scope: `http://127.0.0.1:9001/mcp` (current)

✅ We kept `9001` (project scope). Now remove the user scope:
```bash
claude mcp remove browseros -s user
```

Verify only one remains:
```bash
claude mcp list | grep browseros
```

### Step 4: Start Background Daemon
```bash
claude daemon start
claude daemon status
```

### Step 5: Restart Claude Code
This loads the new `.mcp.json` and `.env`.

## 📊 Final Status

| Area | Status | Impact |
|------|--------|--------|
| MCP Config | ✅ Cleaned (8→8, removed 6 unused) | Faster startup, fewer connection errors |
| .env | ✅ Structured (needs token values) | Enables MCP authentication |
| GitHub MCP | ⚠️ Ready (needs GITHUB_TOKEN) | Unblocks repo automation |
| ClickUp MCP | ✅ Fixed (now uses env var) | Unblocks CRM operations |
| BrowserOS | ⚠️ Ready (needs cleanup) | Unblocks GUI automation |
| Memory MCP | ✅ Fixed path | Unblocks agent memory persistence |
| Duplicate Install | ⚠️ Needs removal | Cleanup |
| Daemon | ⚠️ Not running | Startup speedup pending |

**Est. time to full green:** 5 minutes (fill env vars + restart)
