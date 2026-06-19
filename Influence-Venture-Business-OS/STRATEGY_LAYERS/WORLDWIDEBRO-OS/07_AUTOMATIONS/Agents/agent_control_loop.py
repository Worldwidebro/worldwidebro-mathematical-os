#!/usr/bin/env python3
"""
Agent Control Loop - Unified Autonomous Execution System
Connects: Supabase (data) → Ollama (reasoning) → CEO logic → Composio (execution) → aoc_tasks (audit)

This is the single source of truth for agent autonomy. Runs 24/7 decision loop.
Tasks 9, 10, 14 all use this loop.

DECISION AUTHORITY HIERARCHY:
  CEO (Final Authority) - Makes KILL, OPTIMIZE, SCALE, COMPOUND decisions
  ├── Financial Analyst (CFO) - OWNS all metrics: CAC, LTV, churn, margin, burn, health score
  ├── Operations Manager (CTO) - Executes decisions, escalates operational risks
  └── Sector PMs (4 leads) - Manage ventures in their sector, escalate via Ops Manager

Authority Rules:
  - CFO calculates ALL financial metrics (no other agent does)
  - Ops Manager requests metrics from CFO, does NOT calculate
  - Sector PMs request metrics from CFO for their ventures
  - CEO receives metrics ONLY from CFO
  - Risk escalation: Financial → CFO → Ops Manager → CEO
"""

import os
import json
import time
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

# Knowledge graph integration
try:
    from lightrag_agent_queries import AgentQueryInterface
    from lightrag_supabase_sync import LightRAGSupabaseSync
    GRAPH_AVAILABLE = True
except ImportError:
    GRAPH_AVAILABLE = False
    print("⚠️  Knowledge graph module not available, running without graph context")

