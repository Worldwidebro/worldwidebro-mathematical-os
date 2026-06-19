# HVAC Operations Directives

Executable playbooks for ops-venture-001-hvac. Synced from `01_CEO_COMMAND_CENTER/Goals/HVAC_MRR_Target.md`.

## Lead Enrichment
**Trigger**: Daily 6am | **Owner**: Lead Enrichment Agent | **Goal**: 20+ qualified leads/week

- Scrape Google Maps for HVAC calls in service area
- Enrich with Apify competitor data (pricing, reviews, availability)
- Score leads (0-100) based on service history, property value, budget indicators
- Add to `/10_VENTURES/Operations_Ventures/ops-venture-001-hvac/Leads/qualified_leads.json`
- Alert scheduler if score > 80

**Workflow**: `n8n/lead-enrichment-hvac.json`

## Quote Generation
**Trigger**: On lead score > 70 | **Owner**: Quote Generation Agent | **Goal**: 5+ quotes/day

- Pull lead details from Leads folder
- Match to equipment type (furnace, AC, ductless, heat pump)
- Load pricing rules from `/04_EQUIPMENT_INTELLIGENCE/HVAC/pricing_rules.json`
- Generate estimate using labor rates + material costs
- Save to `/10_VENTURES/Operations_Ventures/ops-venture-001-hvac/Quotes/estimates.json`
- Notify sales team in Slack #hvac-operations

**Workflow**: `n8n/quote-generation-hvac.json`

## Equipment Intelligence Sync
**Trigger**: Daily 8am | **Owner**: Equipment Sync Agent | **Goal**: Real-time pricing accuracy

- Pull latest HVAC equipment pricing from Apify scrapers
- Update cost basis for furnaces, ACs, heat pumps, ductless systems
- Recalculate quote ROI margins
- Sync to `/04_EQUIPMENT_INTELLIGENCE/HVAC/pricing_rules.json`

**Workflow**: `Apify/hvac-pricing-monitor.json`

## Metrics Aggregation
**Trigger**: Daily 9am | **Owner**: Metrics Agent | **Goal**: Real-time dashboard accuracy

- Count leads by source (Google Maps, referral, web)
- Sum quotes generated, value, conversion rate
- Pull revenue from Finance (invoices paid)
- Update `/10_VENTURES/Operations_Ventures/ops-venture-001-hvac/metrics.json`
- Compare vs. target in `01_CEO_COMMAND_CENTER/Goals/HVAC_MRR_Target.md`

**Workflow**: `n8n/metrics-aggregation.json`

---

**Back to**: `07_AUTOMATIONS/VENTURE_DIRECTIVES_MAP.md`
**Synced from**: `01_CEO_COMMAND_CENTER/Goals/HVAC_MRR_Target.md`
