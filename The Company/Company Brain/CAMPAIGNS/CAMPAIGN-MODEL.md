# CAMPAIGN-MODEL — Formal Mathematical & Computational Model

> **Canonical Document ID:** `DOC-MOD-CAM-001`  
> **Authority:** System Architecture & Economic Modeling (CP-006 / CP-027)  
> **Status:** ACTIVE SPECIFICATION

---

## 1. Formal Mathematical Definition

Formally, a **Campaign** \(C\) in Company Brain is defined as a 12-tuple:

$$C = \langle O, A, P, M, D, B, F, T, E, R, G, L \rangle$$

Where:
- **\(O\) (Objective Space):** \(O = \langle O_p, \{O_{s,1}, \dots, O_{s,n}\}, \tau \rangle\), where \(O_p\) is the singular primary metric, \(O_{s}\) are secondary constraints, and \(\tau\) is the terminal deadline.
- **\(A\) (Audience Space):** \(A = \{a \in \text{TAM} \mid \text{Fit}(a) \ge \theta_{\text{ICP}}\}\), the partitioned segment cohort.
- **\(P\) (Problem & Proposition):** \(P = \langle \text{Pain}, \text{Offer}, \text{Price}, \text{Guarantee} \rangle\).
- **\(M\) (Message & Creative):** \(M = \{m_j = (\text{Hook}_j, \text{Body}_j, \text{CTA}_j, \text{Asset}_j)\}\).
- **\(D\) (Distribution Channels):** \(D = \{(c_k, w_k) \mid \sum w_k = 1.0\}\), weighted channel mix.
- **\(B\) (Capital Budget):** \(B = \langle B_{\text{total}}, B_{\text{media}}, B_{\text{asset}}, B_{\text{reserve}}, \dot{B}_{\max} \rangle\).
- **\(F\) (Conversion Funnel):** Graph \(G_F = (V_F, E_F)\), where vertices represent conversion states and edges represent transition probabilities \(p_{ij}\).
- **\(T\) (Telemetry & Attribution):** Function \(\Phi: \text{Touchpoints} \times \text{Events} \to [0, 1]\).
- **\(E\) (Experimental Design):** Set of hypotheses \(H = \{H_0, H_1\}\) with sample sizes \(N\) and significance level \(\alpha = 0.05\).
- **\(R\) (Risk & Stop Rules):** Predicate function \(\Omega(\vec{x}) \in \{\text{CONTINUE}, \text{PAUSE}, \text{PIVOT}, \text{KILL}\}\).
- **\(G\) (Governance & RACI):** Tuple of accountable sovereign roles.
- **\(L\) (Learning Function):** Transformation mapping outcomes to permanent knowledge graph updates: \(\Delta K = \Psi(C, \vec{x}_{\text{actual}})\).

---

## 2. The Economic Value & ROI Equation

The expected monetary value \(\mathbb{E}[V(C)]\) of campaign \(C\) is computed as:

$$\mathbb{E}[V(C)] = \sum_{i=1}^{N_{\text{leads}}} \left( P(\text{Close} \mid \vec{x}_i) \cdot \text{LTV}_i \right) - B_{\text{total}} - C_{\text{ops}}$$

Where:
- \(P(\text{Close} \mid \vec{x}_i) = \prod_{k=1}^{m} p_k\), the product of stage transition probabilities in funnel \(F\).
- \(\text{LTV}_i\) is the projected lifetime customer gross profit.
- \(B_{\text{total}}\) is total capital spend.
- \(C_{\text{ops}}\) is operational overhead (compute, agent inference, human hours).

### Customer Acquisition Cost (CAC) Formula
$$\text{CAC} = \frac{B_{\text{actual}} + C_{\text{ops}}}{N_{\text{acquired}}}$$

### Return On Ad Spend (ROAS) Formula
$$\text{ROAS} = \frac{\text{Recognized Revenue from Campaign}}{\text{Media Spend}}$$

---

## 3. The Grand Slam Offer Value Equation

In alignment with value theory, the attractiveness \(V_{\text{offer}}\) of the campaign proposition is modeled as:

$$V_{\text{offer}} = \frac{\text{Dream Outcome} \times \text{Perceived Likelihood of Achievement}}{\text{Time Delay} \times \text{Effort & Sacrifice}}$$

For `CAM-001` ([`OFR-AUDIT-001`](file:///Users/acebless/Documents/The%20Company/Company%20Brain/COMMERCIAL/OFFERS/OFFER-001-LOCAL-AI-AUDIT.md)):
- **Dream Outcome:** Slashes cloud LLM bills by 60%+ while keeping 100% data privacy.
- **Perceived Likelihood:** High (3X ROI Guarantee contractually backed by escrow).
- **Time Delay:** Minimized (48-hour turnaround).
- **Effort & Sacrifice:** Zero (Client provides read-only repository access; WorldwideBro executes all analysis).
- **Result:** Value quotient is maximized, accelerating discovery-to-close conversion rates.

---

## 4. State Machine Dynamics & Stopping Rules

The operational state \(S(t)\) evolves over time \(t\):

$$S(t) \in \{\text{PLANNING}, \text{QA}, \text{LIVE}, \text{OPTIMIZING}, \text{PAUSED}, \text{KILLED}, \text{COMPLETED}\}$$

Transition to `KILLED` occurs instantaneously if:
$$\text{CPA}(t) > 2.5 \times \text{CPA}_{\text{target}} \quad \text{for} \quad t > t_{\text{warmup}}$$
$$\text{or} \quad \text{Unsubscribes/Complaints} > \theta_{\text{safety}}$$

---

## 5. Related Frameworks

- Master System: [[CAMPAIGNS/CAMPAIGN-OS]]
- Architecture: [[CAMPAIGNS/CAMPAIGN-ARCHITECTURE]]
- Lifecycle: [[CAMPAIGNS/CAMPAIGN-LIFECYCLE]]
- Unit Economics: [[CAMPAIGNS/UNIT-ECONOMICS]]
