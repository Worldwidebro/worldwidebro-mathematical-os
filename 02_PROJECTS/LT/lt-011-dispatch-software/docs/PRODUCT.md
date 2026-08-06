---
name: 02_PROJECTS/LT/lt-011-dispatch-software/docs/PRODUCT
title: LT-011 — DispatchOS
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# LT-011 — DispatchOS

## Product Requirements Document (PRD)

**Product ID:** LT-011  
**Product Name:** DispatchOS  
**Product Category:** Transportation / Dispatch / Logistics / Freight  
**Product Type:** Agentic Transportation Operating System  
**Status:** Product Definition  
**Version:** 1.0  
**Owner:** Worldwidebro / VEX  
**Primary Market:** Transportation, logistics, freight, courier, fleet, and delivery companies  

---

# 1. Executive Summary

LT-011 is an agentic transportation operating system for managing the complete lifecycle of transportation work:

> **Order → Load → Match → Dispatch → Route → Pickup → Transit → Delivery → POD → Billing → Payment → Intelligence**

The system combines:
* Dispatch management
* Logistics management
* Freight management
* Fleet management
* Driver operations
* Carrier management
* Customer management
* Routing and tracking
* Document management
* Communications
* Billing and settlements
* Operational analytics
* AI agents
* Agentic workflows
* Capability/MCP integrations
* Event-driven automation

LT-011 is designed to operate as both:
1. **A transportation operating company platform**, and
2. **A SaaS/white-label platform for transportation businesses.**

The long-term objective is to make LT-011 a reusable transportation capability layer that can also power other VEX ventures such as medical courier, logistics, freight, delivery, and fleet businesses.

---

# 2. Problem

Transportation businesses commonly operate across disconnected systems:
* spreadsheets
* dispatch software
* GPS systems
* phones
* email
* SMS
* accounting software
* load boards
* carrier systems
* document storage
* customer portals
* payment systems

This creates operational problems:
* manual dispatching
* slow driver assignment
* poor visibility
* missed appointments
* delayed deliveries
* inefficient routes
* excessive phone calls
* fragmented customer communication
* document errors
* billing delays
* poor margin visibility
* repetitive administrative work
* limited operational intelligence

LT-011 addresses this by creating one event-driven operational system where agents can monitor, reason, execute, verify, and escalate work.

---

# 3. Product Vision

### Vision
> Build the intelligent operating system for moving people, goods, shipments, and freight.

LT-011 should evolve from:
**Dispatch software**  
into:  
**Transportation Operations OS**  
and eventually:  
**Agentic Transportation Network.**

---

# 4. Target Customers

## Primary customers

### Transportation companies
* trucking companies
* delivery companies
* courier companies
* fleet operators
* last-mile operators
* regional transportation companies

### Logistics companies
* 3PLs
* logistics providers
* managed transportation companies
* fulfillment operators

### Freight companies
* freight brokers
* carriers
* shippers
* freight forwarders
* independent owner-operators

### Specialized transportation
* medical courier
* pharmacy delivery
* food delivery
* retail delivery
* construction logistics
* field service
* equipment transportation

---

# 5. User Personas

## Executive
Needs:
* revenue
* margin
* utilization
* customer profitability
* fleet performance
* agent performance

## Dispatcher
Needs:
* live jobs
* available drivers
* available vehicles
* routes
* exceptions
* customer communication

## Driver
Needs:
* assignments
* navigation
* pickup instructions
* delivery instructions
* documents
* POD
* communication

## Fleet Manager
Needs:
* vehicles
* maintenance
* inspections
* utilization
* compliance

## Freight Broker
Needs:
* loads
* carriers
* rates
* tenders
* tracking
* margins
* documents

## Carrier
Needs:
* available loads
* assignments
* driver management
* POD
* settlements

## Customer
Needs:
* shipment creation
* tracking
* ETA
* documents
* invoices
* communication

## Operations Manager
Needs:
* performance
* exceptions
* SLAs
* throughput
* staffing
* cost

