# PACING — Budget Burn Rate & Pacing Algorithms

> **Canonical Document ID:** `DOC-PAC-CAM-001`  
> **Authority:** Financial Operations (CP-024)  
> **Status:** ACTIVE SPECIFICATION

---

## 1. Daily Pacing Cap

- **Max Daily Spend:** **$150 USD / day**.
- **Pacing Mode:** `LINEAR_ACCELERATING`.
- **Circuit Breaker:** If daily spend exceeds $150 or if bounce rate exceeds 2%, outbound automations halt immediately.

---

## 2. Master Links

- Budget: [[CAMPAIGNS/BUDGET]]
- Spend: [[CAMPAIGNS/SPEND]]
- Stop Rules: [[CAMPAIGNS/STOP-RULES]]
