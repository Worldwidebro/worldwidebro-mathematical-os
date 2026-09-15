# ✅ N8N Build Checklist — Week 1 Revenue Automation

**Target:** Live revenue automation across 6 Tier-0 ventures by Sep 19  
**Date:** 2026-09-15  
**Status:** Ready to build

---

## PRE-BUILD VERIFICATION

- [ ] Access n8n instance: http://100.87.214.70:5678
- [ ] Login credentials: Check Bitwarden "n8n — Company Brain"
- [ ] Google Maps Scraper running: `curl http://100.87.214.70:8080/api/jobs`
- [ ] Supabase accessible: `curl https://rhlkjelglvurowdalrgh.supabase.co/rest/v1/ventures`
- [ ] Neo4j accessible: `curl -u neo4j:changeme http://100.87.214.70:7474/`
- [ ] ClickUp API key ready (Bitwarden)
- [ ] SendGrid API key ready (Bitwarden)
- [ ] Twilio credentials ready for CALLCENTER (if available)

---

## STEP 1: Build Master Workflow (UI-Based)

### Timeline: 60 minutes
**Reference:** [[N8N-MASTER-WORKFLOW-SPEC|N8N-MASTER-WORKFLOW-SPEC.md]]

### In n8n Dashboard:

1. **Create New Workflow**
   - Click: `+ New` → `Workflow`
   - Name: `Revenue Master Orchestrator — Multi-Venture`
   - Click: `Create`

2. **Add Trigger Node**
   - Click: `+` (canvas)
   - Search: `Schedule`
   - Select: `Trigger → Schedule`
   - Config:
     - Trigger mode: `Daily`
     - Time: `6:00 AM`
     - Save

3. **Add Manual Webhook (for testing)**
   - Click: `+`
   - Search: `Webhook`
   - Select: `Webhook`
   - Config:
     - HTTP Method: `POST`
     - Generate webhook URL
     - Copy URL to Slack #revenue-automation
     - Save

4. **Add 13 Workflow Nodes**
   ```
   [Trigger] 
   ├─ [1] Supabase: Load Venture Config
   ├─ [2] HTTP: Call Google Maps Scraper
   ├─ [3] HTTP: Call Neo4j Score Leads
   ├─ [4] Code: Segment Leads (HOT/WARM/COLD)
   ├─ [5] Supabase: Insert Leads
   ├─ [6] If-Else: Has ClickUp?
   │  ├─ [7a] HTTP: Create ClickUp Tasks
   │  └─ [7b] Skip
   ├─ [8] If-Else: Has Email?
   │  ├─ [9a] SendGrid: Send Emails
   │  └─ [9b] Skip
   ├─ [10] If-Else: Has Twilio?
   │   ├─ [11a] Twilio: Queue Calls
   │   └─ [11b] Skip
   ├─ [12] Neo4j: Log Event
   └─ [13] Slack: Send Notification
   ```

### Node Setup (Detailed)

**[1] Supabase: Load Venture Config**
- Add node: `Supabase`
- Select operation: `Query rows`
- Table: `ventures`
- Filter: `id` = `{{ $env.VENTURE_ID }}` (or use input param)
- Result: Store venture config

**[2] HTTP: Google Maps Scraper**
- Add node: `HTTP Request`
- Method: `POST`
- URL: `http://100.87.214.70:8080/api/jobs`
- Body (JSON):
  ```json
  {
    "query": "{{ $node.Supabase.json.lead_target }}",
    "location": "{{ $node.Supabase.json.location }}",
    "results_limit": 100
  }
  ```
- Response: Save job ID for polling

**[3] HTTP: Poll Google Maps Results**
- Add node: `HTTP Request`
- Method: `GET`
- URL: `http://100.87.214.70:8080/api/jobs/{{ $node["HTTP Request"].json.job_id }}`
- Wait (polling): Retry every 10s for up to 30 min
- Response: Extract leads array

