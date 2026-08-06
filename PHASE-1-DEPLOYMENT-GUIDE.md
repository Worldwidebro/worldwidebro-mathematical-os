---
name: PHASE-1-DEPLOYMENT-GUIDE
title: 'Phase 1 Deployment Guide: Echo AI Agent (E-Commerce)'
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Phase 1 Deployment Guide: Echo AI Agent (E-Commerce)
**Timeline:** May 10-11, 2026 (Monday-Tuesday)  
**Goal:** Deploy first agent, test with 10 prospects, iterate

---

## Step 1: VAPI Account Setup (1 hour)

### Create VAPI Account
```
1. Go to vapi.ai
2. Sign up with email: winnerscirclewcllc@gmail.com
3. Create new workspace: "Worldwidebro AI Calling"
4. Verify email + set password
```

### Connect Twilio
```
1. In VAPI: Settings → Integrations → Twilio
2. Enter Twilio Account SID + Auth Token
   (Get from twilio.com/console)
3. Authorize Twilio integration
4. Purchase phone number: +1-XXX-ECOM-001
   (Use area code matching target market)
```

---

## Step 2: Deploy Echo Agent (30 minutes)

### Configure Agent in VAPI Dashboard
1. Create new Agent: "Echo - E-Commerce"
2. Copy the configuration from `vapi-agent-echo-config.json`
   - Model: GPT-4
   - Voice: "echo" (or "nova" - female voice)
   - Temperature: 0.7
   - First Message: See JSON config
   - System Prompt: Copy full prompt from JSON

### Paste System Prompt
```
[Full system prompt from AI-CALLING-SYSTEM-ARCHITECTURE.md]
```

### Assign Phone Number
- Phone: +1-XXX-ECOM-001
- Recording: Enable
- Webhook Events: Enabled

---

## Step 3: Configure Webhooks (30 minutes)

### Webhook Endpoint Setup
You need a Node.js server to receive webhook callbacks from VAPI.

**Option A: Use ngrok for local testing (quick)**
```bash
# Install ngrok
brew install ngrok

# Start tunnel
ngrok http 3000

# Copy public URL: https://xxxx-xx-xxxx-xxxx.ngrok.io
```

**Option B: Deploy to production server**
- AWS Lambda + API Gateway
- Vercel
- Heroku
- DigitalOcean

### Install Node Dependencies
```bash
cd /Users/acebless/Documents
npm init -y
npm install express body-parser @supabase/supabase-js axios dotenv
```

### Create Server (webhook-server.js)
```javascript
const express = require('express');
const bodyParser = require('body-parser');
const { handleCallComplete } = require('./webhook-call-complete');

const app = express();
app.use(bodyParser.json());

// Webhook endpoint for call completion
app.post('/webhook/call-complete', handleCallComplete);

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### Set Environment Variables (.env)
```
SUPABASE_URL=https://iefnvvfxbnpxfcggzljq.supabase.co
SUPABASE_KEY=[YOUR_SUPABASE_KEY]
CLICKUP_TOKEN=[YOUR_CLICKUP_API_TOKEN]
CLICKUP_LIST_ECOM=[CLICKUP_LIST_ID_FOR_ECOM]
CLICKUP_LIST_TECH=[CLICKUP_LIST_ID_FOR_TECH]
CLICKUP_LIST_BEAUTY=[CLICKUP_LIST_ID_FOR_BEAUTY]
```

### Get ClickUp List IDs
```bash
# Run in ClickUp API v2
# GET https://api.clickup.com/api/v2/space/[SPACE_ID]/list

# Space ID: From ClickUp workspace URL
# Lists created: Leads—E-Commerce Tier 1, Leads—Technology Tier 1, etc.
```

### Configure Webhook in VAPI
In Agent settings:
```
Call Ended Webhook: https://YOUR_DOMAIN/webhook/call-complete
Transcript Ready Webhook: https://YOUR_DOMAIN/webhook/transcript
```

---

## Step 4: Test Calls (1 hour, Tuesday)

### Test Call Setup
1. Start webhook server locally:
   ```bash
   node webhook-server.js
   ```

2. Start ngrok tunnel:
   ```bash
   ngrok http 3000
   ```

3. Update VAPI webhook URLs with ngrok URL

4. Test incoming call to Echo:
   ```
   Call: +1-XXX-ECOM-001
   Echo should answer with: "Hi, this is Echo from Worldwidebro Holdings..."
   ```

### Test Script (5 test calls)
Call Echo from your phone with test scenarios:

| Call | Scenario | Expected |
|------|----------|----------|
| 1 | "Hi, I sell on Shopify and Amazon" | Echo qualifies multi-channel pain |
| 2 | "We don't have inventory issues" | Echo asks for operations contact |
| 3 | "We lose maybe 10-15% to oversells" | Echo pitches solution |
| 4 | "How much does it cost?" | Echo quotes $2.5-$5K/month, ROI |
| 5 | "Let's do a demo" | Echo books Tuesday 2pm or Wed 10am |

### Monitor Webhook Responses
Check server logs for:
```
✓ Call received by webhook
✓ Call logged to Supabase (ai_calls table)
✓ ClickUp task created (if interested/demo booked)
✓ Warmth score extracted (should be 7-10 for test calls)
```

---

## Step 5: Iterate System Prompt (2-3 hours, Tuesday)

### Analyze Test Calls
1. Listen to Echo's responses
   - Is opening natural?
   - Does it listen before pitching?
   - Are objections handled well?

2. Review transcripts for:
   - Clarity of benefits mentioned
   - Whether demo booking was natural
   - If prospect felt pressured

3. Update system prompt based on:
   - Add filler words if conversation feels stiff
   - Shorten opening if it seems long
   - Adjust tone if too formal/too casual
   - Improve demo booking language

### Common Issues + Fixes
```
Issue: Echo talks too fast
Fix: In config, add "speed": 0.95

