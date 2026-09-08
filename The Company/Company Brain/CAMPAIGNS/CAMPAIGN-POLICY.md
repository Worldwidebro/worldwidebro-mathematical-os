# CAMPAIGN-POLICY — Campaign Operating Policies & Boundaries

> **Canonical Document ID:** `DOC-POL-CAM-001`  
> **Authority:** Executive Governance & Legal (CP-001 / CP-031)  
> **Status:** ACTIVE MANDATORY POLICY

---

## 1. Purpose & Authority

This policy establishes non-negotiable boundaries for all marketing, outreach, advertising, and commercial campaigns executed on behalf of WorldwideBro and its affiliated operating ventures. Compliance is mandatory for both human operators and autonomous AI agents.

---

## 2. Core Operational Policies

### Policy 1: The Truth & Substantiation Mandate
- No campaign may utter any factual, technical, or financial claim that is not directly backed by reproducible empirical evidence recorded in `_REGISTRIES/CANONICAL/` or `_ONTOLOGY/EVIDENCE_STANDARDS.md`.
- Statements regarding cost reductions (e.g., "Slashes API costs by 60%+") must be backed by audited benchmark logs.

### Policy 2: Capital Deployment & Spending Caps
- No campaign may commit financial capital exceeding its authorized allocation in `_REGISTRIES/CAMPAIGN-BUDGET-REGISTRY.json` without written re-authorization.
- Daily media spend is capped at a strict maximum; automated circuit breakers must halt bidding if daily limits are breached.

### Policy 3: Data Sovereignty & Privacy
- Zero client repository code or proprietary configuration data may be stored outside encrypted local storage (`civos_neo4j`, local Postgres) or transmitted to public LLM endpoints.
- All email outreach must fully comply with CAN-SPAM, GDPR, and CASL regulations, including valid physical business address headers and automated 1-click unsubscribe mechanics.

### Policy 4: Brand Safety & Ethical Boundaries
- No spamming, deceptive subject lines, artificial clickbait, or simulated system alerts.
- Outreach must be direct, technically sophisticated, respectful of engineering time, and transparent regarding commercial intent.

---

## 3. Violation Consequences

Any breach of this policy triggers an automatic freeze of campaign execution, immediate suspension of agent privileges, and mandatory audit logging under [[46-GOVERNANCE]].

---

## 4. Master Links

- Master System: [[CAMPAIGNS/CAMPAIGN-OS]]
- Governance Matrix: [[CAMPAIGNS/GOVERNANCE]]
- Compliance Framework: [[CAMPAIGNS/COMPLIANCE]]
- AntiGravity Operating Contract: [[ANTIGRAVITY.md]]
