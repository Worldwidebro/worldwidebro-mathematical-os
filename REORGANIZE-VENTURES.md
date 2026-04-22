# 🗂️ Venture Reorganization Plan — From Technical to Legal Structure

**Generated:** 2026-04-22
**Goal:** Reorganize folders to match legal/corporate structure
**Current State:** 24 venture folders at `/Documents/` root
**Target State:** Organized by divisions, sectors, and legal entities

---

## 📊 CURRENT STATE (Folders at /Documents/)

### Active Venture Folders (24 total):

| Folder | Sector | Status | GitHub Repo |
|--------|--------|--------|-------------|
| `bw-001-lash-extension-studio/` | Beauty & Wellness | 🟡 Validation | github.com/Worldwidebro/bw-001-lash-extension-studio |
| `con-001-ace-construction/` | Construction | 🟡 Validation | github.com/Worldwidebro/con-001-ace-construction |
| `venture-hub/` | Operations | ✅ Active | github.com/Worldwidebro/venture-hub |
| `venture-factory-core/` | Operations | ✅ Complete | github.com/Worldwidebro/venture-factory-core |
| `autonomous-venture-studio/` | Technology | ✅ Active | github.com/Worldwidebro/autonomous-venture-studio |
| `ai-venture-studio-template/` | Technology | ✅ Template | github.com/Worldwidebro/ai-venture-studio-template |
| `business-template-marketplace/` | E-Commerce | ✅ Active | github.com/Worldwidebro/business-template-marketplace |
| `pitch-kit/` | Operations | ✅ Active | github.com/Worldwidebro/pitch-kit |
| `iza-os-rag-system/` | Technology | 🟡 Development | github.com/Worldwidebro/iza-os-rag-system |
| `mcp-dashboard/` | Operations | 🟡 Development | github.com/Worldwidebro/mcp-dashboard |
| `The office/` | Operations | ✅ Active | github.com/Worldwidebro/the-office |
| `civilization-os-local/` | Operations | 📦 Archive | github.com/Worldwidebro/civilization-os-local |
| `SecondBrain/` | Operations | 🟡 Development | (private) |
| `data/` | Operations | 🟡 Active | (internal) |
| `archive/` | Operations | 📦 Archive | (internal) |
| `Claude/` | Operations | 🗑️ Delete | (delete) |

---

## 🎯 TARGET STATE (Legal Structure)

### New Folder Hierarchy:

```
/Users/acebless/Documents/Winners-Circle-WC-Holdings/
├── 00-Holdings-Board/
│   └── [Board minutes, resolutions, cap tables]
│
├── 01-Divisions/
│   ├── Division-1-Beauty-Wellness/
│   │   └── BW-001-Lash-Extension-Studio/
│   │       ├── Legal/ (LLC docs, EIN, operating agreement)
│   │       ├── Financials/ (P&L, balance sheet, tax returns)
│   │       ├── Operations/ (SOPs, contracts, vendor docs)
│   │       └── Code/ (symlink to existing code repo)
│   │
│   ├── Division-2-Construction-Logistics/
│   │   ├── CON-001-Ace-Construction/
│   │   └── LT-001-Truck-Dispatch/
│   │
│   ├── Division-3-Financial-Services/
│   │   ├── FIN-001-Genixbank-Lite/
│   │   └── FIN-036-Arbitrage-Nexus/
│   │
│   ├── Division-4-Technology-AI/
│   │   ├── TECH-001-AI-Code-Generator/
│   │   └── [Other tech ventures]
│   │
│   └── Division-5-E-Commerce-Retail/
│       ├── EC-001-E-Commerce-Platform/
│       └── [Other EC ventures]
│
├── 02-Shared-Services/
│   ├── HR-Recruiting/
│   ├── Accounting-Finance/
│   ├── Legal-Compliance/
│   ├── Marketing-Brand/
│   ├── IT-Infrastructure/
│   └── Capital-Management/
│
├── 03-Venture-Hub-Inc/          ← Current venture-hub folder
│   ├── app/
│   ├── docs/
│   └── [all existing files]
│
├── 04-Capital-Management-LLC/   ← FIN-036 function
│   ├── Grants/
│   ├── Loans/
│   ├── Government-Contracts/
│   └── Investments/
│
├── 05-Legal-Entity-Docs/
│   ├── Winners-Circle-WC-Holdings-LLC/
│   ├── BW-001-LLC/
│   ├── CON-001-LLC/
│   └── [All 687 subsidiaries]
│
└── 06-Code-Repositories/        ← Symlinks to GitHub repos
    ├── bw-001-lash-extension-studio/
    ├── con-001-ace-construction/
    └── [All other code repos]
```

