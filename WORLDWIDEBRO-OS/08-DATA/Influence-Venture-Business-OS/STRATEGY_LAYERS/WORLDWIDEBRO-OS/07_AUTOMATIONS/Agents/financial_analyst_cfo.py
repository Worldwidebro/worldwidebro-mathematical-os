#!/usr/bin/env python3
"""
Task 9: Financial Analyst Agent (CFO) - Autonomous Metrics Calculation
Runs monthly or on-demand to calculate survival_metric for all ventures
Escalates financial risks to Operations Manager

Execution: `python financial_analyst_cfo.py` or called by agent_control_loop.py
"""

import os
import json
import requests
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://iefnvvfxbnpxfcggzljq.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

@dataclass
class VentureMetrics:
    """Calculated financial metrics"""
    venture_id: str
    venture_name: str
    sector: str
    cac: float
    ltv: float
    ltv_cac_ratio: float
    roi: float
    survival_metric: float
    churn_rate: float
    burn_rate: float
    runway_months: float
    gross_margin_pct: float
    health_status: str  # HEALTHY, CAUTION, CRITICAL, DYING

@dataclass
class FinancialRisk:
    """Risk flagged by CFO"""
    venture_id: str
    venture_name: str
    risk_type: str  # FINANCIAL, OPERATIONAL, STRATEGIC
    severity: str  # LOW, MEDIUM, HIGH, CRITICAL
    description: str
    escalate_to: str  # CTO, CEO


