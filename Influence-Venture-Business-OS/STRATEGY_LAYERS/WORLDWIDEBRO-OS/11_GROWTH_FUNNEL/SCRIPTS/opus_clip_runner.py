#!/usr/bin/env python3
"""
Fragment long-form MOF videos into short clips for distribution.

Modes:
  - local (default): FFmpeg segmenter — no API key required
  - api: Opus Clip API when OPUS_API_KEY + public videoUrl are set

Queues each clip in content_brain publish_queue as ready_for_review.
"""

from __future__ import annotations

import json
import math
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

FUNNEL_ROOT = Path("/Users/acebless/Documents/WORLDWIDEBRO-OS/11_GROWTH_FUNNEL")
OUTPUT_DIR = Path("/Users/acebless/Documents/moneyprinter-output")
sys.path.insert(0, str(FUNNEL_ROOT / "SCRIPTS"))

from content_brain import ContentBrain  # noqa: E402

OPUS_API_BASE = "https://api.opus.pro/api"


def probe_duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        return float(result.stdout.strip())
    except ValueError:
        return 0.0


def segment_local(
    source: Path,
    out_dir: Path,
    segment_sec: float = 30.0,
    max_clips: int = 12,
) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    duration = probe_duration(source)
    if duration <= 0:
        raise RuntimeError(f"Cannot probe duration: {source}")

    count = min(max_clips, max(1, int(math.floor(duration / segment_sec))))
    clips: list[Path] = []

    for index in range(count):
        start = index * segment_sec
        if start >= duration - 1:
            break
        dest = out_dir / f"clip_{index + 1:02d}.mp4"
        cmd = [
            "ffmpeg",
            "-y",
            "-ss",
            f"{start:.2f}",
            "-i",
            str(source),
            "-t",
            f"{segment_sec:.2f}",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            str(dest),
        ]
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        if dest.exists() and dest.stat().st_size > 1000:
            clips.append(dest)

    return clips


def opus_api_create_project(video_url: str, webhook_url: str | None = None) -> dict[str, Any]:
    api_key = os.environ.get("OPUS_API_KEY", "")
    org_id = os.environ.get("OPUS_ORG_ID", "")
    if not api_key:
        raise RuntimeError("OPUS_API_KEY not set")

    body: dict[str, Any] = {
        "videoUrl": video_url,
        "curationPref": {
            "clipDurations": [[0, 60]],
            "genre": "Auto",
            "skipCurate": False,
        },
        "importPref": {"sourceLang": "en"},
    }
    if webhook_url:
        body["conclusionActions"] = [{"type": "WEBHOOK", "notifyFailure": True, "url": webhook_url}]

    data = json.dumps(body).encode()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    if org_id:
        headers["x-opus-org-id"] = org_id

    req = urllib.request.Request(f"{OPUS_API_BASE}/clip-projects", data=data, method="POST", headers=headers)
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode())


def opus_api_fetch_clips(project_id: str) -> list[dict[str, Any]]:
    api_key = os.environ.get("OPUS_API_KEY", "")
    org_id = os.environ.get("OPUS_ORG_ID", "")
    url = f"{OPUS_API_BASE}/exportable-clips?q=findByProjectId&projectId={project_id}"
    headers = {"Authorization": f"Bearer {api_key}"}
    if org_id:
        headers["x-opus-org-id"] = org_id
    req = urllib.request.Request(url, method="GET", headers=headers)
    with urllib.request.urlopen(req, timeout=120) as resp:
        payload = json.loads(resp.read().decode())
        if isinstance(payload, list):
            return payload
        return payload.get("clips") or payload.get("data") or []


def queue_clips(
    brain: ContentBrain,
    venture_id: str,
    funnel_stage: str,
    clips: list[dict[str, Any]],
) -> int:
    count = 0
    for clip in clips:
        brain.queue_publish(
            venture_id,
            funnel_stage,
            clip,
            platform=clip.get("platform", "youtube_shorts"),
        )
        count += 1
    return count


