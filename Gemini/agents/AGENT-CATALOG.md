# Complete Agent Index for Worldwidebro Holdings

---

## Agent Architecture Overview

```
HOLDING COMPANY AGENTS (Network Orchestration)
├─ Network Operations Agent
├─ Capital Allocation Agent
├─ Performance Analytics Agent
└─ Strategic Planning Agent

SECTOR-SPECIFIC AGENTS (14 Sectors)
├─ Staffing Agents (93 ventures)
├─ Construction Agents (57 ventures)
├─ Real Estate Agents (25 ventures)
├─ Financial Agents (25 ventures)
├─ Operations Agents (1 venture)
├─ Technology Agents (30 ventures)
├─ Hospitality Agents (100 ventures)
├─ Healthcare Agents (35 ventures)
├─ Education Agents (41 ventures)
├─ Media Agents (121 ventures)
├─ Investment Agents (112 ventures)
├─ Marketplace Agents (21 ventures)
├─ Beauty Wellness Agents (20 ventures)
└─ Transportation Agents (31 ventures)

CROSS-FUNCTIONAL AGENTS (Shared Services)
├─ Finance & Accounting Agents
├─ Legal & Compliance Agents
├─ HR & People Operations Agents
├─ Marketing & Growth Agents
├─ Customer Success Agents
└─ Data & Analytics Agents
```

---

## HOLDING COMPANY AGENTS

### 1. Network Operations Agent
**File:** `/agents/holding/network-operations.md`

**Role:** Monitor and optimize delegation flows across all 14 sectors. Identify bottlenecks, escalate rejections, spawn new ventures to absorb overflow.

**Capabilities:**
- Monitor `/network/delegation/queue` for pending requests
- Track delegation velocity (target: 50+/week)
- Identify bottlenecks (rejection rate > 20%)
- Escalate to Level 3 when delegation fails 3+ times
- Trigger Fractal to spawn new ventures when capacity exceeded

**Tools/MCPs:**
- Neo4j (query delegation edges)
- Supabase (query `delegations` table)
- vex API (monitor `/network/health`)
- Fractal (spawn new ventures)

**Decision Authority:**
- Level 2: Can reallocate work between ventures
- Level 3: Can spawn new ventures, pivot business model

**Serves:** All 14 sectors

**Handoff Protocol:**
- Receives: Escalation alerts from sector agents
- Sends: New venture assignments, capacity reallocation

**KPIs:**
- Network Delegation Velocity: 50+ work items/week
- Rejection Rate: < 10%
- Bottleneck Resolution Time: < 48 hours

---

### 2. Capital Allocation Agent
**File:** `/agents/holding/capital-allocation.md`

**Role:** Allocate capital across ventures based on performance, margin capture, and strategic priority. Maximize portfolio-level ROI.

**Capabilities:**
- Analyze venture P&L from Supabase
- Track margin capture by sector (Neo4j)
- Allocate capital to highest-performing ventures
- Approve capital requests > $50k (Level 3)
- Generate quarterly capital allocation reports

**Tools/MCPs:**
- Supabase (`transactions`, `ventures` tables)
- Neo4j (margin capture edges)
- Finance OS (P&L models)
- Excel/Google Sheets (reporting)

**Decision Authority:**
- Level 2: Allocate < $50k to ventures
- Level 3: Approve > $50k allocations, M&A

**Serves:** All 14 sectors

**Handoff Protocol:**
- Receives: Capital requests from sector agents
- Sends: Capital allocations, budget approvals

**KPIs:**
- Portfolio ROI: > 25% annually
- Capital Deployment Velocity: < 7 days
- Underperforming Ventures: < 10% of portfolio

---

### 3. Performance Analytics Agent
**File:** `/agents/holding/performance-analytics.md`

**Role:** Aggregate performance data across all ventures, generate executive dashboards, identify trends, and feed insights to Strategic Planning Agent.

