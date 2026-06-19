#!/usr/bin/env python3
"""Batch: init funnel, generate TOF/MOF/BOF, run full Mon–Sun weekly cycle for all ventures."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

FUNNEL_ROOT = Path("/Users/acebless/Documents/WORLDWIDEBRO-OS/11_GROWTH_FUNNEL")
SCRIPTS = FUNNEL_ROOT / "SCRIPTS"
BATCH_JSON = FUNNEL_ROOT / "REGISTRY/construction-batch.json"
DOCS = Path("/Users/acebless/Documents")
OUTPUT = DOCS / "moneyprinter-output"

WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def run(cmd: list[str], dry_run: bool = False) -> int:
    print(f"  $ {' '.join(cmd)}")
    if dry_run:
        return 0
    return subprocess.call(cmd)


def load_ventures(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["ventures"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Batch weekly funnel for all ventures")
    parser.add_argument("--batch", default=str(BATCH_JSON), help="Venture batch JSON")
    parser.add_argument("--skip-init", action="store_true")
    parser.add_argument("--skip-generate", action="store_true")
    parser.add_argument("--skip-weekly", action="store_true")
    parser.add_argument("--render", action="store_true", help="Render Wed/Fri videos (slow)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    ventures = load_ventures(Path(args.batch))
    summary: list[dict] = []
    started = datetime.now().isoformat()

    for v in ventures:
        vid = v["venture_id"]
        code = v.get("venture_code", vid[:8])
        print(f"\n{'='*60}\n{code} {vid}\n{'='*60}")

        if not args.skip_init:
            rc = run(
                ["python3", str(SCRIPTS / "init_venture_funnel.py"), "--venture-id", vid],
                args.dry_run,
            )
            if rc != 0:
                summary.append({"venture_id": vid, "code": code, "error": "init failed"})
                continue

        if not args.skip_generate:
            run(
                [
                    "python3",
                    str(SCRIPTS / "generate_funnel_content.py"),
                    "--venture-id",
                    vid,
                    "--stages",
                    "tof,mof,bof",
                ],
                args.dry_run,
            )

        if not args.skip_weekly:
            for day in WEEKDAYS:
                cmd = [
                    "python3",
                    str(SCRIPTS / "weekly_funnel_runner.py"),
                    "--venture-id",
                    vid,
                    "--day",
                    day,
                ]
                if args.render and day in ("wednesday", "friday"):
                    cmd.append("--render")
                run(cmd, args.dry_run)

        summary.append({"venture_id": vid, "code": code, "status": "ok"})

    report = {
        "started_at": started,
        "finished_at": datetime.now().isoformat(),
        "ventures": len(ventures),
        "results": summary,
        "dry_run": args.dry_run,
    }
    report_path = OUTPUT / "funnel_batch_report.json"
    if not args.dry_run:
        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"\n✅ Batch report: {report_path}")
    else:
        print(f"\n✅ Dry run complete ({len(ventures)} ventures × 7 days)")


if __name__ == "__main__":
    main()
