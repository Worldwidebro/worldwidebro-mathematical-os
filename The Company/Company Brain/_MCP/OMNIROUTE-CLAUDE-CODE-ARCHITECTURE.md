# OmniRoute ↔ Claude Code Architecture Wiring

**Status:** Ready for execution  
**Integration Point:** Messages API gateway  
**Gateway:** http://100.87.214.70:20128/v1  
**CLI Tool:** omniroute v3.8.50+  

---

## System Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                        Claude Code Session                      │
│  (Runs locally with ANTHROPIC_BASE_URL pointing to OmniRoute)   │
│                                                                  │
│  Environment:                                                    │
│  - ANTHROPIC_BASE_URL=http://100.87.214.70:20128 (no /v1)      │
│  - ANTHROPIC_AUTH_TOKEN=oma_live_xxx (Bearer token)             │
│  - ANTHROPIC_MODEL=glm/glm-5.2 (or any gateway model)           │
│  - CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1                │
│                                                                  │
└──────────────────┬───────────────────────────────────────────────┘
                   │
                   │ Messages API calls
                   ↓
┌────────────────────────────────────────────────────────────────┐
│              OmniRoute Gateway (v3.8.50)                        │
│         http://100.87.214.70:20128/v1/messages                 │
│                                                                  │
│  Routes messages to:                                            │
│  ├─ GLM 5.2, 4.7-flash (Alibaba)                               │
│  ├─ Kimi K2.7, K2.6 (Moonshot)                                 │
│  ├─ DeepSeek Pro, V3 (DeepSeek)                                │
│  ├─ Qwen Max, Plus (Alibaba)                                   │
│  ├─ Claude (via proxy)                                         │
│  └─ ...99+ models (110 total)                                  │
│                                                                  │
│  Features:                                                      │
│  ✓ Capability-based routing                                    │
│  ✓ Cost optimization                                           │
│  ✓ Fallback chains                                             │
│  ✓ Usage tracking (Langfuse integration)                       │
│  ✓ Model discovery (/v1/models endpoint)                       │
│  ✓ Telemetry + tracing                                        │
│                                                                  │
└────────────┬────────────────────────┬──────────────────┬────────┘
             │                        │                  │
             ↓                        ↓                  ↓
      ┌─────────────┐        ┌──────────────┐   ┌──────────────┐
      │ GLM Router  │        │ Kimi Router  │   │DeepSeek Route│
      │ (Alibaba)   │        │ (Moonshot)   │   │  (DeepSeek)  │
      └─────────────┘        └──────────────┘   └──────────────┘
```

---

## Messages API Gateway Flow

### Request Flow
```
1. Claude Code sends:
   POST http://100.87.214.70:20128/v1/messages
   Authorization: Bearer oma_live_xxx
   {
     "model": "glm/glm-5.2",
     "messages": [...],
     "max_tokens": 4096,
     ...
   }

2. OmniRoute gateway:
   ✓ Authenticates (Bearer token)
   ✓ Validates model availability
   ✓ Routes to selected provider
   ✓ Handles failures → fallback chain
   ✓ Records telemetry (Langfuse)

3. Provider responds:
   {
     "id": "msg_xxx",
     "content": [...],
     "usage": { "input_tokens": 123, "output_tokens": 456 },
     ...
   }

4. OmniRoute returns to Claude Code:
   ✓ Message content
   ✓ Usage statistics
   ✓ Trace ID (for Langfuse lookup)
```

---

## Environment Variables (Claude Code Startup)

| Variable | Value | Source |
|----------|-------|--------|
| `ANTHROPIC_BASE_URL` | `http://100.87.214.70:20128` | OmniRoute gateway (no /v1) |
| `ANTHROPIC_AUTH_TOKEN` | `oma_live_xxx` | OmniRoute dashboard (API key) |
| `ANTHROPIC_MODEL` | `glm/glm-5.2` | Model profile (or profile name) |
| `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY` | `1` | Enable `/model` picker discovery |
| `CLAUDE_CODE_AUTO_COMPACT_WINDOW` | `190000` | Auto-compact at 190K tokens |

**Set at startup** — Claude Code reads environment once.

---

## Model Profile Generation

### Command
```bash
omniroute setup-claude --remote http://100.87.214.70:20128 --api-key oma_live_xxx
```

### Output
Generates `~/.claude/profiles/<model-name>/settings.json`:
```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "model": "glm/glm-5.2",
  "effortLevel": "xhigh",
  "env": {
    "ANTHROPIC_BASE_URL": "http://100.87.214.70:20128",
    "ANTHROPIC_MODEL": "glm/glm-5.2",
    "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY": "1",
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "190000"
  }
}
```

### Profiles Created
```
~/.claude/profiles/
├── glm52/                 → glm/glm-5.2 (heavy)
├── glm-flash/             → glm/glm-4.7-flash (fast)
├── kimi-k27/              → kimi/kimi-k2.7 (balanced)
├── kimi-k26/              → kimi/kimi-k2.6 (mobile)
├── deepseek-pro/          → deepseek/deepseek-pro
├── deepseek-v3/           → deepseek/deepseek-v3
├── qwen-max/              → qwen/qwen-max
└── ...
```

---

## Gateway Model Discovery Endpoint

### Endpoint
```
GET http://100.87.214.70:20128/v1/models
Authorization: Bearer oma_live_xxx
```

