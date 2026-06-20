# Phase 1 Implementation Checklist

**Timeline:** May 10-11, 2026  
**Goal:** Deploy Echo agent, test, iterate, launch E-Commerce campaign  
**Owner:** Worldwidebro Holdings AI Systems

---

## MONDAY, MAY 10

### Morning (9am-12pm): VAPI Setup & Configuration

- [ ] **09:00** Create VAPI account at vapi.ai
  - Email: winnerscirclewcllc@gmail.com
  - Workspace: "Worldwidebro AI Calling"
  - Verify email + set password

- [ ] **09:30** Connect Twilio integration
  - Settings → Integrations → Twilio
  - Enter Twilio Account SID + Auth Token
  - Authorize integration

- [ ] **10:00** Purchase phone numbers (3 total)
  - Phone 1: +1-XXX-ECOM-001 (E-Commerce)
  - Phone 2: +1-XXX-TECH-001 (Technology)
  - Phone 3: +1-XXX-BW-001 (Beauty)
  - Note phone numbers in tracking doc

- [ ] **10:30** Create Echo agent in VAPI
  - Agent name: "Echo - E-Commerce Sales Agent"
  - Model: GPT-4
  - Voice: "echo" (female, professional)
  - Copy system prompt from vapi-agent-echo-config.json

- [ ] **11:00** Configure Echo settings
  - Temperature: 0.7
  - Max tokens: 1000
  - Recording: Enabled
  - Filler words: Enabled
  - Interruption: Enabled

- [ ] **11:30** Assign phone number
  - Echo → Settings → Phone Number
  - Select: +1-XXX-ECOM-001
  - Save configuration

### Afternoon (1pm-5pm): Webhook Setup & Testing

- [ ] **13:00** Install Node.js dependencies
  ```bash
  cd /Users/acebless/Documents
  npm install
  ```

- [ ] **13:30** Set up environment variables
  - Copy: `cp .env.example .env`
  - Fill in:
    - SUPABASE_URL ✓ (already have)
    - SUPABASE_KEY (get from Supabase dashboard)
    - CLICKUP_TOKEN (get from ClickUp API settings)
    - CLICKUP_LIST_ECOM (create list first, get ID from ClickUp)

- [ ] **14:00** Create ClickUp lists in workspace 9013677375
  - List 1: "Leads—E-Commerce Tier 1"
  - List 2: "Leads—Technology Tier 1"
  - List 3: "Leads—Beauty & Wellness Tier 1"
  - List 4: "Negotiations—Active Deals"
  - List 5: "Closed Deals—Revenue"
  - Note list IDs in .env

- [ ] **14:30** Start webhook server locally
  ```bash
  npm start
  ```
  - Server should start on port 3000
  - Should print ASCII banner

