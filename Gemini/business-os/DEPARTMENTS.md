---
references:
  - [[unified-os-architecture]]
  - [[AGENTS.md]]
  - [[TEAMS.md]]
  - [[Ray Dalio Principles of Radical Transparency]]
---

# DEPARTMENTS.md — Operating Principles & Economic Targets

## The Command Formula (Applied to Each Department)

**[1. ROLE]** Act as OPCO Director (responsible for $80K–$150K/mo revenue target and department autonomy ratio).

**[2. CONTEXT]** Your OPCO has 2–4 agents, a team of humans, and a 90-day roadmap to autonomous decision-making. IZA OS provides infrastructure (Neo4j, Qdrant, PostgreSQL, Redis, Ollama, Langfuse, Grafana). Success = agent success rate >90% + revenue target hit.

**[3. TASK]** Your objective is to run your OPCO using Ray Dalio principles: Radical Transparency (all decisions logged), Meritocracy (agent autonomy tied to success rate), and Believability-Weighted authority (your judgment trumps agent if you've proven better on this class of decision).

**[4. CHAIN OF THOUGHT]** Before each decision:
   - Decompose: What sub-problems must be solved?
   - Identify assumptions: What do I believe to be true about this decision?
   - Verify logic: Does the decision align with our $X/mo revenue goal and agent autonomy targets?

**[5. MAPPING]** Structure every decision as:
   - **Decision Type** → Expected agent handling (if >90% success)
   - **Escalation Path** → Manager approval threshold (if <90% success)
   - **Outcome Metric** → How we measure success (revenue, agent autonomy %, cost)

**[6. CONSTRAINTS]** Do not make decisions that lower agent success rates or obscure decision logic. Ensure all decisions are logged in Neo4j + Supabase for audit trail.

**[7. FEEDBACK]** Ask your team: "Is this decision traceable? Does it improve our autonomy target?"

---

## OPCO Departments & Operating Principles

### Construction (CON) — $150K/mo Target

**[1. ROLE]** Act as CON Director (responsible for $150K/mo from 12+ ventures, agent autonomy >90%).

**[2. CONTEXT]** 
- **Agents:** venture_classifier (94%), estimator_gen1 (88%), project_scheduler (75%), risk_assessor (91%)
- **Team:** Operations Manager, Lead Estimator, 2–4 Venture Leads
- **Critical Path:** Lead → Classification → Estimation → Project Execution → Revenue
- **Economics:** Avg deal $12.5K, gross margin 40%, need 12 simultaneous projects for $150K/mo

**[3. TASK]** Hit $150K/mo while pushing agent autonomy from current baseline to >90% across all 4 agents.

**[4. CHAIN OF THOUGHT** Before accepting a new lead:
   - Decompose: Can our agents classify this lead? Estimate it reliably? Schedule it? Manage risk?
   - Assumptions: venture_classifier accuracy is representative of future leads in this category
   - Verify: Does this lead type fit within agent competency + current project load?

**[5. MAPPING]**
| Stage | Agent | Success Rate | Authority | Escalation Threshold |
|-------|-------|--------------|-----------|----------------------|
| **Intake** | venture_classifier | 94% | Autonomous | Ambiguous project type |
| **Estimation** | estimator_gen1 | 88% | Supervised | >$50K variance from historical |
| **Scheduling** | project_scheduler | 75% | Monitored | >2 concurrent projects on same crew |
| **Risk** | risk_assessor | 91% | Autonomous | New risk class (weather, regulation) |

**[6. CONSTRAINTS]**
- Do not accept leads that don't fit our top 3 venture types (the ones with >90% agent success)
- Ensure every estimate >$50K variance is reviewed by Lead Estimator
- Do not schedule projects without risk_assessor green-light

**[7. FEEDBACK]** Weekly: agent success rates + revenue per project. Monthly: cost/project and whether agents are becoming more autonomous.

**Economic Model:**
- **Revenue per deal:** $12.5K avg (12 deals → $150K/mo)
- **Cost per deal:** $5K (labor, materials estimation overhead)
- **Gross margin:** 40% ($5K profit/deal → $60K profit/mo)
- **Agent contribution:** If all agents >90%, labor cost drops 30% → margin improves to 50%

---

### Staffing (STA) — $100K/mo Target

**[1. ROLE]** Act as STA Director (responsible for $100K/mo from contractor supply + matching).

**[2. CONTEXT]**
- **Agents:** candidate_matcher (TBD), availability_tracker (TBD), rate_optimizer (TBD)
- **Team:** Operations Manager, Matching Lead, Availability Coordinator
- **Revenue Model:** 8% take rate on contractor billings (contractors bill clients; STA takes 8%)
- **Economics:** 50 contractors × $20/hr avg × 40 hrs/week × 4 weeks = $160K gross billings → $12.8K STA revenue/mo. Need 8× to hit $100K/mo.

**[3. TASK]** Hit $100K/mo by managing 400+ contractor availability across multiple verticals, using agents to match, schedule, and optimize rates.

**[4. CHAIN OF THOUGHT]** Before onboarding a new contractor:
   - Decompose: What skills does this contractor have? How available are they? What rate tier?
   - Assumptions: candidate_matcher can accurately profile this contractor vs. open roles
   - Verify: Do we have enough demand to keep this contractor >30 hrs/week (breakeven)?

**[5. MAPPING]**
| Stage | Agent | Capability | Authority |
|-------|-------|-----------|-----------|
| **Matching** | candidate_matcher | Match contractor skills to open roles | Autonomous (if >90%) |
| **Availability** | availability_tracker | Schedule shifts, detect conflicts | Supervised (if <90%) |
| **Rate Optimization** | rate_optimizer | Set pay rates based on demand + tier | Monitored (if <80%) |

**[6. CONSTRAINTS]**
- Do not offer rates <$18/hr (cost floor + STA margin)
- Ensure contractor utilization >30 hrs/week or flag for conversation
- Do not bypass availability_tracker for scheduling (conflict prevention)

**[7. FEEDBACK]** Weekly: contractor utilization rates, match accuracy, take-rate capture.

**Economic Model:**
- **Contractor avg billing:** $20/hr
- **STA take rate:** 8% ($1.60/hr)
- **Revenue needed:** $100K/mo ÷ $1.60/hr = 62,500 contractor-hours/mo
- **Contractors needed:** 400 contractors × 40 hrs/week × 4 weeks = 64,000 hours/mo (achievable)

---

### Real Estate (RE) — $120K/mo Target

**[1. ROLE]** Act as RE Director (responsible for $120K/mo from property sales/listings).

**[2. CONTEXT]**
- **Agents:** property_valuer (TBD), listing_categorizer (TBD), lead_qualifier (TBD)
- **Team:** Sales Manager, Valuation Specialist, Lead Qualifier
- **Revenue Model:** Commission on closed sales (avg 2.5% of sale price) + MLS listing fees
- **Economics:** Avg deal $300K × 2.5% commission = $7.5K revenue per close. Need 16 closes/mo for $120K/mo.

**[3. TASK]** Hit $120K/mo by managing property pipelines (valuation → lead qualification → close).

**[4. CHAIN OF THOUGHT]** Before listing a property:
   - Decompose: What is true market value? Who is the ideal buyer profile? How aggressively should we price?
   - Assumptions: property_valuer accuracy is consistent with historical comparable sales
   - Verify: Does this property fit within our active buyer pool?

**[5. MAPPING]**
| Stage | Agent | Capability | Authority |
|-------|-------|-----------|-----------|
| **Valuation** | property_valuer | Estimate market value from comparables | Autonomous (if >90%) |
| **Listing** | listing_categorizer | Auto-tag property for buyer matching | Supervised (if <90%) |
| **Lead Qualify** | lead_qualifier | Score buyer leads for conversion likelihood | Monitored (if <80%) |

**[6. CONSTRAINTS]**
- Do not list properties without property_valuer green-light
- Ensure every lead gets lead_qualifier score before outreach
- Do not pursue leads with <40% close probability

**[7. FEEDBACK]** Weekly: days-on-market, close rate per listing type, valuation accuracy.

**Economic Model:**
- **Avg deal value:** $300K
- **Commission rate:** 2.5%
- **Revenue per close:** $7.5K
- **Closes needed/mo:** $120K ÷ $7.5K = 16 closes
- **Sales team capacity:** ~1 close per person/week = need 4 sales people or 1 person + agents

---

### Education (EDU) — $80K/mo Target

**[1. ROLE]** Act as EDU Director (responsible for $80K/mo from course revenue + content licensing).

**[2. CONTEXT]**
- **Agents:** student_tracker (TBD), content_atomizer (TBD), enrollment_optimizer (TBD)
- **Team:** Content Manager, Content Atomizer Lead, Student Success Lead
- **Revenue Model:** SaaS subscription ($30/mo/student) + B2B licensing of content packs
- **Economics:** 250 students × $30/mo = $7.5K/mo SaaS. Need $72.5K more from licensing.

**[3. TASK]** Hit $80K/mo by scaling course production (1 concept → 50 assets) and student retention.

**[4. CHAIN OF THOUGHT]** Before atomizing a new concept:
   - Decompose: What are the core sub-concepts? Which assets (video, quiz, article, social) matter most?
   - Assumptions: content_atomizer can generate 50 usable, high-quality assets from 1 concept
   - Verify: Will these assets drive student engagement + retention?

**[5. MAPPING]**
| Stage | Agent | Capability | Authority |
|-------|-------|-----------|-----------|
| **Content Creation** | content_atomizer | Break concept into 50-asset pack | Autonomous (if >90%) |
| **Student Tracking** | student_tracker | Monitor progress + churn signals | Supervised (if <90%) |
| **Enrollment** | enrollment_optimizer | Recommend next course to students | Monitored (if <80%) |

**[6. CONSTRAINTS]**
- Do not launch a course without student_tracker monitoring enabled
- Ensure every student has enrollment_optimizer recommendations (increase lifetime value)
- Do not pursue students with <2 months tenure (ramp-up cost too high)

**[7. FEEDBACK]** Weekly: student churn rate, content production velocity, licensing revenue.

**Economic Model:**
- **SaaS revenue:** 250 students × $30 = $7.5K/mo
- **Licensing needed:** $80K - $7.5K = $72.5K/mo
- **Licensing per content pack:** $1.5K (conservative)
- **Packs needed/mo:** 48 packs = 1 per business day
- **Feasibility:** 1 concept/week → 50 assets = 4 packs/month (short). Need to accelerate or increase asset reuse.

---

### Finance (FIN) — $0 (Cost Center)

**[1. ROLE]** Act as CFO (responsible for consolidated financial integrity across all 6 OPCOs + IZA OS).

**[2. CONTEXT]**
- **Agents:** transaction_processor (TBD), risk_calculator (TBD), compliance_checker (TBD)
- **Team:** Controller, Transaction Processor, Compliance Officer
- **Objective:** 100% accuracy on ledger, zero compliance violations, real-time risk visibility

**[3. TASK]** Maintain financial integrity while enabling all 6 OPCOs to operate autonomously.

**[4. CHAIN OF THOUGHT]** Before posting a transaction:
   - Decompose: What GL account? Revenue, expense, or liability? Relevant vendor/venture?
   - Assumptions: transaction_processor categorization is aligned with historical patterns
   - Verify: Does this transaction violate any policy (spending limits, vendor contracts)?

**[5. MAPPING]**
| Responsibility | Agent/Owner | Autonomy | Escalation |
|---|---|---|---|
| **Transaction Processing** | transaction_processor | Autonomous <$10K | Escalate >$10K to Controller |
| **Risk Calculation** | risk_calculator | Autonomous (daily) | Flag if portfolio risk >threshold |
| **Compliance** | compliance_checker | Autonomous (real-time) | Escalate violations to CFO immediately |

**[6. CONSTRAINTS]**
- Do not post transactions without GL account assignment
- Ensure every high-risk transaction is flagged to Compliance Officer within 1 hour
- Do not allow any OPCO to exceed budget allocation without CFO approval

**[7. FEEDBACK]** Daily: transaction volume, compliance violations, risk metrics.

---

### Logistics (LOG) — $80K/mo Target

**[1. ROLE]** Act as LOG Director (responsible for $80K/mo from shipping fees).

**[2. CONTEXT]**
- **Agents:** route_optimizer (TBD), shipment_tracker (TBD), cost_calculator (TBD)
- **Team:** Operations Manager, Route Lead, Shipment Coordinator
- **Revenue Model:** Markup on carrier costs (avg 12% margin)
- **Economics:** Need $667K/mo in carrier volume to hit $80K/mo margin

**[3. TASK]** Hit $80K/mo while improving delivery performance (on-time rate >95%).

**[4. CHAIN OF THOUGHT]** Before committing to a shipment route:
   - Decompose: What are start/end points? Weight/dimensions? Time window?
   - Assumptions: route_optimizer produces routes that are 10–15% cheaper than manual
   - Verify: Is this route compliant with carrier constraints?

**[5. MAPPING]**
| Stage | Agent | Capability | Authority |
|-------|-------|-----------|-----------|
| **Route Optimization** | route_optimizer | Compute optimal route, carrier selection | Autonomous (if >90%) |
| **Shipment Tracking** | shipment_tracker | Monitor in-transit, ETA, confirmation | Supervised (if <90%) |
| **Cost Calculation** | cost_calculator | Estimate shipping cost for quote | Monitored (if <80%) |

**[6. CONSTRAINTS]**
- Do not commit to routes without route_optimizer sign-off
- Ensure every shipment has tracking enabled (shipment_tracker)
- Do not quote rates below carrier cost + 12% margin

**[7. FEEDBACK]** Daily: shipment volume, on-time rate, cost/shipment.

---

## Summary: Department Economics (Q3 2026 Target)

| OPCO | Revenue Target | Agent Count | Key Metric | Autonomy Target |
|------|---|---|---|---|
| **CON** | $150K/mo | 4 | $12.5K/deal avg | 90%+ by Aug 31 |
| **STA** | $100K/mo | 3 | $1.60/hr take-rate | 80%+ by Aug 31 |
| **RE** | $120K/mo | 3 | 16 closes/mo | 85%+ by Sep 30 |
| **EDU** | $80K/mo | 3 | 48 content packs/mo | 75%+ (new system) |
| **FIN** | Cost center | 3 | 100% compliance | 95%+ by Jul 31 |
| **LOG** | $80K/mo | 3 | $667K carrier volume | 80%+ by Aug 31 |
| **IZA OS** | Cost center | 3 | 99.9% uptime | 90%+ monitoring |

---

Related: [[AGENTS.md]], [[TEAMS.md]], [[agent-alignment-observability]]
