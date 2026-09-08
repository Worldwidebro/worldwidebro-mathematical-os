[[STARTHERE]] | [[REALITY]] | [[NORTH-STAR]] | [[PRIORITIES]] | [[56-ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]

# PRIORITIES — Tactical Operating Directives

> **Canonical Document ID:** `DOC-PRIORITIES-001`  
> **Authority:** Sovereign Operator (CP-001 / CP-027)  
> **Status:** LIVE SPRINT FOCUS  
> **Updated:** 2026-09-05

---

## Tier 1: Commercial Traction & Revenue (URGENT)
- [ ] **Package Commercial Offer #1:** Define an external service offering (e.g., automated code security & capability audit) that solves an acute enterprise problem.
- [ ] **Establish Payment Pathway:** Setup active Stripe payment link or checkout flow.
- [ ] **Direct Customer Engagement:** Place the offer before 10 target ICP prospects.

---

## Tier 2: Infrastructure Stabilization & Pruning (HIGH)
- [ ] **Prune Dead Weight:** Remove crash-looping container `t7shield-neo4j-1` and prune orphaned Docker volumes on Mac Studio.
- [ ] **Consolidate Compose Projects:** Collapse 4 overlapping projects (`civos_*`, `t7shield-*`, `spinup-*`, `buzz-*`) into single canonical `_INFRASTRUCTURE/docker-compose.yml`.
- [ ] **Connect Observability:** Add `success_callback: ["langfuse"]` to `civos_litellm` configuration so port `:3003` receives trace spans.

---

## Tier 3: Registry Synchronization (MEDIUM)
- [x] **Deploy 12-Domain INFRASTRUCTURE System:** Complete 265 documents under `56-ENGINEERING/INFRASTRUCTURE/`.
- [x] **Generate 23 Machine-Readable Registries:** Validated JSON in `_REGISTRIES/`.
- [ ] **Implement Automated Drift Scanner:** Script continuous validation of live Docker state against registries.
