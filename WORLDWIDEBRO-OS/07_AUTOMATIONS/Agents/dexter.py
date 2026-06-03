#!/usr/bin/env python3
"""
DEXTER: Financial Orchestrator
5-layer system for portfolio-level venture decisions & optimization

Layers:
  1. Portfolio Aggregation — fetch ventures, compute network metrics, identify synergies
  2. Risk Management — portfolio variance, fragility detection, concentration risk
  3. Strategic Optimization — PID control, capital allocation, incentive design
  4. Decision Automation — CEO decisions at scale, aggregate by sector
  5. Execution & Feedback — monitor tasks, Bayesian learning, schedule cycles
"""

import os
import json
import math
from datetime import datetime, timedelta
from typing import List, Dict, Tuple
from enum import Enum

try:
    from supabase import create_client, Client
except ImportError:
    print("❌ supabase-py not installed. Install: pip install supabase")
    exit(1)

from financial_analyst_v2 import FinancialAnalystV2, NetworkMetrics, PortfolioTheory, BayesianReasoning

# ============================================================================
# CONFIGURATION
# ============================================================================

SUPABASE_URL = os.getenv('SUPABASE_URL', 'https://iefnvvfxbnpxfcggzljq.supabase.co')
SUPABASE_KEY = os.getenv('SUPABASE_KEY', '')

class DecisionType(Enum):
    KILL = 'kill'
    HOLD = 'hold'
    SCALE = 'scale'
    PIVOT = 'pivot'

# ============================================================================
# LAYER 1: PORTFOLIO AGGREGATION
# ============================================================================

class PortfolioAggregator:
    """Fetch ventures, compute network metrics, identify synergies"""

    def __init__(self, supabase_client: Client = None):
        self.supabase = supabase_client
        self.network = NetworkMetrics()

    def fetch_all_ventures(self) -> List[Dict]:
        """Load all ventures from Supabase"""
        try:
            response = self.supabase.table('ventures').select('*').execute()
            ventures = response.data if response.data else []
            print(f"📥 Loaded {len(ventures)} ventures from Supabase")
            return ventures
        except Exception as e:
            print(f"❌ Failed to load ventures: {e}")
            return []

    def compute_synergies(self, ventures: List[Dict]) -> List[Dict]:
        """Identify synergy relationships between ventures"""
        synergies = []

        # Group ventures by sector for synergy discovery
        by_sector = {}
        for v in ventures:
            sector = v.get('sector', 'unknown')
            if sector not in by_sector:
                by_sector[sector] = []
            by_sector[sector].append(v)

        # Compute synergy strength between ventures in same/related sectors
        for sector, sector_ventures in by_sector.items():
            for i, v1 in enumerate(sector_ventures):
                for v2 in sector_ventures[i+1:]:
                    strength = self._synergy_strength(v1, v2)
                    if strength > 0.3:  # Only keep meaningful synergies
                        synergies.append({
                            'source': v1['venture_id'],
                            'target': v2['venture_id'],
                            'strength': strength,
                            'sector': sector,
                        })

        print(f"🔗 Identified {len(synergies)} synergies across ventures")
        return synergies

    def _synergy_strength(self, v1: Dict, v2: Dict) -> float:
        """Compute synergy strength between two ventures"""
        # Simple heuristic: ventures in same stage + adjacent sectors = higher synergy
        stage_match = 0.5 if v1.get('stage') == v2.get('stage') else 0.2

        # Capability alignment (if available)
        v1_caps = set(v1.get('capabilities', []))
        v2_caps = set(v2.get('capabilities', []))
        if v1_caps and v2_caps:
            jaccard = len(v1_caps & v2_caps) / len(v1_caps | v2_caps)
        else:
            jaccard = 0.3

        return stage_match * 0.4 + jaccard * 0.6

    def compute_network_density(self, ventures: List[Dict], synergies: List[Dict]) -> float:
        """Ecosystem cohesion: D = 2E / (N(N-1))"""
        n = len(ventures)
        e = len(synergies)
        return self.network.network_density(n, e)

    def compute_network_value(self, ventures: List[Dict], density: float) -> float:
        """Metcalfe's Law: Network value V ∝ n² × density"""
        return self.network.network_value(len(ventures), density)

