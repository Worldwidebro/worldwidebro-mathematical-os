#!/usr/bin/env python3
"""Generate short-form video scripts and publish metadata for construction ventures."""

from __future__ import annotations

import csv
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

DOCS = Path("/Users/acebless/Documents")
LINKAGE_CSV = DOCS / "WORLDWIDEBRO-OS/08_RESEARCH/Ventures-Data/WORLDWIDEBRO-VENTURES-REPOS-ALIGNMENT.csv"
CAMPAIGN_JSON = DOCS / "moneyprinter-v2-construction-campaign.json"
OUTPUT_DIR = DOCS / "moneyprinter-output"

# Trade-specific script templates: hook + body lines + cta
TRADE_PLAYBOOKS: dict[str, dict[str, Any]] = {
    "supply_chain": {
        "match": ("supply chain", "material"),
        "topics": [
            "Why jobs stall when materials are late",
            "Lead times contractors ignore until it hurts",
            "Alternate suppliers when your PO fails",
        ],
        "hook": "Job stalled because materials didn't show up?",
        "lines": [
            "That's usually a supply chain problem — not your crew.",
            "Track lead times, alternates, and delivery windows before pour day.",
            "{brand} helps contractors stay on schedule.",
        ],
        "cta": "Get a free logistics audit — link in bio.",
        "keywords": ("delivery truck", "warehouse", "construction schedule"),
    },
    "permits": {
        "match": ("permit", "compliance"),
        "topics": ["Permit delays killing your timeline", "3 permit mistakes that cost weeks"],
        "hook": "Permit holdups can add weeks to a job.",
        "lines": [
            "Missing docs, wrong jurisdiction, expired approvals — it adds up fast.",
            "{brand} streamlines permit tracking so you submit once, correctly.",
            "Stop guessing status. Know what's approved and what's next.",
        ],
        "cta": "Book a permit workflow review — link below.",
        "keywords": ("building permit", "inspection", "compliance"),
    },
    "workforce": {
        "match": ("workforce", "crew"),
        "topics": ["Crew scheduling without the chaos", "When subs no-show"],
        "hook": "Wrong crew on site costs you a full day.",
        "lines": [
            "Scheduling trades, tracking certs, and filling gaps shouldn't be manual.",
            "{brand} keeps workforce plans visible across every active job.",
            "Fewer no-shows. Faster mobilization.",
        ],
        "cta": "Try workforce scheduling demo — link in bio.",
        "keywords": ("construction crew", "hard hat", "jobsite"),
    },
    "inspection": {
        "match": ("inspection", "site inspect"),
        "topics": ["Site inspection failures you can prevent", "Photo documentation that passes review"],
        "hook": "Failed inspection? It's rarely a surprise.",
        "lines": [
            "Document issues in the field before they become punch-list disasters.",
            "{brand} captures site conditions with audit-ready reports.",
            "Catch defects early — not at closeout.",
        ],
        "cta": "Schedule a demo walkthrough — link below.",
        "keywords": ("site inspection", "checklist", "construction quality"),
    },
    "payments": {
        "match": ("payment", "subcontractor pay"),
        "topics": ["Sub payment delays and lien risk", "Getting paid faster on commercial jobs"],
        "hook": "Slow sub payments kill trust on every job.",
        "lines": [
            "Missed draws and disputed invoices stall the whole chain.",
            "{brand} tracks subcontractor payments with clear approval trails.",
            "Pay on time. Protect your reputation.",
        ],
        "cta": "See payment workflow — link in bio.",
        "keywords": ("invoice", "construction finance", "contractor"),
    },
    "bids": {
        "match": ("bid",),
        "topics": ["Win more bids without racing to the bottom", "Estimate accuracy in 48 hours"],
        "hook": "Lost the bid by a margin you never saw coming?",
        "lines": [
            "Bad takeoffs and stale pricing leak margin before you break ground.",
            "{brand} centralizes bids, scopes, and vendor quotes in one place.",
            "Bid smarter — not cheaper.",
        ],
        "cta": "Download bid checklist — link below.",
        "keywords": ("construction estimate", "blueprint", "contractor bid"),
    },
    "equipment": {
        "match": ("equipment", "rental"),
        "topics": ["Equipment idle time is margin bleed", "Rent vs own on mid-size jobs"],
        "hook": "Paying for iron sitting on the lot?",
        "lines": [
            "Idle rentals and double-booked lifts burn budget every week.",
            "{brand} matches equipment to phase so you mobilize what you need, when you need it.",
            "Less downtime. More production.",
        ],
        "cta": "Get equipment utilization review — link in bio.",
        "keywords": ("excavator", "construction equipment", "rental"),
    },
    "analytics": {
        "match": ("analytics", "project analytics"),
        "topics": ["Jobs losing margin before you notice", "Dashboards GCs actually use"],
        "hook": "Your project is off track — do you know by how much?",
        "lines": [
            "Schedule slip, cost creep, and change orders hide in spreadsheets.",
            "{brand} surfaces project analytics before variance becomes loss.",
            "See problems while you can still fix them.",
        ],
        "cta": "Book analytics walkthrough — link below.",
        "keywords": ("project dashboard", "construction data", "analytics"),
    },
    "default": {
        "match": (),
        "topics": ["Construction ops mistake costing you margin", "What top contractors automate first"],
        "hook": "Still running construction ops from spreadsheets?",
        "lines": [
            "Permits, crews, materials, and payments don't belong in fifteen tabs.",
            "{brand} connects the workflow so nothing falls through the cracks.",
            "Built for contractors who scale.",
        ],
        "cta": "See how it works — link in bio.",
        "keywords": ("construction", "contractor", "jobsite"),
    },
}

