---
name: realestate-os/ARCHITECTURE
title: RE-OS Unified Architecture
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# RE-OS Unified Architecture

**Single Operating System for Entire Property Lifecycle: PM → Brokerage → Investing → Construction → Lending**

## System Overview

Unified five-tier SaaS with three role-based portals sharing one data model:

```
Frontend (Next.js 15 - Three Portals)
  ├─ Executive Suite (CEO, CFO, COO, Investors)
  ├─ Operations Portal (PM, Brokers, Asset Managers, Construction PMs)
  └─ Resident Portal (Tenants, Owners, Borrowers, Investors)
  ↓
Auth & Authorization (Role-based access + Workspace isolation)
  ↓
API Layer (Express REST + Real-time WebSocket)
  ↓
Supabase SDK (PostgreSQL + RLS + Real-time)
  ↓
Unified Database (One Schema, Multi-Portal Access)
```

---

## Unified Data Model

**One schema eliminates overlapping "CRM," "PM," "Lending," "Investing" silos**

### Tables (Consolidated from 8 → 9 Core + Relationships)

| Table | Purpose | Key Fields |
|-------|---------|-----------|
| **users** | All roles (landlord, tenant, broker, PM, executive, underwriter) | id, email, name, roles[], workspaces[], aiPreferences |
| **workspaces** | Team/org boundaries | id, name, owner_id, members[], settings, integrations[] |
| **properties** | Real properties (apt complex, office, land, development) | id, workspace_id, address, type, city, state, zip, value, status, aiValuation, riskScore, constructionStage |
| **units** | Individual spaces within property | id, property_id, unit_number, sqft, bedrooms, bathrooms, rent_amount, status (vacant\|occupied\|renovating), tenant_id |
| **leases** | Rental agreements (PM, brokerage, investing unified) | id, unit_id, tenant_id, workspace_id, start_date, end_date, rent, status, terms (JSONB), auto_renew, document_url |
| **deals** | Investment/acquisition/refi/dev pipeline (unified) | id, workspace_id, property_id, stage (prospect\|LOI\|underwriting\|funded\|executing\|complete), dealType (acquisition\|refi\|development\|syndication), capitalStack[], investors[], underwriting (JSONB), timeline (JSONB) |
| **rent_payments** | Rent tracking + accounting | id, unit_id, month, amount, due_date, paid_date, status (pending\|paid\|late\|waived), stripe_id, late_fee |
| **maintenance_requests** | Work orders (PM + construction context) | id, property_id, unit_id, tenant_id, type, description, photos[], priority, status (open\|assigned\|in_progress\|completed), assigned_to, estimate_cost, actual_cost, completed_date |
| **documents** | Contracts, leases, reports, receipts, disclosures | id, workspace_id, type (lease\|contract\|report\|receipt\|disclosure), linked_entity_type, linked_entity_id, content, aiSummary, aiExtractedData (JSONB), versions[], esignatures[] |
| **capital_stack** | Investment structure (equity, debt, mezzanine) | id, deal_id, investor_id, amount, returnType, waterfall_position, distributions (JSONB) |
| **users_workspaces** | Many-to-many + role assignment | user_id, workspace_id, roles[] (landlord\|tenant\|broker\|pm\|executive\|underwriter\|etc), permissions[] |

### Unified RLS Policies

```sql
-- Executive sees: all workspace data (properties, deals, capital stack, performance)
-- PM sees: properties + units they manage, leases, maintenance requests
-- Tenant sees: only their assigned unit, lease, maintenance tickets they filed, documents tied to lease
-- Broker sees: only deals + properties they're transacting
-- Underwriter sees: only deals in underwriting, financial data, risk assessments

CREATE POLICY workspace_isolation ON properties
  USING (
    workspace_id IN (
      SELECT workspace_id FROM users_workspaces WHERE user_id = auth.uid()
    )
    AND (
      -- Role-based column filtering
      has_required_role(auth.uid(), workspace_id, current_role())
    )
  );

-- Similar policies on: deals, leases, documents, maintenance_requests, capital_stack
```

### Indexes (Query Optimization)

- `properties(workspace_id, status)` — portfolio queries
- `units(property_id, status, tenant_id)` — occupancy tracking
- `leases(unit_id, status, end_date)` — expiration alerts
- `deals(workspace_id, stage, dealType)` — pipeline filtering
- `rent_payments(unit_id, month, status)` — arrears detection
- `maintenance_requests(property_id, status)` — open work orders
- `documents(workspace_id, linked_entity_id)` — document retrieval
- `users_workspaces(user_id, workspace_id)` — permission lookup

---

## Portal Architecture

### Portal 1: Executive Suite
**Roles:** CEO, CFO, COO, Fund Managers, Investment Committee

