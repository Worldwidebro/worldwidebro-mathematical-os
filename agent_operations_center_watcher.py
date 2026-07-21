#!/usr/bin/env python3
"""
Agent Operations Center (AOC) Watcher

Live terminal dashboard showing all agent execution in real-time.
Reads from execution.jsonl and updates display every second.

Usage:
    python3 agent_operations_center_watcher.py
"""

import json
import os
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path

try:
    from rich.console import Console
    from rich.table import Table
    from rich.live import Live
    from rich.panel import Panel
    from rich.progress import Progress, BarColumn, TextColumn, PercentComplete
    from rich.text import Text
except ImportError:
    print("ERROR: Install rich first: pip install rich")
    exit(1)

console = Console()
LOG_FILE = Path("/Users/acebless/Documents/execution.jsonl")

def parse_events():
    """Parse all events from execution.jsonl."""
    events = []
    if LOG_FILE.exists():
        with open(LOG_FILE) as f:
            for line in f:
                if line.strip():
                    try:
                        events.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
    return events

def get_status_icon(status: str) -> str:
    """Get icon for status."""
    icons = {
        "queued": "⏳",
        "running": "●",
        "thinking": "🧠",
        "executing": "⚙️",
        "waiting": "⏸",
        "reviewing": "👁️",
        "committing": "💾",
        "complete": "✓",
        "failed": "✗"
    }
    return icons.get(status, "?")

def get_status_color(status: str) -> str:
    """Get color for status."""
    colors = {
        "queued": "yellow",
        "running": "cyan",
        "thinking": "blue",
        "executing": "green",
        "waiting": "yellow",
        "reviewing": "magenta",
        "committing": "green",
        "complete": "green",
        "failed": "red"
    }
    return colors.get(status, "white")

def render_dashboard(events: list) -> Panel:
    """Render live dashboard from events."""

    if not events:
        return Panel(Text("No events yet. Agents will appear here when they start.", style="dim"))

    # Group by agent
    agents = defaultdict(list)
    for event in events:
        agents[event["agent"]].append(event)

    # Get latest event per agent
    latest = {}
    for agent, evts in agents.items():
        latest[agent] = evts[-1]

    # Build table
    table = Table(title="[bold cyan]AI OPERATIONS CENTER[/bold cyan]", show_header=True)
    table.add_column("Agent", style="cyan", width=20)
    table.add_column("Task", style="white", width=30)
    table.add_column("Status", width=12)
    table.add_column("Progress", width=15)
    table.add_column("Tool", style="magenta", width=15)
    table.add_column("Cost", style="yellow", width=10)

    # Count by status
    status_counts = defaultdict(int)
    total_cost = 0.0

    for agent, event in latest.items():
        status = event.get("status", "unknown")
        progress = event.get("progress", 0.0)
        task = event.get("task", "")[:28]
        tool = event.get("tool", "-")
        cost = event.get("cost", 0.0)

        status_counts[status] += 1
        total_cost += cost

        # Format progress bar
        bar = "█" * int(progress * 10) + "░" * (10 - int(progress * 10))
        pct = f"{progress*100:.0f}%"

        # Status with icon
        icon = get_status_icon(status)
        status_text = f"{icon} {status}"
        status_colored = Text(status_text, style=get_status_color(status))

        table.add_row(
            agent,
            task,
            status_colored,
            f"{bar} {pct}",
            tool,
            f"${cost:.3f}"
        )

    # Summary header
    summary = []
    for status in ["running", "thinking", "executing", "complete", "failed", "queued", "waiting"]:
        count = status_counts.get(status, 0)
        if count > 0:
            icon = get_status_icon(status)
            summary.append(f"{icon} {count}")

    summary_text = " | ".join(summary) if summary else "No agents active"
    summary_text += f" | Total: ${total_cost:.2f}"

    # Render with summary
    content = f"[bold]{summary_text}[/bold]\n\n{table}"
    return Panel(content, title="[bold]AGENTS[/bold]", expand=False)

def render_recent_events(events: list, limit: int = 10) -> Panel:
    """Show recent events."""
    if not events:
        return Panel(Text("No events yet.", style="dim"))

    recent = events[-limit:]
    lines = []
    for event in recent:
        ts = event.get("timestamp", "")[:19]  # YYYY-MM-DD HH:MM:SS
        agent = event.get("agent", "")[:20]
        msg = event.get("task", "")[:40]

        icon = get_status_icon(event.get("status", ""))
        line = f"{ts} | {icon} {agent:20} | {msg}"
        lines.append(line)

    return Panel("\n".join(lines), title="[bold]RECENT EVENTS[/bold]", expand=False)

def main():
    """Run live dashboard."""
    console.clear()
    console.print("[bold cyan]Agent Operations Center[/bold cyan] - Press Ctrl+C to exit\n")

    try:
        with Live(console=console, refresh_per_second=1) as live:
            while True:
                events = parse_events()

                # Build layout
                dashboard = render_dashboard(events)
                recent = render_recent_events(events, limit=8)

                layout = f"{dashboard}\n{recent}"
                live.update(layout)

                time.sleep(1)

    except KeyboardInterrupt:
        console.print("\n[dim]AOC stopped.[/dim]")

if __name__ == "__main__":
    main()