# ============================================================================
# LAYER 2: RISK MANAGEMENT
# ============================================================================

class RiskManager:
    """Portfolio variance, fragility detection, concentration risk"""

    def __init__(self):
        self.portfolio = PortfolioTheory()

    def compute_portfolio_metrics(self, ventures: List[Dict], analyses: Dict[str, Dict]) -> Dict:
        """Compute portfolio-level risk metrics"""

        # Extract metrics from analyses
        margins = []
        health_scores = []
        fragility_scores = []

        for v_id, analysis in analyses.items():
            margins.append(analysis.get('gross_margin', 0))
            health_scores.append(analysis.get('health_score', 50))
            fragility_scores.append(analysis.get('fragility_score', 0.5))

        avg_margin = sum(margins) / len(margins) if margins else 0
        avg_health = sum(health_scores) / len(health_scores) if health_scores else 50
        avg_fragility = sum(fragility_scores) / len(fragility_scores) if fragility_scores else 0.5

        # Portfolio variance (correlated failure risk)
        n_ventures = len(ventures)
        correlation = 0.3 if self._same_sector_heavy(ventures) else 0.15
        portfolio_var = self.portfolio.portfolio_variance(n_ventures, correlation)

        # Portfolio fragility
        portfolio_fragility = self.portfolio.fragility_score(portfolio_var, avg_margin)

        # Sector concentration risk
        concentration = self._compute_concentration_risk(ventures)

        return {
            'portfolio_variance': portfolio_var,
            'portfolio_fragility': portfolio_fragility,
            'avg_margin': avg_margin,
            'avg_health': avg_health,
            'avg_fragility': avg_fragility,
            'sector_concentration': concentration,
            'correlated_failure_probability': self._failure_prob(portfolio_fragility),
        }

    def identify_fragile_ventures(self, analyses: Dict[str, Dict]) -> List[str]:
        """Find ventures with fragility > 0.7"""
        fragile = []
        for v_id, analysis in analyses.items():
            if analysis.get('fragility_score', 0) > 0.7:
                fragile.append(v_id)
        return fragile

    def _same_sector_heavy(self, ventures: List[Dict]) -> bool:
        """Check if portfolio is concentrated in few sectors"""
        sectors = {}
        for v in ventures:
            sector = v.get('sector', 'unknown')
            sectors[sector] = sectors.get(sector, 0) + 1

        # If top 3 sectors account for >60% of ventures, we're concentrated
        sorted_counts = sorted(sectors.values(), reverse=True)
        top_3 = sum(sorted_counts[:3]) if len(sorted_counts) >= 3 else sum(sorted_counts)
        return top_3 / len(ventures) > 0.6

    def _compute_concentration_risk(self, ventures: List[Dict]) -> float:
        """Herfindahl-Hirschman Index (HHI) for sector concentration"""
        sectors = {}
        for v in ventures:
            sector = v.get('sector', 'unknown')
            sectors[sector] = sectors.get(sector, 0) + 1

        n = len(ventures)
        hhi = sum((count/n)**2 for count in sectors.values())
        return min(1.0, hhi)

    def _failure_prob(self, fragility: float) -> float:
        """Convert fragility to failure probability"""
        return fragility ** (2/3)  # Sublinear relationship

# ============================================================================
# LAYER 3: STRATEGIC OPTIMIZATION
# ============================================================================

