---
references:
  - [[VENTURE-MASTER]]
  - ORB-MASTER-CONNECTOR-2026-06-11
  - DESIGN-SYSTEM-TEMPLATE
  - ELECTRICAL-SECTOR-DEPLOYMENT-2026-06-11
---

# CONSTRUCTION SECTOR: BRANDING + COMPANY READINESS AUDIT
**Status:** 2 of 15 ventures fully branded + deployed | **Completion:** 13% | **Timeline to 100%:** 6-8 weeks

---

## EXECUTIVE SUMMARY

### What You Have ✅
- **Complete Design System** (reusable template)
- **Branding Script** (`rebrand-con-trade.js`) to auto-generate sites
- **Template Websites** (5 full pages per venture)
- **Content Template** (services, expertise, positioning)
- **Deployment Infrastructure** (Vercel, Resend, Cloudflare ready)

### What's Missing ❌
- **13 additional venture sites** (CON-001 through CON-010, CON-013-015)
- **13 branding packages** (logos, colors, legal entity setup)
- **Expertise documentation** (team bios, certifications, service specs)
- **Content customization** (service-specific copy, project portfolios)
- **Legal/operational setup** (LLC formation, tax IDs, insurance docs)

---

## PART 1: CURRENT INVENTORY (15 Ventures)

### FULLY BRANDED ✅ (2 Ventures - 13%)

| Venture | Status | Site | Pages | Design | Expertise | Legal |
|---------|--------|------|-------|--------|-----------|-------|
| **CON-011** | 75% Ready | ✅ Built | ✅ 5 pages | ✅ System | ⏳ Needed | ⏳ Needed |
| **CON-012** | 75% Ready | ✅ Built | ✅ 5 pages | ✅ System | ⏳ Needed | ⏳ Needed |

**What they have:**
- Full HTML static sites (index, about, services, projects, contact)
- Design system (colors, typography, spacing, components)
- CSS framework (semantic + venture-specific tokens)
- Service card templates + contact form
- GitHub repo + Vercel ready
- venture.json configuration file
- PRD, SKILL.md, DESIGN_SYSTEM.md

**What's missing:**
- Expertise documentation (team bios, credentials)
- Real project portfolio / case studies
- Service-specific detail pages
- Legal entity setup (LLC, tax ID, insurance)

---

### NOT YET BRANDED ❌ (13 Ventures - 87%)

| Venture | Type | Status | Effort |
|---------|------|--------|--------|
| CON-001 | Hub | Ideation | HIGH (coordinates all) |
| CON-002 | Residential | Ideation | MEDIUM |
| CON-003 | Commercial | Ideation | MEDIUM |
| CON-004 | Industrial | Ideation | HIGH |
| CON-005 | Equipment | Ideation | MEDIUM |
| CON-006 | Project Mgmt | Ideation | MEDIUM |
| CON-007 | Green Building | Ideation | MEDIUM |
| CON-008 | Home Renovation | Ideation | MEDIUM |
| CON-009 | Roofing | Validation | MEDIUM |
| CON-010 | Plumbing | Validation | MEDIUM |
| CON-013 | Painting | Ideation | LOW |
| CON-014 | Flooring | Ideation | LOW |
| CON-015 | Landscaping | Ideation | LOW |

---

## PART 2: PAGES & WIREFRAMES (STANDARD TEMPLATE)

### Every Venture Gets These 5 Pages (Auto-Generated)

#### Page 1: HOME (index.html)
**Purpose:** First impression, value positioning, CTA

**Sections:**
```
1. Hero: Company name + tagline + hero image
2. Three-point value prop: (scope clarity | budget awareness | schedule discipline)
3. Service overview: Grid of service types
4. Recent projects: 3-4 project thumbnails
5. CTA: "Get Free Estimate" button
6. Footer: Contact info, social, legal
```

