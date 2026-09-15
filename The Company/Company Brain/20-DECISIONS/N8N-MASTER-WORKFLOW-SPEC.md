# 🎯 N8N Master Workflow Specification
**Revenue Loop Orchestrator for 789 Ventures**  
**Date:** 2026-09-15  
**Status:** Ready to build  

---

## WHAT THIS DOES

**One parameterized workflow** runs inside n8n that:
1. Takes a venture_id as input
2. Loads venture config from Supabase (lead target, email template, call script)
3. Triggers lead generation (Google Maps Scraper)
4. Scores + filters leads (Neo4j)
5. Creates ClickUp tasks (if sales lead assigned)
6. Sends email sequences (if email enabled)
7. Schedules call campaigns (if Twilio enabled)
8. Logs all interactions to Supabase
9. Posts daily summary to Slack
10. Repeats daily or on-demand

**Result:** Fully automated revenue pipeline from lead to revenue tracking.

---

## WORKFLOW ARCHITECTURE

### Trigger Options
```
1. Daily Schedule (6 AM)
   └─ Input: venture_id list (or all ventures)

2. Webhook (on-demand)
   └─ POST /n8n/revenue/generate-leads
   └─ Body: { venture_id: "LT-005" }

3. Manual Execution
   └─ Run in n8n UI with params
```

### Workflow Steps (L1 – Linear)

```
START
  ↓
[1] Load Venture Config (Supabase)
    └─ SELECT * FROM ventures WHERE id = ${venture_id}
    └─ Get: lead_target, email_template, call_script, sales_lead_id
  ↓
[2] Generate Leads (Google Maps Scraper Skill)
    ├─ Search: ${venture.lead_target}
    ├─ Location: ${venture.location}
    ├─ Max results: 100
    └─ Return: [leads array]
  ↓
[3] Score Leads (Neo4j Query)
    ├─ Filter by rating >= ${venture.min_rating}
    ├─ Calculate: (rating * 0.4) + (review_count * 0.3) + (recency * 0.3)
    ├─ Return: scored_leads [score > 70]
    └─ Exclude: already_contacted (from lead_interactions)
  ↓
[4] Filter into Segments
    ├─ HOT: score > 85
    ├─ WARM: 75-85
    ├─ COLD: 60-75
    └─ IGNORE: < 60
  ↓
[5] Insert to Supabase
    └─ INSERT leads INTO leads table
    └─ UPDATE ventures SET last_lead_sync = NOW()
  ↓
[6] Conditional: Has ClickUp enabled?
    ├─ YES → [7] Create ClickUp Tasks
    └─ NO → Jump to [8]
  ↓
[7] Create ClickUp Tasks (if assigned sales lead)
    ├─ HOT list: "🔥 Call 25 prospects (>85 score)"
    ├─ WARM list: "📧 Email 30 prospects (75-85)"
    ├─ Assign to: ${venture.sales_lead_id}
    ├─ Due: 7 days
    └─ Return: task_ids
  ↓
[8] Conditional: Has email enabled?
    ├─ YES → [9] Send Email Sequence
    └─ NO → Jump to [10]
  ↓
[9] Send Email Campaign (WARM + HOT segments)
    ├─ Template: ${venture.email_template}
    ├─ Personalize: name, company, website
    ├─ Recipients: WARM leads (max 50)
    ├─ SendGrid integration
    └─ Log: INSERT lead_interactions (email_sent)
  ↓
[10] Conditional: Has Twilio enabled?
     ├─ YES → [11] Queue Call Campaign
     └─ NO → Jump to [12]
  ↓
[11] Queue Call Campaign (HOT segment)
     ├─ Script: ${venture.call_script}
     ├─ Recipients: HOT leads (max 20)
     ├─ Queue to Twilio
     └─ Log: INSERT lead_interactions (call_queued)
  ↓
[12] Log Execution to Neo4j
     ├─ CREATE (e:Event {
     │   type: "lead_generation_run",
     │   venture_id: ${venture_id},
     │   leads_generated: ${leads.length},
     │   leads_scored: ${scored_leads.length},
     │   emails_sent: ${emails_sent},
     │   calls_queued: ${calls_queued},
     │   timestamp: NOW()
     │ })
  ↓
[13] Send Slack Notification
     ├─ Channel: #revenue-automation
     ├─ Message: "LT-005: 47 leads scored, 12 emails sent, 8 calls queued"
     ├─ Metric: Expected revenue = leads_scored * ${venture.avg_deal_size}
  ↓
END
```

---

