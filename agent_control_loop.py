#!/usr/bin/env python3
"""
Agent Control Loop - Unified Autonomous Execution System
Connects: Supabase (data) → Ollama (reasoning) → CEO logic → Composio (execution) → aoc_tasks (audit)

This is the single source of truth for agent autonomy. Runs 24/7 decision loop.
Tasks 9, 10, 14 all use this loop.
"""

import os
import json
import time
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

# Configuration
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://iefnvvfxbnpxfcggzljq.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://100.87.214.70:11434")
COMPOSIO_URL = os.getenv("COMPOSIO_URL", "http://localhost:3000")
PAPERCLIP_URL = os.getenv("PAPERCLIP_URL", "http://localhost:3101")
PAPERCLIP_COMPANY_ID = os.getenv("PAPERCLIP_COMPANY_ID", "1450a240-2be1-4dc6-b74c-ada307ca6ddb")

# Loop configuration
CYCLE_INTERVAL_HOURS = 6  # Run decision cycle every 6 hours
REASONING_MODEL = "qwen2.5:32b"  # Local Ollama model
CEO_DECISION_THRESHOLD = 50  # ROI threshold for scaling (%)

@dataclass
class VentureMetrics:
    """Financial metrics for a venture"""
    venture_id: str
    venture_name: str
    sector: str
    revenue: float
    cost: float
    gross_margin: float
    roi: float
    cac: float
    ltv: float
    ltv_cac_ratio: float
    churn: float
    runway_months: float
    health_score: int

@dataclass
class AgentDecision:
    """Decision made by CEO agent"""
    venture_id: str
    venture_name: str
    decision_type: str  # KILL, OPTIMIZE, SCALE, COMPOUND
    reasoning: str
    capital_allocation: int
    action_items: List[str]
    timestamp: datetime

@dataclass
class ExecutionTask:
    """Task to execute via Composio"""
    task_id: str
    task_type: str
    venture_id: str
    command: str
    priority: str
    assigned_agent: str
    payload: Dict[str, Any]