---

## 🔄 MIGRATION PLAN

### Phase 1: Create New Structure (30 minutes)

```bash
# Navigate to Documents
cd /Users/acebless/Documents

# Create holding company structure
mkdir -p Winners-Circle-WC-Holdings/00-Holdings-Board
mkdir -p Winners-Circle-WC-Holdings/01-Divisions/Division-1-Beauty-Wellness
mkdir -p Winners-Circle-WC-Holdings/01-Divisions/Division-2-Construction-Logistics
mkdir -p Winners-Circle-WC-Holdings/01-Divisions/Division-3-Financial-Services
mkdir -p Winners-Circle-WC-Holdings/01-Divisions/Division-4-Technology-AI
mkdir -p Winners-Circle-WC-Holdings/01-Divisions/Division-5-E-Commerce-Retail
mkdir -p Winners-Circle-WC-Holdings/02-Shared-Services
mkdir -p Winners-Circle-WC-Holdings/03-Venture-Hub-Inc
mkdir -p Winners-Circle-WC-Holdings/04-Capital-Management-LLC
mkdir -p Winners-Circle-WC-Holdings/05-Legal-Entity-Docs
mkdir -p Winners-Circle-WC-Holdings/06-Code-Repositories
```

### Phase 2: Move Venture Folders (1 hour)

```bash
# Move active ventures to proper divisions
cd /Users/acebless/Documents

# Beauty & Wellness (BW-001)
mv bw-001-lash-extension-studio Winners-Circle-WC-Holdings/01-Divisions/Division-1-Beauty-Wellness/BW-001-Lash-Extension-Studio

# Construction (CON-001)
mv con-001-ace-construction Winners-Circle-WC-Holdings/01-Divisions/Division-2-Construction-Logistics/CON-001-Ace-Construction

# Technology/AI ventures
mv autonomous-venture-studio Winners-Circle-WC-Holdings/01-Divisions/Division-4-Technology-AI/Autonomous-Venture-Studio
mv ai-venture-studio-template Winners-Circle-WC-Holdings/01-Divisions/Division-4-Technology-AI/AI-Venture-Studio-Template
mv iza-os-rag-system Winners-Circle-WC-Holdings/01-Divisions/Division-4-Technology-AI/IZA-OS-RAG-System

# E-Commerce
mv business-template-marketplace Winners-Circle-WC-Holdings/01-Divisions/Division-5-E-Commerce-Retail/Business-Template-Marketplace

# Operations (Shared Services)
mv venture-hub Winners-Circle-WC-Holdings/03-Venture-Hub-Inc
mv venture-factory-core Winners-Circle-WC-Holdings/02-Shared-Services/Venture-Factory-Core
mv pitch-kit Winners-Circle-WC-Holdings/02-Shared-Services/Pitch-Kit
mv "The office" Winners-Circle-WC-Holdings/02-Shared-Services/The-Office
mv mcp-dashboard Winners-Circle-WC-Holdings/02-Shared-Services/MCP-Dashboard
mv civilization-os-local Winners-Circle-WC-Holdings/02-Shared-Services/Civilization-OS-Local
mv data Winners-Circle-WC-Holdings/02-Shared-Services/Data
mv SecondBrain Winners-Circle-WC-Holdings/02-Shared-Services/SecondBrain

# Archive
mv archive Winners-Circle-WC-Holdings/06-Code-Repositories/Archive

# Delete (keep only .localized)
rm -rf Claude
```

