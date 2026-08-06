#!/usr/bin/env python3
"""Gap analysis: active venture needs vs pilot registry capabilities."""

import csv
import json
from collections import defaultdict
from pathlib import Path

REGISTRY = Path(__file__).parent
CSV_PATH = REGISTRY / "repository_registry_pilot.csv"
VOCAB_PATH = REGISTRY / "repo_vocabulary.json"
OUTPUT = REGISTRY / "venture_capability_gaps.json"


def main() -> None:
    vocab = json.loads(VOCAB_PATH.read_text(encoding="utf-8"))
    needs = vocab["venture_capability_needs"]
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))

    covered: dict[str, set[str]] = defaultdict(set)
    repos_by_cap: dict[str, list[str]] = defaultdict(list)

    for row in rows:
        caps = [c for c in row["capabilities"].split(";") if c]
        for cap in caps:
            repos_by_cap[cap].append(row["repo_name"])
        for venture in row["related_ventures"].split(";"):
            if venture in needs:
                covered[venture].update(caps)

    report: dict[str, dict] = {}
    for venture, required in needs.items():
        have = covered.get(venture, set())
        missing = [c for c in required if c not in have]
        report[venture] = {
            "required": required,
            "covered": sorted(have),
            "missing": missing,
            "coverage_pct": round(100 * (len(required) - len(missing)) / len(required), 1),
            "suggested_repos": {
                cap: repos_by_cap.get(cap, [])[:5] for cap in missing
            },
        }

    OUTPUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Gap analysis written to {OUTPUT}")
    for venture, data in report.items():
        print(f"  {venture}: {data['coverage_pct']}% covered, missing {data['missing']}")


if __name__ == "__main__":
    main()
