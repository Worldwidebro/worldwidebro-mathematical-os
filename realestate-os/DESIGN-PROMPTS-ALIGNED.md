# RE-OS Design Prompts Reorganized
**100 design briefs → Aligned to 3 unified portals + shared foundation**

---

## Foundation (12 Prompts)
Shared across all portals — build once, use everywhere.

- [x] Design a complete design system with typography, spacing, color tokens, iconography
- [ ] Modern login page with SSO options
- [ ] Multi-step organization onboarding
- [ ] Team invitation flow
- [ ] Workspace creation wizard
- [ ] Role selection experience
- [ ] Responsive layout that scales seamlessly from desktop to tablet and mobile
- [ ] Notification center
- [ ] Activity feed with comments
- [ ] Settings & Administration with multi-tenant controls
- [ ] Permissions and RBAC management
- [ ] Integration marketplace

---

## Executive Suite (22 Prompts)

### Command Center (8)
- [ ] Executive command center with KPIs, revenue, occupancy, and AI insights
- [ ] CEO dashboard highlighting portfolio health
- [ ] CFO financial analytics workspace
- [ ] COO operations overview
- [ ] Interactive executive map of all managed properties
- [ ] Business intelligence dashboard
- [ ] Geographic portfolio heatmap
- [ ] Executive KPI scorecards

### Deal Funnel (10)
- [ ] Acquisition pipeline
- [ ] Property underwriting interface
- [ ] Investment committee dashboard
- [ ] Portfolio analytics
- [ ] Capital stack visualization
- [ ] Waterfall distribution interface
- [ ] Cash flow forecasting dashboard
- [ ] Investor reporting portal
- [ ] Loan portfolio lending analytics
- [ ] Risk scoring dashboard

### Operations Monitor (4)
- [ ] Construction project dashboard
- [ ] Permit tracking dashboard
- [ ] Lending draw management
- [ ] Autonomous task execution timeline

---

## Operations Portal (48 Prompts)

### Portfolio Dashboard (3)
- [ ] Portfolio overview with occupancy heatmaps
- [ ] Building and unit hierarchy
- [ ] Property detail page

### Property Workspace (15)
- [ ] Lease management dashboard
- [ ] Maintenance request center
- [ ] Work order tracking
- [ ] Tenant portal dashboard
- [ ] Owner portal dashboard
- [ ] Rent collection analytics
- [ ] Vendor assignment workspace
- [ ] Tenant communication interface
- [ ] Property document organization
- [ ] Property timeline & history
- [ ] Occupancy analytics (operational view)
- [ ] Revenue analytics (operational view)
- [ ] Property financials (operational view)
- [ ] Unit availability & pricing
- [ ] Lease expiration alerts

### Deals & Transactions (12)
- [ ] MLS search experience
- [ ] Interactive listing management page
- [ ] Buyer dashboard
- [ ] Seller dashboard
- [ ] Showing scheduler with calendar
- [ ] Offer management interface
- [ ] Transaction coordinator workspace
- [ ] Closing workflow timeline
- [ ] Negotiation timeline
- [ ] Document collaboration (transactions)
- [ ] Commission tracking
- [ ] Transaction analytics

### Construction & Renovation (12)
- [ ] Gantt schedule interface
- [ ] Budget tracking workspace
- [ ] Daily field reports
- [ ] RFI management
- [ ] Change order workflow
- [ ] Punch list interface
- [ ] Contractor assignment
- [ ] Progress photography
- [ ] Safety incident tracking
- [ ] Material tracking
- [ ] Equipment management
- [ ] Subcontractor management

### Lending & Draws (6)
- [ ] Loan origination workflow
- [ ] Borrower profile
- [ ] Underwriting workspace
- [ ] Construction draw management
- [ ] Risk scoring (underwriting view)
- [ ] Loan compliance tracking

---

## Resident Portal (18 Prompts)

### My Portfolio (5)
- [ ] Tenant portal dashboard
- [ ] Owner portal dashboard
- [ ] Investor dashboard
- [ ] Borrower dashboard
- [ ] Portfolio summary & key metrics

### Rent & Payments (5)
- [ ] Rent collection interface (tenant view)
- [ ] Payment history
- [ ] Auto-pay setup interface
- [ ] Invoice & receipt download
- [ ] Late payment notification

### Maintenance & Support (4)
- [ ] Maintenance request submission
- [ ] Work order status tracking
- [ ] Technician arrival notifications
- [ ] Issue resolution confirmation

### Documents Vault (4)
- [ ] Digital document vault
- [ ] Contract review interface (resident view)
- [ ] E-signature workflow
- [ ] Version history comparison

---

## AI Integration Layer (Embedded Everywhere)

These are not separate pages — they are features threaded through all modules above.

- [ ] AI copilot chat integrated into every page
- [ ] Natural language property search
- [ ] AI-generated investment recommendations
- [ ] AI workflow automation builder
- [ ] AI document summarization
- [ ] Predictive maintenance dashboard (alerts in Property Workspace)
- [ ] AI valuation engine visualization (in Deal Funnel underwriting)
- [ ] AI-assisted lead qualification (in Deals & Transactions)

---

## Brand & Visual Language (2 Prompts)

- [x] Design a premium AI-powered RealEstateOS landing page using modern enterprise SaaS aesthetics
- [x] Create a complete design system (colors, typography, components)

---

## Landing Pages (0 Prompts)

**Note:** These are external-facing marketing pages, not app portals. Documented separately in marketing site.

---

## Summary

**Before:** 16 categories, 8 overlapping modules, 100 scattered prompts  
**After:** 3 unified portals, 1 data model, 1 design system, 52 actual UI screens to build

**Build Sequence (No Overlaps):**

| Phase | Focus | Blocks |
|-------|-------|--------|
| ✅ Phase 0 | Design System + Auth | All portals depend on this |
| Phase 1 | Property Workspace (Portfolio + Property drill-down) | Operations Portal core |
| Phase 2 | Command Center (KPI Dashboard) | Executive Suite core |
| Phase 3 | Deal Funnel (Unified pipeline) | Shared by Executive + Operations |
| Phase 4 | Resident Portal (Self-service) | Independent (read-only) |
| Phase 5 | AI Integration (Chat, suggestions, predictions) | Threads through all phases above |

