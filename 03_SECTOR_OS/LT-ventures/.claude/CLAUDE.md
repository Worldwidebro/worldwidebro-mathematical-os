# LT.md — Logistics Sector

**Scope:** Build/test/deploy rules for LT ventures  
**Sector:** `LT` | **Status:** P1, P3, P14  
**Updated:** 2026-07-27

---

## Build/Test/Deploy

```bash
git clone https://github.com/worldwidebro/lt-ventures.git
cd lt-ventures && npm install && cp .env.example .env
npm run migrate && npm run dev
npm test && npm run test:integration
```

## Handoff

✅ **Stay in LT:** LT venture work or P1/P3/P14 features  
🔵 **Cross-sector:** LT data → CON, RE, FIN (post to #sector-dependencies)  
🚨 **Platform:** Routing, GPS, cost algorithms (notify all sectors)

## Quick APIs

```bash
POST /api/shipments/intake
POST /api/dispatch/call-intake
POST /api/pricing/estimate
```

---

**Generated:** 2026-07-27
