# CLAUDE.md — Company Brain (Session Guidance)

**Scope:** Active session instructions only; reference docs in `_REFERENCE/` and master plan in global CLAUDE.md  
**Updated:** 2026-09-10  
**Authority:** Infrastructure CP-027 + Execution CP-033 + Revenue CP-021  
**Current Phase:** Week 1 Revenue Execution (Sep 10–15)

---

## STATUS SNAPSHOT — Sep 10, 2026

✅ **Phase 1 LOCKED** — Agent Enablement complete, audit system operational  
✅ **Infrastructure LIVE** — Neo4j (20,363 edges), Qdrant (17,236 vectors), OmniRoute, Ollama  
✅ **6 Tier-0 Ventures Verified** — All deployed and HTTP 200:
- OPS-001, LT-005, CALLCENTER (Revenue-Ready)
- CON-001, RE-001 (Demo-Ready, 1–2 days)
- LT-011 (Skeleton, assess needed)

🚀 **Week 1 Target:** $7.5K–$20K (execution window open)

---

## WEEK 1 EXECUTION FOCUS (Sep 10–15)

**Master plan:** [[WEEK1-EXECUTION-PLAN|20-DECISIONS/WEEK1-EXECUTION-PLAN.md]]

### Three Revenue-Ready Ventures (Make Calls Now)
1. **OPS-001** → Staffing placement cold calls (script ready)
2. **LT-005** → Medical facility B2B outreach (env vars configured)
3. **CALLCENTER** → Twilio integration (Stripe wired)

### Next Actions (Decision Gates)
- **CON-001:** 6h API build (marketing flow ready, assess first)
- **RE-001:** 25h deal engine (pitch deck ready, assess first)
- **LT-011:** 1h assessment → build/buy/defer decision

**See also:** [[VENTURE-AUDIT-FRAMEWORK|20-DECISIONS/VENTURE-AUDIT-FRAMEWORK.md]] (12-layer methodology)

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
- `INSTITUTIONAL-VENTURE-ARCHITECTURE.md` — **MASTER MAP: All 789 ventures mapped to family office structure + repos + OSS deps + inter-venture trading**
- `WORLDWIDEBRO-HOLDINGS-MASTER-OPERATING-MANUAL.md` — 789-venture holding company framework (portfolio strategy, governance, capital allocation, exits)
- `BUSINESS-CAPITAL-DATA-ROOM/00_ENTERPRISE_BLUEPRINT.md` — Family office structure (Family Trust → Asset/IP/Admin LLCs → Operating C-Corp)
- `CAPITAL-READINESS-ENGINE.md` — 5-venture capital readiness matrix + $4.5M capital sources
- `BUSINESS-CAPITAL-DATA-ROOM/FINANCIAL-ECOSYSTEM-MAPPING.md` — 12-layer financial OS (banking, credit, debt, investment, payments, insurance, government, infrastructure, marketplaces)

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

**Updated:** 2026-09-10 | **Version:** 4.1 (Phase 1 locked, 6 Tier-0 ventures live, Week 1 execution active)
