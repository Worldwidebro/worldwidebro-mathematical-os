---
name: OPENVOLO-INTEGRATION-GUIDE
title: OpenVolo Integration Architecture
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# OpenVolo Integration Architecture

**Status:** Live at http://localhost:3000  
**Deployment Date:** 2026-05-10  
**Purpose:** AI-native social CRM for contact intelligence + agent routing

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA LAYER                               │
├─────────────────────────────────────────────────────────────┤
│ • contacts-extracted.csv (60 initial contacts)              │
│ • Supabase ventures + metadata (687 ventures)               │
│ • Social media enrichment (Playwright → LinkedIn/Twitter)   │
└──────────────────┬──────────────────────────────────────────┘
                   │ IMPORT + ENRICH
                   ▼
┌─────────────────────────────────────────────────────────────┐
│              OPENVOLO (Knowledge Layer)                      │
├─────────────────────────────────────────────────────────────┤
│ • Contact graph (name → company → social → needs)           │
│ • Warmth scoring (enriched from CSV + social signals)       │
│ • Venture matching (contact pain → ECOM/TECH/BEAUTY)        │
│ • Workflow templates (10 seeded, customize per sector)      │
│ • Vector embeddings (RAG for context retrieval)             │
└──────────────────┬──────────────────────────────────────────┘
                   │ QUERY CONTACTS BY SECTOR
                   ▼
┌─────────────────────────────────────────────────────────────┐
│         PULSEAGENT (Decision Layer)                          │
├─────────────────────────────────────────────────────────────┤
│ • Reads contact from OpenVolo                               │
│ • Selects venture match (ECOM-001, TECH-015, etc.)          │
│ • Generates personalized call sequence                      │
│ • Routes to sector agent (Echo/Swift/Bella)                 │
└──────────────────┬──────────────────────────────────────────┘
                   │ GET AGENT + SCRIPT
                   ▼
┌─────────────────────────────────────────────────────────────┐
│            VAPI AGENTS (Execution Layer)                     │
├─────────────────────────────────────────────────────────────┤
│ • Echo (E-Commerce): inventory sync, channel conflict       │
│ • Swift (Technology): deploy time, shipping velocity        │
│ • Bella (Beauty): no-shows, revenue per appointment         │
│ • Call outcomes: demo_booked, interested, not_interested    │
└──────────────────┬──────────────────────────────────────────┘
                   │ CALL COMPLETE
                   ▼
┌─────────────────────────────────────────────────────────────┐
│       OUTCOME LOGGING (ClickUp + Supabase)                   │
├─────────────────────────────────────────────────────────────┤
│ • IF demo_booked → create task in ClickUp "Negotiations"    │
│ • IF interested → log in OpenVolo, schedule callback        │
│ • IF not_interested → mark outcome, don't retry             │
│ • ALL calls → log to Supabase ai_calls table                │
└─────────────────────────────────────────────────────────────┘
```

---

## PHASE 1: Data Import to OpenVolo

### Step 1: Import CSV to OpenVolo Dashboard
**URL:** http://localhost:3000/dashboard

1. Click **"Import Contacts"** 
2. Upload `contacts-extracted.csv`
3. Map fields:
   - `name` → Name
   - `phone` → Phone
   - `email` → Email (if available)
   - `company` → Company
   - `location` → Location
   - `industry_guess` → Industry
   - `warmth_score` → Initial Warmth Score

**Expected:** 60 contacts imported, status: "pending enrichment"

---

### Step 2: Configure Enrichment Workflows

**Goal:** Enhance each contact with social profiles, company data, decision-maker role

**Available Workflows:**
1. **LinkedIn Profile Lookup** (Playwright → LinkedIn)
   - Finds company page, decision-maker title, connection signals
   - Updates warmth_score based on mutual connections
2. **Company Enrichment** (ZoomInfo-style)
   - Company size, funding stage, tech stack
   - Employee count, revenue signals
3. **Social Signal Scoring**
   - Twitter/LinkedIn follower count
   - Recent activity, industry engagement
   - Adjusts warmth_score (active industry people = warmer leads)

**Setup:**
- Dashboard → Settings → Workflows
- Enable: LinkedIn Lookup, Company Enrichment, Social Signals
- Run enrichment: Button **"Enrich All Contacts"**
- Wait for completion (~5-10 min for 60 contacts with Playwright)

---

## PHASE 2: Venture Matching

### Step 3: Map Contacts to Ventures

**Goal:** For each contact, identify which venture(s) they need

**Process:**
1. OpenVolo analyzes contact role + company + industry
2. Queries Supabase ventures table
3. Surfaces top 3 venture matches per contact

**Example:**
```
Contact: "John Smith, VP Sales, E-Commerce Company"
  → Needs: Inventory sync, channel management, reporting
  → Ventures matched:
     1. ECOM-001 (Inventory sync tool) — 95% fit
     2. ECOM-015 (Multi-channel reporting) — 87% fit
     3. ECOM-042 (Order fulfillment) — 76% fit
  → Assigned sector: E-Commerce (Echo agent)
  → Call script: "Hi John, I noticed you're managing [channels]. Quick question..."
