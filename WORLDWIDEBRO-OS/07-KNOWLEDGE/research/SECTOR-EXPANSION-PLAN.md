# 16-Sector Expansion & Alignment Plan

**Status**: Phase 1.2 Network Mapping Extension  
**Timeline**: May 15-31, 2026  
**Scope**: Extend Worldwidebro Holdings from 7 → 16 sector taxonomy

---

## EXECUTIVE SUMMARY

### Current State (7 Sectors)
- **Total Unique Ventures**: 372 (from 583 with 211 duplicates)
- **Supabase Classification**: 7 sectors
- **Obsidian Notes**: 7 sector files created
- **CSV Status**: ventures_updated_2026-05-15.csv (7 sectors)

### New State (16 Sectors)
- **372 Ventures Reclassified** to 16-sector taxonomy
- **Portfolio Composition**:
  - Software-Tech: 189 (50.8%) — CRITICAL MASS
  - E-Commerce: 38 (10.2%) — CRITICAL
  - Education: 32 (8.6%) — HIGH
  - Operations: 24 (6.5%) — HIGH
  - Community: 23 (6.2%) — HIGH
  - Technology: 19 (5.1%) — HIGH
  - All Others: 47 (12.6%) — MEDIUM/LOW

### Key Insight
**Software-Tech sector dominates** with over 50% of portfolio (189 ventures). This is primarily "Ai ___" ventures that are fundamentally software/automation tools. E-Commerce comes second with 38 ventures.

---

## 16-SECTOR TAXONOMY

| # | Sector | Count | % | Strategic Priority |
|---|--------|-------|---|-------------------|
| 1 | Software-Tech | 189 | 50.8% | 🔴 CRITICAL |
| 2 | E-Commerce | 38 | 10.2% | 🔴 CRITICAL |
| 3 | Education | 32 | 8.6% | 🟡 HIGH |
| 4 | Operations | 24 | 6.5% | 🟡 HIGH |
| 5 | Community | 23 | 6.2% | 🟡 HIGH |
| 6 | Technology | 19 | 5.1% | 🟡 HIGH |
| 7 | Financial | 14 | 3.8% | 🟡 MEDIUM |
| 8 | Beauty-Wellness | 10 | 2.7% | 🟢 LOW |
| 9 | Logistics | 6 | 1.6% | 🟡 MEDIUM |
| 10 | Media-Content | 5 | 1.3% | 🟢 LOW |
| 11 | Professional-Services | 4 | 1.1% | 🟡 MEDIUM |
| 12 | Fitness-Sports | 3 | 0.8% | 🟢 LOW |
| 13 | Construction | 2 | 0.5% | 🟢 LOW |
| 14 | Food-Hospitality | 1 | 0.3% | 🟢 LOW |
| 15 | Specialized | 1 | 0.3% | 🟢 LOW |
| 16 | Emerging | 1 | 0.3% | 🟢 LOW |
| **TOTAL** | | **372** | **100%** | |

---

## 7-TO-16 SECTOR MAPPING

### Fintech (47 ventures) → Financial (14) + Professional-Services (4) + Beauty-Wellness (2) + Construction (1) + Operations (21)
- **Primary**: Financial (14) — tax, payments, banking, insurance, crypto, wealth
- **Secondary**: Operations (21) — forecasting, budgeting, planning, management
- **Tertiary**: Professional-Services (4) — business formation, recruitment, consulting
- **Gap**: 8 ventures shifted to other sectors (construction building, beauty wellness, etc.)

### AI (72 ventures) → Software-Tech (55) + Technology (19)
- **Primary**: Software-Tech (55) — automation, algorithms, tools, platforms
- **Secondary**: Technology (19) — innovation, analytics, monitoring, data
- **Alignment**: 100% — AI ventures naturally map to Software-Tech/Technology

### EdTech (69 ventures) → Education (32) + Community (23) + Operations (5) + Professional-Services (3) + Media-Content (2) + Financial (2) + Emerging (1) + Specialized (1)
- **Primary**: Education (32) — training, learning, courses, tutoring, schools
- **Secondary**: Community (23) — incubators, networks, coaching, groups
- **Tertiary**: Operations (5) — planning, forecasting, management
- **Observation**: EdTech ventures spread across 8 sectors — reflects diverse business models

### Health (1 venture) → Fitness-Sports (1)
- **VitalSense** → Fitness-Sports (wearable health monitoring)

