#!/usr/bin/env python3
"""
recursive_scan_loop.py
Runs the complete codebase-scanning, knowledge-graph-building, VEX-site-generation,
and PDF-playbook-building pipeline recursively to sync all intelligence layers.
"""
import os
import sys
import subprocess
import time

DOCS = "/Users/acebless/Documents"


def log(msg):
    print(f"\n✨ {msg}", flush=True)


def run_script(path, args=[]):
    name = os.path.basename(path)
    log(f"Running {name}...")
    if not os.path.exists(path):
        print(f"  Warning: Script not found at {path}, skipping.")
        return False
    try:
        cmd = [sys.executable, path] + args if path.endswith(".py") else [path] + args
        subprocess.run(cmd, check=True, text=True)
        print(f"  ✓ {name} completed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  Error: {name} failed with exit code {e.returncode}")
        return False


def main():
    log("STARTING RECURSIVE INTELLIGENCE SCANNING LOOP")
    print("=" * 60)

    start_time = time.time()

    # Step 1: Scan GitHub Repositories (owned + starred) to index latest capabilities
    run_script(f"{DOCS}/scan_repositories.py")

    # Step 2: Build the static repository capability catalog database
    run_script(f"{DOCS}/build_capability_catalog.py")

    # Step 3: Run the Graph memory synchronizer (Neo4j and Obsidian)
    run_script(f"{DOCS}/obsidian_graph_sync.py")

    # Step 4: Re-build VEX public site static bundle payload
    log("Re-compiling public VEX Hero JSON payload...")
    gen_script = f"{DOCS}/vex-hero-site/scripts/generate-public-data.mjs"
    if os.path.exists(gen_script):
        try:
            subprocess.run(["node", gen_script], check=True, cwd=f"{DOCS}/vex-hero-site")
            print("  ✓ Public VEX JSON successfully generated.")
        except subprocess.CalledProcessError as e:
            print(f"  Error: Public VEX JSON generation failed: {str(e)}")
    else:
        print("  Warning: VEX public data script not found.")

    # Step 5: Regenerate ReportLab PDF playbooks for all active sectors
    run_script(f"{DOCS}/WORLDWIDEBRO-OS/08-DATA/scripts/generate_sector_playbooks.py")

    elapsed = time.time() - start_time
    print("=" * 60)
    log(f"RECURSIVE SCAN LOOP COMPLETE (Elapsed time: {elapsed:.2f}s)")
    print("=" * 60)


if __name__ == "__main__":
    main()
