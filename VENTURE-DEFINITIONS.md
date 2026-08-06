---
name: VENTURE-DEFINITIONS
title: Worldwidebro Holdings — Venture Definitions & Repository
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# Worldwidebro Holdings — Venture Definitions & Repository

**Total Ventures**: 1,088 (892 seeded + 1 Onboarding template)  
**Sectors**: 17 + General  
**GitHub Organization**: https://github.com/Worldwidebro (687 repos indexed as of Apr 22)  
**Last Updated**: May 11, 2026

---

## How This Works

Each venture in Paperclip represents a distinct business unit with:
1. **Name**: Unique identifier (e.g., `GenixBank-9FY93N`)
2. **Sector**: Industry vertical (Financial Services, Construction, E-Commerce, etc.)
3. **Status**: backlog, planned, in_progress, completed, cancelled
4. **Lead Agent**: Sector PM responsible for day-to-day operations
5. **Metrics**: Revenue, costs, CAC, LTV, churn (tracked in Supabase)
6. **GitHub Repo**: Hosted at `github.com/Worldwidebro/{sector-prefix}-{id}-{name}` (e.g., `fin-001-genixbank-lite`)
7. **Dashboard**: http://localhost:3101/companies/1450a240-2be1-4dc6-b74c-ada307ca6ddb/projects

---

## GitHub Repository Structure

All 892 Paperclip ventures have corresponding GitHub repositories in the Worldwidebro organization.

**Repository Naming Convention**:
- Format: `{sector-prefix}-{venture-number}-{venture-name}`
- Examples:
  - **Financial Services**: `fin-001-genixbank-lite`, `fin-036-arbitrage-nexus-platform` (ACTIVE)
  - **Beauty & Wellness**: `bw-001-lash-extension-studio` (Validation), `bw-002-mobile-lash-service` (Development)
  - **Construction**: `con-001-ace-construction`, etc.

**Repository Status Indicators**:
- ✅ **ACTIVE** (Health 90-100): Running in production, revenue generating
- 🟡 **Development/Validation** (Health 60-80): Code in progress, testing phase
- 📝 **Planned** (Health 55): Defined but not yet started

**GitHub Organization**:
- **URL**: https://github.com/Worldwidebro
- **Current Repos**: 687 ventures documented (as of Apr 22, 2026)
- **Gap**: ~205 new ventures seeded to Paperclip May 11 need GitHub repo sync

**To Find a Venture Repository**:
1. GitHub: https://github.com/orgs/Worldwidebro/repositories?q={sector-prefix}-
2. Or direct: `https://github.com/Worldwidebro/{sector-prefix}-{id}-{venture-name}`

---

## Venture Sectors & Templates

### 1. Financial Services (150+ ventures)
**Examples**: GenixBank, TaxBot, PayFlow, WealthOS, CreditMax, InsureMe, InvestHub

**What They Do**:
- Provide financial solutions, payments, lending, investment services
- Banking platforms, fintech apps, financial analytics

**Key Metrics**:
- Monthly Revenue: $50K-$100K target
- CAC/LTV: >3.0 (high customer lifetime value)
- Churn: <3% monthly (low due to switching costs)
- Runway: 12+ months cash required

**Critical Operations**:
- Regulatory compliance & KYC
- Customer onboarding
- Transaction processing
- Risk & fraud detection

**CEO Decision Framework**:
- ROI <0%: Kill (regulatory/compliance risk)
- ROI 0-50%: Optimize (reduce operational overhead)
- ROI 50-100%: Scale (expand geographies/segments)
- ROI >100%: Compound (reinvest profits, cross-sell)

---

### 2. Construction (100+ ventures)
**Examples**: Ace, BuildPro, SafeSite, EquipRent, ConcreteFlow, RoofPro

**What They Do**:
- Project management, contractor services, equipment rental
- Construction marketplace, supply chain

**Key Metrics**:
- Monthly Revenue: $30K-$50K (project-based)
- CAC/LTV: $5K-$15K acquisition cost per contract
- Churn: <5% (long-term projects reduce churn)
- Runway: 12-24 months (high working capital needs)

**Critical Operations**:
- Project estimation & bidding
- Crew scheduling
- Equipment tracking
- Safety compliance

**CEO Decision Framework**:
- ROI <0%: Kill (capacity constraints)
- ROI 0-50%: Optimize (improve project margins)
- ROI 50-100%: Scale (expand to new regions)
- ROI >100%: Compound (vertical integration, M&A)

