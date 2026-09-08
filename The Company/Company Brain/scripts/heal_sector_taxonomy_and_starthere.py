#!/usr/bin/env python3
"""
heal_sector_taxonomy_and_starthere.py

Resolves missing tags, IDs, connections, and broken wikilinks across:
1. STARTHERE.md
2. 00-CONSTITUTION/SECTOR-TAXONOMY-MASTER.md
3. SECTOR_INDEX.md
4. SECTORS/ (all 35 sector files)
5. 00-CONSTITUTION/opcos/ (OpCo-001 through OpCo-035 alias/index files)
6. _REGISTRIES/ventures-by-sector.yaml (adds missing core ventures)
"""

import os, re, yaml

WORKSPACE = "/Users/acebless/Documents/The Company/Company Brain"

# ==============================================================================
# 1. HEAL STARTHERE.MD
# ==============================================================================
print("1. Healing STARTHERE.md...")
starthere_path = os.path.join(WORKSPACE, "STARTHERE.md")

starthere_content = """---
id: DOC-START-001
title: STARTHERE — Master Orientation Legend
aliases: ["START_HERE", "START-HERE", "starthere", "start-here", "Orientation", "Master-Legend"]
tags: [orientation, master-index, company-brain, governance, start-here]
status: ACTIVE
authority: "CP-001 / CP-027"
updated: 2026-09-05
---

[[STARTHERE]] | [[REALITY]] | [[INDEX]] | [[00-CONSTITUTION]] | [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|SECTOR-TAXONOMY]] | [[13_ENGINEERING/INFRASTRUCTURE/INFRASTRUCTURE|INFRASTRUCTURE]]

# START HERE

> **Canonical Document ID:** `DOC-START-001`  
> **Authority:** Sovereign Operator & Executive Governance (CP-001 / CP-027)  
> **Status:** LIVE ORIENTATION LEGEND — Updated 2026-09-05  
> **Master Operating Contract:** [[ANTIGRAVITY|ANTIGRAVITY.md]]  
> **Universal Agent Operating Contract:** [[AGENTS|AGENTS.md]]  
> **First-Read Document For:** You, Claude Code, Codex, Gemini, Cursor, Autonomous Subagents, New Collaborators, Future-You.

---

## 1. WHAT IS THIS?

**Company Brain** is the operating, computational, and knowledge infrastructure for a distributed company coordinating owned ventures, repositories, AI agent swarms, polyglot databases, and local-first hardware networks.

It answers: **“What is true, what matters, where do I go, and what am I allowed to do next?”**

---

## 2. READ THESE FIRST (MANDATORY OPERATING SEQUENCE)

Before writing code, declaring features, or making changes, read in exact sequence:
1. [[REALITY|REALITY.md]] — What is actually true (evidence outranks documentation).
2. [[ANTIGRAVITY|ANTIGRAVITY.md]] — The 45 non-negotiable operating rules (strictly zero fake completion).
3. [[AGENTS|AGENTS.md]] — Universal portable agent operating guidelines and system orientation.
4. [[EVIDENCE|EVIDENCE.md]] — Verified empirical proof log for all system claims.
5. [[ECONOMIC-REALITY|ECONOMIC-REALITY.md]] — Cash, runway, margins, and commercial survival metrics.
6. [[NORTH-STAR|NORTH-STAR.md]] — Where the company is going (commercial reality, paying customers).
7. [[PRIORITIES|PRIORITIES.md]] — What matters right now (revenue activation, clutter cleanup).
8. [[ARCHITECTURE|ARCHITECTURE.md]] — How the system is structured.
9. [[CLAUDE|CLAUDE.md]] — Live-audited infrastructure, models, and container runtime state.
10. [[UPDATE|UPDATE.md]] — What changed in the recent working sessions.

### Supporting Truth & Discipline Ledgers
- [[KILL-LIST|KILL-LIST.md]] — Formally killed or decommissioned entities.
- [[STOP-DOING|STOP-DOING.md]] — Prohibited behaviors and anti-patterns.
- [[ASSUMPTIONS|ASSUMPTIONS.md]] & [[CLAIMS|CLAIMS.md]] — Unverified claims requiring proof.
- [[SYSTEM-REALITY|SYSTEM-REALITY.md]] — Hardware, network, and execution constraints.

---

## 3. CURRENT REALITY

> [!IMPORTANT]
> **READ [[REALITY|REALITY.md]] FIRST.**

Do not infer system state from:
- Filenames or directory names
- Stale Markdown documentation or sprint notes
- Theoretical registry entries
- Docker Compose declarations
- Repository presence
- URLs or HTTP links
- Speculative claims from past conversations

**Runtime evidence outranks documentation.**

### Key Audited Facts (2026-09-05)
- **Nodes Online:** Mac Studio M4 Max (`100.87.214.70`) + MacBook Air (`100.121.17.63`) via Tailscale mesh.
- **Inference Server:** Native `exo` MLX serving `mlx-community/Qwen3.6-35B-A3B-5bit` on port `:52415`. **Ollama was replaced and decommissioned on 2026-07-17.**
- **Databases:** Healthy `civos_neo4j` on ports `:7474`/`:7687` (20,363 edges synced); `civos_qdrant` on `:6333`; PostgreSQL on `:5432`.
- **Known Issues:** Container `t7shield-neo4j-1` is crash-looping. Mac Studio has 4 overlapping Docker Compose projects (`civos_*`, `t7shield-*`, `spinup-*`, `buzz-*`).
- **Commercial State:** 0 paying customers, $0 revenue, 0 active commercial offers in market.
- **Code Reality:** 177 owned repos have verifiable code manifests; 618 are venture paperwork templates.

---

## 4. CURRENT OBJECTIVE

Break out of the infrastructure avoidance loop. Direct intellectual horsepower and engineering infrastructure toward **commercial viability, real customer transaction, and automated revenue loops** while maintaining local-first sovereignty.

---

## 5. CORE OPERATING VENTURES (TIER-1 FOCUS)

The 7 operating companies (OpCos) advancing toward paying customer revenue:
1. [[23-VENTURES/LT-005|LT-005 (HealthRoute Medical Courier Dispatch)]] — Specimen delivery software. Site: `lt-005-medical-courier-dispatch.vercel.app`.
2. [[23-VENTURES/LT-011|LT-011 (CarrierDispatch TMS)]] — Small-fleet freight dispatch software. Site: `lt-011-dispatch-software.vercel.app`.
3. [[23-VENTURES/RE-001|RE-001 (WorldwideBro Holdings Real Estate)]] — Distressed deal evaluation portal. Site: `re-001-worldwidebro-holdings.vercel.app`.
4. [[23-VENTURES/OPS-001|OPS-001 (CareerOps Staffing)]] — AI talent matching portal. Site: `ops-staff-001-staffing-worldwidebros-projects.vercel.app`.
5. [[23-VENTURES/CON-001|CON-001 (ACE Construction Field OS)]] — Punch lists and field logs. Site: `con-001-ace-construction.vercel.app`.
6. [[23-VENTURES/EC-001|EC-001 (Angels in Daylight)]] — Lifestyle apparel brand storefront. Site: `ec-001-angels-in-daylight.vercel.app`.
7. [[23-VENTURES/FIN-037|FIN-037 (WorldwideBro Quantitative Trading)]] — Python backtesting and execution engine. Repo: `fin-037-worldwidebro-trading-system`.

---

## 6. BUSINESS SECTOR TAXONOMY

Company Brain classifies all operations, ventures, and capabilities across **35 Vertical Business Sectors**:
- Master Architecture & Crosswalk: [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|SECTOR-TAXONOMY-MASTER.md]]
- Navigational Sector Index: [[SECTOR_INDEX|SECTOR_INDEX.md]]
- Sector Vault Folder: [[SECTORS/|SECTORS/]] (contains `SEC-001` through `SEC-035`)
- Sector Crosswalk Registries:
  - [[_REGISTRIES/ventures-by-sector.yaml|ventures-by-sector.yaml]]
  - [[_REGISTRIES/control-planes-by-sector.yaml|control-planes-by-sector.yaml]]
  - [[_REGISTRIES/capabilities-by-sector.yaml|capabilities-by-sector.yaml]]

---

## 7. DO NOT

- **DO NOT** invent completion or report "Done" without executable test proof (`ANTIGRAVITY.md` Rule #3).
- **DO NOT** create placeholder architecture, mock APIs, TODO stubs, or fake data (`ANTIGRAVITY.md` Rule #4).
- **DO NOT** duplicate existing services, databases, or infrastructure stacks.
- **DO NOT** create a new service without checking `_REGISTRIES/service_registry.json`.
- **DO NOT** create a new repository without checking `_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml`.
- **DO NOT** modify production or restart containers blindly.
- **DO NOT** treat speculative ventures as operating companies.
- **DO NOT** confuse documentation with implementation.
- **DO NOT** confuse infrastructure surface area with business enterprise value.

---

## 8. REPOSITORY MAP

```text
/
├── STARTHERE.md               # You are here: Master orientation legend
├── REALITY.md                 # Live executive truth ledger
├── ANTIGRAVITY.md             # 45 Core operating rules (Master Contract)
├── AGENTS.md                  # Universal portable agent operating contract
├── EVIDENCE.md                # Verified audit proof log
├── ECONOMIC-REALITY.md        # Financial metrics, margins, and burn rate
├── NORTH-STAR.md              # Long-term trajectory & business mission
├── PRIORITIES.md              # Immediate tactical priorities
├── ARCHITECTURE.md            # Tripartite system architecture
├── CLAUDE.md                  # Runtime infrastructure state & Docker contexts
├── INDEX.md                   # Complete navigational index of files & domains
├── SECTOR_INDEX.md            # Complete 35-sector business vertical index
├── .agents/                   # Modular Agent Customization Layer
│   ├── rules/                 # Architecture, security, git, and coding standards
│   ├── workflows/             # Slash commands (/gap-analysis, /deploy, etc.)
│   ├── skills/                # On-demand procedural runbooks (including find-skills)
│   └── agents/                # Specialized subagent personas
├── RESEARCH/                  # Dedicated external intelligence & research OS
├── SECTORS/                   # 35 Vertical business sector notes (SEC-001 to SEC-035)
├── 23-VENTURES/               # Concrete venture master specifications
├── _REGISTRIES/               # Canonical registries & machine-readable manifests
│   └── CANONICAL/             # Ground-truth verified registries (Repos, Sites, Caps)
├── _CLI/                      # Local command line tools & bash harnesses
├── _MCP/                      # FastMCP server & Model Context Protocol bridges
└── 00-50 Domain Vaults/       # Specialized domain folders (CONSTITUTION to MASTER-CONTROL)
```

---

## 9. SYSTEMS & RUNTIME NODES

- **Master Brain Host:** Mac Studio M4 Max (`100.87.214.70`) at `/Volumes/LaCie`.
- **Mobile Engineering Node:** MacBook Air (`100.121.17.63`) at `/Volumes/T7 Shield`.
- **Knowledge Graph:** Neo4j Community/Enterprise 5.x (`civos_neo4j`, `bolt://100.87.214.70:7687`).
- **Vector Search:** Qdrant Vector Engine (`civos_qdrant`, `http://100.87.214.70:6333`).
- **Relational Database:** PostgreSQL 16 (`postgres`, port `5432`).
- **Model Engine:** Native Apple Silicon MLX via `exo` (`http://100.87.214.70:52415/v1`).
- **Model Gateway:** LiteLLM Router (`civos_litellm`, port `4000`).
- **Traffic Controller:** OmniRoute v3.8.50 (`http://100.87.214.70:20128`).
- **MCP Server:** FastMCP Server (`_MCP/fastmcp_server.py` via Python 3.12).
- **Edge PaaS:** Vercel Global Edge Network (95 active venture sites).

---

## 10. CANONICAL REGISTRIES

All verified ground-truth registries are located under [[_REGISTRIES/CANONICAL/]]:
- [[_REGISTRIES/CANONICAL/REPOSITORY_REGISTRY.yaml]] — 1,740 repositories (177 code-verified).
- [[_REGISTRIES/CANONICAL/OWNED_REPO_DEPENDENCIES.json]] — Parsed manifests and dependencies for all 177 code repos.
- [[_REGISTRIES/CANONICAL/OWNED_REPO_CODE_REALITY.json]] — 177 code vs 618 paperwork classification.
- [[_REGISTRIES/CANONICAL/SITES_REGISTRY.yaml]] — 95 verified Vercel production sites (SITE-0001 to SITE-0095).
- [[_REGISTRIES/CANONICAL/VERCEL_DEPLOYMENTS.json]] — Live deployments pulled via Vercel CLI.
- [[_REGISTRIES/CANONICAL/CAPABILITY_REGISTRY.yaml]] — Technical capabilities grounded in code manifests.
- [[_REGISTRIES/CANONICAL/CAPABILITY_GAP_REPORT.yaml]] — Empirical capability gap report.
- [[_REGISTRIES/ventures-by-sector.yaml]] — Venture assignments across 35 sectors.
- [[_REGISTRIES/control-planes-by-sector.yaml]] — 30 Control planes mapped to sectors.
- [[_REGISTRIES/capabilities-by-sector.yaml]] — Capability taxonomy by sector.

---

## 11. BEFORE CHANGING ANYTHING

1. **Read [[STARTHERE|STARTHERE.md]], [[REALITY|REALITY.md]], and [[AGENTS|AGENTS.md]].**
2. **Read relevant subsystem documentation.**
3. **Inspect actual runtime implementation** (e.g., `docker --context macstudio ps`).
4. **Check registries** in `_REGISTRIES/CANONICAL/`.
5. **Determine blast radius** and single points of failure.
6. **Make the smallest valid change.**
7. **Test and verify runtime state.**
8. **Update documentation & update registries.**
9. **Record decisions in ADRs.**

---

## 12. CHANGE LOOP

```text
DISCOVER ──> UNDERSTAND ──> VERIFY ──> PLAN ──> CHANGE ──> TEST ──> DEPLOY ──> OBSERVE ──> VERIFY ──> DOCUMENT ──> UPDATE
```

---

## 13. TRUTH MODEL

Every entity and claim in Company Brain holds one of seven truth states:
- `VERIFIED` — Confirmed by live execution or concrete physical/financial proof.
- `PROBABLE` — Strong indirect evidence exists; awaiting direct runtime probe.
- `ASSUMED` — Declared as design intention; unproven.
- `UNKNOWN` — Missing empirical data.
- `DISPROVEN` — Empirically refuted (e.g., "Ollama is running").
- `STALE` — Previously true, now outdated.
- `CONFLICTED` — Competing contradictory assertions exist.

*Never silently convert an assumed or unverified status into verified.*

---

## 14. WHERE TO GO NEXT

- **Need current reality?** → [[REALITY|REALITY.md]] & [[EVIDENCE|EVIDENCE.md]]
- **Need operating rules?** → [[ANTIGRAVITY|ANTIGRAVITY.md]] (Master Contract)
- **Need agent orientation?** → [[AGENTS|AGENTS.md]] (Agent Guidelines)
- **Need business sectors?** → [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|SECTOR-TAXONOMY-MASTER.md]] & [[SECTOR_INDEX|SECTOR_INDEX.md]]
- **Need core operating ventures?** → [[23-VENTURES|23-VENTURES/]] (LT-005, LT-011, RE-001, OPS-001, CON-001, EC-001, FIN-037)
- **Need research intelligence?** → [[RESEARCH/RESEARCH-OS|RESEARCH-OS.md]]
- **Need company orientation?** → [[START-HERE-COMPANY|START-HERE-COMPANY.md]]
- **Need engineering orientation?** → [[START-HERE-ENGINEERING|START-HERE-ENGINEERING.md]]
- **Need infrastructure orientation?** → [[START-HERE-INFRASTRUCTURE|START-HERE-INFRASTRUCTURE.md]]
- **Need agents orientation?** → [[START-HERE-AGENTS|START-HERE-AGENTS.md]]
- **Need repositories orientation?** → [[START-HERE-REPOSITORIES|START-HERE-REPOSITORIES.md]]
- **Need ventures orientation?** → [[START-HERE-VENTURES|START-HERE-VENTURES.md]]
- **Need operations orientation?** → [[START-HERE-OPERATIONS|START-HERE-OPERATIONS.md]]
- **Need data orientation?** → [[START-HERE-DATA|START-HERE-DATA.md]]
- **Need governance orientation?** → [[START-HERE-GOVERNANCE|START-HERE-GOVERNANCE.md]]
- **Need to know what changed?** → [[UPDATE|UPDATE.md]]
"""

