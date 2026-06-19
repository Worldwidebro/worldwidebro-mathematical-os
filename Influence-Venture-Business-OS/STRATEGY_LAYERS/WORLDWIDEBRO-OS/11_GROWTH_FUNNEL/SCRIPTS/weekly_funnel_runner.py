#!/usr/bin/env python3
"""Run the weekly funnel job for the current (or specified) weekday."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

DOCS = Path("/Users/acebless/Documents")
FUNNEL_ROOT = DOCS / "WORLDWIDEBRO-OS/11_GROWTH_FUNNEL"
sys.path.insert(0, str(FUNNEL_ROOT / "SCRIPTS"))
sys.path.insert(0, str(DOCS))

from content_brain import ContentBrain  # noqa: E402
from venture_script_engine import (  # noqa: E402
    build_script_package,
    extract_venture_code,
    load_venture,
    short_brand,
    write_metadata,
)

TRIGGERS_PATH = FUNNEL_ROOT / "REGISTRY/weekly-triggers.json"
OUTPUT_DIR = DOCS / "moneyprinter-output"

WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def today_day_name() -> str:
    return WEEKDAYS[datetime.now().weekday()]


def load_triggers() -> dict:
    return json.loads(TRIGGERS_PATH.read_text(encoding="utf-8"))


def generate_hook_variations(brand: str, pain: str, count: int) -> list[str]:
    templates = [
        f"You're losing money if you ignore {pain.lower()}.",
        f"Everyone says they have a system. Most contractors still bleed on {pain.lower()}.",
        f"Contrarian take: your crew isn't the bottleneck — {pain.lower()} is.",
        f"80% of schedule slip traces back to {pain.lower()}.",
        f"Still fixing {pain.lower()} in spreadsheets? That's the hidden tax.",
        f"If {brand} can't see it in one view, you're flying blind.",
        f"The fix for {pain.lower()} isn't more meetings.",
        f"POV: pour day and nobody tracked the delivery window.",
        f"Stop hiring your way out of {pain.lower()}.",
        f"What top GCs automate before they scale past 5 jobs.",
        f"This one ops gap costs more than a bad sub.",
        f"You're not slow — your data trail is.",
        f"Industry secret: winners track {pain.lower()} daily.",
        f"The {brand} workflow in 15 seconds.",
        f"Why '{pain.lower()}' keeps killing margin.",
        f"Do this before your next owner update.",
        f"Field truth: if it's not logged, it didn't happen.",
        f"One dashboard beat fifteen tabs for us.",
        f"Late materials aren't bad luck — they're bad process.",
        f"Next week starts with fixing {pain.lower()}.",
    ]
    return templates[:count]


def run_day(
    venture_id: str,
    day: str,
    dry_run: bool = False,
    render: bool = False,
) -> dict:
    triggers = load_triggers()
    day_cfg = triggers["days"][day]
    venture = load_venture(venture_id)
    code = extract_venture_code(venture["venture_name"])
    brand = short_brand(venture["venture_name"])
    pain = "supply chain and schedule slip"
    brain = ContentBrain()
    log: dict = {"day": day, "venture_id": venture_id, "actions": [], "backend": brain.backend_label()}

    if dry_run:
        log["actions"].append(f"DRY RUN: would execute {day_cfg['actions']}")
        return log

    brain.upsert_venture(venture_id, code, venture["venture_name"], venture.get("sector", ""))

    if day == "monday":
        hooks = generate_hook_variations(brand, pain, day_cfg["outputs"]["hooks"])
        brain.insert_hooks(venture_id, hooks, day, "tof")
        kept = hooks[: day_cfg["outputs"]["hooks_keep"]]
        for i, hook in enumerate(kept[: day_cfg["outputs"]["short_videos"]]):
            pkg = build_script_package(venture, funnel_stage="tof")
            pkg["hook"] = hook
            pkg["script_lines"] = [hook] + pkg["script_lines"][1:]
            write_metadata(venture_id, funnel_stage="tof", output_name=f"metadata_tof_{i+1}.json")
            brain.insert_asset(
                venture_id, "tof", "script_json", hook, pkg.get("script"), day, script_json=pkg, status="queued"
            )
            brain.queue_publish(venture_id, "tof", {"hook": hook, "metadata_file": f"metadata_tof_{i+1}.json"})
        log["actions"].append(f"inserted {len(hooks)} hooks, {len(kept[:3])} video scripts")

    elif day == "tuesday":
        pkg_mof = build_script_package(venture, funnel_stage="mof")
        brain.insert_asset(
            venture_id,
            "mof",
            "post",
            "Here's why this works…",
            pkg_mof["script_lines"][0],
            day,
            status="queued",
        )
        brain.insert_asset(
            venture_id,
            "tof",
            "post",
            None,
            f"Repost winner: amplify top {int(triggers['default_thresholds']['tof_amplify_top_percent']*100)}% from Monday",
            day,
            status="draft",
        )
        log["actions"].append("MOF bridge posts + amplify placeholder")

    elif day == "wednesday":
        pkg = build_script_package(venture, funnel_stage="mof")
        write_metadata(venture_id, funnel_stage="mof", output_name="metadata_mof.json")
        brain.insert_asset(venture_id, "mof", "short_video", pkg["hook"], pkg["script"], day, script_json=pkg)
        brain.queue_publish(venture_id, "mof", {"metadata_file": "metadata_mof.json"})
        if render:
            _render(venture_id, "mof")
        log["actions"].append("MOF demo script + queue")

    elif day == "thursday":
        for title in ("Case study A", "Case study B"):
            brain.insert_asset(
                venture_id,
                "mof",
                "case_study",
                title,
                f"[VERIFY] Before/after for {brand}. Metric + quote required.",
                day,
            )
        brain.insert_asset(
            venture_id,
            "mof",
            "post",
            f"{brand} vs spreadsheets",
            "Comparison: manual tracking vs unified workflow.",
            day,
        )
        log["actions"].append("2 case studies + 1 comparison")

    elif day == "friday":
        pkg = build_script_package(venture, funnel_stage="bof")
        write_metadata(venture_id, funnel_stage="bof", output_name="metadata_bof.json")
        brain.insert_asset(venture_id, "bof", "short_video", pkg["hook"], pkg["script"], day, script_json=pkg)
        brain.insert_asset(
            venture_id,
            "bof",
            "post",
            "ROI breakdown",
            f"Value stack + guarantee for {brand}. See 03_BOF/offers.md",
            day,
        )
        brain.queue_publish(venture_id, "bof", {"metadata_file": "metadata_bof.json"})
        if render:
            _render(venture_id, "bof")
        log["actions"].append("BOF offer + testimonial queue")

    elif day == "saturday":
        week_start = (date.today() - timedelta(days=date.today().weekday())).isoformat()
        report = {
            "week_start": week_start,
            "generated_at": datetime.now().isoformat(),
            "best_hooks": generate_hook_variations(brand, pain, 5),
            "notes": "Connect platform analytics to gf_analytics_snapshots for live scores.",
            "funnel_map": {"tof": "hooks queued", "mof": "demos queued", "bof": "offers queued"},
        }
        report_path = OUTPUT_DIR / venture_id / "funnel" / "reports" / f"week_{week_start}.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        brain.save_weekly_report(venture_id, week_start, report)
        log["actions"].append(f"weekly report → {report_path}")

    elif day == "sunday":
        hooks = generate_hook_variations(brand, pain, day_cfg["outputs"]["hooks"])
        brain.insert_hooks(venture_id, hooks, day, "tof")
        for stage in ("tof", "mof", "bof"):
            pkg = build_script_package(venture, funnel_stage=stage)
            brain.insert_asset(venture_id, stage, "script_json", pkg["hook"], pkg["script"], day, script_json=pkg)
        ideas_path = OUTPUT_DIR / venture_id / "funnel" / "next_week_ideas.json"
        ideas_path.parent.mkdir(parents=True, exist_ok=True)
        ideas_path.write_text(
            json.dumps({"hooks": hooks[:10], "ideas": hooks[10:], "prefetch_monday": True}, indent=2),
            encoding="utf-8",
        )
        log["actions"].append(f"next week batch → {ideas_path}")

    log_path = OUTPUT_DIR / venture_id / "funnel" / "weekly_runs" / f"{day}_{date.today().isoformat()}.json"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(json.dumps(log, indent=2), encoding="utf-8")
    return log


def _render(venture_id: str, stage: str) -> None:
    meta = OUTPUT_DIR / venture_id / f"metadata_{stage}.json"
    default = OUTPUT_DIR / venture_id / "metadata.json"
    if meta.exists():
        default.write_text(meta.read_text(encoding="utf-8"), encoding="utf-8")
    runner = DOCS / "run_venture_video_pipeline.sh"
    if runner.exists():
        subprocess.run(["bash", str(runner), venture_id, "single"], check=False)


def main() -> None:
    parser = argparse.ArgumentParser(description="Weekly funnel runner")
    parser.add_argument("--venture-id", required=True)
    parser.add_argument("--day", default="auto", help="monday..sunday or auto")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--render", action="store_true", help="Render video on Wed/Fri")
    args = parser.parse_args()

    day = today_day_name() if args.day == "auto" else args.day.lower()
    if day not in WEEKDAYS:
        parser.error(f"Invalid day: {day}")

    log = run_day(args.venture_id, day, dry_run=args.dry_run, render=args.render)
    print(f"✅ Weekly job [{day}] venture={args.venture_id}")
    print(f"   Backend: {log['backend']}")
    for action in log["actions"]:
        print(f"   • {action}")


if __name__ == "__main__":
    main()