---

### 3. E-Commerce & Digital (120+ ventures)
**Examples**: ProductHub, DigitalShop, MarketPro, FulfillMax, ShipSmart, VendorCloud

**What They Do**:
- Online marketplace, product sales, fulfillment, logistics
- Inventory management, shipping integration

**Key Metrics**:
- Monthly Revenue: $20K-$50K (product margins vary)
- CAC/LTV: $20-$100 CAC, $200-$2K LTV
- Churn: <10% monthly (high competition)
- Runway: 6-12 months (tight cash flow)

**Critical Operations**:
- Inventory forecasting
- Order fulfillment
- Customer service & returns
- Supply chain management

**CEO Decision Framework**:
- ROI <0%: Kill (unsustainable unit economics)
- ROI 0-50%: Optimize (reduce COGS/CAC)
- ROI 50-100%: Scale (expand inventory/channels)
- ROI >100%: Compound (vertical integration, brands)

---

### 4. SaaS & Software (80+ ventures)
**Examples**: ProjectMgmt, HRMS, Analytics, DataVault, APIHub, CloudSync, SecurityPro

**What They Do**:
- Cloud software, APIs, enterprise tools, analytics platforms
- Subscription-based software solutions

**Key Metrics**:
- Monthly Revenue: $40K-$100K MRR
- CAC/LTV: High enterprise CAC ($5K-$20K), High LTV (>$50K)
- Churn: <5% monthly (high NRR target: >110%)
- Runway: 12+ months (long sales cycles)

**Critical Operations**:
- Product development & releases
- Customer success & onboarding
- API management
- Security & compliance (SOC2, GDPR)

**CEO Decision Framework**:
- ROI <0%: Kill (wrong market fit)
- ROI 0-50%: Optimize (reduce CAC, improve NRR)
- ROI 50-100%: Scale (add features, expand upmarket)
- ROI >100%: Compound (acquisitions, platforms)

---

### 5. Healthcare & Wellness (45+ ventures)
**Examples**: HealthTrack, TeleMed, PharmaCare, FitnessHub, NutritionAI, MentalWell

**Key Metrics**:
- Monthly Revenue: $25K-$50K
- CAC/LTV: Variable by segment
- Churn: <8% (recurring revenue model)
- Runway: 12+ months (regulatory compliance required)

**Critical Operations**:
- HIPAA/regulatory compliance
- Patient onboarding
- Provider coordination
- Outcome tracking

---

### 6. Real Estate (35+ ventures)
**Examples**: PropertyFlow, RentalPro, InvestRealty, BuildTrack, LeaseHub

**Key Metrics**:
- Monthly Revenue: $35K-$75K
- CAC/LTV: High per transaction
- Churn: <3% (long-term relationships)
- Runway: 12+ months

---

### 7. Manufacturing (40+ ventures)
**Examples**: FactoryAI, QualityPro, SupplyChain, ToolMaker, PartsHub

**Key Metrics**:
- Monthly Revenue: $50K-$100K
- CAC/LTV: Industrial sales cycles
- Churn: <2% (OEM relationships)

---

### 8. Logistics & Supply Chain (45+ ventures)
**Examples**: ShipFlow, RouteOptimizer, WarehouseAI, TrackingHub, DeliveryPro

**Key Metrics**:
- Monthly Revenue: $30K-$60K
- CAC/LTV: $2K-$5K per enterprise customer
- Churn: <5% (operational dependency)

---

### 9. Education & Training (30+ ventures)
**Examples**: LearnHub, CoursePlatform, TutorHub, SkillMaster, AcademicFlow

**Key Metrics**:
- Monthly Revenue: $15K-$40K
- CAC/LTV: Variable (B2C vs B2B)
- Churn: <7% (student retention focus)

---

### 10. Entertainment & Media (35+ ventures)
**Examples**: ContentHub, StreamingPlatform, CreatorFlow, MusicHub, PodcastPro

**Key Metrics**:
- Monthly Revenue: $20K-$60K
- CAC/LTV: Content-driven, viral potential
- Churn: <8% (engagement-dependent)

---

### 11-17. Other Sectors (175+ ventures)
- Energy & Sustainability (25)
- Agriculture & Food (40)
- Travel & Hospitality (35)
- Government & Public Services (30)
- Legal & Compliance (25)
- Human Resources (25)
- Professional Services (32)

