# DispatchOS Core Agents

This document defines the 12 primary software agents operating within DispatchOS (LT-011).

| Agent Name | Primary Responsibility | Active Skills | Consumed MCPs |
| :--- | :--- | :--- | :--- |
| **ORDER_AGENT** | Intake, validation, and schema sanitization of new delivery jobs. | `dispatch/create-job` | `documents` |
| **DISPATCH_AGENT** | Recommends, queues, and assigns drivers to pending loads. | `dispatch/assign-driver` | `communication` |
| **ROUTING_AGENT** | Computes optimal paths, stops, and ETAs based on traffic. | `routing/optimize-route` | `maps` |
| **MATCHING_AGENT** | Matchmaker heuristics linking carriers, vehicles, and cargo loads. | `freight/find-carrier` | `freight` |
| **DRIVER_AGENT** | Manages driver profiles, schedules, shifts, and compliance logs. | `driver/onboard-driver` | `documents` |
| **FLEET_AGENT** | Tracks vehicle telemetry, maintenance logs, and fuel logs. | `fleet/track-vehicle` | `gps` |
| **TRACKING_AGENT** | Real-time GPS location monitoring and geofence verification. | `routing/recalculate-eta` | `gps` |
| **EXCEPTION_AGENT** | Identifies delays, accidents, or missed slots; triggers alerts. | `dispatch/resolve-exception` | `communication` |
| **FREIGHT_AGENT** | Coordinates broker tenders, rates, and carrier agreements. | `freight/tender-load` | `freight` |
| **CUSTOMER_AGENT** | Handles customer inquiries, ETA updates, and quote generation. | `customer/process-inquiry` | `communication` |
| **BILLING_AGENT** | Executes OCR checks on PODs/BOLs, generates letters, pays splits. | `billing/validate-pod` | `payments` |
| **ANALYTICS_AGENT**| Calculates operational gross margins, cost-per-mile, and delay risks. | `analytics/report-margins` | `payments` |

---

## Agent Supervision & Policies

Every agent operating in DispatchOS executes under strict security bounds defined in the policy registers:
1.  **Financial Caps:** `BILLING_AGENT` and `payments` MCP calls exceeding $5,000 USD require manual human-in-the-loop (HITL) clearance.
2.  **Telemetry Policies:** GPS lookups run strictly through the geofence checker to mask driver PII when off-shift.
3.  **Exception Escalation:** `EXCEPTION_AGENT` can resolve delays under 30 minutes automatically by firing an SMS trigger; deviations greater than 30 minutes require escalation to the operations manager.
