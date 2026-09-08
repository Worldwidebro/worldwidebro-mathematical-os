---
# SEC-008: Financial Services
---

# CLAUDE.md — SEC-008: Financial Services

**Scope:** All financial ventures (FIN-001 through FIN-300), fintech, payments, banking, insurance.  
**Sector:** SEC-008 | **OpCo:** OpCo-008 | **Control Planes:** CP-020, CP-021, CP-023, CP-030

---

## SECTOR CONTEXT

**Active Ventures:** FIN-001 (Genixbank gateway, wired), Arbitrage Nexus (crypto), 20+ others validating

**Quick Aliases:**
- FIN-NNN = SEC-008-NNN (venture ID)
- CRYPTO-NNN = SEC-030-NNN (fintech payments)
- Sector repos: `github.com/Worldwidebro/fin-ventures`

**ClickUp:** Antwuan Johns workspace (Finance folder + Lead Generation), Zapier workflows live

---

## DISCOVERY ORDER

1. **Venture state:** `ventures-by-sector.yaml#SEC-008` (300+ ventures)
2. **Active projects:** ClickUp Antwuan Johns > Finance folder
3. **Control planes:** `control-planes-by-sector.yaml#SEC-008` → CP-020, CP-021, CP-023, CP-030
4. **Memory files:** `/memory/cross-sector/` (fin revenue loops, crm-system-complete)
5. **Master reference:** [[SEC-008-financial-services]] in Obsidian

---

## ACTIVE VENTURES

| ID | Name | Status | Notes |
|----|------|--------|-------|
| FIN-001 | Genixbank Lite | Operating | Gateway wired, MCP integration live |
| CRYPTO-001 | Arbitrage Nexus | Operating | Crypto arbitrage automation |

---

## RULES

- Fintech = security-critical: all changes require code review + test
- Revenue loop: Gmail → ClickUp → Make → Stripe (all wired)
- Supabase `deal_payments` table canonical for transactions
- HubSpot sync pending OAuth fix (currently blocked)

---

**Updated:** 2026-09-02 | [[SECTOR-TAXONOMY-MASTER]] | [[SEC-008-financial-services]]