def run_opus_pipeline(
    venture_id: str,
    *,
    source_path: Path | None = None,
    video_url: str | None = None,
    funnel_stage: str = "mof",
    segment_sec: float = 30.0,
    max_clips: int = 12,
    mode: str = "auto",
) -> dict[str, Any]:
    venture_dir = OUTPUT_DIR / venture_id
    source = source_path or (venture_dir / "output.mp4")
    if not source.exists():
        raise FileNotFoundError(f"No source video: {source}")

    brain = ContentBrain()
    meta_path = venture_dir / f"metadata_{funnel_stage}.json"
    if not meta_path.exists():
        meta_path = venture_dir / "metadata.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    hook = meta.get("hook", "")

    public_url = video_url or os.environ.get("OPUS_VIDEO_URL", "")
    use_api = mode == "api" or (mode == "auto" and os.environ.get("OPUS_API_KEY") and public_url)

    if use_api:
        project = opus_api_create_project(public_url, os.environ.get("OPUS_WEBHOOK_URL"))
        project_id = project.get("id") or project.get("projectId") or project.get("data", {}).get("id")
        if not project_id:
            project_id = re.search(r'"projectId"\s*:\s*"([^"]+)"', json.dumps(project))
            project_id = project_id.group(1) if project_id else None
        manifest = venture_dir / "work" / "opus_project.json"
        manifest.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_text(json.dumps(project, indent=2), encoding="utf-8")
        return {
            "mode": "api",
            "status": "submitted",
            "project_id": project_id,
            "manifest": str(manifest),
            "note": "Poll with: opus_clip_runner.py --venture-id ... --fetch-project PROJECT_ID",
        }

    clips_dir = venture_dir / "work" / "clips"
    paths = segment_local(source, clips_dir, segment_sec=segment_sec, max_clips=max_clips)
    clip_rows: list[dict[str, Any]] = []
    for index, path in enumerate(paths, start=1):
        clip_rows.append(
            {
                "clip_index": index,
                "path": str(path),
                "hook": hook,
                "parent_video": str(source),
                "funnel_stage": funnel_stage,
                "platform": "youtube_shorts",
                "source": "ffmpeg-segment",
                "duration_sec": segment_sec,
            }
        )

    queued = queue_clips(brain, venture_id, funnel_stage, clip_rows)
    manifest = clips_dir / "manifest.json"
    manifest.write_text(json.dumps({"clips": clip_rows, "queued": queued}, indent=2), encoding="utf-8")

    return {
        "mode": "local",
        "status": "ok",
        "clip_count": len(paths),
        "queued": queued,
        "clips_dir": str(clips_dir),
        "manifest": str(manifest),
    }


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Opus Clip runner (local FFmpeg or Opus API)")
    parser.add_argument("--venture-id", required=True)
    parser.add_argument("--stage", default="mof", choices=["tof", "mof", "bof"])
    parser.add_argument("--source", type=Path, help="Override source MP4")
    parser.add_argument("--video-url", help="Public URL for Opus API mode")
    parser.add_argument("--mode", default="auto", choices=["auto", "local", "api"])
    parser.add_argument("--segment-sec", type=float, default=30.0)
    parser.add_argument("--max-clips", type=int, default=12)
    parser.add_argument("--fetch-project", help="Fetch Opus API clips for project id and queue")
    args = parser.parse_args()

    if args.fetch_project:
        clips = opus_api_fetch_clips(args.fetch_project)
        brain = ContentBrain()
        rows = [
            {
                "opus_project_id": args.fetch_project,
                "clip_id": c.get("id"),
                "url": c.get("url") or c.get("downloadUrl"),
                "title": c.get("title"),
                "platform": "youtube_shorts",
                "source": "opus-api",
            }
            for c in clips
        ]
        queued = queue_clips(brain, args.venture_id, args.stage, rows)
        print(json.dumps({"status": "ok", "fetched": len(clips), "queued": queued}, indent=2))
        return

    result = run_opus_pipeline(
        args.venture_id,
        source_path=args.source,
        video_url=args.video_url,
        funnel_stage=args.stage,
        segment_sec=args.segment_sec,
        max_clips=args.max_clips,
        mode=args.mode,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