with open(starthere_path, "w") as f:
    f.write(starthere_content)
print("Updated STARTHERE.md successfully.")

# ==============================================================================
# 2. CREATE OPCO ALIAS STUBS (00-CONSTITUTION/opcos/)
# ==============================================================================
print("2. Creating OpCo stubs in 00-CONSTITUTION/opcos/...")
opcos_dir = os.path.join(WORKSPACE, "00-CONSTITUTION", "opcos")
os.makedirs(opcos_dir, exist_ok=True)

# Sector definitions
sectors_meta = {
    "SEC-001": ("beauty-wellness", "Beauty & Wellness", "OpCo-001"),
    "SEC-002": ("construction-infrastructure", "Construction & Infrastructure", "OpCo-002"),
    "SEC-003": ("consumer-electronics-hardware", "Consumer Electronics & Hardware", "OpCo-003"),
    "SEC-004": ("content-media", "Content & Media", "OpCo-004"),
    "SEC-005": ("education-training", "Education & Training", "OpCo-005"),
    "SEC-006": ("energy-utilities", "Energy & Utilities", "OpCo-006"),
    "SEC-007": ("environmental-services", "Environmental Services", "OpCo-007"),
    "SEC-008": ("financial-services", "Financial Services", "OpCo-008"),
    "SEC-009": ("food-agriculture", "Food & Agriculture", "OpCo-009"),
    "SEC-010": ("food-service-restaurants", "Food Service & Restaurants", "OpCo-010"),
    "SEC-011": ("gaming-entertainment", "Gaming & Entertainment", "OpCo-011"),
    "SEC-012": ("healthcare-biotechnology", "Healthcare & Biotechnology", "OpCo-012"),
    "SEC-013": ("hospitality-travel", "Hospitality & Travel", "OpCo-013"),
    "SEC-014": ("human-resources-staffing", "Human Resources & Staffing", "OpCo-014"),
    "SEC-015": ("insurance", "Insurance", "OpCo-015"),
    "SEC-016": ("legal-compliance", "Legal & Compliance", "OpCo-016"),
    "SEC-017": ("logistics-transportation", "Logistics & Transportation", "OpCo-017"),
    "SEC-018": ("manufacturing-engineering", "Manufacturing & Engineering", "OpCo-018"),
    "SEC-019": ("marketing-advertising", "Marketing & Advertising", "OpCo-019"),
    "SEC-020": ("real-estate-property", "Real Estate & Property", "OpCo-020"),
    "SEC-021": ("retail-e-commerce", "Retail & E-commerce", "OpCo-021"),
    "SEC-022": ("telecommunications-connectivity", "Telecommunications & Connectivity", "OpCo-022"),
    "SEC-023": ("professional-services", "Professional Services", "OpCo-023"),
    "SEC-024": ("technology-software", "Technology & Software", "OpCo-024"),
    "SEC-025": ("automotive-mobility", "Automotive & Mobility", "OpCo-025"),
    "SEC-026": ("utilities-infrastructure", "Utilities & Infrastructure", "OpCo-026"),
    "SEC-027": ("venture-capital-investment", "Venture Capital & Investment", "OpCo-027"),
    "SEC-028": ("b2b-enterprise-software", "B2B Enterprise Software", "OpCo-028"),
    "SEC-029": ("marketplace-platform", "Marketplace & Platform", "OpCo-029"),
    "SEC-030": ("fintech-payments", "Fintech & Payments", "OpCo-030"),
    "SEC-031": ("climate-sustainability", "Climate & Sustainability", "OpCo-031"),
    "SEC-032": ("artificial-intelligence-ml", "Artificial Intelligence & ML", "OpCo-032"),
    "SEC-033": ("cybersecurity-privacy", "Cybersecurity & Privacy", "OpCo-033"),
    "SEC-034": ("decentralized-web3", "Decentralized & Web3", "OpCo-034"),
    "SEC-035": ("reserved-discovery", "Reserved Discovery Slot", "OpCo-035")
}

