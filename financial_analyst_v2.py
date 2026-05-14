#!/usr/bin/env python3
"""
Financial Analyst Agent v2.0
Integrates real venture data with network mathematics:
- Graph theory (centrality metrics)
- Network science (Metcalfe's Law)
- Control theory (PID loops)
- Portfolio theory (risk analysis)
- Game theory (incentive structures)
- Bayesian reasoning (probability updates)
"""

import json
import math
from datetime import datetime
from typing import List, Dict, Tuple

class NetworkMetrics:
    """Graph theory and network science calculations"""

    @staticmethod
    def degree_centrality(venture_id: str, synergies: List[Dict]) -> float:
        """How connected is this venture? C_D(v) = connections / (n-1)"""
        connections = sum(1 for s in synergies if s['source'] == venture_id or s['target'] == venture_id)
        return float(connections)

    @staticmethod
    def network_value(venture_count: int, network_density: float) -> float:
        """Metcalfe's Law: Network value V ∝ n² × density"""
        metcalfe_base = venture_count ** 2
        return metcalfe_base * network_density * 1.5

    @staticmethod
    def network_density(venture_count: int, synergy_count: int) -> float:
        """Ecosystem cohesion: D = 2E / (N(N-1))"""
        if venture_count < 2:
            return 0
        max_edges = (venture_count * (venture_count - 1)) / 2
        return (2 * synergy_count) / (venture_count * (venture_count - 1)) if max_edges > 0 else 0

    @staticmethod
    def synergy_strength(v1_capabilities: List[str], v1_sector: str, v2_sector: str) -> float:
        """Capability-based complementarity using Jaccard similarity"""
        capability_match = len(v1_capabilities) / (len(set(v1_capabilities)) or 1)
        sector_match = 0.3 if v1_sector == v2_sector else 0.1
        return capability_match * 0.4 + sector_match * 0.6

class ControlTheory:
    """Control loops for KPI management"""

    @staticmethod
    def pid_correction(target: float, current: float, previous_error: float = 0,
                      kp: float = 0.5, ki: float = 0.1, kd: float = 0.2) -> float:
        """PID feedback: u(t) = K_p*e(t) + K_i*∫e(t)dt + K_d*de(t)/dt"""
        error = target - current
        proportional = kp * error
        integral = ki * error
        derivative = kd * (error - previous_error)
        return proportional + integral + derivative

class PortfolioTheory:
    """Risk and correlation analysis"""

    @staticmethod
    def portfolio_variance(venture_count: int, avg_correlation: float) -> float:
        """σ_p² = Σ_i Σ_j w_i w_j σ_ij (correlated failure risk)"""
        weights = 1 / venture_count if venture_count > 0 else 1
        asset_volatility = 0.25  # 25% sector volatility assumption
        return venture_count * (weights ** 2) * (asset_volatility ** 2) * avg_correlation

    @staticmethod
    def fragility_score(portfolio_variance: float, avg_margin: float) -> float:
        """How vulnerable is the portfolio to correlated shocks?"""
        if avg_margin <= 0:
            return 1.0  # Completely fragile
        return min(1.0, portfolio_variance / avg_margin)

class BayesianReasoning:
    """Belief updating with evidence"""

    @staticmethod
    def update_success_probability(prior: float, likelihood: float) -> float:
        """P(Success|Evidence) = P(Evidence|Success) * P(Success) / P(Evidence)"""
        evidence = likelihood * prior + (1 - likelihood) * (1 - prior)
        return (likelihood * prior) / evidence if evidence > 0 else prior

class GameTheory:
    """Incentive structure design"""

    @staticmethod
    def design_incentive_structure(synergy_strength: float) -> Dict:
        """Creates payoff matrix for cooperative vs competitive behavior"""
        payoff_matrix = [
            [8, 8],    # Cooperate-Cooperate: mutual benefit
            [2, 10],   # Cooperate-Defect: one exploited
            [10, 2],   # Defect-Cooperate: one exploits
            [4, 4],    # Defect-Defect: mutual loss
        ]
        nash_eq = "Cooperative" if payoff_matrix[0][0] > payoff_matrix[3][0] else "Competitive"
        return {
            "payoff_matrix": payoff_matrix,
            "nash_equilibrium": nash_eq,
            "incentive_alignment": synergy_strength,
        }

class SystemValue:
    """Overall system valuation formula"""

    @staticmethod
    def compute(capabilities: float, relationships: float, automation: float,
               governance: float, friction: float) -> float:
        """V ≈ (C × R × A × G) - F"""
        return capabilities * relationships * automation * governance - friction