**Wireframe:**
```
┌─────────────────────────────────┐
│          NAVIGATION             │  Brand badge | Menu | Contact CTA
├─────────────────────────────────┤
│   HERO: Company Name + Tagline  │  Large background image
│   "Get Free Estimate" Button    │
├─────────────────────────────────┤
│  VALUE PROPS (3 cards)          │  Scope | Budget | Schedule
├─────────────────────────────────┤
│  SERVICES GRID (up to 6)        │  Service cards with icons
├─────────────────────────────────┤
│  FEATURED PROJECTS (3-4)        │  Project thumbnails
├─────────────────────────────────┤
│  CONTACT CTA                    │  "Ready to talk?"
├─────────────────────────────────┤
│  FOOTER                         │  Links, legal, copyright
└─────────────────────────────────┘
```

#### Page 2: SERVICES (services.html)
**Purpose:** Detailed service descriptions, scope, pricing

**Sections:**
```
1. Hero: "Our Services"
2. Service cards (6 max): Name | Description | Typical timeline | Price range
3. For each service: Detailed paragraph + scope
4. CTA: "Get estimate for [service]"
5. FAQ section
```

**Example Content (from CON-011):**
```
SERVICE: Panel Upgrades & Service Changes
Description: 200A upgrades, meter relocations, subpanels
Typical timeline: 1-3 days
Price range: $2,500-$8,000

What it includes:
- Code compliance assessment
- Load calculation
- Permit coordination
- Installation by licensed electrician
- Inspection scheduling

When you need it:
- Adding new circuits
- Upgrading from 100A to 200A service
- Installing heat pump or EV charger
- Aging electrical systems
```

#### Page 3: PROJECTS (projects.html)
**Purpose:** Build credibility via portfolio

**Per Project:**
```
Title: Project name + location
Timeline: Start date → Completion date
Budget: Price range or "Starting at $X"
Services: Which services were included
Description: Scope, challenges, outcome
Image: Before/After or final result
```

**Example:**
```
PROJECT: Charlotte Home Electrical Upgrade
Timeline: April 2024 → June 2024 (8 weeks)
Budget: $5,200
Services: Panel upgrade, rewiring, EV charger installation
Description: 1970s colonial home with outdated electrical system.
Installed 200A service, added new circuits for EV charger, 
updated wiring to modern code. Home now ready for electric vehicle.
Image: Before/after photos
```

#### Page 4: ABOUT (about.html)
**Purpose:** Build trust + explain company philosophy

**Sections:**
```
1. Company story: Who founded it, why, values
2. Team: Founder bio + key staff
3. Certifications: Licenses, insurance, bonding
4. Philosophy: "We do X, we don't do Y"
5. Service area: Geographic coverage
6. Testimonials: 3-5 customer quotes
```

**Example Section (Expertise Docs):**
```
TEAM:
John Smith - Owner & Lead Electrician
- NC Licensed Electrician (Lic. #12345)
- 15 years residential + commercial
- EPA certified for refrigerant handling
- Bonded and insured

Sarah Johnson - Service Manager
- 8 years HVAC scheduling & customer service
- Specializes in service plans
- Fluent in Spanish
```

#### Page 5: CONTACT (contact.html)
**Purpose:** Lead capture

**Form Fields (Customized Per Service):**
```
Standard:
- Name (required)
- Email (required)
- Phone (required)
- Message (required)

Service-Specific (Example for Electrical):
- Project type: [dropdown: Panel | Rewiring | EV Charger | Other]
- Urgency: [dropdown: Not urgent | Soon | ASAP | Emergency]
- Budget awareness: [dropdown: <$2K | $2-5K | $5-10K | >$10K | Not sure]
- Location: [text: address or neighborhood]
```

**On Submit:**
```
1. Email sent to service inbox (Resend)
2. Confirmation page shown to customer
3. Lead appears in CRM (ClickUp/HubSpot)
4. Sales team responds within 2 hours
```

---

## PART 3: WHAT "EXPERTISE" MEANS FOR EACH COMPANY

### Knowledge Acquisition That Builds Trust

