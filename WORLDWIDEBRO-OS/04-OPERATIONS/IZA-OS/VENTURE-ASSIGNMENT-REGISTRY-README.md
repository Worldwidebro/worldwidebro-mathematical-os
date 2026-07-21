# VENTURE ASSIGNMENT REGISTRY

**Purpose**: Complete routing table mapping all 712 ventures to OPCOs, departments, and assigned agents. Source of truth for venture→capability→department→agent resolution.

**Location**: `/WORLDWIDEBRO-OS/04-OPERATIONS/IZA-OS/ventures/VENTURE-ASSIGNMENT-REGISTRY.yaml`

## Overview

- **712 ventures** mapped to **18 OPCOs**
- **8 departments** (finance, technology, marketing, operations, sales, legal, hr, compliance)
- **Capability routing**: Each venture declares required capabilities → departments → assigned agents
- **Readiness scoring**: 0-100 scale based on stage (planned:15 → live:85)
- **Revenue targets**: Monthly targets per growth stage

## OPCO Distribution

| OPCO | Count | Category |
|------|-------|----------|
| ec (Marketplace) | 110 | Digital Marketplaces |
| ops (Operations) | 67 | Business Operations |
| tech (Technology) | 61 | Technology & Software |
| comm (Communications) | 50 | Media & Communications |
| em (Energy) | 50 | Business Operations |
| spec (Specialized) | 50 | Specialized Services |
| bw (Beauty-Wellness) | 40 | Beauty & Wellness |
| edu (Education) | 40 | Education & Learning |
| fin (Financial) | 36 | Financial Services |
| fh (Healthcare) | 35 | Healthcare Delivery |
| lt (Legal Tech) | 30 | Technology & Software |
| st (Staffing) | 30 | Staffing & Talent |
| con (Construction) | 20 | Construction & Infrastructure |
| mc (Media) | 20 | Media & Communications |
| et (Transportation) | 16 | Transportation & Logistics |
| ps (Professional Services) | 25 | Staffing & Talent |
| fs (Retail Finance) | 25 | Retail & Consumer |
| fi (Financial Instruments) | 5 | Financial Services |
| re (Real Estate) | 1 | Real Estate & Property |
| profile | 1 | Miscellaneous |

## Registry Structure

```yaml
ventures:
  VENTURE-ID:
    name: string                          # Venture name
    opco: string                          # OPCO assignment (fin, tech, ops, etc.)
    sector: string                        # Business sector
    stage: string                         # Development stage (planned|development|alpha|beta|mvp|validation|growth|active|live|archived)
    status: string                        # Current status
    
    required_capabilities:
      finance: [analytics, payments, portfolio]
      technology: [api, authentication, dashboard, database, security]
      marketing: [notifications, crm]
      operations: [automation, scheduling]
      sales: [crm]
    
    assigned_agents:
      finance: fin_{opco}_fin_001         # Department → Agent ID
      technology: tech_{opco}_tech_001
      marketing: mktg_{opco}_mktg_001
      operations: ops_{opco}_ops_001
      sales: sales_{opco}_sales_001
    
    launch_date: 2026-01-01              # Planned launch
    readiness_score: 55                  # 0-100 scale
    revenue_target_monthly: 5000         # Monthly revenue target
    growth_stage: validation             # Current growth phase
    capability_coverage: 75.0            # % of required capabilities implemented
```

## Agent Naming Convention

Agent IDs follow the pattern: `{dept_code}_{opco}_{dept_code}_{instance}`

- `fin_tech_fin_001` = Finance department, Technology OPCO, Finance agent, instance 1
- `mktg_ec_mktg_001` = Marketing department, E-Commerce OPCO, Marketing agent, instance 1

## Usage Examples

### 1. Route a Venture Request
When venture BW-001 needs "payment processing":
1. Look up BW-001 in registry
2. Find "payments" in required_capabilities → belongs to "finance"
3. Get assigned agent: `fin_bw_fin_001`
4. Route request to finance agent

### 2. Find All Ventures by OPCO
```yaml
opco: fin  # All 36 financial ventures
```

### 3. Stage-Based Filtering
```yaml
stage: live        # 85/100 readiness
stage: validation  # 55/100 readiness
stage: planned     # 15/100 readiness
```

### 4. Department Capacity Planning
Count all ventures requiring "technology":
- Find all ventures with technology in `required_capabilities`
- Sum across all OPCOs
- Allocate tech agents accordingly

## Integration Points

- **Supabase**: Load ventures, opco_venture_map, venture_skill_roadmap tables
- **Neo4j**: Create Venture→OPCO→Department→Agent graph relationships
- **Grafana**: Dashboard filtered by OPCO, stage, readiness_score
- **N8n**: Workflow routing based on venture OPCO + required capability

## Stats

- **Total ventures**: 712
- **Planned/Development**: 355 ventures (50%)
- **Active/Live**: 165 ventures (23%)
- **Avg readiness**: 27.7/100
- **Coverage**: 1,046/1,639 repos have populated capabilities

## Last Updated
2026-07-16

## Source
- VENTURES-CAPABILITIES-MAPPED.csv (canonical venture registry)
- OPCO_VENTURE_MAPPING.csv (OPCO → ventures mapping)