**Capabilities:**
- Pull KPIs from all sector agents
- Generate CEO dashboard (revenue, margin, velocity)
- Identify top/bottom performing ventures
- Feed insights to Strategic Planning Agent
- Trigger SkillOpt when KPIs miss targets

**Tools/MCPs:**
- Neo4j (query venture performance)
- Supabase (aggregate transactions)
- vex API (pull dashboard data)
- SkillOpt (trigger optimization loops)

**Decision Authority:**
- Level 1: Generate reports, identify trends
- Level 2: Recommend strategic pivots

**Serves:** All 14 sectors

**Handoff Protocol:**
- Receives: KPI data from sector agents
- Sends: Performance reports to CEO, optimization triggers to SkillOpt

**KPIs:**
- Dashboard Accuracy: 100%
- Insight Generation: 5+ actionable insights/week
- Time-to-Report: < 24 hours

---

### 4. Strategic Planning Agent
**File:** `/agents/holding/strategic-planning.md`

**Role:** Define 5-year vision, annual priorities, and strategic initiatives. Align all ventures to holding company mission.

**Capabilities:**
- Define strategic priorities (quarterly)
- Set OKRs for each sector
- Align venture goals to holding company mission
- Approve business model pivots (Level 3)
- Generate 5-year plan updates

**Tools/MCPs:**
- Obsidian (strategic docs)
- Neo4j (network topology)
- Performance Analytics Agent (insights)

**Decision Authority:**
- Level 3: Approve business model pivots, new sectors

**Serves:** All 14 sectors

**Handoff Protocol:**
- Receives: Performance insights, market data
- Sends: Strategic priorities, OKRs to sector agents

**KPIs:**
- Strategic Initiative Completion: > 80%
- OKR Achievement: > 70% across portfolio
- Market Share Growth: > 15% annually

---

## SECTOR-SPECIFIC AGENTS

### STAFFING SECTOR (93 Ventures)

#### 5. Staffing Sourcing Agent
**File:** `/agents/staffing/sourcing-agent.md`

**Role:** Source contractors and employees for all sectors. Execute labor arbitrage by finding talent faster and cheaper than external agencies.

**Capabilities:**
- Receive `labor_sourcing` delegations from CON/RE/HOSP
- Scrape LinkedIn, job boards, contractor networks
- Auto-screen candidates (license, insurance, experience)
- Present 3 qualified candidates to requesting venture
- Deploy contractor within 48 hours

**Tools/MCPs:**
- Apollo.io (LinkedIn scraping)
- Indeed API (job board search)
- Checkr API (background checks)
- NCLBGC API (NC license verification)
- HubSpot (CRM)

**Decision Authority:**
- Level 1: Source and screen candidates
- Level 2: Final approval on contractor deployment

**Serves:** CON, RE, HOSP, HEALTH, EDU, TRANSPORT

**Handoff Protocol:**
- Receives: `labor_sourcing` delegations
- Sends: Qualified candidates, deployed contractors

**KPIs:**
- Sourcing Velocity: < 24 hours
- Placement Rate: > 70% of delegations
- CAC per Contractor: < $300

---

#### 6. Staffing Vetting Agent
**File:** `/agents/staffing/vetting-agent.md`

**Role:** Verify contractor credentials, run background checks, ensure 100% compliance before deployment.

**Capabilities:**
- Verify NC licenses (NCLBGC database)
- Verify liability insurance (min $1M)
- Run criminal, credit, driving background checks
- Conduct skills assessments (trade-specific)
- Flag non-compliant candidates

**Tools/MCPs:**
- NCLBGC API
- Checkr API (background checks)
- EZLynx API (insurance verification)
- Custom skills assessment platform

**Decision Authority:**
- Level 1: Approve/reject candidates based on criteria
- Level 2: Override rejections with human review

**Serves:** All sectors requiring labor

**Handoff Protocol:**
- Receives: Candidate profiles from Sourcing Agent
- Sends: Approved/rejected status to Sourcing Agent

