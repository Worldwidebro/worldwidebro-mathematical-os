#!/usr/bin/env python3
"""
run_repo_intelligence_pipeline.py — the harmony chain.

Runs the whole Repository-Intelligence toolchain in dependency order, so the tools
work together instead of being run by hand one at a time. Each stage produces an
artifact the next stage consumes:

    STAGE 1  scan_repositories.py            -> REPOSITORY-REGISTRY.json   (stars/forks/lang)
    STAGE 2  repo_classification_phase2.py   -> strategic/revenue/reuse scores in registry
    STAGE 3  build_repo_summaries.py         -> repo-summaries.json
    STAGE 4  build_capability_catalog.py     -> capabilities-catalog.json
    STAGE 5  build_used_by_ventures.py       -> repo-used-by-ventures.json
    STAGE 6  build_execution_readiness.py    -> execution-readiness.csv
    STAGE 7  build_repo_intelligence_score.py-> repo-intelligence-scores.json + leaderboard.csv
    STAGE 8  build_department_view.py        -> repo-department-view.json + DEPARTMENT-VIEW.md

STAGE 1 (and STAGE 6) hit the GitHub API and are slow; use flags to skip them when the
registry / readiness data is already fresh and you only want to re-derive downstream scores.

Usage:
    python3 run_repo_intelligence_pipeline.py               # full chain
    python3 run_repo_intelligence_pipeline.py --skip-scan   # reuse existing registry (fast)
    python3 run_repo_intelligence_pipeline.py --skip-scan --skip-readiness   # scores only
    python3 run_repo_intelligence_pipeline.py --from 7      # only run stages >= 7
    python3 run_repo_intelligence_pipeline.py --dry-run     # print the plan, run nothing
"""
import argparse
import subprocess
import sys
import time
from datetime import datetime

DOCS = "/Users/acebless/Documents"

# (stage_no, label, argv, produces, network_bound)
STAGES = [
    (1, "Scan repositories (GitHub API)", ["scan_repositories.py"],
     "REPOSITORY-REGISTRY.json", True),
    (2, "Classify (strategic/revenue/reuse)", ["repo_classification_phase2.py"],
     "REPOSITORY-REGISTRY.json (enriched)", False),
    (3, "Repo summaries", ["build_repo_summaries.py"],
     "repo-summaries.json", False),
    (4, "Capability catalog", ["build_capability_catalog.py"],
     "capabilities-catalog.json", False),
    (5, "Used-by-ventures join", ["build_used_by_ventures.py"],
     "repo-used-by-ventures.json", False),
    (6, "Execution readiness (GitHub API)", ["build_execution_readiness.py"],
     "execution-readiness.csv", True),
    (7, "Unified intelligence score", ["build_repo_intelligence_score.py"],
     "repo-intelligence-scores.json + leaderboard.csv", False),
    (8, "Department view", ["build_department_view.py"],
     "repo-department-view.json + DEPARTMENT-VIEW.md", False),
]


def run_stage(stage_no, label, argv, dry_run):
    print(f"\n{'─' * 78}")
    print(f"STAGE {stage_no}: {label}")
    print(f"  $ python3 {' '.join(argv)}")
    print("─" * 78)
    if dry_run:
        print("  [dry-run] skipped")
        return True, 0.0
    start = time.time()
    proc = subprocess.run([sys.executable, *argv], cwd=DOCS)
    elapsed = time.time() - start
    ok = proc.returncode == 0
    status = "✅ ok" if ok else f"❌ FAILED (exit {proc.returncode})"
    print(f"  {status} in {elapsed:.1f}s")
    return ok, elapsed


def main():
    ap = argparse.ArgumentParser(description="Chain the Repository-Intelligence pipeline.")
    ap.add_argument("--skip-scan", action="store_true",
                    help="skip STAGE 1 (reuse existing REPOSITORY-REGISTRY.json)")
    ap.add_argument("--skip-readiness", action="store_true",
                    help="skip STAGE 6 (reuse existing execution-readiness.csv)")
    ap.add_argument("--skip-network", action="store_true",
                    help="skip ALL GitHub-API stages (1 and 6)")
    ap.add_argument("--from", dest="from_stage", type=int, default=1,
                    help="only run stages with number >= this")
    ap.add_argument("--dry-run", action="store_true", help="print the plan, run nothing")
    a = ap.parse_args()

    print("=" * 78)
    print("REPOSITORY INTELLIGENCE PIPELINE")
    print(f"  started {datetime.now().isoformat(timespec='seconds')}")
    print("=" * 78)

    skip = set()
    if a.skip_scan or a.skip_network:
        skip.add(1)
    if a.skip_readiness or a.skip_network:
        skip.add(6)

    results = []
    total_elapsed = 0.0
    for stage_no, label, argv, produces, _net in STAGES:
        if stage_no < a.from_stage:
            print(f"\nSTAGE {stage_no}: {label}  —  skipped (< --from {a.from_stage})")
            results.append((stage_no, label, "skipped", 0.0))
            continue
        if stage_no in skip:
            print(f"\nSTAGE {stage_no}: {label}  —  skipped (flag)")
            results.append((stage_no, label, "skipped", 0.0))
            continue

        ok, elapsed = run_stage(stage_no, label, argv, a.dry_run)
        total_elapsed += elapsed
        results.append((stage_no, label, "ok" if ok else "FAILED", elapsed))
        if not ok:
            print(f"\n❌ Pipeline halted at STAGE {stage_no} — downstream stages depend on "
                  f"'{produces}'. Fix the error above and re-run "
                  f"(tip: --from {stage_no} resumes here).")
            _print_summary(results, total_elapsed, halted=True)
            sys.exit(1)

    _print_summary(results, total_elapsed, halted=False)


def _print_summary(results, total_elapsed, halted):
    print("\n" + "=" * 78)
    print("PIPELINE SUMMARY")
    print("=" * 78)
    for stage_no, label, status, elapsed in results:
        mark = {"ok": "✅", "FAILED": "❌", "skipped": "⏭ "}.get(status, "  ")
        t = f"{elapsed:5.1f}s" if elapsed else "     -"
        print(f"  {mark} STAGE {stage_no}: {label:42s} {t}")
    print("-" * 78)
    print(f"  total: {total_elapsed:.1f}s | {'HALTED' if halted else 'COMPLETE'}")
    if not halted:
        print("\n  Artifacts refreshed:")
        print("    repo-intelligence-scores.json / repo-intelligence-leaderboard.csv")
        print("    repo-department-view.json / DEPARTMENT-VIEW.md")
    print("=" * 78)


if __name__ == "__main__":
    main()
