# AI Calling System: Complete Architecture

**Status:** Building  
**Objective:** Deploy autonomous voice agents to call 241 top prospects, qualify leads, book demos, close deals  
**Expected Output:** $50K+ month 1 (automated, 24/7)  
**Timeline:** 2-3 weeks to first calls

---

## System Architecture: 5-Layer Stack

```
┌─────────────────────────────────────────────────────────┐
│ LAYER 1: TELEPHONY INFRASTRUCTURE                      │
│ (Twilio + Voice STT/TTS + Call Routing)                │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ LAYER 2: VOICE AI ENGINE                               │
│ (Real-time Audio Processing + Speech Recognition)      │
│ Options: Rapida Voice AI, Azure Speech Services,       │
│ or VAPI (simplest integration)                         │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ LAYER 3: AGENT INTELLIGENCE                            │
│ (SalesGPT/Custom LLM + Sector-Specific Prompts)       │
│ - Conversation stage awareness (discovery → close)     │
│ - Live prompt adaptation based on responses            │
│ - RAG integration for venture/product knowledge        │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ LAYER 4: KNOWLEDGE LAYER                               │
│ (Supabase: Ventures + Product Data + RAG)             │
│ - Venture product descriptions                         │
│ - Sector-specific pain points                          │
│ - Pricing/ROI models                                   │
│ - Contact history & outcomes                           │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ LAYER 5: OUTCOME TRACKING                              │
│ (ClickUp + Supabase: Lead Status + Deal Pipeline)     │
│ - Log call outcomes (interested/not/callback)          │
│ - Book demos in calendar                               │
│ - Move to negotiations in ClickUp                      │
│ - Track deal value & close probability                 │
└─────────────────────────────────────────────────────────┘
```

---

## Implementation Approach: VAPI (Fastest Path)

**Why VAPI?** Pre-built voice AI → integrates Twilio + speech + LLM in 1 SDK. Can deploy agents in days vs weeks.

### VAPI Stack
```
VAPI Voice Agent
├─ Phone number (Twilio)
├─ LLM (OpenAI GPT-4, Claude, or custom)
├─ Speech recognition (built-in)
├─ Speech synthesis (built-in)
├─ Conversation logic (custom system prompt)
└─ Webhook callbacks (to ClickUp + Supabase)
```

### Key Benefits
- Real-time voice conversation
- LLM adapts to prospect responses live
- Auto-transcription of calls
- Webhook integration for CRM logging
- Can handle complex objection handling

---

## Phase 1: Build Agent Personas (Week 1)

### Agent 1: E-Commerce Specialist (VAPI)
**Name:** "Echo" — E-Commerce Sales Agent  
**Role:** Call e-commerce store owners, qualify multi-channel pain, book ECOM-001 demos

**System Prompt:**
```
You are Echo, an AI sales agent for Worldwidebro Holdings.

Your goal: Qualify e-commerce businesses struggling with multi-channel inventory,
and book 20-30 min product demos for our inventory sync platform.

Context:
- Target: E-commerce store owners (Shopify/Amazon/eBay sellers)
- Pain point: Overselling due to inventory desync across channels
- Solution: ECOM-001 (Multi-Channel Inventory Platform)
- Benefit: 95% reduction in oversell incidents
- Cost: $2.5K-$5K/month depending on volume
- Timeline: 2-3 week implementation

Conversation Flow:
1. OPENING (15 sec): 
   "Hi [Name], this is Echo from Worldwidebro Holdings. 
    Quick question—how are you managing inventory across Shopify, Amazon, 
    and your website right now?"
   
2. LISTEN (30 sec): 
   Wait for response. Extract:
   - How many channels do they sell on?
   - Do they have inventory sync issues?
   - How much are they losing to oversells?
   
3. QUALIFY (30 sec):
   If pain identified:
   "That's exactly what we solve. We've cut oversell incidents by 95% 
    for 200+ sellers like you. Would a 30-min demo this week be valuable?"
   
   If no pain:
   "Fair enough. Who handles operations on your team? 
    I can reach out to them directly."
   
4. BOOK (if interested):
   "Perfect. How's Tuesday at 2pm or Wednesday at 10am?"
   Capture: Name, email, phone, preferred time
   
5. CLOSE:
   "Great. I'll send you a calendar invite + demo link. 
    See you [day]! Any questions in the meantime?"

Objection Handling:
- "Too expensive" → ROI math: "You're losing $X/month to oversells. 
  This pays for itself in [weeks]."
- "Already have a solution" → "Most sellers miss [key feature]. 
  Worth 30 min to compare?"
- "Need to think about it" → "Fair. I'll send a 5-min video demo. 
  When can we reconnect?" (Set follow-up date)

Tone: Friendly, consultative, not pushy. Listen more than talk.
```