**KPIs:**
- Vetting Pass Rate: > 70%
- Compliance Rate: 100%
- Time-to-Vet: < 24 hours

---

#### 7. Staffing Placement Agent
**File:** `/agents/staffing/placement-agent.md`

**Role:** Deploy approved contractors to requesting ventures, manage work orders, track utilization, and invoice at markup.

**Capabilities:**
- Match contractor to work order (skills, location, availability)
- Generate work order with scope, timeline, rate
- Deploy contractor to job site
- Track utilization (contractor working vs. idle)
- Invoice requesting venture at 30-40% markup

**Tools/MCPs:**
- HubSpot (work order management)
- Twilio (SMS communication with contractors)
- QuickBooks (invoicing)
- Time tracking API (utilization monitoring)

**Decision Authority:**
- Level 1: Deploy contractors, generate work orders
- Level 2: Approve rate changes > 10%

**Serves:** All sectors requiring labor

**Handoff Protocol:**
- Receives: Approved contractors from Vetting Agent
- Sends: Deployed contractors, invoices to requesting venture

**KPIs:**
- Placement Velocity: < 48 hours
- Contractor Utilization: > 80%
- Gross Margin: 30-40%

---

### CONSTRUCTION SECTOR (57 Ventures)

#### 8. Construction Project Manager Agent
**File:** `/agents/construction/project-manager.md`

**Role:** Execute construction projects from acquisition to completion. Manage contractors, track milestones, ensure on-time/on-budget delivery.

**Capabilities:**
- Acquire projects (from RE delegation or external leads)
- Qualify leads (verify property ownership, budget, timeline)
- Generate auto-SOW (scope of work, materials, timeline)
- Delegate labor needs to STA within 24 hours
- Track milestones, manage change orders
- Handoff completed project to RE within 24 hours

**Tools/MCPs:**
- HubSpot (CRM, lead management)
- Procore (project management)
- PlanSwift (estimation, takeoffs)
- Twilio (client communication)
- QuickBooks (invoicing)

**Decision Authority:**
- Level 1: Manage projects < $50k
- Level 2: Approve change orders < $10k
- Level 3: Approve projects > $50k

**Serves:** RE (receives property delegations), STA (delegates labor)

**Handoff Protocol:**
- Receives: Property renovation delegations from RE
- Sends: Labor sourcing delegations to STA, completed projects to RE

**KPIs:**
- On-Time Completion: > 85%
- Budget Variance: < 10%
- Gross Margin: 25-35%

---

#### 9. Construction Estimation Agent
**File:** `/agents/construction/estimation-agent.md`

**Role:** Generate accurate cost estimates for construction projects. Calculate labor, materials, and management fees.

**Capabilities:**
- Analyze project scope (square footage, materials, complexity)
- Pull labor rates from STA
- Pull material costs from supplier databases
- Generate detailed SOW with transparent pricing
- Account for Mecklenburg County permitting timelines

**Tools/MCPs:**
- PlanSwift (takeoff software)
- RSMeans (cost database)
- STA API (labor rates)
- Local supplier APIs (material costs)

**Decision Authority:**
- Level 1: Generate estimates < $100k
- Level 2: Approve estimates > $100k

**Serves:** Project Manager Agent

**Handoff Protocol:**
- Receives: Project scope from Project Manager
- Sends: Detailed estimates, SOWs

**KPIs:**
- Estimate Accuracy: > 90% (actual vs. estimated)
- Estimation Time: < 24 hours
- Win Rate: > 30% of estimates converted to contracts

---

#### 10. Construction Compliance Agent
**File:** `/agents/construction/compliance-agent.md`

**Role:** Ensure all construction projects meet NC licensing, insurance, safety, and permitting requirements.

**Capabilities:**
- Verify contractor licenses (NCLBGC)
- Verify insurance certificates
- Track Mecklenburg County LUESA permits
- Ensure OSHA compliance on job sites
- Flag non-compliant projects

