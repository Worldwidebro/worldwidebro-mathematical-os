# Agentic Inbox Implementation — Complete Checklist

**Architecture:** Per-Venture Mailboxes (712 ventures) + Unified Contacts + VAPI Orchestration  
**Timeline:** 7 days  
**Status:** Ready to execute

---

## Phase 0: Infrastructure (Days 1-2)

### 0.1 Deploy Agentic Inbox to Cloudflare

- [ ] Clone: `git clone https://github.com/cloudflare/agentic-inbox`
- [ ] Install: `npm install`
- [ ] Set domain in `wrangler.jsonc`
- [ ] Create R2 bucket: `wrangler r2 bucket create agentic-inbox`
- [ ] Deploy: `npm run deploy`
- [ ] Configure Cloudflare Access (one-click)
- [ ] Set up Email Routing (catch-all rule)
- [ ] Enable Email Service (for sending)
- [ ] Test: Create test mailbox manually (hello@yourdomain.com)
- [ ] Verify: Send/receive test email

**Expected:** Agentic Inbox running at yourdomain.workers.dev with MCP server at /mcp

---

### 0.2 Create Unified Schema

**Migration: `006_unified_contacts_agentic_inbox.sql`**

- [ ] Create `contacts` table (master registry, no venture_id)
  ```sql
  id UUID PRIMARY KEY
  full_name, email (UNIQUE), phone, title, company, location
  contact_type, industry_guess, specialization
  warmth_score INT, engagement_score INT
  vapi_calls, email_sent, email_opened, email_replied, tasks_created
  status, created_at, updated_at
  ```

- [ ] Create `venture_mailboxes` table
  ```sql
  id UUID PRIMARY KEY
  venture_id VARCHAR (FK ventures)
  mailbox_address TEXT ('fin-001@yourdomain.com')
  mailbox_id VARCHAR (Agentic Inbox internal ID)
  system_prompt TEXT (AI agent instructions)
  created_at, updated_at
  ```

- [ ] Create `contact_venture_outreach` table
  ```sql
  id UUID PRIMARY KEY
  contact_id UUID (FK contacts)
  venture_id VARCHAR (FK ventures)
  outreach_date TIMESTAMP
  email_sent, email_opened, email_replied BOOLEAN
  vapi_called, call_outcome TEXT
  engagement_signal INT
  ```

- [ ] Create `email_interactions` table
- [ ] Create `call_interactions` table
- [ ] Migrate existing data from crm_contacts, RE-001 contacts, CSV

**Verify:** All tables created, data migrated, no errors

---

## Phase 1: Venture Mailbox Setup (Days 2-3)

### 1.1 Create venture_mailboxes Script

**File: `scripts/create_venture_mailboxes.py`**

- [ ] Load all ventures from Supabase
- [ ] For each venture: Create mailbox via Agentic Inbox API
- [ ] Store in venture_mailboxes table
- [ ] Error handling: Skip if exists, log failures

**Test:** Create 5 test mailboxes, verify in Agentic Inbox UI

---

## Phase 2: Contact Export & Enrichment (Days 3-4)

### 2.1 Export Contacts for Outreach

**File: `scripts/export_contacts_for_outreach.py`**

- [ ] Load contacts where status='active' AND warmth_score > 60
- [ ] Segment by warmth_score (High/Medium/Low)
- [ ] Export to CSV: `contacts_for_outreach.csv`

**Test:** Run script, verify CSV, check warmth_scores populated

---

### 2.2 Map Contacts to Ventures

**File: `scripts/segment_contacts_by_venture.py`**

- [ ] For each contact: Determine relevant ventures
- [ ] Use: warmth_score + sector alignment
- [ ] Output: `contact_venture_mapping.csv`

**Test:** Verify mapping generated, spot check 5 random contacts

---

## Phase 3: Email Outreach (Days 4-5)

### 3.1 Create Agentic Inbox Sender

**File: `scripts/send_emails_via_agentic_inbox.py`**

- [ ] Function: Send via Agentic Inbox API
- [ ] Rate limiting: 10 emails/minute per mailbox
- [ ] Logging: Log every send to email_interactions table
- [ ] Dry-run mode: --dry-run flag

**Test:** Send 5 test emails (dry-run), verify CSV, send 5 real

---

### 3.2 Webhook Handler: Receive Replies

**File: `routes/webhook.py` endpoint: `/webhook/agentic-inbox-reply`**

- [ ] Receive webhook from Agentic Inbox
- [ ] Parse reply, calculate engagement_signal (0-10)
- [ ] Log to email_interactions table
- [ ] If engagement_signal > 7: Create ClickUp task

**Test:** Send test email, manually reply, verify webhook logs, verify task created

---

## Phase 4: Voice Orchestration (Days 5-6)

### 4.1 VAPI Followup Script

**File: `scripts/coordinate_vapi_followup.py`**

- [ ] Query contacts: opened email + no reply after 3 days
- [ ] Call via VAPI with context
- [ ] Log outcomes to call_interactions table
- [ ] Create ClickUp task if interested/demo_booked

**Test:** Run with 5 test contacts, verify calls made, tasks created

---

## Phase 5: Analytics & Dashboard (Days 6-7)

### 5.1 Campaign Analytics

**File: `scripts/campaign_analytics.py`**

- [ ] Query metrics: sent, opened, replied, called, interested
- [ ] Generate report: `campaign_report.md`

**Test:** Run after Phase 3, verify counts correct

---

## Testing Checklist

### Integration Tests

#### Test 1: Single Venture Campaign
- [ ] Create mailbox: fin-001@yourdomain.com
- [ ] Send 3 emails
- [ ] Reply to 2
- [ ] Verify webhook logs both
- [ ] Verify ClickUp tasks created

**Expected:** All steps pass

---

#### Test 2: Multi-Venture Campaign
- [ ] 3 ventures, 5 contacts, 15 emails
- [ ] Reply to 5 emails
- [ ] Verify all logged + segmented correctly
- [ ] Verify ClickUp tasks only for high-engagement

**Expected:** All steps pass, accurate segmentation

---

#### Test 3: VAPI Followup
- [ ] 3 contacts who need VAPI calls
- [ ] Call all 3
- [ ] Verify tasks created for interested/demo_booked only

**Expected:** All steps pass, correct task filtering

---

## Success Criteria

✅ Phase 0: Agentic Inbox deployed + schema created  
✅ Phase 1: 712 mailboxes created  
✅ Phase 2: Contacts segmented + mapped  
✅ Phase 3: 50+ emails sent + replies tracked  
✅ Phase 4: VAPI followup orchestrated  
✅ Phase 5: Analytics working  

---

## Files to Create

**Scripts:**
- `scripts/create_venture_mailboxes.py`
- `scripts/export_contacts_for_outreach.py`
- `scripts/segment_contacts_by_venture.py`
- `scripts/send_emails_via_agentic_inbox.py`
- `scripts/coordinate_vapi_followup.py`
- `scripts/campaign_analytics.py`

**Routes:**
- `routes/webhook.py` (Agentic Inbox handler)

**Migrations:**
- `migrations/006_unified_contacts_agentic_inbox.sql`

---

Ready to execute Phase 0?