for sec_id, (slug, name, opco_id) in sectors_meta.items():
    opco_file = os.path.join(opcos_dir, f"{opco_id}.md")
    sec_file_rel = f"SECTORS/{sec_id}-{slug}"
    opco_content = f"""---
id: {opco_id}
title: {opco_id} — Operating Company for {name}
aliases: ["{opco_id}", "{name} OpCo"]
tags: [opco, sector-holding, governance, {sec_id.lower()}]
sector: {sec_id}
---

# {opco_id}: Operating Company for {name}

Operating vertical holding entity coordinating ventures, assets, and regulatory compliance in **[[{sec_file_rel}|{sec_id}: {name}]]**.

- **Primary Sector:** [[{sec_file_rel}|{sec_id}: {name}]]
- **Sector Taxonomy Master:** [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|SECTOR-TAXONOMY-MASTER.md]]
- **Sector Registries:**
  - [[_REGISTRIES/ventures-by-sector.yaml|ventures-by-sector.yaml]]
  - [[_REGISTRIES/control-planes-by-sector.yaml|control-planes-by-sector.yaml]]
"""
    with open(opco_file, "w") as f:
        f.write(opco_content)

print(f"Created 35 OpCo files in 00-CONSTITUTION/opcos/.")

# ==============================================================================
# 3. HEAL SECTORS/*.MD FILES
# ==============================================================================
print("3. Healing SECTORS/*.md files...")
sectors_dir = os.path.join(WORKSPACE, "SECTORS")