### Infrastructure (109 ventures) → Software-Tech (54) + Operations (22) + Technology (12) + Media-Content (5) + Professional-Services (4) + Logistics (5) + Community (2) + Financial (3) + E-Commerce (2)
- **Primary**: Software-Tech (54) — platforms, tools, integration, databases
- **Secondary**: Operations (22) — management, resource allocation, forecasting
- **Tertiary**: Technology (12) — monitoring, analytics, cyber, automation
- **Spread**: Infrastructure ventures distributed across 9 sectors — reflects broad application

### Marketplace (194 ventures) → E-Commerce (38) + Software-Tech (64) + Operations (24) + Community (19) + Logistics (6) + Education (8) + Professional-Services (4) + Financial (8) + Technology (4) + Fitness-Sports (3) + Beauty-Wellness (3) + Media-Content (3) + Specialized (1) + Food-Hospitality (1) + Emerging (1) + Construction (1)
- **Primary**: Software-Tech (64) — product tools, matching, automation, optimization
- **Secondary**: E-Commerce (38) — retail, shopping, inventory, marketplace platforms
- **Tertiary**: Operations (24) — logistics planning, forecasting, management
- **Spread**: Marketplace is most diverse — 16-sector portfolio reflects "anything with Ai ___" nature

### DevTools (91 ventures) → Software-Tech (79) + Technology (12)
- **Primary**: Software-Tech (79) — developer tools, APIs, integration, automation
- **Secondary**: Technology (12) — monitoring, analytics, data, cyber
- **Alignment**: 100% — DevTools naturally map to Software-Tech/Technology

---

## FILES CREATED/UPDATED

✅ **ventures_16sector_classification.csv**
- Path: `/Users/acebless/ventures_16sector_classification.csv`
- Columns: ID, Name, Description, Sector_7, Sector_16, Status
- Rows: 372 unique ventures
- Use: Single source of truth for venture classifications

✅ **ventures_sector_alignment_matrix.csv**
- Path: `/Users/acebless/ventures_sector_alignment_matrix.csv`
- Shows: Count, %, top ventures, strategic priority per sector
- Use: Quick reference for sector sizing and priorities

---

## ALIGNMENT WORK REQUIRED

### PHASE A: Supabase Schema Extension (Priority: CRITICAL)

**Action 1**: Add `sector_16` column to ventures table
```sql
ALTER TABLE ventures ADD COLUMN sector_16 VARCHAR(50);
```

**Action 2**: Bulk update sector_16 values from classification CSV
- Use CSV import or batch SQL update
- Map ventures by ID to new sector_16 values

**Action 3**: Validate data integrity
- Verify all 583 ventures (372 unique × 1-2 duplicates) have sector_16 assigned
- Check for NULL values

**Action 4**: Create relationships view
```sql
SELECT sector_16, COUNT(*) as venture_count, ARRAY_AGG(name) as ventures
FROM ventures
GROUP BY sector_16
ORDER BY venture_count DESC;
```

---

### PHASE B: Obsidian Vault Extension (Priority: HIGH)

**Action 1**: Create 16 sector notes in `permanent/`
```
permanent/
├── 02-Fintech-Sector.md (update: split Financial + operations context)
├── 02a-Financial-Sector.md (new)
├── 03-AI-Sector.md (update: Software-Tech + Technology context)
├── 03a-Software-Tech-Sector.md (new: 189 ventures)
├── 03b-Technology-Sector.md (new: 19 ventures)
├── 04-EdTech-Sector.md (keep + cross-link Community/Operations)
├── 04a-Community-Sector.md (new: 23 ventures)
├── 04b-Operations-Sector.md (new: 24 ventures)
├── 05-Healthcare-Sector.md (update → Fitness-Sports)
├── 05a-Beauty-Wellness-Sector.md (new: 10 ventures)
├── 06-Infrastructure-Sector.md (deprecate, archive)
├── 06a-Logistics-Sector.md (new: 6 ventures)
├── 07-Marketplace-Sector.md (update: reference E-Commerce context)
├── 07a-E-Commerce-Sector.md (new: 38 ventures)
├── 08-DevTools-Sector.md (update: reference Software-Tech)
├── 09-Media-Content-Sector.md (new: 5 ventures)
├── 10-Professional-Services-Sector.md (new: 4 ventures)
├── 11-Food-Hospitality-Sector.md (new: 1 venture)
├── 12-Specialized-Sector.md (new: 1 venture)
├── 13-Emerging-Sector.md (new: 1 venture)
└── 10-Network-Map.md (update: reference 16-sector contacts)
```

