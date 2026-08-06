---
name: HRMS-SECTOR-CREWS
title: HRMS Sector Crews & Team Organization
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# HRMS Sector Crews & Team Organization

**Target**: May 13-20, 2026 (Parallel to blockers)  
**Goal**: 17 sector teams ready for launch, each with crew lead + 2-3 implementation partners  
**Total Crew Size**: ~50 people (1 PM lead + 3 crew members × 17 sectors, minus overlaps)

---

## 🏗️ Sector Crew Structure

Each sector has:
- **1 Sector Lead (PM)** — Already assigned in Paperclip (CEO, CTO, CFO, plus 1 TBD)
- **1 Implementation Lead** — Handles technical setup for ventures in sector
- **2-3 Customer Success Reps** — Onboarding + support for paying customers
- **1 Sales Rep** — Outbound to target companies in sector

### Tier 1 Sectors (Largest Market + Most Urgent)

#### 1. **Construction** (100 ventures, $2-5K MRR potential)
- **Sector Lead**: *Assigned TBD* (recruiting from construction software background)
- **Implementation Lead**: Need hire/contractor (Raken, Procore, Toast experience)
- **CS Reps**: 2 (construction-familiar)
- **Sales Rep**: 1 (B2B SaaS + construction)
- **Target Companies**: General contractors, subcontractors, field crews (50-500 employees)
- **Key Features**: Multi-location, crew scheduling, tax-compliant withholding

#### 2. **Logistics** (85 ventures, $1.5-3K MRR potential)
- **Sector Lead**: *Assigned TBD*
- **Implementation Lead**: Need hire (routing, fleet, dispatch software background)
- **CS Reps**: 2 (logistics-familiar)
- **Sales Rep**: 1
- **Target Companies**: 3PLs, trucking companies, delivery networks (30-300 employees)
- **Key Features**: Multi-site payroll, shift patterns, real-time tracking integration

#### 3. **Field Services** (90 ventures, $1.5-3K MRR potential)
- **Sector Lead**: *Assigned TBD*
- **Implementation Lead**: Need hire (ServiceTitan, Jobber, Angi experience)
- **CS Reps**: 2
- **Sales Rep**: 1
- **Target Companies**: HVAC, plumbing, electrical, landscaping contractors (20-200 employees)
- **Key Features**: Technician assignment, travel time, job costing, compliance

#### 4. **Healthcare Services** (70 ventures, $2-4K MRR potential)
- **Sector Lead**: *Assigned TBD*
- **Implementation Lead**: Need hire (medical staffing, clinic software experience)
- **CS Reps**: 2 (healthcare-sensitive)
- **Sales Rep**: 1
- **Target Companies**: Home health agencies, clinics, staffing (40-300 employees)
- **Key Features**: License/credential tracking, shift differentials, HIPAA-aware

### Tier 2 Sectors (Growth Opportunity)

#### 5. **E-Commerce / Fulfillment** (120 ventures, $1-3K MRR potential)
- Implementation Lead: Need hire
- CS Reps: 2
- Sales Rep: 1

#### 6. **Hospitality & Food Service** (95 ventures, $1-2K MRR potential)
- Implementation Lead: Need hire (Toast, Square experience)
- CS Reps: 2
- Sales Rep: 1

#### 7. **SaaS / Tech Services** (80 ventures, $2-5K MRR potential)
- Implementation Lead: Need hire
- CS Reps: 2
- Sales Rep: 1

#### 8. **Manufacturing & Production** (75 ventures, $2-4K MRR potential)
- Implementation Lead: Need hire
- CS Reps: 2
- Sales Rep: 1

#### 9. **Real Estate / Property Management** (65 ventures, $1.5-3K MRR potential)
- Implementation Lead: Need hire
- CS Reps: 2
- Sales Rep: 1

#### 10-17. **Other 8 Sectors** (312 ventures combined)
- Consolidate into 3-4 regional crews
- Each handles 3-4 sectors with shared resources