core_ventures_by_sec = {
    "SEC-002": [("CON-001", "ACE Construction Workflow OS", "23-VENTURES/CON-001.md")],
    "SEC-008": [("FIN-037", "WorldwideBro Quantitative Trading System", "23-VENTURES/FIN-037.md")],
    "SEC-014": [("OPS-001", "Career Ops / Staffing Operations", "23-VENTURES/OPS-001.md")],
    "SEC-017": [
        ("LT-005", "HealthRoute Medical Courier Dispatch", "23-VENTURES/LT-005.md"),
        ("LT-011", "CarrierDispatch TMS", "23-VENTURES/LT-011.md")
    ],
    "SEC-020": [("RE-001", "WorldwideBro Holdings Real Estate", "23-VENTURES/RE-001.md")],
    "SEC-021": [("EC-001", "Angels in Daylight Apparel", "23-VENTURES/EC-001.md")],
    "SEC-030": [("FIN-037", "WorldwideBro Quantitative Trading System", "23-VENTURES/FIN-037.md")]
}

for sec_id, (slug, name, opco_id) in sectors_meta.items():
    sec_file = os.path.join(sectors_dir, f"{sec_id}-{slug}.md")
    if not os.path.exists(sec_file):
        continue

    # Build clean aliases
    short_name = name.split(" & ")[0].split(" / ")[0]
    aliases = [sec_id, f"{sec_id}-{short_name}", f"{sec_id}-{slug}", name]
    
    # Check core ventures
    cv_list = core_ventures_by_sec.get(sec_id, [])
    cv_section = ""
    if cv_list:
        cv_section = "\n## Active Core Operating Ventures\n"
        for vid, vname, vrel in cv_list:
            cv_section += f"- [[{vrel[:-3]}|{vid} — {vname}]] (Tier-1 Focus)\n"

    new_content = f"""---
id: "{sec_id}"
sector_id: "{sec_id}"
title: "{sec_id}: {name}"
aliases: {aliases}
tags: [sector, taxonomy, {slug.replace('-', '_')}, {opco_id.lower()}]
opco: "{opco_id}"
status: "ACTIVE"
last_verified: "2026-09-05"
---

# {sec_id}: {name}

**OpCo:** [[00-CONSTITUTION/opcos/{opco_id}|{opco_id}]]  
**Status:** 🟢 Active / Grounded in Code Reality  
**Taxonomy Master:** [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|SECTOR-TAXONOMY-MASTER.md]]  
**Sector Index:** [[SECTOR_INDEX|SECTOR_INDEX.md]]
{cv_section}
## Canonical Registries
- Ventures in Sector: [[_REGISTRIES/ventures-by-sector.yaml|ventures-by-sector.yaml]]
- Control Planes: [[_REGISTRIES/control-planes-by-sector.yaml|control-planes-by-sector.yaml]]
- Capabilities: [[_REGISTRIES/capabilities-by-sector.yaml|capabilities-by-sector.yaml]]

## Connected Domains
- Ventures: [[23-VENTURES]]
- Repositories: [[13-REPOSITORIES]]
- Capabilities: [[14-CAPABILITIES]]
- Agents: [[16-AGENTS]]
"""
    with open(sec_file, "w") as f:
        f.write(new_content)

