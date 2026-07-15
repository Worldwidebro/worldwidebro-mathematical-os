# Context (from DOCs)

Running notes by topic, appended verbatim (condensed) with source attribution. 6 DOC-type sources in this batch.

---

## Topic: System-Wide Navigation Entry Point
- **source:** `/Users/acebless/Documents/MASTER-INDEX.md` ("Worldwidebro Holdings Master Index", 2026-06-19, precedence 0)
- Positioned as the broad, current, system-wide entry point ("START HERE"). Organizes the system into 4 Orbs: STRATEGY (planning/vision), INFRASTRUCTURE (tech stack/deployment), VENTURES (execution/tracking), REFERENCE (knowledge/learning) — each links to the other 3, looping STRATEGY→INFRASTRUCTURE→VENTURES→REFERENCE→STRATEGY.
- Quick stats asserted here: 712 ventures in pipeline, 1,595 repos classified by capability, 44 agent commands (obsidian-second-brain), 296 total slash commands, 4 capital layers, 31 sectors mapped, daily automation at 6 AM.
- Explicitly cross-references the CEO Command Center Sales/Ops Index (see below) as a narrower, older (2026-05-10), tactical sibling doc — not a competing master index.

## Topic: CEO Command Center Sales/Ops Tooling
- **source:** `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/STRATEGY_LAYERS/WORLDWIDEBRO-OS/01_CEO_COMMAND_CENTER/Indexes/CEO-COMMAND-CENTER-SALES-OPS-INDEX.md` (renamed 2026-07-03 from `MASTER-INDEX.md`; dated content 2026-05-10, "Phase 0"; precedence 3)
- Tactical index scoped to CEO Command Center sales/ops tooling: ClickUp setup/pipeline, deal scripts by sector, VAPI AI-calling architecture, OSINT contact enrichment, OpenVolo CRM integration, vendor procurement, starred-repo install priority.
- Current-state snapshot at time of writing: 687 ventures in Supabase, 58 contacts imported/enriched into OpenVolo, 29 org positions defined, sales scripts for 16 sectors, VAPI configured, ClickUp structure planned but not built (20%).
- Explicitly notes it is superseded in scope by `/Users/acebless/Documents/MASTER-INDEX.md` for overall navigation; this file remains authoritative only for sales-ops execution docs.

## Topic: Repository Intelligence & Knowledge Graph (Research Index)
- **source:** `/Users/acebless/Documents/WORLDWIDEBRO-OS/07-KNOWLEDGE/research/00-MASTER-INDEX.md` ("Master File Index — Worldwidebro OS", 2026-06-13, precedence 3)
- Central navigation for repo-intelligence and capability-analysis artifacts: `repos-classified-by-layer.json`, `venture-to-repos-mapping.json`, `capability-gap-analysis.json`, `SYSTEM-ENHANCEMENT-ROADMAP.md`, `KNOWLEDGE-GRAPH-DASHBOARD.md`, `.planning/graph-data.json`.
- Describes the flow: Repos (700) → Capabilities (1,276 unique) → Core Capabilities (11 types) → Ventures (1,504 in graph, 618 with requirements) → Sectors (31) → Operating System → Company Building (Phase 1-3 roadmap).
- Note: this doc's own `00-MASTER-INDEX.md` filename is flagged for archival under the Master Index Consolidation Plan (see requirements.md REQ-consolidate-index-masters); it is still present as of this ingest.

## Topic: Portfolio PDF Reporting Pipeline
- **source:** `/Users/acebless/Documents/WORLDWIDEBRO-OS/08-DATA/portfolio-reports/README.md` ("Portfolio PDF Reports", precedence 0)
- Pure-Python (reportlab) tool generating a 3-tier PDF set from venture CSV data: Tier 1 holdings master (entity structure, capital stack, sector heat map, OPCO layer audit, repo alignment), Tier 2 per-sector books (18 sectors in current data), Tier 3 per-venture packets (712 rows from `VENTURES-CAPABILITIES-MAPPED.csv`).
- Config-driven via `config/holdings_config.json` (entity/trust structure, 4 capital layers, sector→layer map, unit-economics model, branding).
- Known data-quality caveats disclosed in-doc: `required_capabilities` empty for most ventures; only 14/1,597 repos (0.9%) carry a `related_ventures` link (repo↔venture join unreliable, capability-vocabulary mismatch); 3 sectors have no OPCO mapping (flagged for Board decision); 5 OPCOs have zero ventures currently. Unit economics are explicitly labeled as model-based projections, not actuals.

## Topic: Operating System Quickstart & Phase 1 Roadmap
- **source:** `/Users/acebless/Documents/Worldwidebro-Holdings/README-START-HERE.md` ("Worldwidebro Holdings Operating System", 2026-06-19, precedence 4)
- Quickstart guide for CEO/OPCO Presidents/Board covering 704 ventures across 18 OPCOs plus 10 horizontal shared functions. Reiterates the 6-stage venture lifecycle and 90-day Keep/Scale/Sell/Merge/Pause/Archive cadence (consistent with the Governance Charter constraints).
- Names Airtable as the command-center dashboard/source of truth for venture tracking.
- Lists required reading order: `GOVERNANCE-CHARTER.md` (own copy, in this same folder — distinct from the `_superseded` copy ingested as a SPEC in this batch; see INGEST-CONFLICTS.md), `PHASE-1-EXECUTION-CHECKLIST.md`, `AIRTABLE_DASHBOARD_BLUEPRINT.md`, `VENTURE_INVENTORY_MASTER.csv`, `EXISTING-VENTURE-FILES-AUDIT.md`, `18-PDF-MASTER-TEMPLATE.md`, `TOOL-INTEGRATION-STACK.md`.
- 30-day timeline: Week 1 foundation + Airtable setup, Week 2 founder interviews (47 priority ventures), Week 3 planning/hiring, Week 4 finalization + Board review. Target: $5K-$15K/month revenue + operational governance live.

## Topic: Tool Capability Mapping (MCP)
- **source:** `/Users/acebless/Documents/TOOL_CAPABILITY_MAP.md` ("Tool Capability Map", 2026-06-22, precedence 1)
- Maps business goals to ready MCP tool servers to avoid re-discovery: Airtable (venture DB/dashboard), Slack (channel creation), ClickUp (task management), Notion (docs hub), Zapier (4 automation zaps), Gmail (briefings), GitHub, Graphify, Memory, Google Calendar, Stripe, HubSpot.
- All listed MCPs marked "Ready" as of 2026-06-22. Source of truth declared as `MCP_REGISTRY.json`.