class AgentControlLoop:
    """Main autonomous agent execution loop"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {SUPABASE_KEY}"})
        self.last_cycle = None
        self.decisions_log = []

    def fetch_ventures(self) -> List[Dict]:
        """Load all ventures from Supabase"""
        try:
            response = self.session.get(
                f"{SUPABASE_URL}/rest/v1/ventures",
                params={"select": "*", "limit": "1000"}
            )
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Supabase fetch failed: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Supabase error: {e}")
            return []

    def fetch_venture_metrics(self, venture_id: str) -> Optional[VentureMetrics]:
        """Get calculated metrics for a venture from Supabase"""
        try:
            response = self.session.get(
                f"{SUPABASE_URL}/rest/v1/venture_metrics",
                params={"venture_id": f"eq.{venture_id}", "select": "*"}
            )
            if response.status_code == 200 and response.json():
                data = response.json()[0]
                return VentureMetrics(
                    venture_id=venture_id,
                    venture_name=data.get("venture_name", "Unknown"),
                    sector=data.get("sector", ""),
                    revenue=data.get("revenue", 0),
                    cost=data.get("cost", 0),
                    gross_margin=data.get("gross_margin", 0),
                    roi=data.get("roi", 0),
                    cac=data.get("cac", 0),
                    ltv=data.get("ltv", 0),
                    ltv_cac_ratio=data.get("ltv_cac_ratio", 0),
                    churn=data.get("churn", 0),
                    runway_months=data.get("runway_months", 0),
                    health_score=data.get("health_score", 0)
                )
        except Exception as e:
            print(f"⚠️  Metrics fetch failed for {venture_id}: {e}")
        return None

    def ollama_reason(self, metrics: VentureMetrics) -> str:
        """Get Ollama reasoning about venture decision"""
        prompt = f"""
        Analyze this venture and provide strategic reasoning:

        Venture: {metrics.venture_name}
        Sector: {metrics.sector}

        Financials:
        - Monthly Revenue: ${metrics.revenue:,.0f}
        - Monthly Cost: ${metrics.cost:,.0f}
        - Gross Margin: {metrics.gross_margin:.1f}%
        - ROI: {metrics.roi:.1f}%
        - Health Score: {metrics.health_score}/100

        Unit Economics:
        - CAC: ${metrics.cac:,.0f}
        - LTV: ${metrics.ltv:,.0f}
        - LTV/CAC Ratio: {metrics.ltv_cac_ratio:.1f}x (target: >3x)
        - Monthly Churn: {metrics.churn:.1f}%
        - Runway: {metrics.runway_months:.1f} months

        Provide 2-3 sentences of strategic analysis and recommendation.
        """

        try:
            response = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": REASONING_MODEL,
                    "prompt": prompt,
                    "stream": False,
                    "temperature": 0.7
                },
                timeout=30
            )
            if response.status_code == 200:
                return response.json().get("response", "No reasoning generated").strip()
        except Exception as e:
            print(f"⚠️  Ollama reasoning failed: {e}")

        return "Unable to generate reasoning at this time."

    def ceo_decide(self, metrics: VentureMetrics, reasoning: str) -> AgentDecision:
        """CEO agent decision logic based on ROI and reasoning"""

        # Decision tree based on ROI
        if metrics.roi < 0:
            decision_type = "KILL"
            capital = 0
            actions = ["Wind down operations", "Redeploy capital to growing ventures"]
        elif metrics.roi < CEO_DECISION_THRESHOLD:
            decision_type = "OPTIMIZE"
            capital = 1000  # $1k/month for optimization
            actions = ["Reduce operational costs", "Test new customer acquisition channels", "Improve retention"]
        elif metrics.roi < 100:
            decision_type = "SCALE"
            capital = 3000  # $3k/month for scaling
            actions = ["Double marketing budget", "Expand to new customer segments", "Add team members"]
        else:
            decision_type = "COMPOUND"
            capital = 5000  # $5k/month for compounding
            actions = ["Reinvest all profits", "Expand aggressively", "Build competitive moats", "Explore M&A"]

        decision = AgentDecision(
            venture_id=metrics.venture_id,
            venture_name=metrics.venture_name,
            decision_type=decision_type,
            reasoning=reasoning,
            capital_allocation=capital,
            action_items=actions,
            timestamp=datetime.utcnow()
        )

        return decision

    def composio_execute(self, decision: AgentDecision) -> Dict[str, Any]:
        """Execute decision through Composio command router"""

        # Map decision to Composio commands
        commands = {
            "KILL": ["venture_kill", "reallocate_budget"],
            "OPTIMIZE": ["reduce_burn", "optimize_channels"],
            "SCALE": ["increase_budget", "hire_team"],
            "COMPOUND": ["reinvest_profits", "expand_markets"]
        }

        execution_results = {}

        for cmd in commands.get(decision.decision_type, []):
            try:
                # Send to Composio for execution
                payload = {
                    "command": cmd,
                    "venture_id": decision.venture_id,
                    "capital": decision.capital_allocation,
                    "actions": decision.action_items
                }

                response = requests.post(
                    f"{COMPOSIO_URL}/execute",
                    json=payload,
                    timeout=10
                )

                execution_results[cmd] = {
                    "status": "queued" if response.status_code == 200 else "failed",
                    "response": response.json() if response.status_code == 200 else str(response.text)
                }

            except Exception as e:
                execution_results[cmd] = {"status": "error", "error": str(e)}

        return execution_results

    def audit_log(self, decision: AgentDecision, execution: Dict[str, Any]):
        """Log decision and execution to aoc_tasks for complete audit trail"""

        try:
            audit_record = {
                "task_type": f"ceo_decision_{decision.decision_type.lower()}",
                "venture_id": decision.venture_id,
                "assigned_agent": "CEO Agent",
                "status": "executed",
                "priority": "high" if decision.decision_type in ["KILL", "SCALE", "COMPOUND"] else "medium",
                "payload": {
                    "decision_type": decision.decision_type,
                    "reasoning": decision.reasoning,
                    "capital_allocation": decision.capital_allocation,
                    "action_items": decision.action_items
                },
                "result": execution,
                "created_at": decision.timestamp.isoformat()
            }

            # Insert into aoc_tasks table
            response = self.session.post(
                f"{SUPABASE_URL}/rest/v1/aoc_tasks",
                json=audit_record
            )

            if response.status_code in [200, 201]:
                print(f"✅ Audited: {decision.venture_name} → {decision.decision_type}")
                return True
            else:
                print(f"⚠️  Audit failed: {response.status_code}")
                return False

        except Exception as e:
            print(f"❌ Audit error: {e}")
            return False

    def run_cycle(self, limit: int = None):
        """Run one complete decision cycle across all ventures"""

        print(f"\n{'='*70}")
        print(f"🔄 AGENT DECISION CYCLE - {datetime.utcnow().isoformat()}")
        print(f"{'='*70}\n")

        ventures = self.fetch_ventures()
        if not ventures:
            print("❌ No ventures loaded. Check Supabase connection.")
            return

        print(f"📊 Processing {len(ventures)} ventures...\n")

        cycle_decisions = []
        processed = 0

        for venture in ventures[:limit] if limit else ventures:
            venture_id = venture.get("id")
            venture_name = venture.get("name", "Unknown")

            # Skip if already processed in this cycle
            if venture_id in [d.venture_id for d in cycle_decisions]:
                continue

            # Step 1: Fetch metrics
            metrics = self.fetch_venture_metrics(venture_id)
            if not metrics:
                print(f"⏭️  {venture_name}: No metrics available")
                continue

            # Step 2: Get Ollama reasoning
            print(f"🧠 Reasoning about {venture_name}...", end=" ", flush=True)
            reasoning = self.ollama_reason(metrics)
            print("✓")

            # Step 3: CEO decides
            print(f"👔 CEO decision...", end=" ", flush=True)
            decision = self.ceo_decide(metrics, reasoning)
            print(f"→ {decision.decision_type}")

            # Step 4: Execute via Composio
            print(f"⚙️  Executing {decision.decision_type}...", end=" ", flush=True)
            execution = self.composio_execute(decision)
            print("✓")

            # Step 5: Audit log
            print(f"📝 Logging to audit trail...", end=" ", flush=True)
            self.audit_log(decision, execution)
            print("✓")

            cycle_decisions.append(decision)
            processed += 1

            # Small delay between ventures to avoid rate limiting
            time.sleep(0.5)

        print(f"\n{'='*70}")
        print(f"✅ CYCLE COMPLETE")
        print(f"   Processed: {processed}/{len(ventures)} ventures")
        print(f"   Decisions: {len(cycle_decisions)}")
        print(f"   Next cycle: {(datetime.utcnow() + timedelta(hours=CYCLE_INTERVAL_HOURS)).isoformat()}")
        print(f"{'='*70}\n")

        self.last_cycle = datetime.utcnow()
        self.decisions_log.extend(cycle_decisions)

        return cycle_decisions

    def run_continuous(self):
        """Run continuous 24/7 decision loop (for production)"""

        print(f"""
