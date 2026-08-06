---
name: 02_PROJECTS/LT/lt-011-dispatch-software/docs/DOMAIN-MODEL
title: DispatchOS Domain Model Specifications
desc: ...
tags: []
sources: []
created: 2026-08-06T05:46:10Z
updated: 2026-08-06T05:46:10Z
---

# DispatchOS Domain Model Specifications

This document defines the schemas, state machines, and relational structures of the primary entities in DispatchOS (LT-011).

## 1. State Transitions

### A. Load State Machine
```text
DRAFT ──► TENDERED ──► ASSIGNED ──► DISPATCHED ──► IN_TRANSIT ──► DELIVERED ──► INVOICED ──► SETTLED
  │                                                                 ▲
  └───────────────► CANCELED (From any pre-delivery state) ──────────┘
```

### B. Tender State Machine
```text
SENT ──► ACCEPTED ──► EXPIRED
  │
  └──► REJECTED
```

---

## 2. Entity Database Schema Mapping

```sql
-- PostgreSQL / Supabase Schema definitions for DispatchOS

-- Accounts & Entities
CREATE TABLE brokers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_name TEXT NOT NULL,
  dot_number TEXT UNIQUE,
  credit_score INT,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE carriers (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_name TEXT NOT NULL,
  mc_number TEXT UNIQUE,
  dot_number TEXT UNIQUE,
  insurance_expiry DATE NOT NULL,
  status TEXT DEFAULT 'ACTIVE'
);

-- Core Freight
CREATE TABLE loads (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  reference_number TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'DRAFT',
  origin JSONB NOT NULL, -- { address, lat, lng, scheduled_pickup_window }
  destination JSONB NOT NULL, -- { address, lat, lng, scheduled_delivery_window }
  weight_lbs NUMERIC(10, 2),
  carrier_id UUID REFERENCES carriers(id),
  driver_id UUID,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Financials
CREATE TABLE rate_confirmations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  load_id UUID REFERENCES loads(id) ON DELETE CASCADE,
  broker_id UUID REFERENCES brokers(id),
  base_rate_usd NUMERIC(10, 2) NOT NULL,
  fuel_surcharge_usd NUMERIC(10, 2) DEFAULT 0.00,
  detention_hourly_usd NUMERIC(10, 2) DEFAULT 0.00,
  pdf_url TEXT,
  verified BOOLEAN DEFAULT false
);

CREATE TABLE tenders (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  load_id UUID REFERENCES loads(id) ON DELETE CASCADE,
  carrier_id UUID REFERENCES carriers(id),
  offer_price_usd NUMERIC(10, 2) NOT NULL,
  status TEXT DEFAULT 'SENT',
  expires_at TIMESTAMPTZ NOT NULL
);

-- Documents & Proof
CREATE TABLE shipment_documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  load_id UUID REFERENCES loads(id) ON DELETE CASCADE,
  doc_type TEXT NOT NULL, -- 'BOL', 'POD', 'WEIGHT_TICKET'
  file_url TEXT NOT NULL,
  ocr_raw TEXT,
  signature_present BOOLEAN DEFAULT false,
  signed_at TIMESTAMPTZ
);
```

---

## 3. Financial Settlement Formula

For each completed load, gross profit margin is calculated dynamically upon document verification:

\[\text{Gross Profit} = \text{Revenue} - \left( \text{Carrier Cost} + \text{Driver Pay} + \text{Fuel} + \text{Tolls} + \text{Detention} \right)\]

Where:
*   **Revenue:** `base_rate` + `fuel_surcharge` + `detention` collected from broker.
*   **Carrier Cost:** Settlement fee released to carrier account.
*   **Driver Pay:** Dispatched mileage rate + geofence detention hours.
*   **Detention:** Calculated automatically by `TRACKING_AGENT` when a vehicle's geofenced dwell time at stop $> 2$ hours.
