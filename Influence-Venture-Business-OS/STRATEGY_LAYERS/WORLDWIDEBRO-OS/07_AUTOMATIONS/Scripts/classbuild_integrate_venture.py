#!/usr/bin/env python3
"""
ClassBuild Venture Integration — Update VENTURE.json with course metadata
"""
import json
from pathlib import Path
from datetime import datetime
import sys

VAULT = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/Documents/Obsidian Vault"
VENTURES_DIR = VAULT / "07-BUSINESS-STRATEGY" / "ventures" / "Education"
CONFIG_FILE = Path.home() / "Documents" / "classbuild_ventures.json"


def integrate_course(venture_folder):
    """Update VENTURE.json with ClassBuild course metadata."""
    venture_path = VENTURES_DIR / venture_folder
    venture_json = venture_path / "VENTURE.json"
    courses_dir = venture_path / "courses"

    if not venture_json.exists():
        print(f"❌ {venture_folder}: VENTURE.json not found")
        return False

    if not courses_dir.exists():
        print(f"❌ {venture_folder}: courses/ directory not found")
        return False

    # Check if course has been generated (index.html exists and isn't just template)
    index_html = courses_dir / "index.html"
    if not index_html.exists():
        print(f"⚠️  {venture_folder}: No course generated yet")
        return False

    # Load config and venture data
    try:
        with open(CONFIG_FILE) as f:
            config = json.load(f)
        config_data = config.get(venture_folder)
        if not config_data:
            print(f"❌ {venture_folder}: Not found in config")
            return False

        with open(venture_json) as f:
            venture = json.load(f)

        # Update with ClassBuild metadata
        venture["classbuild"] = {
            "status": "generated",
            "topic": config_data["topic"],
            "chapters": config_data["chapters"],
            "level": config_data["level"],
            "generated_at": datetime.now().isoformat(),
            "courses_path": str(courses_dir)
        }

        with open(venture_json, "w") as f:
            json.dump(venture, f, indent=2)

        print(f"✅ {venture_folder}: Updated VENTURE.json")
        return True

    except Exception as e:
        print(f"❌ {venture_folder}: Integration failed - {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: classbuild_integrate_venture.py VENTURE_FOLDER")
        print("Example: classbuild_integrate_venture.py EDU-023-Cybersecurity-Bootcamp")
        sys.exit(1)

    venture_folder = sys.argv[1]
    if integrate_course(venture_folder):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
