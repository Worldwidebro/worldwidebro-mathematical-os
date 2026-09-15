# 🗺️ Google Maps Scraper + Skills Framework
**Revenue Loop Integration for 789 Ventures**  
**Date:** 2026-09-14  
**Context:** Automating lead generation across company portfolio  

---

## THE SYNERGY

### Google Maps Scraper Kit
- **What:** Local tool extracts business listings from Google Maps
- **Output:** Leads (name, phone, email, website, rating, reviews)
- **Use Case:** Lead generation for Week 1 revenue ventures

### Google Skills Framework
- **What:** Standardizes agentic capabilities as reusable, composable skills
- **Benefit:** Wrap scraper as a skill → Available to ALL 789 ventures

### **Combined = Revenue Loop Automation**

```
┌──────────────────────────────┐
│   Venture Needs Leads        │
│   (OPS-001, LT-005, RE-001)  │
└──────────────┬───────────────┘
               ↓
      ┌─────────────────────┐
      │ Skills Discovery    │
      │ "Find leads"        │
      └────────┬────────────┘
               ↓
      ┌─────────────────────┐
      │ Google Maps Skill   │
      │ (Scraper Kit)       │
      └────────┬────────────┘
               ↓
      ┌─────────────────────┐
      │ Lead List Ready     │
      │ 100+ prospects      │
      └────────┬────────────┘
               ↓
      ┌─────────────────────┐
      │ Auto-Outreach       │
      │ (Email/Call Skill)  │
      └────────┬────────────┘
               ↓
      ┌─────────────────────┐
      │ Revenue Generated   │
      │ $2-5K/week          │
      └─────────────────────┘
```

---

## HOW IT MAPS TO COMPANY BRAIN

### Revenue Loop #1: Lead Generation (REV-LOOP-001)

**Currently:** Manual search + spreadsheets  
**With Skills + Scraper:** Fully autonomous

```typescript
// Define skill ONCE
export const generateLeads = skill({
  name: "operations/generate-leads",
  input: z.object({
    searchQuery: z.string(),        // "coffee shops in Austin"
    location: z.string(),
    category: z.string(),
    maxResults: z.number().default(100)
  }),
  output: z.object({
    leads: z.array(z.object({
      name: z.string(),
      phone: z.string(),
      email: z.string(),
      website: z.string(),
      rating: z.number(),
      reviewCount: z.number(),
      address: z.string()
    })),
    timestamp: z.date(),
    sourceQuality: z.enum(["verified", "unverified"])
  }),
  execute: async (input, context) => {
    // Use Google Maps Scraper Kit via Docker
    const job = await context.googleMaps.createJob({
      query: input.searchQuery,
      location: input.location,
      limit: input.maxResults
    });
    
    // Poll for results
    const results = await context.googleMaps.pollJob(job.id);
    
    // Format + store in Supabase
    await context.supabase
      .from("leads")
      .insert(results.leads.map(lead => ({
        venture_id: context.ventureId,
        ...lead,
        created_at: new Date()
      })));
    
    return results;
  }
});

// Use in ANY venture
// OPS-001 (staffing): "construction companies in Charlotte"
// RE-001 (real estate): "real estate agents in Miami"
// CALLCENTER: "customer service contractors in US"
```

**Week 1 Revenue Impact:**
- OPS-001 generates 100 contractor leads → $2.5K placement fees
- RE-001 generates 50 agent leads → $5-10K pipeline
- CALLCENTER generates 200 call center ops → $10K+ opportunity

---

## DETAILED ARCHITECTURE

### Layer 1: Data Acquisition Skill