```

**Dashboard Action:**
- Contacts → [Contact Name] → "Show Venture Matches"
- Select primary venture (highest fit)
- System auto-assigns sector agent

---

## PHASE 3: PulseAgent Integration (Call Routing)

### Step 4: Configure Agent Routing

**Integration Point:** OpenVolo API → PulseAgent

**PulseAgent Workflow:**
```bash
FOR EACH contact IN openvolo.get_contacts(sector='e-commerce'):
  venture = contact.venture_matched  # e.g., ECOM-001
  script = get_deal_script(sector='e-commerce', venture=venture)
  agent = get_agent_name(sector='e-commerce')  # 'Echo'
  
  # Send to VAPI
  vapi.call({
    'phone': contact.phone,
    'agent': agent,
    'context': {
      'name': contact.name,
      'company': contact.company,
      'venture': venture,
      'pain_point': script.pain_discovery,
      'opening': script.opening
    }
  })
```

**ClickUp Setup Reference:**
- Workspace ID: 9013677375
- Leads—E-Commerce Tier 1: 901327162792
- Leads—Technology Tier 1: 901327162793
- Leads—Beauty & Wellness Tier 1: 901327162794
- Negotiations—Active Deals: 901327162795
- Closed Deals—Revenue: 901327162796

---

## PHASE 4: Call Outcome Logging

### Step 5: Webhook → ClickUp + Supabase

**When VAPI call completes:**

```json
{
  "contact_id": "contact_uuid_from_openvolo",
  "phone": "+1 (704) 807-5038",
  "agent": "Echo",
  "outcome": "demo_booked",
  "demo_date": "2026-05-15T14:00:00Z",
  "call_duration": 480,
  "notes": "Interested in inventory sync, mentioned oversells 2-3x/week"
}
```

**Action 1: Create ClickUp Task**
```
IF outcome == "demo_booked":
  list_id = 901327162795  # Negotiations
  task = {
    "name": "[Echo] Deon D.I.P | ECOM-001 | Demo 5/15 @ 2pm",
    "stage": "demo_scheduled",
    "deal_value": 800,  # $800/month estimate
    "contact_phone": "+1 (704) 807-5038",
    "blockers": "None"
  }
  clickup.create_task(task)
```

**Action 2: Update OpenVolo**
```
contact.update({
  "last_contacted": "2026-05-10T09:15:00Z",
  "demo_scheduled": "2026-05-15T14:00:00Z",
  "outcome": "demo_booked",
  "notes": call_transcript_summary
})
```

**Action 3: Log to Supabase**
```sql
INSERT INTO ai_calls (
  contact_id, 
  phone, 
  agent_type, 
  outcome, 
  call_duration, 
  venture_matched,
  transcription,
  created_at
) VALUES (...)
```

---

## PHASE 5: Weekly Execution Cycle

### Week 1: E-Commerce (Echo)
- **Contacts:** 50 prospects from OpenVolo (warmth_score 5+)
- **Agent:** Echo
- **Target:** 7-10 demos booked (15-20% close rate)
- **Outcome:** Demos move to ClickUp Negotiations

### Week 2: Technology (Swift) 
- **Contacts:** 30 prospects from OpenVolo
- **Agent:** Swift
- **Target:** 5-6 demos booked (18-22% close rate)

### Week 3: Beauty & Wellness (Bella)
- **Contacts:** 40 prospects from OpenVolo
- **Agent:** Bella
- **Target:** 5-7 demos booked (12-18% close rate)

---

## Files Needed

### 1. PulseAgent Integration Script
```python
# pulseagent_orchestrator.py
import openvolo
import vapi
import clickup

for contact in openvolo.list_contacts(sector='e-commerce', warmth_min=5):
    venture = contact.venture_matched
    phone = contact.phone
    
    # Get script
    script = get_script(venture)
    
    # Call via VAPI
    result = vapi.make_call(
        phone=phone,
        agent='Echo',
        context={'venture': venture, 'pain': script.pain_point}
    )
    
    # Log outcome
    if result.outcome == 'demo_booked':
        clickup.create_task(...wait_for_demo_data)
```

### 2. Webhook Handler (VAPI → ClickUp)
```python
# webhook_handler.py
@app.post('/webhook/vapi-outcome')
def handle_vapi_outcome(data):
    contact = openvolo.get_contact(data['contact_id'])
    
    if data['outcome'] == 'demo_booked':
        clickup.create_task(
            list_id=NEGOTIATIONS_LIST,
            name=f"[{data['agent']}] {contact.name} | Demo {data['demo_date']}"
        )
    
    # Log to Supabase
    db.ai_calls.insert(data)
    
    return {'status': 'logged'}
```

---

## Success Metrics (Weekly)

| Week | Sector | Calls | Demos | Close Rate | Revenue |
|------|--------|-------|-------|-----------|---------|
| 1 | E-Commerce | 50 | 7 | 15% | $2-4K/mo |
| 2 | Technology | 30 | 6 | 20% | $1.5-3K/mo |
| 3 | Beauty | 40 | 5 | 13% | $1-2K/mo |
| **Total** | | **120** | **18** | **15%** | **$4.5-9K/mo** |

---

## Next Steps

1. ✅ OpenVolo live (http://localhost:3000)
2. ✅ Playwright installed (for enrichment)
3. ⏳ Import contacts-extracted.csv → OpenVolo
4. ⏳ Run enrichment workflows (LinkedIn, company, social signals)
5. ⏳ Map contacts to ventures
6. ⏳ Build PulseAgent integration
7. ⏳ Configure VAPI → ClickUp webhook
8. ⏳ Execute Week 1 calling campaign (E-Commerce)
