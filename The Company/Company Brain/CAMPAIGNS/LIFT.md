# INCREMENTALITY — Causal Lift & Matched Market Testing

> **Canonical Document ID:** `DOC-INC-CAM-001`  
> **Authority:** Econometrics (CP-024 / CP-040)  
> **Status:** ACTIVE SPECIFICATION  
> **Canonical Alias:** [[CAMPAIGNS/LIFT.md]]

---

## 1. Causal Lift Methodology

To prove that commercial revenue is genuinely caused by the campaign and not organic baseline drift:
- We track holdout control cohorts across our target accounts list.
- We measure incremental revenue lift: \(\Delta \text{Rev} = \text{Rev}_{\text{exposed}} - \text{Rev}_{\text{control}}\).

---

## 2. Master Links

- Measurement: [[CAMPAIGNS/MEASUREMENT]]
- Experiments: [[CAMPAIGNS/EXPERIMENTS]]
