#!/usr/bin/env python3
"""
build_operating_economics.py
Aggregates venture readiness scorecards, revenue models, and financial KPIs
to output a unified operating economics report for investor presentations.
"""
import csv
import json
import os
import sys

DOCS = "/Users/acebless/Documents"
REGISTRIES = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/registries"
KPI_FILE = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/Influence-Venture-Business-OS/STRATEGY_LAYERS/WORLDWIDEBRO-OS/01_CEO_COMMAND_CENTER/KPIs/financial-kpis.json"

SCORECARD_PATH = f"{REGISTRIES}/VENTURE-READINESS-SCORECARD.csv"
REVENUE_MODELS_PATH = f"{REGISTRIES}/VENTURE-REVENUE-MODELS.csv"
UNIT_ECONOMICS_PATH = f"{REGISTRIES}/UNIT-ECONOMICS-BY-VENTURE-TYPE.csv"

OUT_JSON = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/financials/studio_operating_economics.json"
OUT_MD = f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/financials/studio_operating_economics.md"


def log(msg):
    print(f"[*] {msg}", file=sys.stderr)


def main():
    log("Starting operating economics aggregation...")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)

    # 1. Parse Scorecard
    if not os.path.exists(SCORECARD_PATH):
        sys.exit(f"Error: Scorecard not found at {SCORECARD_PATH}")

    ventures = []
    readiness_scores = []
    stages = {}
    sectors = {}

    with open(SCORECARD_PATH, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            vid = row.get("venture_id", "")
            if not vid:
                continue
            r_pct = float(row.get("readiness_pct", 0.0))
            stage = row.get("development_stage", "planned")
            sector = row.get("sector", "unknown")

            ventures.append(row)
            readiness_scores.append(r_pct)
            stages[stage] = stages.get(stage, 0) + 1
            sectors[sector] = sectors.get(sector, 0) + 1

    total_ventures = len(ventures)
    avg_readiness = sum(readiness_scores) / len(readiness_scores) if readiness_scores else 0.0

    # 2. Parse Revenue Models
    revenue_models_count = 0
    model_types = {}
    if os.path.exists(REVENUE_MODELS_PATH):
        with open(REVENUE_MODELS_PATH, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rm = row.get("revenue_model", "").strip()
                if rm and rm.lower() != "unknown" and rm.lower() != "none":
                    revenue_models_count += 1
                    model_types[rm] = model_types.get(rm, 0) + 1

    # 3. Read Financial KPIs
    kpi_data = {}
    if os.path.exists(KPI_FILE):
        with open(KPI_FILE, mode="r", encoding="utf-8") as f:
            kpi_data = json.load(f)

    # 4. Map Unit Economics Reference
    unit_economics = []
    if os.path.exists(UNIT_ECONOMICS_PATH):
        with open(UNIT_ECONOMICS_PATH, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                unit_economics.append({
                    "type": row.get("Venture_Type", ""),
                    "revenue_model": row.get("Revenue_Model", ""),
                    "avg_rev": row.get("Avg_Monthly_Revenue", ""),
                    "margin": row.get("Profit_Margin_Percent", ""),
                    "example": row.get("Examples", "")
                })

    # Compile economics payload
    payload = {
        "generated_at": kpi_data.get("as_of", "2026-07-15"),
        "total_ventures": total_ventures,
        "average_readiness_pct": round(avg_readiness, 2),
        "total_sectors": len(sectors),
        "development_stages": stages,
        "sector_distribution": sectors,
        "revenue_models": {
            "mapped_count": revenue_models_count,
            "distribution": model_types
        },
        "financial_kpis": kpi_data,
        "reference_unit_economics": unit_economics
    }

    # Write JSON
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    log(f"Written JSON report to {OUT_JSON}")

    # Write Markdown Slide
    stages_str = "\n".join([f"  * **{k.title()}**: {v} ventures" for k, v in stages.items()])
    sectors_str = "\n".join([f"  * **{k.title()}**: {v} ventures" for k, v in sorted(sectors.items(), key=lambda x: -x[1])[:8]])
    
    kpi_targets = kpi_data.get("targets", {})
    kpi_current = kpi_data.get("current", {})
    kpi_trend = kpi_data.get("trend", {})

    md_content = f"""# Operating Economics & Portfolio Summary
As-of Date: {payload['generated_at']}

---

## 1. Portfolio Vital Stats
*   **Total Sectors (OpCos):** {payload['total_sectors']}
*   **Total Spawned Ventures:** {payload['total_ventures']}
*   **Average Readiness Score:** {payload['average_readiness_pct']}%
*   **Venture Distribution by Stage:**
{stages_str}

---

## 2. Top Sectors by Scale
{sectors_str}
*   *And {payload['total_sectors'] - 8} other sectors...*

---

## 3. Financial Performance & Revenue Trajectory

| Metric | Current | Target (Q3 2026) | Completion % |
| :--- | :--- | :--- | :--- |
| **Total Monthly Revenue** | ${kpi_current.get('total_monthly_revenue', 0):,} | ${kpi_targets.get('total_monthly_revenue', 0):,} | {kpi_data.get('progress', {}).get('monthly_revenue_progress', '0%')} |
| **SaaS MRR** | ${kpi_current.get('saas_mrr', 0):,} | ${kpi_targets.get('saas_mrr', 0):,} | {kpi_data.get('progress', {}).get('saas_mrr_progress', '0%')} |
| **Operations MRR** | ${kpi_current.get('operations_mrr', 0):,} | ${kpi_targets.get('operations_mrr', 0):,} | {kpi_data.get('progress', {}).get('operations_mrr_progress', '0%')} |
| **Combined ARR** | ${kpi_current.get('combined_arr', 0):,} | ${kpi_targets.get('combined_arr', 0):,} | {kpi_data.get('progress', {}).get('annual_revenue_progress', '0%')} |
| **Net Profit Margin** | {kpi_current.get('net_margin', '0%')} | {kpi_targets.get('net_margin', '0%')} | -- |

*   **Growth Velocity:** {kpi_trend.get('velocity', 'N/A')} ({kpi_trend.get('direction', 'up')}ward trend)
*   **Estimated Target Date:** {kpi_trend.get('eta_to_target', 'N/A')}

---

## 4. Projected Unit Economics Reference

| Venture Type | Revenue Model | Avg Monthly Rev | Target Profit Margin | Sample Ventures |
| :--- | :--- | :--- | :--- | :--- |
"""
    for ue in unit_economics[:6]:
        md_content += f"| {ue['type']} | {ue['revenue_model']} | {ue['avg_rev']} | {ue['margin']} | {ue['example']} |\n"

    md_content += """
---

*Confidential Portfolio Report for Winners Circle WC LLC (IZA OS Venture Factory)*
"""

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(md_content)
    log(f"Written Markdown report to {OUT_MD}")
    log("Operating economics successfully compiled!")


if __name__ == "__main__":
    main()