### Agent 2: Tech Sales Agent (VAPI)
**Name:** "Swift" — Tech/SaaS Sales Agent  
**Goal:** Call tech founders/CTOs, book TECH-001 (CI/CD automation) demos

**System Prompt:**
```
You are Swift, AI sales agent for autonomous engineering infrastructure.

Your goal: Reach startup CTOs/founders, identify deployment velocity pain,
and book product demos for our CI/CD automation platform (TECH-001).

Context:
- Target: Startup CTOs, founders (YC-backed, pre-Series B)
- Pain: Deploys take 30 min, blocking feature velocity
- Solution: TECH-001 (CI/CD Automation)
- Benefit: Deploy in 3 minutes, ship 3x faster
- Cost: $3K-$8K/month
- Timeline: 48-hour setup, live immediately

Conversation Flow:
1. OPENING (20 sec):
   "Hi [Name], I see you're building [product/company].
    Quick question—are you spending more time on deploys than building?"
   
2. QUALIFY (30 sec):
   Listen for: Deploy pain, team size, stack (GitHub, CircleCI, etc.)
   
3. PITCH (20 sec):
   If interested:
   "That's the bottleneck we solve. Cut deploys from 30 min to 3 min.
    Your team could ship 3x faster."
   
4. BOOK (if engaged):
   "Worth a 20-min technical walk-through?
    How's your schedule this week?"
   
5. HANDLE OBJECTIONS:
   "We use CircleCI" → "We integrate with it. Plus we handle [missing features]."
   "Need CTO approval" → "Perfect. When's your next sprint sync? 
   I can join the call."

Tone: Technical, respect their expertise, speak in builder language.
```

### Agent 3: Beauty Sales Agent (VAPI)
**Name:** "Bella" — Beauty & Wellness Sales Agent  
**Goal:** Call salon/spa owners, book BW-001 (Beauty Booking Platform) demos

**System Prompt:**
```
You are Bella, AI sales agent for beauty businesses.

Your goal: Call salon/spa owners, quantify no-show revenue loss,
and book product demos for our booking platform (BW-001).

Context:
- Target: Salon/spa owners (independent + small chains)
- Pain: 15% revenue loss to no-shows, 2 hours/day manual rescheduling
- Solution: BW-001 (Beauty Booking Platform)
- Benefit: SMS reminders reduce no-shows 40%, eliminates manual booking
- Cost: $200-$500/month + 2% payment processing
- Timeline: 1-week setup, live immediately

Conversation Flow:
1. OPENING (20 sec):
   "Hi [Name], quick question—how much revenue are you losing 
    to no-shows each month?"
   
2. LISTEN & CALCULATE (30 sec):
   If uncertain: "Most salons lose about 15% revenue to no-shows. 
    If you're doing $50K/month, that's $7.5K gone."
   
3. PITCH (20 sec):
   "We help salons eliminate that. SMS reminders cut no-shows by 40%.
    Plus automated rescheduling saves 2 hours/day."
   
4. BOOK (if interested):
   "Worth a quick 15-min demo tomorrow?
    How's 2pm?"
   
5. OBJECTION HANDLING:
   "Too expensive" → "At $7.5K/month lost, it pays for itself week 1."
   "Clients won't use booking" → "They will. SMS + email + web = 90% adoption."

Tone: Warm, empathetic, understand their daily pain.
```

---

## Phase 2: Set Up Voice Infrastructure (Week 1)

