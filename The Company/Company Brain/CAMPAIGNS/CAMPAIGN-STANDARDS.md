# CAMPAIGN-STANDARDS — Quality Bars & Verification Standards

> **Canonical Document ID:** `DOC-STD-CAM-001`  
> **Authority:** Quality Assurance & System Architecture (CP-027)  
> **Status:** ACTIVE STANDARD

---

## 1. The Quality Standard Framework

To prevent sloppiness, hallucinated metrics, or incomplete implementations, every campaign must satisfy rigorous technical and operational standards before being classified as `LIVE` or `VERIFIED`.

---

## 2. The 5 Quality Bars

### 1. Copywriting & Communication Bar
- Clear, punchy, direct-response style.
- Eliminates corporate jargon, empty buzzwords, and vague promises.
- Focuses on concrete engineering metrics: token counts, latency, hardware utilization, cash savings.

### 2. Visual & Design Bar
- Professional typography, high-contrast charts, and clean terminal screenshots.
- Zero blurry renderings or unvetted AI-generated stock photography.
- Architecture diagrams must use standard, readable Mermaid or SVG notation.

### 3. Technical & Telemetry Bar
- All links must carry correct UTM parameters.
- Conversion event tracking must fire within 200ms of user action.
- Webhooks must implement retry logic with exponential backoff and HMAC signature verification.

### 4. Code & Graph Bar
- All campaign entities must be indexed in `_REGISTRIES/` with unique IDs conforming to `ID_REGISTRY.yaml`.
- Neo4j graph nodes and relationships must execute cleanly against cypher constraints.

### 5. Empirical Verification Bar
- In accordance with AntiGravity Rule #3, no campaign may be reported as "Complete" without verified results recorded in `CAMPAIGN-RESULT-REGISTRY.json`.

---

## 3. Definition of Done (DoD) for Campaigns

A campaign is considered **DONE** only when:
1. All planned flights have concluded or hit terminal stop-rules.
2. Actual financial spend and revenue have been reconciled in escrow ledgers.
3. Post-mortem retrospective document is completed.
4. Generated customer insights and technical benchmarks are permanently ingested into Knowledge Core.

---

## 4. Master Links

- Master System: [[CAMPAIGNS/CAMPAIGN-OS]]
- QA Standard: [[CAMPAIGNS/QA]]
- Pre-Launch Checklist: [[CAMPAIGNS/PRE-LAUNCH]]