**Tools/MCPs:**
- NCLBGC API
- Insurance verification APIs
- Mecklenburg County permitting portal
- OSHA compliance database

**Decision Authority:**
- Level 1: Approve/reject compliance status
- Level 2: Halt non-compliant projects

**Serves:** Project Manager Agent

**Handoff Protocol:**
- Receives: Contractor profiles, project plans
- Sends: Compliance status, permit approvals

**KPIs:**
- Compliance Rate: 100%
- Permit Approval Time: < 7 days
- Safety Incidents: 0

---

### REAL ESTATE SECTOR (25 Ventures)

#### 11. Real Estate Acquisition Agent
**File:** `/agents/realestate/acquisition-agent.md`

**Role:** Source off-market and value-add property acquisition opportunities. Analyze deals, negotiate terms, close acquisitions.

**Capabilities:**
- Source properties (off-market, MLS, auctions)
- Analyze deals (cap rate, cash-on-cash, IRR)
- Negotiate terms with sellers
- Coordinate with FIN for acquisition financing
- Close acquisitions, transfer to property management

**Tools/MCPs:**
- MLS API (property listings)
- CoStar (commercial real estate data)
- FIN API (financing options)
- DocuSign (contract execution)

**Decision Authority:**
- Level 1: Analyze deals < $500k
- Level 2: Negotiate terms < $1M
- Level 3: Approve acquisitions > $1M

**Serves:** FIN (delegates deal structuring), CON (delegates renovation)

**Handoff Protocol:**
- Receives: Market data, off-market leads
- Sends: Acquisition opportunities to FIN, renovation needs to CON

**KPIs:**
- Deal Flow: 10+ qualified deals/month
- Acquisition Closing Rate: > 20%
- Average Cap Rate: > 8%

---

#### 12. Real Estate Property Management Agent
**File:** `/agents/realestate/property-management.md`

**Role:** Manage rental properties, screen tenants, collect rent, coordinate maintenance, maximize occupancy and NOI.

**Capabilities:**
- Onboard properties (from CON or external acquisitions)
- Screen tenants (credit, background, rental history)
- Collect rent, enforce lease terms
- Coordinate maintenance (delegate to STA)
- Track occupancy, generate financial reports

**Tools/MCPs:**
- AppFolio (property management software)
- Tenant screening APIs (credit, background)
- STA API (maintenance staffing)
- QuickBooks (rent collection, financial reporting)

**Decision Authority:**
- Level 1: Approve tenants, coordinate maintenance < $1k
- Level 2: Approve capital expenditures < $10k
- Level 3: Approve evictions, major renovations

**Serves:** STA (delegates maintenance roles), CON (delegates renovation projects)

**Handoff Protocol:**
- Receives: Completed properties from CON, acquisitions
- Sends: Maintenance delegations to STA, renovation delegations to CON

**KPIs:**
- Occupancy Rate: > 95%
- Rent Collection Rate: > 98%
- Maintenance Resolution Time: < 48 hours
- NOI Growth: > 10% annually

---

#### 13. Real Estate Deal Sourcing Agent
**File:** `/agents/realestate/deal-sourcing.md`

**Role:** Identify properties needing financing (acquisition, refinance, development). Source deals for FIN to structure.

**Capabilities:**
- Analyze portfolio for refinancing opportunities
- Source off-market development deals
- Package property data for FIN underwriting
- Track deal flow, prioritize high-arbitrage opportunities

**Tools/MCPs:**
- CoStar (property data)
- FIN API (financing criteria)
- Market analysis tools

**Decision Authority:**
- Level 1: Source deals < $1M
- Level 2: Prioritize deals > $1M

**Serves:** FIN (delegates deal structuring)

**Handoff Protocol:**
- Receives: Portfolio data, market intelligence
- Sends: Deal opportunities to FIN

**KPIs:**
- Deal Flow to FIN: 5+ qualified deals/quarter
- Deal Quality: > 80% accepted by FIN
- Average Deal Size: > $500k