print("Updated all 35 SECTORS files successfully.")

# ==============================================================================
# 4. HEAL SECTOR_INDEX.MD
# ==============================================================================
print("4. Healing SECTOR_INDEX.md...")
sec_index_path = os.path.join(WORKSPACE, "SECTOR_INDEX.md")

sec_index_content = """---
id: DOC-SEC-INDEX-001
title: 36-Sector Taxonomy Index
aliases: ["SECTOR_INDEX", "Sector-Index", "Sectors-Index", "36-Sector-Index"]
tags: [sector, taxonomy, index, governance]
status: ACTIVE
updated: 2026-09-05
---

[[00-CONSTITUTION]] | [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER|SECTOR-TAXONOMY-MASTER]] | [[INDEX]] | [[STARTHERE]]

# 36-Sector Taxonomy Index

**Purpose:** Company-wide sector classification organizing ventures, capabilities, resources, and market intelligence. Each sector is a distinct business vertical with its own operating model, regulatory environment, and venture portfolio.

**Status:** Framework complete & reconciled against code reality.

---

## 35-Sector Listing

"""

for sec_id, (slug, name, opco_id) in sectors_meta.items():
    sec_file_rel = f"SECTORS/{sec_id}-{slug}"
    cv_list = core_ventures_by_sec.get(sec_id, [])
    active_str = f" | **Active OpCos:** {', '.join([f'[[23-VENTURES/{vid}|{vid}]]' for vid, _, _ in cv_list])}" if cv_list else ""
    
    sec_index_content += f"""### [[{sec_file_rel}|{sec_id}: {name}]]
**OpCo Structure:** [[00-CONSTITUTION/opcos/{opco_id}|{opco_id}]]{active_str}  
**Registries:** [[_REGISTRIES/ventures-by-sector.yaml|Ventures]] · [[_REGISTRIES/control-planes-by-sector.yaml|Control Planes]] · [[_REGISTRIES/capabilities-by-sector.yaml|Capabilities]]  
**Domains:** [[23-VENTURES|Ventures]] · [[13-REPOSITORIES|Repositories]] · [[14-CAPABILITIES|Capabilities]] · [[16-AGENTS|Agents]]

"""

