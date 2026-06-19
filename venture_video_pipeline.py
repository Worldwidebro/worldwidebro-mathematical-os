#!/usr/bin/env python3
"""Gold-standard venture video pipeline: script → TTS → scenes → captions → MP4."""

from __future__ import annotations

import asyncio
import json
import math
import re
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

DOCS = Path("/Users/acebless/Documents")
OUTPUT_DIR = DOCS / "moneyprinter-output"
VENV_PYTHON = DOCS / ".venv-venture-video/bin/python"
SYSTEM_PYTHON = Path("/opt/homebrew/bin/python3.12")
PYTHON = VENV_PYTHON if VENV_PYTHON.exists() else SYSTEM_PYTHON

SIZE = (1080, 1920)
FPS = 30
VOICE = "en-US-GuyNeural"
FONT_BOLD = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]
FONT_REG = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]

SCENE_THEMES = {
    "hook": {"bg": "#0f172a", "accent": "#f97316", "label": "WATCH THIS"},
    "body": {"bg": "#1a1a2e", "accent": "#22c55e", "label": "INSIGHT"},
    "cta": {"bg": "#111827", "accent": "#fbbf24", "label": "NEXT STEP"},
}


def load_font(size: int, bold: bool = False):
    from PIL import ImageFont

    paths = FONT_BOLD if bold else FONT_REG
    for path in paths:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default()


def wrap_text(text: str, width: int = 28) -> list[str]:
    lines: list[str] = []
    for chunk in textwrap.wrap(text, width=width):
        lines.append(chunk)
    return lines or [text[: width * 2]]


def estimate_duration(script: str, line_count: int) -> float:
    words = max(1, len(script.split()))
    # ~150 wpm spoken + small pauses between scenes
    return max(18.0, min(50.0, words / 2.4 + line_count * 0.4))


def format_srt_time(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    hours, rem = divmod(ms, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    secs, millis = divmod(rem, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def build_srt(timed_lines: list[tuple[float, float, str]], path: Path) -> None:
    chunks: list[str] = []
    for index, (start, end, text) in enumerate(timed_lines, start=1):
        chunks.append(
            f"{index}\n{format_srt_time(start)} --> {format_srt_time(end)}\n{text.strip()}\n"
        )
    path.write_text("\n".join(chunks), encoding="utf-8")


def allocate_durations(lines: list[str], total: float) -> list[float]:
    weights = [max(8, len(line)) for line in lines]
    weight_sum = sum(weights)
    return [total * (weight / weight_sum) for weight in weights]


async def synthesize_edge_tts(text: str, out_path: Path) -> bool:
    try:
        import edge_tts
    except ImportError:
        return False

    try:
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(str(out_path))
        return out_path.exists() and out_path.stat().st_size > 1000
    except Exception:
        return False


def synthesize_say(text: str, out_path: Path) -> bool:
    if not shutil.which("say"):
        return False
    m4a = out_path.with_suffix(".m4a")
    try:
        subprocess.run(["say", "-v", "Samantha", "-o", str(m4a), text], check=True, capture_output=True)
        if not m4a.exists() or m4a.stat().st_size < 1000:
            return False
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(m4a), "-ar", "44100", "-ac", "1", str(out_path)],
            check=True,
            capture_output=True,
            text=True,
        )
        return out_path.exists() and out_path.stat().st_size > 1000
    except (subprocess.CalledProcessError, OSError):
        return False


def synthesize_silent(duration: float, out_path: Path) -> None:
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "lavfi",
            "-i",
            "anullsrc=r=44100:cl=mono",
            "-t",
            f"{duration:.2f}",
            "-q:a",
            "9",
            str(out_path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )


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


def synthesize_audio(text: str, out_path: Path, fallback_duration: float) -> tuple[Path, str]:
    try:
        if asyncio.run(synthesize_edge_tts(text, out_path)):
            return out_path, "edge-tts"
    except Exception:
        pass

    if synthesize_say(text, out_path):
        return out_path, "macos-say"

    wav_path = out_path.with_suffix(".wav")
    synthesize_silent(fallback_duration, wav_path)
    return wav_path, "silent-estimated"


def render_scene(
    meta: dict,
    scene: dict,
    path: Path,
    *,
    background_path: Path | None = None,
) -> None:
    from PIL import Image, ImageDraw

    role = scene.get("role", "body")
    theme = SCENE_THEMES.get(role, SCENE_THEMES["body"])

    if background_path and background_path.exists():
        img = Image.open(background_path).convert("RGB")
        img = img.resize(SIZE, Image.Resampling.LANCZOS)
    else:
        img = Image.new("RGB", SIZE, color=theme["bg"])

    draw = ImageDraw.Draw(img)
    if background_path and background_path.exists():
        overlay = Image.new("RGBA", SIZE, (0, 0, 0, 140))
        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
        draw = ImageDraw.Draw(img)

    title_font = load_font(42, bold=True)
    body_font = load_font(56, bold=True)
    label_font = load_font(28, bold=True)
    footer_font = load_font(26, bold=False)

    code = meta.get("venture_code") or "VENTURE"
    brand = meta.get("title") or "Venture"
    draw.rounded_rectangle((60, 80, 360, 150), radius=18, fill=theme["accent"])
    draw.text((80, 98), code, fill="#111827", font=title_font)

    draw.text((60, 170), brand[:36], fill="#94a3b8", font=footer_font)
    draw.text((60, 230), theme["label"], fill=theme["accent"], font=label_font)

    y = 320
    for line in wrap_text(scene["text"], width=22):
        draw.text((60, y), line, fill="#ffffff", font=body_font)
        y += 72
        if y > SIZE[1] - 280:
            break

    keyword = scene.get("visual_keyword", "construction")
    draw.text((60, SIZE[1] - 180), f"▸ {keyword.replace('_', ' ')}", fill=theme["accent"], font=footer_font)
    draw.rounded_rectangle((60, SIZE[1] - 110, SIZE[0] - 60, SIZE[1] - 40), radius=24, outline=theme["accent"], width=3)
    draw.text((90, SIZE[1] - 92), meta.get("cta", "Learn more")[:42], fill=theme["accent"], font=label_font)

    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, format="PNG")


