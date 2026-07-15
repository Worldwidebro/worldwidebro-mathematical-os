---
references:
  - [[VENTURE-MASTER]]
  - [[LOOP-FRAMEWORK]]
  - [[ORB-MASTER-CONNECTOR-2026-06-11]]
---

# Onboarding Subsystems — Reusable OS Module

**Purpose:** Onboarding is not one thing. It's the pipeline that converts a stranger into an active participant. Every venture reuses the same skeleton; only the **Verification + Documents** set and the **archetype** change. This doc is the canonical module the other ~710 ventures inherit instead of re-deriving paperwork each time.

**Status:** ✅ ACTIVE | **Date:** 2026-06-24 | **Shared service:** `onboarding` (see `08-DATA/registries/shared_services.csv`)

**Reference instances (already built):**
- **Code:** `03-PORTFOLIO/opcos/STAFFING/staffing-os/` — Prisma (`Worker, Client, Job, Placement, Timesheet, Commission`) + `n8n-workflows/worker-onboarding.json`
- **Docs (fully worked, supply-side):** `03-PORTFOLIO/ventures/active/Medical-Courier/HIRING/` — 9-doc pipeline
- **Generic hiring template:** `_career/HIRING-PACKAGE-OPTION-D/`
- **Automation engines (owned repos):** `ops-009-onboarding-ai`, `iza-os-hr-onboarding-bot`

---

## 1. The Skeleton (11 subsystems — constant across all ventures)

```text
Marketing → Lead Capture → [ONBOARDING] → Recruiting → Placement → Payroll → Retention
                                │
   1. Acquisition      → new lead / applicant record
   2. Intake           → complete profile
   3. Verification     → verified user        ◄── varies most by sector
   4. Qualification    → approved / rejected / review
   5. Documents        → signed documents      ◄── varies most by sector
   6. Account Provision → active account
   7. Training         → trained user
   8. Workflow Assign  → owner assigned
   9. Communication    → engaged user
  10. Activation       → activated user (first result)
  11. Tracking         → optimization data
```

Neo4j flow:
```text
(:Lead)-[:NEXT]->(:Intake)-[:NEXT]->(:Verification)-[:NEXT]->(:Qualification)
  -[:NEXT]->(:Documents)-[:NEXT]->(:AccountProvision)-[:NEXT]->(:Training)
  -[:NEXT]->(:Assignment)-[:NEXT]->(:Activation)-[:NEXT]->(:Tracking)
```
Per-node tracking props: `status`, `owner`, `entered_at`, `completed_at`, `time_to_activation`, `drop_off`.

---

## 2. The 3 Archetypes (who is being onboarded)

The skeleton is the same; subsystem **weight** shifts by who you onboard.

### A. Supply-side — worker / driver / contractor / pro
Heavy on **Verification + Documents + Training**. This is the hardest pipeline.
- Reference: Medical-Courier `HIRING/`, staffing-os `worker-onboarding.json`
- Subsystem weight: Verification ●●●, Documents ●●●, Training ●●●, Qualification ●●

### B. Demand-side — client / customer / buyer
Heavy on **Qualification**, light **Documents**. Optimize for speed-to-value.
- Reference: staffing `go-to-market/CLIENT-PLACEMENT-AGREEMENT.md`
- Subsystem weight: Qualification ●●●, Documents ●, Verification ●, Activation ●●●

### C. End-user SaaS — user / team member
Collapses to **Account Provisioning + Activation**. Almost no paperwork.
- Subsystem weight: Account Provision ●●●, Activation ●●●, Verification ● (email only)

**Two-sided ventures run A + B in parallel** (staffing = worker + client; marketplaces = pro + homeowner).

---

## 3. Sector Override Table (the Verification + Documents that differ)

| Sector / Venture | Archetype(s) | Who | Verification (subsystem 3) | Documents (subsystem 5) | Activation = first… |
|---|---|---|---|---|---|
| **Staffing** | A + B | Worker + Client | I-9, work auth, skills test | Worker agreement, W-9; client placement agreement | placement / interview |
| **Logistics / Medical-Courier** | A | Driver | License, vehicle, insurance, **HIPAA**, background | Driver agreement, HIPAA, training acks | first delivery |
| **Construction** | A + B | Contractor/sub + GC client | **License, bonding, COI/insurance**, W-9 | Subcontract, COI, safety forms | first job assigned |
| **Financial (GenixBank)** | C (+ regulated) | End customer | **KYC / AML, ID, bank link** | Account agreement, e-sign disclosures | first account / txn |
| **Education / Tutoring** | A + B | Tutor + Student | Tutor: background; Student: payment | Tutor agreement; enrollment/consent | first lesson |
| **Marketplace (plumbing/roofing)** | A + B | Pro + Homeowner | Pro: license + insurance; Homeowner: payment | Pro service agreement; homeowner ToS | first listing / booking |
| **Healthcare** | A | Clinician/staff | License, credentialing, **PHI/HIPAA**, background | BAA, HIPAA, credentialing file | first patient/record |
| **Real Estate** | A + B | Agent + Buyer/Seller | License (agent); pre-qual (buyer) | Listing/buyer agreement | first listing/showing |
| **Beauty/Wellness** | B (+ A staff) | Client (+ stylist) | Client: payment; staff: license | Intake/consent form; staff agreement | first appointment |
| **Retail / E-Commerce** | C | Customer | Email; payment | ToS (click-wrap) | first order |
| **SaaS / Technology** | C | User/team | Email verify | ToS (click-wrap) | first project created |

**Rule of thumb:** to instantiate onboarding for a new venture, keep subsystems 1–2 and 6–11 as-is; swap only the **Verification** and **Documents** cells from this table for the venture's sector + archetype.

---

## 4. How to instantiate for a new venture

1. Pick archetype(s): A, B, C, or A+B (two-sided).
2. Copy the Medical-Courier `HIRING/` doc set (supply-side) or staffing client agreements (demand-side) as the starting template.
3. Swap Verification + Documents per the sector row above.
4. Register the venture against the `onboarding` shared service in `shared_services.csv` (`dependent_ventures`).
5. Wire automation: clone `staffing-os/n8n-workflows/worker-onboarding.json` (or `ops-009-onboarding-ai` / `iza-os-hr-onboarding-bot`) and repoint the verification/document steps.
6. Track subsystem 11 (completion rate, time-to-activation, drop-off) per [[LOOP-FRAMEWORK]].

---

## 5. Gaps to close
- No `onboarding` capability existed in `venture_capability_map.csv` — model it as a capability so ventures can require it.
- Only STAFFING / Medical-Courier / CONSTRUCTION / FINANCIAL have real content; the other 14 opcos are placeholders that inherit this module on activation.
