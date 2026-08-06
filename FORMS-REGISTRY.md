---
name: FORMS-REGISTRY
title: AI Boss OS — Master Form Registry
desc: ...
version: 1.0
date: 2026-07-30
applies: All 712 ventures + AI agent routing
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# AI Boss OS — Master Form Registry

**Purpose**: Canonical source of truth for all business forms across ventures.  
**Status**: P0 forms live (8), full stack (400+) Phase 2.

---

## P0 Forms (Operational Minimum) — v1

### 1. Capability Registration
- **Who**: Venture declares what it provides
- **When**: Venture launch, capability addition
- **Output**: (:Venture)-[:PROVIDES_CAPABILITY]->(:Capability) in Neo4j
- **Agent**: Operations Agent
- **Example**: CON-001 declares "lead-capture" capability

### 2. Capability Request
- **Who**: Venture needs external capability
- **When**: Task requires capability venture doesn't have
- **Output**: (:Venture)-[:NEEDS_CAPABILITY]->(:Capability) in Neo4j
- **Agent**: Operations Agent

### 3. Shared Service Subscription
- **Who**: Venture A pays Venture B for service
- **When**: Inter-venture service agreement
- **Output**: (:Venture)-[:SUBSCRIBES_TO]->(:Venture) + revenue tracking
- **Agent**: Finance Agent

### 4. Partnership / Referral Agreement
- **Who**: Two ventures formalize referral/partnership
- **When**: Revenue-sharing opportunity identified
- **Output**: (:Venture)-[:REFERS_CLIENTS]->(:Venture) in Neo4j
- **Agent**: Sales Agent

### 5. Customer Consent (SMS/Email/Data)
- **Who**: Customer opts in
- **When**: Lead capture, customer account creation
- **Output**: Customer record with consent flags (Supabase)
- **Agent**: Sales Agent

### 6. ACH / Payment Authorization
- **Who**: Customer authorizes recurring payment
- **When**: Subscription or contract signed
- **Output**: Payment method stored (Stripe + Supabase)
- **Agent**: Finance Agent

### 7. Incident / Corrective Action Report
- **Who**: Anyone reports issue
- **When**: Bug, compliance gap, customer complaint
- **Output**: Incident ticket → Neo4j audit trail
- **Agent**: Operations Agent

### 8. Production Change / Deployment Approval
- **Who**: Agent requests to deploy code/config
- **When**: Code merge, config change, agent capability upgrade
- **Output**: Deployment logged to audit trail
- **Agent**: Operations Agent

---

## Universal Forms (Shared by All)

**Company & Legal**: Business Registration, EIN Request, Operating Agreement, Business License, Registered Agent, Founder Agreement, Shareholder Agreement, Equity Grant, IP Assignment, Conflict of Interest Disclosure

**Sales & CRM**: Lead Intake, Contact Form, Customer Profile, Opportunity Record, Quote Request, Proposal, Service Agreement, Invoice, Receipt

**Finance & Treasury**: Purchase Order, Expense Report, Reimbursement Request, Vendor Setup, W-9, Credit Card Auth, Recurring Billing Consent, Refund Auth, Budget Request, Capital Allocation, Funding Request, Investment Proposal

**Legal & Compliance**: NDA, MSA, SOW, Contractor Agreement, Privacy Notice, Data Processing Consent, Terms of Service, Privacy Policy, DPA, SLA

**Human Resources**: Employment Application, Onboarding, Direct Deposit, Emergency Contact, Confidentiality, Equipment Checkout, Performance Review, Promotion Request, Offboarding

**Operations**: SOP Acknowledgement, Incident Report, Quality Checklist, Project Status, Insurance COI, CAR, Root-Cause Analysis, Business Continuity Plan

**Cyber / IT / Security**: API Access Request, Webhook Approval, Data-Sharing Approval, Agent Permission Request, Production Change Approval, Security Exception, Incident Notification

---

## Venture-Specific Forms

### LT-005 (Medical Courier)
Medical Courier Request, STAT Delivery Request, Pickup Authorization, Chain-of-Custody, Proof of Delivery, Temperature Excursion Report, Driver Application, Vehicle Inspection, HIPAA BAA, PHI Access Authorization, Specimen Release Form

### CON-001 (Ace Construction)
Estimate Request, Site Visit Request, Financing Request, Scope of Work, Material Selection, Change Order, Daily Construction Report, Safety Inspection, Punch List, Draw Request, Lien Waiver, Subcontractor Application, Permit Tracker, Notice to Owner, OSHA Toolbox Talk

### STA-001 (Staffing Core)
Employer Registration, Job Order, Staffing Request, Employment Application, Skills Assessment, Availability Form, Background Authorization, I-9, W-4, Assignment Acceptance, Timecard Dispute

### OPS-001 (Venture Operations)
Venture Creation Request, Venture Approval, Repository Request, Agent Deployment Request, MCP Registration, SOP Submission, ADR, Capability Approval, Production Deployment Approval

### EC-001 & EC-112 (E-commerce)
Product Inquiry, Wholesale Application, Customer Account Registration, Return Request (RMA), Refund Request, Warranty Request, Gift Card Request, Affiliate Application, Newsletter Signup, Sales Tax Exemption, MAP Agreement, Influencer Contract

### RE-001 (Property Holdings)
Buyer Intake, Property Inquiry, Showing Request, Offer Submission, Financing Prequalification, Rental Application, Lease Application, Maintenance Request, Move-In/Out Inspection, Letter of Intent, Due-Diligence Checklist, Security Deposit Receipt

### LT-011 (Dispatch SaaS)
Free Trial Signup, Demo Request, Contact Sales, Support Request, Feature Request, Account Onboarding, API Access Request, Billing Update, Cancellation Request, Terms Acceptance, DPA

---

## Cross-Venture Synergy Forms

Partnership Request, Capability Sharing Request, Shared Service Subscription, Referral Agreement Registration, Revenue Sharing Agreement, Joint Venture Proposal, Lead Sharing Agreement, Venture Integration Request

---

## AI Boss OS Internal Forms

Venture Registration, Venture Health Review, Launch Readiness Checklist, Agent Registration, Agent Deployment Request, Agent Permission Request, Repository Registration, Workflow Registration, MCP Registration, Skill Registration

---

## Graph-Native Routing

```cypher
(:Venture)-[:REQUIRES_FORM]->(:Form)
(:Form)-[:DEPENDS_ON]->(:Regulation)
(:Agent)-[:CAN_FILL]->(:Form)
(:Task)-[:NEEDS_FORM]->(:Form)
```

When task arrives:
1. Query Neo4j: "What forms does this venture need?"
2. Check: "Can agent fill this form?"
3. Route to agent
4. Form submission creates relationships automatically

---

## Status

- [x] P0 forms defined (8)
- [x] Venture-specific forms mapped
- [x] Universal forms catalogued
- [ ] JSON schemas for P0 forms (this week)
- [ ] Wire into Neo4j (this week)
- [ ] Agent form-routing logic (Week 2)

