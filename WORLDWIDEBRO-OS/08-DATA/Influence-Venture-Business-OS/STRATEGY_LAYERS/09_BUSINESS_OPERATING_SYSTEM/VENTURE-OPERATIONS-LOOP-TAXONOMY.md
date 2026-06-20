# VENTURE OPERATIONS LOOP TAXONOMY
## Complete Loop Map for 712 Ventures

**Date:** 2026-06-10  
**Scope:** 712 ventures across 18 sectors, 6 phases (Planned → Scale)  
**Active Ventures Needing Loops:** 170 (validation + development + growth)  
**Planned Ventures:** 542 (will activate sequentially)

---

## LOOP FRAMEWORK

A **loop** is an automated workflow that runs on a recurring interval and executes business operations.

**Loops are driven by:**
1. **Venture Stage** — What phase is this venture in? (Planned → MVP → Validation → Growth → Scale)
2. **Business Model** — What revenue stream? (Subscription, Transaction, Marketplace, Advertising, Services, etc.)
3. **Sector** — What industry-specific workflows are needed?
4. **MCP Integrations** — Which tools are available? (Supabase, Slack, GitHub, ClickUp, HubSpot, Gmail, Google Calendar, Stripe)

---

## STAGE-BASED LOOPS (What Runs at Each Phase)

### PHASE 0: PLANNED (542 ventures)
**Status:** Not yet active  
**Loops Running:** None (data collection only)

| Loop | Interval | Tool | Purpose |
|------|----------|------|---------|
| Data Collection | 1x weekly | Supabase | Track venture definitions, team assignments |
| Repo Health Check | 1x weekly | GitHub | Monitor repo creation, initial setup |
| Sector Inventory | 1x weekly | CSV export | Ensure all ventures categorized |

---

### PHASE 1: VALIDATION (72 ventures)
**Status:** MVP built, testing with early customers  
**Loops Running:** 4-6 core loops

| Loop | Interval | Tool | Purpose | KPI |
|------|----------|------|---------|-----|
| **Feedback Collection** | Daily | Google Forms + Supabase | Gather early customer feedback | 10+ responses/week |
| **Revenue Tracking** | Daily | Stripe + Supabase | Track any early revenue | Revenue trend |
| **Cost Monitoring** | 3x weekly | Supabase | Monitor burn rate | Burn rate < target |
| **Status Update** | 2x weekly | Slack | Post progress to venture channel | Team alignment |
| **Blocker Resolution** | Daily | ClickUp | Track & resolve blockers | Resolve 80% within 48h |
| **Health Score** | Weekly | Supabase | Calculate venture health (0-100) | Score > 50 |

**Example: BW-001 (Lash Extension Studio)**
- Validation stage: testing with 5-10 early customers
- Daily revenue tracking: Did we make sales today?
- Weekly feedback: Are customers happy? What do they need?
- Blocker loop: Stuck on legal? Payment processing? Staffing?

---

### PHASE 2: MVP DEVELOPMENT (93 ventures)
**Status:** Active development, preparing for launch  
**Loops Running:** 6-8 core loops

| Loop | Interval | Tool | Purpose | KPI |
|------|----------|------|---------|-----|
| **Code Deployment** | On commit | GitHub + Vercel | Deploy code changes | 0 failed builds |
| **Product Roadmap** | Weekly | ClickUp | Prioritize next features | Sprint clarity |
| **Team Standup** | Daily | Slack | Async standup posts | All team members update |
| **Customer Research** | 2x weekly | Google Forms + ClickUp | Interview customers, log feedback | 5+ interviews/week |
| **Competitive Analysis** | Weekly | Manual + AI | Track competitor moves | Market gap clarity |
| **Hiring Pipeline** | Weekly | ClickUp + HubSpot | Pipeline for needed roles | Cover key roles |
| **Financial Forecast** | Weekly | Supabase | Project launch costs | Revenue model validated |
| **Health Score** | Weekly | Supabase | Launch readiness (0-100) | Score > 70 for launch |

**Example: BW-002 (Mobile Lash Service)**
- MVP stage: building mobile app + website
- Daily deploys: Code changes go live automatically
- Weekly roadmap: Next 2 weeks of features decided
- Customer interviews: Validate market need
- Forecast: Will we be profitable post-launch?

---

