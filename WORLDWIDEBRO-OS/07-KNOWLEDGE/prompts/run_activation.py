#!/usr/bin/env python3
"""
List and optionally run WORLDWIDEBRO-OS activation prompts by phase.

Usage:
  python3 run_activation.py --list
  python3 run_activation.py --phase 1
  python3 run_activation.py --phase 5 --dry-run

Note: This script lists prompts and target outputs. Actual generation requires
an agent session (Cursor) with the prompt body + listed inputs.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
PHASE_MAP = {
    1: [
        "00-DIRECTIVES/prompts/MISSION_VISION_VALUES.prompt.md",
        "00-DIRECTIVES/prompts/OPERATING_PRINCIPLES.prompt.md",
        "00-DIRECTIVES/prompts/NORTH_STAR_METRICS.prompt.md",
    ],
    2: [
        "00-DIRECTIVES/prompts/DATA_GOVERNANCE_DIRECTIVE.prompt.md",
        "00-DIRECTIVES/prompts/DECISION_FRAMEWORK.prompt.md",
        "00-DIRECTIVES/prompts/CAPITAL_ALLOCATION_DIRECTIVE.prompt.md",
        "00-DIRECTIVES/prompts/AGENT_CREATION_DIRECTIVE.prompt.md",
    ],
    3: [
        "01-EXECUTIVES/prompts/CEO_MANDATE.prompt.md",
        "05-AGENTS/templates/AGENT_TEMPLATE.prompt.md",
        "05-AGENTS/executive/CFO_AGENT.prompt.md",
        "05-AGENTS/opco/OPCO_PRESIDENT.prompt.md",
        "03-PORTFOLIO/prompts/VENTURE_PROFILE_TEMPLATE.prompt.md",
        "04-OPERATIONS/prompts/SOP_TEMPLATE.prompt.md",
        "05-AGENTS/venture/VENTURE_MEDICAL_COURIER.prompt.md",
        "05-AGENTS/venture/VENTURE_AI_AGENCY.prompt.md",
        "05-AGENTS/venture/VENTURE_STAFFING.prompt.md",
    ],
    4: [
        "07-KNOWLEDGE/prompts/KNOWLEDGE_GRAPH_MEMORY.prompt.md",
        "REGISTRIES/prompts/REPOSITORY_INDEX.prompt.md",
        "08-DATA/prompts/PORTFOLIO_STATUS.prompt.md",
        "10-STATUS/prompts/HOLDINGS_STATUS.prompt.md",
        "09-DASHBOARDS/prompts/CEO_PULSE_DASHBOARD.prompt.md",
        "06-TECHNOLOGY/prompts/STACK_INTEGRATION.prompt.md",
    ],
    5: [
        "05-AGENTS/orchestration/META_CONTROLLER.prompt.md",
        "05-AGENTS/orchestration/ROUTING_ENGINE.prompt.md",
        "05-AGENTS/orchestration/ESCALATION_POLICY.prompt.md",
        "00-COMMAND/prompts/EXECUTIVE_BRIEFING.prompt.md",
        "00-COMMAND/prompts/CURRENT_PRIORITIES.prompt.md",
        "00-COMMAND/prompts/DECISION_LOG.prompt.md",
    ],
}


def find_all_prompts() -> list[Path]:
    return sorted(ROOT.rglob("*.prompt.md"))


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    meta: dict[str, str] = {}
    if text.startswith("---"):
        end = text.find("---", 3)
        if end > 0:
            block = text[3:end]
            for line in block.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip()
    return meta


def main() -> None:
    parser = argparse.ArgumentParser(description="WORLDWIDEBRO-OS activation prompt runner")
    parser.add_argument("--list", action="store_true", help="List all prompt files")
    parser.add_argument("--phase", type=int, choices=[1, 2, 3, 4, 5], help="Show prompts for phase")
    parser.add_argument("--dry-run", action="store_true", help="Print paths only")
    args = parser.parse_args()

    if args.list:
        for p in find_all_prompts():
            rel = p.relative_to(ROOT)
            meta = parse_frontmatter(p)
            print(f"{rel}\t{meta.get('id', '?')}\tphase={meta.get('phase', '?')}")
        return

    if args.phase:
        paths = [ROOT / rel for rel in PHASE_MAP[args.phase]]
        print(f"Phase {args.phase} — {len(paths)} prompts:\n")
        for p in paths:
            if not p.exists():
                print(f"  MISSING {p.relative_to(ROOT)}")
                continue
            meta = parse_frontmatter(p)
            print(f"  [{meta.get('id', p.stem)}]")
            print(f"    path: {p.relative_to(ROOT)}")
            if args.dry_run:
                print(f"    agent: {meta.get('agent_role', 'n/a')}")
                print(f"    outputs: {meta.get('outputs', 'n/a')}")
            print()
        print("Run each prompt in Cursor with listed inputs to generate output artifacts.")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
