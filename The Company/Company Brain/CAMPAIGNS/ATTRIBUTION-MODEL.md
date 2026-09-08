# ATTRIBUTION — Multi-Touch Attribution Engine

> **Canonical Document ID:** `DOC-ATR-CAM-001`  
> **Authority:** Telemetry & Analytics (CP-040)  
> **Status:** ACTIVE SPECIFICATION  
> **Canonical Alias:** [[CAMPAIGNS/ATTRIBUTION-MODEL.md]]

---

## 1. Attribution Model: W-Shaped Algorithmic Allocation

For high-touch enterprise deal flow, single-touch attribution (first or last touch) distorts channel value. We implement a **W-Shaped Attribution Model**:

```text
[First Touch: 30%] ──> [Lead Creation: 30%] ──> [Opportunity Creation: 30%] ──> [Remaining Touches: 10%]
```

- **30% Credit:** First touchpoint (e.g., initial cold outbound email open).
- **30% Credit:** Lead creation (e.g., reply or discovery call booking).
- **30% Credit:** Opportunity creation (e.g., completed discovery call and SOW delivery).
- **10% Credit:** Shared across intermediary nurturing touches (whitepapers, LinkedIn posts).

---

## 2. Master Links

- Measurement: [[CAMPAIGNS/MEASUREMENT]]
- Tracking: [[CAMPAIGNS/TRACKING]]
- UTM Taxonomy: [[CAMPAIGNS/UTM]]
