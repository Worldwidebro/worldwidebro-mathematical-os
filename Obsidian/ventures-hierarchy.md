# Ventures Knowledge Graph Dashboard

**Last Updated:** 2026-05-22  
**Total Ventures Indexed:** 618  
**Graph Nodes:** 634 (ventures + tiers + departments + repositories)  
**Graph Edges:** 1477 (relationships)  

---

## 📊 Executive Overview

### Tier Distribution
| Tier | Count | Type | Description |
|------|-------|------|-------------|
| TIER 1 | 19 | **Revenue-Generating** | Operating firms, active revenue streams |
| TIER 2 | 9 | **Dispatch/Broker** | Marketplace intermediaries, referral networks |
| TIER 3 | 43 | **Platform/Hub** | Aggregation platforms, system coordinators |
| TIER 4 | 3 | **Infrastructure** | Core tools, foundational systems |
| TIER 5 | 544 | **Experimental/R&D** | Ideas, pilots, research projects |

**Distribution:** 19 + 9 + 43 + 3 + 544 = **618 ventures**

### Business Model Distribution
| Model | Count | Pattern |
|-------|-------|---------|
| **FIRM** | 19 | Staffing/services (hourly/project dispatch) |
| **BROKER** | 9 | Transaction margin (referral commission) |
| **PLATFORM** | 590 | System-level fees (exponential leverage) |

### Revenue Model Distribution
| Model | Count |
|-------|-------|
| hourly/project | 19 |
| margin | 9 |
| system-fees | 590 |

---

## 🏗️ Department Breakdown

### INTELLIGENCE_LAYER (474 ventures)
Knowledge work, AI/analytics, decision systems
- **Tier 1:** 11 ventures | **Tier 2:** 3 | **Tier 3:** 38 | **Tier 4:** 1 | **Tier 5:** 421

### INFRASTRUCTURE (118 ventures)
Core systems, tools, foundational technology
- **Tier 1:** 5 ventures | **Tier 2:** 4 | **Tier 3:** 4 | **Tier 4:** 2 | **Tier 5:** 103

### REAL_ESTATE (13 ventures)
Property, logistics, location-based services
- **Tier 1:** 0 ventures | **Tier 2:** 1 | **Tier 3:** 0 | **Tier 4:** 0 | **Tier 5:** 12

### STAFFING (3 ventures)
Worker placement, dispatch, employment
- **Tier 1:** 3 ventures | **Tier 2:** 0 | **Tier 3:** 0 | **Tier 4:** 0 | **Tier 5:** 0

### LOGISTICS (6 ventures)
Distribution, delivery, supply chain
- **Tier 1:** 1 venture | **Tier 2:** 0 | **Tier 3:** 0 | **Tier 4:** 0 | **Tier 5:** 5

### TEMPLATES (3 ventures)
Reusable patterns, frameworks
- **Tier 1:** 0 ventures | **Tier 2:** 0 | **Tier 3:** 0 | **Tier 4:** 0 | **Tier 5:** 3

### R&D (1 venture)
Pure research, exploratory
- **Tier 1:** 0 ventures | **Tier 2:** 0 | **Tier 3:** 0 | **Tier 4:** 0 | **Tier 5:** 1

---

## 🔗 Tier Dependency Architecture

### TIER 1 → TIER 2 Dependencies
Revenue-generating firms depend on dispatch/broker intermediaries
- **Pattern:** TIER 1 FIRM ventures require TIER 2 BROKER matching services
- **Example:** Credit Repair Automation (TIER 1) → depends on TIER 2 dispatch via mission-control

### TIER 1/2 → TIER 3 Dependencies
Operating tiers depend on platform coordination
- **Pattern:** TIER 1/2 ventures connect through TIER 3 platforms
- **Example:** Staffing dispatch → aggregates to Niche Mastery OS (TIER 3)

### All Tiers → TIER 4 Dependencies
Infrastructure provides foundational technology
- **Pattern:** All ventures accessing knowledge graph, authentication, payment require TIER 4 tools
- **Repositories:** LightRAG, opensre, mission-control, thunderbolt