---

# 6. Core Product Modules

LT-011 consists of:

```text
LT-011
│
├── Executive Dashboard
├── Dispatch
├── Orders
├── Loads
├── Shipments
├── Routing
├── Live Tracking
├── Drivers
├── Vehicles
├── Fleet
├── Carriers
├── Brokers
├── Customers
├── Documents
├── Communications
├── Exceptions
├── Billing
├── Payments
├── Settlements
├── Analytics
├── Agents
├── Workflows
├── Integrations
└── Administration
```

---

# 7. MVP Scope

The MVP must prove the fundamental transportation loop.

## MVP workflow

```text
Customer
   ↓
Create Order
   ↓
Validate
   ↓
Find Driver
   ↓
Find Vehicle
   ↓
Assign
   ↓
Driver Accepts
   ↓
Pickup
   ↓
Transit
   ↓
Delivery
   ↓
POD
   ↓
Invoice
   ↓
Payment
```

## MVP modules

### Required
* Authentication
* Organizations
* Users
* Customers
* Orders
* Jobs
* Drivers
* Vehicles
* Assignments
* Dispatch board
* Route information
* Shipment status
* Driver portal
* Customer portal
* POD
* Documents
* Notifications
* Invoices
* Basic analytics
* Event ledger
* Audit log

### Deferred
* Advanced freight brokerage
* Carrier marketplace
* Predictive maintenance
* Advanced pricing
* Network optimization
* External marketplace
* Advanced AI forecasting

---

# 8. Core Pages

## Executive
```text
/overview
```
Displays:
* active jobs
* completed jobs
* delayed jobs
* drivers
* vehicles
* utilization
* revenue
* margin
* exceptions
* agent status

---

## Dispatch
```text
/dispatch
/dispatch/live
/dispatch/board
/dispatch/orders
/dispatch/jobs
/dispatch/assignments
/dispatch/exceptions
```

---

## Orders
```text
/orders
/orders/new
/orders/:id
```

---

## Freight
```text
/freight
/freight/loads
/freight/load-board
/freight/tenders
/freight/carriers
/freight/brokers
/freight/rates
/freight/documents
/freight/settlements
```

---

## Fleet
```text
/fleet
/fleet/vehicles
/fleet/drivers
/fleet/maintenance
/fleet/inspections
/fleet/compliance
```

---

## Tracking
```text
/tracking
/tracking/:shipmentId
```

---

## Customer
```text
/customer
/customer/orders
/customer/shipments
/customer/documents
/customer/invoices
/customer/messages
```

---

## Driver
```text
/driver
/driver/jobs
/driver/routes
/driver/documents
/driver/earnings
/driver/messages
```

---

## Finance
```text
/finance
/finance/rates
/finance/invoices
/finance/payments
/finance/settlements
/finance/margins
```

---

## Intelligence
```text
/analytics
/analytics/operations
/analytics/fleet
/analytics/drivers
/analytics/customers
/analytics/freight
/analytics/financial
```

---

## Agent Control
```text
/agents
/agents/:agentId
/agents/tasks
/agents/activity
/agents/approvals
```

---

# 9. Dispatch Board Requirements

The dispatch board is the primary operational workspace.

It must display:
* unassigned jobs
* assigned jobs
* accepted jobs
* en-route jobs
* pickup status
* delivery status
* delayed jobs
* completed jobs
* canceled jobs
* driver availability
* vehicle availability

Dispatcher actions:
* create
* assign
* reassign
* prioritize
* cancel
* reschedule
* notify
* escalate
* override agent recommendation

---

# 10. Order Model

An order contains:

```text
Order
├── customer
├── pickup
├── delivery
├── stops
├── cargo
├── requirements
├── appointment
├── driver
├── vehicle
├── route
├── rate
├── documents
├── status
└── timestamps
```

Order states:

```text
DRAFT
CREATED
VALIDATED
ASSIGNED
ACCEPTED
PICKUP_PENDING
PICKED_UP
IN_TRANSIT
DELIVERY_PENDING
DELIVERED
POD_PENDING
COMPLETED
CANCELED
EXCEPTION
```

