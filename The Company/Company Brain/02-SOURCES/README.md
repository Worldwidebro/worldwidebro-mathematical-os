# 02-SOURCES — Data Sources & MCPs

**Feeds into:** [[01-IDENTITY]] → [[00-CONSTITUTION/SECTOR-TAXONOMY-MASTER]]

---

## Overview

Internal & external data sources, APIs, databases, repositories that feed into entity resolution and sector taxonomy.

## Data Flow

```
MCPs & APIs (ClickUp, HubSpot, Gmail, Slack, etc.)
    ↓
Data Ingestion (03-INGESTION)
    ↓
Entity Resolution (06-ENTITY-RESOLUTION)
    ↓
Identity Registry (01-IDENTITY)
    ↓
Sector Taxonomy (00-CONSTITUTION)
    ↓
Agent Routing (16-AGENTS)
    ↓
People & Teams (52-PEOPLE)
```

## Connected Domains

- [[01-IDENTITY]] → downstream (identity registry)
- [[03-INGESTION]] → data processing
- [[06-ENTITY-RESOLUTION]] → deduplication
- [[16-AGENTS]] → routing agents
- [[52-PEOPLE]] → people management

## Status

🟡 In progress | Connected to identity flow

---

Last updated: 2026-09-02