class StrategicOptimizer:
    """PID control loops, capital allocation, incentive design"""

    def __init__(self, total_capital: float = 500000):
        self.total_capital = total_capital
        self.bayesian = BayesianReasoning()

    def optimize_capital_allocation(self, ventures: List[Dict], analyses: Dict[str, Dict]) -> Dict[str, float]:
        """Allocate $500K monthly budget across ventures based on ROI + health"""
        allocations = {}

        # Score each venture: health_score * (ltv/cac ratio) * success_probability
        scored = []
        for v in ventures:
            v_id = v['venture_id']
            if v_id not in analyses:
                continue

            analysis = analyses[v_id]
            health = analysis.get('health_score', 50) / 100
            roi = min(1.0, analysis.get('cac_ltv_ratio', 1) / 5)  # Cap at 5x
            success = analysis.get('success_probability', 0.5)

            score = health * roi * success
            scored.append((v_id, score, v.get('stage', 'planned')))

        # Allocate capital proportional to score
        if not scored:
            return allocations

        total_score = sum(s[1] for s in scored)
        if total_score == 0:
            total_score = 1

        for v_id, score, stage in scored:
            allocation = (score / total_score) * self.total_capital
            # Floor at stage minimum (prevent under-investment)
            stage_floor = {'planned': 500, 'validation': 1000, 'build': 2000, 'launch': 1500, 'growth': 3000, 'scale': 5000}.get(stage, 1000)
            allocations[v_id] = max(stage_floor, allocation)

        return allocations

    def design_incentive_structures(self, synergies: List[Dict]) -> Dict[str, Dict]:
        """Game theory: create payoff matrices for cooperative ventures"""
        structures = {}

        for synergy in synergies:
            key = f"{synergy['source']}-{synergy['target']}"
            strength = synergy['strength']

            # Payoff matrix scaled by synergy strength
            base_coop = 8 * strength
            base_compete = 4 * strength

            structures[key] = {
                'cooperate_cooperate': base_coop,
                'cooperate_defect': 2,
                'defect_cooperate': 2,
                'defect_defect': base_compete,
                'recommended': 'cooperative' if base_coop > base_compete else 'competitive',
            }

        return structures

    def apply_pid_control(self, venture: Dict, analysis: Dict, target_health: float = 75) -> Dict:
        """PID feedback loop for KPI management"""
        current_health = analysis.get('health_score', 50)
        error = target_health - current_health

        # PID coefficients
        kp, ki, kd = 0.5, 0.1, 0.2

        # Simple proportional control (full PID requires historical data)
        adjustment = kp * error

        return {
            'current_health': current_health,
            'target_health': target_health,
            'error': error,
            'recommended_adjustment': adjustment,
            'action': 'increase_investment' if adjustment > 0 else 'reduce_investment',
        }

# ============================================================================
# LAYER 4: DECISION AUTOMATION
# ============================================================================