**[4] HTTP: Neo4j Score Leads**
- Add node: `HTTP Request`
- Method: `POST`
- URL: `http://100.87.214.70:7474/db/neo4j/tx/commit`
- Auth: Basic (neo4j / changeme)
- Body (Cypher):
  ```cypher
  WITH {{$node["HTTP Request 2"].json.leads}} as leads
  UNWIND leads as lead
  WITH lead,
    (toFloat(lead.rating) * 0.4) + 
    (toFloat(lead.reviewCount) * 0.3) * 0.01 + 
    1 as score
  WHERE score > {{ $node.Supabase.json.min_rating }}
  RETURN lead, score
  ORDER BY score DESC
  ```
- Response: Scored leads

**[5] Code: Segment Leads**
- Add node: `Code`
- Language: `JavaScript`
- Code:
  ```javascript
  const leads = $node['HTTP Request 3'].json.leads;
  
  const hot = leads.filter(l => l.score > 85);
  const warm = leads.filter(l => l.score > 75 && l.score <= 85);
  const cold = leads.filter(l => l.score >= 60 && l.score <= 75);
  
  return {
    hot,
    warm,
    cold,
    total: leads.length
  };
  ```

**[6] Supabase: Insert Leads**
- Add node: `Supabase`
- Operation: `Insert rows`
- Table: `leads`
- Data (from leads array):
  ```json
  {
    "venture_id": "{{ $node.Supabase.json.id }}",
    "name": "{{ item.name }}",
    "phone": "{{ item.phone }}",
    "email": "{{ item.email }}",
    "website": "{{ item.website }}",
    "rating": "{{ item.rating }}",
    "review_count": "{{ item.reviewCount }}",
    "address": "{{ item.address }}",
    "score": "{{ item.score }}",
    "status": "new",
    "created_at": "now()"
  }
  ```

**[7] If-Else: Has ClickUp?**
- Add node: `If`
- Condition: `{{ $node.Supabase.json.has_clickup }} == true`
- True path: Go to [7a] Create ClickUp Tasks
- False path: Skip to [8]

**[7a] HTTP: Create ClickUp Tasks**
- Add node: `HTTP Request`
- Method: `POST`
- URL: `https://api.clickup.com/api/v2/list/{{ $env.CLICKUP_LIST_ID }}/task`
- Auth: Bearer token (from Bitwarden)
- Body (create HOT task):
  ```json
  {
    "name": "🔥 CALL {{ $node["Code"].json.hot.length }} prospects (score > 85)",
    "description": "Lead list:\n{{ $node["Code"].json.hot.map(l => l.name + ' - ' + l.phone).join('\n') }}",
    "assignee": "{{ $node.Supabase.json.sales_lead_id }}",
    "priority": 1,
    "due_date": "{{ $now + 7*24*60*60*1000 }}"
  }
  ```
- Repeat for WARM and COLD segments

**[8] If-Else: Has Email?**
- Add node: `If`
- Condition: `{{ $node.Supabase.json.has_email }} == true`
- True path: Go to [9a] Send Emails
- False path: Skip to [10]

**[9a] SendGrid: Send Email Campaign**
- Add node: `HTTP Request`
- Method: `POST`
- URL: `https://api.sendgrid.com/v3/mail/send`
- Auth: Bearer token (from Bitwarden)
- Body (personalized for each lead):
  ```json
  {
    "personalizations": [
      {
        "to": [{"email": "{{ item.email }}"}],
        "dynamic_template_data": {
          "firstName": "{{ item.name.split(' ')[0] }}",
          "company": "{{ item.name }}",
          "website": "{{ item.website }}"
        }
      }
    ],
    "from": {"email": "outreach@company.com"},
    "template_id": "{{ $node.Supabase.json.email_template }}"
  }
  ```
- Loop: Once per WARM lead (max 50)

**[10] If-Else: Has Twilio?**
- Add node: `If`
- Condition: `{{ $node.Supabase.json.has_twilio }} == true`
- True path: Go to [11a] Queue Calls
- False path: Skip to [12]

