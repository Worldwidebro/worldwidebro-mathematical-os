# CLAUDE.md — Company Brain (Session Guidance)

**Scope:** Active session instructions only (reference docs moved to `_REFERENCE/`)  
**Updated:** 2026-09-09  
**Authority:** Infrastructure CP-027 + Execution CP-033 + Revenue CP-021

---

## PHASE 1 STATUS — Sep 8-30

✅ **Infrastructure:** Neo4j (20,363 edges), Qdrant (17,236 vectors), OmniRoute, Ollama all LIVE  
⚠️ **Orchestration:** 94 URLs working independently, webhook automations NOT wired  
🔴 **Revenue:** $0, zero automation, cold calls not made

**CRITICAL:** Fix blocking issues (fix #1-3 below) before Sep 11 to hit $2.5K revenue target.

---

## THREE IMMEDIATE FIXES (Do These First)

### Fix #1: Make Cold Calls (Sep 9-10)
- OPS-001: Call 10 HIGH-priority staffing prospects (script ready)
- CON-001: Call 50 NC construction companies (script ready)
- LT-005: B2B outreach to medical facilities
- **This is the only thing blocking first revenue.** Everything else is wired.

### Fix #2: Deploy CON-001 to Vercel (5 min)
```bash
cd SECTORS/SEC-002-Construction/ventures/CON-001
vercel deploy  # Fix CLI auth if blocked
```

### Fix #3: Wire LT-005 Keys (5 min)
Add to Vercel env vars:
- `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`
- `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY`

---

## NAMING CONSOLIDATION

**One system, one name: VEX**

| What | GitHub | Deployed | Status |
|------|--------|----------|--------|
| **VEX** | Worldwidebro/Worldwidebro-Vex | vex-hero-site-sigma.vercel.app | ✅ Portfolio live |
| Growth OS | Worldwidebro/worldwidebro-marketing-os | localhost:3030 | ✅ Dashboard live |

**Removed:** "Venture Portal", "Hermes Command Center" (old naming)

---

## QUICK REFERENCE

**Infrastructure Status:** [[INFRASTRUCTURE-STATUS-2026-09|_REFERENCE/INFRASTRUCTURE-STATUS-2026-09.md]]  
**Venture Roadmap:** [[VENTURE-ROADMAP-2026-09|_REFERENCE/VENTURE-ROADMAP-2026-09.md]]  
**Digital Librarian:** [[DIGITAL-LIBRARIAN-ARCHITECTURE|_REFERENCE/DIGITAL-LIBRARIAN-ARCHITECTURE.md]]

**Quick Commands:**
```bash
docker --context macstudio ps              # Verify all services
curl http://100.87.214.70:6333/health     # Check Qdrant
curl http://100.87.214.70:7474            # Check Neo4j browser
ssh macstudio                               # Connect to Mac Studio
```

**Dashboard Access:**
| Service | URL | Auth |
|---------|-----|------|
| OmniRoute | http://100.87.214.70:20128 | Bitwarden "OmniRoute — Company Brain" |
| Neo4j | http://100.87.214.70:7474 | neo4j / changeme |
| Growth OS | localhost:3030 | No auth |
| VEX | vex-hero-site-sigma.vercel.app | No auth |

---

## ONE RULE

**Verify before claiming it works.**

- ✅ Check: `docker --context macstudio ps`, actual CLI output, live queries
- ❌ Never: Trust documentation, commit messages, "should be working"
- 🛑 Always: Ask before retrying if uncertain — don't loop blindly

---

## GIT INVARIANTS

1. All venture changes → Git + PR
2. Commit messages include venture ID when applicable
3. Tests must pass before merge
4. No force-push to main
5. Attribution: `Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>`

---

## WHAT I MUST NEVER DO

1. Claim infrastructure works without verification
2. Invent or guess credentials (use Bitwarden or MCP auth)
3. Modify production without approval gate
4. Duplicate existing infrastructure/capability
5. Create ventures outside Git + Supabase PR flow

---

## REFERENCE FILES (Moved from CLAUDE.md)

**Infrastructure & Systems:**
- `_REFERENCE/INFRASTRUCTURE-STATUS-2026-09.md` — Services, hardware, credentials, routing gaps
- `_REFERENCE/VENTURE-ROADMAP-2026-09.md` — 7 Tier-1 ventures, critical blockers, timeline
- `_REFERENCE/DIGITAL-LIBRARIAN-ARCHITECTURE.md` — 5-layer research OS (OSS candidate evaluation)
- `_REFERENCE/OPERATIONAL-STATE-2026-09.md` — What's working vs. NOT wired

**Capital & Holding Company Architecture:**
- `BUSINESS-CAPITAL-DATA-ROOM/00_ENTERPRISE_BLUEPRINT.md` — Family office structure (Family Trust → Asset/IP/Admin LLCs → Operating C-Corp)
- `CAPITAL-READINESS-ENGINE.md` — 5-venture capital readiness matrix + $4.5M capital sources
- `BUSINESS-CAPITAL-DATA-ROOM/FINANCIAL-ECOSYSTEM-MAPPING.md` — 12-layer financial OS (banking, credit, debt, investment, payments, insurance, government, infrastructure, marketplaces)
- `WORLDWIDEBRO-HOLDINGS-MASTER-OPERATING-MANUAL.md` — **789-venture holding company framework** (portfolio strategy, governance, capital allocation, exits)

**Master Orientation (Root Docs):**
- [[STARTHERE]] — Phase 0 locked, Phase 1 execution
- [[REALITY]] — Verified truth ledger
- [[ANTIGRAVITY]] — 45 operating rules
- [[RESPECT]] — 20 governance rules
- [[INDEX]] — Master navigation

---

## SESSION START CHECKLIST

✅ Load CLAUDE.md (this file)  
✅ Load [[STARTHERE]] (orientation)  
✅ Verify services: `docker --context macstudio ps`  
✅ Identify context (venture? sector? phase?)  
✅ Load relevant reference docs

---

**Generated:** 2026-09-09 | **Version:** 4.0 (Trimmed to ~4KB, reference docs separated)