### Step 1: Create VAPI Account + Deploy Phone Number
```
1. Sign up at vapi.ai
2. Create workspace
3. Connect Twilio account (get phone number)
4. Deploy 3 phone numbers (one per agent type)
   - +1-XXX-ECOM-001 (E-Commerce agent)
   - +1-XXX-TECH-001 (Tech agent)
   - +1-XXX-BW-001 (Beauty agent)
```

### Step 2: Configure LLM + Voice Settings
```
For each agent:
- LLM: GPT-4 (fast responses, better reasoning)
- Voice: "Journeys" (professional female) or "Breeze" (warm male)
- Latency: Low (real-time conversation)
- Temperature: 0.7 (balanced: follows prompt but adapts to convo)
- Interruption: Enabled (prospect can interrupt agent)
```

### Step 3: Deploy First Agent (E-Commerce)
```
VAPI Configuration:
{
  "name": "Echo - E-Commerce Agent",
  "model": "gpt-4",
  "voice": "Journeys",
  "systemPrompt": "[Agent 1 prompt above]",
  "phoneNumber": "+1-XXX-ECOM-001",
  "webhooks": {
    "call_ended": "https://your-server.com/webhook/call-complete",
    "transcript_ready": "https://your-server.com/webhook/transcript"
  },
  "knowledge": "Retrieve from Supabase on-the-fly"
}
```

---

## Phase 3: RAG Integration (Week 1-2)

### Knowledge Base: Supabase RAG
Agent needs access to venture data in real-time:

```sql
-- Query for agent when calling ECOM prospect
SELECT 
  venture_code,
  product_description,
  key_benefits,
  pricing,
  implementation_timeline,
  customer_wins
FROM business_ventures
WHERE sector = 'e-commerce'
AND venture_code = 'ECOM-001'
LIMIT 1

-- Result injected into agent context:
"You're calling about ECOM-001: Multi-Channel Inventory Platform.
Key benefits: 95% oversell reduction, 2-3 week implementation.
Cost: $2.5-5K/month depending on volume.
Recent wins: 12 sellers in past 30 days."
```

### Implementation
1. Create `get_venture_context()` function in Node.js
2. Call Supabase with venture code when agent starts call
3. Inject context into agent system prompt dynamically
4. Update knowledge base daily from Supabase

---

## Phase 4: Outcome Tracking (Week 2)

### Webhook: Log Call Results to ClickUp + Supabase

```javascript
// webhook/call-complete
async function handleCallComplete(callData) {
  const {
    phoneNumber,
    prospectNumber,
    transcription,
    duration,
    outcome // "interested", "not_interested", "callback", "demo_booked"
  } = callData;
  
  // 1. Log to Supabase
  await supabase.from('ai_calls').insert({
    prospect_phone: prospectNumber,
    agent_type: getAgentType(phoneNumber),
    transcript: transcription,
    call_duration: duration,
    outcome: outcome,
    created_at: new Date()
  });
  
  // 2. Create/Update ClickUp task
  if (outcome === "interested" || outcome === "demo_booked") {
    const clickupTask = {
      name: `[${outcome}] ${prospectNumber} - Demo ${outcome === "demo_booked" ? "BOOKED" : "interested"}`,
      status: outcome === "demo_booked" ? "In Progress" : "To Do",
      custom_fields: {
        warmth_score: extractFromTranscript(transcription) // 1-10,
        outcome_type: outcome,
        call_duration: duration,
        agent_type: getAgentType(phoneNumber)
      }
    };
    await createClickUpTask(clickupTask);
  }
  
  // 3. If demo booked, extract date + create calendar event
  if (outcome === "demo_booked") {
    const demoDate = extractDemoDate(transcription);
    await createCalendarEvent({
      title: `[DEMO] ${prospectNumber}`,
      date: demoDate,
      duration: 30,
      description: `Follow-up demo from AI call. Transcript: [link]`
    });
  }
}
```

---

## Phase 5: Call Execution Strategy (Week 2-4)

