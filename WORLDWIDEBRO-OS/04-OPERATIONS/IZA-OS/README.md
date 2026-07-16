# IZA OS — Intelligent Zeta Automation Operating System

## Overview

IZA OS is a complete AI-native operating system designed to coordinate 712 ventures across 31 sectors through 12 capability departments and 18 OPCO territories.

**Created:** 2026-07-16  
**Status:** Foundation Complete (Phase 1A)  
**Governance Model:** Hermes + 12 Departments + 18 OPCOs + 712 Ventures

---

## Foundational Documents (Phase 1A Complete)

### 1. **IZA OS Constitution** ✅
**File:** `/IZA-OS-CONSTITUTION.md`

The founding law for the entire system.

---

### 2. **Universal Agent Contract** ✅
**File:** `/AGENT-CONTRACT-TEMPLATE.md`

Standard agreement for every agent in the system.

---

### 3. **Master Organization Registry** ✅
**File:** `/organization.yaml`

Complete organizational structure:
- **Hermes** — Chief Operating Intelligence
- **12 Departments** — Finance, Tech, Operations, Sales, Marketing, Product, People, Legal, Risk, Research, Customer Success, Governance
- **18 OPCOs** — Market territories
- **712 Ventures** — Product layer

---

## Quick Start

**How the system works:**

1. **Venture launches** → Requests capabilities from departments
2. **Hermes routes** → Assigns agents to serve the venture
3. **Departments deliver** → Finance handles accounting, Tech builds product, Marketing generates demand
4. **Communication** → Event-driven messaging (REQUEST, REPORT, ESCALATION, STATUS)
5. **Decisions logged** → Constitution enforces accountability

---

## File Structure

```
/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/

├── README.md (this file)
├── IZA-OS-CONSTITUTION.md (founding law)
├── AGENT-CONTRACT-TEMPLATE.md (standard agent agreement)
└── organization.yaml (organizational registry)
```

---

## Key Principles

### Departments Own Capabilities (Not Ventures)

Finance: accounting, invoicing, tax planning  
Technology: websites, APIs, AI integration  
Marketing: landing pages, ads, content  

Ventures **consume** these capabilities as needed.

### OPCOs Own Markets (Not Ventures)

Construction OPCO owns: General Contractor, Materials, Utilities ventures  
Healthcare OPCO owns: Clinics, Telemedicine, Elderly Care ventures  
Technology OPCO owns: SaaS, Developer Tools, AI Apps ventures

### Event-Driven Communication

```
REQUEST → Department receives capability request
REPORT → Agent delivers results  
ESCALATION → Requires higher authority
STATUS → Progress update
```

---

## Related Files

- **Constitution:** `IZA-OS-CONSTITUTION.md`
- **Agent Contract:** `AGENT-CONTRACT-TEMPLATE.md`
- **Organization:** `organization.yaml`
- **Ventures:** `/../../08-DATA/registries/VENTURES-CAPABILITIES-MAPPED.csv`
- **OPCOs:** `/../../02-GOVERNANCE/holdings/_superseded/Worldwidebro-Holdings/OPCO_VENTURE_MAPPING.csv`
- **Agents:** `/../../05-AGENTS/agent_registry.yaml`

---

**Version:** 2.0 | **Last Updated:** 2026-07-16