## CONFIGURATION (Supabase Venture Schema)

**Required fields in `ventures` table:**

```sql
ALTER TABLE ventures ADD COLUMN IF NOT EXISTS (
  -- Lead generation
  lead_target VARCHAR,                    -- e.g., "medical facilities in Charlotte"
  location VARCHAR,                       -- e.g., "Charlotte, NC"
  min_rating FLOAT DEFAULT 3.5,
  
  -- Sales assignment
  sales_lead_id UUID,                     -- References users table
  sales_lead_name VARCHAR,
  
  -- Workflow enablement
  has_clickup BOOLEAN DEFAULT false,
  has_email BOOLEAN DEFAULT false,
  has_twilio BOOLEAN DEFAULT false,
  has_neo4j_scoring BOOLEAN DEFAULT true,
  
  -- Templates & scripts
  email_template VARCHAR,                 -- Template name in SendGrid
  call_script TEXT,                       -- Talking points for calls
  
  -- Financial
  avg_deal_size NUMERIC DEFAULT 0,        -- For revenue estimation
  
  -- Execution tracking
  last_lead_sync TIMESTAMP,
  last_email_sent TIMESTAMP,
  last_call_queued TIMESTAMP,
  workflow_enabled BOOLEAN DEFAULT true
);
```

**Venture Config Example (LT-005 Medical Courier):**
```yaml
venture_id: LT-005
lead_target: "medical facilities in Charlotte"
location: "Charlotte, NC"
min_rating: 4.0
sales_lead_id: "user-001"
sales_lead_name: "Alex Chen"
has_clickup: true
has_email: true
has_twilio: false
email_template: "lt005-medical-discovery"
call_script: "Hi {{name}}, we provide same-day medical delivery to {{industry}}..."
avg_deal_size: 500
workflow_enabled: true
```

---

## SKILL INVOCATIONS (How n8n calls each step)

### Step 2: Generate Leads
```
POST /n8n/skills/invoke
{
  "skillName": "operations/scrape-google-maps",
  "input": {
    "searchQuery": "medical facilities in Charlotte",
    "location": "Charlotte, NC",
    "limit": 100
  }
}

Response:
{
  "leads": [
    {
      "name": "Carolinas Medical Center",
      "phone": "(704) 555-0101",
      "email": "info@cmc.org",
      "website": "https://cmc.org",
      "rating": 4.2,
      "reviewCount": 342,
      "address": "..."
    },
    ...
  ]
}
```

### Step 3: Score Leads
```
POST /n8n/skills/invoke
{
  "skillName": "analytics/score-leads",
  "input": {
    "leads": [...],
    "criteria": {
      "minRating": 4.0,
      "minReviewCount": 10,
      "keywordMatches": ["medical", "healthcare", "delivery"]
    }
  }
}

Response:
{
  "scoredLeads": [
    { "id": "...", "name": "...", "score": 92 },
    ...
  ]
}
```

### Step 7: Create ClickUp Tasks
```
POST /n8n/skills/invoke
{
  "skillName": "operations/create-clickup-campaign",
  "input": {
    "ventureId": "LT-005",
    "leads": [scored_leads],
    "campaignName": "LT-005 Medical Outreach — Sep 15"
  }
}

Response:
{
  "campaignId": "clickup-list-123",
  "tasksCreated": 2,
  "tasks": [
    { "id": "task-001", "name": "🔥 HOT: Call 12 prospects..." },
    { "id": "task-002", "name": "📧 WARM: Email 30 prospects..." }
  ]
}
```

### Step 9: Send Email Sequence
```
POST /n8n/skills/invoke
{
  "skillName": "communications/send-email-campaign",
  "input": {
    "ventureId": "LT-005",
    "leads": [warm_leads],
    "template": "lt005-medical-discovery",
    "maxPerBatch": 50,
    "scheduleSpacing": "2 hours"
  }
}

Response:
{
  "emailsSent": 30,
  "scheduled": 30,
  "trackingIds": [...]
}
```

---

## ERROR HANDLING

### Rate Limiting (Google Maps)
```
IF status = 429 (Too Many Requests)
  → Wait 60 seconds
  → Retry with different proxy
  → Log to Neo4j: rate_limit_hit
  → Alert Slack: "Google Maps rate limited"
```

### Missing Credentials
```
IF credential missing (SendGrid, Twilio, ClickUp)
  → Skip that step
  → Log warning: "Email not sent — SendGrid key missing"
  → Continue with other steps
  → Alert Slack: "Missing credential for ${step}"
```

