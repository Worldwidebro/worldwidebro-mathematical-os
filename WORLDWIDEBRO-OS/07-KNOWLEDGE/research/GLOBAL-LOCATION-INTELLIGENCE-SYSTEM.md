# Global Location Intelligence System

**Purpose:** Map the world as a network of optimization nodes for Worldwidebro's 712 ventures + personal strategy

**Status:** Framework in progress (awaiting personal constraints)

---

## PART A: LOCATION ATTRIBUTES SCHEMA

Every location is scored on 20+ dimensions:

### ECONOMIC TIER (Revenue Opportunity)

1. **Wage Arbitrage** — Local wages vs. global market
   - Example: Dev in Bali ($800/mo) vs. SF ($150K/yr)
   - Relevant for: Service ventures, talent recruitment, labor arbitrage

2. **Startup Ecosystem Strength** — Maturity of business environment
   - Scoring: Tier 1 (SF, NYC, London) → Tier 4 (emerging)
   - Relevant for: Company formation, investor access, networking

3. **Industry Specialization** — What the location is known for
   - Example: Tokyo (manufacturing), Bangalore (tech), Miami (finance)
   - Relevant for: Venture placement, talent matching

4. **Capital Availability** — Access to funding
   - Local VCs, angel networks, SBA equivalents
   - Relevant for: Scaling ventures, raising capital

### COST TIER (Operating Expense)

5. **Cost of Living Index** (1-100, where 100 = NYC)
   - Housing, food, transport, utilities
   - Example: Lisbon (35) vs. San Francisco (100)

6. **Effective Tax Rate** — Income + corporate taxes combined
   - Relevant for: Profit optimization, HQ location

7. **Real Estate** — Office/manufacturing/housing costs
   - Per sq ft/month residential vs. commercial
   - Relevant for: HQ setup, manufacturing, scaling

8. **Talent Acquisition Cost** — What you pay to hire locally
   - Salary expectations, benefits, compliance
   - Relevant for: Team building, operational costs

### BUSINESS TIER (Execution Ease)

9. **Ease of Company Formation** — Time + cost to register LLC/Corp
   - Example: Delaware (24 hours, $200) vs. India (30 days, $3K)
   - Relevant for: Venture launch speed

10. **Banking Infrastructure** — Account opening, international transfers
    - Speed, fees, regulatory complexity
    - Relevant for: Cash flow, operations

11. **Regulatory Compliance** — Labor laws, liability, tax reporting
    - Complexity score (1=simple, 5=nightmare)
    - Relevant for: Risk management

12. **Government Support** — Grants, incentives, visa programs
    - Tax breaks, startup visas, subsidies
    - Relevant for: Capital efficiency

### LIFESTYLE TIER (Personal Quality)

13. **Quality of Life Index** — Healthcare, education, safety, culture
    - Combines Numbeo, UN Development Index
    - Relevant for: Personal relocation decisions

14. **Climate/Weather** — Average temps, humidity, seasons
    - Relevant for: Personal preference, health

15. **Language Barrier** — English prevalence, expat community
    - Relevant for: Ease of relocation

16. **Internet Quality** — Speed, reliability, cost
    - Measured: Mbps, uptime %, latency
    - Critical for: Remote work

### INFRASTRUCTURE TIER (Operational Capability)

17. **Transportation Hub Status** — Flights, trains, ports
    - Example: Singapore (massive hub) vs. rural Montana (none)
    - Relevant for: Supply chain, travel efficiency

18. **Power Reliability** — Uptime %, brownouts
    - Critical for: Manufacturing, data centers

19. **Timezone** — UTC offset from markets you serve
    - Relevant for: Customer service, team coordination

### RISK TIER (Downside Protection)

20. **Political Stability** — Government consistency, coup risk
    - Measured: Political risk index (0=safest, 10=dangerous)

21. **Crime Rate** — Personal safety, theft, fraud
    - Per capita incidents, tourist safety ratings

22. **Natural Disaster Risk** — Earthquakes, hurricanes, floods
    - Frequency + severity

23. **Regulatory Risk** — Sudden law changes that hurt business
    - Example: Crypto bans, visa restrictions, tax audits

24. **Currency Stability** — FX volatility vs. USD
    - Relevant for: Revenue stability, pricing

---

## PART B: THE OPTIMIZATION PROBLEM

**Goal:** Assign each venture to the location that maximizes:

```
Score = (Revenue Opportunity × Venture Type)
       - (Operating Costs × Cost Sensitivity)  
       + (Strategic Advantage × 1.5)
       - (Risk × Risk Tolerance)
```

**Venture Types & Their Location Preferences:**

| Venture Type | Cost Priority | Opportunity Priority | Location Profile |
|--------------|---------------|----------------------|------------------|
| **Service** (labor arbitrage) | 🔴 Critical | 🟡 Medium | Low-cost + English speaking |
| **SaaS** (global digital) | 🟡 Medium | 🔴 Critical | Startup hub + talent + timezone |
| **Manufacturing** | 🔴 Critical | 🟡 Medium | Low-cost manufacturing + ports |
| **Content** (digital media) | 🟢 Low | 🔴 Critical | Good internet + lifestyle |
| **Capital/Finance** | 🟢 Low | 🔴 Critical | Major financial centers |

---

## PART C: TOP 5 CANDIDATE HUB LOCATIONS

*Pending your personal constraints, analyzing:*