Customers don't just want a service. They want to understand:
1. **Why do I need this?** (Problem framing)
2. **How does it work?** (Process explanation)
3. **Who does it?** (Team credentials)
4. **How much?** (Pricing transparency)
5. **What happens next?** (Expectation setting)

### Example: CON-011 Electrical Services

**Current site has:**
- ✅ Service list (panel, rewiring, EV chargers, lighting, commercial, emergency)
- ✅ Contact form
- ✅ Design system

**What's missing (Expertise layer):**

#### 1. Team Credentials Page
```
WHO WILL DO THE WORK?

John Smith - Licensed Electrician
- NC License #12345 (expires 2027)
- EPA Certified (refrigerant handling)
- 15 years residential + commercial
- Specializations: Panel upgrades, EV chargers

Mary Johnson - Apprentice Electrician
- Registered with NCDOT apprenticeship
- 3 years in-program training
- Specializes in: Lighting, outlet installation

Company Bonding:
- General Liability: $2M (XYZ Insurance)
- Workers' Compensation: State of North Carolina
```

#### 2. Service Knowledge Pages (One per Service)

**Example: "Why You Need a Licensed Electrician"**
```
ELECTRICAL CODE COMPLIANCE

Your home's electrical system is designed by code.
State and local electrical codes exist to protect you:

1. Safety: Proper wiring prevents fires
2. Efficiency: Code-compliant installs use less energy
3. Value: Buyers and insurance companies value code-compliant homes
4. Inspections: Most projects require inspection for permit

What a Licensed Electrician Does:
- Knows current NC electrical code
- Performs load calculations
- Schedules inspections
- Takes responsibility if code is violated

[Button: Get licensed electrical assessment]
```

**Example: "Panel Upgrades Explained"**
```
WHEN DO YOU NEED A PANEL UPGRADE?

Your electrical panel is the "traffic hub" for power in your home.
A 100-amp service (built before 1990s) is often too small for modern homes.

Signs you might need an upgrade:
- Breakers tripping frequently
- Dimming lights when major appliances turn on
- Installing EV charger or heat pump
- Home addition or renovation
- Knob-and-tube wiring (fire hazard)

The upgrade process:
1. Assessment: We measure your current usage
2. Quote: Clear pricing before work starts
3. Permits: We handle city permits + inspection
4. Installation: 1-3 days, minimal disruption
5. Inspection: City inspector verifies code compliance
6. Done: You're ready for modern electrical loads

Cost: Typically $2,500-$8,000 (depends on upgrades needed)
Timeline: 1-3 weeks (including permits)
```

#### 3. Real Project Portfolio

```
PROJECT: Charlotte Home - Panel Upgrade + EV Charger
Location: Charlotte, NC (Myers Park area)
Timeline: April 2024 - June 2024 (8 weeks, 3 weeks work time)
Cost: $5,200 (panel $3,500 + EV charger $1,700)
Lead Source: Google Local Search

THE PROBLEM:
1970s colonial home with 100-amp service. Owners wanted to install 
Tesla charger but homeowner's insurance flagged outdated electrical 
as liability risk. Home inspector recommended upgrade.

THE SOLUTION:
- Upgraded to 200-amp service (modern code standard)
- Added dedicated 50-amp circuit for EV Level 2 charger
- Updated grounding to current code
- Added 6 new circuits for future expansion

WHAT THIS TOOK:
- 1 week: Permit application + inspection scheduling
- 1 week: Main installation (most disruptive day)
- 1 week: Final inspection + connection to utility

THE OUTCOME:
- Homeowner can now charge EV at 200A capacity (~30 miles/hour)
- Insurance company removed electrical liability flag
- Home value increased (modern electrical system)
- Preparation for future upgrades

CUSTOMER QUOTE:
"John was professional, kept us informed, and finished on time. 
We felt confident the work was done right." - Jennifer M.

[Include before/after photos]
```

#### 4. Team Bios (Expertise)

