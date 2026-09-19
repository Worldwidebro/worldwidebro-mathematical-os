# Runbook: Authentication/API Key Invalid

**Status:** Task classification fails with 401. Falls back to keyword matching.

**MTTR:** 2-5 minutes | **Severity:** Medium | **Owned By:** Security Team

---

## Symptoms

**Operational Impact:**
- Task classification always returns keyword-based fallback (low accuracy)
- Logs show "401 Unauthorized" on LLM API calls
- `/api/orchestrator/classify-task` succeeds but uses poor classification
- Monitoring shows classification confidence < 0.3 (normal > 0.8)

**Monitoring Alerts:**
- Claude/Haiku API authentication failures
- Fallback classification in use
- Classification confidence below threshold for 2+ hours

**User Reports:**
- "My tasks are getting misclassified"
- "Discovery finding wrong agents"
- "Logs show API key errors"

---

## Root Cause Analysis

### Step 1: Check Auth Provider Configuration
```bash
# Check which auth provider is configured
grep -r "auth_provider\|api_key\|api_token" _REFERENCE/INFRASTRUCTURE-STATUS* \
  services/omniroute/config.yaml \
  .env.production 2>/dev/null | head -20

# Expected: Shows configured provider (claude-haiku-auth, etc.)
```

### Step 2: Verify Credential Storage
```bash
# Check if credentials in Bitwarden
# (Manual step - cannot auto-access Bitwarden without user intervention)

# Alternative: Check if key is in environment
echo $CLAUDE_API_KEY
echo $ANTHROPIC_API_KEY
echo $HAIKU_AUTH_TOKEN

# Expected: Should print key (sensitive, be careful)
# If: Empty or "PLACEHOLDER" → key not loaded
```

### Step 3: Check Credential Freshness
```bash
# Test the API key by making a simple request
curl -s -X POST https://api.anthropic.com/v1/messages \
  -H "x-api-key: $CLAUDE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-haiku-4.5-20251001",
    "max_tokens": 100,
    "messages": [{"role": "user", "content": "test"}]
  }' | jq '.error'

# Expected: null (no error)
# If: {"type":"authentication_error","message":"Invalid API key"} → key invalid/expired
```

**Findings:**
- [ ] API key valid → issue is elsewhere (network, rate limit)
- [ ] API key invalid → key expired or rotated (see Resolution)
- [ ] Connection refused → network blocked or API down
- [ ] Rate limited (429) → quota exceeded (see "Prevention")

### Step 4: Check When Key Was Last Rotated
```bash
# Check git history for auth changes
git log --oneline --grep="auth\|api.key\|credential" | head -10

# Check Bitwarden (manual)
# Look at "Last Modified" date on credential
# If > 90 days → may have expired

# Check OmniRoute logs
ssh macstudio
docker logs omniroute 2>&1 | grep -i "auth\|401\|unauthorized" | tail -20
```

**Findings:**
- [ ] Key modified recently (< 7 days) → likely valid
- [ ] Key modified > 90 days ago → likely expired/rotated
- [ ] No auth failures in logs → issue elsewhere

### Step 5: Check API Provider Status
```bash
# Check if Claude/Haiku API is operational
# Go to https://status.anthropic.com (manual check)
# Or check OmniRoute health endpoint:
curl http://100.87.214.70:20128/health | jq '.services.claude_api'

# Expected: {"status": "ok", "latency_ms": 150}
# If: {"status": "unavailable"} → API is down
```

---

## Immediate Action

