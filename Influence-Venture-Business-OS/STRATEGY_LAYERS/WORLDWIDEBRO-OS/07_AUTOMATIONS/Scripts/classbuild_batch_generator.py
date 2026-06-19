#!/usr/bin/env python3
"""
ClassBuild Batch Generator — Auto-generate complete courses for education ventures.
Reads classbuild_ventures.json, orchestrates ClassBuild CLI for each venture.
"""
import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime

VAULT = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault"
VENTURES_DIR = VAULT / "07-BUSINESS-STRATEGY" / "ventures" / "Education"
CONFIG_FILE = Path.home() / "Documents" / "classbuild_ventures.json"
CLASSBUILD_DIR = Path("/tmp/classbuild")
OUTPUT_BASE = Path.home() / "Documents" / "generated-courses"


def load_config():
    """Load ClassBuild venture configuration."""
    with open(CONFIG_FILE) as f:
        return json.load(f)


def ensure_environment():
    """Check if ClassBuild is installed and has dependencies."""
    if not CLASSBUILD_DIR.exists():
        print("❌ ClassBuild not found at /tmp/classbuild")
        print("   Run: cd /tmp && git clone https://github.com/jtangen/classbuild.git")
        return False

    # Check for node_modules
    if not (CLASSBUILD_DIR / "node_modules").exists():
        print("⚠️  Installing ClassBuild dependencies...")
        result = subprocess.run(
            ["npm", "install"],
            cwd=CLASSBUILD_DIR,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"❌ npm install failed: {result.stderr}")
            return False
        print("✓ Dependencies installed")

    # Check for API key
    import os
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("❌ ANTHROPIC_API_KEY not set")
        print("   Set it: export ANTHROPIC_API_KEY=sk-...")
        return False

    return True


def generate_course(venture_name, venture_folder, topic, chapters, level, notes):
    """Generate a course using ClassBuild CLI."""
    output_dir = OUTPUT_BASE / venture_folder
    output_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "npx", "tsx", "scripts/generate-course.ts",
        "--topic", topic,
        "--chapters", str(chapters),
        "--level", level,
        "--theme", "midnight",
        "--length", "standard",
        "--output", str(output_dir),
        "--notes", notes
    ]

    print(f"\n📚 {venture_folder}")
    print(f"   Topic: {topic}")
    print(f"   Chapters: {chapters} | Level: {level}")
    print(f"   → Generating...", end=" ", flush=True)

    try:
        result = subprocess.run(
            cmd,
            cwd=CLASSBUILD_DIR,
            capture_output=True,
            text=True,
            timeout=1800  # 30 min timeout per course
        )

        if result.returncode == 0:
            print("✓")
            return True
        else:
            print(f"\n   ❌ Generation failed")
            if result.stderr:
                print(f"   Error: {result.stderr[:200]}")
            return False
    except subprocess.TimeoutExpired:
        print(f"\n   ❌ Timeout (30 min)")
        return False
    except Exception as e:
        print(f"\n   ❌ {e}")
        return False


def integrate_course(venture_folder, venture_path):
    """Copy generated course materials into venture folder."""
    source = OUTPUT_BASE / venture_folder
    if not source.exists():
        return False

    # Create courses/ subdirectory in venture
    courses_dir = venture_path / "courses"
    courses_dir.mkdir(exist_ok=True)

    # Copy generated files
    try:
        for item in source.iterdir():
            dest = courses_dir / item.name
            if item.is_dir():
                import shutil
                if dest.exists():
                    shutil.rmtree(dest)
                shutil.copytree(item, dest)
            else:
                import shutil
                shutil.copy2(item, dest)
        return True
    except Exception as e:
        print(f"   ⚠️  Integration failed: {e}")
        return False


def update_venture_metadata(venture_path, config_data):
    """Update VENTURE.json with ClassBuild metadata."""
    venture_json_path = venture_path / "VENTURE.json"
    if not venture_json_path.exists():
        return False

    try:
        with open(venture_json_path) as f:
            venture = json.load(f)

        venture["classbuild"] = {
            "topic": config_data["topic"],
            "chapters": config_data["chapters"],
            "level": config_data["level"],
            "status": "generated",
            "generated_at": datetime.now().isoformat()
        }

        with open(venture_json_path, "w") as f:
            json.dump(venture, f, indent=2)
        return True
    except Exception as e:
        print(f"   ⚠️  Metadata update failed: {e}")
        return False


def main():
    print("🚀 ClassBuild Batch Course Generator")
    print("=" * 70)

    if not ensure_environment():
        sys.exit(1)

    config = load_config()
    print(f"\n📊 Configuration loaded: {len(config)} ventures identified for course generation")

    total = len(config)
    generated = 0
    integrated = 0

    for venture_folder, config_data in config.items():
        # Find venture folder
        venture_path = VENTURES_DIR / venture_folder
        if not venture_path.exists():
            print(f"⚠️  {venture_folder} folder not found, skipping")
            continue

        # Generate course
        success = generate_course(
            venture_folder,
            venture_folder,
            config_data["topic"],
            config_data["chapters"],
            config_data["level"],
            config_data["notes"]
        )

        if success:
            generated += 1

            # Integrate into venture
            if integrate_course(venture_folder, venture_path):
                integrated += 1
                update_venture_metadata(venture_path, config_data)
                print(f"   ✓ Integrated into {venture_folder}/courses/")
            else:
                print(f"   ⚠️  Could not integrate course materials")

    # Summary
    print("\n" + "=" * 70)
    print("✅ Generation Complete\n")
    print(f"  Total ventures: {total}")
    print(f"  Courses generated: {generated}")
    print(f"  Courses integrated: {integrated}")
    print(f"\n📁 Generated courses at: {OUTPUT_BASE}")
    print(f"   Copy to venture folders as needed:")
    print(f"   cp -r {OUTPUT_BASE}/EDU-* {VENTURES_DIR}/")


if __name__ == "__main__":
    main()