FUNNEL_STAGES = ("tof", "mof", "bof")

FUNNEL_STAGE_CONFIG: dict[str, dict[str, Any]] = {
    "tof": {
        "label": "Top of funnel — attention",
        "duration_cap": 20,
        "cta_soft": "Follow for more contractor ops tips.",
        "platform": "youtube_shorts",
        "video_type": "viral_hook",
        "line_mode": "short",
    },
    "mof": {
        "label": "Middle of funnel — proof",
        "duration_cap": 45,
        "cta_soft": None,
        "platform": "youtube_shorts",
        "video_type": "demo_walkthrough",
        "line_mode": "full",
    },
    "bof": {
        "label": "Bottom of funnel — conversion",
        "duration_cap": 35,
        "cta_soft": None,
        "platform": "youtube_shorts",
        "video_type": "conversion",
        "line_mode": "proof",
    },
}


def extract_venture_code(name: str) -> str | None:
    match = re.match(r"^(CON-\d+)", name.strip())
    return match.group(1) if match else None


def short_brand(name: str) -> str:
    code = extract_venture_code(name)
    if code:
        return name.replace(code, "").strip() or name
    return name


def pick_playbook(venture_name: str) -> dict[str, Any]:
    lowered = venture_name.lower()
    for key, playbook in TRADE_PLAYBOOKS.items():
        if key == "default":
            continue
        if any(token in lowered for token in playbook["match"]):
            return playbook
    return TRADE_PLAYBOOKS["default"]


def load_campaign_topics() -> dict[str, list[str]]:
    if not CAMPAIGN_JSON.exists():
        return {}
    data = json.loads(CAMPAIGN_JSON.read_text(encoding="utf-8"))
    return {
        key: value.get("video_topics", [])
        for key, value in data.get("content_topics", {}).items()
    }


def load_venture(venture_id: str) -> dict[str, str]:
    with LINKAGE_CSV.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row.get("venture_id", "").strip() == venture_id:
                return {k: (v or "").strip() for k, v in row.items()}
    raise ValueError(f"Venture not found in linkage CSV: {venture_id}")


def pick_topic(playbook: dict[str, Any], venture_code: str | None, campaign_topics: dict[str, list[str]]) -> str:
    if venture_code and venture_code in campaign_topics and campaign_topics[venture_code]:
        return campaign_topics[venture_code][0]
    return playbook["topics"][0]


def adapt_lines_for_funnel(
    funnel_stage: str | None,
    hook: str,
    body_lines: list[str],
    cta: str,
    brand: str,
) -> tuple[str, list[str], str]:
    if not funnel_stage or funnel_stage not in FUNNEL_STAGE_CONFIG:
        return hook, body_lines, cta

    cfg = FUNNEL_STAGE_CONFIG[funnel_stage]
    if funnel_stage == "tof":
        hook = f"You're losing money if you ignore this on every job."
        body_lines = [body_lines[0]] if body_lines else [f"Most contractors miss this until it's too late."]
        cta = cfg["cta_soft"] or cta
    elif funnel_stage == "mof":
        hook = f"Here's how {brand} fixes the problem — in 3 steps."
        body_lines = body_lines[:2] + [f"That's the workflow {brand} runs for active jobs."]
    elif funnel_stage == "bof":
        hook = "Still on the fence? Here's what changes when you switch."
        body_lines = [
            f"Contractors using {brand} cut delays and protect margin.",
            "Clear process. Audit-ready trail. No spreadsheet chaos.",
        ]
        cta = cta if "book" in cta.lower() or "free" in cta.lower() else f"Book a free walkthrough — link below."

    return hook, body_lines, cta


