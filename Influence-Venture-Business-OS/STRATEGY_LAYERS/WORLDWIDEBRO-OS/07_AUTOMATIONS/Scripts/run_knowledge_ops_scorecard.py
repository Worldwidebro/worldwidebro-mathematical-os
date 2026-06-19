#!/usr/bin/env python3
"""Compute Knowledge Ops Score from alignment JSON, registries, and optional RAG health."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path
from typing import Any, Dict, List
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[3]
ALIGNMENT = ROOT / ".planning" / "venture-hub-alignment.json"
OWNED_REGISTRY = ROOT / "venture-hub" / "registries" / "github_owned.csv"
STARRED_REGISTRY = ROOT / "venture-hub" / "registries" / "github_starred.csv"
BRIDGE = ROOT / "venture-hub" / "registries" / "venture_uuid_slug_bridge.csv"
UNIFIED_712 = ROOT / "WORLDWIDEBRO-OS" / "08_RESEARCH" / "Ventures-Data" / "WORLDWIDEBRO-712-UNIFIED.csv"
GRAPH_DATA = ROOT / ".planning" / "graph-data.json"
SCORECARD_DIR = ROOT / "WORLDWIDEBRO-OS" / "08_RESEARCH" / "Knowledge-Ops"
RAG_HEALTH_URL = "http://127.0.0.1:8000/health"


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def pct(n: float, d: float) -> float:
    return round((n / d) * 100, 2) if d else 100.0


def score_data_fidelity(alignment: Dict[str, Any]) -> float:
    ventures = alignment.get("ventures", []) or []
    if not ventures:
        return 0.0
    def owned_found(v: dict) -> bool:
        val = v.get("owned_repo_found")
        if isinstance(val, bool):
            return val
        return str(val or "").lower() in ("yes", "true", "matched", "1")

    owned_ok = sum(1 for v in ventures if owned_found(v))
    starred_ok = sum(1 for v in ventures if int(v.get("starred_repos_count") or 0) > 0)
    aligned = sum(1 for v in ventures if v.get("alignment_status") == "aligned")
    bridge_ok = 100.0
    if BRIDGE.exists():
        with BRIDGE.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        unmatched = sum(1 for r in rows if (r.get("match_method") or "") == "unmatched")
        bridge_ok = pct(len(rows) - unmatched, len(rows)) if rows else 100.0
    urls_712 = 100.0
    if UNIFIED_712.exists():
        with UNIFIED_712.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        if rows and "owned_repo_url" in rows[0]:
            urls_712 = pct(sum(1 for r in rows if (r.get("owned_repo_url") or "").startswith("http")), len(rows))
    return round(
        (pct(owned_ok, len(ventures)) + pct(starred_ok, len(ventures)) + pct(aligned, len(ventures)) + bridge_ok + urls_712)
        / 5,
        2,
    )


def score_graph(alignment: Dict[str, Any]) -> float:
    ventures = alignment.get("ventures", []) or []
    if not ventures:
        return 0.0
    connected = sum(1 for v in ventures if v.get("graph_connected"))
    graph_score = pct(connected, len(ventures))
    freshness = 50.0
    if GRAPH_DATA.exists():
        gd = load_json(GRAPH_DATA)
        entity_count = gd.get("entity_count") or len(gd.get("entities", []) or [])
        freshness = 100.0 if entity_count > 1000 else 70.0
    return round((graph_score * 0.8) + (freshness * 0.2), 2)


def score_rag(rag_eval_pct: float | None, rag_healthy: bool) -> float:
    if rag_eval_pct is not None:
        return rag_eval_pct
    if rag_healthy:
        return 50.0  # placeholder until manual rag-eval-questions.md grading
    return 0.0


def score_socraticode() -> float:
    profiles = ROOT / "socraticode_profiles.json"
    deps = ROOT / "WORLDWIDEBRO-OS" / "08_RESEARCH" / "Ventures-Data" / "ventures_dependencies.json"
    if not profiles.exists():
        return 50.0
    prof = load_json(profiles)
    indexed = len(prof.get("repos", prof) if isinstance(prof, dict) else [])
    if isinstance(prof, dict) and "repos" not in prof:
        indexed = len(prof)
    dep_data = load_json(deps).get("dependencies", {}) if deps.exists() else {}
    required: List[str] = []
    for dep in dep_data.values():
        required.extend(dep.get("required_repos", []) or [])
    required_set = {r.lower() for r in required[:150]}
    if not required_set:
        return min(100.0, 50.0 + indexed)
    return min(100.0, round(50 + min(indexed, 50), 2))


def score_execution() -> float:
    mcp_health = 70.0
    matrix = ROOT / "venture-hub" / "docs" / "INSTALL_VERIFICATION_MATRIX.csv"
    if matrix.exists():
        with matrix.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        if rows:
            ok = sum(1 for r in rows if (r.get("status") or "").lower() in ("ok", "pass", "verified"))
            mcp_health = pct(ok, len(rows))
    adoption = ROOT / "venture-hub" / "registries" / "compounding_adoption_log.csv"
    compounding = 50.0
    if adoption.exists():
        with adoption.open(newline="", encoding="utf-8") as f:
            rows = [r for r in csv.DictReader(f) if any((r.get("repo") or r.get("starred_repo") or "").strip())]
        compounding = min(100.0, 50 + len(rows) * 5)
    return round((mcp_health * 0.6) + (compounding * 0.4), 2)


def rag_health_check() -> bool:
    try:
        req = Request(RAG_HEALTH_URL, method="GET")
        with urlopen(req, timeout=3) as resp:
            return resp.status == 200
    except Exception:
        return False


def write_scorecard_row(scores: Dict[str, float], notes: str) -> Path:
    SCORECARD_DIR.mkdir(parents=True, exist_ok=True)
    out = SCORECARD_DIR / f"knowledge-ops-scorecard-{date.today().isoformat()}.csv"
    fieldnames = [
        "week_ending",
        "data_fidelity_pct",
        "graph_connectivity_pct",
        "lightrag_eval_pct",
        "socraticode_coverage_pct",
        "execution_compounding_pct",
        "knowledge_ops_score",
        "notes",
    ]
    row = {
        "week_ending": date.today().isoformat(),
        "data_fidelity_pct": scores["data_fidelity_pct"],
        "graph_connectivity_pct": scores["graph_connectivity_pct"],
        "lightrag_eval_pct": scores["lightrag_eval_pct"],
        "socraticode_coverage_pct": scores["socraticode_coverage_pct"],
        "execution_compounding_pct": scores["execution_compounding_pct"],
        "knowledge_ops_score": scores["knowledge_ops_score"],
        "notes": notes,
    }
    write_header = not out.exists()
    with out.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            w.writeheader()
        w.writerow(row)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Knowledge Ops weekly scorecard")
    parser.add_argument("--rag-eval", type=float, help="Manual RAG eval percent (0-100)")
    parser.add_argument("--notes", default="", help="Optional notes for this week")
    args = parser.parse_args()

    alignment = load_json(ALIGNMENT)
    summary = alignment.get("summary", {})

    data_pct = score_data_fidelity(alignment)
    graph_pct = score_graph(alignment)
    rag_pct = score_rag(args.rag_eval, rag_health_check())
    soc_pct = score_socraticode()
    exec_pct = score_execution()

    total = round(
        data_pct * 0.25 + graph_pct * 0.20 + rag_pct * 0.25 + soc_pct * 0.15 + exec_pct * 0.15,
        2,
    )

    scores = {
        "data_fidelity_pct": data_pct,
        "graph_connectivity_pct": graph_pct,
        "lightrag_eval_pct": rag_pct,
        "socraticode_coverage_pct": soc_pct,
        "execution_compounding_pct": exec_pct,
        "knowledge_ops_score": total,
    }

    notes = args.notes or (
        f"aligned={summary.get('ventures_aligned')}/{summary.get('total_ventures')} "
        f"attention={summary.get('ventures_needing_attention')}"
    )
    out = write_scorecard_row(scores, notes)

    print("Knowledge Ops Score:", total)
    for k, v in scores.items():
        print(f"  {k}: {v}")
    print("Wrote:", out)
    if args.rag_eval is None:
        print("Tip: grade rag-eval-questions.md then re-run with --rag-eval 85")


if __name__ == "__main__":
    main()