╔════════════════════════════════════════════════════════════╗
║        AGENT CONTROL LOOP - CONTINUOUS MODE                ║
║     Worldwidebro Holdings Autonomous Operations             ║
╚════════════════════════════════════════════════════════════╝

Starting continuous cycle every {CYCLE_INTERVAL_HOURS} hours...
Press Ctrl+C to stop.
        """)

        try:
            while True:
                self.run_cycle()

                # Wait until next cycle
                wait_seconds = CYCLE_INTERVAL_HOURS * 3600
                print(f"⏰ Sleeping for {CYCLE_INTERVAL_HOURS} hours until next cycle...\n")
                time.sleep(wait_seconds)

        except KeyboardInterrupt:
            print("\n\n✋ Agent control loop stopped.")
            self.print_summary()

    def print_summary(self):
        """Print summary of all decisions made"""

        if not self.decisions_log:
            print("No decisions made yet.")
            return

        print(f"\n{'='*70}")
        print(f"📊 DECISION SUMMARY")
        print(f"{'='*70}\n")

        decisions_by_type = {}
        for decision in self.decisions_log:
            dtype = decision.decision_type
            decisions_by_type[dtype] = decisions_by_type.get(dtype, 0) + 1

        print("Decisions by Type:")
        for dtype, count in sorted(decisions_by_type.items()):
            print(f"  {dtype}: {count}")

        print(f"\nTotal Capital Allocated: ${sum(d.capital_allocation for d in self.decisions_log):,.0f}")
        print(f"Average Health Score: {sum(1 for d in self.decisions_log) / len(self.decisions_log) if self.decisions_log else 0:.0f}")


def main():
    """Main entry point"""
    import sys

    # Check for environment
    if not SUPABASE_KEY:
        print("""
❌ SUPABASE_KEY not set!

Set your Supabase API key:
  export SUPABASE_KEY=your_key_here

Get it from: https://app.supabase.com/project/[project-id]/settings/api
        """)
        return

    loop = AgentControlLoop()

    # Check for CLI flags
    if len(sys.argv) > 1:
        if sys.argv[1] == "continuous":
            # Run 24/7
            loop.run_continuous()
        elif sys.argv[1] == "test":
            # Test with just 5 ventures
            loop.run_cycle(limit=5)
        elif sys.argv[1].startswith("--limit="):
            # Test with specific number
            limit = int(sys.argv[1].split("=")[1])
            loop.run_cycle(limit=limit)
    else:
        # Default: run one full cycle
        loop.run_cycle()
        loop.print_summary()


if __name__ == "__main__":
    main()
