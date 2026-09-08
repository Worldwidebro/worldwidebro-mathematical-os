# RISKS — Enterprise & Operational Campaign Risk Matrix

> **Canonical Document ID:** `DOC-RSK-CAM-001`  
> **Authority:** Risk Management (CP-034)  
> **Status:** ACTIVE SPECIFICATION  
> **Machine Registry:** [`_REGISTRIES/CAMPAIGN-RISK-REGISTRY.json`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/_REGISTRIES/CAMPAIGN-RISK-REGISTRY.json)  
> **Canonical Alias:** [[CAMPAIGNS/RISK-REGISTER.md]]

---

## 1. Risk Governance Architecture

Campaign risks are identified, scored, and assigned mitigations prior to flighting. Every risk is scored on a standard \(5 \times 5\) Probability \(\times\) Impact matrix.

| Risk ID | Risk Name | Prob | Impact | Mitigation Strategy | Owner |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`RSK-001`** | Enterprise Security Code Inspection Friction | Med | High | Provide zero-install local Docker scanner running air-gapped on client nodes. | Systems Arch |
| **`RSK-002`** | Prospect Skepticism of 3X ROI Guarantee | Low | Med | Back guarantee contractually with escrow deposit refund clause. | Commercial Lead |
| **`RSK-003`** | Outbound Email Domain Burn / Deliverability Trap | Med | High | Throttle warmup to 25/day, use 3 secondary domains, enforce <2% bounce rate. | Outbound Lead |
| **`RSK-004`** | LLM Provider Pricing Cuts Undermining Savings Math | Low | Med | Anchor value on hallucination elimination and 100% data sovereignty. | Sovereign Operator |

---

## 2. Master Links

- Master OS: [[CAMPAIGNS/CAMPAIGN-OS]]
- Stop Rules: [[CAMPAIGNS/STOP-RULES]]
- Kill Criteria: [[CAMPAIGNS/KILL-CRITERIA]]