**Action 2**: Update master index
- Edit `permanent/01-Sectors.md` to show 16 sectors
- Add navigation links to all 16 sector notes

**Action 3**: Update knowledge graph
- Regenerate `graphify/graph.json` with 16 sector nodes
- Preserve existing venture nodes (372)
- Add new sector-to-sector relationships

---

### PHASE C: CSV Extension (Priority: HIGH)

**Action 1**: Create sector-specific contact lists
```
sectors/
├── fintech-contacts.csv (from Financial + Professional-Services ventures)
├── software-tech-contacts.csv (from 189 ventures)
├── ecommerce-contacts.csv (from 38 ventures)
├── education-contacts.csv (from 32 ventures)
├── operations-contacts.csv (from 24 ventures)
├── community-contacts.csv (from 23 ventures)
├── technology-contacts.csv (from 19 ventures)
└── ... (10 more sector files)
```

**Action 2**: Create sector priority triage CSVs
- Week 1 Focus: Software-Tech + E-Commerce + Education (top 259 ventures)
- Week 2 Expansion: Operations + Community + Technology (70 more)
- Week 3 Backlog: All remaining sectors (43 ventures)

---

### PHASE D: Agent Integration (Priority: MEDIUM)

**Action 1**: Update Claude Code skills
- Create 16 sector-specific skills (one per sector)
- Map venture spin-up to sector GTM strategies
- Update agent routing to sector handlers

**Action 2**: Update Paperclip agent configs
- Assign sector ownership (which agents manage which sectors)
- Configure automation per sector (high-touch vs. batch)

---

### PHASE E: ClickUp Automation (Priority: MEDIUM)

**Action 1**: Create 16 ClickUp projects (one per sector)
- Project naming: `[SECTOR] - Phase 1.2 Network Mapping`
- Tags: sector_16, network-mapping, phase-1.2

**Action 2**: Bulk import ventures to projects
- Group by sector_16
- Create task per venture: "Extract contacts from [VENTURE_NAME]"

---

## GTM STRATEGY BY SECTOR

### 🔴 CRITICAL (Software-Tech, E-Commerce)

**Software-Tech (189 ventures)**
- **Focus**: Developer-first outreach (GitHub, Twitter, HackerNews)
- **Primary Contact**: Founders, CTO, Lead Engineers
- **Timeline**: Week 1-2 extraction, Week 3-4 sequencing
- **Target**: 300+ technical founders, 50+ investors
- **GTM Channel**: Dev community, open source, GitHub sponsorships

**E-Commerce (38 ventures)**
- **Focus**: Merchant/marketplace operator outreach
- **Primary Contact**: Founders, VP Marketing, Operations Leads
- **Timeline**: Week 1-2 extraction, Week 2-3 sequencing
- **Target**: 80+ merchants, 20+ retail investors
- **GTM Channel**: Shopify ecosystem, marketplace platforms, retail networks

### 🟡 HIGH (Education, Operations, Community, Technology)

**Education (32 ventures)**
- **Focus**: EdTech founders, course creators, school admins
- **Primary Contact**: Founders, Head of Product, Curriculum Directors
- **Timeline**: Week 2 extraction
- **Target**: 100+ education leaders, 15+ EdTech investors
- **GTM Channel**: Teacher networks, education conferences, LinkedIn

**Operations (24 ventures)**
- **Focus**: Operations professionals, workflow automation buyers
- **Primary Contact**: COOs, Operations Managers, Process Owners
- **Timeline**: Week 2-3 extraction
- **Target**: 80+ enterprise ops, 10+ operations-focused VCs
- **GTM Channel**: LinkedIn, enterprise software, process automation communities

**Community (23 ventures)**
- **Focus**: Community builders, network facilitators, incubators
- **Primary Contact**: Community Managers, Coaches, Network Leads
- **Timeline**: Week 2-3 extraction
- **Target**: 100+ community leaders, 5+ community-focused investors
- **GTM Channel**: Slack communities, Discord, community management platforms

**Technology (19 ventures)**
- **Focus**: Tech innovation, analytics, data, cyber
- **Primary Contact**: CTOs, Data Leaders, Security Heads
- **Timeline**: Week 3 extraction
- **Target**: 60+ tech leaders, 10+ tech-focused investors
- **GTM Channel**: Tech conferences, data communities, cyber summits

