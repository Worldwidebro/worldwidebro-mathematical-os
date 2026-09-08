# AUDIENCE-STRATEGY — Targeting Strategy & Data Extraction

> **Canonical Document ID:** `DOC-AST-CAM-001`  
> **Authority:** Growth & Outbound Operations (CP-006)  
> **Status:** ACTIVE STRATEGY

---

## 1. Account Selection & Signal-Based Targeting

We do not blast cold spray-and-pray emails. We deploy **Signal-Based Targeting** based on empirical indicators of acute token spend:

### Primary Ingestion Signals
1. **Hiring Velocity Signals:** Companies actively recruiting "AI Engineer", "Agentic Systems Developer", or "Platform Engineer".
2. **GitHub Activity Signals:** Active open-source repositories showing high commit volume, TypeScript/Python dependencies on `openai`, `@anthropic-ai/sdk`, or `langgraph`.
3. **Funding Milestones:** Seed or Series A announcements ($2M–$15M raised in the last 18 months), indicating capital budget and mandate to scale engineering velocity.

---

## 2. List Extraction & Data Hygiene Protocol

1. Extract company URLs from Apollo / Crunchbase.
2. Filter for company size: 10 to 60 total employees (15 to 40 engineers).
3. Extract verified emails for titles: VP of Engineering, Head of Platform, CTO, Technical Co-Founder.
4. Scrub list through NeverBounce / ZeroBounce; discard any email with <98% deliverability confidence.

---

## 3. Master Links

- Master OS: [[CAMPAIGNS/CAMPAIGN-OS]]
- Audiences Master: [[CAMPAIGNS/AUDIENCES]]
- Outbound Channel: [[CAMPAIGNS/CHANNELS/OUTBOUND]]
