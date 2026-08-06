# DispatchOS Freight Marketplaces & Bidding Guide

This guide outlines where to source freight loads (for bidding) and where to acquire owner-operators (for dispatching).

---

## 1. Where to Bid on Freight Loads

To secure cargo runs and generate revenue, DispatchOS integrations target three primary tiers of freight markets:

### A. High-Volume Commercial Load Boards (Spot Market)
These are standard industry load boards where shippers and brokers post active loads daily.
*   **DAT One (DAT Power):** The industry standard. Features real-time spot rates, lane pricing history, and instant carrier checks.
*   **Truckstop.com:** The second largest portal, particularly strong for flatbed and specialized LTL freight.
*   **123Loadboard:** A cost-effective board popular among independent logistics providers and regional dispatchers.

### B. Brokerage Directories & Portals (Contract & Route Bidding)
Major third-party logistics (3PL) companies host private bidding portals. Carriers bid on loads here to establish long-term contract lanes:
*   **C.H. Robinson Navisphere:** Access to the largest private shipper network in North America.
*   **Coyote Logistics (UPS):** High volume of consumer packaged goods and dry van loads.
*   **J.B. Hunt 360:** Instant bidding and booking interface for contract freight.
*   **Echo Global Logistics / Convoy Network:** Access to digitized dispatch bookings.

### C. Government & Institutional Bidding (High-Value / Low-Risk)
State and federal logistics requests offer stable, highly profitable contracts:
*   **SAM.gov (System for Award Management):** Sourced through federal agency requests for transportation, mail transit routes, and regional distribution.
*   **USASpending.gov:** Used to trace active logistical awards and identify General Contractors (GCs) looking for logistics subcontractors in North Carolina.
*   **FEMA Logistics (Disaster Relief):** Immediate dispatch bids for moving water, food, and emergency supplies during weather events (paying up to 3x standard spot rates).

---

## 2. Where to Source and Dispatch Owner-Operators

To move the loads we bid on, dispatchers source equipment and drivers using:

### A. Carrier Directories
*   **DAT Directory:** Search through 100,000+ active trucking companies filtered by location, operating authority (MC/DOT), and safety rating.
*   **Carrier411:** Essential compliance check portal to verify carrier insurance status and safety scores before dispatching a load.
*   **Trucker Path:** Dedicated network containing millions of truck drivers where dispatchers can post open load availability.

### B. Fleet & Truck Rentals (For Short-Term Dispatch)
If operators need trucks/equipment:
*   **Fluid Truck / COOP by Ryder:** Instant rental of dry vans, cargo vans, and box trucks on an hourly or daily rate.
*   **Penske / Ryder Logistics:** Long-term tractor leases for CDL drivers.

---

## 3. The Bidding & Dispatching SOP

```
   1. FIND LOAD  ──► Search DAT One / J.B. Hunt 360 for high-margin routes
                      │
                      ▼
   2. CALC COST  ──► Run Routing/Pricing engine to determine margin
                      │
                      ▼
   3. PLACE BID  ──► Bid on load portal (e.g. Navisphere)
                      │
                      ▼ (Bid is won and Rate Confirmation is received)
   4. INGEST     ──► Email Rate Confirmation PDF to DispatchOS (Parses stop addresses)
                      │
                      ▼
   5. MATCH      ──► Query DAT Directory / active drivers database
                      │
                      ▼
   6. DISPATCH   ──► Tender load to the matched driver's Driver App
```