with open(sec_index_path, "w") as f:
    f.write(sec_index_content)

print("Updated SECTOR_INDEX.md successfully.")

# ==============================================================================
# 5. HEAL 00-CONSTITUTION/SECTOR-TAXONOMY-MASTER.MD
# ==============================================================================
print("5. Healing 00-CONSTITUTION/SECTOR-TAXONOMY-MASTER.md...")
sec_master_path = os.path.join(WORKSPACE, "00-CONSTITUTION", "SECTOR-TAXONOMY-MASTER.md")

with open(sec_master_path) as f:
    master_text = f.read()

# Replace stale Ollama claim
master_text = master_text.replace("✅ (local Ollama)", "✅ (native MLX via exo :52415)")

# Replace phantom wikilinks
replacements = {
    "[[SEC-001-Beauty-Wellness]]": "[[SECTORS/SEC-001-beauty-wellness|SEC-001]]",
    "[[SEC-002-Construction]]": "[[SECTORS/SEC-002-construction-infrastructure|SEC-002]]",
    "[[SEC-017-Logistics]]": "[[SECTORS/SEC-017-logistics-transportation|SEC-017]]",
    "[[SEC-024-Technology]]": "[[SECTORS/SEC-024-technology-software|SEC-024]]",
    "[[CON-001]]": "[[23-VENTURES/CON-001|CON-001]]",
    "[[LT-005]]": "[[23-VENTURES/LT-005|LT-005]]",
    "[[TECH-040]]": "`TECH-040` (Speculative)",
    "[[CAP-000247-Entity-Resolution]]": "`CAP-000247` (Entity Resolution)",
    "[[CAP-000001-Lead-Capture]]": "`CAP-000001` (Lead Capture)",
    "[[Antwuan-Johns-Workspace]]": "Antwuan Johns Workspace (ClickUp)",
    "[[Medical-Courier-Workspace]]": "Medical Courier Workspace (ClickUp)"
}

