# DispatchOS Product & UI Wireframe Map

This document serves as the UI/UX blueprints for all screens in DispatchOS (LT-011).

## 1. Executive Dashboard (`/overview`)
Provides aggregate stats on operational health, active loads, exceptions, and live dispatch events.

```text
┌─────────────────────────────────────────────────────────────┐
│ LT-011 DISPATCH OS                         🔔 Admin          │
├──────────┬──────────────────────────────────────────────────┤
│          │                                                  │
│ Overview │  TODAY                                           │
│ Dispatch │  248 Jobs       192 Active       31 Exceptions  │
│ Orders   │                                                  │
│ Freight  │  ┌────────────────────┐ ┌─────────────────────┐ │
│ Drivers  │  │ LIVE DISPATCH MAP  │ │ OPERATIONS HEALTH   │ │
│ Vehicles │  │                    │ │                     │ │
│ Routes   │  │      • • • •       │ │ On time     94.2%   │ │
│ Tracking │  │    •     •         │ │ Utilization 82%     │ │
│ Customers│  │ •       •          │ │ Exceptions   7      │ │
│ Finance  │  │                    │ │ Revenue   $24,820    │ │
│ Analytics│  └────────────────────┘ └─────────────────────┘ │
│ Agents   │                                                  │
│ Settings │  ACTIVITY                                        │
│          │  Driver assigned → Load accepted → Route active │
└──────────┴──────────────────────────────────────────────────┘
```

---

## 2. Dispatch Views
*   **Live Board (`/dispatch/live`):** Renders mapping overlays and job queues.
*   **Exceptions Control (`/dispatch/exceptions`):** Centralises warning triggers (e.g., driver delays, vehicle issues).

```text
┌──────────────────────────────────────────────────────────────┐
│ LIVE DISPATCH                              [+ Create Job]     │
├───────────────────────────────────┬──────────────────────────┤
│                                   │                          │
│          LIVE MAP                 │ ACTIVE JOBS              │
│                                   │                          │
│       🚚 →                         │ #10482  En Route        │
│              🚚                    │ #10483  Pickup          │
│   🚚                            🚚 │ #10484  Delayed         │
│                                   │ #10485  Delivered        │
│                                   │                          │
├───────────────────────────────────┴──────────────────────────┤
│ EXCEPTIONS                                                   │
│ ⚠ Driver delayed   ⚠ Vehicle unavailable   ⚠ Late pickup   │
└──────────────────────────────────────────────────────────────┘
```

---

## 3. Order & Freight Lifecycle (`/orders/:id`)
Tracks the linear progress:
`ORDER` $\rightarrow$ `CUSTOMER` $\rightarrow$ `PICKUP` $\rightarrow$ `DELIVERY` $\rightarrow$ `REQUIREMENTS` $\rightarrow$ `RATE` $\rightarrow$ `ASSIGNMENT` $\rightarrow$ `TRACKING` $\rightarrow$ `POD` $\rightarrow$ `INVOICE`.

### Load Board (`/freight/load-board`)
Used by dispatch agents to coordinate with external carriers.

```text
┌─────────────────────────────────────────────────────────────┐
│ LOAD BOARD                                                   │
├────────────┬────────────┬────────────┬───────────┬──────────┤
│ Load       │ Origin     │ Destination│ Equipment │ Rate     │
├────────────┼────────────┼────────────┼───────────┼──────────┤
│ #8821      │ Charlotte  │ Atlanta    │ Dry Van   │ $1,250   │
│ #8822      │ Charlotte  │ Dallas     │ Reefer    │ $3,400   │
│ #8823      │ Raleigh    │ Miami      │ Flatbed   │ $2,850   │
└────────────┴────────────┴────────────┴───────────┴──────────┘
```

---

## 4. Portals

### A. Driver Portal (`/driver`)
*   Provides clear delivery checkpoints.
*   Triggers location logging and camera scan gates (e.g. proof of delivery signature).

```text
/driver

TODAY
──────────────────────

NEXT JOB
Charlotte → Atlanta

Pickup
10:30 AM

Delivery
2:45 PM

[START ROUTE]

──────────────────────

Today's Jobs
✓ Job 10481
→ Job 10482
○ Job 10483
```

### B. Customer Portal (`/customer`)
*   Exposes ETA tracking, invoice histories, and chat boxes.

```text
/customer

MY SHIPMENTS

#8821
Charlotte → Atlanta
IN TRANSIT
ETA 2:45 PM

[TRACK SHIPMENT]

────────────────

Recent
Delivered
Invoices
Documents
Requests
...
```

---

## 5. Agent Control Center (`/agents`)
Visualizes agent health, average execution times, and pipeline success logs.

```text
/agents

AGENT CONTROL CENTER

┌──────────────────────────────────────────────────────┐
│ DISPATCH AGENT                    ● RUNNING           │
│ Tasks: 42   Success: 98.4%   Avg: 1.2 sec            │
├──────────────────────────────────────────────────────┤
│ ROUTING AGENT                      ● RUNNING           │
│ Tasks: 31   Success: 97.1%                          │
├──────────────────────────────────────────────────────┤
│ FREIGHT AGENT                      ● RUNNING           │
│ Tasks: 18   Success: 94.8%                          │
└──────────────────────────────────────────────────────┘
```
