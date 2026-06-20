#!/usr/bin/env python3
"""
Venture Data Delegation Layer
Formats venture metrics, risks, and context for agent consumption
Ready-to-use briefings for CEO/CFO/CTO decision-making
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../Scripts'))

try:
    from lightrag_agent_queries import AgentQueryInterface
except ImportError:
    print("⚠️  LightRAG not available. Using mock data.")


@dataclass
class VentureMetrics:
    """Structured venture performance metrics"""
    survival_metric: float  # 0-100, health score
    ltv_cac_ratio: float   # Customer lifetime value / acquisition cost
    runway_weeks: int      # Weeks of cash remaining
    revenue_growth: float  # % month-over-month
    profitable: bool       # Positive cash flow
    mrr: Optional[float] = None  # Monthly recurring revenue
    arr: Optional[float] = None  # Annual recurring revenue
    churn_rate: Optional[float] = None  # % monthly churn
    unit_economics_healthy: bool = False

    def to_dict(self) -> Dict:
        return {
            "survival_metric": self.survival_metric,
            "ltv_cac_ratio": self.ltv_cac_ratio,
            "runway_weeks": self.runway_weeks,
            "revenue_growth": self.revenue_growth,
            "profitable": self.profitable,
            "mrr": self.mrr,
            "arr": self.arr,
            "churn_rate": self.churn_rate,
            "unit_economics_healthy": self.unit_economics_healthy
        }


@dataclass
class VentureRisk:
    """Identified risk for a venture"""
    name: str
    severity: str  # low, medium, high, critical
    impact: str  # financial, operational, market, team
    mitigation: Optional[str] = None

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "severity": self.severity,
            "impact": self.impact,
            "mitigation": self.mitigation
        }


@dataclass
class VentureContext:
    """Full context briefing for venture analysis"""
    venture_id: str
    venture_name: str
    sector: str
    stage: str  # pre-launch, MVP, beta, launch, growth, mature
    team_size: int
    founded_date: Optional[str] = None
    description: Optional[str] = None
    market_opportunity: Optional[str] = None

    def to_dict(self) -> Dict:
        return {
            "venture_id": self.venture_id,
            "venture_name": self.venture_name,
            "sector": self.sector,
            "stage": self.stage,
            "team_size": self.team_size,
            "founded_date": self.founded_date,
            "description": self.description,
            "market_opportunity": self.market_opportunity
        }


class VentureDataDelegation:
    """Formats venture data for agent briefings"""

    def __init__(self, query_interface: Optional[AgentQueryInterface] = None):
        self.query = query_interface

    def build_venture_briefing(self, venture_id: str) -> Dict:
        """Build complete briefing for CEO/CFO/CTO agents"""

        # Get context
        context = self._get_venture_context(venture_id)

        # Get metrics
        metrics = self._get_venture_metrics(venture_id)

        # Get risks
        risks = self._get_venture_risks(venture_id)

        # Build briefing
        briefing = {
            "venture_id": venture_id,
            "timestamp": datetime.now().isoformat(),
            "context": context.to_dict(),
            "metrics": metrics.to_dict(),
            "risks": [r.to_dict() for r in risks],
            "readiness": {
                "ceo_ready": True,
                "cfo_ready": True,
                "cto_ready": True,
                "briefing_complete": True
            }
        }

        return briefing

    def build_sector_briefing(self, sector: str) -> Dict:
        """Build sector-level briefing for portfolio decisions"""

        briefing = {
            "sector": sector,
            "timestamp": datetime.now().isoformat(),
            "ventures": [],
            "sector_metrics": {
                "total_ventures": 0,
                "healthy_ventures": 0,
                "at_risk_ventures": 0,
                "total_runway_weeks": 0,
                "average_survival_metric": 0
            }
        }

        return briefing

    def _get_venture_context(self, venture_id: str) -> VentureContext:
        """Get venture context from knowledge graph or mock"""

        if not self.query:
            return VentureContext(
                venture_id=venture_id,
                venture_name=f"Venture {venture_id}",
                sector="TECH",
                stage="growth",
                team_size=8,
                founded_date="2024-01-15",
                description="High-growth technology venture",
                market_opportunity="$50M TAM"
            )

        try:
            context_data = self.query.query_venture_context(venture_id)
            # Parse context_data into VentureContext
            return VentureContext(
                venture_id=venture_id,
                venture_name=context_data.results.get("name", f"Venture {venture_id}"),
                sector=context_data.results.get("sector", "TECH"),
                stage=context_data.results.get("stage", "growth"),
                team_size=context_data.results.get("team_size", 5)
            )
        except Exception as e:
            print(f"⚠️  Context lookup failed: {e}. Using defaults.")
            return VentureContext(
                venture_id=venture_id,
                venture_name=f"Venture {venture_id}",
                sector="TECH",
                stage="growth",
                team_size=5
            )

    def _get_venture_metrics(self, venture_id: str) -> VentureMetrics:
        """Get venture metrics from knowledge graph or mock"""

        if not self.query:
            return VentureMetrics(
                survival_metric=65.0,
                ltv_cac_ratio=3.5,
                runway_weeks=24,
                revenue_growth=15.0,
                profitable=False,
                mrr=25000,
                arr=300000,
                churn_rate=3.5,
                unit_economics_healthy=True
            )

        try:
            metrics_data = self.query.query_venture_metrics(venture_id)
            # Parse metrics_data into VentureMetrics
            return VentureMetrics(
                survival_metric=float(metrics_data.results.get("survival_metric", 50)),
                ltv_cac_ratio=float(metrics_data.results.get("ltv_cac_ratio", 2.0)),
                runway_weeks=int(metrics_data.results.get("runway_weeks", 12)),
                revenue_growth=float(metrics_data.results.get("revenue_growth", 10)),
                profitable=bool(metrics_data.results.get("profitable", False)),
                mrr=metrics_data.results.get("mrr"),
                arr=metrics_data.results.get("arr"),
                churn_rate=metrics_data.results.get("churn_rate"),
                unit_economics_healthy=bool(metrics_data.results.get("unit_economics_healthy", False))
            )
        except Exception as e:
            print(f"⚠️  Metrics lookup failed: {e}. Using defaults.")
            return VentureMetrics(
                survival_metric=50.0,
                ltv_cac_ratio=2.0,
                runway_weeks=12,
                revenue_growth=10.0,
                profitable=False
            )

    def _get_venture_risks(self, venture_id: str) -> List[VentureRisk]:
        """Get venture risks from knowledge graph or mock"""

        if not self.query:
            return [
                VentureRisk("Market Saturation", "medium", "market", "Differentiation needed"),
                VentureRisk("Team Retention", "low", "team", "Equity refresh"),
                VentureRisk("Cash Burn", "medium", "financial", "Reduce runway target to 18mo")
            ]

        try:
            risks_data = self.query.query_venture_risks(venture_id)
            # Parse risks_data into list of VentureRisk
            return [
                VentureRisk(
                    r.get("name", "Unknown Risk"),
                    r.get("severity", "medium"),
                    r.get("impact", "operational"),
                    r.get("mitigation")
                )
                for r in risks_data.results if isinstance(r, dict)
            ]
        except Exception as e:
            print(f"⚠️  Risks lookup failed: {e}. Using defaults.")
            return [
                VentureRisk("Unknown Risk", "low", "operational")
            ]

    def format_for_ceo(self, briefing: Dict) -> Dict:
        """Format briefing for CEO consumption"""
        return {
            "venture_id": briefing["venture_id"],
            "context": briefing["context"],
            "metrics_summary": {
                "health": briefing["metrics"]["survival_metric"],
                "runway": briefing["metrics"]["runway_weeks"],
                "growth": briefing["metrics"]["revenue_growth"]
            },
            "top_risks": briefing["risks"][:3],  # Top 3 risks
            "recommendation_ready": True
        }

    def format_for_cfo(self, briefing: Dict) -> Dict:
        """Format briefing for CFO consumption"""
        return {
            "venture_id": briefing["venture_id"],
            "financial_metrics": {
                "mrr": briefing["metrics"].get("mrr"),
                "arr": briefing["metrics"].get("arr"),
                "ltv_cac_ratio": briefing["metrics"]["ltv_cac_ratio"],
                "profitable": briefing["metrics"]["profitable"]
            },
            "runway_analysis": {
                "runway_weeks": briefing["metrics"]["runway_weeks"],
                "funding_needed": briefing["metrics"]["runway_weeks"] < 12
            },
            "cash_flow_risks": [r for r in briefing["risks"] if r["impact"] == "financial"]
        }

    def format_for_cto(self, briefing: Dict) -> Dict:
        """Format briefing for CTO consumption"""
        return {
            "venture_id": briefing["venture_id"],
            "product_metrics": {
                "stage": briefing["context"]["stage"],
                "team_size": briefing["context"]["team_size"],
                "growth": briefing["metrics"]["revenue_growth"]
            },
            "technical_risks": [r for r in briefing["risks"] if r["impact"] in ["operational", "market"]],
            "scalability_assessment": "growth_ready" if briefing["metrics"]["survival_metric"] > 60 else "stabilize_first"
        }


def demo_delegation():
    """Demonstrate data delegation for agents"""

    print(f"\n📊 Venture Data Delegation (Week 1)")
    print(f"{'='*70}\n")

    # Initialize delegation layer
    delegation = VentureDataDelegation()

    # Build venture briefing
    sample_ventures = ["venture_hrms_001", "venture_ai_002"]

    print(f"📋 Building Venture Briefings\n")

    for venture_id in sample_ventures:
        briefing = delegation.build_venture_briefing(venture_id)

        print(f"   Venture: {venture_id}")
        print(f"   Health: {briefing['metrics']['survival_metric']:.0f}/100")
        print(f"   Runway: {briefing['metrics']['runway_weeks']}w")
        print(f"   Growth: {briefing['metrics']['revenue_growth']}%")
        print()

    # Format for different agents
    print(f"👨‍💼 Formatting for Agents\n")

    briefing = delegation.build_venture_briefing("venture_hrms_001")

    ceo_brief = delegation.format_for_ceo(briefing)
    print(f"   CEO Brief: {len(ceo_brief)} fields")

    cfo_brief = delegation.format_for_cfo(briefing)
    print(f"   CFO Brief: {len(cfo_brief)} fields")

    cto_brief = delegation.format_for_cto(briefing)
    print(f"   CTO Brief: {len(cto_brief)} fields")
    print()

    print(f"{'='*70}")
    print(f"✅ Data Delegation Operational")
    print(f"   {len(sample_ventures)} ventures delegated")
    print(f"   3 agent formats ready (CEO/CFO/CTO)")
    print()


if __name__ == "__main__":
    demo_delegation()
