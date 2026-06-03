#!/usr/bin/env python3
"""
Dexter Terminal UI — Week 2 Portfolio Dashboard
Interactive terminal interface for portfolio visualization, rebalancing, and scenario testing
Integrates CFO agent, portfolio optimizer, and forecasting models
"""

import os
import json
import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional
from datetime import datetime
import requests

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://cyhzilqldouzgynacqpe.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")


class DexterTerminal:
    """Terminal UI for Dexter Financial Orchestrator"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {SUPABASE_KEY}"})
        self.ventures_cache = None
        self.portfolio_metrics = None

    def fetch_ventures(self) -> pd.DataFrame:
        """Load ventures from Supabase"""
        try:
            response = self.session.get(
                f"{SUPABASE_URL}/rest/v1/ventures",
                params={"select": "id,name,sector,roi,gross_margin_pct,burn_rate_monthly,runway_months,health_score,allocation_target"}
            )
            if response.status_code == 200:
                data = response.json()
                self.ventures_cache = pd.DataFrame(data)
                return self.ventures_cache
            else:
                print(f"❌ Failed to fetch ventures: {response.status_code}")
                return pd.DataFrame()
        except Exception as e:
            print(f"❌ Fetch ventures error: {e}")
            return pd.DataFrame()

    def portfolio_health_check(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Calculate portfolio health metrics"""
        if df.empty:
            return {}

        total_allocated = df['allocation_target'].sum()
        total_revenue = df['revenue'].sum() if 'revenue' in df.columns else 0
        avg_burn = df['burn_rate_monthly'].mean() if 'burn_rate_monthly' in df.columns else 0
        portfolio_runway = total_allocated / avg_burn if avg_burn > 0 else float('inf')

        # HHI concentration
        weights = df['allocation_target'] / total_allocated if total_allocated > 0 else df['allocation_target']
        hhi = (weights ** 2).sum() * 10000

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "total_capital": round(total_allocated, 2),
            "monthly_revenue": round(total_revenue, 2),
            "average_burn": round(avg_burn, 2),
            "portfolio_runway_months": round(portfolio_runway, 1),
            "average_health_score": round(df['health_score'].mean(), 1),
            "portfolio_roi_percent": round(df['roi'].mean(), 1),
            "concentration_risk_pct": round((df['allocation_target'].max() / total_allocated * 100), 2),
            "hhi_index": round(hhi, 0),
            "venture_count": len(df),
            "low_runway_ventures": len(df[df['runway_months'] < 6]),
            "high_roi_ventures": len(df[df['roi'] > 50])
        }

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
            print("⚠️  PyPortfolioOpt not available. Skipping optimization.")
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
        except Exception as e:
            print(f"⚠️  Efficient frontier error: {e}")
            return {}

    def rebalancing_recommendation(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Compare current vs optimal allocation"""
        if df.empty:
            return {"error": "No venture data"}

        try:
            current_alloc = dict(zip(df['id'], df['allocation_target']))
            total_current = sum(current_alloc.values())

            current_weights = {k: v / total_current if total_current > 0 else 0 for k, v in current_alloc.items()}
            optimal_weights = self.efficient_frontier(df)

            moves = {}
            for venture_id in df['id']:
                current_w = current_weights.get(venture_id, 0)
                optimal_w = optimal_weights.get(venture_id, 0)
                delta = optimal_w - current_w

                if abs(delta) > 0.01:
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
                }
            }
        except Exception as e:
            print(f"⚠️  Rebalancing error: {e}")
            return {"error": str(e)}

    def scenario_test(self, df: pd.DataFrame, additional_capital: float = 0) -> Dict[str, Any]:
        """Test: what if portfolio received $X capital?"""
        if df.empty:
            return {"error": "No venture data"}

        try:
            current_total = df['allocation_target'].sum()
            new_total = current_total + additional_capital
            optimal_weights = self.efficient_frontier(df)

            new_allocation = {vid: (w * new_total) for vid, w in optimal_weights.items()}
            old_concentration = (df['allocation_target'].max() / current_total * 100) if current_total > 0 else 0
            new_concentration = (max(new_allocation.values()) / new_total * 100) if new_total > 0 else 0

            return {
                "scenario": "capital_injection",
                "additional_capital": round(additional_capital, 2),
                "previous_total": round(current_total, 2),
                "new_total": round(new_total, 2),
                "concentration_before_pct": round(old_concentration, 2),
                "concentration_after_pct": round(new_concentration, 2),
            }
        except Exception as e:
            return {"error": str(e)}

    def display_header(self):
        """Display Dexter terminal header"""
        print("\n" + "="*80)
        print(" " * 20 + "DEXTER FINANCIAL ORCHESTRATOR")
        print(" " * 25 + "Portfolio Dashboard")
        print("="*80 + "\n")

    def display_portfolio_health(self, health: Dict[str, Any]):
        """Display portfolio health metrics"""
        print("📊 PORTFOLIO HEALTH CHECK")
        print("-" * 80)
        print(f"  Total Capital:           ${health['total_capital']:>15,.0f}")
        print(f"  Monthly Revenue:         ${health['monthly_revenue']:>15,.0f}")
        print(f"  Average Burn Rate:       ${health['average_burn']:>15,.0f}")
        print(f"  Portfolio Runway:        {health['portfolio_runway_months']:>15.1f} months")
        print(f"  Avg Health Score:        {health['average_health_score']:>15.1f} / 100")
        print(f"  Avg ROI:                 {health['portfolio_roi_percent']:>15.1f}%")
        print(f"  Concentration Risk:      {health['concentration_risk_pct']:>15.2f}%")
        print(f"  HHI Index:               {health['hhi_index']:>15.0f} {'(Competitive)' if health['hhi_index'] < 1500 else '(Concentrated)'}")
        print(f"  Ventures:                {health['venture_count']:>15} total")
        print(f"  Low Runway (<6mo):       {health['low_runway_ventures']:>15} ventures")
        print(f"  High ROI (>50%):         {health['high_roi_ventures']:>15} ventures")
        print()

    def display_rebalancing(self, rebal: Dict[str, Any]):
        """Display rebalancing recommendations"""
        print("🎯 REBALANCING RECOMMENDATIONS")
        print("-" * 80)
        summary = rebal.get('summary', {})
        print(f"  Total Moves:             {summary.get('moves_suggested', 0):>15} recommended")
        print(f"  Increases:               {summary.get('increases', 0):>15} ventures")
        print(f"  Decreases:               {summary.get('decreases', 0):>15} ventures")
        print()

        if rebal.get('recommendations'):
            print("  Top Recommendations:")
            print("  " + "-" * 76)
            for i, (vid, rec) in enumerate(list(rebal['recommendations'].items())[:5]):
                action_symbol = "↑" if rec["action"] == "INCREASE" else "↓"
                print(f"    {action_symbol} {vid:12} {rec['current_weight']:>6.2f}% → {rec['optimal_weight']:>6.2f}% ({rec['delta_percent']:>+6.2f}%)")
            if len(rebal['recommendations']) > 5:
                print(f"    ... and {len(rebal['recommendations']) - 5} more")
            print()

    def display_risk_matrix(self, df: pd.DataFrame):
        """Display venture risk matrix"""
        print("⚠️  VENTURE RISK MATRIX (sorted by runway)")
        print("-" * 80)

        df_sorted = df.sort_values('runway_months')
        for _, row in df_sorted.head(10).iterrows():
            runway_status = "🔴" if row['runway_months'] < 3 else "🟡" if row['runway_months'] < 6 else "🟢"
            roi_status = "⭐" if row['roi'] > 100 else "✓" if row['roi'] > 50 else ""
            print(f"  {runway_status} {row['id']:12} | Runway: {row['runway_months']:>5.1f}mo | Health: {row['health_score']:>3.0f} | ROI: {row['roi']:>6.1f}% {roi_status}")
        print()

    def display_sector_breakdown(self, df: pd.DataFrame):
        """Display sector distribution"""
        print("🏢 SECTOR BREAKDOWN")
        print("-" * 80)

        sector_data = df.groupby('sector').agg({
            'allocation_target': 'sum',
            'id': 'count',
            'roi': 'mean',
            'health_score': 'mean'
        }).round(1)

        total_alloc = sector_data['allocation_target'].sum()
        for sector, row in sector_data.iterrows():
            pct = (row['allocation_target'] / total_alloc * 100) if total_alloc > 0 else 0
            print(f"  {sector:15} | ${row['allocation_target']:>12,.0f} ({pct:>5.1f}%) | {int(row['id']):>2} ventures | Avg ROI: {row['roi']:>6.1f}% | Health: {row['health_score']:>5.1f}")
        print()

    def interactive_menu(self, df: pd.DataFrame):
        """Interactive terminal menu"""
        while True:
            print("\n📋 COMMANDS:")
            print("  [H] Health Check       [R] Rebalancing        [S] Scenario (+$K)")
            print("  [M] Risk Matrix        [B] Sector Breakdown   [Q] Quit")
            print()

            cmd = input("Command: ").strip().upper()

            if cmd == "Q":
                print("\n👋 Exiting Dexter Terminal")
                break
            elif cmd == "H":
                health = self.portfolio_health_check(df)
                self.display_portfolio_health(health)
            elif cmd == "R":
                rebal = self.rebalancing_recommendation(df)
                self.display_rebalancing(rebal)
            elif cmd == "M":
                self.display_risk_matrix(df)
            elif cmd == "B":
                self.display_sector_breakdown(df)
            elif cmd == "S":
                try:
                    capital = float(input("Additional capital ($K): ")) * 1000
                    scenario = self.scenario_test(df, capital)
                    print(f"\n💰 SCENARIO: +${scenario['additional_capital']:,.0f}")
                    print(f"  Previous Total: ${scenario['previous_total']:,.0f}")
                    print(f"  New Total:      ${scenario['new_total']:,.0f}")
                    print(f"  Concentration:  {scenario['concentration_before_pct']:.2f}% → {scenario['concentration_after_pct']:.2f}%\n")
                except ValueError:
                    print("Invalid input")
            else:
                print("Unknown command")

    def run(self):
        """Run the Dexter terminal"""
        self.display_header()

        print("📡 Loading ventures from Supabase...")
        df = self.fetch_ventures()

        if df.empty:
            print("❌ No ventures loaded. Check Supabase connection and SUPABASE_KEY.")
            return

        print(f"✅ Loaded {len(df)} ventures\n")

        # Display initial metrics
        health = self.portfolio_health_check(df)
        self.display_portfolio_health(health)

        rebal = self.rebalancing_recommendation(df)
        self.display_rebalancing(rebal)

        self.display_risk_matrix(df)
        self.display_sector_breakdown(df)

        # Interactive menu
        self.interactive_menu(df)


def main():
    terminal = DexterTerminal()
    terminal.run()


if __name__ == "__main__":
    main()