class FinancialAnalystCFO:
    """CFO Agent - Owns all financial metrics calculations"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {SUPABASE_KEY}"})
        self.risks_flagged = []
        self.metrics_calculated = []

    def fetch_ventures(self) -> List[Dict]:
        """Load all ACTIVE ventures from Supabase"""
        try:
            response = self.session.get(
                f"{SUPABASE_URL}/rest/v1/ventures",
                params={
                    "select": "*",
                    "status": f"eq.ACTIVE",
                    "limit": "1000"
                }
            )
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Fetch ventures failed: {response.status_code}")
                return []
        except Exception as e:
            print(f"❌ Error fetching ventures: {e}")
            return []

    def calculate_metrics(self, venture_id: str) -> Optional[VentureMetrics]:
        """Calculate all financial metrics for a venture by calling CFO SQL functions"""
        try:
            venture_response = self.session.get(
                f"{SUPABASE_URL}/rest/v1/ventures",
                params={"id": f"eq.{venture_id}", "select": "*"}
            )

            if venture_response.status_code != 200 or not venture_response.json():
                return None

            venture = venture_response.json()[0]

            # Call SQL functions via RPC (CFO owns all calculations)
            cac_response = self.session.post(
                f"{SUPABASE_URL}/rest/v1/rpc/calculate_cac",
                json={"venture_id_param": venture_id}
            )

            ltv_response = self.session.post(
                f"{SUPABASE_URL}/rest/v1/rpc/calculate_ltv",
                json={"venture_id_param": venture_id}
            )

            survival_response = self.session.post(
                f"{SUPABASE_URL}/rest/v1/rpc/calculate_survival_metric",
                json={"venture_id_param": venture_id}
            )

            # Extract calculated values
            cac = cac_response.json() if cac_response.status_code == 200 else 0
            ltv = ltv_response.json() if ltv_response.status_code == 200 else 0

            # Fetch updated venture with calculated survival_metric
            updated_venture = self.session.get(
                f"{SUPABASE_URL}/rest/v1/ventures",
                params={"id": f"eq.{venture_id}", "select": "*"}
            ).json()[0]

            survival_metric = updated_venture.get("survival_metric", 0)
            roi = updated_venture.get("roi", 0)
            churn = updated_venture.get("churn", 0)
            burn = updated_venture.get("burn_rate_monthly", 0)
            runway = updated_venture.get("runway_months", 0)
            margin = updated_venture.get("gross_margin_pct", 0)

            # Determine health status
            if survival_metric > 70:
                health_status = "HEALTHY"
            elif survival_metric > 50:
                health_status = "CAUTION"
            elif survival_metric > 30:
                health_status = "CRITICAL"
            else:
                health_status = "DYING"

            ltv_cac_ratio = ltv / cac if cac > 0 else 0

            metrics = VentureMetrics(
                venture_id=venture_id,
                venture_name=venture.get("name", "Unknown"),
                sector=venture.get("sector", ""),
                cac=cac,
                ltv=ltv,
                ltv_cac_ratio=ltv_cac_ratio,
                roi=roi,
                survival_metric=survival_metric,
                churn_rate=churn,
                burn_rate=burn,
                runway_months=runway,
                gross_margin_pct=margin,
                health_status=health_status
            )

            return metrics

        except Exception as e:
            print(f"⚠️  Metrics calculation failed for {venture_id}: {e}")
            return None

    def flag_underperforming_ventures(self) -> List[FinancialRisk]:
        """Identify ventures with survival_metric < 50 and flag as risks"""
        try:
            response = self.session.post(
                f"{SUPABASE_URL}/rest/v1/rpc/flag_underperforming_ventures",
                json={}
            )

            if response.status_code == 200:
                underperforming = response.json()
                risks = []

                for venture in underperforming:
                    if venture.get("survival_metric", 0) < 30:
                        severity = "CRITICAL"
                        escalate_to = "CEO"
                    else:
                        severity = "HIGH"
                        escalate_to = "CTO"

                    risk = FinancialRisk(
                        venture_id=venture.get("id"),
                        venture_name=venture.get("name"),
                        risk_type="FINANCIAL",
                        severity=severity,
                        description=f"Survival metric {venture.get('survival_metric', 0):.0f}/100 — underperforming vs. target (>50)",
                        escalate_to=escalate_to
                    )
                    risks.append(risk)

                return risks
            else:
                print(f"⚠️  Underperformance flag failed: {response.status_code}")
                return []

        except Exception as e:
            print(f"❌ Underperformance check error: {e}")
            return []

    def escalate_risk(self, risk: FinancialRisk) -> bool:
        """Log risk to week_0_risks table and route to appropriate manager"""
        try:
            risk_record = {
                "venture_id": risk.venture_id,
                "risk_type": risk.risk_type,
                "severity": risk.severity,
                "description": risk.description,
                "owner_escalated_to": risk.escalate_to,
                "resolved": False,
                "created_at": datetime.utcnow().isoformat()
            }

            response = self.session.post(
                f"{SUPABASE_URL}/rest/v1/week_0_risks",
                json=risk_record
            )

            if response.status_code in [200, 201]:
                print(f"🚨 Risk escalated: {risk.venture_name} → {risk.escalate_to}")
                return True
            else:
                print(f"⚠️  Risk escalation failed: {response.status_code}")
                return False

        except Exception as e:
            print(f"❌ Risk escalation error: {e}")
            return False

    def run_monthly_cycle(self) -> Dict[str, Any]:
        """Execute full monthly financial analysis cycle"""
        print(f"\n{'='*70}")
        print(f"💰 FINANCIAL ANALYST MONTHLY CYCLE - {datetime.utcnow().isoformat()}")
        print(f"{'='*70}\n")

        ventures = self.fetch_ventures()
        if not ventures:
            print("❌ No ventures loaded.")
            return {"status": "failed", "reason": "No ventures"}

        print(f"📊 Analyzing {len(ventures)} ventures...\n")

        metrics_calculated = 0
        risks_flagged = 0

        # Step 1: Calculate metrics for all ventures
        for venture in ventures:
            venture_id = venture.get("id")
            venture_name = venture.get("name", "Unknown")

            print(f"💹 {venture_name}...", end=" ", flush=True)
            metrics = self.calculate_metrics(venture_id)

            if metrics:
                print(f"✓ (Survival: {metrics.survival_metric:.0f}/100, Status: {metrics.health_status})")
                self.metrics_calculated.append(metrics)
                metrics_calculated += 1
            else:
                print("✗ (metrics unavailable)")

        # Step 2: Flag underperforming ventures
        print(f"\n🚨 Checking for underperforming ventures...\n")
        underperforming = self.flag_underperforming_ventures()

        for risk in underperforming:
            print(f"⚠️  {risk.venture_name} (Severity: {risk.severity})")
            self.escalate_risk(risk)
            self.risks_flagged.append(risk)
            risks_flagged += 1

        # Summary
        print(f"\n{'='*70}")
        print(f"✅ FINANCIAL ANALYSIS COMPLETE")
        print(f"   Metrics calculated: {metrics_calculated}/{len(ventures)}")
        print(f"   Risks flagged: {risks_flagged}")
        print(f"   Status: Ready for CEO decision cycle")
        print(f"{'='*70}\n")

        return {
            "status": "success",
            "metrics_calculated": metrics_calculated,
            "risks_flagged": risks_flagged,
            "timestamp": datetime.utcnow().isoformat()
        }

    def print_summary(self):
        """Print summary of metrics calculated"""
        if not self.metrics_calculated:
            print("No metrics calculated.")
            return

        print(f"\n{'='*70}")
        print(f"📈 METRICS SUMMARY")
        print(f"{'='*70}\n")

        by_health = {}
        for metrics in self.metrics_calculated:
            status = metrics.health_status
            by_health[status] = by_health.get(status, 0) + 1

        print("Ventures by Health Status:")
        for status, count in sorted(by_health.items()):
            print(f"  {status}: {count}")

        avg_survival = sum(m.survival_metric for m in self.metrics_calculated) / len(self.metrics_calculated)
        avg_ltv_cac = sum(m.ltv_cac_ratio for m in self.metrics_calculated) / len(self.metrics_calculated)

        print(f"\nAverage Survival Metric: {avg_survival:.1f}/100")
        print(f"Average LTV/CAC Ratio: {avg_ltv_cac:.2f}x (target: >3x)")


def main():
    """Main entry point"""
    if not SUPABASE_KEY:
        print("❌ SUPABASE_KEY not set!")
        return

    cfo = FinancialAnalystCFO()
    result = cfo.run_monthly_cycle()
    cfo.print_summary()

    return result


if __name__ == "__main__":
    main()