```typescript
// Wraps google-maps-scraper-kit in skill interface
skills/operations/google-maps-lead-generation.ts

export const googleMapsLeadScraper = skill({
  name: "operations/scrape-google-maps",
  description: "Extract business leads from Google Maps for a location/category",
  
  // Pre-built configurations per sector
  configs: {
    staffing: { searchQuery: "staffing agencies", minRating: 3.5 },
    real_estate: { searchQuery: "real estate brokers", minRating: 4.0 },
    construction: { searchQuery: "contractors", minRating: 3.0 }
  },
  
  rateLimit: {
    maxJobsPerDay: 10,      // ← Prevents IP blocking
    minDelayBetweenJobs: 30, // seconds
    rotateProxy: true
  },
  
  execute: async (input, context) => {
    // Docker container runs locally at 100.87.214.70:8080
    const response = await fetch("http://100.87.214.70:8080/api/jobs", {
      method: "POST",
      body: JSON.stringify({
        query: input.searchQuery,
        location: input.location,
        results_limit: input.limit
      })
    });
    
    const job = await response.json();
    
    // Poll until complete (5-15 min)
    let results = null;
    let attempts = 0;
    while (!results && attempts < 30) {
      await new Promise(r => setTimeout(r, 10000)); // Wait 10s
      const statusResponse = await fetch(`http://100.87.214.70:8080/api/jobs/${job.id}`);
      const status = await statusResponse.json();
      
      if (status.status === "completed") {
        results = status.results;
      }
      attempts++;
    }
    
    return { leads: results, jobId: job.id };
  }
});
```

### Layer 2: Skill Composition (Multi-Step Lead Pipeline)

```typescript
// Compose multiple skills into revenue workflow
export const automatedLeadGeneration = async (ventureId, sector) => {
  // Step 1: Generate leads
  const leads = await skills.invoke("operations/scrape-google-maps", {
    searchQuery: sectorConfigs[sector].query,
    location: sectorConfigs[sector].location,
    limit: 100
  });
  
  // Step 2: Enrich leads (add emails via Hunter.io if available)
  const enrichedLeads = await skills.invoke("integrations/enrich-leads", {
    leads: leads,
    dataFields: ["email", "linkedin_url", "employee_count"]
  });
  
  // Step 3: Score leads (which are most likely to convert)
  const scoredLeads = await skills.invoke("analytics/score-leads", {
    leads: enrichedLeads,
    criteria: sectorConfigs[sector].scoringCriteria
  });
  
  // Step 4: Generate outreach (personalized emails/calls)
  const campaigns = await skills.invoke("operations/generate-outreach", {
    leads: scoredLeads,
    ventureId: ventureId,
    templates: ["discovery_call", "partnership_inquiry"]
  });
  
  // Step 5: Log to Neo4j for learning
  await context.neo4j.session().run(
    `CREATE (c:Campaign) SET c.leads = $count, c.ventureId = $vid, c.createdAt = timestamp()`,
    { count: leads.length, vid: ventureId }
  );
  
  return { leadsGenerated: leads.length, campaignsCreated: campaigns.length };
};
```

### Layer 3: Multi-Venture Deployment

```typescript
// Deploy to 789 ventures at once
async function deployLeadGenerationAcrossPortfolio() {
  const ventures = await supabase
    .from("ventures")
    .select("id, sector, status")
    .eq("status", "operating");
  
  const results = [];
  for (const venture of ventures) {
    try {
      const outcome = await automatedLeadGeneration(venture.id, venture.sector);
      results.push({
        ventureId: venture.id,
        success: true,
        leadsGenerated: outcome.leadsGenerated
      });
    } catch (error) {
      results.push({
        ventureId: venture.id,
        success: false,
        error: error.message
      });
    }
  }
  
  return results;
}

