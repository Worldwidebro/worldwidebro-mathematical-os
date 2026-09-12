[[STARTHERE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[CLAUDE]]

# OmniRoute Credential Setup Guide

## ✅ Dashboard Access (READY NOW)

### Login Credentials
```
URL: http://100.87.214.70:20128/dashboard
Username: admin
Password: _.Thewave12
```

### Step 1: Access Dashboard
1. Open browser → http://100.87.214.70:20128/dashboard
2. Click **Login** (top right)
3. Enter credentials above
4. Click **Sign In**

---

## 🔧 Provider Configuration in Dashboard

Once logged in, follow these steps:

### Step 2: Navigate to Provider Management
1. Left sidebar → **Connections** or **Providers** section
2. You should see 6 providers listed:
   - lma (LiteLLM Arena)
   - cc (Anthropic Claude)
   - cmd (Command)
   - agentrouter
   - bb-web (Brave Browser)
   - copilot-web (Copilot Web)

### Step 3: Configure Each Provider

For **cc (Anthropic Claude):**
1. Click provider name → **Edit** or **Configure**
2. Paste Anthropic API key: `sk-ant-...` (from Bitwarden)
3. Click **Save** or **Test Connection**
4. Should show ✅ **Connected**

For **lma (LiteLLM Arena):**
1. Click provider → **Edit**
2. Enter LiteLLM API key (from Bitwarden or local LiteLLM instance)
3. URL should be: `http://100.87.214.70:4000` or `http://host.docker.internal:4000`
4. Click **Save**
5. Should show ✅ **Connected**

For **other providers:**
1. If you don't have credentials yet, mark as **Disabled** or leave blank
2. Can enable later when you have the keys

### Step 4: Verify Provider Health
1. Dashboard → **Provider Health** or **Status**
2. Should show connection status for each:
   ```
   ✅ cc (Anthropic) — Connected
   ✅ lma (LiteLLM) — Connected
   ⚠️  cmd — Disabled (no credentials)
   ⚠️  agentrouter — Disabled (no credentials)
   ⚠️  bb-web — Disabled (no credentials)
   ⚠️  copilot-web — Disabled (no credentials)
   ```

### Step 5: Model Aliasing (Optional)
1. Dashboard → **Model Aliases** or **Routing**
2. Create friendly names:
   - `default` → `lma/claude-haiku-4-5-20251001`
   - `best-chat` → `cc/claude-opus-4-1`
   - `fast` → `lma/claude-haiku-4-5-20251001`
3. Click **Save**

---

## 🧪 Test After Configuration

### Quick Test via Dashboard
1. Dashboard → **Playground** or **Test**
2. Select model: `cc/claude-haiku-4-5-20251001`
3. Enter prompt: "Say hello"
4. Click **Submit**
5. Should receive LLM response (not "No credentials" error)

### Test via API (Command Line)
```bash
# Test inference via API
curl -s http://100.87.214.70:20128/v1/messages \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "cc/claude-haiku-4-5-20251001",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 10
  }' | jq '.content[0].text'

# Expected: "Hello! How can I help?" (or similar)
```

### Verify via Logs
```bash
ssh macstudio "docker logs omniroute -f" | grep -i "connected\|provider"
# Should show: [PROVIDER] Anthropic connected ✓
```

---

## 🔐 API Keys Location (Bitwarden)

Need to retrieve these from Bitwarden:

| Provider | Key Name | Location |
|----------|----------|----------|
| **Anthropic** | ANTHROPIC_API_KEY | Bitwarden → "Anthropic API" or "Claude API" |
| **LiteLLM** | LITELLM_API_KEY | Bitwarden → "LiteLLM" or "OmniRoute" |
| **Others** | (if needed) | Check Bitwarden team vault |

**How to get from Bitwarden:**
```bash
# Option 1: Use Bitwarden CLI (if installed)
bw get item "Anthropic API" | jq '.login.password'

# Option 2: Open https://vault.bitwarden.com in browser
# Search for each API key
```

---

## 📋 Troubleshooting

### Dashboard won't load (404)
- Make sure OmniRoute container is running: `docker ps | grep omniroute`
- If not running: `docker --context macstudio start omniroute`
- Try again after 5 seconds

### Can't login (wrong password)
- Password might be case-sensitive
- Try: `_.Thewave12` (with dot and capital T)
- If still fails: See "Reset Password" section below

### Provider shows "Not Connected" after saving
- Check API key is valid (test in Bitwarden)
- Check network connectivity: `curl https://api.anthropic.com` (for Anthropic)
- For LiteLLM: Verify it's running on port 4000

### Still getting "No active credentials" error
- Reload dashboard (browser F5)
- Restart OmniRoute: `docker --context macstudio restart omniroute`
- Wait 10 seconds for provider health check to run
- Try API test again

---

## 🔄 Reset Password (If Needed)

If you can't login:

```bash
# SSH to Mac Studio
ssh macstudio

# Stop OmniRoute
docker --context macstudio stop omniroute

# Delete settings (forces password reset on next start)
docker exec omniroute rm -f /app/data/settings.json

# Restart (will use INITIAL_PASSWORD from env)
docker --context macstudio start omniroute

# Wait 5 seconds
sleep 5

# Now login with: admin / _.Thewave12
```

---

## ✅ Success Criteria

Once configured, you should be able to:

1. ✅ Login to dashboard with `admin` / `_.Thewave12`
2. ✅ See all 6 providers listed
3. ✅ At least 2 providers show ✅ **Connected** (cc + lma)
4. ✅ Models list shows 200+ (was 99 before, should grow)
5. ✅ Inference test returns LLM response (not "No credentials" error)
6. ✅ MCP tools count reaches 110+

---

## 📞 Support

If stuck:
1. Check provider logs: `docker logs omniroute -f`
2. Verify network: `curl http://100.87.214.70:20128/api/v1/models`
3. Check Bitwarden for actual API key values
4. Ask: "Is the provider URL correct?" (should be cloud endpoint, not local)

---

**Status:** Ready to configure  
**Time to full operation:** ~15-20 minutes (credential entry + testing)  
**Next step:** Open http://100.87.214.70:20128/dashboard and login