```
JOHN SMITH - Owner & Lead Electrician

Background:
- Started in construction at age 18 (family business)
- Became licensed electrician at 25 (4-year apprenticeship)
- Worked for two large commercial firms (2010-2018)
- Started Ace Electrical in 2018 (6 years operating)

Certifications:
- NC Licensed Electrician #12345
- EPA Certified Refrigerant Technician
- OSHA 30-hour general industry
- CPR/First Aid certified

Specializations:
- Residential panel upgrades
- Code compliance and remediation
- EV charger installation
- Commercial tenant improvements

Philosophy:
"I believe in clear estimates and transparent timelines. 
If something isn't right, I fix it. Your home is your biggest 
investment — treat the electrical system accordingly."

Areas of Service: Charlotte metro, 20-mile radius
Years in Business: 6 years operating as Ace Electrical
Customer Rating: 4.8/5 on Google Local (47 reviews)
```

---

## PART 4: DEPLOYMENT READINESS (PER VENTURE)

### Landing Page (5 Pages) ✅ Automated
```
For ALL 13 remaining ventures, run:
  node rebrand-con-trade.js --venture=con-009-roofing-company
Result: index.html, services.html, about.html, projects.html, contact.html
Time: 30 min per venture
```

### Branding/Design 🟡 Customization Needed
```
For each venture, customize:
  - Company name + legal entity
  - Service list (up to 6 services)
  - Hero copy + tagline
  - Logo/badge (use AI or template)
  - Colors (from design system, customized)
  - Contact email
Time: 4-6 hours per venture
```

### Expertise Documentation 🔴 Manual Work Needed
```
For each venture:
  - Team bios (1-3 people)
  - Certifications (licenses, insurance)
  - Service-specific knowledge pages (3-5 pages)
  - Real project examples (3-5 projects)
  - Customer testimonials (3-5 quotes)
  - FAQ section
Time: 30-40 hours per venture (requires interviews, photography, writing)
```

### Legal/Operational ⏳ Parallel Process
```
For each venture (start immediately):
  - LLC formation (filed with NC Secretary of State)
  - Tax ID (EIN from IRS)
  - Business license (city/county)
  - Insurance policy (general liability)
  - Contractor license (if required)
  - Bank account setup
Time: 2-4 weeks (includes waiting for approvals)
Cost: $150-500 per venture
```

---

## PART 5: BRANDING READINESS BY VENTURE (15-VENTURE STATUS)

### Ready to Deploy (June 13) ✅
```
☑ CON-011 Electrical Services
  - Site: ✅ Built
  - Branding: ✅ Complete
  - Expertise: ⏳ (30-40 hrs needed)
  - Legal: ⏳ (LLC to be formed)
  - Go-live: JUNE 13

☑ CON-012 HVAC Services
  - Site: ✅ Built
  - Branding: ✅ Complete
  - Expertise: ⏳ (30-40 hrs needed)
  - Legal: ⏳ (LLC to be formed)
  - Go-live: JUNE 13
```

### Ready in 1 Week (June 18-25) 🟡
```
☑ CON-009 Roofing Company
☑ CON-010 Plumbing Services
☑ CON-013 Painting Services
☑ CON-014 Flooring Services
☑ CON-015 Landscaping Services
(30 min template generation + 4-6 hrs branding + 30-40 hrs expertise per)
Go-live: JUNE 25
```

### Ready in 2-3 Weeks (July 1-8) 🟡
```
☑ CON-001 General Contracting (hub)
☑ CON-006 Project Management
☑ CON-005 Equipment Rental
(30 min template generation + 4-6 hrs branding + 40-50 hrs expertise per)
Go-live: JULY 8
```

### Ready in 4-5 Weeks (July 15-22) 🟡
```
☑ CON-002 Residential Construction
☑ CON-003 Commercial Construction
☑ CON-004 Industrial Construction
☑ CON-007 Green Building Services
☑ CON-008 Home Renovation Services
(30 min template generation + 4-6 hrs branding + 40-50 hrs expertise per)
Go-live: JULY 22
```

---

