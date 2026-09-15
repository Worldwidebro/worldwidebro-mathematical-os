# 📊 Lead Management Architecture
**Where Leads Flow: Supabase → ClickUp → Twenty (CRM)**  
**Date:** 2026-09-14  
**Context:** Centralizing lead pipeline across 789 ventures  

---

## EXECUTIVE SUMMARY

**Three-Tier Lead Management System:**

```
Google Maps Scraper
       ↓
Supabase (Raw Lead Storage) ← Single Source of Truth
       ↓
Neo4j (Scoring + Relationships)
       ↓
ClickUp (Workflow/Campaigns)  OR  Twenty (Full CRM)
       ↓
Agent Outreach (Email/Call Skills)
       ↓
Revenue Generation
```

---

## CURRENT STATE (What You Have)

From your credentials audit:

| System | Purpose | Status | Use Case |
|--------|---------|--------|----------|
| **Supabase** | Live venture data | ✅ Active | Core database |
| **ClickUp** | Task management | ✅ Active | Team workflow |
| **Twenty** | Open-source CRM | ❓ Unknown | Not yet adopted |
| **Neo4j** | Knowledge graph | ✅ Active | Relationships + scoring |
| **HubSpot** | Commercial CRM | ❌ Not integrated | Alternative |

---

## OPTION 1: Supabase-Only (Minimum Viable)

### Architecture
```
Google Maps → Supabase (leads table) → Agent Skills → Outreach
```

### Schema
```sql
CREATE TABLE leads (
  id UUID PRIMARY KEY,
  venture_id VARCHAR,
  name VARCHAR,
  phone VARCHAR,
  email VARCHAR,
  website VARCHAR,
  rating FLOAT,
  review_count INT,
  address VARCHAR,
  source VARCHAR DEFAULT 'google_maps',
  status VARCHAR DEFAULT 'new',  -- new, contacted, qualified, won, lost
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  scored_at TIMESTAMP,
  score FLOAT,  -- 0-100 lead quality score
  tags JSONB,  -- ["hot", "followup_ready", etc]
  metadata JSONB  -- custom fields per venture
);

CREATE TABLE lead_interactions (
  id UUID PRIMARY KEY,
  lead_id UUID REFERENCES leads(id),
  venture_id VARCHAR,
  interaction_type VARCHAR,  -- email_sent, call_made, reply_received, converted
  timestamp TIMESTAMP,
  notes TEXT,
  agent_id VARCHAR  -- which agent took action
);
```

### Pros & Cons

✅ **Pros:**
- Single database for all lead data
- Already have Supabase running
- Easy integration with skills/agents
- Live data (real-time updates)
- Cost-effective

❌ **Cons:**
- No built-in lead scoring UI
- No native sales pipeline visualization
- Team can't easily see "who's calling what"
- Manual workflow management

### Best For
Small ventures (1-5 team members), or when you want to own all the data.

---

## OPTION 2: Supabase + ClickUp (Recommended)

### Architecture
```
Google Maps → Supabase (raw leads) → ClickUp (campaigns + workflow)
                     ↓
                  Neo4j (scoring)
                     ↓
              Agent Outreach Skills
```

### Data Flow

**Phase 1: Lead Generation**
```typescript
// Skill: google-maps-scraper
const leads = await skills.invoke("operations/scrape-google-maps", {
  searchQuery: "medical facilities in Charlotte",
  location: "Charlotte, NC"
});

// Write to Supabase (source of truth)
await supabase.from("leads").insert(leads.map(lead => ({
  venture_id: "LT-005",
  name: lead.name,
  phone: lead.phone,
  email: lead.email,
  website: lead.website,
  rating: lead.rating,
  status: "new",
  created_at: new Date()
})));
```

**Phase 2: Scoring (Neo4j)**
```typescript
// Skill: score-leads
const scoredLeads = await skills.invoke("analytics/score-leads", {
  leads: leads,
  criteria: {
    minRating: 4.0,
    minReviewCount: 10,
    keywordMatches: ["medical", "healthcare", "delivery"]
  }
});

// Update Supabase with scores
await supabase.from("leads")
  .update({ score: 85, scored_at: new Date() })
  .eq("id", lead.id);

// Also log to Neo4j for relationship analysis
await neo4j.session().run(
  `CREATE (l:Lead {id: $id, score: $score, ventureId: $vid}) SET l.scoredAt = timestamp()`,
  { id: lead.id, score: 85, vid: "LT-005" }
);
```

