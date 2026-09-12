#!/usr/bin/env python3
"""
Company Brain — Token Control Center Dashboard
Generates real-time token telemetry matching the canonical Local AI OS dashboard specification.

Authority: System Architecture & Infrastructure Control Plane (CP-027)
"""

import sys
import json
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from _ENGINE.token_ledger import ledger


def render_dashboard():
    summary = ledger.get_summary()
    ledger_file = ledger.ledger_file

    local_model_tokens = defaultdict(int)
    cloud_model_tokens = defaultdict(int)
    agent_tokens = defaultdict(int)
    unexpected_providers = 0
    unknown_endpoints = 0
    runaway_loops = 0
    unexpected_retries = 0

    if ledger_file.exists():
        with open(ledger_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    t = data.get("tokens", {})
                    total_tok = t.get("total", 0)
                    model = data.get("model", "unknown")
                    provider = data.get("provider", "unknown")
                    agent = data.get("agent", "Antigravity")
                    endpoint = data.get("endpoint", "")
                    status = data.get("status", "PASS")

                    if data.get("is_local", False):
                        local_model_tokens[model] += total_tok
                    else:
                        cloud_model_tokens[model] += total_tok

                    agent_tokens[agent] += total_tok

                    if provider.upper() == "UNKNOWN":
                        unexpected_providers += 1
                    if not endpoint or endpoint.upper() == "UNKNOWN":
                        unknown_endpoints += 1
                    if "LOOP" in status:
                        runaway_loops += 1
                    if "RETRY" in status:
                        unexpected_retries += 1

                except Exception:
                    continue

    today_local = summary["tokens"]["local_tokens"]
    today_cloud = summary["tokens"]["cloud_tokens"]
    today_cost = summary["financial"]["total_cost_usd"]

    output = []
    output.append("=" * 45)
    output.append("             TOKEN CONTROL CENTER")
    output.append("=" * 45)
    output.append("")
    output.append("TODAY")
    output.append("─" * 45)
    output.append(f"Local tokens:             {today_local:>15,}")
    output.append(f"Cloud tokens:             {today_cloud:>15,}")
    output.append(f"Cloud cost:               ${today_cost:>14.2f}")
    output.append("")
    output.append("LOCAL INFERENCE")
    output.append("─" * 45)
    for mdl, tok in sorted(local_model_tokens.items(), key=lambda x: x[1], reverse=True):
        output.append(f"{mdl:<25} {tok:>15,}")
    if not local_model_tokens:
        output.append(f"{'No local calls':<25} {0:>15,}")
    output.append("")
    output.append("CLOUD MODELS (ZERO-CLOUD GUARANTEE)")
    output.append("─" * 45)
    for c_mdl in ["OpenAI", "Anthropic", "Google", "OpenRouter", "Z.ai GLM"]:
        tok = cloud_model_tokens.get(c_mdl, 0)
        output.append(f"{c_mdl:<25} {tok:>15,}")
    output.append("")
    output.append("AGENTS ATTRIBUTION")
    output.append("─" * 45)
    for ag, tok in sorted(agent_tokens.items(), key=lambda x: x[1], reverse=True):
        output.append(f"{ag:<25} {tok:>15,}")
    if not agent_tokens:
        output.append(f"{'No active agents':<25} {0:>15,}")
    output.append("")
    output.append("SECURITY & OBSERVABILITY ALERTS")
    output.append("─" * 45)
    output.append(f"Unexpected provider:      {unexpected_providers:>15}")
    output.append(f"Runaway loops:            {runaway_loops:>15}")
    output.append(f"Unexpected retries:       {unexpected_retries:>15}")
    output.append(f"Unknown endpoint:         {unknown_endpoints:>15}")
    output.append("=" * 45)

    dashboard_text = "\n".join(output)
    print(dashboard_text)
    return dashboard_text


if __name__ == "__main__":
    render_dashboard()
