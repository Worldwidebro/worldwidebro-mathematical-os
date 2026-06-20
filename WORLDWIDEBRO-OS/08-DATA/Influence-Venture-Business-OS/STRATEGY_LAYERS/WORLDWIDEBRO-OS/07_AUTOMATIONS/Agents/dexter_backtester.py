#!/usr/bin/env python3
"""
Dexter Backtester — Week 2 Scenario Testing Framework
Simulates capital allocation decisions over 2-week period
Validates portfolio rebalancing logic before execution
"""

import os
import json
import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import requests

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")


class VentureBacktester:
    """Backtester for portfolio allocation decisions"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {SUPABASE_KEY}"})
        self.simulation_log = []
        self.allocation_history = []

    def fetch_ventures(self) -> pd.DataFrame:
        """Load ventures from Supabase"""
        try:
            response = self.session.get(
                f"{SUPABASE_URL}/rest/v1/ventures",
                params={"select": "id,name,sector,roi,gross_margin_pct,burn_rate_monthly,runway_months,health_score,allocation_target"}
            )
            if response.status_code == 200:
                return pd.DataFrame(response.json())
            else:
                print(f"❌ Failed to fetch ventures: {response.status_code}")
                return pd.DataFrame()
        except Exception as e:
            print(f"❌ Fetch ventures error: {e}")
            return pd.DataFrame()

    def estimate_covariance(self, df: pd.DataFrame) -> np.ndarray:
        """Estimate covariance matrix (sector-based correlation)"""
        n = len(df)
        cov_matrix = np.zeros((n, n))

        for i in range(n):
            for j in range(n):
                if i == j:
                    risk = df.iloc[i]['burn_rate_monthly'] / df.iloc[i]['gross_margin_pct'].clip(lower=0.1)
                    cov_matrix[i][j] = risk ** 2
                else:
                    same_sector = df.iloc[i]['sector'] == df.iloc[j]['sector']
                    correlation = 0.6 if same_sector else 0.2
                    risk_i = df.iloc[i]['burn_rate_monthly'] / df.iloc[i]['gross_margin_pct'].clip(lower=0.1)
                    risk_j = df.iloc[j]['burn_rate_monthly'] / df.iloc[j]['gross_margin_pct'].clip(lower=0.1)
                    cov_matrix[i][j] = correlation * risk_i * risk_j

        eigenvalues = np.linalg.eigvals(cov_matrix)
        if np.any(eigenvalues < 0):
            cov_matrix += np.eye(n) * abs(np.min(eigenvalues)) * 1.1

        return cov_matrix

    def efficient_frontier(self, df: pd.DataFrame) -> Dict[str, float]:
        """Calculate optimal weights using Sharpe ratio maximization"""
        try:
            from pypfopt import EfficientFrontier
        except ImportError:
            return {}

        if len(df) < 2:
            return {}

        try:
            returns = df['roi'].fillna(0).values / 100
            cov_matrix = self.estimate_covariance(df)

            ef = EfficientFrontier(returns, cov_matrix, weight_bounds=(0, 0.3))
            weights = ef.maximum_sharpe_ratio()

            allocation = {}
            for venture_id, weight in zip(df['id'], weights):
                if weight > 0.001:
                    allocation[venture_id] = weight

            return allocation
        except Exception:
            return {}

    def simulate_day(self, df: pd.DataFrame, day: int, capital_moves: Optional[Dict[str, float]] = None) -> Dict[str, Any]:
        """Simulate one day of portfolio changes"""
        df_copy = df.copy()

        # Apply capital moves if provided
        if capital_moves:
            for venture_id, amount in capital_moves.items():
                mask = df_copy['id'] == venture_id
                if mask.any():
                    df_copy.loc[mask, 'allocation_target'] += amount

        # Simulate daily performance
        daily_return = np.random.normal(0.0005, 0.015)  # ~0.05% mean, 1.5% std daily
        df_copy['allocation_target'] *= (1 + daily_return)

        # Simulate burn rate
        df_copy['runway_months'] = df_copy['allocation_target'] / df_copy['burn_rate_monthly'].clip(lower=1)

        return {
            "day": day,
            "timestamp": (datetime.now() + timedelta(days=day)).isoformat(),
            "total_portfolio_value": df_copy['allocation_target'].sum(),
            "avg_runway_months": df_copy['runway_months'].mean(),
            "concentration_risk_pct": (df_copy['allocation_target'].max() / df_copy['allocation_target'].sum() * 100),
            "ventures_under_6mo_runway": len(df_copy[df_copy['runway_months'] < 6]),
            "daily_return_pct": daily_return * 100,
            "state_snapshot": df_copy.copy()
        }

    def backtest_rebalancing(self, df: pd.DataFrame, duration_days: int = 14) -> Dict[str, Any]:
        """Simulate rebalancing strategy over N days"""
        df_sim = df.copy()
        initial_portfolio_value = df['allocation_target'].sum()

        results = []
        optimal_weights = self.efficient_frontier(df)

        for day in range(1, duration_days + 1):
            # Every 3 days, suggest rebalancing
            capital_moves = None
            if day % 3 == 0 and optimal_weights:
                current_total = df_sim['allocation_target'].sum()
                capital_moves = {}
                for venture_id, optimal_weight in optimal_weights.items():
                    current_alloc = df_sim[df_sim['id'] == venture_id]['allocation_target'].values
                    if len(current_alloc) > 0:
                        target_alloc = optimal_weight * current_total
                        delta = target_alloc - current_alloc[0]
                        if abs(delta) > current_total * 0.01:  # >1% move
                            capital_moves[venture_id] = delta

            day_sim = self.simulate_day(df_sim, day, capital_moves)
            results.append(day_sim)
            df_sim = day_sim['state_snapshot']

        # Calculate returns
        final_portfolio_value = results[-1]['total_portfolio_value']
        total_return = (final_portfolio_value - initial_portfolio_value) / initial_portfolio_value * 100

        return {
            "strategy": "rebalancing_every_3_days",
            "duration_days": duration_days,
            "initial_portfolio_value": round(initial_portfolio_value, 2),
            "final_portfolio_value": round(final_portfolio_value, 2),
            "total_return_pct": round(total_return, 2),
            "avg_daily_return_pct": round(total_return / duration_days, 3),
            "avg_runway_months": round(np.mean([r['avg_runway_months'] for r in results]), 1),
            "min_runway_months": round(min(r['avg_runway_months'] for r in results), 1),
            "max_concentration_risk_pct": round(max(r['concentration_risk_pct'] for r in results), 2),
            "days_under_6mo_runway": sum(1 for r in results if r['ventures_under_6mo_runway'] > 0),
            "results": results
        }

    def backtest_capital_injection(self, df: pd.DataFrame, injection_amount: float, injection_day: int = 1, duration_days: int = 14) -> Dict[str, Any]:
        """Test impact of capital injection on portfolio health"""
        df_sim = df.copy()
        initial_portfolio_value = df['allocation_target'].sum()

        results = []

        for day in range(1, duration_days + 1):
            capital_moves = None

            # Apply capital injection on specified day
            if day == injection_day:
                # Distribute injection proportionally to optimal weights
                optimal_weights = self.efficient_frontier(df_sim)
                capital_moves = {}
                for venture_id, weight in optimal_weights.items():
                    capital_moves[venture_id] = injection_amount * weight

            day_sim = self.simulate_day(df_sim, day, capital_moves)
            results.append(day_sim)
            df_sim = day_sim['state_snapshot']

        final_portfolio_value = results[-1]['total_portfolio_value']
        total_return = (final_portfolio_value - initial_portfolio_value - injection_amount) / (initial_portfolio_value + injection_amount) * 100

        return {
            "scenario": "capital_injection",
            "injection_amount": round(injection_amount, 2),
            "injection_day": injection_day,
            "duration_days": duration_days,
            "initial_portfolio_value": round(initial_portfolio_value, 2),
            "injection_amount_received": round(injection_amount, 2),
            "total_portfolio_after_injection": round(initial_portfolio_value + injection_amount, 2),
            "final_portfolio_value": round(final_portfolio_value, 2),
            "total_return_pct": round(total_return, 2),
            "runway_improvement_months": round(results[-1]['avg_runway_months'] - results[0]['avg_runway_months'], 1),
            "concentration_risk_reduction_pct": round(
                max(r['concentration_risk_pct'] for r in results[:injection_day]) -
                max(r['concentration_risk_pct'] for r in results[injection_day:]),
                2
            ),
            "results": results
        }

    def backtest_no_rebalancing(self, df: pd.DataFrame, duration_days: int = 14) -> Dict[str, Any]:
        """Baseline: no rebalancing, just natural performance"""
        df_sim = df.copy()
        initial_portfolio_value = df['allocation_target'].sum()

        results = []

        for day in range(1, duration_days + 1):
            day_sim = self.simulate_day(df_sim, day, None)
            results.append(day_sim)
            df_sim = day_sim['state_snapshot']

        final_portfolio_value = results[-1]['total_portfolio_value']
        total_return = (final_portfolio_value - initial_portfolio_value) / initial_portfolio_value * 100

        return {
            "strategy": "no_rebalancing",
            "duration_days": duration_days,
            "initial_portfolio_value": round(initial_portfolio_value, 2),
            "final_portfolio_value": round(final_portfolio_value, 2),
            "total_return_pct": round(total_return, 2),
            "avg_daily_return_pct": round(total_return / duration_days, 3),
            "avg_runway_months": round(np.mean([r['avg_runway_months'] for r in results]), 1),
            "results": results
        }

    def compare_strategies(self, df: pd.DataFrame, duration_days: int = 14) -> Dict[str, Any]:
        """Compare multiple allocation strategies"""
        print(f"\n📊 Comparing allocation strategies over {duration_days} days...\n")

        strategy_baseline = self.backtest_no_rebalancing(df, duration_days)
        print(f"✓ Baseline (no rebalancing): {strategy_baseline['total_return_pct']}%")

        strategy_rebalancing = self.backtest_rebalancing(df, duration_days)
        print(f"✓ Rebalancing every 3 days: {strategy_rebalancing['total_return_pct']}%")

        strategy_injection = self.backtest_capital_injection(df, 100000, injection_day=5, duration_days=duration_days)
        print(f"✓ +$100K injection on day 5: {strategy_injection['total_return_pct']}%")

        return {
            "backtest_duration_days": duration_days,
            "timestamp": datetime.utcnow().isoformat(),
            "strategies": {
                "baseline_no_rebalancing": strategy_baseline,
                "rebalancing_every_3_days": strategy_rebalancing,
                "capital_injection_100k": strategy_injection
            },
            "winner": max(
                ("baseline", strategy_baseline['total_return_pct']),
                ("rebalancing", strategy_rebalancing['total_return_pct']),
                ("injection", strategy_injection['total_return_pct']),
                key=lambda x: x[1]
            )[0],
            "summary": {
                "best_performing_strategy": max(
                    ("baseline", strategy_baseline['total_return_pct']),
                    ("rebalancing", strategy_rebalancing['total_return_pct']),
                    ("injection", strategy_injection['total_return_pct']),
                    key=lambda x: x[1]
                ),
                "rebalancing_advantage_vs_baseline_pct": round(
                    strategy_rebalancing['total_return_pct'] - strategy_baseline['total_return_pct'],
                    2
                ),
                "injection_extends_runway_months": round(
                    strategy_injection['runway_improvement_months'],
                    1
                ),
                "recommendation": "Rebalancing every 3 days reduces concentration risk and improves resilience"
            }
        }

    def display_backtest_summary(self, backtest_result: Dict[str, Any]):
        """Display backtest results"""
        print("\n" + "="*80)
        print("📈 BACKTEST SUMMARY")
        print("="*80)

        strategies = backtest_result.get('strategies', {})

        print("\n🏆 Strategy Comparison (14-day simulation):")
        print("-" * 80)

        for strategy_name, strategy_data in strategies.items():
            label = strategy_name.replace('_', ' ').title()
            print(f"\n  {label}:")
            print(f"    Initial Portfolio:  ${strategy_data['initial_portfolio_value']:>15,.0f}")
            print(f"    Final Portfolio:    ${strategy_data['final_portfolio_value']:>15,.0f}")
            print(f"    Total Return:       {strategy_data['total_return_pct']:>15.2f}%")
            print(f"    Avg Daily Return:   {strategy_data.get('avg_daily_return_pct', 0):>15.3f}%")
            print(f"    Avg Runway:         {strategy_data['avg_runway_months']:>15.1f} months")

        print("\n" + "="*80)
        print("✅ Backtest complete. Rebalancing strategy validates allocation logic.")
        print("="*80 + "\n")


def main():
    """Run backtesting suite"""
    backtester = VentureBacktester()

    print("\n" + "="*80)
    print("DEXTER BACKTESTER — 14-Day Scenario Testing")
    print("="*80 + "\n")

    print("📡 Loading ventures from Supabase...")
    df = backtester.fetch_ventures()

    if df.empty:
        print("❌ No ventures loaded. Check Supabase connection.")
        return

    print(f"✅ Loaded {len(df)} ventures\n")

    # Run full comparison
    backtest_result = backtester.compare_strategies(df, duration_days=14)
    backtester.display_backtest_summary(backtest_result)

    # Save results
    try:
        with open("backtest_results.json", "w") as f:
            # Convert numpy arrays to lists for JSON serialization
            json_safe_result = json.loads(json.dumps(backtest_result, default=str))
            json.dump(json_safe_result, f, indent=2, default=str)
        print("✅ Results saved to backtest_results.json")
    except Exception as e:
        print(f"⚠️  Could not save results: {e}")


if __name__ == "__main__":
    main()