class DecisionAutomator:
    """CEO decisions at scale, aggregate by sector"""

    def __init__(self):
        self.analyzer = FinancialAnalystV2()
        self.bayesian = BayesianReasoning()

    def make_decisions(self, ventures: List[Dict], analyses: Dict[str, Dict]) -> Dict[str, Dict]:
        """Generate CEO decision for each venture in parallel"""
        decisions = {}

        for v in ventures:
            v_id = v['venture_id']
            if v_id not in analyses:
                continue

            analysis = analyses[v_id]
            decision = self._decide_venture(v, analysis)
            decisions[v_id] = decision

        return decisions

    def _decide_venture(self, venture: Dict, analysis: Dict) -> Dict:
        """CEO decision logic for single venture"""
        health = analysis.get('health_score', 50)
        fragility = analysis.get('fragility_score', 0.5)
        success_prob = analysis.get('success_probability', 0.65)
        cac_ltv = analysis.get('cac_ltv_ratio', 1)
        runway = analysis.get('runway_months', 6)

        # Decision thresholds
        if health < 30 or fragility > 0.8:
            decision = DecisionType.KILL
            reasoning = f"Critical: health={health}, fragility={fragility:.0%}"
            capital = 0
        elif health < 50 or success_prob < 0.5:
            decision = DecisionType.HOLD
            reasoning = f"Below threshold: health={health}, success={success_prob:.0%}"
            capital = 0
        elif health < 75 or success_prob < 0.8:
            decision = DecisionType.SCALE
            reasoning = f"Moderate: health={health}, success={success_prob:.0%}"
            capital = int(venture.get('monthly_budget', 5000) * 1.2)
        else:
            decision = DecisionType.SCALE
            reasoning = f"Strong: health={health}, success={success_prob:.0%}, ltv/cac={cac_ltv:.1f}x"
            capital = int(venture.get('monthly_budget', 5000) * 1.5)

        return {
            'venture_id': venture['venture_id'],
            'venture_name': venture.get('name', 'Unknown'),
            'sector': venture.get('sector', 'unknown'),
            'decision': decision.value,
            'reasoning': reasoning,
            'capital_allocation': capital,
            'expected_roi': analysis.get('cac_ltv_ratio', 1) * 100,
            'health_score': health,
            'success_probability': success_prob,
            'timestamp': datetime.utcnow().isoformat(),
        }

    def aggregate_by_sector(self, decisions: Dict[str, Dict]) -> Dict[str, Dict]:
        """Aggregate decisions by sector"""
        by_sector = {}

        for v_id, decision in decisions.items():
            sector = decision.get('sector', 'unknown')
            if sector not in by_sector:
                by_sector[sector] = {
                    'count': 0,
                    'kill': 0,
                    'hold': 0,
                    'scale': 0,
                    'total_capital': 0,
                    'avg_health': 0,
                    'avg_success': 0,
                }

            by_sector[sector]['count'] += 1
            by_sector[sector][decision['decision']] += 1
            by_sector[sector]['total_capital'] += decision['capital_allocation']
            by_sector[sector]['avg_health'] += decision['health_score']
            by_sector[sector]['avg_success'] += decision['success_probability']

        # Normalize averages
        for sector in by_sector:
            count = by_sector[sector]['count']
            if count > 0:
                by_sector[sector]['avg_health'] /= count
                by_sector[sector]['avg_success'] /= count

        return by_sector

# ============================================================================
# LAYER 5: EXECUTION & FEEDBACK
# ============================================================================

class ExecutionManager:
    """Monitor task completion, Bayesian learning, schedule cycles"""

    def __init__(self):
        self.bayesian = BayesianReasoning()
        self.task_log = []

    def queue_execution_tasks(self, decisions: Dict[str, Dict]) -> List[Dict]:
        """Convert decisions to execution tasks"""
        tasks = []

        for v_id, decision in decisions.items():
            decision_type = decision['decision']

            if decision_type == 'scale':
                tasks.extend([
                    {'venture_id': v_id, 'title': 'Increase marketing budget', 'priority': 'high'},
                    {'venture_id': v_id, 'title': 'Hire talent', 'priority': 'high'},
                    {'venture_id': v_id, 'title': 'Expand capacity', 'priority': 'medium'},
                ])
            elif decision_type == 'hold':
                tasks.extend([
                    {'venture_id': v_id, 'title': 'Analyze churn drivers', 'priority': 'high'},
                    {'venture_id': v_id, 'title': 'Optimize unit economics', 'priority': 'high'},
                ])
            elif decision_type == 'kill':
                tasks.extend([
                    {'venture_id': v_id, 'title': 'Notify customers', 'priority': 'urgent'},
                    {'venture_id': v_id, 'title': 'Plan wind-down', 'priority': 'urgent'},
                ])

        return tasks

    def update_success_probabilities(self, analyses: Dict[str, Dict], new_evidence: Dict[str, float]) -> Dict[str, float]:
        """Bayesian learning: update probabilities based on new evidence"""
        updated = {}

        for v_id, analysis in analyses.items():
            old_prob = analysis.get('success_probability', 0.65)

            # Evidence strength (0-1)
            if v_id in new_evidence:
                evidence = new_evidence[v_id]
                new_prob = self.bayesian.update_success_probability(old_prob, evidence)
                updated[v_id] = new_prob

        return updated

    def schedule_next_cycle(self, cycle_date: datetime) -> datetime:
        """Schedule next portfolio analysis cycle (24-hour later)"""
        return cycle_date + timedelta(hours=24)