**[11a] Twilio: Queue Call Campaign**
- Add node: `HTTP Request`
- Method: `POST`
- URL: `https://api.twilio.com/2010-04-01/Accounts/{{ $env.TWILIO_ACCOUNT_SID }}/Calls`
- Auth: Basic (Account SID + Auth Token)
- Body:
  ```json
  {
    "From": "+1{{ $env.TWILIO_FROM_NUMBER }}",
    "To": "{{ item.phone }}",
    "Url": "https://{{ $env.TWILIO_APP_SID }}/call?prospect={{ item.id }}&script={{ $node.Supabase.json.call_script }}"
  }
  ```
- Loop: Once per HOT lead (max 20)

**[12] Neo4j: Log Execution Event**
- Add node: `HTTP Request`
- Method: `POST`
- URL: `http://100.87.214.70:7474/db/neo4j/tx/commit`
- Body (Cypher):
  ```cypher
  CREATE (e:Event {
    type: "lead_generation_run",
    venture_id: "{{ $node.Supabase.json.id }}",
    leads_generated: {{ $node["HTTP Request 2"].json.leads.length }},
    leads_scored: {{ $node["HTTP Request 3"].json.leads.length }},
    emails_sent: {{ $node["SendGrid"].json.personalizations.length || 0 }},
    calls_queued: {{ $node["Twilio"].json.calls.length || 0 }},
    timestamp: timestamp()
  })
  RETURN e
  ```

**[13] Slack: Send Notification**
- Add node: `Slack`
- Send to: `#revenue-automation`
- Message:
  ```
  🚀 **Revenue Run: {{ $node.Supabase.json.id }}**
  
  📊 **Results:**
  • Leads generated: {{ $node["Code"].json.total }}
  • Leads scored: {{ $node["HTTP Request 3"].json.leads.length }}
  • HOT (>85): {{ $node["Code"].json.hot.length }}
  • WARM (75-85): {{ $node["Code"].json.warm.length }}
  • Emails sent: {{ $node["SendGrid"].json.personalizations.length || 0 }}
  • Calls queued: {{ $node["Twilio"].json.calls.length || 0 }}
  
  💰 **Est. Revenue:** ${{ $node["Code"].json.total * $node.Supabase.json.avg_deal_size }}
  
  ✅ Status: Complete
  ```

---

## STEP 2: Test with LT-005 (Manual)

**Timeline: 15 minutes**

### Dry Run (No email/calls)

1. **Update LT-005 venture config** (Supabase):
   ```sql
   UPDATE ventures SET 
     has_email = false,
     has_twilio = false,
     has_clickup = true,
     workflow_enabled = true
   WHERE id = 'LT-005';
   ```

2. **Execute workflow in n8n**:
   - Click: `Test workflow`
   - Input: `{ venture_id: "LT-005" }`
   - Monitor execution

3. **Expected output**:
   ```json
   {
     "venture_id": "LT-005",
     "leads_generated": 47,
     "leads_scored": 38,
     "hot": 8,
     "warm": 15,
     "cold": 15,
     "emails_sent": 0,
     "calls_queued": 0,
     "clickup_tasks": 3,
     "status": "success"
   }
   ```

4. **Verify in databases**:
   ```bash
   # Check Supabase
   curl -X GET "https://rhlkjelglvurowdalrgh.supabase.co/rest/v1/leads?venture_id=eq.LT-005" \
     -H "Authorization: Bearer $SUPABASE_KEY" | jq '.[] | .name, .score' | head -20
   
   # Check ClickUp (should have 3 new tasks)
   # Login to ClickUp > LT-005 workspace > Check lists
   
   # Check Neo4j
   curl -u neo4j:changeme http://100.87.214.70:7474/ \
     -d 'MATCH (e:Event {venture_id: "LT-005"}) RETURN e ORDER BY e.timestamp DESC LIMIT 1'
   ```

### Live Run (With email/calls)

