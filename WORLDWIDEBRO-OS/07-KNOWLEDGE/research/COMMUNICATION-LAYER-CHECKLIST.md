# Communication Layer — Build Checklist & Test Plan

**Status:** Planning  
**Start Date:** 2026-06-06  
**Target Completion:** 2026-06-13 (1 week)

---

## Phase 1: Foundation (Day 1-2)

### Supabase Schema
- [ ] Verify `contacts` table exists (venture_id, name, email, title, status)
- [ ] Create `email_campaigns` table (id, name, segment, template, status, created_at)
- [ ] Create `email_interactions` table (id, campaign_id, contact_id, email_sent, email_opened, reply_received, reply_date, engagement_score, notes)
- [ ] Create `email_templates` table (id, name, subject_template, body_template, variables)
- [ ] Add indexes: campaigns(status), interactions(campaign_id, contact_id), templates(name)

### Python Scripts
- [ ] Create `export_contacts.py` — Query Supabase contacts, filter by status, output CSV
- [ ] Create `email_template_engine.py` — Personalize templates with Jinja2 ({{venture_name}}, {{first_name}}, etc.)
- [ ] Create `batch_email_orchestrator.py` — Load CSV, validate emails, queue for send
- [ ] Create `gmail_batch_sender.py` — Wrapper around Gmail MCP, rate limiting, error handling
- [ ] Create `response_listener.py` — Search Gmail labels, parse replies, log to Supabase

---

## Phase 2: Integration (Day 3-4)

### Gmail MCP Integration
- [ ] Test Gmail MCP authentication (already configured?)
- [ ] Create email draft via MCP (test with single recipient)
- [ ] Search Gmail for thread history (test thread retrieval)
- [ ] Label emails programmatically (tag sent emails)
- [ ] Schedule emails (test delayed send)

### ClickUp Integration
- [ ] Test ClickUp MCP authentication
- [ ] Create task from email reply (auto-generate follow-up tasks)
- [ ] Assign task to team member
- [ ] Link task to venture/contact record

### Slack Notifications
- [ ] Post campaign start to #niche-mastery
- [ ] Post daily summary (sent, opened, replied counts)
- [ ] Post blockers/errors in real-time

---

## Phase 3: Workflow (Day 5-6)

### Contact Segmentation
- [ ] Load all 712 ventures
- [ ] Segment by: stage (seed/growth/mature), sector (31-sector taxonomy), engagement_score
- [ ] Create CSV: segment_name | contact_count | avg_engagement_score

### Email Templates
- [ ] Create template: "Venture Inquiry" (outreach to founders)
- [ ] Create template: "Capability Match" (role-based)
- [ ] Create template: "Partnership Opportunity"
- [ ] Test personalization: {{venture_name}}, {{first_name}}, {{sector}}, {{stage}}

### Campaign Workflow
- [ ] Define campaign: name, segment, template, send_date, rate_limit (e.g., 10/day)
- [ ] Create campaign record in Supabase
- [ ] Queue emails for send (batch of 10)
- [ ] Log each send to email_interactions table

---

## Phase 4: Response Tracking (Day 7)

### Response Listener
- [ ] Search Gmail for replies to sent emails (label: "campaign-name")
- [ ] Parse reply (extract key phrases, sentiment)
- [ ] Update email_interactions: reply_received=true, reply_date, engagement_score+=1
- [ ] Trigger ClickUp task if reply indicates interest

### Analytics
- [ ] Query: total sent, opened, replied, bounce rate
- [ ] Query: reply rate by segment
- [ ] Query: avg time to first reply
- [ ] Export to CSV for dashboard

---

## Test Checklist

### Unit Tests (Python)

#### `test_export_contacts.py`
- [ ] Test: Query returns all contacts (expect >1000)
- [ ] Test: Filter by stage (seed) returns subset
- [ ] Test: Filter by sector (e.g., SaaS) returns correct count
- [ ] Test: Email validation (skip invalid emails)
- [ ] Test: CSV output format (headers: venture_id, contact_name, email, title, stage)

#### `test_email_template_engine.py`
- [ ] Test: Render template with all variables
- [ ] Test: Handle missing variables (skip or default)
- [ ] Test: Escape special characters in names
- [ ] Test: Subject line truncation (max 100 chars)
- [ ] Test: Personalization: "Hi {{first_name}}" → "Hi John"

#### `test_batch_email_orchestrator.py`
- [ ] Test: Load CSV, validate structure
- [ ] Test: Validate email addresses (reject invalid)
- [ ] Test: Rate limit (queue 100 emails, send 10/day)
- [ ] Test: Skip duplicates (same contact, same campaign)
- [ ] Test: Error handling (connection timeout, retry logic)

#### `test_gmail_batch_sender.py`
- [ ] Test: Create draft via Gmail MCP
- [ ] Test: Search existing thread
- [ ] Test: Label email after send
- [ ] Test: Handle Gmail API rate limit (429)
- [ ] Test: Retry failed send (exponential backoff)

#### `test_response_listener.py`
- [ ] Test: Search Gmail for replies to label
- [ ] Test: Parse reply date from email
- [ ] Test: Extract engagement signal (yes/no/maybe)
- [ ] Test: Update Supabase interaction record
- [ ] Test: Create ClickUp task on positive reply

---

### Integration Tests

#### `test_end_to_end_single_campaign.py`
**Objective:** Send 1 email, verify it arrives, log interaction, test reply flow

**Setup:**
```python
- Create test contact: test@example.com
- Create test campaign: "test-campaign-001"
- Create test template with {{first_name}}, {{venture_name}}
```

