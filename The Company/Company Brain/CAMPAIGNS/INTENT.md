# INTENT — Commercial Intent Scoring Model

> **Canonical Document ID:** `DOC-INT-CAM-001`  
> **Authority:** Sales Operations (CP-006)  
> **Status:** ACTIVE SPECIFICATION

---

## 1. The Intent Score Formula (\(I_s\))

$$I_s = w_{\text{fit}} \cdot S_{\text{ICP}} + w_{\text{spend}} \cdot S_{\text{API}} + w_{\text{action}} \cdot S_{\text{behavior}}$$

Where weights are calibrated as:
- \(w_{\text{fit}} = 0.35\) (Company size & engineering headcount)
- \(w_{\text{spend}} = 0.45\) (Self-reported or inferred LLM API burn)
- \(w_{\text{action}} = 0.20\) (Click, reply, or booking velocity)

---

## 2. Intent Action Thresholds

- **Score \(I_s \ge 80\):** Urgent Outbound / Fast-track calendar invite.
- **Score \(50 \le I_s < 80\):** Standard 3-touch outbound sequence.
- **Score \(I_s < 50\):** Nurture with technical whitepapers; do not deploy high-touch sales hours.

---

## 3. Master Links

- Master OS: [[CAMPAIGNS/CAMPAIGN-OS]]
- Behavior: [[CAMPAIGNS/BEHAVIOR]]
- Qualification: [[CAMPAIGNS/QUALIFICATION]]