**Phase 3: Campaign Management (ClickUp)**

ClickUp structure per venture:
```
Workspace: LT-005 Medical Courier
├─ List: Lead Generation (Sep 14)
│  ├─ Task: "Generate leads - medical facilities Charlotte" (DONE)
│  └─ Task: "Score leads - filter > 4.0 rating" (DONE)
├─ List: Outreach Campaign
│  ├─ Task: "Call delivery directors (50 leads, score > 85)"
│  ├─ Task: "Email facility managers (30 leads, score > 75)"
│  └─ Task: "Follow-up sequences (pending responses)"
└─ List: Won Deals
   ├─ Task: "Signed with Carolinas Medical Center"
   └─ Task: "Onboarded 3 ambulatory surgical centers"
```

**ClickUp Automation (via skill):**

```typescript
// Skill: create-clickup-campaign
export const createClickUpCampaign = skill({
  name: "operations/create-clickup-campaign",
  execute: async (input, context) => {
    const { leads, ventureId, campaignName } = input;
    
    // Create ClickUp list
    const list = await context.clickup.spaces[ventureId].createList({
      name: campaignName,
      due_date: new Date().getTime() + 7*24*60*60*1000  // 1 week from now
    });
    
    // Create one task per outreach bundle
    const hotLeads = leads.filter(l => l.score > 85);
    const warmLeads = leads.filter(l => l.score > 75 && l.score <= 85);
    
    if (hotLeads.length > 0) {
      await context.clickup.lists[list.id].createTask({
        name: `🔥 HOT: Call ${hotLeads.length} prospects (score > 85)`,
        description: hotLeads.map(l => `${l.name} - ${l.phone}`).join("\n"),
        assignee: context.ventureLeadId,  // Sales lead for LT-005
        priority: "urgent"
      });
    }
    
    if (warmLeads.length > 0) {
      await context.clickup.lists[list.id].createTask({
        name: `📧 WARM: Email ${warmLeads.length} prospects (score 75-85)`,
        description: warmLeads.map(l => `${l.name} - ${l.email}`).join("\n"),
        assignee: context.ventureLeadId,
        priority: "high"
      });
    }
    
    return { campaignId: list.id, tasksCreated: 2 };
  }
});
```

**Phase 4: Outreach (Skills + Automation)**

```typescript
// Skill: send-outreach-sequence
export const sendOutreachSequence = skill({
  name: "operations/send-outreach",
  execute: async (input, context) => {
    const { ventureId, leads } = input;
    
    for (const lead of leads) {
      // Send email
      await skills.invoke("communications/send-email", {
        to: lead.email,
        template: "lead_discovery",
        variables: { companyName: lead.name }
      });
      
      // Log in Supabase
      await supabase.from("lead_interactions").insert({
        lead_id: lead.id,
        venture_id: ventureId,
        interaction_type: "email_sent",
        timestamp: new Date()
      });
      
      // Update ClickUp task
      await clickup.updateTask(input.clickupTaskId, {
        status: "in progress"
      });
    }
  }
});
```

### ClickUp Schema (per Venture)

**Custom Fields in ClickUp:**
- Lead Score (0-100)
- Segment (hot/warm/cold)
- Last Interaction Date
- Response Rate
- Expected Revenue

### Pros & Cons

✅ **Pros:**
- Supabase = raw data (source of truth)
- ClickUp = operational workflow (teams see it)
- Neo4j = intelligence layer (scoring)
- Already have ClickUp API key in Bitwarden
- Team visibility + accountability
- Easy to track "who's doing what"

❌ **Cons:**
- Requires ClickUp task automation setup
- Supabase data NOT reflected live in ClickUp (must sync via skills)
- ClickUp not ideal for high-volume lead lists (1000+ per week)

### Best For
**Most ventures (OPS-001, LT-005, RE-001, CON-001)** — team-based execution with accountability.