class FinancialAnalystV2:
    """Enhanced Financial Analyst Agent with network intelligence"""

    def __init__(self):
        self.name = "Financial Analyst Agent v2.0"
        self.network = NetworkMetrics()
        self.control = ControlTheory()
        self.portfolio = PortfolioTheory()
        self.bayesian = BayesianReasoning()
        self.game_theory = GameTheory()

    def analyze_venture(self, venture_id: str, metrics: Dict, synergies: List[Dict] = None) -> Dict:
        """Comprehensive venture analysis with network effects"""
        if synergies is None:
            synergies = []

        print(f"\n📊 {self.name} analyzing {venture_id}...")

        # Basic unit economics
        revenue = metrics.get('monthly_revenue', 0)
        costs = metrics.get('monthly_costs', 0)
        customers = metrics.get('active_customers', 1)
        marketing = metrics.get('marketing_spend_mom', 0)
        churn = metrics.get('churn_rate', 0.05)
        new_customers = metrics.get('new_customers_mom', 1)

        cac = marketing / new_customers if new_customers > 0 else 0
        revenue_per_customer = revenue / customers if customers > 0 else 0
        ltv_months = 12 / churn if churn > 0 else 12
        ltv = revenue_per_customer * ltv_months
        margin = (revenue - costs) / revenue if revenue > 0 else 0
        cac_ltv_ratio = ltv / cac if cac > 0 else 0

        # Network effects
        degree_centrality = self.network.degree_centrality(venture_id, synergies)
        density = self.network.network_density(100, len(synergies))  # Assume ~100 ventures
        network_value = self.network.network_value(100, density)

        # Risk assessment
        portfolio_var = self.portfolio.portfolio_variance(100, 0.3)
        fragility = self.portfolio.fragility_score(portfolio_var, margin)

        # Probability update
        base_success_prob = 0.65
        evidence_strength = cac_ltv_ratio / 3  # normalize to 0-1
        updated_success_prob = self.bayesian.update_success_probability(base_success_prob, min(1, evidence_strength))

        # System value
        sys_value = SystemValue.compute(
            capabilities=min(1, cac_ltv_ratio / 3),
            relationships=min(1, degree_centrality / 10),
            automation=0.6,  # assumed process automation
            governance=0.7,  # assumed governance quality
            friction=0.2     # operational friction
        )

        analysis = {
            'venture_id': venture_id,
            'timestamp': datetime.utcnow().isoformat(),
            'metrics': metrics,
            # Unit economics
            'cac': round(cac, 2),
            'ltv': round(ltv, 2),
            'cac_ltv_ratio': round(cac_ltv_ratio, 2),
            'gross_margin': round(margin, 3),
            'runway_months': round(metrics.get('runway_months', 0), 1),
            # Network intelligence
            'degree_centrality': round(degree_centrality, 2),
            'network_density': round(density, 3),
            'network_value': round(network_value, 0),
            # Risk metrics
            'portfolio_variance': round(portfolio_var, 4),
            'fragility_score': round(fragility, 2),
            # Probability & system
            'success_probability': round(updated_success_prob, 2),
            'system_value': round(sys_value, 2),
            # Health assessment
            'health_score': round(min(100, cac_ltv_ratio * 20), 1),
            'assessment': self._assess_health(cac_ltv_ratio, margin, metrics.get('runway_months', 0)),
        }

        # Print summary
        print(f"   Unit Economics: CAC ${analysis['cac']} | LTV ${analysis['ltv']} | Ratio {analysis['cac_ltv_ratio']}x")
        print(f"   Network Position: Degree {analysis['degree_centrality']} | Density {analysis['network_density']:.1%}")
        print(f"   Risk Assessment: Fragility {analysis['fragility_score']:.0%} | Portfolio Var {analysis['portfolio_variance']:.4f}")
        print(f"   Probability: Success {analysis['success_probability']:.0%} | System Value {analysis['system_value']:.1f}")
        print(f"   Health: {analysis['health_score']}/100 — {analysis['assessment']}")

        return analysis

    def _assess_health(self, cac_ltv_ratio: float, gross_margin: float, runway: float) -> str:
        """Multi-factor health assessment"""
        score = 0
        if cac_ltv_ratio >= 3:
            score += 40
        elif cac_ltv_ratio >= 2:
            score += 25
        elif cac_ltv_ratio >= 1:
            score += 10

        if gross_margin >= 0.50:
            score += 40
        elif gross_margin >= 0.35:
            score += 20
        elif gross_margin >= 0.20:
            score += 10

        if runway >= 12:
            score += 20
        elif runway >= 6:
            score += 10

        if score >= 80:
            return "🟢 EXCELLENT: Strong fundamentals, network position, low risk"
        elif score >= 60:
            return "🟡 GOOD: Solid metrics, monitor risk exposure"
        elif score >= 40:
            return "🟠 CAUTION: Viable but needs optimization, elevated risk"
        else:
            return "🔴 CRITICAL: Unit economics unsustainable, high fragility"


if __name__ == '__main__':
    # Test with GenixBank-Lite metrics
    from test_genixbank_lite import VentureMetrics

    analyst = FinancialAnalystV2()
    metrics = VentureMetrics('FIN-001-GenixBank-Lite').to_dict()

    # Mock synergies (in real system, fetch from Supabase)
    synergies = [
        {'source': 'FIN-001-GenixBank-Lite', 'target': 'FIN-002-PayFlow', 'strength': 0.75},
        {'source': 'FIN-001-GenixBank-Lite', 'target': 'FIN-003-WealthOS', 'strength': 0.65},
    ]

    analysis = analyst.analyze_venture('FIN-001-GenixBank-Lite', metrics, synergies)
    print(json.dumps(analysis, indent=2))
