# TRACKING — Telemetry Implementation & Webhook Protocols

> **Canonical Document ID:** `DOC-TRK-CAM-001`  
> **Authority:** Observability (CP-041)  
> **Status:** ACTIVE SPECIFICATION  
> **Canonical Aliases:** [[CAMPAIGNS/CONVERSION-TRACKING.md]], [[CAMPAIGNS/EVENT-TRACKING.md]]

---

## 1. Webhook & Event Protocol

All telemetry events fire to our local ingest gateway (`http://100.87.214.70:4000/events`):
```json
{
  "event_id": "EVT-001-0984",
  "campaign_id": "CAM-001",
  "event_type": "CAL_BOOKING_COMPLETED",
  "timestamp": "2026-09-05T11:15:00Z",
  "prospect": {
    "domain": "targetai.com",
    "title": "VP of Engineering",
    "spend_tier": "$10k-$25k/mo"
  },
  "utm": {
    "source": "direct_outbound",
    "medium": "email",
    "campaign": "local-ai-audit-q3-2026",
    "content": "tear_down_v1"
  }
}
```

---

## 2. Master Links

- Measurement: [[CAMPAIGNS/MEASUREMENT]]
- Event Registry: [[_REGISTRIES/CAMPAIGN-EVENT-REGISTRY.json]]
