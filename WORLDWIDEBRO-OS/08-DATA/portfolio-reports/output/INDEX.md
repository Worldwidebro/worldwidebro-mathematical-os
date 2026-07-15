# Worldwidebro Holdings — Portfolio, Entity & Trust Playbook

Generated 2026-07-03 by `generate_portfolio_pdfs.py` from `config/holdings_config.json` +
`VENTURES-CAPABILITIES-MAPPED.csv` + `REPOSITORY-REGISTRY.json`. Regenerate anytime with:

```bash
cd WORLDWIDEBRO-OS/08-DATA/portfolio-reports
python3 generate_portfolio_pdfs.py
```

## Contents

- `00-HOLDINGS-MASTER.pdf` (29 pp) — single source of truth. Sections:
  1. Entity & Trust Structure (Trust → Holdings → LLC → 18 OPCOs → 712 Ventures)
  2. Capital Stack (4 layers)
  3. Portfolio by Sector
  4. **OPCO Layer audit** — which sectors map to which OPCO, and at what confidence
  5. **Repository Alignment** — live pull from the 1,597-repo registry, category breakdown, top 15 by strategic value
  6. Top 25 Ventures by Strategic Score
  7. Full Venture Index (venture, sector, OPCO, stage)
- `sectors/*.pdf` (18 books) — one per sector, now labeled with its OPCO + match confidence
- `ventures/<id>.pdf` (712 packets) — each now has an OPCO row in the Evaluation Snapshot

## Known gaps (surfaced in the PDF, not hidden)

- **3 sectors have no OPCO assignment**: `emerging`, `specialized` — flagged in §4, needs a Board decision.
- **2 sectors are approximate matches**: `community` → OPCO-Operations, `fitness-sports` → OPCO-Healthcare,
  `professional-services` → OPCO-Staffing — judgment calls, not prior authority.
- **5 OPCOs have zero ventures**: Agriculture, Energy, Investment, Manufacturing, Retail — empty shells.
- **Repo↔venture join is 14/1,597 (0.9%)** — `related_ventures` is populated for almost nothing.
  This is the real blocker to true topology awareness; §5 is inventory, not a build map, until fixed.
- **Trust is "Planned" status** — no trust has been formed yet, only modeled in the entity table.

## Next step to close the repo↔venture gap

Capability vocabulary mismatch is the root cause (see memory `company-factory-and-repo-platform`).
Fixing it means re-running the capability backfill against a shared vocabulary, not re-running this PDF pipeline.
