#!/usr/bin/env python3
"""Generate TOF/MOF/BOF script JSON and optional metadata for video pipeline."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

DOCS = Path("/Users/acebless/Documents")
FUNNEL_ROOT = DOCS / "WORLDWIDEBRO-OS/11_GROWTH_FUNNEL"
sys.path.insert(0, str(DOCS))

from venture_script_engine import FUNNEL_STAGES, build_script_package, load_venture, write_metadata  # noqa: E402

OUTPUT_DIR = DOCS / "moneyprinter-output"


def stage_output_name(stage: str) -> str:
    return f"metadata_{stage}.json"


def generate_stages(venture_id: str, stages: list[str]) -> list[Path]:
    venture = load_venture(venture_id)
    paths: list[Path] = []
    funnel_scripts = OUTPUT_DIR / venture_id / "funnel"
    funnel_scripts.mkdir(parents=True, exist_ok=True)

    for stage in stages:
        if stage not in FUNNEL_STAGES:
            continue
        package = build_script_package(venture, funnel_stage=stage)
        script_paths = {
            "tof": funnel_scripts / "01_TOF/scripts/tof-01.json",
            "mof": funnel_scripts / "02_MOF/scripts/mof-01.json",
            "bof": funnel_scripts / "03_BOF/scripts/bof-01.json",
        }
        script_path = script_paths[stage]
        script_path.parent.mkdir(parents=True, exist_ok=True)
        script_path.write_text(json.dumps(package, indent=2), encoding="utf-8")
        meta_path = write_metadata(venture_id, funnel_stage=stage, output_name=stage_output_name(stage))
        paths.extend([script_path, meta_path])
    return paths


def render_stage(venture_id: str, stage: str) -> None:
    meta = OUTPUT_DIR / venture_id / stage_output_name(stage)
    default_meta = OUTPUT_DIR / venture_id / "metadata.json"
    if meta.exists():
        default_meta.write_text(meta.read_text(encoding="utf-8"), encoding="utf-8")
    runner = DOCS / "run_venture_video_pipeline.sh"
    if runner.exists():
        subprocess.run(["bash", str(runner), venture_id, "single"], check=False)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate funnel stage scripts")
    parser.add_argument("--venture-id", required=True)
    parser.add_argument("--stages", default="tof,mof,bof", help="Comma-separated: tof,mof,bof")
    parser.add_argument("--render", help="Render video for one stage (tof|mof|bof)")
    args = parser.parse_args()

    stages = [s.strip().lower() for s in args.stages.split(",") if s.strip()]
    paths = generate_stages(args.venture_id, stages)
    print(f"✅ Generated {len(paths)} files for {args.venture_id}")
    for p in paths:
        print(f"   • {p}")

    if args.render:
        render_stage(args.venture_id, args.render.strip().lower())
        print(f"   🎬 Render triggered for stage {args.render}")


if __name__ == "__main__":
    main()