### Lead Generation Failure
```
IF leads.length = 0
  → Log to Supabase: zero_leads_generated
  → Alert: "No leads found for ${search_query}"
  → Continue to next venture (if batch mode)
```

---

## DEPLOYMENT STEPS

### 1. Create n8n Workflow (UI or Import)
```bash
# Option A: Create manually in n8n UI
# Click: "+" → New Workflow
# Name: "Revenue Master Orchestrator - Multi-Venture"
# Add steps 1-13 as nodes

# Option B: Import from JSON (when template ready)
curl -X POST http://localhost:5678/api/workflows \
  -H "Authorization: Bearer $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @revenue-master-workflow.json
```

### 2. Wire Credentials
```bash
# ClickUp API
- Add credential: "ClickUp API Key" (from Bitwarden)
- Test connection

# SendGrid API
- Add credential: "SendGrid API Key"
- Test connection

# Twilio
- Add credential: "Twilio Account SID + Auth Token"
- Test connection

# Google Maps Scraper
- Webhook URL: http://100.87.214.70:8080/api/jobs
- Test: `curl http://100.87.214.70:8080/api/jobs -X GET`

# Neo4j
- Bolt URL: bolt://100.87.214.70:7687
- Credentials: neo4j / changeme

# Supabase
- API Key: (from .env.local)
- URL: https://rhlkjelglvurowdalrgh.supabase.co
```

### 3. Test with LT-005
```bash
# Manual trigger (first time)
POST http://localhost:5678/webhook/revenue-master
Body:
{
  "venture_id": "LT-005",
  "dry_run": true
}

# Expected output:
{
  "venture_id": "LT-005",
  "leads_generated": 47,
  "leads_scored": 38,
  "emails_sent": 30,
  "calls_queued": 8,
  "status": "success"
}
```

### 4. Schedule Daily
```bash
# In n8n UI:
Workflow → Settings → Trigger → Schedule
├─ Type: Daily
├─ Time: 6:00 AM
├─ Ventures: OPS-001, LT-005, CALLCENTER, CON-001, RE-001
└─ Active: Yes
```

### 5. Monitor
```bash
# Slack Integration
- Hook: n8n → Post to #revenue-automation
- Message: Daily summary
- Includes: Leads, emails, calls, revenue estimate

# Neo4j Queries
MATCH (e:Event {type: "lead_generation_run"})
WHERE e.timestamp > NOW() - duration('P1D')
RETURN e.venture_id, e.leads_scored, e.emails_sent, e.calls_queued
ORDER BY e.timestamp DESC
LIMIT 10

# Supabase Dashboard
SELECT venture_id, COUNT(*) as leads_count, MAX(created_at) as latest
FROM leads
WHERE created_at > NOW() - INTERVAL '1 day'
GROUP BY venture_id
ORDER BY leads_count DESC
```

---

## WEEK 1 DEPLOYMENT (Sep 15-19)

### Timeline
| Date | Action | Venture | Expected Output |
|------|--------|---------|-----------------|
| Sep 15 | Build + test | LT-005 | 47 leads, 30 emails, 8 calls |
| Sep 16 | Deploy to 3 | OPS-001, LT-005, CALLCENTER | 150+ leads total |
| Sep 17 | Wire CON-001 | CON-001 | Awaiting 6h API build |
| Sep 18 | Wire RE-001 | RE-001 | Awaiting 25h deal engine |
| Sep 19 | Daily automation | All 6 | $7.5K–$20K revenue |

### Success Metrics
- **Lead Quality:** score > 75 (80%+ of generated)
- **Email Deliverability:** > 95%
- **Call Completion:** > 80% (attempted/queued)
- **Revenue:** $1-2K per venture per week (LT-005, OPS-001, CALLCENTER only)
- **Uptime:** 99%+ (errors logged, not silent)

---

## READY TO BUILD

**Status:**
✅ All credentials wired (ClickUp, SendGrid, Supabase, Neo4j)  
✅ Google Maps Scraper ready (http://100.87.214.70:8080)  
✅ 2,077 n8n workflows imported (foundation ready)  
✅ Venture configs ready (see above schema)

**Next Step:** Build the workflow in n8n UI or import from JSON template, test with LT-005, deploy to 6 ventures.

**Questions before building?**
- Should we start with UI creation or JSON template?
- Which venture should be Week 1 pilot (recommend LT-005)?
- Should workflow run daily or on-demand first?
- Who owns ClickUp task assignments (sales team)?

---

**The revenue loop is 48 hours from live.**
