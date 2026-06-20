#!/usr/bin/env python3.11
"""
Obsidian Daily Sync Automation — Runs at 6:00 AM daily
Exports vault entities + updates knowledge graph
"""

import subprocess
import json
from datetime import datetime
from pathlib import Path

VAULT_PATH = Path("/Users/acebless/Documents")
SYNC_LOGS = VAULT_PATH / ".obsidian" / "sync-logs"

def ensure_log_dir():
    """Create sync logs directory"""
    SYNC_LOGS.mkdir(parents=True, exist_ok=True)

def log_sync(status: str, message: str):
    """Log sync operation to daily JSON file"""
    timestamp = datetime.now().isoformat()
    log_entry = {"timestamp": timestamp, "status": status, "message": message}

    log_file = SYNC_LOGS / f"{datetime.now().strftime('%Y-%m-%d')}.json"
    logs = json.loads(log_file.read_text()) if log_file.exists() else []

    logs.append(log_entry)
    log_file.write_text(json.dumps(logs, indent=2))
    print(f"[{timestamp}] {status}: {message}")

def run_graph_sync():
    """Run obsidian_graph_sync.py"""
    try:
        result = subprocess.run(
            ["python3.11", "obsidian_graph_sync.py"],
            cwd=str(VAULT_PATH),
            capture_output=True,
            text=True,
            timeout=300
        )
        if result.returncode == 0:
            log_sync("SUCCESS", "Graph sync completed")
            return True
        else:
            log_sync("ERROR", f"Graph sync failed: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        log_sync("TIMEOUT", "Graph sync exceeded 5 minutes")
        return False
    except Exception as e:
        log_sync("ERROR", f"Exception: {str(e)}")
        return False

def main():
    """Main sync workflow"""
    ensure_log_dir()
    print("🔄 Obsidian Daily Sync Started")
    log_sync("START", "Daily sync initiated at 6:00 AM")

    if run_graph_sync():
        log_sync("COMPLETE", "All operations successful")
        return 0
    else:
        log_sync("FAILED", "Sync completed with errors")
        return 1

if __name__ == "__main__":
    exit(main())
