# Communication Layer — File Alignment Audit

**Status:** UPDATED FOR AGENTIC INBOX  
**Date:** 2026-06-06  
**Architecture:** Option B (Cross-Venture Contacts) + Agentic Inbox (Email Infrastructure)  
**Core Stack:** VAPI (voice) + Agentic Inbox (email) + Supabase (unified contacts) + ClickUp (tasks)

---

## Executive Summary

You have **3 separate contact schemas** + **4 communication channels** (voice, email, enrichment, task) scattered across 5+ files. 

**Key Decision:** Contacts are **NOT venture-scoped**. One person reaches out to a contact about multiple ventures (HRMS + Construction + etc). This means contacts table has no `venture_id` FK—ventures reference contacts, not vice versa.

**Critical Conflicts (Must Fix):**
- [ ] 2 different "contacts" tables (crm_contacts vs contacts) → merge into single `contacts` table
- [ ] crm_contacts has venture_id FK → remove, use campaign_venture_mapping instead
- [ ] RE-001 contacts is real-estate-only → merge into unified contacts
- [ ] VAPI + ClickUp not synced (calls don't create tasks)
- [ ] Make.com enrichment workflow exists but not integrated
- [ ] Email templates in Python but Gmail MCP not hooked up

**Gaps (Need Creation):**
- [ ] email_interactions table (logs sent/opened/replied)
- [ ] email_campaigns table (campaign definitions, can be venture-specific OR cross-venture)
- [ ] email_templates table (template management)
- [ ] campaign_contact_mapping table (which contact in which campaign)
- [ ] campaign_venture_mapping table (which ventures in which campaign)

---

## Current Contact Schemas (3 VERSIONS — CONSOLIDATE INTO 1)

### Version 1: CRM Contacts (Venture Hub)
**File:** `/venture-hub/supabase/migrations/002_create_contracts_crm_tables.sql`  
**Table:** `crm_contacts` (WILL BE DEPRECATED)

```sql
id UUID PRIMARY KEY
venture_id TEXT ← REMOVE (contacts are cross-venture)
full_name TEXT
role TEXT
email TEXT
phone TEXT
type TEXT ('client', 'lead', 'prospect', 'partner', 'vendor')
status TEXT ('active', 'inactive', 'churned')
notes TEXT
created_at, updated_at
```

**Action:** Keep structure, remove `venture_id` FK, migrate data to unified `contacts` table.

---

### Version 2: RE-001 Contacts (Real Estate)
**File:** `/RE-001-Worldwidebro-Holdings/24_INTEGRATIONS/supabase/schema.sql`  
**Table:** `contacts` (WILL BE CONSOLIDATED)

```sql
id UUID PRIMARY KEY
contact_name TEXT
contact_type TEXT
title TEXT
company TEXT
phone TEXT
email TEXT
city, state
specialization TEXT
```

**Action:** Merge into unified `contacts` table, map fields.

---

### Version 3: CSV Contacts (WORLDWIDEBRO OS)
**File:** `/WORLDWIDEBRO-OS/03_SALES/Contacts/contacts-extracted.csv`  
**Rows:** 59 contacts

```csv
name, phone, email, company, location, industry_guess, warmth_score
```

**Action:** Import into unified `contacts` table via migration script.

---

## NEW: Unified Contacts Table (Option B Architecture)

**Table: `contacts`** (Master contact registry — NO venture_id)

```sql
id UUID PRIMARY KEY DEFAULT gen_random_uuid()

-- Identity
full_name TEXT NOT NULL
email TEXT UNIQUE
phone TEXT
title TEXT
company TEXT
location TEXT (city, state)

-- Contact Classification
contact_type TEXT ('prospect', 'client', 'partner', 'vendor', 'influencer')
industry_guess TEXT
specialization TEXT

-- Engagement Metrics (accumulated across all ventures)
warmth_score INT (0-100, calculated by Make.com)
engagement_score INT (0-100, calculated from interactions)
last_interaction_date TIMESTAMP
interaction_count INT

-- Interaction History
vapi_calls_received INT DEFAULT 0
email_sent INT DEFAULT 0
email_opened INT DEFAULT 0
email_replied INT DEFAULT 0
tasks_created INT DEFAULT 0

-- Metadata
notes TEXT
status TEXT ('active', 'inactive', 'churned')
created_at TIMESTAMP DEFAULT NOW()
updated_at TIMESTAMP DEFAULT NOW()

-- Audit
source_system TEXT ('crm_contacts', 'real_estate', 'csv')
source_id VARCHAR
```

**Key Change:** Contacts exist independently. Ventures reference them via campaigns, not directly.

---

## Communication Infrastructure (4 CHANNELS — PARTIALLY CONNECTED)

### Channel 1: Voice (VAPI)
**File:** `/WORLDWIDEBRO-OS/07_AUTOMATIONS/VAPI-API-USAGE.md`  
**Status:** ✅ Ready

**Current Capabilities:**
- ✅ Agent deployment (Echo, Swift, Bella)
- ✅ Outbound calls
- ✅ Transcript capture
- ✅ Campaign orchestration
- ✅ Webhook on call completion

**Missing:**
- ❌ Supabase logging of call results
- ❌ ClickUp task creation on call
- ❌ Contact table integration

---

### Channel 2: Email (Agentic Inbox — Replaces Gmail MCP)
**Status:** ✅ OPTIMAL CHOICE (Self-hosted, per-venture mailboxes)

**Agentic Inbox Capabilities:**
- ✅ Self-hosted on Cloudflare Workers
- ✅ Send/receive via Cloudflare Email Service + Email Routing
- ✅ Built-in AI agent (reads, searches, drafts, sends)
- ✅ Per-mailbox SQLite storage
- ✅ R2 attachment storage
- ✅ MCP server at /mcp (native Claude Code integration)
- ✅ Auto-drafts replies (AI-generated, requires human confirmation)

**Per-Venture Mailbox Architecture:**
```
712 ventures → 712 mailboxes
  FIN-001 → fin-001@yourdomain.com
  FIN-002 → fin-002@yourdomain.com
  CON-001 → con-001@yourdomain.com
  ...
```

**What This Replaces:**
- ❌ Gmail MCP (removed—Agentic Inbox is better)
- ❌ response_listener.py (removed—built-in to Agentic Inbox)
- ❌ email_template_engine.py (simplified—AI agent generates drafts)
- ⚠️ batch_email_orchestrator.py (simplified—Agentic Inbox API handles sends)

**What We Still Need:**
- ✅ export_contacts.py (load contacts from Supabase)
- ✅ Simple sender: `send_via_agentic_inbox.py` (call /api/send endpoint)
- ✅ Webhook handler: receive replies → update contacts table
- ✅ Campaign orchestrator: route contacts to ventures

---

### Channel 3: Contact Enrichment (Make.com)
**File:** `/make-workflows/workflow-3-contact-enrichment.json`  
**Status:** ⚠️ Workflow defined, not integrated

**Current Capabilities:**
- ✅ OSINT enrichment (LinkedIn, GitHub, Twitter patterns)
- ✅ Warmth score calculation (0-100)
- ✅ Fit score matching (venture alignment)
- ✅ Sector expertise mapping

**Missing:**
- ❌ No Supabase contact table to enrich
- ❌ No trigger mechanism
- ❌ No output table for enriched data

---

### Channel 4: Task Management (ClickUp)
**Status:** ⚠️ API ready, integration missing

**Missing:**
- ❌ No automation linking call → task
- ❌ No automation linking email reply → task
- ❌ No automation linking enrichment → task

---

## Database Schema Changes (With Agentic Inbox)

```sql
-- Master contacts (no venture_id, cross-venture)
CREATE TABLE contacts (
  id UUID PRIMARY KEY,
  full_name TEXT NOT NULL,
  email TEXT UNIQUE,
  phone TEXT,
  title, company, location,
  contact_type, industry_guess, specialization,
  warmth_score INT, engagement_score INT,
  vapi_calls_received INT DEFAULT 0,
  email_sent INT DEFAULT 0,
  email_opened INT DEFAULT 0,
  email_replied INT DEFAULT 0,
  tasks_created INT DEFAULT 0,
  status, created_at, updated_at
);

-- VENTURE → MAILBOX MAPPING (New: Per-venture Agentic Inbox mailbox)
CREATE TABLE venture_mailboxes (
  id UUID PRIMARY KEY,
  venture_id VARCHAR REFERENCES ventures(venture_id),
  mailbox_address TEXT (e.g., 'fin-001@yourdomain.com'),
  mailbox_id VARCHAR (Agentic Inbox internal ID),
  agentic_inbox_api_key TEXT (secure),
  system_prompt TEXT (AI agent instructions per venture),
  created_at, updated_at
);

-- CONTACT → VENTURE OUTREACH (Track which ventures we've reached out to)
CREATE TABLE contact_venture_outreach (
  id UUID PRIMARY KEY,
  contact_id UUID REFERENCES contacts(id),
  venture_id VARCHAR REFERENCES ventures(venture_id),
  outreach_date TIMESTAMP,
  email_sent BOOLEAN,
  email_opened BOOLEAN,
  email_replied BOOLEAN,
  reply_content TEXT,
  vapi_called BOOLEAN,
  call_outcome TEXT,
  engagement_signal INT (0-10),
  tasks_created INT
);

-- EMAIL INTERACTIONS (Logged from Agentic Inbox)
CREATE TABLE email_interactions (
  id UUID PRIMARY KEY,
  venture_id VARCHAR REFERENCES ventures(venture_id),
  contact_id UUID REFERENCES contacts(id),
  mailbox_id VARCHAR,
  direction TEXT ('inbound', 'outbound'),
  subject TEXT,
  body TEXT,
  sent_at TIMESTAMP,
  opened_at TIMESTAMP,
  replied_at TIMESTAMP,
  reply_content TEXT,
  engagement_signal INT (0-10)
);

-- VOICE INTERACTIONS (From VAPI)
CREATE TABLE call_interactions (
  id UUID PRIMARY KEY,
  venture_id VARCHAR REFERENCES ventures(venture_id),
  contact_id UUID REFERENCES contacts(id),
  agent_name TEXT,
  call_duration_seconds INT,
  outcome TEXT ('interested', 'not_interested', 'demo_booked'),
  transcript TEXT,
  recording_url TEXT,
  called_at TIMESTAMP
);
```

**Key Differences from Previous Schema:**
- ❌ Removed: `campaigns`, `campaign_venture_mapping`, `campaign_contact_mapping` (replaced by per-venture mailboxes)
- ✅ Added: `venture_mailboxes` (one mailbox per venture, managed by Agentic Inbox)
- ✅ Added: `contact_venture_outreach` (tracks per-venture engagement)
- ✅ Simplified: Direct venture_id references (no campaign layer needed)

---

## Database Alignment Issues (Now with Option B Clarity)

### Issue 1: No Central Contact ID (RESOLVED)
**Problem:** 
- crm_contacts has UUID id
- RE-001 contacts has UUID id
- CSV contacts have name (no ID)
- VAPI logs by phone
- Gmail logs by email
- Make.com processes by email

**Solution:** Create unified contact ID mapping table

### Issue 2: Missing Campaign Context
**Problem:**
- Email templates exist but no `email_campaigns` table
- No `campaign_contact_mapping` tracking
- No unified campaign ID

### Issue 3: Warmth & Engagement Scores
**Problem:**
- CSV has warmth_score
- Make.com calculates warmth_score
- But no unified engagement_score table
- No time-series tracking

---

## Integration Priority (Recommend This Order)

| Phase | Task | Files | Timeline |
|-------|------|-------|----------|
| **1** | Schema unification | operating_system_schema.sql | Day 1-2 |
| **2** | Create communication tables | migrations/*.sql | Day 1-2 |
| **3** | Wire VAPI → Supabase → ClickUp | VAPI-API-USAGE.md + new script | Day 3-4 |
| **4** | Wire Make.com enrichment → Supabase | workflow-3-contact-enrichment.json | Day 3-4 |
| **5** | Email infrastructure (export + batch + listener) | 5 new Python scripts | Day 5-6 |
| **6** | Campaign orchestrator | new campaign_orchestrator.py | Day 6-7 |
| **7** | Test full flow (email + voice + task) | integration test | Day 7 |

---

## Implementation Plan: Agentic Inbox + Unified Contacts

### Phase 0: Infrastructure Setup (Days 1-2 — FOUNDATION)

**Step 1: Deploy Agentic Inbox to Cloudflare**
```bash
# Clone repo
git clone https://github.com/cloudflare/agentic-inbox
cd agentic-inbox
npm install

# Configure
# 1. Set DOMAINS in wrangler.jsonc (your domain)
# 2. Create R2 bucket: wrangler r2 bucket create agentic-inbox
# 3. Deploy: npm run deploy
# 4. Configure Cloudflare Access (one-click)
# 5. Set up Email Routing (catch-all rule)
# 6. Enable Email Service (for sending)
```

**Step 2: Create Unified Contacts Schema**
```bash
# Migration: 006_unified_contacts_with_agentic_inbox.sql
-- 1. Create master contacts table
CREATE TABLE contacts (id, full_name, email, phone, ...);

-- 2. Migrate existing data
INSERT INTO contacts SELECT * FROM crm_contacts;
INSERT INTO contacts SELECT * FROM re_001_contacts;
INSERT INTO contacts SELECT * FROM csv_contacts;

-- 3. Create venture-mailbox mapping
CREATE TABLE venture_mailboxes (venture_id, mailbox_address, mailbox_id, system_prompt, ...);

-- 4. Create outreach tracking
CREATE TABLE contact_venture_outreach (contact_id, venture_id, email_sent, email_opened, ...);

-- 5. Create interaction logging
CREATE TABLE email_interactions (venture_id, contact_id, mailbox_id, direction, ...);
CREATE TABLE call_interactions (venture_id, contact_id, outcome, transcript, ...);

-- 6. Keep old tables for backward compatibility
ALTER TABLE crm_contacts RENAME TO crm_contacts_deprecated;
CREATE VIEW crm_contacts AS SELECT * FROM contacts;
```

### Phase 1: Venture Mailbox Setup (Day 2-3)

**Script: `create_venture_mailboxes.py`**
```python
# For each venture in ventures table:
for venture in ventures:
    mailbox_address = f"{venture.venture_id}@yourdomain.com"
    
    # Call Agentic Inbox API to create mailbox
    mailbox = agentic_inbox_api.create_mailbox(
        address=mailbox_address,
        system_prompt=VENTURE_SYSTEM_PROMPTS[venture.sector]
    )
    
    # Store in venture_mailboxes table
    db.insert_venture_mailbox(
        venture_id=venture.venture_id,
        mailbox_address=mailbox_address,
        mailbox_id=mailbox.id,
        agentic_inbox_api_key=mailbox.api_key
    )
```

**Result:** 712 mailboxes created, one per venture.

### Phase 2: Contact Export & Enrichment (Day 3-4)

**Script: `export_contacts_for_outreach.py`**
```python
# Load all contacts from contacts table
contacts = db.query("SELECT * FROM contacts WHERE status='active'")

# Segment by warmth_score + fit_score (from Make.com enrichment)
high_warmth = [c for c in contacts if c.warmth_score > 70]
medium_warmth = [c for c in contacts if c.warmth_score 40-70]

# Export to CSV for review
export_csv(high_warmth, "high-warmth-contacts.csv")
```

### Phase 3: Email Outreach (Day 4-5)

**Script: `send_emails_via_agentic_inbox.py`**
```python
for venture in ventures[:10]:  # Start with 10 ventures
    mailbox = db.get_venture_mailbox(venture.venture_id)
    
    for contact in get_contacts_for_venture(venture):
        # Send via Agentic Inbox API
        agentic_inbox_api.send_email(
            mailbox_id=mailbox.mailbox_id,
            to=contact.email,
            subject=f"Opportunity in {venture.name}",
            body=VENTURE_EMAIL_TEMPLATES[venture.sector]
        )
        
        # Log to email_interactions
        db.insert_email_interaction(
            venture_id=venture.venture_id,
            contact_id=contact.id,
            direction='outbound',
            sent_at=datetime.now()
        )

# Agentic Inbox handles:
# ✅ Receiving replies
# ✅ Storing in SQLite per mailbox
# ✅ AI agent reads + auto-drafts responses
# ✅ Webhook notifies us of replies
```

**Webhook Handler (Agentic Inbox → Supabase):**
```python
@app.post("/webhook/agentic-inbox-reply")
def handle_inbox_reply(event):
    # Event: { mailbox_id, contact_email, subject, body }
    
    contact = db.get_contact_by_email(event.contact_email)
    venture = db.get_venture_by_mailbox(event.mailbox_id)
    
    # Update contacts table
    db.update_contact(contact.id, email_replied=True)
    
    # Log interaction
    db.insert_email_interaction(
        venture_id=venture.venture_id,
        contact_id=contact.id,
        direction='inbound',
        reply_content=event.body,
        engagement_signal=ENGAGEMENT_SCORER(event.body)  # 0-10
    )
    
    # Update outreach tracking
    db.update_contact_venture_outreach(
        contact_id=contact.id,
        venture_id=venture.venture_id,
        email_replied=True,
        engagement_signal=ENGAGEMENT_SCORER(event.body)
    )
    
    # If high engagement: create ClickUp task
    if ENGAGEMENT_SCORER(event.body) > 7:
        create_clickup_task(
            title=f"Follow up: {contact.full_name} for {venture.name}",
            venture_id=venture.venture_id,
            contact_id=contact.id
        )

    return {"status": "logged"}
```

### Phase 4: Voice + Task Automation (Day 5-6)

**Script: `coordinate_voice_followup.py`**
```python
# For contacts who opened email but didn't reply after 3 days
for outreach in db.query("""
    SELECT co.* FROM contact_venture_outreach co
    WHERE co.email_opened=TRUE 
    AND co.email_replied=FALSE
    AND co.outreach_date < NOW() - INTERVAL '3 days'
"""):
    contact = db.get_contact(outreach.contact_id)
    venture = db.get_venture(outreach.venture_id)
    
    # Trigger VAPI call
    vapi_result = vapi_api.call(
        contact.phone,
        agent_id=VENTURE_AGENTS[venture.sector],
        context=f"Interested in {venture.name}"
    )
    
    # Log call
    db.insert_call_interaction(
        venture_id=venture.venture_id,
        contact_id=contact.id,
        call_duration_seconds=vapi_result.duration,
        outcome=vapi_result.outcome,  # 'interested', 'demo_booked', etc
        transcript=vapi_result.transcript
    )
    
    # Update outreach
    db.update_contact_venture_outreach(
        outreach.id,
        vapi_called=True,
        call_outcome=vapi_result.outcome
    )
    
    # If call positive: create task
    if vapi_result.outcome in ['interested', 'demo_booked']:
        create_clickup_task(
            title=f"Schedule {vapi_result.outcome}: {contact.full_name} for {venture.name}",
            venture_id=venture.venture_id,
            contact_id=contact.id,
            priority='high'
        )
```

### Phase 5: Testing (Day 6-7)

**Test Plan:**
```
1. Create 3 test mailboxes (FIN-001, FIN-002, CON-001)
2. Send test emails to 5 contacts
3. Manually reply to 2 (Agentic Inbox should receive)
4. Verify webhook logs replies to Supabase
5. Verify ClickUp tasks created for positive replies
6. Verify AI agent auto-drafted response (shown in UI, pending confirmation)
7. Trigger VAPI call to remaining 3
8. Verify call interactions logged
```

---

## SIMPLIFIED CHECKLIST (vs. Old Gmail Version)

| Task | Old Stack | New Stack |
|------|-----------|-----------|
| Email sending | Custom batch sender | Agentic Inbox API |
| Email receiving | Gmail labels + search | Agentic Inbox webhook |
| Response detection | response_listener.py (custom) | Agentic Inbox native |
| AI drafting | None (manual) | Agentic Inbox built-in |
| Template management | Jinja2 engine | Agentic Inbox system_prompt |
| Storage | Supabase only | SQLite (per mailbox) + Supabase (summary) |
| Self-hosted | ❌ | ✅ Cloudflare Workers |
| Per-venture isolation | ❌ | ✅ (712 mailboxes) |
| Python scripts needed | 5 | 3 |

**3 Scripts Needed:**
1. `create_venture_mailboxes.py` — Setup
2. `send_emails_via_agentic_inbox.py` — Outreach
3. `coordinate_voice_followup.py` — VAPI orchestration

(vs. 5 scripts with Gmail MCP)

