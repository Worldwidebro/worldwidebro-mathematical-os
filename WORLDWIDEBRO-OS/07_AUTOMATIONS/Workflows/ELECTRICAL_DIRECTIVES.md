# Electrical Operations Directives

Executable playbooks for ops-venture-002-electrical. Synced from `01_CEO_COMMAND_CENTER/Goals/ELECTRICAL_MRR_Target.md`.

## Lead Enrichment
**Trigger**: Daily 6am | **Owner**: Lead Enrichment Agent | **Goal**: 20+ qualified leads/week

- Scrape Google Maps for electrical service calls in service area
- Enrich with Apify competitor data (pricing, reviews, availability)
- Score leads (0-100) based on property type (residential/commercial), panel age, service history
- Add to `/10_VENTURES/Operations_Ventures/ops-venture-002-electrical/Leads/qualified_leads.json`
- Alert scheduler if score > 80

**Workflow**: `n8n/lead-enrichment-electrical.json`

## Quote Generation
**Trigger**: On lead score > 70 | **Owner**: Quote Generation Agent | **Goal**: 5+ quotes/day

- Pull lead details from Leads folder
- Match to service type (panel upgrade, new circuit, troubleshooting, rewire, inspection)
- Load pricing rules from `/04_EQUIPMENT_INTELLIGENCE/Electrical/pricing_rules.json`
- Generate estimate using labor rates + material costs
- Save to `/10_VENTURES/Operations_Ventures/ops-venture-002-electrical/Quotes/estimates.json`
- Notify sales team in Slack #electrical-operations

**Workflow**: `n8n/quote-generation-electrical.json`

## Equipment Intelligence Sync
**Trigger**: Daily 8am | **Owner**: Equipment Sync Agent | **Goal**: Real-time pricing accuracy

- Pull latest electrical material pricing from Apify scrapers (panels, breakers, wire, labor)
- Update cost basis for common service types
- Recalculate quote ROI margins
- Sync to `/04_EQUIPMENT_INTELLIGENCE/Electrical/pricing_rules.json`

**Workflow**: `Apify/electrical-pricing-monitor.json`

## Metrics Aggregation
**Trigger**: Daily 9am | **Owner**: Metrics Agent | **Goal**: Real-time dashboard accuracy

- Count leads by source (Google Maps, referral, web)
- Sum quotes generated, value, conversion rate
- Pull revenue from Finance (invoices paid)
- Update `/10_VENTURES/Operations_Ventures/ops-venture-002-electrical/metrics.json`
- Compare vs. target in `01_CEO_COMMAND_CENTER/Goals/ELECTRICAL_MRR_Target.md`

**Workflow**: `n8n/metrics-aggregation.json`

---

**Back to**: `07_AUTOMEROS/VENTURE_DIRECTIVES_MAP.md`
**Synced from**: `01_CEO_COMMAND_CENTER/Goals/ELECTRICAL_MRR_Target.md`