---

## 📋 Crew Onboarding Checklist

### Phase 1: Sector Lead Onboarding (Days 1-2)
**Owner**: CEO agent  
**Duration**: 2 days  
**Deliverables**: Sector playbook + KPI dashboard

- [ ] **Day 1: Context & Tools**
  - [ ] Access to Paperclip (with sector dashboard)
  - [ ] Access to Supabase (venture metrics)
  - [ ] Review: All 892 venture definitions + 17 sector templates
  - [ ] Training: HRMS product, compliance requirements
  - [ ] Training: Salesforce/Pipedrive CRM basics

- [ ] **Day 2: Planning & Targets**
  - [ ] Review: Sector profitability model (CAC, LTV, margins)
  - [ ] Set: Monthly customer acquisition target (e.g., 5-10 for Tier 1)
  - [ ] Review: Risk factors (e.g., construction seasonality, healthcare licensing)
  - [ ] Decision: Prioritize 20 pilot ventures within sector
  - [ ] Schedule: Weekly standup (same time weekly)

**Success Criteria**: 
- ✅ Can access all systems
- ✅ Understands KPI targets
- ✅ Has identified 20 pilot ventures
- ✅ Knows weekly reporting cadence

---

### Phase 2: Implementation Lead Onboarding (Days 1-3)
**Owner**: CTO agent  
**Duration**: 3 days  
**Deliverables**: Technical setup playbook + integration checklist

- [ ] **Day 1: Product Deep Dive**
  - [ ] Access to HRMS codebase (GitHub)
  - [ ] Training: Core payroll logic (tax withholding, deductions, net pay)
  - [ ] Training: Multi-location setup
  - [ ] Training: API integrations (Stripe, ADP, QuickBooks)
  - [ ] Review: Compliance checklist (state/federal requirements)

- [ ] **Day 2: Integration Patterns**
  - [ ] Document: How to connect Stripe to ventures
  - [ ] Document: How to map existing payroll to HRMS
  - [ ] Document: How to migrate 5 pilot ventures
  - [ ] Test: Run migration script on demo data
  - [ ] Review: Rollback procedures if issues

- [ ] **Day 3: Support & Escalation**
  - [ ] Create: Technical troubleshooting guide
  - [ ] Define: When to escalate to CTO (vs. handle as implementation lead)
  - [ ] Collect: List of 5 common setup questions
  - [ ] Schedule: Weekly tech sync with CTO

**Success Criteria**:
- ✅ Can set up HRMS for new venture in <30 min
- ✅ Knows all 5 common issues and solutions
- ✅ Can escalate correctly to CTO
- ✅ Has rollback plan documented

---

### Phase 3: Customer Success Rep Onboarding (Days 1-2)
**Owner**: Operations Manager agent  
**Duration**: 2 days  
**Deliverables**: Onboarding scripts + SLA documentation

- [ ] **Day 1: Product & Customer Journey**
  - [ ] Training: HRMS feature walkthrough (employee self-service, admin dashboard)
  - [ ] Training: Common customer use cases by role
  - [ ] Review: SLA targets (response <2 hrs, resolution <24 hrs)
  - [ ] Review: Customer health metrics (login frequency, feature adoption)

- [ ] **Day 2: Execution & Escalation**
  - [ ] Practice: 3 onboarding calls with CS trainer (shadowing)
  - [ ] Practice: Troubleshoot 5 common issues
  - [ ] Create: Personal escalation checklist
  - [ ] Review: When to escalate to Implementation Lead vs. CTO
  - [ ] Schedule: Weekly check-in with Sector Lead on customer health

**Success Criteria**:
- ✅ Can run onboarding call without script (but has it as backup)
- ✅ Knows how to escalate technical issues
- ✅ Can identify at-risk customers (low adoption, angry emails)
- ✅ Reports weekly on customer health

---

