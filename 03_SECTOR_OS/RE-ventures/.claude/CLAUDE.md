# RE.md — Real Estate Sector

**Scope:** Build/test/deploy rules for RE ventures  
**Sector:** `RE` | **Status:** P1, P8, P10, P14  
**Updated:** 2026-07-27

---

## Build/Test/Deploy

```bash
git clone https://github.com/worldwidebro/re-ventures.git
cd re-ventures && npm install && cp .env.example .env
npm run migrate && npm run dev
npm test && npm run test:integration
npm run verify:listings
```

## Handoff

✅ **Stay in RE:** RE venture work or P1/P8/P10/P14  
🔵 **Cross-sector:** RE data → FIN (valuation), CON (renovation), LOG (distribution)  
🚨 **Platform:** Property data, MLS integration, valuations (notify all)

## Quick APIs

```bash
POST /api/leads/property-inquiry
POST /api/documents/listing-gen
POST /api/contracts/lease-review
POST /api/pricing/dynamic-rental
```

---

**Generated:** 2026-07-27
