# Claude Code ↔ OmniRoute Gateway Integration

**Status:** Ready for setup  
**Gateway:** http://100.87.214.70:20128  
**Local OmniRoute:** bolt://localhost:20128  
**Auth:** OMNIROUTE_API_KEY from OmniRoute dashboard

---

## Quick Start (Local OmniRoute)

### Launch Claude Code via OmniRoute
```bash
# Auto-detects active OmniRoute context
omniroute launch

# Or explicit local gateway
omniroute launch --remote http://100.87.214.70:20128 --api-key oma_live_xxx
```

### Generate Model Profiles
```bash
# Creates ~/.claude/profiles/<model-name>/settings.json
omniroute setup-claude

# Dry run (preview without writing)
omniroute setup-claude --dry-run

# Only specific providers
omniroute setup-claude --only glm,kimi,deepseek

# Remote VPS
omniroute setup-claude --remote http://100.87.214.70:20128 --api-key oma_live_xxx
```

### Launch Specific Model Profile
```bash
# After setup-claude, launch with a specific model
omniroute launch --profile glm52        # GLM 5.2
omniroute launch --profile kimi-k27     # Kimi K2.7
omniroute launch --profile deepseek-pro # DeepSeek Pro
```

---

## Environment Variables (Claude Code ← OmniRoute)

Set **once at startup**, then restart Claude Code.

| Variable | Purpose | Example |
|----------|---------|---------|
| `ANTHROPIC_BASE_URL` | Gateway root (no /v1 suffix) | `http://100.87.214.70:20128` |
| `ANTHROPIC_AUTH_TOKEN` | OmniRoute API key (Bearer) | `oma_live_xxx...` |
| `ANTHROPIC_API_KEY` | Alternative auth (x-api-key header) | `oma_live_xxx...` |
| `ANTHROPIC_MODEL` | Force specific model | `glm/glm-5.2` |
| `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY` | List gateway models in /model picker | `1` |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | Cap output tokens per response | `65536` |
| `CLAUDE_CODE_AUTO_COMPACT_WINDOW` | Auto-compact at token threshold | `190000` |

**Note:** If both `ANTHROPIC_AUTH_TOKEN` and `ANTHROPIC_API_KEY` are set, `ANTHROPIC_AUTH_TOKEN` wins (Bearer token).

---

## Profile Generation

### Profile File Location
```
~/.claude/profiles/
├── glm52/
│   ├── settings.json        # Model: glm/glm-5.2
│   └── history/             # Session history
├── kimi-k27/
│   └── settings.json        # Model: kimi/kimi-k2.7
├── deepseek-pro/
│   └── settings.json        # Model: deepseek/deepseek-pro
└── ...
```

### Example Profile (settings.json)
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

**Important:** Auth token is NOT stored in profile. Pass via:
- `omniroute launch --profile <name>` (auto-injects token)
- Export `ANTHROPIC_AUTH_TOKEN` manually

---

## Model Tier Routing (Advanced)

Route to different models by capability tier:

```bash
# Set in ~/.zshrc or environment
export ANTHROPIC_DEFAULT_OPUS_MODEL="glm/glm-5.2"        # Heavy tasks
export ANTHROPIC_DEFAULT_SONNET_MODEL="kimi/kimi-k2.6"   # Balanced
export ANTHROPIC_DEFAULT_HAIKU_MODEL="glm/glm-4.7-flash" # Fast
```

Or in profile settings.json:
```json
{
  "env": {
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm/glm-5.2",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "kimi/kimi-k2.6",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm/glm-4.7-flash"
  }
}
```

---

## Auto-Sync Profiles (Optional)

OmniRoute can auto-regenerate profiles when provider catalog changes:

```bash
# Enable via CLI dashboard: "CLI profile auto-sync"
# Or environment variable:
export OMNIROUTE_AUTO_SYNC_CLAUDE_PROFILES=1

# Must also enable config writes (default: on)
export CLI_ALLOW_CONFIG_WRITES=1
```

When enabled:
- ✅ New/renamed models get profiles automatically
- ✅ Only writes profile files (never touches ~/.claude/settings.json)
- ✅ Default Claude config unchanged

---

## Remote Mode (VPS OmniRoute)