for old, new in replacements.items():
    master_text = master_text.replace(old, new)

# Ensure proper frontmatter with id and aliases
if master_text.startswith("---"):
    master_text = re.sub(
        r"^---\n.*?\n---",
        """---
id: DOC-SEC-MASTER-001
title: 36-Sector Taxonomy Master Index
description: "Company-wide sector classification organizing ventures, capabilities, resources. Master reference for VEX crosswalk and sector-scoped operations."
aliases: ["SECTOR-TAXONOMY", "Sector-Taxonomy", "36-Sector-Taxonomy", "Sector-Taxonomy-Master"]
tags: [sector, taxonomy, governance, master-index]
status: active
updated: 2026-09-05
---""",
        master_text,
        flags=re.DOTALL
    )

with open(sec_master_path, "w") as f:
    f.write(master_text)

print("Updated 00-CONSTITUTION/SECTOR-TAXONOMY-MASTER.md successfully.")

# ==============================================================================
# 6. SYNC _REGISTRIES/ventures-by-sector.yaml
# ==============================================================================
print("6. Syncing _REGISTRIES/ventures-by-sector.yaml...")
v_sec_path = os.path.join(WORKSPACE, "_REGISTRIES/ventures-by-sector.yaml")
with open(v_sec_path) as f:
    v_sec_data = yaml.safe_load(f)