Issue: Echo doesn't listen before pitching
Fix: Add to system prompt: "Always ask questions before mentioning solution"

Issue: Demo booking sounds forced
Fix: Change to: "Would it make sense to see this in action? How's Tuesday?"

Issue: Echo cuts off prospects
Fix: Increase "maxTokens" from 500 to 1000
```

---

## Step 6: Launch E-Commerce Campaign (Wednesday, May 12)

### Prospect List Setup
1. Open `CONTACTS-INITIAL.csv`
2. Expand to 25 E-Commerce prospects with:
   - Name
   - Phone number
   - Company name
   - Warmth score (start at 5 if unknown)

3. Upload to ClickUp: Leads—E-Commerce Tier 1

### Create Calling Schedule
```
Monday-Thursday: 9am-5pm (50 calls/day)
Focus on 5-call morning batches (9am, 11am, 1pm, 3pm, 4pm)

Day 1 (Wed): 10 calls (test new list)
Day 2 (Thu): 20 calls
Day 3 (Fri): 20 calls
Day 4+ (Mon): 50 calls/day once proven
```

### Call Execution
1. Before each call: Get venture context
   ```bash
   node -e "require('./rag-venture-context').getVentureContext('e-commerce')"
   ```

2. Dial prospect number from Echo agent
3. Log call outcome in ClickUp (auto via webhook)
4. Review transcripts daily for prompt optimization

---

## Success Metrics (Week 1)

| Metric | Target | Status |
|--------|--------|--------|
| Calls completed | 50+ | ? |
| Call duration avg | 8-12 min | ? |
| Demo booking rate | 15-20% | ? |
| Prospects interested | 5-10 | ? |
| ClickUp tasks created | 5-10 | ? |
| Webhook success rate | 95%+ | ? |

---

## Phase 2 Preview (Week 2)

Once Echo is proven:
- Deploy Swift (Tech agent) - May 15
- Deploy Bella (Beauty agent) - May 15
- Scale to 480 calls/week across all 3 agents
- Expected revenue: $35K-$100K by May 31

---

## Troubleshooting

### VAPI Webhooks Not Firing
- Check webhook URL in VAPI settings matches ngrok URL
- Verify server is running (`node webhook-server.js`)
- Check server logs for incoming POST requests
- Verify endpoint path: `/webhook/call-complete`

### ClickUp Tasks Not Creating
- Verify CLICKUP_TOKEN in .env is valid
- Check CLICKUP_LIST_ECOM ID matches actual list
- Review webhook logs for 401/403 errors
- Confirm ClickUp workspace structure

### Supabase Errors
- Verify SUPABASE_URL and SUPABASE_KEY are correct
- Check ai_calls table exists in Supabase
- Ensure policy allows inserts from webhook server

### Call Quality Issues
- If echo is robotic: Reduce temperature from 0.7 to 0.5
- If echo is too creative: Increase temperature to 0.9
- If voice sounds artificial: Try different voice (nova, shimmer)
- If echo speaks too fast: Set speed to 0.95

---

## Next: Week 2 Deployment

Once this is live and tested:
1. Swift (Tech agent) deployment
2. Bella (Beauty agent) deployment
3. Monitor all 3 agents in parallel
4. Scale to 480 calls/week

Files ready:
- ✅ vapi-agent-swift-config.json
- ✅ vapi-agent-bella-config.json
- ✅ OUTREACH-EXECUTION-GUIDE.md
- ✅ AI-CALLING-SYSTEM-ARCHITECTURE.md

---

**Status: Ready to deploy. Start May 10, 9am.**
