---
references:
  - [[COMPANY-SPINE]]
  - [[VENTURE-MASTER]]
  - [[LOOP-FRAMEWORK]]
  - [[ORB-MASTER-CONNECTOR-2026-06-11]]
---

# VENTURE GROWTH OS — The Reusable Engine

**Directive:** Do NOT build a business from scratch per venture. Build ONE growth engine; each of the 712 ventures is a **configuration**, not a rebuild. Improve the engine once -> every venture benefits.

**Authority:** Pairs with [[COMPANY-SPINE]] (entity/sector/tool structure). This file owns the universal funnel, credibility engine, AI growth team, and the 5 OS modules.

---

## 1. Universal Venture Funnel (14 stages)

Every company — moving, pressure washing, staffing, real estate, AI services, cleaning — runs the same journey. Each stage gets automation + an AI agent.

```
Market -> Attention -> Interest -> Trust -> Lead -> Qualification
-> Estimate/Proposal -> Decision -> Purchase -> Delivery
-> Proof -> Review -> Referral -> Repeat Business
```

---

## 2. Credibility Engine (build trust in this order)

People buy because they trust you, not because you're available. Every completed job creates new credibility assets for the next sale.

| Layer | Purpose | Assets |
|-------|---------|--------|
| Identity | Look legitimate | Logo, branded site, pro email |
| Authority | Show expertise | Educational videos, guides, FAQs |
| Social Proof | Show results | Reviews, testimonials, before/after |
| Portfolio | Demonstrate work | Case studies, completed projects |
| Transparency | Reduce uncertainty | Pricing ranges, process, guarantees |
| Risk Reduction | Lower hesitation | Warranties, insured/bonded |
| Consistency | Reinforce trust | Uniform branding, fast follow-up |

---

## 3. The AI Growth Team (10 agents) -> OS module -> tool

Think in **functions**, not employees. Each agent drives a specific tool.

| # | Agent | Job | OS Module | Drives (tool) |
|---|-------|-----|-----------|---------------|
| 1 | Target | Find likely customers (ICP, geo, buying signals) | Marketing | Airtable + Zapier |
| 2 | Research | Gather context before outreach (company, DM, reviews) | Marketing | Tavily/Exa + Notion |
| 3 | Outreach | Run campaigns (email/SMS/phone/social/referral) | Marketing | Zapier (Gmail/Twilio) |
| 4 | Nurture | Keep relationship warm (6-week drip) | Sales | HubSpot sequences |
| 5 | Qualification | Budget/timeline/scope/DM/urgency fit | Sales | HubSpot |
| 6 | Close | Proposals, objections, signatures, deposits | Sales | HubSpot + Stripe |
| 7 | Operations | Crew, equipment, calendar, materials, routes | Operations | ClickUp + Calendar |
| 8 | Quality | Photos, checklist, satisfaction, warranty | Operations | ClickUp + Airtable |
| 9 | Review | Request review/testimonial/referral, collect media | Customer Success | Zapier |
| 10 | Expansion | Cross-sell adjacent services to existing customers | Customer Success | HubSpot |

**Cross-sell example (Expansion):** Moving -> packing -> storage -> junk removal -> cleaning -> handyman -> painting -> real estate referral. One customer = many services over time.

---

## 4. The 5 Shared OS Modules

| Module | Owns | Primary tools |
|--------|------|---------------|
| **Marketing OS** | Awareness + leads (agents 1-3) | Airtable, Zapier, Tavily/Exa, Higgsfield (content) |
| **Sales OS** | Qualify, nurture, close (agents 4-6) | HubSpot, Stripe |
| **Operations OS** | Schedule crews/equipment/work (agents 7-8) | ClickUp, Google Calendar |
| **Finance OS** | Invoice, collect, measure profit | Stripe, DuckDB, Grafana |
| **Customer Success OS** | Reviews, referrals, repeat (agents 9-10) | HubSpot, Zapier, Slack |

---

## 5. Shared Engine vs Venture-Customized

Adding a new venture = **configuring** the platform, not starting over.

| Shared Engine (build once) | Customized per venture (config) |
|----------------------------|----------------------------------|
| CRM (HubSpot) | Services offered |
| Lead management (HubSpot/Airtable) | Pricing |
| Scheduling (ClickUp/Calendar) | Equipment lists |
| Contracts (Notion) | Training materials |
| Payments (Stripe) | Checklists |
| Marketing automation (Zapier) | Brand identity |
| Review collection (Zapier) | Certifications / licenses |
| Reporting (DuckDB/Grafana) | Service workflows |

---

## 6. Complete Operating Loop

```
Traffic -> Target -> Research -> Outreach -> Lead -> Nurture
-> Qualification -> Close -> Operations -> Crew Dispatch -> Job Completion
-> Quality -> Invoice -> Review -> Referral -> Expansion -> Repeat Customer
```

---

## 7. How it plugs into the spine

- **Holdings -> 18 sectors -> 712 ventures** ([[COMPANY-SPINE]] section 1-2). Every venture inherits this engine.
- **One engine, per-venture config** stored in Airtable (intake/config) + Supabase (truth).
- **Tool roles** are fixed by [[COMPANY-SPINE]] section 4; this doc assigns each tool to an OS module + agent.
- **Improve once, benefit everywhere:** a fix to Marketing OS propagates to all 712.