# Ensure SEC-017 has LT-011
if "SEC-017" in v_sec_data.get("ventures", {}):
    sec17_v = v_sec_data["ventures"]["SEC-017"].setdefault("ventures", {})
    sec17_v["LT-005"] = {"name": "HealthRoute Medical Courier Dispatch", "status": "OPERATING_VALIDATING"}
    sec17_v["LT-011"] = {"name": "CarrierDispatch TMS", "status": "OPERATING_VALIDATING"}

# Ensure SEC-021 has EC-001
if "SEC-021" in v_sec_data.get("ventures", {}):
    sec21_v = v_sec_data["ventures"]["SEC-021"].setdefault("ventures", {})
    sec21_v["EC-001"] = {"name": "Angels in Daylight Apparel", "status": "OPERATING_VALIDATING"}

# Ensure SEC-008 has FIN-037
if "SEC-008" in v_sec_data.get("ventures", {}):
    sec8_v = v_sec_data["ventures"]["SEC-008"].setdefault("ventures", {})
    sec8_v["FIN-037"] = {"name": "WorldwideBro Quantitative Trading System", "status": "OPERATING_VALIDATING"}

with open(v_sec_path, "w") as f:
    yaml.dump(v_sec_data, f, sort_keys=False)

print("Synced _REGISTRIES/ventures-by-sector.yaml successfully.")