# ============================================================================
# MAIN ORCHESTRATOR
# ============================================================================

class DexterOrchestrator:
    """Unified 5-layer orchestrator"""

    def __init__(self, test_mode: bool = False):
        self.test_mode = test_mode
        if not test_mode:
            self.supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
            self.aggregator = PortfolioAggregator(self.supabase)
        else:
            self.aggregator = None
        self.risk_mgr = RiskManager()
        self.optimizer = StrategicOptimizer()
        self.decision_auto = DecisionAutomator()
        self.executor = ExecutionManager()
        self.analyzer = FinancialAnalystV2()

    def _generate_test_ventures(self, count: int = 10) -> List[Dict]:
        """Generate synthetic ventures for testing"""
        import random
        sectors = ['financial', 'construction', 'ecommerce', 'saas', 'healthcare']
        stages = ['planned', 'validation', 'build', 'launch', 'growth', 'scale']

        ventures = []
        for i in range(count):
            ventures.append({
                'venture_id': f'TEST-{i:03d}',
                'name': f'Test Venture {i}',
                'sector': random.choice(sectors),
                'stage': random.choice(stages),
                'monthly_revenue': random.randint(2000, 50000),
                'monthly_costs': random.randint(1000, 30000),
                'active_customers': random.randint(10, 500),
                'new_customers_mom': random.randint(2, 50),
                'churn_rate': random.uniform(0.02, 0.15),
                'marketing_spend_mom': random.randint(500, 5000),
                'runway_months': random.uniform(3, 24),
                'monthly_budget': random.randint(2000, 10000),
                'capabilities': ['product', 'marketing', 'sales'],
            })
        return ventures

    def run_full_cycle(self, limit: int = None) -> Dict:
        """Execute complete orchestration cycle"""

        print("""
╔════════════════════════════════════════════════════════════╗
║              DEXTER ORCHESTRATOR — FULL CYCLE              ║
║           Portfolio Analysis & Decision Making             ║
╚════════════════════════════════════════════════════════════╝
        """)

        # Layer 1: Portfolio Aggregation
        print("\n📥 Layer 1: Portfolio Aggregation...")
        if self.test_mode:
            ventures = self._generate_test_ventures(limit or 10)
            aggregator = PortfolioAggregator(None)  # Create temporary aggregator for synergy computation
        else:
            ventures = self.aggregator.fetch_all_ventures()
            if limit:
                ventures = ventures[:limit]
            aggregator = self.aggregator

        synergies = aggregator.compute_synergies(ventures)
        density = aggregator.compute_network_density(ventures, synergies)
        network_value = aggregator.compute_network_value(ventures, density)

        print(f"   ✓ {len(ventures)} ventures loaded")
        print(f"   ✓ Network density: {density:.3f}")
        print(f"   ✓ Network value: ${network_value:,.0f}")

        # Run financial analysis on each venture
        print("\n📊 Financial Analysis...")
        analyses = {}
        for v in ventures:
            v_id = v['venture_id']

            # Extract metrics (or use defaults)
            metrics = {
                'venture_id': v_id,
                'monthly_revenue': v.get('monthly_revenue', 5000),
                'monthly_costs': v.get('monthly_costs', 3000),
                'active_customers': v.get('active_customers', 50),
                'new_customers_mom': v.get('new_customers_mom', 5),
                'churn_rate': v.get('churn_rate', 0.05),
                'marketing_spend_mom': v.get('marketing_spend_mom', 1000),
                'runway_months': v.get('runway_months', 6),
            }

            # Analyze with network context
            analysis = self.analyzer.analyze_venture(v_id, metrics, synergies)
            analyses[v_id] = analysis

        print(f"   ✓ Analyzed {len(analyses)} ventures")

        # Layer 2: Risk Management
        print("\n⚠️  Layer 2: Risk Management...")
        portfolio_metrics = self.risk_mgr.compute_portfolio_metrics(ventures, analyses)
        fragile_ventures = self.risk_mgr.identify_fragile_ventures(analyses)

        print(f"   ✓ Portfolio variance: {portfolio_metrics['portfolio_variance']:.6f}")
        print(f"   ✓ Portfolio fragility: {portfolio_metrics['portfolio_fragility']:.0%}")
        print(f"   ✓ Fragile ventures: {len(fragile_ventures)}")

        # Layer 3: Strategic Optimization
        print("\n⚙️  Layer 3: Strategic Optimization...")
        allocations = self.optimizer.optimize_capital_allocation(ventures, analyses)
        synergy_structures = self.optimizer.design_incentive_structures(synergies)

        total_allocated = sum(allocations.values())
        print(f"   ✓ Capital allocated: ${total_allocated:,.0f} / $500,000")
        print(f"   ✓ Synergy structures: {len(synergy_structures)}")

        # Layer 4: Decision Automation
        print("\n👔 Layer 4: Decision Automation...")
        decisions = self.decision_auto.make_decisions(ventures, analyses)
        sector_summary = self.decision_auto.aggregate_by_sector(decisions)

        decision_counts = {'scale': 0, 'hold': 0, 'kill': 0}
        for d in decisions.values():
            decision_counts[d['decision']] += 1

        print(f"   ✓ SCALE: {decision_counts['scale']} ventures")
        print(f"   ✓ HOLD: {decision_counts['hold']} ventures")
        print(f"   ✓ KILL: {decision_counts['kill']} ventures")

        # Layer 5: Execution & Feedback
        print("\n🚀 Layer 5: Execution & Feedback...")
        tasks = self.executor.queue_execution_tasks(decisions)
        next_cycle = self.executor.schedule_next_cycle(datetime.utcnow())

        print(f"   ✓ Tasks queued: {len(tasks)}")
        print(f"   ✓ Next cycle: {next_cycle.isoformat()}")

        # Compile results
        results = {
            'timestamp': datetime.utcnow().isoformat(),
            'cycle_duration_hours': 24,
            'layer_1': {
                'ventures_analyzed': len(ventures),
                'synergies_identified': len(synergies),
                'network_density': density,
                'network_value': network_value,
            },
            'layer_2': portfolio_metrics,
            'layer_3': {
                'total_capital_allocated': total_allocated,
                'synergy_structures': len(synergy_structures),
            },
            'layer_4': {
                'decisions': decision_counts,
                'by_sector': sector_summary,
            },
            'layer_5': {
                'tasks_queued': len(tasks),
                'next_cycle': next_cycle.isoformat(),
            },
        }

        # Save results
        print(f"\n💾 Saving results...")
        with open('dexter-cycle-results.json', 'w') as f:
            json.dump(results, f, indent=2)

        print(f"""
╔════════════════════════════════════════════════════════════╗
║                   ✅ CYCLE COMPLETE                        ║
╠════════════════════════════════════════════════════════════╣
║ Ventures:       {len(ventures)} analyzed                          ║
║ Synergies:      {len(synergies)} identified                       ║
║ Scale:          {decision_counts['scale']} ventures                           ║
║ Hold:           {decision_counts['hold']} ventures                            ║
║ Kill:           {decision_counts['kill']} ventures                            ║
║ Capital:        ${total_allocated:,.0f}                          ║
║ Results:        dexter-cycle-results.json                ║
╚════════════════════════════════════════════════════════════╝
        """)

        return results


# ============================================================================
# TEST
# ============================================================================

def main():
    import sys

    # Parse arguments
    test_mode = '--test' in sys.argv
    limit = None
    if '--limit' in sys.argv:
        idx = sys.argv.index('--limit')
        if idx + 1 < len(sys.argv):
            limit = int(sys.argv[idx + 1])

    dexter = DexterOrchestrator(test_mode=test_mode)
    results = dexter.run_full_cycle(limit=limit or (10 if test_mode else None))


if __name__ == '__main__':
    main()
