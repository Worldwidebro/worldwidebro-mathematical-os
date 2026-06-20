# Campaign Factory

**Multi-agent orchestrated marketing campaigns at scale across 712 ventures**

Agent-driven 12-stage campaign pipeline: Research → Positioning → Design → Creative → Social → Email → Analytics.

## Structure

```
campaign-factory/
├── automations/               # Orchestration engine
│   └── campaign_orchestrator.py
├── registries/                # Configuration & templates
│   ├── campaign-registry.json
│   └── campaign-ventures-template.csv
├── schema/                    # Database schema
│   └── campaign-supabase-schema.sql
├── dashboards/                # Real-time visibility
│   └── CAMPAIGN-FACTORY-DASHBOARD.md
├── CAMPAIGN-FACTORY-INTEGRATION-GUIDE.md
└── README.md (this file)
```

## Quick Start

### 1. Deploy Schema
```bash
psql postgresql://... < schema/campaign-supabase-schema.sql
```

### 2. Launch Campaign
```bash
python3 automations/campaign_orchestrator.py \
  --venture v-hrms-001 \
  --template tmpl-service-launch \
  --name "HRMS MVP Launch" \
  --budget 3000
```

### 3. Monitor
Open `dashboards/CAMPAIGN-FACTORY-DASHBOARD.md` in Obsidian for live metrics.

## Components

### campaign_orchestrator.py
Coordinates 12-stage agent execution with quality tracking.

### campaign-registry.json
- 4 campaign templates
- 12 stage configurations
- 5 channel configs
- 7 agent definitions

### campaign-supabase-schema.sql
5 new tables for campaigns, stages, content, channels, metrics.

### CAMPAIGN-FACTORY-DASHBOARD.md
Obsidian dashboard with live campaign visibility.

## Status

✅ **Production Ready**

---

**Created**: 2026-06-08 · **Ventures**: 712 · **Agents**: 7 · **Stages**: 12