---

# 11. Freight Model

A freight load contains:

```text
Load
├── shipper
├── broker
├── origin
├── destination
├── stops
├── equipment
├── weight
├── commodity
├── appointment
├── rate
├── carrier
├── driver
├── documents
├── tracking
└── settlement
```

Freight lifecycle:

```text
LOAD_CREATED
→ PRICED
→ CARRIER_SEARCH
→ TENDERED
→ ACCEPTED
→ DISPATCHED
→ PICKUP
→ IN_TRANSIT
→ DELIVERED
→ POD
→ SETTLEMENT
→ INVOICED
→ PAID
```

---

# 12. Agent Architecture

LT-011 uses specialized agents instead of one general-purpose agent.

## Core agents

```text
ORDER_AGENT
DISPATCH_AGENT
ROUTING_AGENT
MATCHING_AGENT
DRIVER_AGENT
FLEET_AGENT
TRACKING_AGENT
EXCEPTION_AGENT
FREIGHT_AGENT
CARRIER_AGENT
PRICING_AGENT
DOCUMENT_AGENT
COMPLIANCE_AGENT
CUSTOMER_AGENT
BILLING_AGENT
ANALYTICS_AGENT
```

---

# 13. Agent Responsibilities

## ORDER_AGENT
* validate orders
* identify missing information
* classify transportation requirements
* create operational jobs

## DISPATCH_AGENT
* identify available resources
* assign jobs
* prioritize jobs
* reassign jobs
* coordinate dispatch

## MATCHING_AGENT
Match:
```text
Job
+
Driver
+
Vehicle
+
Location
+
Availability
+
Skills
+
Equipment
+
Compliance
```

## ROUTING_AGENT
* calculate routes
* optimize multi-stop routes
* calculate ETA
* recalculate ETA
* identify inefficient routes

## TRACKING_AGENT
* monitor GPS
* monitor ETA
* detect deviation
* trigger events

## EXCEPTION_AGENT
* detect problems
* classify problems
* determine response
* automatically resolve eligible exceptions
* escalate others

## FREIGHT_AGENT
* manage loads
* search carriers
* manage tenders
* manage freight lifecycle

## BILLING_AGENT
* calculate charges
* validate documents
* generate invoices
* reconcile payments

---

# 14. Agentic Workflow Architecture

Every workflow follows:

```text
EVENT
 ↓
CONTEXT
 ↓
AGENT
 ↓
SKILL
 ↓
POLICY
 ↓
TOOL / MCP
 ↓
ACTION
 ↓
VERIFICATION
 ↓
EVENT
```

This creates a continuous event loop.

---

# 15. Core Workflow: Order to Delivery

```text
order.created
       ↓
ORDER_AGENT
       ↓
validate
       ↓
MATCHING_AGENT
       ↓
find resources
       ↓
ROUTING_AGENT
       ↓
calculate route
       ↓
DISPATCH_AGENT
       ↓
assignment.offer
       ↓
DRIVER_AGENT
       ↓
driver.accepted
       ↓
TRACKING_AGENT
       ↓
pickup
       ↓
transit
       ↓
delivery
       ↓
DOCUMENT_AGENT
       ↓
POD verified
       ↓
BILLING_AGENT
       ↓
invoice.created
```

---

# 16. Exception Workflow

```text
GPS / Driver / Customer Event
          ↓
   EXCEPTION_AGENT
          ↓
      CLASSIFY
          ↓
     POLICY CHECK
          ↓
  Can agent resolve?
      /          \
    YES           NO
     ↓             ↓
EXECUTE         ESCALATE
     ↓             ↓
     └──────┬──────┘
            ↓
     CUSTOMER UPDATE
            ↓
       AUDIT EVENT
```

---

# 17. Agent Permissions

Agents must not have unlimited authority.

## Level 0 — Observe
Can:
* read data
* analyze
* recommend