### Phase 4: Sales Rep Onboarding (Days 1-2)
**Owner**: CEO agent  
**Duration**: 2 days  
**Deliverables**: Sales playbook + lead routing

- [ ] **Day 1: Product & Positioning**
  - [ ] Training: HRMS feature positioning (not a generic HR tool, focus on specific sector pain points)
  - [ ] Training: Competitive differentiation (vs. ADP, Guidepoint, Toast payroll)
  - [ ] Training: Pricing & trial structure ($199/mo Starter, 14-day free trial)
  - [ ] Review: Customer testimonials + case studies (from pilot ventures)

- [ ] **Day 2: Sales Process & Execution**
  - [ ] Practice: Discovery call script (pain points, budget, decision timeline)
  - [ ] Practice: Objection handling (pricing too high, switching cost, compliance concerns)
  - [ ] Review: Qualification criteria (company size, tech stack, growth stage)
  - [ ] Practice: Trial signup + upsell (day 3, 7, 10 of trial)
  - [ ] Setup: CRM access + lead routing

**Success Criteria**:
- ✅ Can run discovery call confidently
- ✅ Knows what makes a qualified lead
- ✅ Can handle top 5 objections
- ✅ Understands trial → paid conversion process

---

## 📊 Crew Hiring Targets

### Immediate Hires (By May 15)
- **4 Sector Leads** (already recruiting from internal agents)
- **4 Implementation Leads** (Tier 1 sectors: Construction, Logistics, Field Services, Healthcare)
- **8 Customer Success Reps** (2 × Tier 1 sectors)
- **4 Sales Reps** (1 × Tier 1 sectors)

**Total**: 20 people (Cost: ~$30K/month fully loaded)

### Phase 2 Hires (By May 27)
- **4 Implementation Leads** (Tier 2 sectors)
- **8 Customer Success Reps** (Tier 2 sectors)
- **4 Sales Reps** (Tier 2 sectors)
- **2 Regional Leads** (consolidate Tier 3 sectors)

**Total**: +18 people → 38 total

### Hiring Strategy
- **Where to source**: 
  - Construction: Raken, Procore, Toast alumni
  - Logistics: TForce, XPO, ArcBest ops managers
  - Field Services: ServiceTitan, Jobber, Angi techs
  - LinkedIn + AngelList + founder networks
  
- **Interview process**: 15 min culture fit + 30 min scenario (handle difficult customer/setup)
- **Offer structure**: Base $50-70K + equity 0.05-0.1% + bonus (MRR targets)

---

## 🎯 Quick Start (This Week)

**By EOD May 13**:
- [ ] Identify 4 Sector Lead candidates (internal or external)
- [ ] Post LinkedIn/job listings for Implementation Leads
- [ ] Reach out to network for CS + Sales hires

**By EOD May 15**:
- [ ] Offer letters sent to Sector Leads
- [ ] 4 Implementation Leads identified/offered
- [ ] 8 CS Reps identified
- [ ] 4 Sales Reps identified

**By May 20**:
- [ ] All Tier 1 crew onboarded and operational
- [ ] Pilot ventures assigned to crews
- [ ] Sales process live (discovery calls starting)

---

## 💼 Success Metrics (30 days)

**Crew Effectiveness**:
- Avg customer onboarding time: <2 hours
- Avg technical setup time: <30 min
- Customer satisfaction (onboarding): 4.5/5
- Implementation Lead productivity: 3 ventures/week each

**Sales Effectiveness**:
- Discovery calls completed: 20+ by end of week
- Trial signups: 5-10 by end of week
- Trial→paid conversion: 40%+
- Average CAC (from pilot): <$500

**Financial Impact**:
- Tier 1 MRR (4 sectors × 5 customers): $4-6K by May 27
- Crew cost: $30K/month (breakeven at 15 customers)
- Target: 20+ customers by June 5 ($3-5K MRR per sector × 2-3 sectors)
