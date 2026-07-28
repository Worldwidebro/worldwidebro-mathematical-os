#!/usr/bin/env python3
"""
Fractal Agent Spawner for Worldwidebro OS
Programmatically launch and coordinate hierarchical agent loops across ventures.
"""

import subprocess
import json
import time
from pathlib import Path
from typing import Optional

class FractalSpawner:
    def __init__(self, venv_path=".fractal-venv"):
        self.venv_path = Path(venv_path)
        self.activate = f"source {self.venv_path}/bin/activate && "

    def spawn_node(
        self,
        workspace: str,
        goal: str,
        parallel_children: int = 2,
        max_tokens: int = 100000,
        timeout_minutes: int = 60
    ) -> dict:
        """
        Spawn a Fractal node for a specific workspace/goal.

        Returns: {node_id, status, workspace, goal}
        """
        cmd = (
            f"{self.activate}"
            f"fractal node start "
            f"--workspace {workspace} "
            f"--goal '{goal}' "
            f"--parallel-children {parallel_children} "
            f"--max-tokens {max_tokens} "
            f"--timeout {timeout_minutes}"
        )

        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            return {"error": result.stderr, "cmd": cmd}

        # Parse Fractal output (typically JSON or structured text)
        return {
            "workspace": workspace,
            "goal": goal,
            "status": "spawned",
            "stdout": result.stdout,
            "parallel_children": parallel_children
        }

    def spawn_venture_audit(self, opco_code: str, ventures_count: int) -> dict:
        """
        Spawn a Fractal audit node for a specific OPCO.
        Example: opco_code='CON', ventures_count=121
        """
        goal = f"Audit {ventures_count} {opco_code} ventures for readiness"
        return self.spawn_node(
            workspace="ventures",
            goal=goal,
            parallel_children=min(5, ventures_count // 20),  # ~20 ventures per child
            max_tokens=160000,  # Per OPCO budget
            timeout_minutes=30
        )

    def spawn_research_node(self) -> dict:
        """Spawn repository intelligence research node."""
        return self.spawn_node(
            workspace="research",
            goal="Analyze 1,639 repos, extract capabilities, map to 712 ventures",
            parallel_children=4,
            max_tokens=300000,
            timeout_minutes=45
        )

    def spawn_infrastructure_node(self) -> dict:
        """Spawn infrastructure deployment node."""
        return self.spawn_node(
            workspace="infrastructure",
            goal="Verify all IZA OS services, test connectivity, sync data",
            parallel_children=2,
            max_tokens=50000,
            timeout_minutes=20
        )

    def monitor_node(self, node_id: str) -> dict:
        """Monitor a running Fractal node."""
        cmd = f"{self.activate}fractal node monitor --node-id {node_id}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return {"node_id": node_id, "status": result.stdout}

    def list_nodes(self) -> dict:
        """List all active Fractal nodes."""
        cmd = f"{self.activate}fractal nodes list"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return {"nodes": result.stdout}


# Example Usage
if __name__ == "__main__":
    spawner = FractalSpawner()

    print("=== Fractal Agent Spawner ===\n")

    # Option 1: Single OPCO audit
    print("📊 Spawning Construction OPCO audit...")
    result = spawner.spawn_venture_audit("CON", 121)
    print(f"✅ {json.dumps(result, indent=2)}\n")

    # Option 2: Research node
    print("🔬 Spawning Repository Intelligence research...")
    result = spawner.spawn_research_node()
    print(f"✅ {json.dumps(result, indent=2)}\n")

    # Option 3: Infrastructure node
    print("🏗️  Spawning Infrastructure verification...")
    result = spawner.spawn_infrastructure_node()
    print(f"✅ {json.dumps(result, indent=2)}\n")

    # List all active nodes
    print("📋 Active Fractal Nodes:")
    result = spawner.list_nodes()
    print(result["nodes"])
