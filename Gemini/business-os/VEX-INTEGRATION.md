# vex: Delegation Network Orchestration Layer

## Current State
vex is a static portfolio showcase.

## New State
vex is the orchestration layer showing real-time delegation flows across the network.

---

## 1. Database Schema (Supabase / Postgres Integration)

The frontend maps real-time UI components to PostgreSQL tables:

### 1.1 `ventures`
Tracks venture status, MRR, and completion percentage.
- `id` (UUID, Primary Key)
- `venture_id` (VARCHAR, e.g. `CON-001`)
- `name` (VARCHAR)
- `category` (VARCHAR)
- `status` (VARCHAR)
- `revenue_estimate` (DECIMAL)

### 1.2 `venture_runs`
Triggers n8n/Fractal workflow runs.
- `id` (UUID, Primary Key)
- `venture_id` (VARCHAR)
- `sector` (VARCHAR)
- `goal` (TEXT)
- `status` (VARCHAR, e.g., `running`, `done`)

### 1.3 `phase_executions`
Logs durations and costs for the 14 phases.
- `id` (UUID, Primary Key)
- `venture_id` (VARCHAR)
- `phase_id` (INT)
- `status` (VARCHAR)
- `cost_usd` (DECIMAL)
- `duration_seconds` (INT)
- `completed_at` (TIMESTAMP)

### 1.4 `decisions`
Stores audit trails of agentic actions.
```json
{
  "decision_id": "D-477",
  "timestamp": "2026-07-25T10:15:00Z",
  "venture_id": "CON-001",
  "sector": "construction",
  "question": "Submit high-rise bid #2041?",
  "framework": "Strategic Fit",
  "agents_involved": ["estimator", "analyst", "risk"],
  "recommendation": "Approve submission",
  "confidence_score": 92,
  "status": "pending_human_approval"
}
```

---

## 2. New Routes

### /network/opportunities
Displays all open delegation requests across the network.

**Sub-routes:**
- `/network/staffing-to-construction`: Open contractor roles posted by CON, waiting for STA to fill
- `/network/construction-to-realestate`: Completed projects ready for RE to manage
- `/network/realestate-to-finance`: Properties needing financing, sourced by RE
- `/network/finance-to-investment`: Structured deals ready for capital deployment

**Data Displayed:**
- Opportunity ID
- Requesting Venture
- Receiving Venture
- Opportunity Type
- Value Estimate
- Expected Margin
- Timeline
- Status (Pending, Accepted, In Progress)

### /network/delegation
Tracks all delegation requests (pending, active, completed).

**Sub-routes:**
- `/network/delegation/queue`: Pending delegation requests (not yet accepted)
- `/network/delegation/active`: In-progress delegations (accepted, work underway)
- `/network/delegation/completed`: Completed delegations with captured margins

**Data Displayed:**
- Delegation ID
- Requesting Venture
- Receiving Venture
- Opportunity Type
- Value
- Margin Captured
- Completion Date
- Status

### /network/margins
Displays margin captured across the network, by venture and by type.

**Sub-routes:**
- `/network/margins/staffing-margins`: Labor arbitrage margin captured by STA
- `/network/margins/project-margins`: Project execution margin captured by CON
- `/network/margins/property-margins`: Property management margin captured by RE
- `/network/margins/capital-margins`: Financing margin captured by FIN
- `/network/margins/delegation-margins`: Internal transfer pricing captured by OPS

**Data Displayed:**
- Venture
- Margin Type
- Margin Captured (MTD, QTD, YTD)
- Margin % (actual vs. target)
- Trend (improving, declining, stable)

### /network/health
Displays network health metrics.

**Data Displayed:**
- Delegation Velocity: Work items flowing between sectors per week
- Network Margin: Total margin captured across all handoffs
- Cross-Sector Revenue %: % of revenue from delegation (vs. direct sales)
- Placement Velocity: Time from opportunity creation to work completion
- Bottlenecks: Where delegation is breaking down

### /ventures/[venture-id]
Displays individual venture details, including delegation activity.

**Data Displayed:**
- Venture ID
- Industry
- Current Phase
- Delegation Requests Sent (to other ventures)
- Delegation Requests Received (from other ventures)
- Margin Captured (from delegations)
- KPIs (industry-specific)

## Dashboard Views

### Network Overview
- Total delegations (pending, active, completed)
- Total margin captured (MTD, QTD, YTD)
- Delegation velocity (work items/week)
- Network health score (composite metric)

### Venture Performance
- Revenue by venture
- Margin by venture
- Delegation activity by venture
- KPIs by venture

### Delegation Flow
- Visual map of delegation flows between ventures
- Bottleneck identification
- Margin capture at each handoff

## Integration with Knowledge Graph

All vex routes pull data from Knowledge Graph:
- Delegation requests logged as edges between venture nodes
- Margins captured logged as properties on edges
- Completion dates logged as timestamps
- Performance metrics aggregated from individual delegation events

## Monday Launch

### Goal
Prove one complete delegation cycle visible in vex.

### Steps
1. CON-001 posts 5 open contractor roles → Logged in `/network/opportunities/staffing-to-construction`
2. STA-001 receives delegation → Status changes to "Accepted" in `/network/delegation/active`
3. STA-001 places 3 contractors → Status changes to "Completed" in `/network/delegation/completed`
4. Margin captured ($X) → Displayed in `/network/margins/staffing-margins`
5. Dashboard shows: "3 placements, $X margin, $Y revenue to STA"

### Success Metric
One complete delegation cycle visible in vex, from opportunity creation to margin capture.
