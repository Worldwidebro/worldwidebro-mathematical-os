#!/usr/bin/env python3
"""
Audit file structure: find files scattered outside WORLDWIDEBRO-OS folder.
Reports what should move to T7 Shield.
"""

from pathlib import Path

def audit_documents():
    """Scan /Documents for files outside WORLDWIDEBRO-OS."""
    docs_root = Path("/Users/acebless/Documents")

    # Known safe locations (should NOT be moved)
    known_safe = {
        ".planning", ".obsidian-sync", ".venv-venture-video", "node_modules",
        ".git", "Gemini", "Civilization", ".claude", "tools"
    }

    # Categorize
    governance, data, scripts, config, scattered, temp = [], [], [], [], [], []

    print("📁 FILE STRUCTURE AUDIT\n" + "=" * 70)

    for item in sorted(docs_root.iterdir()):
        if item.name in known_safe or item.name.startswith(".") or item.name == "WORLDWIDEBRO-OS":
            continue

        if item.is_file():
            size = item.stat().st_size / 1024
            if any(k in item.name.upper() for k in ["HOLDING", "CORPORATE", "EXECUTION", "SECTOR", "READINESS", "ROADMAP"]):
                governance.append((item.name, size))
            elif item.name.endswith((".csv", ".json")) and any(k in item.name.upper() for k in ["VENTURE", "REPO", "CAPABILITY", "SCORECARD"]):
                data.append((item.name, size / 1024))
            elif item.name.endswith((".py",)) and any(k in item.name for k in ["populate", "obsidian", "build_", "scan_"]):
                scripts.append((item.name, size))
            elif item.name.endswith((".yml", ".yaml", ".sql")):
                config.append((item.name, size))
            else:
                temp.append((item.name, size))

        elif item.is_dir():
            try:
                size = sum(f.stat().st_size for f in item.rglob("*")) / (1024 * 1024)
                scattered.append((item.name, size))
            except:
                scattered.append((item.name, 0))

    print(f"\n🔴 GOVERNANCE (Move to T7)")
    for name, size in governance:
        print(f"  {name:<45} {size:>8.1f} KB")

    print(f"\n🟠 DATA (Move to T7)")
    for name, size in data:
        print(f"  {name:<45} {size:>8.1f} MB")

    print(f"\n🟡 SCRIPTS (Keep in /tools)")
    for name, size in scripts:
        print(f"  {name:<45} {size:>8.1f} KB")

    print(f"\n🟢 CONFIG (Keep in /Documents)")
    for name, size in config:
        print(f"  {name:<45} {size:>8.1f} KB")

    print(f"\n⚠️  FOLDERS (Review)")
    for name, size in scattered[:15]:
        print(f"  {name:<45} {size:>8.1f} MB")
    if len(scattered) > 15:
        print(f"  ... and {len(scattered) - 15} more")

    print(f"\n{'=' * 70}")
    print(f"TOTALS: {len(governance)} governance + {len(data)} data → T7 Shield")
    print(f"        {len(scripts)} scripts in /tools, {len(config)} configs in /Documents")
    print(f"        {len(scattered)} folders need review")
    print(f"{'=' * 70}")

if __name__ == "__main__":
    audit_documents()