def build_script_package(
    venture: dict[str, str],
    topic: str | None = None,
    funnel_stage: str | None = None,
) -> dict[str, Any]:
    name = venture["venture_name"]
    code = extract_venture_code(name)
    brand = short_brand(name)
    playbook = pick_playbook(name)
    campaign_topics = load_campaign_topics()
    chosen_topic = topic or pick_topic(playbook, code, campaign_topics)

    hook = playbook["hook"]
    body_lines = [line.format(brand=brand) for line in playbook["lines"]]
    cta = playbook["cta"]
    hook, body_lines, cta = adapt_lines_for_funnel(funnel_stage, hook, body_lines, cta, brand)
    spoken_lines = [hook] + body_lines + [cta]
    full_script = " ".join(spoken_lines)
    stage_cfg = FUNNEL_STAGE_CONFIG.get(funnel_stage or "", {})

    scenes = []
    for index, line in enumerate(spoken_lines):
        scenes.append(
            {
                "index": index,
                "text": line,
                "role": "hook" if index == 0 else ("cta" if index == len(spoken_lines) - 1 else "body"),
                "visual_keyword": playbook["keywords"][index % len(playbook["keywords"])],
            }
        )

    slug = re.sub(r"[^a-z0-9]+", "-", chosen_topic.lower()).strip("-")[:48]
    hashtags = ["#construction", "#contractor", "#buildbetter", "#shorts"]
    if code:
        hashtags.insert(0, f"#{code.lower()}")

    return {
        "schema_version": 2,
        "venture_id": venture["venture_id"],
        "venture_code": code,
        "title": brand,
        "topic": chosen_topic,
        "hook": hook,
        "script_lines": spoken_lines,
        "script": full_script,
        "cta": cta,
        "scenes": scenes,
        "funnel_stage": funnel_stage or "mof",
        "duration_target_sec": max(
            15,
            min(stage_cfg.get("duration_cap", 45), len(full_script.split()) // 2),
        ),
        "music_type": "professional",
        "subtitle_style": "burned_in",
        "video_type": stage_cfg.get("video_type", "promotional"),
        "target_platform": stage_cfg.get("platform", "youtube_shorts"),
        "quality": "1080p",
        "publish": {
            "youtube_title": f"{chosen_topic} | {brand}"[:95],
            "youtube_description": (
                f"{chosen_topic}\n\n{full_script}\n\n{' '.join(hashtags[:6])}"
            ),
            "hashtags": hashtags,
            "thumbnail_text": chosen_topic[:40],
        },
        "created_at": datetime.now().isoformat(),
    }


def write_metadata(
    venture_id: str,
    topic: str | None = None,
    funnel_stage: str | None = None,
    output_name: str = "metadata.json",
) -> Path:
    venture = load_venture(venture_id)
    package = build_script_package(venture, topic=topic, funnel_stage=funnel_stage)
    out_dir = OUTPUT_DIR / venture_id
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / output_name
    path.write_text(json.dumps(package, indent=2), encoding="utf-8")
    return path


def regenerate_all_construction(limit: int | None = None) -> list[Path]:
    paths: list[Path] = []
    with LINKAGE_CSV.open(encoding="utf-8") as handle:
        rows = [row for row in csv.DictReader(handle) if row.get("sector", "").lower() == "con"]
    if limit:
        rows = rows[:limit]
    for row in rows:
        vid = row["venture_id"].strip()
        paths.append(write_metadata(vid, topic=None))
    return paths


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Generate venture video scripts")
    parser.add_argument("--venture", help="Venture UUID")
    parser.add_argument("--all-con", action="store_true", help="Regenerate all construction ventures")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--topic", help="Override topic string")
    parser.add_argument(
        "--funnel-stage",
        choices=list(FUNNEL_STAGES),
        help="Adapt script for tof, mof, or bof",
    )
    args = parser.parse_args()

    if args.all_con:
        paths = regenerate_all_construction(limit=args.limit)
        print(f"✅ Regenerated {len(paths)} metadata files")
        return

    if not args.venture:
        parser.error("Provide --venture UUID or --all-con")

    path = write_metadata(args.venture, topic=args.topic, funnel_stage=args.funnel_stage)
    meta = json.loads(path.read_text(encoding="utf-8"))
    print(f"✅ {path}")
    print(f"   Stage: {meta.get('funnel_stage', 'mof')}")
    print(f"   Topic: {meta['topic']}")
    print(f"   Hook: {meta['hook']}")
    for line in meta["script_lines"]:
        print(f"   • {line}")


if __name__ == "__main__":
    main()