## Level 1 — Low-risk execution
Can:
* send notifications
* update status
* calculate routes
* create drafts

## Level 2 — Operational execution
Can:
* assign jobs
* reassign jobs
* communicate with drivers
* reschedule

## Level 3 — Financial actions
Requires policy/approval:
* change rates
* issue credits
* approve settlements
* authorize refunds

## Level 4 — Restricted
Requires human approval:
* legal/compliance decisions
* major financial commitments
* customer termination
* carrier suspension

---

# 18. Skills Architecture

Every skill follows:

```text
skill/
├── SKILL.md
├── schema.json
├── policies.yaml
├── examples/
└── tests/
```

Example:
```text
skills/dispatch/assign-driver/
```

### SKILL.md
Defines:
* purpose
* inputs
* outputs
* prerequisites
* procedure
* failure modes
* escalation conditions

### schema.json
Defines structured input/output.

### policies.yaml
Defines:
* permissions
* limits
* approval requirements
* safety constraints

---

# 19. MCP Architecture

MCPs expose external capabilities.

```text
mcp/
├── maps/
├── gps/
├── communications/
├── documents/
├── payments/
├── fleet/
└── freight/
```

Examples:
```text
maps.calculate_route()
maps.calculate_eta()

gps.get_vehicle_location()

communications.send_sms()
communications.send_email()

documents.extract()
documents.verify()

payments.create_invoice()
payments.reconcile()

freight.search_carriers()
freight.search_loads()
```

The business logic remains in LT-011.

---

# 20. Event Architecture

Important events:

```text
order.created
order.validated
order.assigned
driver.notified
driver.accepted
driver.rejected
pickup.arrived
pickup.completed
shipment.in_transit
shipment.delayed
shipment.exception
delivery.arrived
delivery.completed
pod.received
pod.verified
invoice.created
invoice.sent
payment.received
```

Every important action becomes an event.

---

# 21. Data Model

Core tables:

```text
organizations
users
customers
contacts
orders
loads
shipments
stops
drivers
vehicles
fleets
carriers
brokers
routes
assignments
rates
tenders
appointments
documents
exceptions
messages
invoices
payments
settlements
events
agent_tasks
agent_actions
audit_logs
```

---

# 22. Source of Truth

PostgreSQL is the transactional source of truth.

Supporting systems:

```text
PostgreSQL
    ↓
Transactional data

Redis
    ↓
Fast state / queues / caching

Qdrant
    ↓
Semantic retrieval

Neo4j
    ↓
Relationships / capability graph

Object Storage
    ↓
Documents / images / PODs

Event Stream
    ↓
Operational events
```

The dashboard should not invent state.
It should read operational state from the source-of-truth APIs.

---

# 23. Knowledge Graph

Neo4j should connect:

```text
Customer
   ↓
Order
   ↓
Load
   ↓
Carrier
   ↓
Driver
   ↓
Vehicle
   ↓
Route
   ↓
Shipment
```

And capabilities:

```text
Capability
   ↓
Skill
   ↓
Agent
   ↓
MCP
   ↓
Repository
   ↓
Service
```

This allows the larger VEX system to discover reusable transportation capabilities.

---

# 24. Financial Model

LT-011 should track:

### Revenue
* dispatch fees
* transportation revenue
* freight margin
* SaaS subscriptions
* transaction fees
* tracking fees
* premium AI
* API fees
* white-label licensing

### Costs
* driver costs
* carrier costs
* fuel
* tolls
* maintenance
* insurance
* software
* communications
* AI inference
* infrastructure
* payment processing
* labor

### Metrics

```text
Revenue
Gross Revenue
Net Revenue
Gross Margin
Contribution Margin
Cost per Load
Cost per Shipment
Revenue per Vehicle
Revenue per Driver
Revenue per Customer
```

---

# 25. SaaS Pricing Architecture

