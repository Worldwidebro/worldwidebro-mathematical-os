#!/usr/bin/env python3
"""Generate venture promo videos from metadata using PIL + FFmpeg (no moviepy)."""

from __future__ import annotations

import json
import shutil
import subprocess
import textwrap
from pathlib import Path

OUTPUT_DIR = Path("/Users/acebless/Documents/moneyprinter-output")
SIZE = (1080, 1920)
BG_COLOR = "#1a1a2e"
TITLE_COLOR = "#ffffff"
SCRIPT_COLOR = "#00ff00"
DURATION_SEC = 30
FONT_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/Library/Fonts/Arial.ttf",
]


def load_font(size: int):
    from PIL import ImageFont

    for path in FONT_CANDIDATES:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default()


def wrap_lines(text: str, width: int = 38) -> list[str]:
    lines: list[str] = []
    for sentence in text.replace("\n", " ").split(". "):
        chunk = sentence.strip()
        if not chunk:
            continue
        if not chunk.endswith("."):
            chunk += "."
        lines.extend(textwrap.wrap(chunk, width=width) or [chunk])
    return lines


def render_frame(title: str, script: str, frame_path: Path) -> None:
    from PIL import Image, ImageDraw

    img = Image.new("RGB", SIZE, color=BG_COLOR)
    draw = ImageDraw.Draw(img)
    title_font = load_font(52)
    script_font = load_font(34)

    draw.text((60, 120), title, fill=TITLE_COLOR, font=title_font)

    y = 320
    for line in wrap_lines(script):
        draw.text((60, y), line, fill=SCRIPT_COLOR, font=script_font)
        y += 52
        if y > SIZE[1] - 120:
            break

    frame_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(frame_path, format="PNG")


def encode_video(frame_path: Path, output_path: Path) -> None:
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("ffmpeg not found on PATH")

    cmd = [
        "ffmpeg",
        "-y",
        "-loop",
        "1",
        "-i",
        str(frame_path),
        "-c:v",
        "libx264",
        "-t",
        str(DURATION_SEC),
        "-pix_fmt",
        "yuv420p",
        "-r",
        "30",
        str(output_path),
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True)


def generate_video_from_metadata(metadata_file: Path, output_file: Path) -> bool:
    metadata = json.loads(metadata_file.read_text(encoding="utf-8"))
    title = metadata.get("title", "Venture Promo")
    script = metadata.get("script", metadata.get("description", ""))

    print(f"🎬 Creating video: {title}")

    frame_path = metadata_file.parent / "_frame.png"
    try:
        render_frame(title, script, frame_path)
        encode_video(frame_path, output_file)

        log = {
            "status": "success",
            "title": title,
            "output": str(output_file),
            "duration_sec": DURATION_SEC,
            "method": "pil+ffmpeg",
        }
        (metadata_file.parent / "generation_log.json").write_text(
            json.dumps(log, indent=2), encoding="utf-8"
        )
        print(f"   ✅ Video saved: {output_file}")
        return True
    except Exception as exc:
        print(f"   ❌ Failed: {exc}")
        (metadata_file.parent / "generation_failed.log").write_text(str(exc), encoding="utf-8")
        return False
    finally:
        if frame_path.exists():
            frame_path.unlink()


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Generate venture promo MP4s")
    parser.add_argument("--venture", help="Venture folder name (UUID) or 'all'")
    args = parser.parse_args()

    metadata_files = sorted(OUTPUT_DIR.glob("*/metadata.json"))
    if args.venture and args.venture != "all":
        metadata_files = [OUTPUT_DIR / args.venture / "metadata.json"]

    if not metadata_files:
        print("⚠️  No metadata files found")
        return

    ok = 0
    for metadata_file in metadata_files:
        if generate_video_from_metadata(metadata_file, metadata_file.parent / "output.mp4"):
            ok += 1

    print(f"\n📊 Complete: {ok}/{len(metadata_files)}")


if __name__ == "__main__":
    main()