### PHASE 3: GROWTH (5 ventures + next wave)
**Status:** Launched, acquiring customers, measuring CAC/LTV  
**Loops Running:** 8-12 core loops

| Loop | Interval | Tool | Purpose | KPI |
|------|----------|------|---------|-----|
| **Lead Capture** | Real-time | Webform + HubSpot | Capture inbound leads | 50+ leads/week |
| **Sales Pipeline** | Daily | HubSpot + ClickUp | Track deals through sales funnel | Pipeline clarity |
| **Customer Onboarding** | On signup | Stripe + Email | Automated welcome sequence | 80%+ activation |
| **Expansion Revenue** | Weekly | Stripe | Track upsells, cross-sells | MRR growth 5%+ |
| **Churn Monitoring** | Daily | Supabase | Track customer cancellations | Churn < 5%/month |
| **Acquisition Analytics** | Daily | Google Analytics + Supabase | Track CAC by channel | CAC < LTV/3 |
| **Marketing Campaigns** | Weekly | Slack + HubSpot | Launch new campaigns | 3-5 live campaigns |
| **Team Scaling** | Weekly | ClickUp + Slack | Hire for growth | 2-3 new hires/month |
| **Investor Updates** | Weekly | Slack + Supabase | Track metrics for investors | Deck ready |
| **Cash Flow** | Daily | Stripe + Supabase | Monitor runway | Runway > 6 months |
| **Health Score** | Daily | Supabase | Growth momentum (0-100) | Score > 80 |
| **Burndown** | Weekly | ClickUp | Track sprint progress | On-time delivery 90%+ |

**Example: FIN-036 (Arbitrage Nexus - Already Active)**
- Growth stage: Acquiring customers at scale
- Daily lead capture: Every visitor sign-up recorded
- Sales pipeline: Every lead tracked through buying journey
- CAC tracking: Know exactly how much it costs to acquire each customer
- Churn monitoring: Alert if 2+ customers cancel in one day
- Weekly campaigns: 5 marketing campaigns running simultaneously

---

### PHASE 4: SCALE (next tier)
**Status:** Proven model, systematic growth, hired team  
**Loops Running:** 12-15 loops + automation

| Loop | Interval | Tool | Purpose | KPI |
|------|----------|------|---------|-----|
| **All Phase 3 loops** | (continuous) | (all tools) | (baseline operations) | (all KPIs) |
| **Cohort Analysis** | Weekly | Supabase | Segment customers by cohort, measure retention | Cohort health |
| **Product Experimentation** | Continuous | GitHub + Supabase | A/B tests, feature gates | Win rate > 5% |
| **International Expansion** | Monthly | HubSpot + Stripe | Enter new markets | Revenue/market |
| **Team Management** | Weekly | ClickUp + Slack | Manage 20+ person team | Retention > 90% |
| **Operations Efficiency** | Weekly | Supabase | Cost per unit metric | Unit economics improving |
| **Strategic Partnerships** | Monthly | Email + Calendar | Build partnerships that accelerate growth | Partnership revenue |
| **Acquisition Strategy Pivot** | Monthly | Analytics + Supabase | Test new channels, double down winners | CAC/LTV ratio optimized |

---

## BUSINESS MODEL LOOPS (By Revenue Stream)

### Stream 1: SUBSCRIPTION (Recurring Monthly)
**Ventures:** SaaS, membership, premium courses  
**Must-Have Loops:**

| Loop | Interval | Purpose |
|------|----------|---------|
| **Billing Sync** | Daily | Charge customers, handle failed payments |
| **Churn Analysis** | Daily | Alert if cancellation rate spikes |
| **Renewal Campaigns** | 7 days before renewal | Email reminder + incentive |
| **Dunning Management** | Automatic on failed payment | Retry failed charges 3x with delays |
| **Expansion Revenue** | Daily | Track upsells to higher tier |
| **Feature Gating** | Real-time | Show/hide features by subscription tier |
| **Usage Analytics** | Daily | Track usage to predict churn |

**Example Loop Script:**
```
/loop 1d /subscription-health-check
  - Check Stripe for failed payments
  - Alert ClickUp if >5% daily churn
  - Post to Slack: "MRR: $X, Active: Y, Churn: Z%"
```

---

### Stream 2: TRANSACTION (One-time Purchase)
**Ventures:** E-commerce, digital products, course sales  
**Must-Have Loops:**