1. **Enable email & Twilio** (update Supabase):
   ```sql
   UPDATE ventures SET 
     has_email = true,
     has_twilio = false,  -- Leave false until we test
     workflow_enabled = true
   WHERE id = 'LT-005';
   ```

2. **Execute workflow again**:
   - Input: `{ venture_id: "LT-005" }`
   - Monitor: Should send 30 emails to WARM leads
   - Check: SendGrid dashboard for delivery status

3. **Verify email deliverability**:
   ```bash
   # Check SendGrid activity
   curl -X GET "https://api.sendgrid.com/v3/mail/stats" \
     -H "Authorization: Bearer $SENDGRID_API_KEY" | jq '.stats[-1]'
   ```

---

## STEP 3: Deploy to 6 Ventures (Sep 16)

### Venture Configuration (All ready)

| Venture | Lead Target | Has Email | Has ClickUp | Has Twilio | Email Template |
|---------|-------------|-----------|-------------|-----------|-----------------|
| **OPS-001** | staffing agencies, recruitment | true | true | false | ops001-cold-call |
| **LT-005** | medical facilities | true | true | false | lt005-medical |
| **CALLCENTER** | call center operators | false | true | true | — |
| **CON-001** | construction companies | true | true | false | con001-bid |
| **RE-001** | real estate brokers | true | true | false | re001-partnership |
| **LT-011** | dispatch software prospects | false | false | false | — |

### Batch Execution (One workflow, multi-venture)

1. **Update workflow trigger**:
   - Change from single venture to batch mode
   - Loop over: `{{ $env.VENTURE_LIST }}`
   - Set env var: `VENTURE_LIST=["OPS-001", "LT-005", "CALLCENTER", "CON-001", "RE-001", "LT-011"]`

2. **Schedule daily**:
   - Workflow → Settings
   - Trigger: `Schedule`
   - Time: `6:00 AM daily`
   - Click: `Activate`

3. **Monitor daily**:
   - Slack: #revenue-automation gets daily summary
   - Supabase: Dashboard shows daily leads
   - Neo4j: Query execution history

---

## STEP 4: Add to Production (Sep 17-18)

- [ ] Load test (all 6 ventures simultaneously)
- [ ] Error handling verified (rate limits, missing creds)
- [ ] Slack alerts for failures
- [ ] Rollback plan documented (disable via workflow toggle)
- [ ] Revenue tracking in Supabase verified

---

## TROUBLESHOOTING

### Workflow Fails on Google Maps
```
Error: "429 Too Many Requests"
→ Add retry logic with exponential backoff
→ Change schedule: Run one venture per hour instead of all at once
```

### Email Not Sending
```
Error: "SendGrid authentication failed"
→ Verify API key in Bitwarden
→ Check SendGrid sender verification (admin@company.com whitelisted?)
→ Test with single email first
```

### ClickUp Tasks Not Created
```
Error: "ClickUp list not found"
→ Verify CLICKUP_LIST_ID matches actual LT-005 list
→ Check ClickUp API key has workspace access
→ Create list manually if missing
```

### Neo4j Connection Fails
```
Error: "Connection refused"
→ Verify Mac Studio is running: docker --context macstudio ps
→ Check firewall: curl http://100.87.214.70:7687
→ Restart Neo4j: docker --context macstudio restart neo4j
```

---

## SUCCESS METRICS (Week 1)

| Metric | Target | Actual |
|--------|--------|--------|
| Workflow runs | 6 ventures × 7 days = 42 | — |
| Leads generated | 50-100 per venture | — |
| Email deliverability | > 95% | — |
| ClickUp tasks created | 3 per venture × 6 = 18 | — |
| Revenue generated | $7.5K–$20K | — |
| Uptime | 99%+ | — |

---

## NEXT STEPS (After Build)

1. ✅ Build workflow (Step 1-2)
2. 🔄 Test with LT-005 (Step 2)
3. 🚀 Deploy to 6 ventures (Step 3)
4. 📊 Monitor + optimize (Step 4)
5. 💰 Scale to full portfolio (Oct 1+)

---

**You have everything. Build it.**
