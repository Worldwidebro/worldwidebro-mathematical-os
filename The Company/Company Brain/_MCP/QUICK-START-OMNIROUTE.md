# OmniRoute ↔ Claude Code: Quick Start (5 Minutes)

**API Key:** ✅ CONFIGURED  
**Gateway:** http://100.87.214.70:20128  
**Status:** Ready to launch

---

## One-Time Setup (Mac Studio)

### 1. Export API Key
```bash
export OMNIROUTE_API_KEY="sk-89df9958a35a1f3e-a5b3fe-a1b77b99"
export ANTHROPIC_BASE_URL="http://100.87.214.70:20128"
export ANTHROPIC_AUTH_TOKEN="$OMNIROUTE_API_KEY"
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"
```

**Persistent:** Add to `~/.zshrc` or `~/.bashrc`:
```bash
# At end of file:
source /Users/acebless/Documents/The\ Company/Company\ Brain/_MCP/OMNIROUTE-API-KEY-SETUP.sh
```

### 2. Verify Connection
```bash
# Health check
curl -s http://100.87.214.70:20128/api/health | jq .

# List models
curl -s -H "Authorization: Bearer $OMNIROUTE_API_KEY" \
  http://100.87.214.70:20128/v1/models | jq '.data[] | {id, owned_by}'
```

### 3. Generate Claude Code Profiles
```bash
omniroute setup-claude --remote http://100.87.214.70:20128 --api-key $OMNIROUTE_API_KEY
```

Expected output:
```
✓ glm52/settings.json       → glm/glm-5.2 (heavy)
✓ glm-flash/settings.json   → glm/glm-4.7-flash (fast)
✓ kimi-k27/settings.json    → kimi/kimi-k2.7 (balanced)
✓ deepseek-pro/settings.json → deepseek/deepseek-pro
...
```

---

## Launch Claude Code

### Option 1: Default Profile
```bash
omniroute launch --profile glm52
```
→ Launches Claude Code with GLM 5.2

### Option 2: Kimi K2.7 (Balanced)
```bash
omniroute launch --profile kimi-k27
```

### Option 3: Fast Model (Flash)
```bash
omniroute launch --profile glm-flash
```

### Option 4: Manual Environment
```bash
export ANTHROPIC_BASE_URL="http://100.87.214.70:20128"
export ANTHROPIC_AUTH_TOKEN="sk-89df9958a35a1f3e-a5b3fe-a1b77b99"
export ANTHROPIC_MODEL="glm/glm-5.2"
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"

claude
```

---

## In Claude Code Session

### Verify Gateway Connection
```
$ /model
→ Should show gateway models:
  - glm/glm-5.2
  - kimi/kimi-k2.7
  - deepseek/deepseek-pro
  - ... and others

$ echo $ANTHROPIC_BASE_URL
→ http://100.87.214.70:20128

$ echo $ANTHROPIC_AUTH_TOKEN
→ sk-89df9958a35a1f3e-a5b3fe-a1b77b99
```

### Use Gateway Models
```
[Type] /model → Select from gateway list
→ Claude Code will use selected model via OmniRoute

All messages route through: http://100.87.214.70:20128/v1/messages
With authentication: Bearer sk-89df9958a35a1f3e-a5b3fe-a1b77b99
```

---

## Troubleshooting

### Gateway Returns 401
```bash
# Cause: Wrong API key
# Fix: export OMNIROUTE_AUTH_TOKEN="sk-89df9958a35a1f3e-a5b3fe-a1b77b99"
# Restart Claude Code
```

### /model Picker Empty
```bash
# Cause: CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY not set
# Fix: export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"
# Restart Claude Code
```

### OmniRoute Not Responding
```bash
# Check if container is running:
docker --context macstudio ps | grep omniroute

# Restart if needed:
docker --context macstudio restart omniroute

# Health check:
curl -s http://100.87.214.70:20128/api/health
```

---

## Quick Aliases (Add to ~/.zshrc)

```bash
# Health check
alias omniroute-health="curl -s http://100.87.214.70:20128/api/health | jq ."

# List models
alias omniroute-models="curl -s -H \"Authorization: Bearer sk-89df9958a35a1f3e-a5b3fe-a1b77b99\" http://100.87.214.70:20128/v1/models | jq '.data[] | {id, owned_by}'"

# Launch with profiles
alias claude-glm="omniroute launch --profile glm52"
alias claude-kimi="omniroute launch --profile kimi-k27"
alias claude-fast="omniroute launch --profile glm-flash"
```

Then just run:
```bash
claude-glm     # GLM 5.2 (heavy)
claude-kimi    # Kimi K2.7 (balanced)
claude-fast    # Flash (fast)
```

---

## Models Available

| Model | Provider | Use Case | Profile |
|-------|----------|----------|---------|
| glm/glm-5.2 | Alibaba | Heavy reasoning, coding | `glm52` |
| glm/glm-4.7-flash | Alibaba | Fast responses | `glm-flash` |
| kimi/kimi-k2.7 | Moonshot | Balanced (long context) | `kimi-k27` |
| kimi/kimi-k2.6 | Moonshot | Mobile-optimized | `kimi-k26` |
| deepseek/deepseek-pro | DeepSeek | General-purpose | `deepseek-pro` |
| deepseek/deepseek-v3 | DeepSeek | Latest version | `deepseek-v3` |
| qwen/qwen-max | Alibaba | General-purpose | `qwen-max` |
| ...99+ more | Various | Full catalog at /v1/models | — |

---

## Architecture Summary

```
Claude Code (local)
    ↓ (HTTP POST with Bearer token)
OmniRoute Gateway (http://100.87.214.70:20128)
    ↓ (routes to selected provider)
Provider (GLM, Kimi, DeepSeek, etc.)
    ↓ (returns response)
OmniRoute (exports trace to Langfuse)
    ↓
Claude Code (displays response)
```

**Benefits:**
- ✅ One gateway for 110+ models
- ✅ Automatic fallback if provider down
- ✅ Cost optimization built-in
- ✅ Usage tracking (Langfuse)
- ✅ No API key management per model

---

## Next Steps

1. **Export API key:** `source _MCP/OMNIROUTE-API-KEY-SETUP.sh`
2. **Generate profiles:** `omniroute setup-claude --remote ...`
3. **Launch Claude Code:** `omniroute launch --profile glm52`
4. **Verify in session:** `/model` → should list gateway models
5. **Use models:** Select from /model picker in Claude Code

**Total Time: 5 minutes**

---

**Documentation:**
- Full integration guide: [`CLAUDE-CODE-OMNIROUTE-INTEGRATION.md`](CLAUDE-CODE-OMNIROUTE-INTEGRATION.md)
- Architecture details: [`OMNIROUTE-CLAUDE-CODE-ARCHITECTURE.md`](OMNIROUTE-CLAUDE-CODE-ARCHITECTURE.md)
- MCP wiring: [`OMNIROUTE-MCP-WIRING.md`](OMNIROUTE-MCP-WIRING.md)

**Authority:** CP-027 (Infrastructure) + CP-034 (Engineering)
