#!/usr/bin/env python3
"""
Agent Event Emitter — Execution Bus

Agents call emitter.emit() to log structured events to execution.jsonl.
AOC watcher reads this file in real-time to show agent progress.

Usage:
    from agent_event_emitter import emitter
    emitter.emit(agent="my-agent", task="do X", status="running", progress=0.5, tool="tool_name", file="file.txt", tokens=100, cost=0.01)
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

class AgentEventEmitter:
    def __init__(self, log_file: str = "execution.jsonl"):
        self.log_file = Path(log_file)
        # Create empty file if it doesn't exist
        if not self.log_file.exists():
            self.log_file.touch()

    def emit(
        self,
        agent: str,
        task: str,
        status: str,  # queued, running, thinking, executing, waiting, reviewing, committing, complete, failed
        progress: float = 0.0,  # 0.0-1.0
        tool: str = None,
        file: str = None,
        tokens: int = 0,
        cost: float = 0.0,
        error: str = None,
        next_step: str = None
    ):
        """
        Emit an event to the execution bus.

        Args:
            agent: Agent name/ID (e.g., "contract-handler-01")
            task: Current task (e.g., "Process contract #123")
            status: One of: queued, running, thinking, executing, waiting, reviewing, committing, complete, failed
            progress: Completion percentage (0.0-1.0)
            tool: Tool being used (e.g., "stirling_pdf", "stripe", "neo4j")
            file: File being modified
            tokens: LLM tokens used
            cost: Cost in USD
            error: Error message if status=="failed"
            next_step: What happens next
        """
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "agent": agent,
            "task": task,
            "status": status,
            "progress": progress,
            "tool": tool,
            "file": file,
            "tokens": tokens,
            "cost": cost,
            "error": error,
            "next_step": next_step
        }

        # Write to execution.jsonl (append)
        with open(self.log_file, "a") as f:
            f.write(json.dumps(event) + "\n")

    def clear(self):
        """Clear the execution log (for testing)."""
        self.log_file.write_text("")

# Singleton instance
emitter = AgentEventEmitter("/Users/acebless/Documents/execution.jsonl")

if __name__ == "__main__":
    # Test emit
    emitter.emit(
        agent="test-agent-001",
        task="Test task",
        status="running",
        progress=0.5,
        tool="test_tool",
        file="test.txt",
        tokens=100,
        cost=0.01
    )
    print("✓ Event emitted to execution.jsonl")

    # Show last event
    with open("/Users/acebless/Documents/execution.jsonl") as f:
        lines = f.readlines()
        if lines:
            print(f"Last event: {lines[-1]}")
