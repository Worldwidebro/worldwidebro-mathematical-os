# FIN.md — Finance Sector

**Scope:** Build/test/deploy rules for FIN ventures  
**Sector:** `FIN` | **Status:** P1, P7, P10, P14  
**Updated:** 2026-07-27

---

## Build/Test/Deploy

```bash
git clone https://github.com/worldwidebro/fin-ventures.git
cd fin-ventures && npm install && cp .env.example .env
npm run migrate && npm run dev
npm test && npm run test:integration
npm run verify:compliance  # Audit trail + encryption checks
```

## Handoff

✅ **Stay in FIN:** FIN venture work or P1/P7/P10/P14 features  
🔵 **Cross-sector:** FIN data → ALL sectors (HIGH PRIORITY) — post to #sector-dependencies  
🚨 **Platform:** Compliance, audit logs, risk models (notify all)

## Quick APIs

```bash
POST /api/leads/qualify
POST /api/investment-memos/generate
POST /api/contracts/review
```

## Compliance

⚠️ Required: Audit trail, encryption, SOX compliance, compliance API key

---

**Generated:** 2026-07-27