### Option 1: Verify and Update Credential (Low risk)
```bash
# Step 1: Get current key from Bitwarden (manual)
# - Open Bitwarden at https://vault.bitwarden.com
# - Find credential "Claude API Key" or "Anthropic API Key"
# - Copy the value

# Step 2: Verify it's correct by testing
curl -s -X POST https://api.anthropic.com/v1/messages \
  -H "x-api-key: YOUR_API_KEY_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-haiku-4.5-20251001",
    "max_tokens": 50,
    "messages": [{"role": "user", "content": "test"}]
  }' | jq '.id'

# Expected: Should see message ID in response (looks like "msg_...")
# If: See error → key is invalid

# Step 3: Update OmniRoute configuration
# Option A: Update environment variable
ssh macstudio
export CLAUDE_API_KEY="YOUR_VALID_KEY"
docker-compose -f services/omniroute/docker-compose.yml restart omniroute

# Option B: Update .env file
cd services/omniroute
echo "CLAUDE_API_KEY=YOUR_VALID_KEY" >> .env.production
docker-compose restart omniroute
```

### Option 2: Switch to Fallback Classifier (Immediate relief)
```bash
# In OmniRoute config
orchestrator:
  classification:
    mode: 'keyword_fallback'  # Use keyword matching temporarily
    timeout_fallback: true    # Always fallback on timeout
    
# Restart service
docker-compose -f services/omniroute/docker-compose.yml restart omniroute

# NOTE: Fallback is lower quality; fix auth ASAP
```

### Option 3: Request New API Key
```bash
# If key has expired or been revoked:
# 1. Go to https://console.anthropic.com
# 2. Navigate to API Keys
# 3. Generate a new key
# 4. Update in Bitwarden
# 5. Restart OmniRoute (see Option 1, Step 3)

# Verify new key works before committing
curl -s -X POST https://api.anthropic.com/v1/messages \
  -H "x-api-key: NEW_KEY_HERE" \
  -H "Content-Type: application/json" \
  -d '{"model": "claude-haiku-4.5-20251001", "max_tokens": 50, "messages": [{"role": "user", "content": "test"}]}' | jq '.id'
```

---

## Resolution

### Step 1: Determine Root Cause
**From analysis above:**

**If:** Key is expired
- Action: Request new key from Anthropic console
- Timeline: Immediate (new key available instantly)

**If:** Key is invalid/wrong
- Action: Verify against Bitwarden, confirm in Anthropic console
- Timeline: 2-5 minutes

**If:** Key never set
- Action: Generate new key and configure
- Timeline: 5 minutes

**If:** API provider is down
- Action: Monitor status page, use fallback temporarily
- Timeline: Wait for provider recovery (typically < 1 hour)

### Step 2: Update All References
```bash
# After confirming new key works, update everywhere it appears:

# 1. Update Bitwarden
# (Manual via https://vault.bitwarden.com)

# 2. Update OmniRoute environment
ssh macstudio
cd services/omniroute
export CLAUDE_API_KEY="NEW_KEY"

# 3. Update Docker secrets (if using Docker secrets)
echo "NEW_KEY" | docker secret create claude_api_key -

# 4. Verify OmniRoute has new key
docker-compose logs omniroute | grep -i "auth\|connected\|ready"

# Expected: Should see "API authenticated" or similar
```

### Step 3: Test Classification Endpoint
```bash
# Send test task through classification
curl -s -X POST http://100.87.214.70:20128/api/orchestrator/classify-task \
  -H "Content-Type: application/json" \
  -d '{
    "task_id": "AUTH-TEST-001",
    "description": "Process customer invoice and record payment",
    "venture": "FIN-001",
    "urgency": "high"
  }' | jq '.classification'

# Expected: Should see detailed classification with confidence > 0.8
# If: Still using fallback → restart may not have completed, wait 30s and retry
```

### Step 4: Verify Confidence Returned to Normal
```bash
# Check recent classification confidence levels
docker logs omniroute 2>&1 | grep "confidence" | tail -10

# Expected: Numbers > 0.8
# If: Still < 0.3 → fallback still in use, check step 3 results
```

---

## Recovery

### Step 1: Monitor Classification Quality
```bash
# Query classification logs from last hour
docker logs omniroute --since 1h 2>&1 | grep -i "classify" | wc -l

# Expected: Should see normal volume of classifications
# If: 0 → no classifications, check if tasks being submitted
```

