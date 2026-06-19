# UNIFIED REPO NAMING STANDARD & Action Plan for 42 Scattered Repos

**Generated:** 2026-06-05  
**Status:** 🔴 ACTION REQUIRED — 42 repos need renaming/recategorization  
**Audience:** Engineering team, repo governance  

---

## THE PROBLEM: 855 Repos Not Coherently Named

| Category | Count | Status | Problem |
|----------|-------|--------|---------|
| ✅ Venture Repos (20 prefixes) | 580 | Good | Correctly named |
| ⚠️ Infrastructure Repos | 233 | Named OK | No unified prefix |
| 🔴 Misnamed/Scattered Repos | 42 | **BROKEN** | Unclear category, wrong prefix |

**Issue:** You have ONE body (855 repos serving 712 ventures across 9 layers), but repo names scatter across 40+ different prefixes instead of unified naming.

---

## UNIFIED NAMING STANDARD (ONE BODY)

### Standard 1: Venture Repos (580 repos across 20 categories)

**Format:** `PREFIX-NUMBER-NAME`

```
EC-001-Angels-in-Daylight              → E-commerce
OPS-002-Supply-Chain-Optimizer         → Operations  
TECH-001-Quantum-Algorithm-AI          → Technology
SPEC-004-Private-Chef-AI               → Specialized Services
EM-001-Space-Habitat-AI                → Emerging Tech
COMM-002-Brotherhood-Coaching          → Community/Social
EDU-003-Coding-Mentor-Cert             → Education
BW-001-Lash-Extension-Studio           → Beauty/Wellness
FIN-001-GenixBank-Lite                 → Financial
FH-001-Personal-Chef-Service           → Food/Hospitality
ST-001-SaaS-Platform                   → Software-Tech
LT-002-Freight-Brokerage               → Logistics/Transport
PS-001-Business-Consulting             → Professional Services
FS-001-Gym                             → Fitness/Sports
MC-001-YouTube-Channel-Network         → Media/Content
CON-001-ACE-Construction               → Construction
ET-001-Online-Tutoring                 → EdTech
FI-001-Financial-Interest              → Financial-Interest
RE-001-Real-Estate-Empire              → Real Estate
PROFILE-001-Name                       → Profile/Misc
```

### Standard 2: Platform Infrastructure (77 repos)

**Format:** `PLATFORM-NUMBER-COMPONENT` or `SYSTEM-NAME`

```
IZA-001 through IZA-186                → IZA OS Knowledge Graph
AI-001-Boss-Holdings-V4                → AI Agent Platform
VENTURE-HUB-Core                       → Venture management
PITCH-KIT-Core                         → Pitch generation
MISSION-CONTROL-Orchestrator           → Task orchestration
THUNDERBOLT-Engine                     → Agent execution
CIVILIZATION-OS-Core                   → Core OS system
LIGHTRAG-Core                          → Semantic indexing
```

### Standard 3: Cross-Functional Infrastructure (198 repos)

**Format:** `INFRA-[TYPE]-[NAME]`

```
INFRA-TEMPLATE-Business-Model          → Reusable templates
INFRA-FRAMEWORK-Shared-Kernels         → Shared code
INFRA-AUTOMATION-Workflow-System       → Automation tools
INFRA-SYSTEM-Governance                → Governance systems
INFRA-TOOL-Data-Management             → Operational tools
INFRA-PLATFORM-Media-Empire            → Platform systems
INFRA-INTEGRATION-External-Services    → Third-party integrations
```

---

## 42 MISNAMED REPOS: How to Fix

### Group A: Venture Repos That Use Wrong Prefix (14 repos)

These should be renamed to fit one of the 20 venture categories:

| Current | New Name | Category | Reasoning |
|---------|----------|----------|-----------|
| consult-001-venture-consulting | PS-026-Venture-Consulting | Professional Services | Consulting → PS |
| deliv-713-roadrunner-cannabis | LT-031-Roadrunner-Cannabis | Logistics/Transport | Delivery → LT |
| ft-001-api-gateway | TECH-062-FT-API-Gateway | Technology | FinTech → TECH |
| ft-001-core-ledger | TECH-063-FT-Core-Ledger | Technology | FinTech → TECH |
| ft-001-docs | TECH-064-FT-Docs | Technology | FinTech → TECH |
| fund-001-civilization-credit-fund | FIN-037-Civilization-Fund | Financial | Fund → FIN |
| ins-001-venture-insurance | FIN-038-Venture-Insurance | Financial | Insurance → FIN |
| ht-004-data-api | ST-031-HT-Data-API | Software-Tech | Tech product → ST |
| ht-004-firmware | ST-032-HT-Firmware | Software-Tech | Tech product → ST |
| ht-004-mobile-app | ST-033-HT-Mobile-App | Software-Tech | Tech product → ST |
| investment-fund-management | FIN-039-Investment-Fund-Mgmt | Financial | Investment → FIN |
| tax-company-2026 | FIN-040-Tax-Preparation | Financial | Tax → FIN |
| quantum-brain-sync-website | TECH-065-Quantum-Brain-Sync | Technology | Advanced tech → TECH |
| real-estate-empire | RE-001-Real-Estate-Empire | Real Estate | RE-001 (already correct) |

### Group B: Infrastructure Repos With Wrong Prefix (28 repos)

These should be renamed with INFRA prefix:

| Current | New Name | Type |
|---------|----------|------|
| autonomous-venture-studio | INFRA-FRAMEWORK-Autonomous-Venture-Studio | Framework |
| business-template-marketplace | INFRA-TEMPLATE-Business-Templates | Template |
| ace-community-impact-templates | INFRA-TEMPLATE-ACE-Community | Template |
| ace-ecommerce-templates | INFRA-TEMPLATE-ACE-Ecommerce | Template |
| acquisition-vehicle-automation | INFRA-AUTOMATION-Acquisition-Vehicle | Automation |
| avs-omni | INFRA-PLATFORM-AVS-Omni | Platform |
| billionaire-brain-assistant | INFRA-TOOL-Billionaire-Brain | Tool |
| billionaire-consciousness-empire | INFRA-SYSTEM-Billionaire-Consciousness | System |
| billionaire-workflow-automation | INFRA-AUTOMATION-Billionaire-Workflow | Automation |
| capital-orchestrator | INFRA-SYSTEM-Capital-Orchestrator | System |
| consciousness-deployment-system | INFRA-SYSTEM-Consciousness-Deployment | System |
| data-management | INFRA-TOOL-Data-Management | Tool |
| deployment-orchestrator | INFRA-SYSTEM-Deployment-Orchestrator | System |
| enhanced-cursor-rules | INFRA-CONFIG-Cursor-Rules | Config |
| genixbank-insight-compass | INFRA-TOOL-GenixBank-Insight | Tool |
| intellectual-property-management | INFRA-SYSTEM-IP-Management | System |
| maps | INFRA-TOOL-Maps-Visualization | Tool |
| media-empire-platform | INFRA-PLATFORM-Media-Empire | Platform |
| mobile-access-manager | INFRA-SYSTEM-Mobile-Access | System |
| nexus-ai-enterprise-platform | INFRA-PLATFORM-Nexus-AI | Platform |
| partnership-network-management | INFRA-SYSTEM-Partnership-Network | System |
| research-processing-pipeline | INFRA-SYSTEM-Research-Pipeline | System |
| shared-kernels | INFRA-FRAMEWORK-Shared-Kernels | Framework |
| sovereign-life | INFRA-PLATFORM-Sovereign-Life | Platform |
| wealth-optimization-platform | INFRA-PLATFORM-Wealth-Optimization | Platform |
| xyops-integration | INFRA-INTEGRATION-XYOPS | Integration |
| _master-governance | INFRA-SYSTEM-Master-Governance | System |
| clients | INFRA-CONFIG-Clients-Registry | Config |

### Group C: Personal/Archive (Archive or Delete)

| Current | Action | Reason |
|---------|--------|--------|
| Resume | ARCHIVE | Personal document |
| divine-johns-portfolio | ARCHIVE | Personal portfolio |
| babystepsmatrix1 | ARCHIVE | Personal project |
| claude-workflow-demo | ARCHIVE | Demo/example |
| Up-Next-Marketplace | DELETE | Old planning |
| YES-LLC-CONTRACTOR-DELIVERY | DELETE | Defunct entity |
| Avs-Omni- | DELETE | Duplicate of avs-omni |