### Phase 3: Create Legal Entity Subfolders (30 minutes)

```bash
# For each active venture, create Legal/Financials/Operations subfolders
cd /Users/acebless/Documents/Winners-Circle-WC-Holdings

# BW-001
mkdir -p "01-Divisions/Division-1-Beauty-Wellness/BW-001-Lash-Extension-Studio/Legal"
mkdir -p "01-Divisions/Division-1-Beauty-Wellness/BW-001-Lash-Extension-Studio/Financials"
mkdir -p "01-Divisions/Division-1-Beauty-Wellness/BW-001-Lash-Extension-Studio/Operations"

# CON-001
mkdir -p "01-Divisions/Division-2-Construction-Logistics/CON-001-Ace-Construction/Legal"
mkdir -p "01-Divisions/Division-2-Construction-Logistics/CON-001-Ace-Construction/Financials"
mkdir -p "01-Divisions/Division-2-Construction-Logistics/CON-001-Ace-Construction/Operations"

# [Repeat for all ventures]
```

### Phase 4: Create Symlinks for Code (Optional, 30 minutes)

```bash
# If you want code accessible from both locations
cd /Users/acebless/Documents/Winners-Circle-WC-Holdings/06-Code-Repositories

# Create symlinks to venture code
ln -s "../01-Divisions/Division-1-Beauty-Wellness/BW-001-Lash-Extension-Studio" bw-001-lash-extension-studio
ln -s "../01-Divisions/Division-2-Construction-Logistics/CON-001-Ace-Construction" con-001-ace-construction
```

---

## 📋 POST-MIGRATION CHECKLIST

### Legal Documentation (Week 1-2):
- [ ] File 7 LLCs with NC Secretary of State
- [ ] Obtain 7 EINs from IRS
- [ ] Create operating agreements for all LLCs
- [ ] Create inter-company service agreements
- [ ] File S-Corp elections (Holdings + operating subs)
- [ ] File C-Corp election (FIN-036)

### Financial Setup (Week 2-3):
- [ ] Open 7 business bank accounts
- [ ] Apply for business credit cards
- [ ] Purchase insurance policies
- [ ] Set up accounting system (QuickBooks)
- [ ] Set up payroll system (Gusto)

### Folder Alignment (Week 3-4):
- [ ] Add Legal/ docs to all 687 venture folders
- [ ] Add Financials/ templates to all venture folders
- [ ] Add Operations/ SOPs to all venture folders
- [ ] Update all README.md files with new paths
- [ ] Update documentation links

---

## 🌐 GITHUB REPO URLs (All 687 Ventures)

### Master List Location:
**File:** `/Users/acebless/Documents/venture-hub/ventures-master.csv`

**Format:**
```csv
venture_id,name,sector,repository_url
FIN-001,Genixbank Lite,financial,https://github.com/Worldwidebro/fin-001-genixbank-lite
BW-001,Lash Extension Studio,beauty-wellness,https://github.com/Worldwidebro/bw-001-lash-extension-studio
CON-001,Ace Construction,construction,https://github.com/Worldwidebro/con-001-ace-construction
```

### GitHub Organization:
**URL:** https://github.com/Worldwidebro

**Access:** All 986 repos are under the `Worldwidebro` GitHub organization

