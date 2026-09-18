# VEX Dashboard — Application Flow & Navigation

**Version**: 1.0 | **Updated**: 2026-09-18 | **Owner**: Product

---

## PRIMARY USER JOURNEYS

### Journey 1: Portfolio Health Check (5 min)
**Actor**: Portfolio Manager | **Goal**: Quick venture status overview

```
Login → Dashboard (KPIs) → Drill into struggling venture → Financial tab
  → Revenue Attribution → Identify blocker → Decisions tab → Approve action
```

**Screens**: Dashboard → Ventures → Financial → Decisions

### Journey 2: Weekly Operations Review (15 min)
**Actor**: Venture Operations | **Goal**: Ensure all ventures executing

```
Dashboard → Tasks (filter by status) → Bottlenecks (identify constraints)
  → Dependencies (map blockers) → Approvals (unblock) → Audit (verify)
```

**Screens**: Dashboard → Tasks → Bottlenecks → Dependencies → Approvals → Audit

### Journey 3: Agent Health Check (10 min)
**Actor**: AI Systems Engineer | **Goal**: Monitor agent operations

```
Agents (view module workload) → Orchestrator (see workflow status)
  → Analytics (check success rates) → Alerts (respond to failures)
```

**Screens**: Agents → Orchestrator → Analytics → Alerts

### Journey 4: Month-End Close (30 min)
**Actor**: Financial Analyst | **Goal**: Revenue reconciliation

```
Financial → Revenue Attribution → OPCOs (by sector)
  → Capacity Tracking (headcount allocation) → CEOCockpit (executive summary)
```

**Screens**: Financial → RevenueAttribution → OPCOs → CapacityTracking → CEOCockpit

---

## NAVIGATION STRUCTURE

### Header
- **Logo** (click → Dashboard)
- **Search** (cmd+K → find any venture/task/agent)
- **Real-time alerts** (badge count)
- **User menu** (settings, logout)

### Sidebar (Primary Navigation)
```
📊 Overview
  └─ Dashboard
  └─ Mission Control
  └─ System Map

🏢 Structure
  └─ Organization
  └─ Org Chart
  └─ Ventures
  └─ GitHub
  └─ Settings

⚙️ Operations
  └─ Tasks
  └─ Workflows
  └─ Dependencies
  └─ Bottlenecks
  └─ Decisions
  └─ Approvals
  └─ Audit
  └─ Communications

📈 Intelligence
  └─ Analytics
  └─ Revenue Attribution
  └─ Capacity Tracking
  └─ Memory
  └─ Knowledge Graph
  └─ Alerts
  └─ Activity Stream

💰 Executive
  └─ Financial
  └─ Sales
  └─ CEO Cockpit
  └─ OPCOs

🤖 Agents
  └─ Agents
  └─ Orchestrator
  └─ Automation Command

⚡ Commands
  └─ Infrastructure
  └─ Security
  └─ Repository
```

### Secondary Navigation (In-Tab)
- Tab-specific filters (status, sector, date range)
- Drill-down breadcrumbs
- Related links (e.g., Financial → Venture detail)

---

## INTERACTION PATTERNS

### Drill-Down Pattern
```
List View (e.g., Ventures table)
  ↓ (click row)
Detail View (e.g., Venture profile)
  ↓ (click related tab)
Cross-Tab Navigation (e.g., Financial)
```

### Filter & Sort Pattern
```
Cards/Table Display
  ↑ (filter sidebar)
Active Filters (chips, removable)
Results (count, empty state)
```

### Real-Time Updates
- WebSocket push for agent status changes
- Auto-refresh badges (task count, alert count)
- Notification toast (new approvals, task complete)

### Modal Pattern
- Forms (create, edit, approve)
- Confirmations (delete, submit)
- Escape closes modal
- Accessible focus management

---

## STATE MANAGEMENT

### Navigation State
- **Current tab**: URL-based (e.g., `/holdings/agents`)
- **Sidebar collapse**: LocalStorage (per-user)
- **Filters**: URL params (e.g., `?status=active`)

### Tab State
- **Scroll position**: Restored on back-navigation
- **Expanded sections**: LocalStorage (collapsible panels)
- **Selected row**: Highlighted (no page navigation)

### Global State
- **User auth**: Supabase JWT
- **Real-time subscriptions**: WebSocket connected
- **Alert count**: Live via badge

---

## RESPONSIVE BEHAVIOR

### Mobile (< 640px)
- Sidebar collapsed (hamburger icon)
- Single-column layout
- Cards stack vertically
- Table → Card view (swipe-able)
- Modal full-screen

### Tablet (640px - 1024px)
- Sidebar always visible
- 2-column layouts
- Cards 50% width
- Table condensed

### Desktop (> 1024px)
- Standard sidebar + content
- Multi-column grids
- Full interactivity
- Keyboard shortcuts enabled

---

## ACCESSIBILITY FEATURES

- **Keyboard nav**: Tab through all interactive elements
- **Screen reader**: All sections labeled with ARIA
- **Focus visible**: 2px cyan outline
- **High contrast**: Minimum 4.5:1 WCAG AA
- **Reduced motion**: Animations disabled if requested

---

## PAGE LOAD SEQUENCE

```
1. Show skeleton loaders (0ms)
2. Render sidebar + header (50ms)
3. Fetch critical data (API calls in parallel)
4. Render main content (200ms)
5. Load secondary data (analytics, graphs)
6. Enable interactivity (250ms)
7. Cache data in Redis (background)
```

**Target**: Visually complete in < 1.5s

---

**Next**: Tab Specifications (detailed requirements per tab)
