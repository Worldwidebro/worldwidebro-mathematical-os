# DispatchOS Agentic Workflows

This document specifies the step-by-step logic, inputs, triggers, and state progressions for the core operational loops.

## 1. Order-to-Delivery Workflow (Logistics Core)

```text
CUSTOMER CREATES ORDER
          │
          ▼ [Event: order.created]
ORDER_AGENT (Validates structure, cargo weight, dimensions)
          │
          ▼ [Event: order.validated]
DISPATCH_AGENT (Checks driver availability ledger)
          │
          ▼
ROUTING_AGENT (Queries Maps MCP to compute path mileage)
          │
          ▼
MATCHING_AGENT (Selects optimal driver + vehicle pair)
          │
          ▼
DRIVER_AGENT (Sends mobile push notification; waits for response)
          │
          ▼ [Event: driver.accepted]
TRACKING_AGENT (Polls Traccar GPS signals; geofences origin warehouse)
          │
          ▼ [Event: pickup.started]
EXCEPTION_AGENT (Continually evaluates ETA; resolves minor deviations)
          │
          ▼ [Event: delivery.completed]
POD_AGENT (Runs OCR on camera-uploaded delivery receipt)
          │
          ▼ [Event: pod.verified]
BILLING_AGENT (Issues invoice PDF and triggers Stripe split payouts)
```

---

## 2. Freight Tendering Workflow (Carrier/Broker Integration)

```text
LOAD CREATED (Broker portal upload or Rate Confirmation PDF OCR scan)
     │
     ▼
LOAD_AGENT (Extracts rate tables and cargo requirements)
     │
     ▼
RATE_ENGINE (Calculates minimum profitable baseline based on fuel costs)
     │
     ▼
CARRIER_AGENT (Bids or posts target load to carrier network)
     │
     ▼
CARRIER ACCEPTS (Tender converted to binding assignment)
     │
     ▼
RATE CONFIRMATION (Digitally signed and committed to database)
     │
     ▼
DISPATCHED (Driver dispatched; GPS tracking initialized)
     │
     ▼
POD VERIFICATION (OCR checks seal numbers and consignee signature)
     │
     ▼
SETTLEMENT (Release payment ledger splits to broker/carrier accounts)
```

---

## 3. Exception Resolution Workflow (Durable Agent Recovery)

```text
GPS TELEMETRY EVENT
   │
   ▼ (ETA deviation detected by Tracking Agent)
EXCEPTION_AGENT (Classifies exception category: Traffic, Weather, Delay, Breakdown)
   │
   ├── [ETA delay < 30 min] ──► Automatically notify customer via SMS/Novu trigger
   │
   └── [ETA delay >= 30 min or Breakdown]
         │
         ▼
     HUMAN REVIEW (Flag block in Operations Dashboard and suggest recovery routes)
         │
         ▼
     DECISION INGEST (Dispatcher confirms route change or vehicle replacement)
         │
         ▼
     AUDIT LOGGED (Record decision outcome in Neo4j to update agent confidence)
```