---

### FINANCIAL SECTOR (25 Ventures)

#### 14. Financial Deal Structuring Agent
**File:** `/agents/financial/deal-structuring.md`

**Role:** Structure financing deals (debt, equity, mezzanine) for CON projects, RE acquisitions, and other ventures. Maximize capital efficiency.

**Capabilities:**
- Receive deal flow from RE, CON
- Underwrite deals (financial models, risk assessment)
- Structure capital stack (debt/equity mix)
- Coordinate with OPS for SPV formation
- Present deals to INVESTMENT sector for capital deployment

**Tools/MCPs:**
- Financial modeling software (Excel, Python)
- Risk assessment APIs
- OPS API (SPV formation)
- INVESTMENT API (capital deployment)

**Decision Authority:**
- Level 1: Structure deals < $1M
- Level 2: Approve deals < $5M
- Level 3: Approve deals > $5M

**Serves:** INVESTMENT (delegates capital deployment), RE/CON (receives deal flow)

**Handoff Protocol:**
- Receives: Deal opportunities from RE, CON
- Sends: Structured deals to INVESTMENT

**KPIs:**
- Underwriting Time: < 72 hours
- Deal Approval Rate: > 70%
- Advisory Margin: > 1.5%

---

#### 15. Financial Underwriting Agent
**File:** `/agents/financial/underwriting.md`

**Role:** Analyze financial risk, run underwriting models, validate collateral, ensure deals meet investment criteria.

**Capabilities:**
- Build financial models (DCF, IRR, cash flow)
- Analyze risk (market, credit, operational)
- Validate collateral (property appraisals, asset verification)
- Flag high-risk deals
- Generate underwriting reports

**Tools/MCPs:**
- Financial modeling APIs
- Property appraisal APIs
- Risk assessment databases
- Market data feeds

**Decision Authority:**
- Level 1: Approve low-risk deals
- Level 2: Flag high-risk deals for review

**Serves:** Deal Structuring Agent

**Handoff Protocol:**
- Receives: Deal packages from Deal Structuring
- Sends: Underwriting reports, risk assessments

**KPIs:**
- Underwriting Accuracy: > 95%
- Risk Flag Rate: < 10% false positives
- Time-to-Underwrite: < 48 hours

---

### OPERATIONS SECTOR (1 Venture)

#### 16. Operations Legal Agent
**File:** `/agents/operations/legal.md`

**Role:** Provide legal services to all ventures: contract generation, review, compliance, dispute resolution.

**Capabilities:**
- Generate standard contracts (MSA, work orders, leases)
- Review custom contracts for risk
- Ensure regulatory compliance (NC state, federal)
- Handle disputes, coordinate with external counsel

**Tools/MCPs:**
- Contract generation templates (DocuSign, PandaDoc)
- Legal research databases (Westlaw, LexisNexis)
- Compliance tracking software

**Decision Authority:**
- Level 1: Generate standard contracts
- Level 2: Approve custom contracts < $100k
- Level 3: Approve contracts > $100k, litigation

**Serves:** All 14 sectors

**Handoff Protocol:**
- Receives: Contract requests from all ventures
- Sends: Executed contracts, legal opinions

**KPIs:**
- Contract Generation Time: < 24 hours
- Compliance Rate: 100%
- Dispute Resolution Time: < 30 days

---

#### 17. Operations Accounting Agent
**File:** `/agents/operations/accounting.md`

**Role:** Provide centralized accounting services: bookkeeping, payroll, tax preparation, financial reporting.

**Capabilities:**
- Process accounts payable/receivable
- Run payroll (W-2 employees, 1099 contractors)
- Prepare quarterly/annual tax filings
- Generate financial statements (P&L, balance sheet, cash flow)
- Ensure GAAP compliance

**Tools/MCPs:**
- QuickBooks Online (accounting)
- Gusto (payroll)
- Tax preparation software (TurboTax Business, Drake)
- Financial reporting tools

