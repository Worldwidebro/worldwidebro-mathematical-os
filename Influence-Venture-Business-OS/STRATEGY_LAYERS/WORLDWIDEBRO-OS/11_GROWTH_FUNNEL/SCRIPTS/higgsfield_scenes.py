#!/usr/bin/env python3
"""Generate and download Higgsfield scene stills for the video pipeline."""

from __future__ import annotations

import json
import re
import subprocess
import urllib.request
from pathlib import Path
from typing import Any

URL_RE = re.compile(r"https?://[^\s\"')\]}>,]+")


def extract_media_urls(text: str) -> list[str]:
    urls = URL_RE.findall(text)
    cleaned: list[str] = []
    for url in urls:
        url = url.rstrip(".,;")
        if any(ext in url.lower() for ext in (".png", ".jpg", ".jpeg", ".webp", "cdn", "higgsfield", "cloudfront")):
            cleaned.append(url)
    if not cleaned:
        cleaned = [u for u in urls if u.startswith("http")]
    return cleaned


def download_file(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "venture-media-factory/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        dest.write_bytes(resp.read())


def higgsfield_scene_path(work_dir: Path, index: int) -> Path | None:
    hf_dir = work_dir / "higgsfield"
    for name in (f"scene_{index:02d}.png", f"scene_{index}.png"):
        path = hf_dir / name
        if path.exists() and path.stat().st_size > 1000:
            return path
    return None


def generate_scenes_for_metadata(
    meta_path: Path,
    out_dir: Path,
    cli: str = "higgsfield",
    model: str = "nano_banana_2",
    aspect_ratio: str = "9:16",
    dry_run: bool = False,
) -> dict[str, Any]:
    """Create scene_XX.png files under out_dir from metadata scenes."""
    if not meta_path.exists():
        return {"status": "missing_metadata", "scenes": []}

    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    scenes = meta.get("scenes") or []
    out_dir.mkdir(parents=True, exist_ok=True)
    results: list[dict[str, Any]] = []

    for index, scene in enumerate(scenes[:5]):
        dest = out_dir / f"scene_{index:02d}.png"
        if dest.exists() and dest.stat().st_size > 1000:
            results.append({"index": index, "path": str(dest), "source": "cached"})
            continue

        prompt = (
            f"Vertical 9:16 cinematic b-roll still for construction SaaS ad. "
            f"Scene: {scene.get('text', '')}. "
            f"Keyword: {scene.get('visual_keyword', 'jobsite')}. No text overlay."
        )
        if dry_run:
            results.append({"index": index, "prompt": prompt, "source": "dry-run"})
            continue

        cmd = [
            cli,
            "generate",
            "create",
            model,
            "--prompt",
            prompt,
            "--aspect_ratio",
            aspect_ratio,
            "--wait",
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        combined = (proc.stdout or "") + (proc.stderr or "")
        manifest = out_dir / f"scene_{index:02d}.json"
        manifest.write_text(
            json.dumps({"prompt": prompt, "returncode": proc.returncode, "raw": combined[-4000:]}, indent=2),
            encoding="utf-8",
        )

        if proc.returncode != 0:
            results.append({"index": index, "error": combined[-300:], "source": "higgsfield-error"})
            continue

        urls = extract_media_urls(combined)
        if not urls:
            results.append({"index": index, "error": "no URL in CLI output", "source": "higgsfield-error"})
            continue

        try:
            download_file(urls[0], dest)
            results.append({"index": index, "path": str(dest), "url": urls[0], "source": "higgsfield"})
        except Exception as exc:  # noqa: BLE001
            results.append({"index": index, "error": str(exc), "url": urls[0], "source": "download-error"})

    ok = sum(1 for r in results if r.get("path"))
    return {"status": "ok" if ok else "partial", "generated": ok, "scenes": results}


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Generate Higgsfield scene PNGs")
    parser.add_argument("--metadata", required=True, type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    result = generate_scenes_for_metadata(args.metadata, args.out_dir, dry_run=args.dry_run)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