**Modules:**
- **Command Center** (KPI dashboard + analytics merged)
  - Portfolio health, revenue, occupancy trends, cash flow forecasting
  - Risk scorecards, AI-generated insights
  - Geographic heatmap of all properties
  
- **Deal Funnel** (Unified acquisition → underwriting → execution)
  - Pipeline visualization (same for all deal types: acquisitions, refinancing, development)
  - Underwriting workspace with AI valuation & risk scoring
  - Capital stack & waterfall distribution
  - Investor management & reporting
  
- **Operations Monitor** (All active deals, projects, properties)
  - Construction schedules (Gantt view)
  - Lending draw pipeline
  - Maintenance alerts & emerging issues
  - Autonomous AI alerts for anomalies

**Data Access:** Full workspace read; restricted by executive role

---

### Portal 2: Operations Portal
**Roles:** Property Manager, Broker, Asset Manager, Construction PM, Underwriter

**Modules:**
- **Portfolio Dashboard** (All properties in grid/map view)
  - Occupancy %, rent collection status, maintenance needs
  - Quick actions: lease, maintenance request, tenant communication
  
- **Property Workspace** (Drill-down from portfolio)
  - Units/buildings hierarchy
  - Active leases (renewal alerts, expiring dates)
  - Maintenance tickets (open, in-progress, completed)
  - Work order assignment & tracking
  - Vendor management & payment
  - Tenant contact info & payment history
  
- **Deals & Transactions** (Brokers + acquisition teams)
  - MLS search (unified across all listings)
  - Showing scheduler
  - Offer management & negotiation
  - Transaction coordinator workspace
  - Closing timeline & document tracking
  
- **Construction & Renovation**
  - Project timeline (Gantt from unified data model)
  - Budget tracking & change orders
  - Daily field reports
  - RFI management & punch list
  - Permit tracking
  
- **Lending & Draws**
  - Loan origination (if lending desk role)
  - Construction draw requests (visible in Property Workspace)
  - Borrower profile access (read-only for PMs)
  - Underwriting workspace (if underwriter role)

**Data Access:** Filtered by role (PM sees their properties, broker sees their deals, etc.)

---

### Portal 3: Resident Portal
**Roles:** Tenant, Property Owner, Investor, Borrower

**Modules:**
- **My Portfolio**
  - Tenant: leased unit details, lease terms, payment info
  - Owner: all owned properties, portfolio value, performance
  - Investor: all invested deals, capital allocation, returns
  - Borrower: loan details, draw status, documentation
  
- **Rent & Payments**
  - Payment history
  - Auto-pay setup
  - Invoices & receipts
  - Late payment alerts
  
- **Maintenance Requests**
  - Submit ticket with photos
  - Track status in real-time
  - View maintenance history
  
- **Documents Vault**
  - Lease (download, e-sign addendums)
  - Rent receipts & tax documents
  - Insurance docs
  - Closing docs (for investors/borrowers)
  - Communication history
  
- **Statements & Reports**
  - Rent collected/paid (for owner/tenant)
  - Investment returns (for investor)
  - Loan statements & draws (for borrower)

**Data Access:** Read-only; filtered by entity (see only your leases, deals, documents)

---

## Consolidation: Old Silos → Unified

| Old Module | New Location | Strategy |
|---|---|---|
| **CRM** | Operations Portal → Deals & Transactions + Property Workspace (contacts embedded) | One funnel for acquisitions + brokerage deals; tenants are contacts tracked in leases |
| **Property Management** | Operations Portal → Property Workspace (main UI) | Portfolio dashboard + property drill-down with units, leases, maintenance |
| **Brokerage** | Operations Portal → Deals & Transactions | Same deal funnel; broker-specific UI (MLS, showings, offers, closing) |
| **Investing** | Executive Suite → Deal Funnel + Command Center | Capital stack, waterfall, investor reporting in executive suite; property performance in analytics |
| **Lending** | Operations Portal → Lending & Draws + Executive Suite (portfolio view) | Draw requests visible in Property Workspace; loan portfolio analysis in Executive Dashboard |
| **Construction** | Operations Portal → Construction & Renovation | Gantt, budget, RFIs, punch list; driven by unified maintenance_requests + deals entities |
| **Analytics** | Embedded everywhere (Executive Dashboard + Operations Portal drill-downs) | No separate "Analytics" page; AI insights on every screen + Command Center KPIs |
| **Documents** | Linked from every entity + Resident Portal → Documents Vault | One vault; accessible based on role (tenant sees lease, investor sees cap stack docs) |
| **Mobile** | Responsive design across all portals | One app, three portals, fully mobile-responsive |
| **Collaboration** | Embedded in workspaces (comments, activity feed, assignments) | Not a separate module; integrated into Operations & Executive workspaces |
| **AI Copilot** | Sidebar + inline suggestions on every page (all modules) | Not a separate module; threaded through everything |
| **Settings & Administration** | Top-level workspace settings | Members, roles, integrations, AI configuration (consistent across all portals) |