- [ ] **15:00** Start ngrok tunnel (new terminal)
  ```bash
  ngrok http 3000
  ```
  - Copy public URL (https://xxxx-xx-xxxx-xxxx.ngrok.io)

- [ ] **15:30** Update VAPI webhook URLs
  - Echo agent → Webhooks
  - Call Ended: https://[NGROK_URL]/webhook/call-complete
  - Transcript Ready: https://[NGROK_URL]/webhook/transcript
  - Save

- [ ] **16:00** Test webhook connectivity
  - In VAPI: Send test event to webhook
  - Check server logs for: `[timestamp] POST /webhook/call-complete`
  - Verify 200 response

- [ ] **16:30** Test incoming call
  - Call +1-XXX-ECOM-001 from personal phone
  - Echo should answer with: "Hi, this is Echo from Worldwidebro Holdings..."
  - Stay on line for 60 seconds (test conversation)
  - End call

- [ ] **17:00** Review call outcome
  - Check server logs for webhook event
  - Check Supabase: ai_calls table should have 1 record
  - Check ClickUp: Should have task created if positive outcome
  - Verify transcription captured

---

## TUESDAY, MAY 11

### Morning (9am-12pm): Test Calls & Refinement

- [ ] **09:00** Prepare test calling script
  - Create 5 test scenarios (see PHASE-1-DEPLOYMENT-GUIDE.md)
  - Scenario 1: Multi-channel pain discovery
  - Scenario 2: No pain point
  - Scenario 3: Quantified problem
  - Scenario 4: Cost objection
  - Scenario 5: Demo booking

- [ ] **09:30** Execute test call #1
  - Call +1-XXX-ECOM-001
  - Trigger: "Hi, I sell on Shopify and Amazon"
  - Expected: Echo asks about inventory sync issues
  - Record observations

- [ ] **10:00** Execute test call #2
  - Call +1-XXX-ECOM-001
  - Trigger: "We don't have inventory issues"
  - Expected: Echo pivots to asking for operations contact
  - Record observations

- [ ] **10:30** Execute test calls #3-5
  - Test cost objection handling
  - Test demo booking
  - Test follow-up request
  - Record all observations

- [ ] **11:00** Review all 5 transcripts
  - Check Supabase: ai_calls table should have 5 records
  - Review transcription quality
  - Note any:
    - Unclear responses from Echo
    - Missed opportunities to qualify
    - Awkward transitions
    - Voice/speed issues

- [ ] **11:30** Identify prompt improvements
  - Issue: Echo doesn't listen before pitching?
    - Action: Add "Always ask 2 questions before mentioning solution"
  - Issue: Demo booking sounds forced?
    - Action: Change to "Would it make sense to see this in action?"
  - Issue: Opening is too long?
    - Action: Trim to 15 seconds max

- [ ] **12:00** Deploy updated system prompt
  - Edit: vapi-agent-echo-config.json
  - Update system prompt with improvements
  - Copy new prompt into VAPI dashboard
  - Save

### Afternoon (1pm-5pm): Production Test & Launch Prep

- [ ] **13:00** Prepare 10-prospect test list
  - Source: Personal network, LinkedIn, Facebook
  - Industry: E-commerce (Shopify, Amazon, eBay sellers)
  - Company size: 1-50 people
  - Create spreadsheet with: Name, Phone, Company, Warmth Score (5-7)

- [ ] **13:30** Import test prospects to ClickUp
  - Leads—E-Commerce Tier 1
  - Create 10 tasks (one per prospect)
  - Set custom fields: warmth_score, venture_matched (ECOM-001), notes

- [ ] **14:00** Execute test campaign: 5 calls
  - Call prospects 1-5
  - Dial from Echo agent (+1-XXX-ECOM-001)
  - Each call: introduce, ask about channels, listen, pitch if relevant
  - Log outcome in ClickUp (auto via webhook)

- [ ] **14:30** Monitor webhook success rate
  - Expected: 5 calls → 5 webhook events → 5 ClickUp tasks
  - Check for any 401/403 errors in logs
  - Verify all calls logged to Supabase

- [ ] **15:00** Analyze results from 5 calls
  - Demo booking rate: 0-2 booked (20% target)
  - Warmth score range: should be 3-8
  - Any technical issues?
  - Any script improvements needed?

- [ ] **15:30** Final prompt refinement
  - If needed, make additional changes
  - Re-test with calls 6-10
  - Verify improvements

- [ ] **16:00** Confirm production readiness
  - ✓ Echo agent responding naturally
  - ✓ Webhook capturing all calls
  - ✓ ClickUp tasks auto-creating
  - ✓ Supabase logging all outcomes
  - ✓ Demo booking achievable
  - ✓ No critical errors in logs

- [ ] **16:30** Set up production calling schedule
  - Create calendar: Mon-Thu 9am-5pm
  - Block: 9am, 11am, 1pm, 3pm, 4pm (5 call sessions/day)
  - Starting: Wednesday May 12
  - Target: 20 calls Wed + Thu = 40 calls week 1

- [ ] **17:00** Final documentation
  - Update .env with confirmed values
  - Save ngrok URL for reference (will change if restarted)
  - Document any custom settings from testing
  - Confirm deployment guide is accurate

---

## WEDNESDAY, MAY 12 onwards

### Daily Calling Execution

- [ ] **09:00** Morning sync
  - Review ClickUp: New prospects added?
  - Check Supabase: Any issues overnight?
  - Start webhook server (if local)
  - Start ngrok tunnel (if local)

- [ ] **09:30 - 16:30** Calling blocks
  - Block 1 (9:30-10:30): 5-8 calls
  - Block 2 (11:00-12:00): 5-8 calls
  - Block 3 (13:00-14:00): 5-8 calls
  - Block 4 (14:30-15:30): 5-8 calls
  - Block 5 (15:30-16:30): 5-8 calls
  - Target: 20-40 calls/day

- [ ] **17:00** Evening review
  - Check ClickUp: Tasks created today?
  - Check Supabase: All calls logged?
  - Review warmth scores: Any patterns?
  - Update notes on best-performing prospects
  - Note any demo bookings

- [ ] **Daily** Iterate system prompt
  - If demo booking rate <15%, adjust opening
  - If too many "think about it", add urgency
  - If prospect confusion, simplify pitch
  - Make changes nightly, test next morning

### Success Targets (Week 1)

- [ ] 50+ calls attempted
- [ ] 5-10 demos booked (10-20% rate)
- [ ] 10+ tasks created in ClickUp
- [ ] 0-2 deals in negotiation stage
- [ ] 95%+ webhook success rate
- [ ] No critical errors in logs

---

## NEXT: Phase 2 (Week 2)

Once Echo is proven:
- [ ] Deploy Swift (Tech agent) - May 15
- [ ] Deploy Bella (Beauty agent) - May 15
- [ ] Expand to 480 calls/week
- [ ] Scale revenue to $35K-$100K/week

---

**Status: Ready for deployment Monday May 10, 9am.**

Files prepared:
- ✅ vapi-agent-echo-config.json
- ✅ vapi-agent-swift-config.json
- ✅ vapi-agent-bella-config.json
- ✅ webhook-call-complete.js
- ✅ rag-venture-context.js
- ✅ webhook-server.js
- ✅ package.json
- ✅ .env.example
- ✅ PHASE-1-DEPLOYMENT-GUIDE.md
- ✅ PHASE-1-CHECKLIST.md (this file)