---

## Understanding Venture Metrics

### Financial Metrics (Updated Monthly)
- **Monthly Revenue**: Total income from all sources
- **Monthly Cost**: Total operational spend
- **Gross Margin**: (Revenue - COGS) / Revenue
- **ROI**: (Revenue - Cost) / Cost × 100%

### Unit Economics (Most Important)
- **CAC (Customer Acquisition Cost)**: Total marketing spend / new customers
- **LTV (Customer Lifetime Value)**: Expected total revenue per customer over lifetime
- **LTV/CAC Ratio**: Healthy when >3.0 (earn 3x what you spend to acquire)
- **Payback Period**: CAC / (Monthly Margin per Customer)

### Churn & Retention
- **Monthly Churn**: % of customers lost per month
- **NRR (Net Revenue Retention)**: Revenue from existing customers after churn + expansion
- **Healthy NRR**: >100% (expansion offsets churn)

### Runway & Cash
- **Monthly Burn Rate**: Cost - Revenue (negative if losing money)
- **Runway**: Cash / Monthly Burn (how many months until no cash)
- **Alert**: Red if runway <6 months

---

## CEO Decision Framework

All ventures are evaluated monthly by CEO agent using ROI thresholds:

| ROI Range | Decision | Action | Budget |
|-----------|----------|--------|--------|
| < 0% | **KILL** | Wind down, redeploy capital | $0 |
| 0-50% | **OPTIMIZE** | Reduce costs 20%, test channels | $1K/mo |
| 50-100% | **SCALE** | 2x marketing, expand segments | $3K/mo |
| >100% | **COMPOUND** | Reinvest all profits, hire aggressively | $5K/mo |

### Example Decision (GenixBank-9FY93N)
```
Revenue:        $7,831.88/mo
Cost:           $3,887.66/mo
Gross Margin:   50.4%
ROI:            101.5%
LTV/CAC Ratio:  5.69x
Churn:          6.2%

Decision: COMPOUND
Reasoning: Strong ROI, though churn >5%. Reinvest profits, expand team, build retention.
Budget: $5,000/month
Action Items:
  - Reinvest all profits
  - Expand team aggressively
  - Build competitive moats
  - Explore adjacent markets
```

---

## Accessing Venture Data

### Via Paperclip Web UI
```
http://localhost:3101/
→ Companies → Worldwidebro Holdings
→ Projects → [Search by name or sector]
```

### Via API
```bash
# List all ventures
curl http://localhost:3101/api/companies/1450a240-2be1-4dc6-b74c-ada307ca6ddb/projects?limit=1000

# Get specific venture
curl http://localhost:3101/api/companies/1450a240-2be1-4dc6-b74c-ada307ca6ddb/projects/{ventureId}
```

### Via Scripts
```bash
# Test end-to-end decision flow
npx ts-node e2e-venture-test.ts

# Seed more ventures
npx ts-node sector-seeding.ts
```

---

## What Claude Needs to Know About Each Venture

When reviewing ventures, Claude should understand:

✅ **Available Now**:
- Sector & vertical (name, description)
- Assigned operator (lead agent)
- Status (backlog, planned, in_progress)
- URL to view in Paperclip

❌ **Not Yet Available** (Task 9+):
- Actual financial metrics (in Supabase)
- Historical performance data
- Customer feedback & NPS
- Team composition
- Actual code/codebase links

**Next Step**: Integrate Supabase ventures table → metrics dashboard for real-time visibility.

---

## Task Status

- ✅ Task 7: Seeded 892 ventures across 17 sectors
- ✅ Task 8: Validated end-to-end decision flow
- 🟡 Task 9: Implement financial analyst logic (CAC/LTV calculations)
- 🟡 Task 10: Implement CEO decision framework (ROI thresholds)
- 🟡 Task 11: Implement operations manager execution
- 🔴 Task 14: Activate 24-hour autonomous cycles
- 🔴 Task 16: Deploy to Vercel

---

## Summary

**You now have**:
- 1,088 ventures in Paperclip (892 seeded + 1 template)
- 9 agents ready to make decisions (CEO, CTO, CFO, 4 PMs, 2 additional)
- Complete decision flow validated (metrics → analysis → decision)
- Dashboard at http://localhost:3101

**Next**: Implement the financial calculations and autonomous cycles to have the system make real decisions about capital allocation across all ventures.