---

## API Architecture

### Routes

| Path | Handler | Auth |
|------|---------|------|
| `POST /auth/register` | User signup | None |
| `POST /auth/login` | User signin | None |
| `GET /properties` | List landlord's properties | X-User-ID header |
| `POST /properties` | Create property | X-User-ID header |
| `GET /properties/:id` | Property detail + units | X-User-ID header |
| `POST /rent-payments/create-payment-link` | Stripe checkout | X-User-ID header |
| `POST /webhooks/stripe` | Payment webhook | Stripe signature |
| `POST /maintenance` | Tenant submits request | X-User-ID header |
| `GET /maintenance` | List requests | X-User-ID header |
| `PUT /maintenance/:id` | Update status | X-User-ID header |
| `GET /reports/property/:id/plp` | P&L report | X-User-ID header |
| `GET /reports/property/:id/tenants` | Tenant roster CSV | X-User-ID header |

### Request Flow

```
POST /properties
  → Express route handler
  → Extract X-User-ID from headers
  → supabase.from('properties').insert()
  → PostgreSQL RLS check: auth.uid() = created_by
  → 201 response with created property
```

### Authentication

1. **Register:** `POST /auth/register` → Supabase creates user + JWT
2. **Login:** `POST /auth/login` → Returns accessToken
3. **API calls:** Send `X-User-ID` header (extracted from token)
4. **RLS:** PostgreSQL policies use auth.uid() for isolation

---

## Frontend (Next.js 15)

### Pages

- `/` — Landing/login (redirects to `/dashboard` if logged in)
- `/dashboard` — Landlord dashboard (property cards, stats)
- `/properties/:id` — Property detail (units, leases)
- `/tenant/:id` — Tenant portal (lease, pay rent, submit maintenance)
- `/settings` — Account & billing

### State Management

- **Zustand** — global auth state
- **React hooks** — local form/UI state
- **Supabase Auth UI** — pre-built login component

### Components

- Property card, lease preview, payment form
- Maintenance request list, status badge
- shadcn/ui + Radix UI + Tailwind CSS

---

## Stripe Integration

### Rent Payment Flow

```
1. Landlord → create-payment-link
   POST /api/rent-payments/create-payment-link
   { unitId, month, amount }

2. Backend
   - stripe.checkout.sessions.create()
   - Insert rent_payment (status='pending')

3. Response → session.url (Stripe checkout)

4. Tenant opens link, pays

5. Stripe webhook → checkout.session.completed

6. Backend
   POST /api/webhooks/stripe
   - Verify signature
   - Update rent_payment (status='paid', paid_date=now)
```

### Webhook Security

Signature verified before processing:
```typescript
const event = stripe.webhooks.constructEvent(
  req.body,
  req.headers['stripe-signature'],
  STRIPE_WEBHOOK_SECRET
);
```

---

## Deployment

### Vercel (Frontend)

```
git push main
  ↓ GitHub Actions: test + build
  ↓ Vercel auto-deploy
  ↓ CDN + Next.js SSR
```

### Railway (Backend)

```
git push main
  ↓ Detect: package.json
  ↓ Build: npm install, npm run build
  ↓ Start: npm start
  ↓ Expose: port 3001
```

### Supabase (Database)

- Managed PostgreSQL
- Auto RLS enforcement
- Webhook logging

---

## Security

- **RLS:** Data isolation at database level (cannot bypass via API)
- **Auth:** Supabase JWT (refreshed automatically)
- **Secrets:** Vercel/Railway secure storage (never in git)
- **Validation:** Basic input validation + PostgreSQL constraints
- **HTTPS:** All connections encrypted (Vercel, Railway, Supabase)

---

## Performance

- **Indexes:** Fast queries on `created_by`, `property_id`, `status`
- **Caching:** Redis (docker-compose, unused in MVP; for phase 2)
- **Assets:** Next.js Image optimization, Tailwind minification

---

## Monitoring (Production)

- Vercel Analytics
- Railway logs (stdout/stderr)
- Stripe Dashboard
- Supabase Logs (errors, RLS denials)

---

## Known Limitations (MVP)

- Single database (no read replicas)
- Maintenance costs estimated (not from invoices)
- Email/SMS reminders (manual setup required)
- No asset versioning (S3 URLs)

---

## Phase 2 Roadmap

- Message queue (Temporal/Bull)
- Mobile app (React Native)
- SMS/email reminders (Twilio)
- Advanced analytics (data warehouse)
- Landlord API (programmatic access)
