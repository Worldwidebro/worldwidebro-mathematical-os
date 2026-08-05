# DispatchOS Freight Domain Model

This document outlines the freight, logistics, and dispatch schemas mapping our entities and state machines in DispatchOS (LT-011).

```
                     [ Opportunity / Quote ]
                                │
                                ▼
                       [ Load (DRAFT) ]
                                │
                                ▼ (Tender posted)
                       [ Load (TENDERED) ]
                                │
         ┌──────────────────────┴──────────────────────┐
         ▼ (Accepted)                                  ▼ (Declined / Expired)
  [ Load (ASSIGNED) ]                           [ Load (CANCELED) ]
         │
         ▼ (Driver dispatched)
  [ Load (DISPATCHED) ]
         │
         ▼ (Arrived at pickup / BOL signed)
  [ Load (IN TRANSIT) ]
         │
         ▼ (Arrived at destination / POD uploaded)
  [ Load (DELIVERED) ]
         │
         ▼ (POD verified / OCR matched)
  [ Load (INVOICED) ]
         │
         ▼ (Payment cleared)
  [ Load (SETTLED) ]
```

---

## 1. Core Data Entities

### A. Load (The Central Unit)
Represents a specific cargo shipment moving from Origin to Destination.
*   `load_id`: UUID (Primary Key)
*   `reference_number`: String (Broker/Carrier tracking reference)
*   `status`: Enum (`DRAFT`, `TENDERED`, `ASSIGNED`, `DISPATCHED`, `IN_TRANSIT`, `DELIVERED`, `INVOICED`, `SETTLED`, `CANCELED`)
*   `origin`: JSON `{ address, lat, lng, contact_phone, scheduled_pickup_window }`
*   `destination`: JSON `{ address, lat, lng, contact_phone, scheduled_delivery_window }`
*   `weight_lbs`: Numeric
*   `dimensions`: JSON `{ length_in, width_in, height_in }`
*   `hazmat`: Boolean
*   `carrier_id`: UUID (Foreign Key $\rightarrow$ Carrier)
*   `driver_id`: UUID (Foreign Key $\rightarrow$ Driver)
*   `vehicle_id`: UUID (Foreign Key $\rightarrow$ Vehicle)

### B. Rate Confirmation (Financial Contract)
Binds the carrier to execute the load at the agreed price.
*   `rate_confirmation_id`: UUID
*   `load_id`: UUID (Foreign Key $\rightarrow$ Load)
*   `broker_id`: UUID (Foreign Key $\rightarrow$ Broker)
*   `base_rate_usd`: Numeric
*   `fuel_surcharge_usd`: Numeric
*   `accessorial_rates`: JSON `{ detention_hourly, layover_flat, lumper_reimbursement }`
*   `rate_con_pdf_url`: String (Storage link)
*   `verified`: Boolean

### C. Tender (The Transaction Offer)
*   `tender_id`: UUID
*   `load_id`: UUID (Foreign Key $\rightarrow$ Load)
*   `carrier_id`: UUID (Foreign Key $\rightarrow$ Carrier)
*   `offer_price_usd`: Numeric
*   `status`: Enum (`SENT`, `ACCEPTED`, `REJECTED`, `EXPIRED`)
*   `expires_at`: Timestamp

### D. Documents (BOL & POD)
*   `document_id`: UUID
*   `load_id`: UUID (Foreign Key $\rightarrow$ Load)
*   `type`: Enum (`BOL`, `POD`, `LUMPER_RECEIPT`, `WEIGHT_TICKET`)
*   `file_url`: String
*   `ocr_extracted_text`: JSON
*   `signature_present`: Boolean
*   `signed_by`: String
*   `signed_at`: Timestamp

---

## 2. Actors & Relationship Graph

```
  [ Broker ] ────( posts loads )───► [ DispatchOS ]
      │                                    ▲
      │ (sends rate confirmation)          │
      ▼                                    │
  [ Carrier ] ───( assigns shifts )───► [ Driver ]
```

*   **Broker:** Sets cargo requirements, posts opportunities, issues rate confirmations.
*   **Carrier:** Manages a fleet of vehicles and drivers, bids on tenders, and delegates assignments.
*   **Driver:** Interfaces with mobile app, updates GPS telemetry, records BOL/POD scans at stops.

---

## 3. Automation Workflows & Agent Roles

### A. Order-to-Dispatch (freight-agent)
1.  `freight-agent` monitors broker portals or parsed email attachments.
2.  If a new Rate Confirmation PDF is detected, it runs OCR extraction to parse `base_rate`, stops, and weight.
3.  Creates a `Load` in `DRAFT` status and links it to the broker.
4.  Tenders the load to appropriate carriers based on geographical historical performance.

### B. Transit & Tracking (tracking-agent)
1.  `tracking-agent` polls active vehicle GPS signals (via Traccar integration).
2.  Recalculates routing ETAs every 10 minutes.
3.  If ETA exceeds destination appointment windows by $\ge 30$ minutes, it logs an Exception event and alerts the broker.
4.  Automatically logs detention time when the vehicle spends $> 2$ hours geofenced at a loading dock.

### C. Delivery-to-Invoice (billing-agent)
1.  Once the driver uploads a POD image at the destination, `billing-agent` triggers an OCR layout parser.
2.  Verifies that the POD matches the `Load` ID, carries a signature, and matches the weight ticket.
3.  Changes the Load status to `INVOICED` and generates a billing invoice PDF using the ReportLab package.
4.  Releases split payments via Stripe Connect.