Final pricing should be validated against competitors and actual operating economics, but the product should support:
* **Starter:** Small fleet / small dispatch operation.
* **Professional:** Growing transportation company.
* **Enterprise:** Large fleet / 3PL / broker / multi-location.
* **Usage Charges:** discretionary fees for tracking, AI actions, API usage, or document extractions.
* **White Label:** Custom enterprise deployment.

---

# 26. Analytics

## Operations
* on-time delivery
* utilization
* jobs/day
* driver productivity
* route efficiency
* exception rate

## Fleet
* utilization
* downtime
* maintenance
* cost/mile

## Freight
* revenue/load
* cost/load
* margin/load
* carrier performance
* lane performance

## Customers
* shipment volume
* revenue
* margin
* SLA performance
* retention

## Agents
* tasks
* success rate
* failure rate
* escalation rate
* execution time
* cost
* revenue enabled

---

# 27. Action Ledger

Every agent action should be recorded:

```text
agent
workflow
skill
event
timestamp
user
organization
tool
input
output
compute_cost
human_equivalent_cost
revenue_enabled
result
approval
```

This allows LT-011 to calculate:
> **What did automation cost and what economic value did it create?**

---

# 28. Repository Structure

```text
LT-011-dispatch-os/
│
├── apps/
│   ├── dispatch-web/
│   ├── driver-app/
│   ├── customer-portal/
│   ├── admin-console/
│   └── public-tracking/
│
├── agents/
├── skills/
├── workflows/
├── services/
├── domain/
├── events/
├── mcp/
├── db/
├── docs/
├── tests/
└── infra/
```

---

# 29. Documentation

Required documentation:

```text
docs/
├── PRODUCT.md
├── BUSINESS-MODEL.md
├── DOMAIN-MODEL.md
├── DISPATCH.md
├── LOGISTICS.md
├── FREIGHT.md
├── FLEET.md
├── DRIVER-OPERATIONS.md
├── CUSTOMER-OPERATIONS.md
├── BILLING.md
├── PRICING.md
├── COMPLIANCE.md
├── AGENT-ARCHITECTURE.md
├── WORKFLOWS.md
├── EVENTS.md
├── MCP.md
├── API.md
├── DATA-MODEL.md
├── SECURITY.md
├── SOP.md
└── RUNBOOK.md
```

---

# 30. Relationship to Other VEX Ventures

LT-011 is a reusable transportation capability layer.

For example:

```text
LT-011
│
├── dispatch
├── routing
├── tracking
├── fleet
├── driver
├── freight
├── carrier
├── billing
└── communication
       │
       ├──────────────┐
       ▼              ▼
    LT-005         Future
 Medical          Transport
 Courier           Ventures
```

LT-005 can specialize LT-011 for medical transportation rather than rebuilding dispatch infrastructure.

---

# 31. Security Requirements

The system must provide:
* organization isolation
* role-based access
* agent permissions
* audit logs
* encrypted credentials
* encrypted sensitive data
* API authentication
* rate limiting
* secure document storage
* approval controls
* data retention policies
* tenant isolation

---

# 32. Compliance Architecture

Compliance should be configurable by transportation type.
The system should support:
* driver qualification
* vehicle documentation
* insurance
* inspections
* licensing
* customer-specific requirements
* shipment-specific requirements
* document expiration
* operational policies

Compliance agents should **flag and escalate** rather than autonomously make regulated/legal determinations unless explicitly authorized by policy and appropriate human oversight.

---

# 33. Non-Functional Requirements

### Performance
Dashboard should feel near-real-time.

### Availability
Transportation operations require high availability.

### Observability
Every:
```text
event
agent action
workflow
API request
integration
failure
```
should be observable.

### Recoverability
Failed workflows must be retryable and idempotent.

### Auditability
Critical operational and financial actions must be traceable.

---

# 34. Definition of Done

A feature is not complete merely because the UI exists.
Each capability requires:
```text
SKILL.md
+
schema.json
+
policies.yaml
+
implementation
+
event definitions
+
agent integration
+
MCP/tool integration
+
unit tests
+
integration tests
+
E2E tests
+
observability
+
audit logging
+
documentation
```