---

## THE ONE UNIFIED BODY (After Renaming)

```
ALL 855 REPOS NOW FOLLOW ONE NAMING SYSTEM:

├─ VENTURE REPOS (580 repos)
│  ├─ EC-* (E-commerce, 110)
│  ├─ OPS-* (Operations, 67)
│  ├─ TECH-* (Technology, 61)
│  ├─ SPEC-* (Specialized, 50)
│  ├─ EM-* (Emerging, 50)
│  ├─ COMM-* (Community, 50)
│  ├─ EDU-* (Education, 40)
│  ├─ BW-* (Beauty/Wellness, 40)
│  ├─ FIN-* (Financial, 36)
│  ├─ FH-* (Food/Hospitality, 35)
│  ├─ ST-* (Software-Tech, 30)
│  ├─ LT-* (Logistics, 30)
│  ├─ PS-* (Professional Services, 25)
│  ├─ FS-* (Fitness/Sports, 25)
│  ├─ MC-* (Media/Content, 20)
│  ├─ CON-* (Construction, 20)
│  ├─ ET-* (EdTech, 16)
│  ├─ FI-* (Financial-Interest, 5)
│  ├─ RE-* (Real Estate, 1)
│  └─ PROFILE-* (Profile, 1)

├─ PLATFORM INFRASTRUCTURE (77 repos)
│  ├─ IZA-* (Knowledge graph, 186... wait, that's separate)
│  ├─ AI-* (Agents, 7)
│  ├─ VENTURE-* (Hub)
│  ├─ PITCH-* (Generation)
│  ├─ MISSION-* (Orchestration)
│  ├─ THUNDERBOLT-* (Execution)
│  └─ CIVILIZATION-* (OS)

└─ CROSS-FUNCTIONAL INFRASTRUCTURE (198 repos)
   ├─ IZA-* (Knowledge graph, 186)
   ├─ INFRA-TEMPLATE-* (Templates)
   ├─ INFRA-FRAMEWORK-* (Frameworks)
   ├─ INFRA-AUTOMATION-* (Automation)
   ├─ INFRA-SYSTEM-* (Systems)
   ├─ INFRA-TOOL-* (Tools)
   ├─ INFRA-PLATFORM-* (Platforms)
   └─ INFRA-INTEGRATION-* (Integrations)

RESULT: 0 scattered/misnamed repos
        855/855 repos follow one unified naming system
        ONE COHERENT BODY
```

---

## Execution Steps

### 1. Rename Repos (GitHub CLI)
```bash
# Example: Rename consult-001 to PS-026
gh repo rename Worldwidebro/consult-001-venture-consulting \
  --new-name ps-026-venture-consulting

# Repeat for all 42 repos using script
for repo in $(cat /tmp/repos_to_rename.txt); do
  # Apply mapping from table above
  gh repo rename Worldwidebro/$repo --new-name [NEW_NAME]
done
```

### 2. Update Registry
```bash
# Edit MASTER-REPO-REGISTRY.csv with new names
# Update CSV rows to match new naming

# Run sync scripts
python3 populate_venture_knowledge_graph.py
python3 obsidian_graph_sync.py
```

### 3. Verify Completion
```bash
# Should return 855 (all repos)
gh repo list Worldwidebro --limit 1000 --json name | jq 'length'

# Should return 0 (no misnamed)
gh repo list Worldwidebro --limit 1000 --json name | \
  jq '.[] | select(.name | test("[^A-Z0-9-]")) | .name' | wc -l
```

---

## Files to Update After Renaming

1. ✅ MASTER-REPO-REGISTRY.csv
2. ✅ DATA-SOURCES.md
3. ✅ COMPLETE-855-GITHUB-REPOS-MAPPING.md
4. ✅ Supabase (via populate script)
5. ✅ Obsidian (via sync script)

---

## Result: ONE UNIFIED BODY ✅

- All 855 repos follow one naming standard
- Clear categorization (Venture / Platform / Infrastructure)
- No scattered/misnamed repos
- Easy navigation and understanding
- Coherent with 9-layer architecture
- Single source of truth

