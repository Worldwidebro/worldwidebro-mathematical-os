#!/usr/bin/env python3
"""
Fractal Monitoring Dashboard
Real-time visibility into parallel agent nodes, budget tracking, and task completion.
"""

import subprocess
import json
import time
from pathlib import Path
from datetime import datetime

class FractalMonitor:
    def __init__(self, venv_path=".fractal-venv"):
        self.venv_path = Path(venv_path)
        self.activate = f"source {self.venv_path}/bin/activate && "

    def get_node_status(self) -> dict:
        """Get current status of all running Fractal nodes."""
        cmd = f"{self.activate}fractal status"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return {"raw": result.stdout, "timestamp": datetime.now().isoformat()}

    def monitor_live(self, update_interval=10):
        """Live monitoring dashboard (10s updates)."""
        print("🎯 Fractal Live Monitor\n")
        print("Timestamp\t\t\tWorkspace\tStatus\t\tTokens Used\tChildren")
        print("-" * 100)

        while True:
            status = self.get_node_status()
            print(status["raw"])
            print()
            time.sleep(update_interval)

    def get_budget_report(self) -> dict:
        """Summarize budget usage across all nodes."""
        return {
            "timestamp": datetime.now().isoformat(),
            "note": "Run: fractal budget-report"
        }

    def get_completion_status(self) -> dict:
        """Get task completion status."""
        return {
            "timestamp": datetime.now().isoformat(),
            "note": "Check wiki/.wiki/obsidian/ for progress"
        }


if __name__ == "__main__":
    import sys

    monitor = FractalMonitor()

    if len(sys.argv) > 1 and sys.argv[1] == "--live":
        monitor.monitor_live()
    else:
        print("📊 Fractal Node Status")
        print(f"  Timestamp: {datetime.now().isoformat()}")
        print(f"\n  To monitor live: python3 .fractal_monitor.py --live")
        print(f"  Updates every 10 seconds")