| Loop | Interval | Purpose |
|------|----------|---------|
| **Inventory Check** | Real-time | Prevent overselling |
| **Order Fulfillment** | On order | Ship product, send tracking |
| **Payment Processing** | Real-time | Charge card, handle failures |
| **Refund Processing** | On request | Handle returns, refund within 48h |
| **Email Receipts** | On purchase | Send order confirmation + delivery status |
| **Conversion Analytics** | Daily | Track conversion rate by traffic source |
| **Revenue Reporting** | Daily | Revenue by product, category |

**Example Loop Script:**
```
/loop daily /ecommerce-operations
  - Check orders in queue
  - Process refunds < 7 days old
  - Post daily revenue: "Sales: $X, Orders: Y, ROI: Z%"
```

---

### Stream 3: MARKETPLACE (Take Rate on Transactions)
**Ventures:** Uber, Airbnb model — take 15-30% commission  
**Must-Have Loops:**

| Loop | Interval | Purpose |
|------|----------|---------|
| **Transaction Monitoring** | Real-time | Track buyer + seller activity |
| **Commission Calculation** | Daily | Calculate seller payouts |
| **Payout Processing** | Weekly | Pay sellers their cut (85-90%) |
| **Dispute Resolution** | On complaint | Mediate buyer-seller conflicts |
| **Fraud Detection** | Real-time | Block suspicious transactions |
| **Seller Onboarding** | On signup | KYC verification, setup seller account |
| **Network Health** | Daily | Ratio of buyers to sellers balanced |

**Example Loop Script:**
```
/loop 1h /marketplace-health
  - Check transaction volume
  - Alert if disputes spike
  - Post hourly: "Txns: X, Sellers: Y, Buyer/Seller Ratio: Z"
```

---

### Stream 4: ADVERTISING (CPM, CPC, CPA)
**Ventures:** Content sites, YouTube channel, ad-supported apps  
**Must-Have Loops:**

| Loop | Interval | Purpose |
|------|----------|---------|
| **Traffic Analytics** | Hourly | Track visits, impressions, engagement |
| **Ad Network Sync** | Daily | Verify impressions match revenue |
| **Revenue Reporting** | Daily | Revenue by ad network, placement |
| **Content Performance** | Daily | Which content generates most revenue |
| **Ad Optimization** | Weekly | Test new placements, sizes, networks |
| **Brand Safety** | Real-time | Block ads on sensitive content |
| **Audience Growth** | Daily | Track subscriber/follower growth |

**Example Loop Script:**
```
/loop daily /ads-operations
  - Check Google Adsense earnings
  - Calculate daily revenue (views × CPM)
  - Post: "Impressions: X, Revenue: $Y, RPM: $Z"
```

---

### Stream 5: SERVICE-BASED (Billable Hours, Projects)
**Ventures:** Consulting, agencies, freelance marketplaces  
**Must-Have Loops:**

| Loop | Interval | Purpose |
|------|----------|---------|
| **Time Tracking** | Daily | Log billable hours per project |
| **Invoice Generation** | Weekly | Generate invoices from time logs |
| **Payment Collection** | On invoice | Track payment status, send reminders |
| **Utilization Analytics** | Weekly | % of team time billable vs overhead |
| **Resource Planning** | Weekly | Allocate team to upcoming projects |
| **Project Profitability** | Weekly | Revenue per project minus labor cost |
| **Sales Pipeline** | Daily | Track sales of new projects |

**Example Loop Script:**
```
/loop 5d /services-billing
  - Compile time logs from team
  - Generate invoices for completed projects
  - Post: "Billable Hours: X, Revenue: $Y, Utilization: Z%"
```

---

### Stream 6: ASSET-BASED (Ownership, Yield)
**Ventures:** Real estate, equity stakes, licensing  
**Must-Have Loops:**

| Loop | Interval | Purpose |
|------|----------|---------|
| **Portfolio Valuation** | Monthly | Update asset values |
| **Income Collection** | Monthly | Collect rent, royalties, dividends |
| **Expense Tracking** | Monthly | Property taxes, maintenance, insurance |
| **Tax Reporting** | Quarterly | Prepare capital gains, depreciation |
| **Asset Rebalancing** | Quarterly | Buy/sell to maintain target allocation |
| **Risk Monitoring** | Monthly | Tenant health, market conditions |
| **Appreciation Tracking** | Quarterly | Real estate/equity appreciation |

