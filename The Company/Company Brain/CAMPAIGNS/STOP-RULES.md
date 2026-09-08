# STOP-RULES — Automatic Execution Circuit Breakers

> **Canonical Document ID:** `DOC-STP-CAM-001`  
> **Authority:** Executive Governance & Risk (CP-001 / CP-034)  
> **Status:** MANDATORY AUTOMATED CIRCUIT BREAKERS

---

## 1. Automated Circuit Breakers

Execution automatically pauses and notifies the Sovereign Operator if:
1. **Deliverability Circuit Breaker:** Email bounce rate exceeds **3.0%** across any 50-send batch.
2. **Spam Complaint Circuit Breaker:** Spam complaint rate exceeds **0.1%** (1 in 1,000).
3. **Cost Burn Circuit Breaker:** Outbound spend reaches **$1,000** with **0 discovery calls booked**.
4. **Safety Circuit Breaker:** Any regulatory or compliance inquiry is received.

---

## 2. Master Links

- Kill Criteria: [[CAMPAIGNS/KILL-CRITERIA]]
- Risks: [[CAMPAIGNS/RISKS]]