### Step 2: Run Classification Accuracy Test
```bash
# Send 5 test classifications covering different domains
# Check confidence is > 0.75 for each

for venture in OPS-001 LT-005 FIN-037 CON-001 RE-001; do
  curl -s -X POST http://100.87.214.70:20128/api/orchestrator/classify-task \
    -H "Content-Type: application/json" \
    -d '{
      "task_id": "TEST-'$venture'",
      "description": "Sample task for '$venture'",
      "venture": "'$venture'",
      "urgency": "medium"
    }' | jq '.confidence'
done

# Expected: All > 0.75
```

### Step 3: Verify Agent Discovery Accuracy
```bash
# Since classification feeds discovery, verify agents being matched correctly
curl -s -X POST http://100.87.214.70:20128/api/orchestrator/find-best-agents \
  -H "Content-Type: application/json" \
  -d '{
    "task_id": "DISCOVERY-TEST",
    "description": "B2B sales outreach for medical facilities",
    "required_capabilities": ["CAP-001", "CAP-002"],
    "venture": "LT-005",
    "min_success_rate": 0.75
  }' | jq '.agents | length'

# Expected: Should return 3+ agents with high relevance
```

---

## Prevention

### 1. Set Up Key Rotation Alerts
```bash
# Add reminder to Bitwarden
# Mark API key with expiration date (typically 1 year from creation)
# Set calendar reminder for 30 days before expiration

# Alternatively: Use Bitwarden's "Expiration" field if available
```

### 2. Implement API Key Monitoring
```javascript
// In OmniRoute startup
async function validateApiKeys() {
  const apiKey = process.env.CLAUDE_API_KEY;
  if (!apiKey) {
    logger.error('CLAUDE_API_KEY not set');
    process.exit(1);
  }
  
  // Make test API call
  const response = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {'x-api-key': apiKey},
    body: JSON.stringify({
      model: 'claude-haiku-4.5-20251001',
      max_tokens: 10,
      messages: [{role: 'user', content: 'ok'}]
    })
  });
  
  if (response.status === 401) {
    logger.error('API key validation failed');
    process.exit(1);
  }
}

// Call on startup
validateApiKeys();
```

### 3. Track API Key Versions
```yaml
# api_key_registry.yaml
current_key:
  created_at: 2026-09-10
  expires_at: 2027-09-10
  status: 'active'
  last_tested: 2026-09-18T14:22:00Z
  
previous_keys:
  - created_at: 2026-06-01
    expires_at: 2027-06-01
    status: 'rotated'
    rotated_date: 2026-09-10
```

### 4. Add API Key Fallback
```javascript
// Support multiple API keys, use next one if current fails
const apiKeys = [
  process.env.CLAUDE_API_KEY_PRIMARY,
  process.env.CLAUDE_API_KEY_SECONDARY,
  process.env.CLAUDE_API_KEY_TERTIARY
];

async function classifyTask(task) {
  for (const key of apiKeys) {
    try {
      return await classify(task, key);
    } catch (e) {
      if (e.status === 401) continue;  // Try next key
      throw e;
    }
  }
  // All keys failed
  return fallbackClassification(task);
}
```

### 5. Test Auth During Deployment
```bash
# Add to CI/CD pipeline
# Before deploying OmniRoute update:
curl -X POST https://api.anthropic.com/v1/messages \
  -H "x-api-key: $CLAUDE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-haiku-4.5-20251001",
    "max_tokens": 50,
    "messages": [{"role": "user", "content": "test"}]
  }' || exit 1  # Fail deployment if auth fails
```

---

**Related Runbooks:**
- [[ORCHESTRATOR-TASK-STALLED]] (when tasks stall due to classification failure)
- [[NEO4J-DISCOVERY-BROKEN]] (when discovery fails due to bad classification)

**Owned By:** Security Team  
**Escalation:** If auth broken > 10 min, page security team lead
