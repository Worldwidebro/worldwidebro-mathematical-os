#!/usr/bin/env python3
"""
Master Orchestrator — single control layer for the Venture Media Factory.

Coordinates: content brain → funnel strategy → script/video production →
optional Higgsfield visuals → publish queue → n8n/Supabase.

Usage:
  python3 MASTER_ORCHESTRATOR.py run --venture-id UUID
  python3 MASTER_ORCHESTRATOR.py run --auto
  python3 MASTER_ORCHESTRATOR.py run --batch
  python3 MASTER_ORCHESTRATOR.py status
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

FUNNEL_ROOT = Path(__file__).resolve().parent
SCRIPTS = FUNNEL_ROOT / "SCRIPTS"
DOCS = Path("/Users/acebless/Documents")
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(DOCS))

from content_brain import ContentBrain  # noqa: E402
from venture_script_engine import FUNNEL_STAGES, load_venture  # noqa: E402

CONFIG_PATH = FUNNEL_ROOT / "REGISTRY/orchestrator-config.json"
STATE_PATH = FUNNEL_ROOT / "DATA/orchestrator_state.json"
RUNS_LOG = FUNNEL_ROOT / "DATA/orchestrator_runs.jsonl"

WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


@dataclass
class RunPlan:
    venture_id: str
    venture_code: str | None
    goal: str
    funnel_stage: str | None
    render: bool
    higgsfield: bool
    opus_clip: bool
    steps: list[str] = field(default_factory=list)


@dataclass
class RunResult:
    plan: RunPlan
    ok: bool
    started_at: str
    finished_at: str
    outputs: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def today_name() -> str:
    return WEEKDAYS[datetime.now().weekday()]


def load_batch(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))["ventures"]


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return {"round_robin_index": 0, "last_runs": {}}


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2), encoding="utf-8")


def pick_venture(cfg: dict, venture_id: str | None) -> dict:
    batch = load_batch(Path(cfg["paths"]["venture_batch"]))
    if venture_id:
        for v in batch:
            if v["venture_id"] == venture_id:
                return v
        venture = load_venture(venture_id)
        return {
            "venture_id": venture_id,
            "venture_code": venture.get("venture_name", "")[:8],
            "venture_name": venture["venture_name"],
        }
    state = load_state()
    idx = state.get("round_robin_index", 0) % len(batch)
    state["round_robin_index"] = (idx + 1) % len(batch)
    save_state(state)
    return batch[idx]


def resolve_goal_and_stage(cfg: dict, goal: str | None) -> tuple[str, str | None]:
    day = today_name()
    if goal in ("weekly", "batch", "status", "full_cycle", "produce"):
        return goal, None
    if goal == "auto" or goal is None:
        mapped = cfg["funnel_stage_by_weekday"].get(day, "tof")
        if mapped in ("analytics", "prep"):
            return "weekly", mapped
        return "produce", mapped
    if goal in FUNNEL_STAGES:
        return "produce", goal
    return goal, cfg["funnel_stage_by_weekday"].get(day, "tof")


def run_python(script: Path, args: list[str], dry_run: bool = False) -> tuple[int, str]:
    cmd = ["python3", str(script), *args]
    if dry_run:
        return 0, " ".join(cmd)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    out = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode, out


def run_shell(cmd: list[str], dry_run: bool = False) -> tuple[int, str]:
    if dry_run:
        return 0, " ".join(cmd)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    out = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode, out


def higgsfield_available(cfg: dict) -> bool:
    if os.environ.get(cfg["higgsfield"]["enabled_env"], "").lower() in ("1", "true", "yes"):
        return True
    cli = cfg["higgsfield"]["cli"]
    proc = subprocess.run(["which", cli], capture_output=True)
    return proc.returncode == 0


def generate_higgsfield_scenes(
    cfg: dict,
    venture_id: str,
    meta_path: Path,
    dry_run: bool,
) -> dict[str, Any]:
    from higgsfield_scenes import generate_scenes_for_metadata  # noqa: WPS433

    out_dir = Path(cfg["paths"]["output_dir"]) / venture_id / "work" / "higgsfield"
    hf_cfg = cfg["higgsfield"]
    return generate_scenes_for_metadata(
        meta_path,
        out_dir,
        cli=hf_cfg["cli"],
        model=hf_cfg["scene_model_image"],
        aspect_ratio=hf_cfg["aspect_ratio"],
        dry_run=dry_run,
    )


def notify_n8n(cfg: dict, endpoint: str, body: dict, dry_run: bool) -> None:
    if not cfg["defaults"].get("notify_n8n") and not os.environ.get("ORCHESTRATOR_NOTIFY_N8N"):
        return
    base = cfg["n8n"]["webhook_base"].rstrip("/")
    url = base + cfg["n8n"]["endpoints"].get(endpoint, f"/{endpoint}")
    secret = os.environ.get(cfg["n8n"]["secret_env"], "")
    data = json.dumps(body).encode()
    headers = {"Content-Type": "application/json"}
    if secret:
        headers["X-Funnel-Secret"] = secret
    if dry_run:
        return
    req = urllib.request.Request(url, data=data, method="POST", headers=headers)
    try:
        urllib.request.urlopen(req, timeout=60)
    except urllib.error.URLError as exc:
        raise RuntimeError(f"n8n notify failed: {exc}") from exc


def append_run_log(result: RunResult) -> None:
    RUNS_LOG.parent.mkdir(parents=True, exist_ok=True)
    line = {
        "venture_id": result.plan.venture_id,
        "goal": result.plan.goal,
        "funnel_stage": result.plan.funnel_stage,
        "ok": result.ok,
        "started_at": result.started_at,
        "finished_at": result.finished_at,
        "outputs": result.outputs,
        "errors": result.errors,
    }
    with RUNS_LOG.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(line) + "\n")


def execute_plan(plan: RunPlan, cfg: dict, dry_run: bool = False) -> RunResult:
    started = datetime.now().isoformat()
    outputs: dict[str, Any] = {}
    errors: list[str] = []
    brain = ContentBrain()
    vid = plan.venture_id

    try:
        venture = load_venture(vid)
        brain.upsert_venture(vid, plan.venture_code, venture["venture_name"], venture.get("sector", ""))

        if plan.goal == "batch":
            code, out = run_python(SCRIPTS / "batch_weekly_all_ventures.py", [], dry_run)
            outputs["batch"] = out
            if code != 0:
                errors.append("batch_weekly_all_ventures failed")
            notify_n8n(cfg, "batch", {}, dry_run)

        elif plan.goal == "weekly":
            day = plan.funnel_stage or today_name()
            if day in ("analytics", "prep"):
                day_arg = "saturday" if day == "analytics" else "sunday"
            else:
                day_arg = day if day in WEEKDAYS else today_name()
            args = ["--venture-id", vid, "--day", day_arg]
            if plan.render:
                args.append("--render")
            code, out = run_python(SCRIPTS / "weekly_funnel_runner.py", args, dry_run)
            outputs["weekly"] = out
            if code != 0:
                errors.append("weekly_funnel_runner failed")
            notify_n8n(cfg, "weekly", {"venture_id": vid, "day": day_arg, "render": plan.render}, dry_run)

        elif plan.goal in ("produce", "full_cycle"):
            stage = plan.funnel_stage or "mof"
            plan.steps.append(f"generate_funnel_content:{stage}")
            code, out = run_python(
                SCRIPTS / "generate_funnel_content.py",
                ["--venture-id", vid, "--stages", stage],
                dry_run,
            )
            outputs["generate"] = out
            if code != 0:
                errors.append("generate_funnel_content failed")

            meta_name = f"metadata_{stage}.json"
            meta_path = Path(cfg["paths"]["output_dir"]) / vid / meta_name
            outputs["metadata"] = str(meta_path)

            if plan.higgsfield and higgsfield_available(cfg):
                plan.steps.append("higgsfield_scenes")
                outputs["higgsfield"] = generate_higgsfield_scenes(cfg, vid, meta_path, dry_run)
            elif plan.higgsfield:
                outputs["higgsfield"] = "skipped (CLI not available; set HIGGSFIELD_ENABLED=1)"

            if plan.render or plan.goal == "full_cycle":
                plan.steps.append("render_video")
                default_meta = Path(cfg["paths"]["output_dir"]) / vid / "metadata.json"
                if not dry_run and meta_path.exists():
                    default_meta.write_text(meta_path.read_text(encoding="utf-8"), encoding="utf-8")
                env = os.environ.copy()
                if plan.higgsfield:
                    env["USE_HIGGSFIELD"] = "1"
                cmd = ["bash", str(DOCS / "run_venture_video_pipeline.sh"), vid, "single"]
                if dry_run:
                    code, out = 0, " ".join(cmd)
                else:
                    proc = subprocess.run(cmd, capture_output=True, text=True, env=env)
                    code, out = proc.returncode, (proc.stdout or "") + (proc.stderr or "")
                outputs["video"] = out
                outputs["mp4"] = str(Path(cfg["paths"]["output_dir"]) / vid / "output.mp4")
                if code != 0:
                    errors.append("video pipeline failed")

            run_opus = plan.opus_clip or (
                (plan.render or plan.goal == "full_cycle")
                and stage == "mof"
                and (cfg["defaults"].get("opus_clip_after_render") or os.environ.get("OPUS_CLIP_AFTER_RENDER"))
            )
            if run_opus and not dry_run:
                mp4 = Path(cfg["paths"]["output_dir"]) / vid / "output.mp4"
                if mp4.exists():
                    plan.steps.append("opus_clip_fragment")
                    code, out = run_python(
                        SCRIPTS / "opus_clip_runner.py",
                        ["--venture-id", vid, "--stage", stage, "--mode", "auto"],
                        dry_run=False,
                    )
                    outputs["opus"] = out
                    if code != 0:
                        errors.append("opus_clip_runner failed")
                else:
                    outputs["opus"] = "skipped (no output.mp4)"

            if not dry_run:
                meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
                brain.queue_publish(
                    vid,
                    stage,
                    {"metadata_file": meta_name, "hook": meta.get("hook"), "goal": plan.goal},
                )
                brain.insert_asset(
                    vid,
                    stage,
                    "script_json",
                    meta.get("hook"),
                    meta.get("script"),
                    today_name(),
                    script_json=meta,
                    status="queued",
                )

            if cfg["defaults"].get("sync_supabase_after_run") or os.environ.get("SYNC_SUPABASE_AFTER_RUN"):
                code, out = run_python(SCRIPTS / "sync_sqlite_to_supabase.py", [], dry_run)
                outputs["supabase_sync"] = out

            notify_n8n(
                cfg,
                "weekly",
                {"venture_id": vid, "day": today_name(), "render": plan.render, "stage": stage},
                dry_run,
            )

        else:
            errors.append(f"unknown goal: {plan.goal}")

    except Exception as exc:  # noqa: BLE001
        errors.append(str(exc))

    finished = datetime.now().isoformat()
    result = RunResult(
        plan=plan,
        ok=len(errors) == 0,
        started_at=started,
        finished_at=finished,
        outputs=outputs,
        errors=errors,
    )
    if not dry_run:
        append_run_log(result)
        state = load_state()
        state.setdefault("last_runs", {})[vid] = {"at": finished, "goal": plan.goal, "ok": result.ok}
        save_state(state)
    return result


def cmd_status(cfg: dict) -> None:
    state = load_state()
    brain = ContentBrain()
    print("Venture Media Factory — status")
    print(f"  Content brain: {brain.backend_label()}")
    print(f"  Round-robin index: {state.get('round_robin_index', 0)}")
    print(f"  Today: {today_name()} → stage {cfg['funnel_stage_by_weekday'].get(today_name())}")
    print(f"  Higgsfield CLI: {'yes' if higgsfield_available(cfg) else 'no'}")
    print(f"  Opus API: {'yes' if os.environ.get('OPUS_API_KEY') else 'local ffmpeg only'}")
    print(f"  Supabase: {'configured' if os.environ.get('SUPABASE_URL') else 'sqlite only'}")
    print(f"  Runs log: {RUNS_LOG}")
    if RUNS_LOG.exists():
        lines = RUNS_LOG.read_text(encoding="utf-8").strip().split("\n")
        print(f"  Recent runs: {len(lines)}")
        for line in lines[-3:]:
            rec = json.loads(line)
            print(f"    • {rec['venture_id'][:8]}… {rec['goal']} ok={rec['ok']}")


def cmd_run(args: argparse.Namespace, cfg: dict) -> int:
    if args.batch:
        plan = RunPlan(
            venture_id="batch",
            venture_code=None,
            goal="batch",
            funnel_stage=None,
            render=args.render,
            higgsfield=args.higgsfield,
            opus_clip=args.opus_clip,
        )
        result = execute_plan(plan, cfg, dry_run=args.dry_run)
    else:
        venture = pick_venture(cfg, None if args.auto else args.venture_id)
        goal, stage = resolve_goal_and_stage(cfg, args.goal)
        if args.stage:
            stage = args.stage
            goal = "produce"
        plan = RunPlan(
            venture_id=venture["venture_id"],
            venture_code=venture.get("venture_code"),
            goal=goal,
            funnel_stage=stage,
            render=args.render or cfg["defaults"]["render_video"],
            higgsfield=args.higgsfield or cfg["defaults"]["higgsfield_scenes"],
            opus_clip=args.opus_clip or cfg["defaults"].get("opus_clip_after_render", False),
        )
        result = execute_plan(plan, cfg, dry_run=args.dry_run)

    print(f"\n{'✅' if result.ok else '❌'} Orchestrator run complete")
    print(f"   Venture: {result.plan.venture_id}")
    print(f"   Goal: {result.plan.goal}  Stage: {result.plan.funnel_stage}")
    for step in result.plan.steps:
        print(f"   → {step}")
    for key, val in result.outputs.items():
        if isinstance(val, str) and len(val) > 200:
            val = val[:200] + "…"
        print(f"   {key}: {val}")
    for err in result.errors:
        print(f"   ERROR: {err}")
    return 0 if result.ok else 1


def main() -> None:
    parser = argparse.ArgumentParser(description="Master orchestrator for Venture Media Factory")
    sub = parser.add_subparsers(dest="command", required=True)

    run_p = sub.add_parser("run", help="Execute one orchestrated cycle")
    run_p.add_argument("--venture-id", help="Target venture UUID")
    run_p.add_argument("--auto", action="store_true", help="Auto-pick venture (round-robin) + today's goal")
    run_p.add_argument("--batch", action="store_true", help="Run full batch for all ventures in registry")
    run_p.add_argument("--goal", help="produce|full_cycle|weekly|batch|auto|tof|mof|bof")
    run_p.add_argument("--stage", choices=list(FUNNEL_STAGES), help="Override funnel stage")
    run_p.add_argument("--render", action="store_true", help="Run FFmpeg video pipeline")
    run_p.add_argument("--higgsfield", action="store_true", help="Generate Higgsfield scene visuals")
    run_p.add_argument("--opus-clip", action="store_true", help="Fragment MOF video into shorts (FFmpeg or Opus API)")
    run_p.add_argument("--dry-run", action="store_true")

    sub.add_parser("status", help="Show factory status")

    args = parser.parse_args()
    cfg = load_config()

    if args.command == "status":
        cmd_status(cfg)
        raise SystemExit(0)
    if args.command == "run":
        if not args.venture_id and not args.auto and not args.batch:
            print("Provide --venture-id, --auto, or --batch")
            raise SystemExit(2)
        raise SystemExit(cmd_run(args, cfg))


if __name__ == "__main__":
    main()
