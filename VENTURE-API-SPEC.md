# Growth OS Venture API Specification

**Status:** Ready to wire on n8n  
**Base URL:** `http://n8n.internal:5678/webhook/venture-campaign` (Tailscale: `100.87.214.70:5678`)  
**Auth:** Venture ID in payload (MVP: no secret required)

---

## Endpoint: Trigger Campaign

**POST** `/webhook/venture-campaign`

### Request
```json
{
  "venture_id": "CON-001",
  "campaign_type": "lead_gen",
  "target_audience": "electrical_contractors_nc",
  "budget_usd": 5000,
  "duration_days": 30,
  "objectives": ["leads", "brand_awareness"],
  "custom_notes": "Focus on Charlotte metro area"
}
```

### Response (Success)
```json
{
  "status": "success",
  "campaign_id": "camp_abc123xyz",
  "venture_id": "CON-001",
  "agents_assigned": 47,
  "workflows_triggered": 8,
  "estimated_lead_volume": 120,
  "created_at": "2026-07-22T14:30:00Z",
  "dashboard_url": "http://localhost:3000/marketing?campaign=camp_abc123xyz"
}
```

### Response (Error)
```json
{
  "status": "error",
  "code": "INVALID_VENTURE_ID",
  "message": "Venture CON-001 not found in registry"
}
```

---

## cURL Example

```bash
curl -X POST http://100.87.214.70:5678/webhook/venture-campaign \
  -H "Content-Type: application/json" \
  -d '{
    "venture_id": "CON-001",
    "campaign_type": "lead_gen",
    "target_audience": "electrical_contractors_nc",
    "budget_usd": 5000,
    "duration_days": 30,
    "objectives": ["leads", "brand_awareness"]
  }'
```

---

## Supabase Schema

```sql
CREATE TABLE campaigns (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  venture_id TEXT NOT NULL,
  campaign_type TEXT,
  target_audience TEXT,
  budget_usd DECIMAL(10,2),
  duration_days INT,
  status TEXT DEFAULT 'active',
  agents_assigned INT,
  workflows_triggered INT,
  estimated_leads INT,
  actual_leads INT DEFAULT 0,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

ALTER TABLE campaigns ADD CONSTRAINT fk_venture 
  FOREIGN KEY (venture_id) REFERENCES ventures(id);
```

---

## n8n Workflow Logic

**Trigger:** Webhook POST  
**Steps:**
1. Parse & validate `venture_id` against Supabase `ventures` table
2. Fetch venture profile (sector, location, cap table)
3. Dispatch to agents:
   - Intelligence: market research
   - Brand: positioning
   - Creative: ad creative generation
   - Content: landing page + copy
   - Distribution: media buying
   - Paid: Google Ads, Meta setup
   - Organic: SEO, content calendar
   - Lifecycle: email nurture
4. Create campaign record in Supabase
5. Return `campaign_id`, `status`, agent count

---

## MVP Scope (This Session)

- ✅ n8n webhook listens for POST
- ✅ Validate venture_id
- ✅ Create campaign row in Supabase
- ✅ Return campaign_id + metadata
- ⏳ Agent orchestration (can expand after MVP)

---

## Live Test: CON-001

```bash
# Send campaign trigger
curl -X POST http://100.87.214.70:5678/webhook/venture-campaign \
  -H "Content-Type: application/json" \
  -d '{
    "venture_id": "CON-001",
    "campaign_type": "lead_gen",
    "target_audience": "electrical_contractors_nc",
    "budget_usd": 5000,
    "duration_days": 30,
    "objectives": ["leads"]
  }'

# Expected response (within 2s):
# {
#   "status": "success",
#   "campaign_id": "camp_abc...",
#   "venture_id": "CON-001",
#   "agents_assigned": 47,
#   "workflows_triggered": 8
# }

# Verify in Supabase:
SELECT * FROM campaigns WHERE venture_id = 'CON-001' ORDER BY created_at DESC LIMIT 1;
```

---

**Created:** 2026-07-22  
**Status:** Ready to implement on n8n  
**Target:** Live test by end of session
