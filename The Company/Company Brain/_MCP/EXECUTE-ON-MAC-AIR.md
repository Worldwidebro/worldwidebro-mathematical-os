# Execute OmniRoute Setup on Mac Air (100.121.17.63)

**Run these commands on Mac Air to connect all providers**

---

## Quick Setup (10 min)

### Step 1: Export Credentials
```bash
export OMNIROUTE_API_KEY="sk-89df9958a35a1f3e-a5b3fe-a1b77b99"
export ANTHROPIC_BASE_URL="http://100.87.214.70:20128"
export ANTHROPIC_AUTH_TOKEN="$OMNIROUTE_API_KEY"
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"
```

### Step 2: Health Check
```bash
curl -s -H "Authorization: Bearer $OMNIROUTE_API_KEY" \
  http://100.87.214.70:20128/api/health | jq .
```
✅ Expected: `"status": "healthy"`

### Step 3: Count Models (110 Total)
```bash
curl -s -H "Authorization: Bearer $OMNIROUTE_API_KEY" \
  http://100.87.214.70:20128/v1/models | jq '.data | length'
```

### Step 4: Generate Profiles
```bash
npm install -g omniroute  # If not installed

omniroute setup-claude \
  --remote http://100.87.214.70:20128 \
  --api-key $OMNIROUTE_API_KEY
```

### Step 5: Launch Claude Code
```bash
# Option A: Specific model
omniroute launch --profile glm52      # GLM 5.2 (heavy)
omniroute launch --profile kimi-k27   # Kimi K2.7 (balanced)
omniroute launch --profile glm-flash  # Flash (fast)

# Option B: Manual
export ANTHROPIC_BASE_URL="http://100.87.214.70:20128"
export ANTHROPIC_AUTH_TOKEN="sk-89df9958a35a1f3e-a5b3fe-a1b77b99"
claude
```

### Step 6: Verify in Claude Code
```
Inside Claude Code session:
/model  → Should list gateway models
```

---

## Connected Providers

| Provider | Count | Examples |
|----------|-------|----------|
| Alibaba GLM | 2 | glm/glm-5.2, glm/glm-4.7-flash |
| Moonshot Kimi | 3 | kimi/kimi-k2.7, kimi/kimi-k2.6 |
| DeepSeek | 3 | deepseek/deepseek-pro, deepseek-v3 |
| Qwen | 3 | qwen/qwen-max, qwen-plus, qwen-turbo |
| Ollama | 6 | qwen2.5-coder, nomic-embed, hermes3, llama3.1 |
| exo MLX | 120 | Qwen3.6, GLM, DeepSeek, etc. (1 exposed) |
| **TOTAL** | **110+** | All available via gateway |

---

## Make Persistent (~/.zshrc)

```bash
cat >> ~/.zshrc << 'ALIASES'

# OmniRoute
export OMNIROUTE_API_KEY="sk-89df9958a35a1f3e-a5b3fe-a1b77b99"
export ANTHROPIC_BASE_URL="http://100.87.214.70:20128"
export ANTHROPIC_AUTH_TOKEN="$OMNIROUTE_API_KEY"
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"

# Quick commands
alias claude-glm="omniroute launch --profile glm52"
alias claude-kimi="omniroute launch --profile kimi-k27"
alias claude-fast="omniroute launch --profile glm-flash"
alias omniroute-health="curl -s -H 'Authorization: Bearer $OMNIROUTE_API_KEY' http://100.87.214.70:20128/api/health | jq .status"
ALIASES

source ~/.zshrc
```

Then:
```bash
claude-glm    # Launch Claude Code with GLM 5.2
```

---

**Status: Ready to execute on Mac Air**