### Response
```json
{
  "object": "list",
  "data": [
    {
      "id": "glm/glm-5.2",
      "object": "model",
      "owned_by": "alibaba",
      "permission": [],
      "created": 1725811200
    },
    {
      "id": "kimi/kimi-k2.7",
      "object": "model",
      "owned_by": "moonshot",
      ...
    },
    ...
  ]
}
```

### Claude Code Integration
When `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1`:
- `/model` command lists gateway models
- Non-claude* models appear in picker
- Pre-populated model names in profiles

---

## Launch Workflows

### Workflow 1: Auto-Detect (Recommended)
```bash
# After: omniroute connect http://100.87.214.70:20128
omniroute launch

# Resolves:
# - Base URL from active context
# - API token from scoped access token
# - Launches Claude Code with env vars set
```

### Workflow 2: Profile-Based
```bash
omniroute launch --profile glm52

# Launches Claude Code using:
# - CLAUDE_CONFIG_DIR=~/.claude/profiles/glm52
# - ANTHROPIC_MODEL=glm/glm-5.2
# - All env vars from profile settings.json
# - Auth token injected from active context
```

### Workflow 3: Manual Environment
```bash
export ANTHROPIC_BASE_URL="http://100.87.214.70:20128"
export ANTHROPIC_AUTH_TOKEN="oma_live_xxx"
export ANTHROPIC_MODEL="glm/glm-5.2"
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"
claude  # Launch Claude Code with env set
```

### Workflow 4: Profile + Environment Override
```bash
ANTHROPIC_MODEL="kimi/kimi-k2.7" \
  omniroute launch --profile glm52
# Uses profile from glm52 but overrides model to Kimi
```

---

## Model Tier System

### Tier Mapping (Optional)
```bash
export ANTHROPIC_DEFAULT_OPUS_MODEL="glm/glm-5.2"        # Tier: opus (heavy)
export ANTHROPIC_DEFAULT_SONNET_MODEL="kimi/kimi-k2.7"   # Tier: sonnet (mid)
export ANTHROPIC_DEFAULT_HAIKU_MODEL="glm/glm-4.7-flash" # Tier: haiku (fast)
```

### Usage in Code
```python
# Claude Code automatically routes based on tier
# (This is internal; users select via /model picker)
```

---

## Telemetry Integration (Langfuse)

### Tracing Flow
```
Claude Code
  ↓ (message request)
OmniRoute Gateway
  ↓ (with trace ID header)
Provider (GLM/Kimi/etc.)
  ↓ (response)
OmniRoute
  ↓ (exports trace to Langfuse)
Langfuse Dashboard (localhost:3003)
  ↓
Visible traces:
- Model: glm/glm-5.2
- Tokens: 234 input, 567 output
- Cost: $0.0047
- Duration: 1.2s
- Provider: Alibaba
```

---

## Execution Steps (Company Brain)

### Step 1: Verify Connectivity (2 min)
```bash
# Check OmniRoute health
curl -s http://100.87.214.70:20128/api/health | jq .

# Expected:
# {
#   "status": "healthy",
#   "version": "3.8.50",
#   "mcp_status": "connected"
# }
```

### Step 2: Generate Profiles (3 min)
```bash
# Export API key
export OMNIROUTE_API_KEY="oma_live_xxx"  # From OmniRoute dashboard

# Generate profiles
omniroute setup-claude --remote http://100.87.214.70:20128

# Verify
ls -la ~/.claude/profiles/
```

### Step 3: Launch Claude Code (1 min)
```bash
# Option A: Auto-detect
omniroute connect http://100.87.214.70:20128
omniroute launch

# Option B: Profile
omniroute launch --profile glm52

# Option C: Manual
export ANTHROPIC_BASE_URL="http://100.87.214.70:20128"
export ANTHROPIC_AUTH_TOKEN="oma_live_xxx"
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"
claude
```

### Step 4: Verify Gateway in Claude Code (1 min)
```
Inside Claude Code session:
/model       # Should list: glm/glm-5.2, kimi/kimi-k2.7, etc.
echo $ANTHROPIC_BASE_URL  # Should print: http://100.87.214.70:20128
```

**Total Setup Time: 7 minutes**

---

## Quick Reference

| Task | Command |
|------|---------|
| Health check | `curl http://100.87.214.70:20128/api/health` |
| List models | `curl http://100.87.214.70:20128/v1/models` |
| Generate profiles | `omniroute setup-claude --remote http://100.87.214.70:20128` |
| Launch with profile | `omniroute launch --profile glm52` |
| List profiles | `ls ~/.claude/profiles/` |
| Manual launch | `ANTHROPIC_BASE_URL=... ANTHROPIC_AUTH_TOKEN=... claude` |
| View traces | Open http://localhost:3003 (Langfuse) |

---

## Troubleshooting

### Gateway returns 401 Unauthorized
```bash
# Cause: ANTHROPIC_AUTH_TOKEN not set or wrong
# Fix: export ANTHROPIC_AUTH_TOKEN="oma_live_xxx"
```

### /model picker empty
```bash
# Cause: CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY not set
# Fix: export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1
# Restart Claude Code (env read once at startup)
```

### Profile doesn't launch
```bash
# Cause: omniroute CLI not installed
# Fix: npm install -g omniroute
```

---

## Architecture Authority

- **Control Plane:** CP-027 (Infrastructure)
- **Layer:** Layer 15 (Execution + Observability)
- **Integration:** MCP Server (fastmcp-server) ↔ OmniRoute Gateway ↔ Claude Code
- **Status:** Ready for execution

**Next:** Run setup-claude-omniroute.sh on Mac Studio