**Example Loop Script:**
```
/loop 1M /asset-operations
  - Collect rent from tenants
  - Pay property expenses
  - Post: "Portfolio Value: $X, Monthly Income: $Y, ROI: Z%"
```

---

### Stream 7: DATA MONETIZATION (Insights, Analytics)
**Ventures:** B2B analytics, market research, intelligence platforms  
**Must-Have Loops:**

| Loop | Interval | Purpose |
|------|----------|---------|
| **Data Collection** | Continuous | Ingest data from sources |
| **Data Processing** | Daily | Clean, deduplicate, enrich data |
| **Insights Generation** | Weekly | Extract patterns, create reports |
| **Customer Subscriptions** | Daily | Track who has access to what |
| **API Usage** | Real-time | Track API calls, bill based on usage |
| **Report Distribution** | Weekly/Monthly | Email reports to subscribers |
| **Data Freshness** | Daily | Ensure data is up-to-date |

**Example Loop Script:**
```
/loop 1d /data-ops
  - Ingest new data sources
  - Generate weekly insights
  - Post: "Data Points: X, Subscribers: Y, Revenue: $Z"
```

---

## SECTOR-SPECIFIC LOOPS

### Financial Sector (41 ventures)
**Additional Loops:**

| Loop | Interval | Purpose |
|------|----------|---------|
| **Compliance Check** | Daily | KYC, AML, regulatory compliance |
| **Risk Monitoring** | Real-time | Fraud detection, account limits |
| **Banking Integration** | Real-time | Account transfers, ACH, wire |
| **Interest Calculation** | Daily | Calculate interest accrual |
| **Audit Trail** | Continuous | Log all transactions for compliance |
| **Portfolio Rebalancing** | Monthly | Investment portfolio optimization |

**Example:** FIN-036 (Arbitrage Nexus) runs:
- Real-time price monitoring (detect arbitrage opportunities)
- Automatic trade execution (buy on exchange A, sell on B)
- Settlement verification
- Tax lot tracking (for reporting)

---

### E-Commerce (110 ventures)
**Additional Loops:**

| Loop | Interval | Purpose |
|------|----------|---------|
| **Inventory Sync** | Real-time | Sync inventory across channels |
| **Price Sync** | Daily | Update prices on all platforms |
| **Supplier Orders** | Automatic | Reorder stock when below threshold |
| **Shipping Integration** | On order | Generate labels, track shipments |
| **Product Reviews** | Daily | Collect + display customer reviews |
| **Returns Processing** | On request | Generate return labels, process refunds |
| **Competitor Pricing** | Weekly | Monitor competitor prices, adjust |

**Example:** BW-001 (Lash Extension Studio) might run:
- Daily inventory check (lash supplies, glue, tools)
- Weekly supplier orders (auto-reorder when stock low)
- Customer reviews collection (ask for 5-star reviews post-service)
- Booking/appointment management

---

### Operations/Services (67 ventures)
**Additional Loops:**

| Loop | Interval | Purpose |
|------|----------|---------|
| **Scheduling** | Real-time | Manage staff calendars, client bookings |
| **Payroll** | Bi-weekly | Pay staff, withhold taxes, file reports |
| **Vendor Management** | Weekly | Track vendor contracts, renewals |
| **Quality Assurance** | Continuous | Service quality monitoring |
| **Customer Satisfaction** | Post-service | NPS surveys, feedback collection |
| **Staff Scheduling** | Weekly | Optimize staff allocation to clients |

**Example:** OPS-001 (Venture Staffing) runs:
- Weekly contractor matching (match contractors to venture needs)
- Payroll processing (bi-weekly to all contractors)
- Utilization tracking (% of time billable)
- Quality feedback collection (venture reviews contractor)

---

### Education/Training (40 ventures)
**Additional Loops:**

| Loop | Interval | Purpose |
|------|----------|---------|
| **Course Progress Tracking** | Daily | Student progress through course |
| **Certificate Issuance** | On completion | Auto-issue completion certificate |
| **Email Nurture** | 3x weekly | Course reminders, next steps |
| **Content Updates** | Monthly | Update course materials, record new videos |
| **Student Surveys** | Post-course | Gather feedback for improvement |
| **Credential Verification** | On request | Verify student credentials |