---

# 35. MVP Acceptance Criteria

LT-011 MVP is complete when a test customer can:
1. Create an account.
2. Create a customer.
3. Create an order.
4. Enter pickup and delivery.
5. Validate the order.
6. Find available drivers.
7. Assign a driver.
8. Driver receives assignment.
9. Driver accepts.
10. Dispatcher sees assignment.
11. Shipment becomes active.
12. Driver updates status.
13. Customer sees status.
14. Delivery is completed.
15. Driver uploads POD.
16. POD is verified.
17. Invoice is generated.
18. Customer receives invoice.
19. Payment is recorded.
20. Complete event history is available.
21. Agent actions are logged.
22. Exceptions can be escalated.
23. Operations dashboard reflects the transaction.

---

# 36. Phase Roadmap

## Phase 0 — Foundation
* repository
* architecture
* database
* authentication
* organizations
* event model
* permissions

## Phase 1 — Dispatch MVP
* orders
* jobs
* drivers
* vehicles
* assignments
* dispatch board
* driver portal
* customer portal

## Phase 2 — Tracking
* GPS
* routes
* ETA
* live tracking
* geofencing
* exceptions

## Phase 3 — Documents & Billing
* POD
* BOL
* invoices
* payments
* settlements

## Phase 4 — Agentic Operations
* dispatch agent
* matching agent
* routing agent
* tracking agent
* exception agent
* billing agent

## Phase 5 — Freight
* loads
* carriers
* brokers
* tendering
* load board
* rate management

## Phase 6 — Intelligence
* profitability
* forecasting
* predictive exceptions
* carrier scoring
* route optimization
* customer intelligence

## Phase 7 — Platform
* SaaS
* API
* white-label
* marketplace
* capability reuse
* multi-venture deployment

---

# 37. North-Star Metrics

The primary product metrics should be:

### Operational
**On-Time Delivery Rate**

### Efficiency
**Cost per Completed Shipment**

### Utilization
**Revenue per Vehicle**

### Automation
**Percentage of Eligible Tasks Completed Without Human Intervention**

### Reliability
**Successful Workflow Completion Rate**

### Financial
**Contribution Margin per Shipment**

### Customer
**Customer Retention / Expansion**

### Agentic
**Revenue Enabled per Automated Agent Action**

---

# 38. North-Star Product Loop

```text
             MORE CUSTOMERS
                   ↓
             MORE SHIPMENTS
                   ↓
                MORE DATA
                   ↓
          BETTER AGENT CONTEXT
                   ↓
          BETTER DECISIONS
                   ↓
             MORE AUTOMATION
                   ↓
             LOWER COST
                   ↓
            BETTER MARGINS
                   ↓
            BETTER SERVICE
                   ↓
             MORE CUSTOMERS
```

---

# 39. Final Product Definition

LT-011 should ultimately be understood as five products in one:

```text
┌────────────────────────────────────────────┐
│                 LT-011                     │
│                                            │
│  1. DISPATCH PLATFORM                     │
│     Coordinate transportation operations   │
│                                            │
│  2. LOGISTICS OS                           │
│     Manage movement and visibility         │
│                                            │
│  3. FREIGHT PLATFORM                       │
│     Manage loads, carriers and rates      │
│                                            │
│  4. AGENTIC OPERATIONS ENGINE              │
│     Automate operational decisions         │
│                                            │
│  5. TRANSPORTATION INTELLIGENCE PLATFORM   │
│     Turn operational data into decisions   │
└────────────────────────────────────────────┘
```

### The ultimate LT-011 equation

**Transportation demand**
→ **orders/loads**
→ **matching**
→ **dispatch**
→ **routing**
→ **execution**
→ **tracking**
→ **exception management**
→ **delivery**
→ **POD**
→ **billing**
→ **payment**
→ **data**
→ **intelligence**
→ **better operations**
→ **higher margin**
→ **more transportation volume**

That is the core PRD and business architecture for **LT-011 DispatchOS**.