### HUB 1: Remote Work + Service Ops (Low-Cost Base)
**Candidates:** Lisbon, Chiang Mai, Bali, Mexico City, Buenos Aires

**Profile needed:**
- Cost of living: <$2K/month for comfortable lifestyle
- Timezone: Americas-friendly or UTC+0 (bridges both)
- Internet: 50+ Mbps reliable
- Visa: Nomad visa or easy tourist extensions
- English: Medium-high prevalence
- Services: Coworking, restaurants, community

**Venture fit:** Service ventures (staffing, consulting), content creation, remote-first SaaS teams

---

### HUB 2: Manufacturing + Logistics (Low-Cost + Infrastructure)
**Candidates:** Vietnam, Poland, Mexico, India, Romania

**Profile needed:**
- Cost of labor: <$400/month skilled workers
- Manufacturing base: Existing supply chains
- Ports/logistics: Access to shipping
- Regulatory: Favorable trade status
- Quality: Reliable production

**Venture fit:** E-commerce, product manufacturing, fulfillment

---

### HUB 3: Capital + Finance (High-Opportunity)
**Candidates:** Singapore, Miami, Dubai, Hong Kong, London

**Profile needed:**
- Banking: Easy business accounts, forex, international transfers
- Capital: VC access, angel networks, family offices
- Regulatory: Crypto-friendly or crypto-neutral
- Tax: Favorable for wealth accumulation
- Network: World-class talent, investors

**Venture fit:** Trading, acquisitions, capital management, investment ventures

---

### HUB 4: SaaS + Talent (High-Opportunity)
**Candidates:** Berlin, Austin, Toronto, Dubai, Singapore

**Profile needed:**
- Startup ecosystem: VCs, accelerators, founder community
- Talent pool: Deep developer, designer, PM populations
- Cost: Mid-range (not SF cheap)
- Regulatory: Immigration-friendly for top talent
- Culture: Innovation-focused

**Venture fit:** Tech SaaS, digital products, marketplace platforms

---

### HUB 5: Personal Base (Optimization for YOU)
**Candidates:** TBD based on your constraints

**Profile needed:**
- Quality of life: Healthcare, education, culture, climate
- Cost: Sustainable long-term
- Timezone: Works with your natural rhythm
- Community: Friends, family, or expat network
- Visa: Long-term residency or citizenship path

**Venture fit:** HQ location, family stability, life design

---

## PART D: VENTURE-TO-LOCATION MAPPING FRAMEWORK

**Question:** Of your 712 ventures, how many in each category?

```
712 Total Ventures
├── Service (labor arbitrage)? ___ ventures
│   └── → Hub 1 (Low-cost base)
├── SaaS/Digital (global)? ___ ventures
│   └── → Hub 3 or 4 (Capital or Talent)
├── Manufacturing/E-commerce? ___ ventures
│   └── → Hub 2 (Manufacturing)
├── Content/Community? ___ ventures
│   └── → Hub 1 (Remote-friendly)
└── Capital/Investment? ___ ventures
    └── → Hub 3 (Finance)
```

**Mapping logic:**
1. Classify each venture by primary revenue model
2. Match to location where ROI is highest
3. Create "venture clusters" (5-10 ventures per location, shared ops)
4. Minimize operating costs, maximize revenue opportunity

**Example:** Your roofing company (CON-009) might be:
- HQ'd in Miami (Hub 3: capital + finance hub)
- Operations in Mexico (Hub 2: low-cost labor)
- Serving US markets (timezone-friendly, large market)

---

## PART E: PERSONAL 6-MONTH LOCATION STRATEGY

**Framework:** Where should YOU be for the next 6 months?

**Months 1-2 (Setup Phase):**
- Base location: _____________
- Purpose: OPTION 3 execution (ecosystem mapping)
- Requirement: Stable, predictable, low distractions
- Suggested: Where you are now OR close to current

**Months 3-4 (Execution Phase):**
- Base location: _____________
- Purpose: OPTION 1-2 execution (clarity + launch machine)
- Requirement: Good internet, some community, business-friendly
- Opportunity: Can relocate if needed

**Months 5-6 (Scaling Phase):**
- Base location: _____________
- Purpose: Scale what works, operate from optimal location
- Requirement: Support multiple ventures, capital access
- Opportunity: Experiment with location that maximizes ROI

---

## NEXT STEPS

To build complete system, I need:

1. **Current situation:**
   - Where are you now?
   - Family/dependents? (affects location selection)
   - Any location constraints? (must stay in US, can't move, etc.)

2. **Venture breakdown:**
   - Of 712 ventures, estimate distribution:
     - % Service-based?
     - % Digital/SaaS?
     - % Manufacturing/E-commerce?
     - % Content/Community?
     - % Capital/Investment?

3. **Personal priorities (rank 1-5):**
   - Cost minimization
   - Opportunity maximization
   - Quality of life
   - Family/education
   - Business networking

4. **Timeline:**
   - Can relocate in 30 days? 90 days? 6 months?
   - How long stay in one place?

---

**System Framework:** ✅ Complete

**Pending:** Your inputs → Will generate complete location mapping

---

Once you provide those inputs, I will create:
1. ✅ 5 Hub Location Profiles (detailed scoring)
2. ✅ Venture-to-Location Matrix (which ventures go where)
3. ✅ Personal 6-Month Location Strategy (month-by-month)
4. ✅ Operating Model Integration (how hubs work together)
5. ✅ Relocation Checklist (if you move)