**Example:** BW-004 (Lash Training Academy) runs:
- Weekly lesson distribution (send next lesson module)
- Progress tracking (students complete 80% to proceed)
- Certification issuance (auto-generate cert on completion)
- Job placement assistance (match graduates to jobs)

---

## CORE INFRASTRUCTURE LOOPS (Run for All Ventures)

These loops run regardless of stage/model:

| Loop | Interval | Tool | Purpose | Applies To |
|------|----------|------|---------|-----------|
| **Health Score Update** | Daily | Supabase | Calculate venture health (0-100) | All ventures |
| **Knowledge Graph Sync** | Daily | Supabase → Obsidian | Update venture data in knowledge graph | All ventures |
| **Slack Notifications** | Daily | Slack | Post daily metrics to venture channels | All ventures (active) |
| **ClickUp Sync** | Daily | ClickUp | Sync tasks, blockers, progress | All ventures |
| **GitHub Health** | Daily | GitHub | Monitor repo commits, PRs, deployments | All ventures with code |
| **Metrics Dashboard** | Hourly | DuckDB → Grafana | Update real-time dashboards | All ventures |
| **Risk Detection** | Daily | Supabase ML | Flag ventures with health < 40 | All ventures |
| **Quarterly Review** | Quarterly | Supabase + Slack | Full venture review, pivot/shutdown decisions | All ventures |

---

## VENTURE LIFECYCLE LOOPS

### Onboarding New Venture (Week 1)
```
/loop 1d /venture-onboarding-[venture-id]
  ✓ Create GitHub repo
  ✓ Set up Supabase schema
  ✓ Create Slack channel
  ✓ Add to ClickUp workspace
  ✓ Initialize health score
  ✓ Add to knowledge graph
  ✓ Send welcome email to team
  → DISABLE after week 1
```

### Validation Phase (Weeks 1-8)
```
/loop 1d /validation-[venture-id]
  ✓ Feedback collection
  ✓ Revenue tracking
  ✓ Cost monitoring
  ✓ Blocker resolution
  ✓ Health score update
  ✓ Team status post
  → UPGRADE to MVP loop at week 8
```

### MVP Development (Weeks 1-16)
```
/loop 1d /mvp-[venture-id]
  ✓ Code deployments
  ✓ Customer research
  ✓ Feature prioritization
  ✓ Team standup
  ✓ Financial forecast
  ✓ Health score update
  → UPGRADE to Growth loop at launch
```

### Growth Phase (Months 1-12)
```
/loop 1d /growth-[venture-id]
  ✓ Lead capture
  ✓ Sales pipeline
  ✓ Onboarding automation
  ✓ Churn monitoring
  ✓ CAC/LTV tracking
  ✓ Expansion revenue
  ✓ Campaign management
  ✓ Health score update
  → SCALE to automated operations
```

### Sunset Decision (When Health < 20)
```
/loop 1d /sunset-evaluation-[venture-id]
  ✓ Check if revenue recovering
  ✓ Check if blockers resolving
  ✓ Check if team committed
  → If no improvement after 30 days: ESCALATE for shutdown decision
```

---

## RUNNING LOOPS ACROSS ALL 712 VENTURES

### Current State (June 2026)
- **Planned (542):** No active loops
- **Validation (72):** Each needs 4-6 loops
- **MVP (93):** Each needs 6-8 loops
- **Growth (5):** Each needs 8-12 loops

### Loop Count
- Validation: 72 × 5 avg = **360 loops**
- MVP: 93 × 7 avg = **651 loops**
- Growth: 5 × 10 avg = **50 loops**
- **Total Active Loops: ~1,061**

### Grouped by Function (Easier to Manage)
Instead of 1,061 individual loops, group by function:

| Function | Interval | Ventures | Loop Script |
|----------|----------|----------|------------|
| **Daily Health Checks** | 1d | All 170 | `/loop 1d /all-ventures-daily-health` |
| **Weekly Reviews** | 1W | All 170 | `/loop 1W /all-ventures-weekly-review` |
| **Slack Updates** | 1d | All 170 | `/loop 1d /post-venture-metrics` |
| **Revenue Tracking** | 1d | Active only | `/loop 1d /revenue-tracking` |
| **Customer Feedback** | 3d | MVP + Growth | `/loop 3d /customer-feedback-loop` |
| **Team Sync** | 2d | MVP + Growth | `/loop 2d /team-standup` |
| **Marketing Campaigns** | 1W | Growth only | `/loop 1W /marketing-campaigns` |
| **CAC/LTV Analysis** | 1d | Growth only | `/loop 1d /cac-ltv-analysis` |

