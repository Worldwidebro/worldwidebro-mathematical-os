# Venture-Repo Mapping & Organization Guide

**Last Updated**: 2026-06-01 | **Total Ventures**: 629 | **Worldwidebro Repos**: 12

---

## Worldwidebro Ventures → GitHub Repos

### Infrastructure Layer (6)
| Venture | Repo | Tier | Status |
|---------|------|------|--------|
| Civilization OS | `civilization-os` | 3 | ✓ Live |
| IZA OS RAG System | `iza-os-rag-system` | 1 | ✓ Live |
| The Office | `the-office` | 1 | ✓ Live |
| Venture Factory Core | `venture-factory-core` | 1 | ✓ Live |
| Venture Hub | `venture-hub` | 1 | ✓ Live |
| Autonomous Venture Studio | `autonomous-venture-studio` | 2 | ✓ Live |

### Research & Templates (2)
| Venture | Repo | Tier | Status |
|---------|------|------|--------|
| AI Venture Studio Template | `ai-venture-studio-template` | 2 | ✓ Template |
| Pitch Kit | `pitch-kit` | 2 | ✓ Live |

### Operations (2)
| Venture | Repo | Tier | Status |
|---------|------|------|--------|
| HVAC Operations | `con-012-hvac-services` | 1 | ✓ Live |
| Electrical Operations | `lt-009-hvac-technician-dispatch` | 1 | ✓ Live |

### Marketplace (1)
| Venture | Repo | Tier | Status |
|---------|------|------|--------|
| Business Template Marketplace | `business-template-marketplace` | 3 | ✓ Live |

### Construction (1)
| Venture | Repo | Tier | Status |
|---------|------|------|--------|
| CON-001 Ace Construction | `con-001-ace-construction` | 1 | ✓ Live |

---

## Folder Organization Plan

### Moving Spare Folders into WORLDWIDEBRO-OS Structure

| Current Folder | Target Location | Purpose | Size |
|---|---|---|---|
| `_inbox` | `01_CEO_COMMAND_CENTER/Inbox` | Incoming items to triage | TBD |
| `archive` | `08_RESEARCH/Archive` | Archived projects/documentation | TBD |
| `generated-courses` | `02_MARKETING/Content_Library/Courses` | Generated educational content | TBD |
| `staffing-os` | `15_PEOPLE_OPERATIONS/Staffing_OS` | Staffing and hiring operations | 172M |
| `mcp-dashboard` | `07_AUTOMATIONS/Dashboards` | MCP dashboard automation | 286M |
| `integrations` | `07_AUTOMATIONS/Integrations` | Third-party integrations | 2.6G |
| `Claude` | `08_RESEARCH/Claude_Research` | Claude-related research | TBD |
| `SecondBrain` | `08_RESEARCH/SecondBrain` | Knowledge base and notes | TBD |
| `Knowledge Graph` | `08_RESEARCH/Knowledge_Graph` | Knowledge graph data | TBD |
| `magic-portfolio` | `09_RESUME_PORTFOLIO/Magic_Portfolio` | Portfolio and case studies | TBD |

---

## Navigation Structure

After reorganization:

```
WORLDWIDEBRO-OS/
├── 01_CEO_COMMAND_CENTER/
│   └── Inbox/                    ← Moved from /_inbox
├── 02_MARKETING/
│   └── Content_Library/Courses/  ← Moved from /generated-courses
├── 07_AUTOMATIONS/
│   ├── Workflows/
│   │   ├── HVAC_DIRECTIVES.md
│   │   └── ELECTRICAL_DIRECTIVES.md
│   ├── Integrations/             ← Moved from /integrations
│   └── Dashboards/               ← Moved from /mcp-dashboard
├── 08_RESEARCH/
│   ├── Archive/                  ← Moved from /archive
│   ├── SecondBrain/              ← Moved from /SecondBrain
│   ├── Knowledge_Graph/          ← Moved from /Knowledge Graph
│   └── Claude_Research/          ← Moved from /Claude
├── 10_VENTURES/
│   ├── Operations_Ventures/
│   │   ├── ops-venture-001-hvac/
│   │   └── ops-venture-002-electrical/
│   └── SaaS_Ventures/
├── 15_PEOPLE_OPERATIONS/
│   └── Staffing_OS/              ← Moved from /staffing-os
└── VENTURE_REPO_MAPPING.md       ← This file
```

---

## How to Navigate

**Find a venture:**
- Check `10_VENTURES/Operations_Ventures/` for HVAC/Electrical
- Check `10_VENTURES/SaaS_Ventures/` for infrastructure ventures
- Check CSV for sector/tier/status

**Find directives to execute:**
- `07_AUTOMATIONS/VENTURE_DIRECTIVES_MAP.md` → links to specific venture directives
- `07_AUTOMATIONS/Workflows/HVAC_DIRECTIVES.md` → daily tasks for HVAC
- `07_AUTOMATIONS/Workflows/ELECTRICAL_DIRECTIVES.md` → daily tasks for Electrical

**Find executive layer:**
- `01_CEO_COMMAND_CENTER/Goals/` → venture targets
- `01_CEO_COMMAND_CENTER/KPIs/` → real-time metrics
- `01_CEO_COMMAND_CENTER/Inbox/` → incoming items to triage

---

## CSV Sync Status

629 total ventures in `ventures_classification_final.csv`:
- ✓ 12 Worldwidebro ventures (with GitHub repos mapped)
- ✓ 618 other ventures (various sectors, mostly planned)
- ✓ All have sector, tier, department, revenue_model assigned

All repos are private and hosted on GitHub Worldwidebro org.