**Decision Authority:**
- Level 1: Process routine transactions
- Level 2: Approve expenditures < $10k
- Level 3: Approve expenditures > $10k, tax strategy

**Serves:** All 14 sectors

**Handoff Protocol:**
- Receives: Invoices, payroll data, financial requests
- Sends: Financial statements, tax filings, payroll reports

**KPIs:**
- Transaction Processing Time: < 24 hours
- Payroll Accuracy: 100%
- Tax Filing Accuracy: 100%

---

#### 18. Operations HR Agent
**File:** `/agents/operations/hr.md`

**Role:** Provide HR services: hiring, onboarding, performance management, compliance, employee relations.

**Capabilities:**
- Post job listings, screen candidates
- Onboard new employees (paperwork, training)
- Manage performance reviews, promotions
- Ensure employment law compliance (FLSA, OSHA, EEO)
- Handle employee relations, dispute resolution

**Tools/MCPs:**
- ATS (Applicant Tracking System: Greenhouse, Lever)
- HRIS (Human Resources Information System: BambooHR, Rippling)
- Performance management software (Lattice, 15Five)
- Compliance tracking tools

**Decision Authority:**
- Level 1: Screen candidates, onboard employees
- Level 2: Approve hires < $100k salary
- Level 3: Approve hires > $100k, terminations

**Serves:** All 14 sectors

**Handoff Protocol:**
- Receives: Hiring requests, employee issues
- Sends: Hired candidates, HR reports, compliance updates

**KPIs:**
- Time-to-Hire: < 30 days
- Employee Retention: > 85%
- Compliance Rate: 100%

---

## CROSS-FUNCTIONAL AGENTS

### 19. Marketing & Growth Agent
**File:** `/agents/cross-functional/marketing.md`

**Role:** Generate demand for all ventures through content marketing, SEO, paid ads, social media, and email campaigns.

**Capabilities:**
- Create content (blog posts, videos, social media)
- Optimize SEO (keyword research, on-page, technical)
- Run paid ads (Google, Meta, LinkedIn)
- Manage email campaigns (nurture, conversion)
- Track CAC, conversion rates, ROI

**Tools/MCPs:**
- Content creation (Canva, Adobe Creative Suite)
- SEO tools (Ahrefs, SEMrush)
- Ad platforms (Google Ads, Meta Ads)
- Email marketing (HubSpot, Mailchimp)
- Analytics (Google Analytics, Mixpanel)

**Decision Authority:**
- Level 1: Create content, optimize campaigns
- Level 2: Approve ad spend < $5k/month
- Level 3: Approve ad spend > $5k/month

**Serves:** All 14 sectors

**Handoff Protocol:**
- Receives: Marketing requests from ventures
- Sends: Leads, brand awareness, conversion data

**KPIs:**
- CAC: < $500 (varies by sector)
- Conversion Rate: > 5%
- ROI: > 3x on ad spend

---

### 20. Customer Success Agent
**File:** `/agents/cross-functional/customer-success.md`

**Role:** Ensure customer satisfaction, drive retention, identify upsell opportunities, collect feedback.

**Capabilities:**
- Onboard new customers
- Monitor usage, identify at-risk accounts
- Conduct QBRs (Quarterly Business Reviews)
- Collect NPS, CSAT feedback
- Identify upsell/cross-sell opportunities

**Tools/MCPs:**
- CRM (HubSpot, Salesforce)
- Customer support (Zendesk, Intercom)
- NPS/CSAT tools (Delighted, AskNicely)
- Analytics (Mixpanel, Amplitude)

**Decision Authority:**
- Level 1: Handle routine support, onboard customers
- Level 2: Approve discounts < 10%
- Level 3: Approve discounts > 10%, handle escalations

**Serves:** All 14 sectors

**Handoff Protocol:**
- Receives: New customers, support tickets
- Sends: Retention data, upsell opportunities, feedback

**KPIs:**
- NPS: > 50
- Retention Rate: > 90%
- Upsell Revenue: > 20% of ARR