---

## OPTION 3: Supabase + Twenty (Full CRM)

### Architecture
```
Google Maps → Supabase → Twenty CRM (full pipeline)
                     ↓
                  Neo4j (scoring)
                     ↓
              Agent Outreach Skills
```

### Why Twenty?

**Twenty** is an open-source CRM designed for this:
- Lead scoring + pipeline
- Company/Contact relationships
- Deal tracking
- Activity logging
- Custom workflows
- Self-hosted (no SaaS cost)
- PostgreSQL-based (can sync with Supabase)

### Setup

```typescript
// Skill: sync-leads-to-twenty
export const syncLeadsToTwenty = skill({
  name: "crm/sync-leads-to-twenty",
  execute: async (input, context) => {
    const { leads, ventureId } = input;
    
    for (const lead of leads) {
      // Create company in Twenty
      const company = await context.twenty.api.createCompany({
        name: lead.name,
        domainName: extractDomain(lead.website),
        linkedinLink: lead.linkedinUrl
      });
      
      // Create contact
      const contact = await context.twenty.api.createContact({
        firstName: extractFirstName(lead.name),
        lastName: extractLastName(lead.name),
        email: lead.email,
        phone: lead.phone,
        company: company.id,
        stage: "qualified"  // Pipeline stage
      });
      
      // Create opportunity (deal)
      const opportunity = await context.twenty.api.createOpportunity({
        name: `${lead.name} - Partnership`,
        company: company.id,
        amount: venture.avgDealSize,
        probability: lead.score / 100,  // Convert to probability
        stage: "prospecting"
      });
      
      return { companyId: company.id, contactId: contact.id, opportunityId: opportunity.id };
    }
  }
});
```

### Twenty Schema

**Company Object:**
- Name
- Website
- Phone
- Industry
- Size
- Pitch (custom notes)

**Contact Object:**
- Name
- Email
- Phone
- Role/Title
- Company
- Stage (new, contacted, qualified, etc.)

**Opportunity Object:**
- Company + Contact linked
- Deal amount
- Stage (prospecting → negotiation → closed)
- Probability (auto-calculated from lead score)
- Expected close date

### Pros & Cons

✅ **Pros:**
- Full CRM features (scoring, pipeline, deals)
- Open-source (self-hosted)
- PostgreSQL backend (can sync with Supabase)
- Better for high-volume leads
- Professional pipeline management
- Activity history + reporting

❌ **Cons:**
- Requires hosting + maintenance
- Steeper learning curve
- Overkill if you don't need full CRM
- Another system to manage

### Best For
**Large-scale operation (100+ leads/week) or if you want a true CRM** — better for sales teams who live in CRM.

---

## RECOMMENDATION BY VENTURE TYPE

| Venture | Team Size | Lead Volume | Recommended | Reason |
|---------|-----------|-------------|-------------|--------|
| **OPS-001** (Staffing) | 2-3 | 100+/week | Supabase + ClickUp | High velocity, team coordination |
| **LT-005** (Medical) | 2-3 | 50+/week | Supabase + ClickUp | Partnership-focused, good for ClickUp tasks |
| **RE-001** (Real Estate) | 3-5 | 50+/week | Supabase + Twenty | Deal pipeline critical, needs CRM |
| **CALLCENTER** | 5+ | 200+/week | Supabase + Twenty | High volume, needs pipeline mgmt |
| **CON-001** (Construction) | 2-3 | 75+/week | Supabase + ClickUp | Project-based, task-oriented |

---

## ARCHITECTURE RECOMMENDATION: HYBRID (Best of Both)

### For ALL Ventures:

```
┌─────────────────────────────────────────────────┐
│       Google Maps Scraper (Skill)               │
└──────────────────┬──────────────────────────────┘
                   ↓
        ┌──────────────────────┐
        │ Supabase (Raw Leads) │ ← Single source of truth
        │ leads table          │
        │ lead_interactions    │
        └──────────────────────┘
                   ↓
        ┌──────────────────────┐
        │ Neo4j Scoring        │
        │ (Relationships +     │
        │  ML scoring logic)   │
        └──────────────────────┘
                   ↓
    ┌──────────────┴──────────────┐
    ↓                             ↓
┌─────────────┐          ┌─────────────────┐
│   ClickUp   │          │   Twenty CRM    │
│ (Workflow)  │          │ (Full Pipeline) │
│ - Tasks     │          │ - Companies     │
│ - Campaigns │          │ - Contacts      │
│ - Team view │          │ - Opportunities │
└─────────────┘          │ - Deals         │
                         └─────────────────┘
    ↓ (Team action)          ↓ (Sales pipeline)
┌─────────────────────────────────────────────┐
│    Agent Outreach Skills                    │
│ - Send Email                                │
│ - Make Call                                 │
│ - Log Interaction                           │
└──────────────────┬──────────────────────────┘
                   ↓
           ┌───────────────┐
           │ Revenue!      │
           └───────────────┘
```

### Data Sync Strategy

**Supabase (master) → ClickUp (team view) → Twenty (CRM)**

```typescript
// Skill: sync-leads-everywhere
export const syncLeadsEverywhere = skill({
  name: "operations/sync-leads-everywhere",
  execute: async (input, context) => {
    const { leads, ventureId } = input;
    const venture = await context.supabase
      .from("ventures")
      .select("*")
      .eq("id", ventureId)
      .single();
    
    // 1. Store in Supabase (source of truth)
    const supabaseLeads = await context.supabase
      .from("leads")
      .insert(leads);
    
    // 2. If venture uses ClickUp, sync there
    if (venture.has_clickup) {
      await skills.invoke("operations/create-clickup-campaign", {
        leads: leads,
        ventureId: ventureId
      });
    }
    
    // 3. If venture uses Twenty, sync there
    if (venture.has_twenty) {
      await skills.invoke("crm/sync-leads-to-twenty", {
        leads: leads,
        ventureId: ventureId
      });
    }
    
    // 4. Enrich in Neo4j
    await skills.invoke("analytics/score-leads", {
      leads: leads
    });
    
    return {
      supabaseInserted: supabaseLeads.length,
      clickupSynced: venture.has_clickup,
      twentySynced: venture.has_twenty,
      scored: true
    };
  }
});
```

---

## IMPLEMENTATION TIMELINE

### Week 1: Supabase Foundation
- [ ] Create `leads` table in Supabase
- [ ] Create `lead_interactions` table
- [ ] Deploy Google Maps scraper skill
- [ ] Test with OPS-001 (100 leads)

### Week 2: ClickUp Integration
- [ ] Connect ClickUp API
- [ ] Create sync skill (Supabase → ClickUp)
- [ ] Test workflows with team
- [ ] Deploy to 3 ventures

### Week 3: Twenty CRM (Optional)
- [ ] Deploy Twenty instance (Docker)
- [ ] Create sync skill (Supabase → Twenty)
- [ ] Configure pipeline stages
- [ ] Test with RE-001 (deal-heavy)

### Week 4: Full Automation
- [ ] All 4 Tier-0 ventures live
- [ ] Leads flowing through entire pipeline
- [ ] Revenue tracking via Neo4j
- [ ] Scale to portfolio

---

## STORAGE DECISION

### PRIMARY (Must Have):
**Supabase** — Raw lead storage, source of truth

### SECONDARY (Choose One or Both):

**ClickUp** if:
- Team-based execution
- Task/workflow focused
- Medium volume (50-200/week)
- Need accountability + visibility

**Twenty** if:
- Sales pipeline critical
- High volume (200+/week)
- Need full CRM features
- Deal tracking important

---

## ANSWER TO YOUR QUESTION

**"Where should leads go?"**

1. **First:** Supabase (always, raw data)
2. **Then:** ClickUp IF your venture uses task management
3. **Or:** Twenty IF your venture does deal/pipeline management
4. **Both:** Supabase + ClickUp + Twenty for OPS-001 and RE-001

**Recommendation:** Start with **Supabase + ClickUp** for all 4 Tier-0 ventures. Add Twenty later if you need full CRM pipeline.

---

**Next Step:** Confirm which ventures use ClickUp, then deploy the sync skills.