---

## IMPLEMENTATION ROADMAP

### Week 1: Foundation Loops (All Ventures)
- [ ] Daily health score updates
- [ ] Weekly knowledge graph sync
- [ ] Daily Slack notifications

### Week 2: Revenue Loops (Active Ventures)
- [ ] Daily revenue tracking (subscription + transaction)
- [ ] Daily churn monitoring
- [ ] Weekly financial forecasts

### Week 3: Customer Loops (Growth Stage)
- [ ] Lead capture automation
- [ ] Email nurture sequences
- [ ] Customer onboarding

### Week 4: Analysis Loops (All Stages)
- [ ] CAC/LTV calculation
- [ ] Cohort analysis
- [ ] Competitive intelligence

### Weeks 5-8: Scaling Loops (As Ventures Progress)
- [ ] A/B testing infrastructure
- [ ] International expansion workflows
- [ ] Team management automation

---

## LOOP MANAGEMENT COMMANDS

Once loops are set up, manage them with:

```bash
# List all active loops
/loop list

# Check loop status
/loop status [loop-id]

# Pause a loop (maintenance)
/loop pause [loop-id]

# Resume a loop
/loop resume [loop-id]

# Kill a loop (venture sunset)
/loop kill [loop-id]

# View loop output logs
/loop logs [loop-id] --last 7d
```

---

## KEY METRICS BY LOOP

Every loop should output a key metric to track:

| Loop | Key Metric | Alert Threshold |
|------|-----------|-----------------|
| Daily Health | Health Score | < 40 = alert |
| Revenue | MRR / Daily Revenue | < 70% of target |
| Churn | Monthly Churn % | > 5% |
| CAC | Customer Acq Cost | > LTV/3 |
| Burn Rate | Monthly cash burn | > 6-month runway |
| Team | Utilization % | < 70% |
| Product | Feature velocity | < 3 features/week |
| Customer | NPS (Net Promoter) | < 40 |

---

## QUICK REFERENCE: LOOPS BY VENTURE TYPE

### SaaS Venture (Subscription)
**Loops Needed:** Billing, Churn, Renewal, Expansion, Usage Analytics, Health Score = **6 loops**
**Interval:** All Daily except Health Score (Weekly)

### E-Commerce Venture (Transaction)
**Loops Needed:** Inventory, Orders, Fulfillment, Returns, Reviews, Analytics = **6 loops**
**Interval:** Inventory Real-time, Orders Daily, Fulfillment On-order, Reviews Daily

### Agency Venture (Service-based)
**Loops Needed:** Time Tracking, Invoicing, Collections, Utilization, Resource Planning, Sales = **6 loops**
**Interval:** Daily/Weekly mix

### Marketplace Venture (Commissions)
**Loops Needed:** Transactions, Commissions, Payouts, Disputes, Fraud, Network Health = **6 loops**
**Interval:** Real-time for critical, Daily for calculations

### Content Venture (Ads)
**Loops Needed:** Traffic, Ad Networks, Revenue, Performance, Optimization, Growth = **6 loops**
**Interval:** Hourly/Daily/Weekly

### Construction Venture (Services + Products)
**Loops Needed:** Scheduling, Payroll, Vendor Management, Quality, Customer Satisfaction, Project Tracking = **6 loops**
**Interval:** Real-time/Daily/Weekly

---

## NEXT STEPS

1. **Pick 5 active ventures** (FIN-036, BW-001, BW-002, BW-010, OPS-001)
2. **Map their loops** (use Stage + Business Model tables above)
3. **Create core 3 loops per venture** (Health + Revenue + Team)
4. **Test with `/loop` skill** (run first week manually)
5. **Expand to 170 active ventures** (use automated grouping)
6. **Activate planned ventures** sequentially (as team capacity allows)

---

**Questions to refine with user:**
- Which 5 ventures should activate loops FIRST?
- Which metrics matter most for each sector?
- Group loops by stage, or by business model, or by sector?
- How aggressive: full automation or more manual reviews?
