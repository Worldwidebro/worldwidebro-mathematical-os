#!/usr/bin/env python3
"""Scaffold TOF/MOF/BOF funnel folder for a venture from linkage CSV."""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

DOCS = Path("/Users/acebless/Documents")
FUNNEL_ROOT = DOCS / "WORLDWIDEBRO-OS/11_GROWTH_FUNNEL"
TEMPLATE = FUNNEL_ROOT / "_TEMPLATE"
LINKAGE_CSV = DOCS / "WORLDWIDEBRO-OS/08_RESEARCH/Ventures-Data/WORLDWIDEBRO-VENTURES-REPOS-ALIGNMENT.csv"
VENTURES_DIR = FUNNEL_ROOT / "ventures"
OUTPUT_DIR = DOCS / "moneyprinter-output"


def extract_venture_code(name: str) -> str | None:
    match = re.match(r"^(CON-\d+)", name.strip())
    return match.group(1) if match else None


def short_brand(name: str) -> str:
    code = extract_venture_code(name)
    if code:
        return name.replace(code, "").strip() or name
    return name


def load_venture(venture_id: str) -> dict[str, str]:
    with LINKAGE_CSV.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row.get("venture_id", "").strip() == venture_id:
                return {k: (v or "").strip() for k, v in row.items()}
    raise ValueError(f"Venture not found: {venture_id}")


def fill_placeholders(text: str, ctx: dict[str, str]) -> str:
    for key, value in ctx.items():
        text = text.replace(f"{{{{{key}}}}}", value)
    return text


def copy_template(dest: Path) -> None:
    if dest.exists():
        return
    shutil.copytree(TEMPLATE, dest)


def personalize_files(venture_dir: Path, ctx: dict[str, str]) -> None:
    for path in venture_dir.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".json", ".csv"}:
            content = path.read_text(encoding="utf-8")
            path.write_text(fill_placeholders(content, ctx), encoding="utf-8")


def write_manifest(venture_dir: Path, venture: dict[str, str], code: str | None) -> None:
    manifest = {
        "venture_id": venture["venture_id"],
        "venture_code": code,
        "venture_name": venture["venture_name"],
        "sector": venture.get("sector", ""),
        "created_at": datetime.now().isoformat(),
        "stages": ["foundation", "tof", "mof", "bof", "retention"],
        "agents": json.loads((FUNNEL_ROOT / "REGISTRY/funnel-agents.json").read_text())["default_routing"],
        "output_video_dir": str(OUTPUT_DIR / venture["venture_id"]),
    }
    (venture_dir / "funnel_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def init_funnel(venture_id: str, also_output: bool = True) -> Path:
    venture = load_venture(venture_id)
    code = extract_venture_code(venture["venture_name"]) or venture_id[:8]
    venture_dir = VENTURES_DIR / code
    copy_template(venture_dir)

    ctx = {
        "venture_id": venture_id,
        "venture_code": code,
        "venture_name": venture["venture_name"],
        "brand": short_brand(venture["venture_name"]),
        "sector": venture.get("sector", "con"),
        "icp": "Commercial GCs and specialty contractors",
        "pain": "Schedule slip and margin bleed from ops chaos",
        "outcome": "Predictable jobs and audit-ready workflows",
        "trigger": "Tax season, scaling stress, cashflow gaps",
        "tone": "technical, direct",
        "cta": "Book a free workflow review",
    }
    personalize_files(venture_dir, ctx)
    write_manifest(venture_dir, venture, code)

    if also_output:
        out_funnel = OUTPUT_DIR / venture_id / "funnel"
        if not out_funnel.exists():
            shutil.copytree(venture_dir, out_funnel)
    return venture_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Init venture growth funnel scaffold")
    parser.add_argument("--venture-id", required=True)
    parser.add_argument("--no-output-copy", action="store_true")
    args = parser.parse_args()
    path = init_funnel(args.venture_id, also_output=not args.no_output_copy)
    print(f"✅ Funnel scaffold: {path}")
    print(f"   Also copied to moneyprinter-output/{{id}}/funnel (unless --no-output-copy)")


if __name__ == "__main__":
    main()