### Connect to Remote OmniRoute
```bash
# One-time connection setup
omniroute connect http://192.168.0.15:20128 --api-key oma_live_xxx

# Now all omniroute commands target remote:
omniroute launch                  # Uses remote OmniRoute
omniroute setup-claude           # Generates profiles for remote
```

### Launch with Remote Profile
```bash
omniroute launch --profile kimi-k27
# Auto-injects remote token + base URL
```

### Override Per-Invocation
```bash
omniroute launch --profile glm52 \
  --remote http://192.168.0.15:20128 \
  --api-key oma_live_xxx
```

---

## Troubleshooting

### Issue: Claude Code still uses default API
**Problem:** `ANTHROPIC_BASE_URL` has `/v1` suffix  
**Solution:** Remove `/v1`, only base URL:
```bash
# ❌ WRONG
export ANTHROPIC_BASE_URL="http://100.87.214.70:20128/v1"

# ✅ CORRECT
export ANTHROPIC_BASE_URL="http://100.87.214.70:20128"

# Restart Claude Code (env read once at startup)
claude
```

### Issue: Model picker empty / missing gateway models
**Problem:** Gateway models not showing in `/model` picker  
**Solution:** Requires Claude Code v2.1.129+ and gateway discovery enabled:
```bash
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1

# Force non-claude* model:
export ANTHROPIC_MODEL="glm/glm-5.2"

# Restart Claude Code
claude
```

### Issue: Authentication failed
**Problem:** Profile has no token (tokens never stored)  
**Solution:** Use `omniroute launch --profile <name>` (auto-injects) or:
```bash
export ANTHROPIC_AUTH_TOKEN="oma_live_xxx"
CLAUDE_CONFIG_DIR=~/.claude/profiles/glm52 claude
```

### Issue: Profiles not isolated
**Problem:** Multiple profiles interfere with each other  
**Solution:** Verify correct config dir:
```bash
# Should print the profile path
echo $CLAUDE_CONFIG_DIR
# Expected: ~/.claude/profiles/<model-name>
```

---

## Company Brain Setup (Mac Studio)

### Current State
- ✅ OmniRoute running at http://100.87.214.70:20128
- ✅ 110 tools available
- ✅ Model catalog: GLM 5.2, Kimi K2.7, DeepSeek, etc.
- ⏳ Claude Code profiles: TO CREATE

### Next Steps

1. **Generate profiles** (2 min):
   ```bash
   omniroute setup-claude --remote http://100.87.214.70:20128 --api-key $OMNIROUTE_API_KEY
   ```

2. **Launch via OmniRoute** (1 min):
   ```bash
   omniroute launch --profile glm52  # Launch Claude Code with GLM 5.2
   ```

3. **Verify gateway in Claude Code**:
   - Type `/model` → should list gateway models
   - Should show: `glm/glm-5.2`, `kimi/kimi-k2.7`, `deepseek/deepseek-pro`, etc.

4. **Create model tier shortcuts** (optional):
   ```bash
   # Add to ~/.zshrc for quick access
   alias claude-heavy="omniroute launch --profile glm52"
   alias claude-fast="omniroute launch --profile glm-flash"
   alias claude-balanced="omniroute launch --profile kimi-k27"
   ```

---

## Architecture

```
Claude Code (local session)
    ↓ (with ANTHROPIC_BASE_URL + token)
OmniRoute Gateway (http://100.87.214.70:20128)
    ↓
Provider Router
    ├─ GLM (Alibaba)
    ├─ Kimi (Moonshot)
    ├─ DeepSeek
    ├─ Qwen (Alibaba)
    └─ ...99+ more
```

**Benefits:**
✅ Single CLI for multiple models  
✅ Automatic fallback/retry  
✅ Cost optimization (route to cheapest)  
✅ Unified telemetry/tracing  

---

## Integration Checklist

- [ ] OmniRoute running (`docker ps | grep omniroute`)
- [ ] OMNIROUTE_API_KEY exported (`echo $OMNIROUTE_API_KEY`)
- [ ] Profiles generated (`omniroute setup-claude`)
- [ ] `~/.claude/profiles/` directory created
- [ ] Test launch: `omniroute launch --profile glm52`
- [ ] Verify `/model` shows gateway models in Claude Code
- [ ] Create aliases for quick access (optional)

**Expected Time:** 5-10 minutes

---

**Authority:** Infrastructure Control Plane (CP-027) + Gateway Integration  
**Next:** Execute setup on Mac Studio