### 🟡 MEDIUM (Financial, Logistics, Professional-Services)

**Financial (14 ventures)**
- **Focus**: Finance/fintech buyers and investors
- **Target**: 50+ financial services leaders, 5+ fintech VCs
- **Timeline**: Week 2-3
- **GTM Channel**: Fintech events, finance networks

**Logistics (6 ventures)**
- **Focus**: Supply chain, logistics operators
- **Target**: 30+ logistics leaders, 2+ logistics investors
- **Timeline**: Week 3
- **GTM Channel**: Logistics associations, supply chain forums

**Professional-Services (4 ventures)**
- **Focus**: Consulting, legal, recruiting sectors
- **Target**: 20+ professional service leaders, 1-2 investors
- **Timeline**: Week 3
- **GTM Channel**: Professional networks, service marketplaces

### 🟢 LOW (Beauty-Wellness, Media-Content, Fitness-Sports, Construction, Food-Hospitality, Specialized, Emerging)

**These 16 ventures** combined (3.3% of portfolio)
- **Focus**: Emerging/niche segments
- **Target**: 50+ founders, 2-3 specialist investors
- **Timeline**: Week 3-4 backlog
- **GTM Channel**: Niche communities, industry associations

---

## SUCCESS METRICS (Phase 1.2)

### By End of Week 1 (May 21)
- ✅ Supabase schema updated with sector_16
- ✅ 16 Obsidian sector notes created
- ✅ Knowledge graph regenerated (16 sector nodes)
- ✅ Contact extraction started on CRITICAL sectors (227 ventures)
- ✅ Target: 150+ warm contacts identified

### By End of Week 2 (May 28)
- ✅ Contact extraction complete on HIGH priority sectors (94 ventures)
- ✅ Sector-specific contact lists created (7 files)
- ✅ Contact priority matrix built (Tier 1-3 mapping)
- ✅ ClickUp projects created (16 sector projects)
- ✅ Target: 350+ qualified contacts extracted

### By End of Week 3 (May 31)
- ✅ All 372 ventures have contact extraction started
- ✅ Outreach sequences drafted per sector
- ✅ Phase 1.3 (Social Media Audit) prep complete
- ✅ Q2 execution roadmap ready
- ✅ Target: 500+ leads triaged and prioritized

---

## RISKS & MITIGATION

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Software-Tech (189) dominates portfolio | May miss niche sectors | Focus CRITICAL on software + E-commerce, backlog others |
| Contact extraction from 372 ventures | Manual work could take 40+ hours | Use Supabase SQL + Python scripts to automate 70% |
| Supabase schema change mid-execution | May break existing queries | Create sector_16 as new column, keep sector_7 intact |
| Obsidian vault performance (from 8 → 16 sector notes) | Search/graph may slow | Archive old sector notes, rebuild graph with Dataview |
| Duplicate ventures (211 still in data) | May extract same contact twice | Deduplicate before contact extraction (consolidate to 372 unique) |

---

## NEXT IMMEDIATE ACTIONS (Today)

1. **Update Supabase**: Add sector_16 column and bulk populate
2. **Create Obsidian Notes**: First 5 CRITICAL sector files (Software-Tech, E-Commerce, Education, Operations, Community)
3. **Regenerate Graph**: Update graphify/graph.json with 16 sector nodes
4. **Start Contact Extraction**: Begin on Software-Tech (189 ventures) using ventures_16sector_classification.csv
5. **Create ClickUp Projects**: Set up 16 sector-specific projects in ClickUp

---

## DELIVERABLES

📊 **CSVs**
- ventures_16sector_classification.csv ✅
- ventures_sector_alignment_matrix.csv ✅
- sector-specific contact lists (pending extraction)
- sector priority triage (pending prioritization)

📝 **Obsidian**
- 16 sector notes (pending creation)
- Updated 01-Sectors.md master index (pending update)
- Updated knowledge graph (pending regeneration)

🔧 **Tools**
- ClickUp: 16 sector projects (pending creation)
- Supabase: sector_16 column + bulk update (pending execution)
- Claude Code: 16 sector skills (pending generation)

---

**Status**: Ready for execution  
**Owner**: Phase 1.2 Network Mapping Team  
**Timeline**: May 15-31, 2026
