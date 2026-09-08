---
# SEC-024: Technology & Software
---

# CLAUDE.md — SEC-024: Technology & Software

**Scope:** All tech ventures (TECH-001+), VEX platform, SaaS, infrastructure, AI/ML.  
**Sector:** SEC-024 | **OpCo:** OpCo-024 | **Control Planes:** CP-001, CP-004-8, CP-011-30 (19/30 CPs)

---

## SECTOR CONTEXT

**Active Ventures:** VEX Hero (platform), TECH-038 (Voice OS), TECH-040 (Securify), TECH-062 (IZA OS), 80+ others

**Quick Aliases:**
- TECH-NNN = SEC-024-NNN (venture ID)
- AI-NNN = SEC-032-NNN (AI/ML subset)
- ML-NNN = SEC-032-NNN (ML infrastructure)
- Sector repos: `github.com/Worldwidebro/tech-ventures`

**ClickUp:** Antwuan Johns workspace (PRIMARY, 59 folders, all control planes)

---

## DISCOVERY ORDER

1. **Venture state:** `ventures-by-sector.yaml#SEC-024` (85+ ventures)
2. **Active projects:** ClickUp Antwuan Johns > Projects, Infrastructure, Build Pipeline
3. **Control planes:** `control-planes-by-sector.yaml#SEC-024` (19 CPs) → all major operations
4. **Memory files:** `/memory/sec-024-technology/` (ClickUp v2.0, VEX setup, TECH ventures)
5. **Master reference:** [[SEC-024-technology-software]] in Obsidian

---

## ACTIVE VENTURES

| ID | Name | Status | Repo | Notes |
|----|------|--------|------|-------|
| VEX | VEX Hero Platform | Operating | vex-hero-site-sigma | Dashboard live, marketplace front-end |
| TECH-038 | Shared Voice OS | Operating | tech-038-shared-voice-os | Open-source stack, $7K/mo licensing |
| TECH-040 | Securify | Operating | tech-040-securify | Security frontend, live |
| TECH-062 | IZA OS | Operating | tech-062-iza-os | Lead capture system live |

---

## INFRASTRUCTURE

**ClickUp Antwuan Johns:**
- 59 folders organized by control plane (Gates 0-9, Projects, Finance, Agents, Infrastructure)
- 150+ lists (all major operations)
- Gates 0-9 = 10 control planes mapped explicitly

**Local Services:**
- Ollama (Qwen 2.5 32B, zero API cost)
- Neo4j (4,031 nodes, indexes pending)
- Qdrant (17,236 vectors)
- Supabase (Postgres, RLS, pgvector)
- Redis (temporary state)

**Deployment:**
- Vercel (frontends)
- Railway/Render (backends)
- Supabase Cloud (databases)

---

## RULES

- VEX is unified marketplace front-end for all 789 ventures
- Tech sector hosts infrastructure for other sectors (cross-sector responsibility)
- All code: Git + PR, tests pass before merge
- ClickUp v2.0 spec in use: 15 categories, 23 task types, 13 views
- API keys: never in code, use .env + browser-automated extraction
- Neo4j indexing: PRIORITY (4,031 nodes, no indexes = performance blocker)

---

## BLOCKERS (Sector-Specific)

- **HubSpot OAuth:** Expired token, blocks CRM integration
- **Neo4j indexes:** Missing, performance risk at scale
- **Railway auth:** Needed for backend deployments

---

**Updated:** 2026-09-02 | [[SECTOR-TAXONOMY-MASTER]] | [[SEC-024-technology-software]]
