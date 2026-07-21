# OPCO Document Template System

Master templates for all 6 OPCOs, eliminating redundancy while enabling data-driven sales engines.

---

## ESSENTIAL DOCUMENTS (Every OPCO Needs These 7)

### 1. OPCO-CHARTER.md
Role, responsibilities, governance, SLAs for this OPCO

### 2. OPCO-DEPENDENCY-ARCHITECTURE.md  
What tech systems this OPCO depends on, impact of outages

### 3. OPCO-AGENT-SETUP.md
How OPCO President agent self-configures, reads files, escalates

### 4. OPCO-DATA-MODEL.md
What data does this OPCO track? Supabase tables, Neo4j nodes, Qdrant vectors

### 5. OPCO-CAPABILITY-REQUIREMENTS.md
What capabilities does this OPCO's ventures need? Which are missing?

### 6. OPCO-MARKET-POSITION.md
Market, channels, positioning, pricing, growth strategy

### 7. OPCO-AGENT-DECISION-LOG.md
Audit trail of every agent decision (auto-generated)

---

## FILE STORAGE & DELEGATION

```
T7 SHIELD (Source of Truth)
├─ 01_VENTURES/
│  ├─ CON/ → CON-CHARTER.md, CON-MARKET-POSITION.md, etc.
│  ├─ STA/ → STA-CHARTER.md, STA-MARKET-POSITION.md, etc.
│  ├─ RE/, EDU/, FIN/, LOG/ (same pattern)
│
├─ 03_AGENTS/
│  ├─ con-president-agent/ → reads CON docs
│  ├─ sta-president-agent/ → reads STA docs
│  └─ etc.
│
├─ 14_INFRASTRUCTURE/
│  ├─ data/ → shared OPCO-DATA-MODEL.md files
│  ├─ templates/ → OPCO-CHARTER-TEMPLATE.md, etc.
│  └─ repositories/ → moved from MacBook Air
│
└─ 05_SOFTWARE_FACTORY/
   ├─ opco-agent-setup-templates/
   └─ logs/ → OPCO-AGENT-DECISION-LOG.md files
```

---

## TEMPLATE PATTERN (Zero Redundancy)

**Create once:**
- OPCO-CHARTER-TEMPLATE.md (2h)
- OPCO-DEPENDENCY-ARCHITECTURE-TEMPLATE.md
- OPCO-AGENT-SETUP-TEMPLATE.md
- OPCO-DATA-MODEL-TEMPLATE.md
- OPCO-CAPABILITY-REQUIREMENTS-TEMPLATE.md
- OPCO-MARKET-POSITION-TEMPLATE.md

**Fill for each OPCO (15 min each):**
- CON-CHARTER.md (fill: mission, governance, SLAs)
- STA-CHARTER.md (fill: mission, governance, SLAs)
- etc. × 6 OPCOs

**Result:** 3.5 hours per OPCO (vs 12 hours writing from scratch), 100% consistency

---

## SALES ENGINE (Data-Driven)

**Flow:**
Agent reads OPCO docs → understands market, data model, capabilities → monitors TECH-050 dashboard → sees real-time revenue, ventures, gaps → makes decisions → logs to audit trail → Hermes learns → applies to other OPCOs

**Observable:** Revenue by OPCO, capability coverage, venture health, agent decisions, CAC/LTV

---

## File Owner Assignment

| Document | Owner | Location | Update Frequency |
|----------|-------|----------|------------------|
| OPCO-CHARTER.md | OPCO President | T7/01_VENTURES/{OPCO}/ | Quarterly |
| OPCO-DEPENDENCY-ARCHITECTURE.md | CTO | T7/14_INFRASTRUCTURE/ | When systems change |
| OPCO-AGENT-SETUP.md | COO | T7/05_SOFTWARE_FACTORY/ | When agent capabilities change |
| OPCO-DATA-MODEL.md | Data Engineer | T7/14_INFRASTRUCTURE/data/ | When schema changes |
| OPCO-CAPABILITY-REQUIREMENTS.md | OPCO President | T7/01_VENTURES/{OPCO}/ | Quarterly |
| OPCO-MARKET-POSITION.md | CFO + OPCO President | T7/01_VENTURES/{OPCO}/ | Annually |
| OPCO-AGENT-DECISION-LOG.md | Hermes (auto-logged) | T7/05_SOFTWARE_FACTORY/logs/ | Real-time |

---

## Create per OPCO (Checklist)

For CON, STA, RE, EDU, FIN, LOG:

- [ ] OPCO-CHARTER.md
- [ ] OPCO-DEPENDENCY-ARCHITECTURE.md
- [ ] OPCO-AGENT-SETUP.md
- [ ] OPCO-DATA-MODEL.md
- [ ] OPCO-CAPABILITY-REQUIREMENTS.md
- [ ] OPCO-MARKET-POSITION.md
- [ ] OPCO-AGENT-DECISION-LOG.md (auto-generated)

**Effort:** 6-12 hours total (fill templates × 6 OPCOs)

---

## Related Documents

- [[TECH-SECTOR-CHARTER]] — Template pattern
- [[OPCO-DEPENDENCY-ARCHITECTURE]] — Dependency template
- [[IZA-OS-CONSTITUTION]] — Governance template
- [[2026-07-19_SYSTEM-ARCHITECTURE-SYNTHESIS]] — Complete solution order