**Test Steps:**
- [ ] Step 1: Export contacts (should include test contact)
- [ ] Step 2: Generate email (verify personalization)
- [ ] Step 3: Send via Gmail MCP (verify draft created)
- [ ] Step 4: Check Supabase email_interactions (verify sent_at logged)
- [ ] Step 5: Label email in Gmail
- [ ] Step 6: Simulate reply in Gmail (send reply email manually)
- [ ] Step 7: Run response_listener (verify reply detected)
- [ ] Step 8: Check Supabase (verify reply_received=true, reply_date logged)
- [ ] Step 9: Verify ClickUp task created (if engagement_score > threshold)

**Expected Result:**
- Supabase email_interactions row: campaign_id, contact_id, email_sent, reply_received=true, reply_date logged

---

#### `test_campaign_segmentation.py`
**Objective:** Verify contact segmentation by stage/sector

**Test Cases:**
- [ ] Test 1: Export "seed stage + SaaS" (expect 50-100 contacts)
- [ ] Test 2: Export "growth stage + HR Tech" (expect 20-50 contacts)
- [ ] Test 3: Verify no duplicates across segments
- [ ] Test 4: Verify all emails are valid format
- [ ] Test 5: CSV sorted by engagement_score (descending)

---

#### `test_rate_limiting.py`
**Objective:** Verify batch sender respects rate limits

**Setup:**
- Create campaign with 50 test contacts
- Set rate_limit = 10 per day

**Test Steps:**
- [ ] Step 1: Queue 50 emails
- [ ] Step 2: Send batch (should send 10, queue 40)
- [ ] Step 3: Check Supabase (verify 10 interactions logged, status="sent")
- [ ] Step 4: Check 40 queued (status="queued")
- [ ] Step 5: Run scheduler again next day (should send next 10)

**Expected Result:**
- Day 1: 10 sent, 40 queued
- Day 2: 20 sent, 30 queued
- Day 5: 50 sent

---

### Manual Tests (Verification)

#### Manual Test 1: Single Email Send
```
1. Run: python3 export_contacts.py --segment "test" --limit 1
2. Run: python3 batch_email_orchestrator.py --csv contacts.csv --template "venture_inquiry" --dry-run
3. Verify: Email preview shows correct personalization
4. Run: python3 batch_email_orchestrator.py --csv contacts.csv --template "venture_inquiry"
5. Check Gmail: Draft folder should have 1 email
6. Verify Supabase: email_interactions should have 1 row
```

**Expected:** Email sent successfully, logged in Supabase

---

#### Manual Test 2: Campaign Dashboard
```
1. Run: python3 populate_venture_knowledge_graph.py (update contact counts)
2. Run: python3 obsidian_graph_sync.py
3. Open Obsidian: KNOWLEDGE-GRAPH-DASHBOARD.md
4. Verify: Contact counts by sector displayed
5. Create new view: Campaign Summary (sent/opened/replied by segment)
```

**Expected:** Dashboard shows real-time campaign metrics

---

#### Manual Test 3: Response Tracking
```
1. Run: python3 response_listener.py --campaign "test-campaign-001"
2. Check Supabase: email_interactions.reply_received updated
3. Check ClickUp: New task created for positive reply
4. Verify Slack: Notification posted to #niche-mastery
```

**Expected:** Reply detected, task created, notification sent

---

### Performance Tests

- [ ] Test: Send 1000 emails (rate: 10/day) — verify queuing works
- [ ] Test: Search 500 replies in Gmail — response_listener runs in <5 min
- [ ] Test: Supabase query performance (email_interactions table with 10k rows)
- [ ] Test: Memory usage (batch_email_orchestrator with 10k contacts in memory)

---

### Error Handling Tests

- [ ] Test: Invalid email address → skip, log error
- [ ] Test: Gmail API rate limit → exponential backoff
- [ ] Test: Supabase connection timeout → retry with exponential backoff
- [ ] Test: Missing template variable → use default or skip
- [ ] Test: Duplicate send attempt → idempotent (skip if already sent)
- [ ] Test: Contact deleted between export and send → graceful fail

---

## Success Criteria

✅ **Phase 1 (Schema + Scripts):** All Python scripts run without error  
✅ **Phase 2 (Integration):** Gmail MCP sends/receives emails, ClickUp creates tasks  
✅ **Phase 3 (Workflow):** Campaign created, contacts segmented, emails queued  
✅ **Phase 4 (Tracking):** Replies detected, engagement_score updated, tasks created  

**Final Verification:**
- [ ] Send 10 test emails to real email (Gmail)
- [ ] Manually reply to 5
- [ ] Run response_listener (verify all 5 replies detected)
- [ ] Check Supabase (all 5 have reply_received=true, reply_date logged)
- [ ] Check ClickUp (5 follow-up tasks created)
- [ ] Check Slack (campaign summary posted)

---

## Timeline

| Phase | Task | Start | End | Owner |
|-------|------|-------|-----|-------|
| 1 | Schema + Scripts | 2026-06-06 | 2026-06-07 | Claude |
| 2 | Gmail + ClickUp Integration | 2026-06-08 | 2026-06-09 | Claude |
| 3 | Workflow + Templates | 2026-06-10 | 2026-06-11 | Claude |
| 4 | Response Tracking | 2026-06-12 | 2026-06-13 | Claude |
| 5 | Testing + Verification | 2026-06-13 | 2026-06-13 | Claude |

---

## Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Gmail API rate limit (500/day) | Implement queue, rate-limit to 50/day for safety |
| Invalid contacts | Validate email format before send, maintain bounce list |
| Duplicate sends | Check email_interactions before sending |
| Reply spam | Filter by domain, check for auto-replies |
| ClickUp task overload | Create tasks only for high-engagement replies (score > 3) |