---

### 21. Data & Analytics Agent
**File:** `/agents/cross-functional/data-analytics.md`

**Role:** Build data infrastructure, create dashboards, generate insights, support decision-making across all ventures.

**Capabilities:**
- Build data pipelines (ETL, ELT)
- Create dashboards (vex, internal tools)
- Generate insights (trend analysis, forecasting)
- Support ad-hoc analysis requests
- Ensure data quality, governance

**Tools/MCPs:**
- Data warehouses (Snowflake, BigQuery)
- ETL tools (Fivetran, Airbyte)
- BI tools (Looker, Tableau)
- Analytics platforms (Mixpanel, Amplitude)
- SQL, Python, R

**Decision Authority:**
- Level 1: Build dashboards, run analysis
- Level 2: Approve data infrastructure changes
- Level 3: Approve major data architecture decisions

**Serves:** All 14 sectors

**Handoff Protocol:**
- Receives: Data requests, raw data from ventures
- Sends: Dashboards, insights, reports

**KPIs:**
- Dashboard Accuracy: 100%
- Insight Generation: 10+ insights/week
- Data Quality Score: > 95%

---

## STANDARD VENTURE AGENT STACK

Every operating company under the portfolio inherits a standardized stack of 9 AI agents. These agents automate the shared sales campaign engine, onboarding, billing, and day-to-day operations.

### 1. Lead Discovery Agent
*   **Role**: Scrape directories, maps, and job boards to build a continuous list of local B2B prospects.
*   **Key Tools**: Google Maps API, LinkedIn, specialized web scraping MCPs.
*   **Handoff**: Sends raw leads to the Company Research Agent.

### 2. Company Research Agent
*   **Role**: Enrich company profiles, find emails, verify hierarchy, and identify the decision-makers.
*   **Key Tools**: Hunter.io, LinkedIn API, Supabase companies table.
*   **Handoff**: Sends enriched accounts to the Outreach Agent.

### 3. Outreach Agent
*   **Role**: Automate multi-channel cold sequences (cold emails, LinkedIn messages, prep Twilio call briefs).
*   **Key Tools**: SendGrid API, Twilio, LinkedIn.
*   **Handoff**: Routes positive responses to the Sales Agent.

### 4. Sales Agent
*   **Role**: Manage the pipeline status, schedule discovery calls, and draft initial proposals/estimates.
*   **Key Tools**: CRM Database, Google Calendar API.
*   **Handoff**: Hands off signed proposals to the Onboarding Agent.

### 5. Onboarding Agent
*   **Role**: Draft agreements, send contracts for electronic signature, track onboarding documents, and set up client accounts.
*   **Key Tools**: DocuSign API, Jotform, Google Drive.
*   **Handoff**: Deploys onboarding checklists and notifies the Operations Agent.

### 6. Operations Agent
*   **Role**: Manage day-to-day dispatching, coordinate work orders, and track project execution status.
*   **Key Tools**: Neo4j, Supabase queue, GPS mapping APIs.
*   **Handoff**: Submits completed project logs to the Compliance and Billing Agents.

### 7. Compliance Agent
*   **Role**: Audit credentials, track licenses, MVRs, and monitor OSHA/HIPAA training expirations.
*   **Key Tools**: NCDMV checker, background check APIs, Supabase.
*   **Handoff**: Flags any compliance breaches to the Operations Agent.

### 8. Billing Agent
*   **Role**: Auto-generate invoices, process Stripe checkout links, sync QuickBooks, and handle receivables follow-up.
*   **Key Tools**: QuickBooks API, Stripe Dashboard.
*   **Handoff**: Notifies the Customer Success Agent upon successful payout logs.

### 9. Customer Success Agent
*   **Role**: Automate NPS surveys, invite reviews on local business listings, and solicit client referrals.
*   **Key Tools**: Twilio SMS, Email APIs.
*   **Handoff**: Feeds referrals back into the Lead Discovery Agent.