// One-time deploy → Benefits all 789 ventures automatically
// New ventures inherit the skill immediately
```

---

## RATE LIMITING + IP BLOCKING STRATEGY

**Risk:** Google Maps blocks high-volume scraping

**Solution with Skills Framework:**

```typescript
// Skill integrates rate limiting + proxy rotation
export const rateLimitedMapsScraper = skill({
  name: "operations/scrape-google-maps-safe",
  
  rateLimit: {
    maxJobsPerDay: 5,           // Start conservative
    minDelayBetweenJobs: 60,    // 1 min between jobs
    rotateProxy: true,          // Use rotating proxy
    maxRetriesOnBlock: 3,       // Retry with new proxy
    backoffMultiplier: 2        // Exponential backoff
  },
  
  proxyService: "https://proxy-service.company-brain/",
  
  execute: async (input, context) => {
    const proxy = await context.proxy.getNext();
    
    try {
      return await scrapeWithProxy(input, proxy);
    } catch (error) {
      if (error.statusCode === 429) {  // Rate limited
        context.logger.warn("Rate limited, retrying with new proxy");
        const newProxy = await context.proxy.getNext();
        return await scrapeWithProxy(input, newProxy);
      }
      throw error;
    }
  }
});
```

**Monitoring + Alerts:**
- Track blocked IPs in Neo4j
- Auto-pause job on repeated blocks
- Notify on trends (too many blocks = adjust strategy)

---

## SECTOR-SPECIFIC CONFIGURATIONS

### Staffing (OPS-001)
```typescript
googleMapsLeadScraper.configs.staffing = {
  searchQuery: "staffing agencies, recruitment firms",
  location: "Charlotte, NC",  // Adjustable per venture
  minRating: 3.5,
  fieldsNeeded: ["phone", "email", "website", "reviewer_count"],
  outreachTemplate: "recruitment_partnership"
};
```

### Real Estate (RE-001)
```typescript
googleMapsLeadScraper.configs.real_estate = {
  searchQuery: "real estate brokers, realtors",
  location: "nationwide",
  minRating: 4.0,
  fieldsNeeded: ["phone", "email", "website", "avg_response_time"],
  outreachTemplate: "deal_sourcing_partnership"
};
```

### Construction (CON-001)
```typescript
googleMapsLeadScraper.configs.construction = {
  searchQuery: "contractors, construction companies",
  location: "US metros",
  minRating: 3.5,
  fieldsNeeded: ["phone", "email", "website", "years_in_business"],
  outreachTemplate: "bidding_platform_invitation"
};
```

---

## INSTALLATION ROADMAP

### ✅ Week 1: Setup

**Step 1: Install Google Skills Framework**
```bash
npm install -g @google/skills
npx skills init company-brain-skills
```

**Step 2: Install Google Maps Scraper Kit**
```bash
git clone https://github.com/Mahanaicoach/google-maps-scraper-kit
cd google-maps-scraper-kit
docker-compose up -d  # Runs on localhost:8080
```

**Step 3: Create wrapper skill**
```typescript
// company-brain-skills/ventures/google-maps-scraper.ts
// Integrates scraper kit with Skills framework
```

### ✅ Week 2: Test + Verify

**Proof-of-concept:** LT-005 (Medical Courier)
- Search: "Medical facilities in Charlotte"
- Extract: 50 leads
- Enrich: Add emails + contact persons
- Score: Rank by delivery volume potential
- Deploy: Generate outreach sequence

**Expected output:** 50 qualified leads ready for outreach

### ✅ Week 3-4: Scale

- Deploy to 4 Tier-0 ventures
- Monitor for rate limiting
- Adjust configs per sector
- Track conversion rates

### ✅ Month 2: Portfolio-Wide

- Available to all 789 ventures
- Each inherits lead gen capability automatically
- Estimated revenue impact: $50-200K/month

---

## LEGAL + COMPLIANCE

**Important:**
- Google Maps ToS: Scraping is gray area
- Guidance from kit: Use for "lead verification, not redistribution"
- Data protection: Must comply with GDPR/CCPA when contacting
- Recommendation: Include legal review before large-scale deployment

**Safe Practices:**
- ✅ Use for B2B outreach (less regulated)
- ✅ Verify data before using
- ✅ Include unsubscribe option in outreach
- ✅ Respect rate limits (don't over-scrape)
- ❌ Don't sell/redistribute lead lists
- ❌ Don't use for spam campaigns

---

## FINANCIAL IMPACT

### Revenue Loop Acceleration

| Scenario | Leads/Week | Close Rate | Revenue/Week |
|----------|-----------|-----------|--------------|
| Manual (today) | 20 | 5% | $1K |
| Semi-Auto (skills) | 500 | 5% | $25K |
| Full Auto (1000s) | 2000 | 3% | $60K |

**With 789 Ventures:**
- Even at 10% adoption = 79 ventures using skill
- 79 ventures × $5K/week = **$395K/week revenue from lead gen alone**

---

## RECOMMENDATION

### ✅ **Proceed with Installation**

1. **Google Skills** - For standardizing skills across agents
2. **Google Maps Scraper Kit** - For lead generation

**Combined Use Case:**
- Wrap scraper as a "lead-generation" skill
- Deploy to all 789 ventures
- Auto-discover in agent routing (Layer 9)
- Drive revenue loop REV-LOOP-001

**Timeline:** 2 weeks to first revenue, 4 weeks to portfolio deployment

**Risk Mitigation:**
- Start with 3-5 ventures (test rate limiting)
- Monitor IP blocking (pause if needed)
- Adjust query intensity based on results

---

**Next Action:** Install both. Deploy proof-of-concept to LT-005 by end of week.