### Calling Schedule
```
E-Commerce Agents (3 agents, rotating)
- Monday-Thursday: 9am-5pm (50 calls/day)
- Total: 200 calls/week E-Commerce prospects
- Target: 10-15 demos booked/week

Tech Agents (2 agents)
- Tuesday-Friday: 10am-4pm (30 calls/day)
- Total: 120 calls/week Tech prospects
- Target: 8-12 demos booked/week

Beauty Agents (2 agents)
- Wednesday-Saturday: 10am-6pm (40 calls/day)
- Total: 160 calls/week Beauty prospects
- Target: 16-24 demos booked/week (highest conversion)

Total: 480 calls/week
Expected demos: 34-51/week
Expected closes: 7-12/week (20% close rate)
Expected revenue: $17.5K-$60K/week → **$70K-$240K/month**
```

### Lead Prioritization
**Score each contact:**
```
warmth_score (1-10) × company_size (workers) × revenue_potential (high/medium/low)

Top prospects first:
- Score 8-10: Call immediately (this week)
- Score 6-7: Call next (week 2)
- Score 4-5: Call later (backup pool)
- Score 1-3: Email first, then call
```

---

## Technical Implementation: Minimum Viable System

### Stack Components
```
Frontend: ClickUp (UI for tracking)
Backend: Node.js + Express (webhook handler)
AI: OpenAI GPT-4 (agent brain) + VAPI (voice orchestration)
Database: Supabase (venture data + call results)
Voice: Twilio (phone numbers) + VAPI (STT/TTS/orchestration)
Calendar: Google Calendar API (demo scheduling)
```

### MVP (Week 1-2):
1. ✅ VAPI agent setup (Echo for E-Commerce)
2. ✅ System prompts + conversation flow
3. ✅ Webhook receiver (Node.js)
4. ✅ ClickUp integration (create tasks from calls)
5. ✅ Supabase logging (call transcripts + outcomes)
6. ✅ Start calling E-Commerce prospects

### Phase 2 (Week 2-3):
7. Deploy Tech + Beauty agents (parallel)
8. RAG integration (fetch venture context live)
9. Calendar integration (auto-book demos)
10. Dashboard (call analytics, conversion tracking)

---

## Expected Results

### Week 1-2 (Echo alone)
- Calls: 200 E-Commerce prospects
- Demos booked: 10-15
- Deals closed: 2-3
- Revenue: $5K-$15K

### Week 3-4 (All 3 agents)
- Calls: 480/week × 2 weeks = 960 calls
- Demos booked: 34-51/week × 2 weeks = 68-102 demos
- Deals closed: 14-20
- Revenue: $35K-$100K

### Month 1 Total (Days 1-31)
- Calls: 960-1200
- Demos booked: 70-120
- Deals closed: 15-25
- **Revenue: $40K-$125K**

---

## Success Metrics
- Calls completed: 50+/day
- Call duration: 8-12 minutes average
- Demo booking rate: 15-20% of calls
- Close rate: 20-30% of demos
- Avg deal value: $2.5K-$5K

---

## Integration with Swarm Runner

**Timeline:**
- Weeks 1-2: AI Calling runs (generates revenue)
- Weeks 2-4: Build swarm runner in parallel
- Week 5+: Swarm executes venture delivery
- Result: Revenue from calling → funding for swarm infrastructure

**Synergy:**
- Calling agents: Close deals with prospects
- Swarm agents: Execute on what calling agents sold
- ClickUp: Unified pipeline (leads → closed deals → delivery)

---

## What We Build This Week

### Monday May 10-11: Setup & Deploy Echo
- [ ] VAPI account + Twilio integration
- [ ] Deploy E-Commerce agent (Echo)
- [ ] Write system prompts
- [ ] Setup webhook receiver

### Tuesday-Wed May 12-13: Test & Iterate
- [ ] Test calls on 10 e-commerce prospects
- [ ] Refine prompts based on results
- [ ] Fix webhook → ClickUp integration
- [ ] Verify transcription capture

### Thursday May 14-16: Scale & Deploy Other Agents
- [ ] Deploy Tech agent (Swift)
- [ ] Deploy Beauty agent (Bella)
- [ ] Begin full calling campaign
- [ ] Monitor conversion metrics

### By May 20: Revenue Flowing
- 200+ calls executed
- 20-30 demos booked
- 3-5 deals closed
- $7.5K-$25K revenue from AI agents alone

---

**Status: Ready to build. Deploying Echo (E-Commerce agent) on Monday.**