### TIER 5 Cascade Planning
Experimental ventures can promote to TIER 1-3 via successful validation
- **Promotion Path:** TIER 5 idea → TIER 4 infrastructure acquired → TIER 3 platform adoption → TIER 2 broker integration → TIER 1 revenue generation

---

## 📁 Repository Requirements

### Primary Repos
- **LightRAG** - Knowledge graph, semantic search, database backbone
- **opensre** - Search, retrieval, inference infrastructure
- **mission-control** - Task dispatch, matching, orchestration
- **thunderbolt** - Real-time coordination, websockets

### Dependencies by Control Type
| Control Type | Primary Repos | Secondary |
|--------------|---------------|-----------|
| FIRM | mission-control, opensre | authentication, payment, security |
| BROKER | LightRAG, thunderbolt | api, matching, dashboard |
| PLATFORM | LightRAG, opensre | knowledge-graph, semantic-search, database |

---

## 🚀 Next Steps

### Knowledge Graph Integration
1. **Agent Routing** - Match venture needs to repo capabilities via graph traversal
2. **Cascade Planning** - Changes to TIER 1/2 automatically re-evaluate TIER 3/4/5 dependencies
3. **Capability Matching** - Graph queries find ventures requiring [repo1, repo2, repo3]
4. **Dependency Resolution** - Detect missing infrastructure or circular dependencies

### Sync Status
- ✅ Classification CSV: 618 ventures complete
- ✅ Dependencies JSON: Tier interconnections mapped
- ✅ Knowledge Graph JSON: 634 nodes, 1477 edges
- 🔄 Supabase Sync: Ready to execute (update_ventures_classification.sql)

---

## 📈 Key Metrics

**Concentration by Tier:**
- Top tier (TIER 1): 3.1% (19 ventures)
- Operating (TIER 1-2): 4.5% (28 ventures)
- Platforms (TIER 3): 7.0% (43 ventures)
- Infrastructure (TIER 4): 0.5% (3 ventures)
- Experimental (TIER 5): 88.0% (544 ventures)

**Concentration by Department:**
- Intelligence Layer: 76.7% (474 ventures)
- Infrastructure: 19.1% (118 ventures)
- Real Estate: 2.1% (13 ventures)
- Staffing: 0.5% (3 ventures)
- Other: 1.6% (10 ventures)

**Control Diversity:**
- FIRM model: 19 ventures (hourly/project margin)
- BROKER model: 9 ventures (transaction margin)
- PLATFORM model: 590 ventures (exponential system fees)

---

## 🔍 Example Dependency Chains

### Tax Intelligence Platform (TIER 3)
```
Tax Intelligence Platform (TIER 3, INTELLIGENCE_LAYER, PLATFORM)
├─ Depends on: TIER 4 infrastructure
├─ Requires: LightRAG, opensre
└─ Serves: TIER 1 fintech operations
```

### Credit Repair Automation (TIER 1)
```
Credit Repair Automation (TIER 1, INTELLIGENCE_LAYER, FIRM)
├─ Depends on: TIER 2 dispatch, TIER 4 infrastructure
├─ Requires: mission-control, opensre
└─ Margin model: $8-30/hr (worker cost $15-25, client bill $35-50)
```

### U Haul Rental Affiliate (TIER 2)
```
U Haul Rental Affiliate (TIER 2, REAL_ESTATE, BROKER)
├─ Depends on: TIER 3, TIER 4
├─ Requires: LightRAG, thunderbolt
└─ Revenue model: Transaction margin on referrals
```

---

## 🎯 Knowledge Graph Queries

### Find all ventures in a tier:
```
TIER_N → venture nodes (all incoming "belongs_to_tier" edges)
```

### Find venture dependencies:
```
venture_id → depends_on_tier edges → dependent TIER → upstream ventures
```

### Find repository impact:
```
REPO_name ← requires_repo edges ← venture nodes (which ventures need this repo)
```

### Cascade analysis:
```
Change to venture X → depends_on_tier chain → find all affected downstream ventures
```

---

**Knowledge Graph Status:** LIVE  
**Last Graph Build:** 2026-05-22 13:29:40  
**Graph Engine:** Unified OS (data → graph → agents → execution)