# Configuration
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://iefnvvfxbnpxfcggzljq.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
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
    survival_metric: float
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

        # Initialize knowledge graph queries if available
        self.graph_queries = None
        if GRAPH_AVAILABLE:
            try:
                sync = LightRAGSupabaseSync()
                self.graph_queries = AgentQueryInterface(sync)
                print("✅ Knowledge graph queries initialized")
            except Exception as e:
                print(f"⚠️  Knowledge graph initialization failed: {e}")

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
        """Get calculated metrics for a venture from Supabase via CFO SQL functions"""
        try:
            # Step 1: Call CFO SQL function to calculate survival_metric (updates ventures table)
            rpc_response = self.session.post(
                f"{SUPABASE_URL}/rest/v1/rpc/calculate_survival_metric",
                json={"venture_id_param": venture_id}
            )

            # Step 2: Fetch venture with all calculated metrics
            response = self.session.get(
                f"{SUPABASE_URL}/rest/v1/ventures",
                params={"id": f"eq.{venture_id}", "select": "*"}
            )
            if response.status_code == 200 and response.json():
                data = response.json()[0]
                return VentureMetrics(
                    venture_id=venture_id,
                    venture_name=data.get("name", "Unknown"),
                    sector=data.get("sector", ""),
                    revenue=data.get("revenue", 0),
                    cost=data.get("cost", 0),
                    gross_margin=data.get("gross_margin_pct", 0),
                    roi=data.get("roi", 0),
                    cac=data.get("cac", 0),
                    ltv=data.get("ltv", 0),
                    ltv_cac_ratio=data.get("ltv_cac_ratio", 0),
                    churn=data.get("churn", 0),
                    runway_months=data.get("runway_months", 0),
                    survival_metric=data.get("survival_metric", 0),
                    health_score=data.get("health_score", 0)
                )
        except Exception as e:
            print(f"⚠️  Metrics fetch failed for {venture_id}: {e}")
        return None

    def ollama_reason(self, metrics: VentureMetrics) -> str:
        """Get Ollama reasoning about venture decision"""

        # Enrich prompt with knowledge graph context if available
        graph_context = ""
        if self.graph_queries:
            try:
                query_context = self.graph_queries.query_venture_context(metrics.venture_id)
                if query_context.results:
                    venture_data = query_context.results[0]
                    entities_list = ", ".join(venture_data.get("entities", [])[:5])
                    graph_context = f"\n\nKnowledge Graph Context:\n- Extracted Entities: {entities_list}\n- Total Relationships: {venture_data.get('total_relationships', 0)}"
            except Exception as e:
                pass  # Silently continue if graph queries fail

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
        - Runway: {metrics.runway_months:.1f} months{graph_context}

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
        """CEO decision logic: Week 0 decision tree (ROI + survival_metric)

        Decision Tree (Immutable Algorithm):
          IF roi < 0% AND survival < 50 → KILL (venture dying)
          ELSE IF roi < 50% → OPTIMIZE (cost reduction, improve LTV/CAC)
          ELSE IF roi < 100% → SCALE (controlled growth)
          ELSE (roi ≥ 100%) → COMPOUND (aggressive reinvestment)
        """

        # Week 0 decision tree: ROI + survival_metric
        if metrics.roi < 0 and metrics.survival_metric < 50:
            decision_type = "KILL"
            capital = 0
            actions = ["Wind down operations", "Close outstanding deals", "Redeploy capital to high-ROI ventures"]
        elif metrics.roi < CEO_DECISION_THRESHOLD:
            decision_type = "OPTIMIZE"
            capital = 1000  # $1k/month for optimization
            actions = ["Reduce operational costs", "Improve LTV/CAC ratio", "Retarget high-margin segments"]
        elif metrics.roi < 100:
            decision_type = "SCALE"
            capital = 3000  # $3k/month for scaling
            actions = ["Expand sourcing to new segments", "Increase SMS volume", "Hire additional outreach team"]
        else:
            decision_type = "COMPOUND"
            capital = 5000  # $5k/month for compounding
            actions = ["Aggressive multi-channel growth", "Enterprise expansion", "Reinvest all profits"]

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
        """Execute decision through Operations Manager execution layers:
        Lead Activation → SMS Messaging → Outreach & Acquisition → Composio command router

        Execution Hierarchy:
          CEO Decision (KILL/OPTIMIZE/SCALE/COMPOUND)
            ↓ Ops Manager receives with capital allocation
            ↓ Dispatch to execution teams
            ├─ Lead Activation Team (identify high-intent leads)
            ├─ SMS Messaging Service (send campaigns)
            └─ Outreach & Acquisition Team (direct outreach, track CAC)
            ↓ Route through Composio for cross-platform commands
        """

        # Map decision to execution teams + Composio commands
        execution_plan = {
            "KILL": {
                "teams": ["lead_activation_pause", "sms_halt"],
                "composio": ["venture_kill", "reallocate_budget"]
            },
            "OPTIMIZE": {
                "teams": ["lead_activation_retarget", "sms_optimize_messages"],
                "composio": ["reduce_burn", "optimize_channels"]
            },
            "SCALE": {
                "teams": ["lead_activation_expand_segment", "sms_increase_volume", "outreach_hire_team"],
                "composio": ["increase_budget", "hire_team"]
            },
            "COMPOUND": {
                "teams": ["lead_activation_aggressive", "sms_multi_channel", "outreach_expansion"],
                "composio": ["reinvest_profits", "expand_markets"]
            }
        }

        plan = execution_plan.get(decision.decision_type, {"teams": [], "composio": []})
        execution_results = {}

        # Step 1: Execute via Ops Manager execution teams
        for team_cmd in plan["teams"]:
            try:
                payload = {
                    "command": team_cmd,
                    "venture_id": decision.venture_id,
                    "capital": decision.capital_allocation,
                    "actions": decision.action_items,
                    "team": self._get_team_from_command(team_cmd)
                }

                response = requests.post(
                    f"{COMPOSIO_URL}/execute",
                    json=payload,
                    timeout=10
                )

                execution_results[team_cmd] = {
                    "status": "queued" if response.status_code == 200 else "failed",
                    "response": response.json() if response.status_code == 200 else str(response.text)
                }

            except Exception as e:
                execution_results[team_cmd] = {"status": "error", "error": str(e)}

        # Step 2: Execute Composio commands
        for cmd in plan["composio"]:
            try:
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

    def _get_team_from_command(self, cmd: str) -> str:
        """Extract team name from execution command"""
        if "lead_activation" in cmd:
            return "Lead Activation Team"
        elif "sms" in cmd:
            return "SMS Messaging Service"
        elif "outreach" in cmd:
            return "Outreach & Acquisition Team"
        return "Unknown Team"

    def audit_log(self, decision: AgentDecision, execution: Dict[str, Any], metrics: VentureMetrics = None):
        """Log decision to week_0_decisions table (governance audit trail)"""

        try:
            # Log to week_0_decisions (governance authority layer)
            week0_record = {
                "venture_id": decision.venture_id,
                "decision_type": decision.decision_type,
                "roi_percent": metrics.roi if metrics else 0,
                "survival_metric_at_decision": metrics.survival_metric if metrics else 0,
                "capital_allocated": decision.capital_allocation,
                "decided_by": "Worldwidebro CEO",
                "rationale": decision.reasoning,
                "created_at": decision.timestamp.isoformat()
            }

            response = self.session.post(
                f"{SUPABASE_URL}/rest/v1/week_0_decisions",
                json=week0_record
            )

            if response.status_code not in [200, 201]:
                print(f"⚠️  Week 0 decision log failed: {response.status_code}")

            # Also log to aoc_tasks for legacy audit trail
            aoc_record = {
                "task_type": f"ceo_decision_{decision.decision_type.lower()}",
                "venture_id": decision.venture_id,
                "assigned_agent": "CEO Agent",
                "status": "executed",
                "priority": "high" if decision.decision_type in ["KILL", "SCALE", "COMPOUND"] else "medium",
                "payload": {
                    "decision_type": decision.decision_type,
                    "reasoning": decision.reasoning,
                    "capital_allocation": decision.capital_allocation,
                    "action_items": decision.action_items,
                    "survival_metric": metrics.survival_metric if metrics else 0
                },
                "result": execution,
                "created_at": decision.timestamp.isoformat()
            }

            response = self.session.post(
                f"{SUPABASE_URL}/rest/v1/aoc_tasks",
                json=aoc_record
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

    # ========== PORTFOLIO-LEVEL CFO METHODS (Dexter Financial Orchestrator) ==========

    def portfolio_health_check(self) -> Dict[str, Any]:
        """Daily portfolio health snapshot: called by CEO agent for rebalancing decisions"""
        try:
            # Fetch all ventures with their financials
            response = self.session.get(
                f"{SUPABASE_URL}/rest/v1/ventures",
                params={"select": "id,name,sector,monthly_revenue,burn_rate_monthly,runway_months,allocation_target,health_score,roi"}
            )
            if response.status_code != 200:
                return {}

            ventures = response.json()
            if not ventures:
                return {}

            # Calculate portfolio-level aggregates
            total_allocated = sum(v.get("allocation_target", 0) for v in ventures)
            total_revenue = sum(v.get("monthly_revenue", 0) for v in ventures)
            avg_burn = sum(v.get("burn_rate_monthly", 0) for v in ventures) / len(ventures) if ventures else 0
            min_runway = min((v.get("runway_months", float('inf')) for v in ventures), default=0)
            avg_health = sum(v.get("health_score", 0) for v in ventures) / len(ventures) if ventures else 0

            # Portfolio ROI (weighted by allocation)
            total_roi = 0
            for v in ventures:
                alloc = v.get("allocation_target", 0)
                roi = v.get("roi", 0)
                if total_allocated > 0:
                    total_roi += (alloc / total_allocated) * roi

            # Concentration risk (% in top venture)
            allocations = sorted([v.get("allocation_target", 0) for v in ventures], reverse=True)
            concentration = (allocations[0] / total_allocated * 100) if total_allocated > 0 else 0

            # Low runway ventures (need capital infusion)
            low_runway = [v for v in ventures if v.get("runway_months", 0) < 6]
            high_roi = [v for v in ventures if v.get("roi", 0) > 50]

            health_snapshot = {
                "timestamp": datetime.utcnow().isoformat(),
                "total_capital": total_allocated,
                "monthly_revenue": total_revenue,
                "average_burn": avg_burn,
                "portfolio_runway_months": min_runway,
                "average_health_score": avg_health,
                "portfolio_roi_percent": total_roi,
                "concentration_risk_pct": concentration,
                "venture_count": len(ventures),
                "low_runway_ventures": [{"name": v["name"], "runway": v.get("runway_months", 0)} for v in low_runway],
                "high_roi_ventures": [{"name": v["name"], "roi": v.get("roi", 0)} for v in high_roi]
            }

            return health_snapshot
        except Exception as e:
            print(f"❌ Portfolio health check failed: {e}")
            return {}

    def capital_concentration_risk(self) -> Dict[str, float]:
        """Calculate allocation concentration risk (% in top N ventures)"""
        try:
            response = self.session.get(
                f"{SUPABASE_URL}/rest/v1/ventures",
                params={"select": "id,name,allocation_target", "order": "allocation_target.desc"}
            )
            if response.status_code != 200:
                return {}

            ventures = response.json()
            total = sum(v.get("allocation_target", 0) for v in ventures)

            if total == 0:
                return {}

            return {
                "top_1_pct": (ventures[0].get("allocation_target", 0) / total * 100) if ventures else 0,
                "top_3_pct": (sum(v.get("allocation_target", 0) for v in ventures[:3]) / total * 100) if len(ventures) >= 3 else 0,
                "top_5_pct": (sum(v.get("allocation_target", 0) for v in ventures[:5]) / total * 100) if len(ventures) >= 5 else 0,
                "herfindahl_index": sum((v.get("allocation_target", 0) / total) ** 2 for v in ventures)  # HHI: 0=diversified, 1=concentrated
            }
        except Exception as e:
            print(f"❌ Concentration risk calc failed: {e}")
            return {}

    def ventures_under_runway_threshold(self, threshold_months: int = 6) -> List[Dict[str, Any]]:
        """Find ventures at risk: runway < threshold"""
        try:
            response = self.session.get(
                f"{SUPABASE_URL}/rest/v1/ventures",
                params={"select": "id,name,runway_months,monthly_revenue,burn_rate_monthly,allocation_target",
                        "runway_months": f"lt.{threshold_months}",
                        "order": "runway_months.asc"}
            )
            if response.status_code == 200:
                return response.json()
            return []
        except Exception as e:
            print(f"❌ Low runway query failed: {e}")
            return []

    def allocation_rebalance_recommendation(self) -> Dict[str, Any]:
        """Suggest capital reallocation based on health scores and runway"""
        try:
            response = self.session.get(
                f"{SUPABASE_URL}/rest/v1/ventures",
                params={"select": "id,name,health_score,runway_months,roi,allocation_target"}
            )
            if response.status_code != 200:
                return {}

            ventures = response.json()

            # Simple rule: reduce allocation to low health/short runway, increase to high health/high ROI
            recommendations = []
            for v in ventures:
                health = v.get("health_score", 50)
                runway = v.get("runway_months", 12)
                roi = v.get("roi", 0)
                current = v.get("allocation_target", 0)

                # Score: (health + roi/10) adjusted for runway risk
                score = health + (roi / 10)
                if runway < 3:
                    score -= 30  # Penalize critical runway
                elif runway < 6:
                    score -= 15  # Penalize low runway

                recommendation = {
                    "venture_id": v["id"],
                    "venture_name": v["name"],
                    "current_allocation": current,
                    "health_score": health,
                    "runway_months": runway,
                    "roi_percent": roi,
                    "rebalance_score": score,
                    "suggested_action": "MAINTAIN" if score > 60 else "REDUCE" if score < 40 else "WATCH"
                }
                recommendations.append(recommendation)

            # Sort by rebalance score
            recommendations.sort(key=lambda x: x["rebalance_score"], reverse=True)

            return {
                "timestamp": datetime.utcnow().isoformat(),
                "recommendations": recommendations,
                "summary": {
                    "high_priority_reductions": len([r for r in recommendations if r["suggested_action"] == "REDUCE"]),
                    "maintain_positions": len([r for r in recommendations if r["suggested_action"] == "MAINTAIN"]),
                    "watch_positions": len([r for r in recommendations if r["suggested_action"] == "WATCH"])
                }
            }
        except Exception as e:
            print(f"❌ Rebalance recommendation failed: {e}")
            return {}

    def save_portfolio_snapshot(self, snapshot: Dict[str, Any]) -> bool:
        """Persist portfolio health to portfolio_metrics table for historical tracking"""
        try:
            record = {
                "metric_date": datetime.utcnow().date().isoformat(),
                "total_capital": snapshot.get("total_capital", 0),
                "allocated_capital": snapshot.get("total_capital", 0),
                "liquid_cash": snapshot.get("total_capital", 0),  # TODO: calculate from balance
                "total_portfolio_roi": snapshot.get("portfolio_roi_percent", 0),
                "avg_health_score": int(snapshot.get("average_health_score", 0)),
                "concentration_risk": self.capital_concentration_risk().get("herfindahl_index", 0),
                "portfolio_runway_months": snapshot.get("portfolio_runway_months", 0),
                "venture_count": snapshot.get("venture_count", 0)
            }

            response = self.session.post(
                f"{SUPABASE_URL}/rest/v1/portfolio_metrics",
                json=record
            )

            if response.status_code in [200, 201]:
                print(f"✅ Portfolio snapshot saved: {datetime.utcnow().isoformat()}")
                return True
            else:
                print(f"⚠️  Portfolio snapshot save failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Portfolio snapshot error: {e}")
            return False

    # ========== END PORTFOLIO METHODS ==========

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

            # Step 2a: Query knowledge graph context
            graph_info = ""
            if self.graph_queries:
                try:
                    context = self.graph_queries.query_venture_context(venture_id)
                    if context.results:
                        data = context.results[0]
                        graph_info = f" (Graph: {data.get('total_entities', 0)} entities, {data.get('total_relationships', 0)} links)"
                except Exception:
                    pass

            # Step 2b: Get Ollama reasoning
            print(f"🧠 Reasoning about {venture_name}{graph_info}...", end=" ", flush=True)
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

            # Step 5: Audit log (includes Week 0 governance and legacy aoc_tasks)
            print(f"📝 Logging to audit trail...", end=" ", flush=True)
            self.audit_log(decision, execution, metrics)
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
