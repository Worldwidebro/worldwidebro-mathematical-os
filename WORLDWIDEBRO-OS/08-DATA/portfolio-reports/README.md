---
references:
  - [[VENTURE-MASTER]]
  - [[unified-company-roadmap-2026]]
  - [[ORB-MASTER-CONNECTOR-2026-06-11]]
---

# Portfolio PDF Reports

Renders a 3-tier PDF document set for Worldwidebro Holdings from venture CSV data.
Pure-Python (reportlab) — no LaTeX, no headless browser, no network.

## Tiers

| Tier | Output | What it is |
|------|--------|-----------|
| 1 | `output/00-HOLDINGS-MASTER.pdf` | Trust → Holdings → LLC → 18 OPCOs → Ventures entity structure, capital stack, sector heat map, **OPCO layer audit**, **repository alignment** (live from REPOSITORY-REGISTRY.json), top-25, full index |
| 2 | `output/sectors/<sector>.pdf` | One book per sector — economics + venture list (18 sectors in current data) |
| 3 | `output/ventures/<venture_id>.pdf` | One evaluation packet per venture (snapshot, unit economics, capabilities, auto-flagged risks) |

## Run

```bash
cd /Users/acebless/Documents
python3 WORLDWIDEBRO-OS/08-DATA/portfolio-reports/generate_portfolio_pdfs.py            # all 3 tiers (~3s for 731 PDFs)
python3 .../generate_portfolio_pdfs.py --tier master                                    # Tier 1 only
python3 .../generate_portfolio_pdfs.py --tier sectors                                   # Tier 1 + 2
python3 .../generate_portfolio_pdfs.py --limit 5                                        # cap packets (smoke test)
python3 .../generate_portfolio_pdfs.py --ventures-csv path/to/other.csv                 # different source
```

## Inputs

- **`config/holdings_config.json`** — entity/trust structure, 4 capital layers, sector→layer map, unit-economics model. Edit this to change entity names, targets, or branding (navy `#0B1F3A` / gold `#C9A24B`).
- **`VENTURES-CAPABILITIES-MAPPED.csv`** (repo root, 712 rows) — source of truth. Columns: `venture_id, name, sector, stage, status, required_capabilities` (last is `|`-delimited).

## Notes / next steps

- Unit economics are **model-based projections** keyed off each venture's capital layer (labeled as such in every doc). Wire live Supabase metrics (`ventures`, `graph_entities`) into `build_venture()` to replace projections with actuals.
- `required_capabilities` is empty for most ventures in the current CSV — packets show "no capabilities mapped" until the capability cross-ref is populated.
- **OPCO layer** (added 2026-07-03): `config/holdings_config.json` → `opco_layer.sector_to_opco` maps each of the 18 sectors to one of 18 OPCO shells, each tagged `exact` / `approximate` / `unassigned`. 3 sectors (`emerging`, `specialized`, and any future new sector) have no OPCO — flagged in §4 of the master PDF, needs a Board decision. 5 OPCOs (Agriculture, Energy, Investment, Manufacturing, Retail) currently have zero ventures.
- **Repository alignment** (added 2026-07-03): `load_repo_registry()` reads `REPOSITORY-REGISTRY.json` live at build time (never embedded in config, so it can't go stale) and reports category counts + top-15 by strategic value in §5. Coverage caveat: only 14/1,597 repos (0.9%) carry a `related_ventures` link — the repo↔venture join is not reliable yet (capability-vocabulary mismatch, see memory `company-factory-and-repo-platform`). §5 is inventory, not a build map, until that's fixed.
- Not included: live infrastructure topology (Supabase/DuckDB/Qdrant/Neo4j connection strings, Tailscale device map, MCP registry). That data contains credentials and shouldn't be baked into a portable PDF/ZIP — see `MCP_REGISTRY.json` and CLAUDE.md for that layer instead.
- Output (`output/`) is regenerated on every run; safe to gitignore or commit as a snapshot. A dated portable bundle is zipped to `WORLDWIDEBRO-HOLDINGS-PLAYBOOK-<date>.zip` alongside this README.
