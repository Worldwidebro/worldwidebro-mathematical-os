[[STARTHERE]] | [[_INFRASTRUCTURE/README|Infrastructure Hub]] | [[CLAUDE]]

# OmniRoute URLs & Endpoints Reference

## 🌐 MAIN DASHBOARD & ACCESS

### Dashboard
- **URL:** http://100.87.214.70:20128/dashboard
- **Login:** admin / _.Thewave12
- **Purpose:** Provider configuration, model management, testing
- **Status:** ✅ Accessible (307 redirect → login)

---

## 🔌 API ENDPOINTS (No Auth Required)

### Model Discovery
- **List Models:** http://100.87.214.70:20128/api/v1/models
- **Purpose:** Get all 99+ available models
- **Method:** GET
- **Returns:** JSON array of models with providers

### Inference Endpoints

#### OpenAI Compatible (v1/messages)
- **URL:** http://100.87.214.70:20128/v1/messages
- **Method:** POST
- **Purpose:** Claude-style message completion
- **Example:**
```bash
curl -s http://100.87.214.70:20128/v1/messages \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "cc/claude-haiku-4-5-20251001",
    "messages": [{"role": "user", "content": "hi"}],
    "max_tokens": 10
  }'
```

#### OpenAI Compatible (v1/chat/completions)
- **URL:** http://100.87.214.70:20128/api/v1/chat/completions
- **Method:** POST
- **Purpose:** GPT-style chat completion
- **Example:**
```bash
curl -s http://100.87.214.70:20128/api/v1/chat/completions \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lma/gpt-4",
    "messages": [{"role": "user", "content": "hello"}]
  }'
```

#### Embeddings
- **URL:** http://100.87.214.70:20128/v1/embeddings
- **Method:** POST
- **Purpose:** Generate embeddings
- **Example:**
```bash
curl -s http://100.87.214.70:20128/v1/embeddings \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nomic-embed-text",
    "input": "Company Brain"
  }'
```

---

## 🛠️ ADMIN/DEBUG ENDPOINTS (Auth Required)

### Provider Management
- **List Providers:** http://100.87.214.70:20128/api/admin/providers
- **Provider Health:** http://100.87.214.70:20128/api/admin/provider-health
- **Purpose:** View all providers and their connection status
- **Method:** GET
- **Note:** Requires authentication

### MCP Tools
- **List Tools:** http://100.87.214.70:20128/mcp/tools
- **Invoke Tool:** http://100.87.214.70:20128/mcp/tools/invoke
- **Purpose:** Discover and execute MCP tools (110+ tools)
- **Expected:** 110+ tools after credential configuration

### Health & Status
- **Health Check:** http://100.87.214.70:20128/api/health
- **Status:** http://100.87.214.70:20128/api/status
- **Routing Logs:** http://100.87.214.70:20128/debug/last-routing
- **Network Test:** http://100.87.214.70:20128/debug/network-test

---

## 🔐 PROVIDER ENDPOINTS (Behind OmniRoute)

These are the actual provider APIs that OmniRoute routes to:

### Local Services (Within Docker Network)
- **LiteLLM:** http://100.87.214.70:4000 (or http://host.docker.internal:4000 from containers)
  - Also: http://civos_litellm:4000 (container DNS, if on same network)
- **Ollama:** http://100.87.214.70:11434 (or http://host.docker.internal:11434)
- **exo (MLX):** http://100.87.214.70:52415/v1

### Cloud Services (Via OmniRoute)
- **Anthropic Claude:** https://api.anthropic.com/v1
- **LiteLLM Arena:** https://litellm.ai (or internal instance)
- **Others:** Configured in OmniRoute dashboard

---

## 📊 MONITORING & OBSERVABILITY

### Logs
- **View logs:** `docker logs omniroute -f`
- **Tail logs:** `ssh macstudio "docker logs omniroute -f | grep -i provider"`
- **Filter by level:** `docker logs omniroute -f | grep -E '\[ERROR\]|\[WARN\]'`

### Dashboard Monitoring (When Logged In)
- **Provider Health:** http://100.87.214.70:20128/dashboard → Connections/Status
- **Model Availability:** http://100.87.214.70:20128/dashboard → Models
- **Routing Logs:** http://100.87.214.70:20128/dashboard → Analytics/Logs
- **Usage Stats:** http://100.87.214.70:20128/dashboard → Usage

---

## 🧪 QUICK TEST COMMANDS

### Test 1: Check if running
```bash
curl -s http://100.87.214.70:20128/api/v1/models | jq '.data | length'
# Expected: 99+
```

### Test 2: List available models
```bash
curl -s http://100.87.214.70:20128/api/v1/models | jq '.data[] | .id' | head -20
```

### Test 3: Simple inference (after credentials set)
```bash
curl -s http://100.87.214.70:20128/v1/messages \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "cc/claude-haiku-4-5-20251001",
    "messages": [{"role": "user", "content": "Hi"}],
    "max_tokens": 5
  }' | jq '.content[0].text'
# Expected: LLM response text
```

### Test 4: Check MCP tools
```bash
curl -s http://100.87.214.70:20128/mcp/tools | jq '.tools | length'
# Expected: 110+ (after full configuration)
```

---

## 📍 ALTERNATIVE ACCESS METHODS

### SSH into Mac Studio and test locally
```bash
ssh macstudio
curl -s http://localhost:20128/api/v1/models | jq '.data | length'
# Or use internal Docker network:
docker exec omniroute curl -s http://localhost:20128/api/v1/models
```

### Via Tailscale
If using Tailscale directly:
```bash
curl -s http://mac-studio.tailba9617.ts.net:20128/api/v1/models
# (Replace with your actual Tailscale hostname)
```

---

## 🔗 RELATED SERVICES (Used by OmniRoute)

### LiteLLM Config
- **File:** /Users/divinejohns/Iza-OS-Tree-of-Life/ops/infra/litellm-config.yaml
- **Port:** 4000
- **Purpose:** Model abstraction layer
- **Restart:** `docker restart civos_litellm`

### OmniRoute Config
- **File:** (Inside container at /app/data/settings.json after initialization)
- **Access:** Via dashboard → Settings
- **Reset:** Delete settings.json + restart

### Provider Credentials
- **Storage:** Bitwarden (recommended)
- **Or:** OmniRoute dashboard (encrypted in SQLite)

---

## 📝 ENDPOINT CHEAT SHEET

| Purpose | URL | Method | Auth | Status |
|---------|-----|--------|------|--------|
| **Login** | /dashboard | GET | No | ✅ |
| **List Models** | /api/v1/models | GET | No | ✅ |
| **Chat** | /v1/messages | POST | No | ✅ |
| **Chat (GPT style)** | /api/v1/chat/completions | POST | No | ✅ |
| **Embeddings** | /v1/embeddings | POST | No | ✅ |
| **Providers** | /api/admin/providers | GET | Yes | ✅ |
| **Provider Health** | /api/admin/provider-health | GET | Yes | ✅ |
| **MCP Tools** | /mcp/tools | GET | No | ✅ |
| **Health** | /api/health | GET | Yes | ✅ |
| **Status** | /api/status | GET | Yes | ✅ |

---

**Last Updated:** 2026-09-09  
**OmniRoute Version:** diegosouzapw/omniroute:latest  
**Container Status:** ✅ Running