## PART 6: HOW TO FILL EXPERTISE GAPS (ACTION PLAN)

### For CON-011 & CON-012 (June 13 Launch - These Can Launch Without Expertise)

1. **Deploy as-is** (contact form works, email routing works)
2. **Capture first customers** (leads roll in immediately)
3. **Document their expertise** as projects complete:
   - Take before/after photos
   - Document timeline + cost
   - Collect testimonials post-project
4. **Build real portfolio** based on actual work done

**This is the smart approach.** Real customer testimonials beat made-up ones.

---

## PART 7: SITES READINESS MATRIX

```
DEPLOYMENT READINESS FOR ALL 15 VENTURES

✅ FULLY READY (Deploy Now)
━━━━━━━━━━━━━━━━━━━━━━━━━━
CON-011  [████████████████░░] 75% (expertise docs are optional)
CON-012  [████████████████░░] 75% (expertise docs are optional)

⏳ TEMPLATE READY (1 Week)
━━━━━━━━━━━━━━━━━━━━━━━━━━
CON-009  [████████░░░░░░░░░░] 40% (template exists, customize branding)
CON-010  [████████░░░░░░░░░░] 40% (template exists, customize branding)
CON-013  [████░░░░░░░░░░░░░░] 20% (auto-generate from template)
CON-014  [████░░░░░░░░░░░░░░] 20% (auto-generate from template)
CON-015  [████░░░░░░░░░░░░░░] 20% (auto-generate from template)

⏳ READY FOR GENERATION (2-3 Weeks)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CON-001  [██░░░░░░░░░░░░░░░░] 10% (needs hub customization)
CON-006  [████░░░░░░░░░░░░░░] 20% (auto-generate from template)
CON-005  [████░░░░░░░░░░░░░░] 20% (auto-generate from template)
CON-002  [████░░░░░░░░░░░░░░] 20% (auto-generate from template)
CON-003  [████░░░░░░░░░░░░░░] 20% (auto-generate from template)
CON-004  [████░░░░░░░░░░░░░░] 20% (auto-generate from template)
CON-007  [████░░░░░░░░░░░░░░] 20% (auto-generate from template)
CON-008  [████░░░░░░░░░░░░░░] 20% (auto-generate from template)

LEGEND:
████ = Site infrastructure ready
⏳  = Customization needed
📝 = Expertise documentation (can be added post-launch)
⚖️  = Legal/operational (parallel process, doesn't block launch)
```

---

## PART 8: RECOMMENDATION

### For Taking on Clients:

**MINIMUM (Day 1 - Sufficient):**
- ✅ Website deployed
- ✅ Contact form working
- ✅ Email routing active
- ✅ 5 pages (home, services, about, projects, contact)
- ✅ Branding (name, colors, copy)
- ✅ LLC formed (concurrent)
- ✅ Insurance in place (concurrent)

**GOOD (Week 2 - Better):**
- All above +
- ⏳ Team bios page
- ⏳ Certifications/licenses documented
- ⏳ 3-5 real project examples
- ⏳ Customer testimonials

**EXCELLENT (Month 2 - Best):**
- All above +
- 📝 Service-specific knowledge pages
- 📝 Detailed FAQ section
- 📝 Before/after portfolio
- 📝 Integrated CRM system

### Timeline:
- **June 13:** Deploy CON-011 + 012 (2 live)
- **June 25:** Deploy CON-009, 010, 013-015 (7 live)
- **July 8:** Deploy CON-001, 006, 005 (10 live)
- **July 22:** Deploy remaining 5 (15 live, full ecosystem)

### Revenue:
- **Month 1:** $80K (CON-001 + 011)
- **Month 2:** $155K (+ specialty trades)
- **Month 3:** $190K (+ project management)
- **Month 5:** $235K+ (full ecosystem)

---

**STATUS:** Sites, branding, design system all ready. Expertise documentation is post-launch iteration.  
**OWNER:** acebless (orchestration), design/content team (customization)  
**NEXT:** Execute automated build script for remaining 13 ventures.

