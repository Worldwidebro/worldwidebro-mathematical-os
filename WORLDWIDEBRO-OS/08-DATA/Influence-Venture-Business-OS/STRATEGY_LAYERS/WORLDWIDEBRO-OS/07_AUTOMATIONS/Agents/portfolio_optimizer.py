#!/usr/bin/env python3
"""
Portfolio Optimizer for Dexter Financial Orchestrator
Uses PyPortfolioOpt to suggest optimal capital allocation across venture portfolio
Wires to CFO agent's rebalancing_signals() output
"""

import os
import json
import numpy as np
import pandas as pd
from typing import Dict, List, Any, Optional
from datetime import datetime

try:
    from pypfopt import EfficientFrontier, portfolio_performance
    from pypfopt.risk_models import CovarianceShrinkage
    PYPFOPT_AVAILABLE = True
except ImportError:
    PYPFOPT_AVAILABLE = False
    print("⚠️  PyPortfolioOpt not available. Install: pip install pypfopt")

import requests

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")


class VenturePortfolioOptimizer:
    """Optimal capital allocation using Modern Portfolio Theory"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {SUPABASE_KEY}"})

    def fetch_venture_data(self) -> pd.DataFrame:
        """Load ventures with financial metrics from Supabase"""
        try:
            response = self.session.get(
                f"{SUPABASE_URL}/rest/v1/ventures",
                params={
                    "select": "id,name,sector,roi,gross_margin_pct,burn_rate_monthly,runway_months,health_score,allocation_target"
                }
            )
            if response.status_code == 200:
                ventures = response.json()
                df = pd.DataFrame(ventures)

                # Prepare expected_return and risk columns
                df['expected_return'] = df['roi'].fillna(0) / 100  # Convert % to decimal
                df['risk'] = df['burn_rate_monthly'].fillna(0) / df['gross_margin_pct'].fillna(1).clip(lower=0.1)  # Volatility proxy
                df['runway_factor'] = (12 / (df['runway_months'].fillna(12).clip(lower=1)))  # Risk adjustment for short runway

                return df
            else:
                print(f"⚠️  Failed to fetch ventures: {response.status_code}")
                return pd.DataFrame()
        except Exception as e:
            print(f"❌ Fetch venture data error: {e}")
            return pd.DataFrame()

    def estimate_covariance(self, df: pd.DataFrame) -> np.ndarray:
        """Estimate covariance matrix from venture financials (grouped by sector)"""
        try:
            # Group by sector and calculate returns correlation
            sector_returns = df.groupby('sector')['expected_return'].mean()

            # Create synthetic correlation: ventures in same sector are more correlated
            n = len(df)
            cov_matrix = np.zeros((n, n))

            for i in range(n):
                for j in range(n):
                    if i == j:
                        # Variance = risk^2
                        cov_matrix[i][j] = df.iloc[i]['risk'] ** 2
                    else:
                        # Cross-venture covariance (higher if same sector)
                        same_sector = df.iloc[i]['sector'] == df.iloc[j]['sector']
                        correlation = 0.6 if same_sector else 0.2
                        cov_matrix[i][j] = correlation * df.iloc[i]['risk'] * df.iloc[j]['risk']

            # Ensure matrix is positive semi-definite via shrinkage
            eigenvalues = np.linalg.eigvals(cov_matrix)
            if np.any(eigenvalues < 0):
                # Add small positive value to diagonal
                cov_matrix += np.eye(n) * abs(np.min(eigenvalues)) * 1.1

            return cov_matrix
        except Exception as e:
            print(f"❌ Covariance estimation error: {e}")
            return np.eye(len(df))

    def efficient_frontier(self, df: pd.DataFrame) -> Dict[str, float]:
        """Calculate optimal weights using Sharpe ratio maximization"""
        if not PYPFOPT_AVAILABLE or len(df) < 2:
            return {}

        try:
            returns = df['expected_return'].values
            cov_matrix = self.estimate_covariance(df)

            # Mean Variance Optimization
            ef = EfficientFrontier(returns, cov_matrix, weight_bounds=(0, 0.3))  # Max 30% per venture
            weights = ef.maximum_sharpe_ratio()

            # Map to venture IDs
            allocation = {}
            for venture_id, weight in zip(df['id'], weights):
                if weight > 0.001:  # Only include meaningful allocations
                    allocation[venture_id] = weight

            return allocation
        except Exception as e:
            print(f"❌ Efficient frontier calculation failed: {e}")
            return {}

    def rebalancing_recommendation(self) -> Dict[str, Any]:
        """Compare current allocation vs optimal, recommend moves"""
        df = self.fetch_venture_data()
        if df.empty:
            return {"error": "No venture data available"}

        try:
            # Current allocation
            current_alloc = dict(zip(df['id'], df['allocation_target']))
            total_current = sum(current_alloc.values())

            # Normalize current to weights
            current_weights = {k: v / total_current if total_current > 0 else 0 for k, v in current_alloc.items()}

            # Optimal allocation
            optimal_weights = self.efficient_frontier(df)

            # Calculate moves (optimal - current)
            moves = {}
            for venture_id in df['id']:
                current_w = current_weights.get(venture_id, 0)
                optimal_w = optimal_weights.get(venture_id, 0)
                delta = optimal_w - current_w

                if abs(delta) > 0.01:  # Only recommend if > 1% change
                    moves[venture_id] = {
                        "current_weight": round(current_w * 100, 2),
                        "optimal_weight": round(optimal_w * 100, 2),
                        "delta_percent": round(delta * 100, 2),
                        "action": "INCREASE" if delta > 0 else "DECREASE"
                    }

            return {
                "timestamp": datetime.utcnow().isoformat(),
                "recommendations": moves,
                "summary": {
                    "moves_suggested": len(moves),
                    "increases": len([m for m in moves.values() if m["action"] == "INCREASE"]),
                    "decreases": len([m for m in moves.values() if m["action"] == "DECREASE"]),
                    "current_total_allocation": round(total_current, 2)
                }
            }
        except Exception as e:
            print(f"❌ Rebalancing recommendation error: {e}")
            return {"error": str(e)}

    def scenario_test(self, additional_capital: float = 0, scenario_name: str = "baseline") -> Dict[str, Any]:
        """Test: what if portfolio received $X capital?"""
        df = self.fetch_venture_data()
        if df.empty:
            return {"error": "No venture data"}

        try:
            current_total = df['allocation_target'].sum()
            new_total = current_total + additional_capital

            # Recalculate optimal weights with new total
            optimal_weights = self.efficient_frontier(df)

            # Apply to new capital pool
            new_allocation = {vid: (w * new_total) for vid, w in optimal_weights.items()}

            # Calculate impact metrics
            old_concentration = (df['allocation_target'].max() / current_total * 100) if current_total > 0 else 0
            new_concentration = (max(new_allocation.values()) / new_total * 100) if new_total > 0 else 0

            return {
                "scenario": scenario_name,
                "additional_capital": additional_capital,
                "previous_total": round(current_total, 2),
                "new_total": round(new_total, 2),
                "concentration_before_pct": round(old_concentration, 2),
                "concentration_after_pct": round(new_concentration, 2),
                "new_allocation": {vid: round(alloc, 2) for vid, alloc in new_allocation.items()},
                "timestamp": datetime.utcnow().isoformat()
            }
        except Exception as e:
            print(f"❌ Scenario test error: {e}")
            return {"error": str(e)}


def main():
    """Test the optimizer"""
    optimizer = VenturePortfolioOptimizer()

    print("\n" + "="*70)
    print("PORTFOLIO OPTIMIZER TEST")
    print("="*70 + "\n")

    # Test 1: Current allocation
    df = optimizer.fetch_venture_data()
    print(f"📊 Loaded {len(df)} ventures")
    if not df.empty:
        print(f"   Total allocated: ${df['allocation_target'].sum():,.0f}")
        print(f"   Portfolio ROI (weighted): {(df['roi'].mean()):.1f}%\n")

    # Test 2: Rebalancing recommendation
    print("🎯 Rebalancing Recommendation:")
    rebal = optimizer.rebalancing_recommendation()
    if "recommendations" in rebal:
        for venture_id, rec in list(rebal["recommendations"].items())[:3]:
            print(f"   {venture_id}: {rec['action']} from {rec['current_weight']}% to {rec['optimal_weight']}%")
        print(f"   ... ({len(rebal['recommendations'])} total moves)\n")

    # Test 3: Scenario - add $10k capital
    print("📈 Scenario: Add $10,000 Capital")
    scenario = optimizer.scenario_test(additional_capital=10000, scenario_name="expansion_round")
    if "new_allocation" in scenario:
        print(f"   Total portfolio: ${scenario['new_total']:,.0f}")
        print(f"   Concentration risk: {scenario['concentration_before_pct']:.1f}% → {scenario['concentration_after_pct']:.1f}%\n")

    print("✅ Optimizer ready for integration with CFO agent")


if __name__ == "__main__":
    main()