### Browse Repos Online:
1. **Main Org Page:** https://github.com/Worldwidebro?tab=repositories
2. **By Sector:**
   - Financial: https://github.com/orgs/Worldwidebro/repositories?q=fin-
   - Beauty & Wellness: https://github.com/orgs/Worldwidebro/repositories?q=bw-
   - Construction: https://github.com/orgs/Worldwidebro/repositories?q=con-
   - E-Commerce: https://github.com/orgs/Worldwidebro/repositories?q=ec-
   - Technology: https://github.com/orgs/Worldwidebro/repositories?q=tech-
   - Logistics: https://github.com/orgs/Worldwidebro/repositories?q=lt-
   - Operations: https://github.com/orgs/Worldwidebro/repositories?q=ops-

### View Venture Progress:
Each repo contains:
- `README.md` — Project overview
- `SKILL.md` — Capabilities & metadata
- `CLAUDE.md` — Operational guide (for top 10 ventures)
- Source code in `/app/`, `/src/`, or root

---

## 📊 VENTURE STATUS TRACKING

### Active Ventures (Local Folders):

| Venture | Local Path | GitHub | Status | Progress |
|---------|-----------|--------|--------|----------|
| **BW-001** | `Winners-Circle-WC-Holdings/01-Divisions/Division-1-Beauty-Wellness/BW-001-Lash-Extension-Studio/` | [GitHub](https://github.com/Worldwidebro/bw-001-lash-extension-studio) | 🟡 Validation | 65% |
| **CON-001** | `Winners-Circle-WC-Holdings/01-Divisions/Division-2-Construction-Logistics/CON-001-Ace-Construction/` | [GitHub](https://github.com/Worldwidebro/con-001-ace-construction) | 🟡 Validation | 60% |
| **FIN-036** | (Code in venture-hub) | [GitHub](https://github.com/Worldwidebro/fin-036-arbitrage-nexus-platform) | ✅ Active | 95% |
| **Venture Hub** | `Winners-Circle-WC-Holdings/03-Venture-Hub-Inc/venture-hub/` | [GitHub](https://github.com/Worldwidebro/venture-hub) | ✅ Active | 80% |
| **Pitch Kit** | `Winners-Circle-WC-Holdings/02-Shared-Services/Pitch-Kit/pitch-kit/` | [GitHub](https://github.com/Worldwidebro/pitch-kit) | ✅ Deployed | 85% |
| **The Office** | `Winners-Circle-WC-Holdings/02-Shared-Services/The-Office/` | [GitHub](https://github.com/Worldwidebro/the-office) | ✅ Active | 90% |

---

## 🎯 EXECUTION ORDER

### **TODAY (2 hours):**
1. ✅ Run Phase 1 script (create structure)
2. ✅ Run Phase 2 script (move folders)
3. ✅ Run Phase 3 script (create subfolders)
4. ✅ Verify all moves successful

### **THIS WEEK (4 hours):**
1. ⏳ File 7 LLCs ($875)
2. ⏳ Obtain 7 EINs (FREE)
3. ⏳ Open 7 bank accounts (FREE)
4. ⏳ Purchase insurance ($5K-20K/year)

### **NEXT WEEK (8 hours):**
1. ⏳ Create operating agreements
2. ⏳ Create inter-company service agreements
3. ⏳ File S-Corp/C-Corp elections
4. ⏳ Set up accounting/payroll systems

---

## 📞 SUPPORT RESOURCES

### NC Secretary of State:
- Website: www.sosnc.gov
- LLC Filing: $125 per entity
- Expedited: $200 extra (24 hours)

### IRS EIN Application:
- Website: www.irs.gov/ein
- Cost: FREE
- Time: Immediate (online)

### Business Banks:
- Mercury: mercury.com (startup-friendly)
- BlueVine: bluevine.com (high interest)
- Novo: novo.co (FREE, online)
- Bank of America: Local branches

### Business Insurance:
- Hiscox: hiscox.com (general liability)
- Next Insurance: nextinsurance.com (instant quotes)
- Progressive Commercial: progressivecommercial.com (trucks)

---

**Documentation:** `REORGANIZE-VENTURES.md` — This file.

**NEXT:** Run the migration scripts above → File LLCs → Open bank accounts → Revenue. 🚀
