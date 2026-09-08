# DEPENDENCIES — Critical Path DAG & Pre-Flight Blockers

> **Canonical Document ID:** `DOC-DEP-CAM-001`  
> **Authority:** Program Architecture (CP-027)  
> **Status:** ACTIVE DEPENDENCY MAP

---

## 1. Critical Path DAG

```mermaid
graph TD
    D1[Domain Warmup Complete] --> LCH[Launch Outbound Wave 1]
    D2[Apollo List Scraped & Scrubbed] --> LCH
    D3[Cal.com Discovery Link Verified] --> LCH
    D4[3X ROI SOW Template Approved] --> DIS[Discovery Call Execution]
    LCH --> DIS
    DIS --> SOW[SOW Sent]
    SOW --> CASH[Deposit Paid in Escrow]
    CASH --> AUD[48-Hour Audit Execution]
```

---

## 2. Master Links

- Timeline: [[CAMPAIGNS/TIMELINE]]
- Launch Checklist: [[CAMPAIGNS/LAUNCH-CHECKLIST]]