def build_concat_file(scene_paths: list[Path], durations: list[float], concat_path: Path) -> None:
    lines: list[str] = []
    for index, (scene_path, duration) in enumerate(zip(scene_paths, durations)):
        lines.append(f"file '{scene_path.as_posix()}'")
        lines.append(f"duration {duration:.3f}")
    lines.append(f"file '{scene_paths[-1].as_posix()}'")
    concat_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def encode_video(
    concat_path: Path,
    audio_path: Path,
    srt_path: Path,
    output_path: Path,
) -> None:
    work_dir = concat_path.parent
    # Scene PNGs already include line text; optional SRT kept for upload packages.
    _ = srt_path
    cmd = [
        "ffmpeg",
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        concat_path.name,
        "-i",
        audio_path.name,
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "-r",
        str(FPS),
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-shortest",
        str(output_path.resolve()),
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True, cwd=work_dir)


def render_venture_video(venture_dir: Path, regenerate_script: bool = False, use_higgsfield: bool = False) -> dict:
    venture_id = venture_dir.name
    metadata_path = venture_dir / "metadata.json"

    if regenerate_script or not metadata_path.exists():
        sys.path.insert(0, str(DOCS))
        from venture_script_engine import write_metadata

        write_metadata(venture_id)

    meta = json.loads(metadata_path.read_text(encoding="utf-8"))
    lines = meta.get("script_lines") or [meta.get("hook", ""), meta.get("script", "")]
    script = meta.get("script") or " ".join(lines)
    scenes = meta.get("scenes") or [{"text": line, "role": "body", "visual_keyword": "construction"} for line in lines]

    work = venture_dir / "work"
    work.mkdir(exist_ok=True)

    hf_dir = work / "higgsfield"
    if use_higgsfield:
        sys.path.insert(0, str(DOCS / "WORLDWIDEBRO-OS/11_GROWTH_FUNNEL/SCRIPTS"))
        from higgsfield_scenes import generate_scenes_for_metadata  # noqa: WPS433

        generate_scenes_for_metadata(metadata_path, hf_dir)

    fallback_duration = float(meta.get("duration_target_sec") or estimate_duration(script, len(lines)))
    audio_path = work / "voice.wav"
    audio_mp3 = work / "voice.mp3"
    audio_path_used, tts_method = synthesize_audio(script, audio_mp3, fallback_duration)
    if audio_path_used != audio_path:
        if audio_path_used.suffix == ".mp3":
            subprocess.run(
                ["ffmpeg", "-y", "-i", str(audio_path_used), str(audio_path)],
                check=True,
                capture_output=True,
                text=True,
            )
        elif audio_path_used.suffix == ".wav" and audio_path_used != audio_path:
            shutil.copy(audio_path_used, audio_path)
    duration = probe_duration(audio_path) or fallback_duration

    durations = allocate_durations(lines, duration)
    scene_paths: list[Path] = []
    for index, scene in enumerate(scenes):
        scene_path = work / f"scene_{index:02d}.png"
        bg_path = None
        if use_higgsfield:
            candidate = hf_dir / f"scene_{index:02d}.png"
            if candidate.exists():
                bg_path = candidate
        render_scene(meta, scene, scene_path, background_path=bg_path)
        scene_paths.append(scene_path)

    timed_lines = []
    cursor = 0.0
    for line, seg in zip(lines, durations):
        timed_lines.append((cursor, cursor + seg, line))
        cursor += seg

    srt_path = work / "captions.srt"
    build_srt(timed_lines, srt_path)

    concat_path = work / "concat.txt"
    build_concat_file(scene_paths, durations, concat_path)

    output_path = venture_dir / "output.mp4"
    encode_video(concat_path, audio_path, srt_path, output_path)

    publish_path = venture_dir / "publish.json"
    publish_path.write_text(json.dumps(meta.get("publish", {}), indent=2), encoding="utf-8")

    log = {
        "status": "success",
        "venture_id": venture_id,
        "venture_code": meta.get("venture_code"),
        "topic": meta.get("topic"),
        "tts_method": tts_method,
        "duration_sec": round(duration, 2),
        "scene_count": len(scenes),
        "higgsfield": use_higgsfield,
        "output": str(output_path),
        "publish": str(publish_path),
        "captions": str(srt_path),
    }
    (venture_dir / "generation_log.json").write_text(json.dumps(log, indent=2), encoding="utf-8")
    return log


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Render gold-standard venture videos")
    parser.add_argument("--venture", help="Venture folder UUID")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--regenerate-script", action="store_true")
    parser.add_argument(
        "--use-higgsfield",
        action="store_true",
        help="Use Higgsfield PNGs from work/higgsfield/ (generates if missing)",
    )
    args = parser.parse_args()

    if args.all:
        dirs = sorted(p for p in OUTPUT_DIR.iterdir() if p.is_dir() and (p / "metadata.json").exists())
        if args.limit:
            dirs = dirs[: args.limit]
    elif args.venture:
        dirs = [OUTPUT_DIR / args.venture]
    else:
        parser.error("Provide --venture UUID or --all")

    print("=" * 60)
    print("Venture Video Pipeline")
    print("=" * 60)

    for venture_dir in dirs:
        if not venture_dir.exists():
            print(f"⚠️  Skip missing {venture_dir}")
            continue
        print(f"\n🎬 {venture_dir.name}")
        try:
            log = render_venture_video(
                venture_dir,
                regenerate_script=args.regenerate_script,
                use_higgsfield=args.use_higgsfield,
            )
            print(f"   ✅ {log['output']}")
            print(f"   🔊 TTS: {log['tts_method']} ({log['duration_sec']}s, {log['scene_count']} scenes)")
            print(f"   📣 Topic: {log['topic']}")
        except subprocess.CalledProcessError as exc:
            print(f"   ❌ FFmpeg failed: {exc.stderr[-400:] if exc.stderr else exc}")
        except Exception as exc:
            print(f"   ❌ {exc}")


if __name__ == "__main__":
    main()