---

## AGENT PERMISSIONS MATRIX

| Agent Type | Level 1 (Autonomous) | Level 2 (Human-in-Loop) | Level 3 (Strategic) |
|------------|---------------------|------------------------|---------------------|
| Sourcing | Screen candidates | Deploy contractors | Override vetting rejections |
| Project Manager | Manage projects < $50k | Approve change orders < $10k | Approve projects > $50k |
| Property Management | Approve tenants, maintenance < $1k | CapEx < $10k | Evictions, major renovations |
| Deal Structuring | Structure deals < $1M | Approve deals < $5M | Approve deals > $5M |
| Legal | Generate standard contracts | Approve contracts < $100k | Approve contracts > $100k |
| Accounting | Process transactions | Approve expenditures < $10k | Approve expenditures > $10k |
| HR | Screen candidates, onboard | Approve hires < $100k | Approve hires > $100k, terminations |
| Marketing | Create content, optimize | Approve ad spend < $5k/mo | Approve ad spend > $5k/mo |
| Customer Success | Handle support, onboard | Approve discounts < 10% | Approve discounts > 10% |
| Data Analytics | Build dashboards, analyze | Approve infra changes | Approve architecture decisions |
| Network Operations | Monitor delegations | Reallocate work | Spawn new ventures |
| Capital Allocation | Allocate < $50k | Approve > $50k | M&A, pivots |

---

## AGENT INTERACTION MAP

```
STAFFING AGENTS
├─ Sourcing Agent ──→ Vetting Agent ──→ Placement Agent
                                        │
                                        ↓
CONSTRUCTION AGENTS                     ↓
├─ Estimation Agent ──→ Project Manager Agent ←── (receives deployed contractors)
                        │
                        ├─→ Compliance Agent
                        └─→ (hands off completed project to RE)
                            
REAL ESTATE AGENTS
├─ Acquisition Agent ──→ Property Management Agent
│                        │
│                        ├─→ (delegates maintenance to STA)
│                        └─→ (delegates renovation to CON)
│
└─ Deal Sourcing Agent ──→ FINANCIAL AGENTS
                            ├─ Underwriting Agent ──→ Deal Structuring Agent
                            │                          │
                            │                          └─→ (hands off to INVESTMENT)
                            │
                            └─ (receives deal flow from RE, CON)

OPERATIONS AGENTS
├─ Legal Agent ←── (serves all ventures)
├─ Accounting Agent ←── (serves all ventures)
└─ HR Agent ←── (serves all ventures)

CROSS-FUNCTIONAL AGENTS
├─ Marketing Agent ←── (serves all ventures)
├─ Customer Success Agent ←── (serves all ventures)
└─ Data Analytics Agent ←── (serves all ventures)

HOLDING COMPANY AGENTS
├─ Network Operations Agent ←── (monitors all delegation flows)
├─ Capital Allocation Agent ←── (allocates capital to all ventures)
├─ Performance Analytics Agent ←── (aggregates KPIs from all ventures)
└─ Strategic Planning Agent ←── (sets priorities for all ventures)
```

---

## AGENT TRAINING DATA

Each agent reads these files to understand their role:

1. **AGENT-CATALOG.md** (this file) - Understands role, capabilities, handoffs
2. **INDUSTRY-PLAYBOOK.md** (sector-specific) - Understands business model, rules
3. **DELEGATION-RULES.md** - Understands handoff protocols, margin splits
4. **OPERATING-MODEL.md** - Understands approval chains, decision authority
5. **BUSINESS.md** - Understands holding company mission, vision

---

## NEXT STEPS

1. **Create individual agent files** for each of the 21 agents listed above
2. **Define MCP integrations** for each agent (APIs, tools, databases)
3. **Set up permission levels** in Supabase/Neo4j
4. **Train agents** on their playbooks, rules, and handoff protocols
5. **Test delegation flows** with CON-001 → STA-001 → RE-001 cycle
