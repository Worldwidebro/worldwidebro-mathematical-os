#!/usr/bin/env python3
"""
Direct LangSmith Integration for Eval Harness
No deepeval dependency — pure traces to LangSmith
"""

import os
import json
import time
from datetime import datetime
from typing import Dict, List
import requests

class EvalHarnessLangSmith:
    """Send eval results directly to LangSmith"""

    def __init__(self):
        self.api_key = os.getenv('LANGSMITH_API_KEY')
        self.endpoint = os.getenv('LANGSMITH_ENDPOINT', 'https://api.smith.langchain.com')
        self.project = os.getenv('LANGSMITH_PROJECT', 'company-brain-evals')
        self.results = []

        if not self.api_key:
            raise ValueError("LANGSMITH_API_KEY not set")

        print(f"✅ LangSmith configured:")
        print(f"   Project: {self.project}")
        print(f"   Endpoint: {self.endpoint}")
        print()

    def send_eval(self, agent_id: str, metric: str, score: float, passed: bool, details: Dict = None):
        """Send eval result to LangSmith"""

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        trace_data = {
            "name": f"eval-{metric}-{agent_id}",
            "run_type": "evaluation",
            "inputs": {
                "agent_id": agent_id,
                "metric_type": metric,
            },
            "outputs": {
                "score": score,
                "passed": passed,
                **(details or {})
            },
            "status": "success" if passed else "failed",
            "start_time": datetime.utcnow().isoformat() + "Z",
            "end_time": datetime.utcnow().isoformat() + "Z",
            "metadata": {
                "agent_id": agent_id,
                "metric": metric,
                "score": score,
                "phase": "phase-0-week1",
                "source": "company-brain-evals"
            }
        }

        try:
            response = requests.post(
                f"{self.endpoint}/api/v1/runs",
                headers=headers,
                json=trace_data,
                timeout=5
            )

            if response.status_code in [200, 201]:
                result_data = {
                    "agent_id": agent_id,
                    "metric": metric,
                    "score": score,
                    "passed": passed,
                    "timestamp": datetime.utcnow().isoformat(),
                    "status": "sent_to_langsmith"
                }
                self.results.append(result_data)
                return result_data
            else:
                print(f"⚠️ LangSmith response: {response.status_code}")
                print(f"   Body: {response.text[:200]}")
                return {"error": response.status_code}
        except Exception as e:
            print(f"❌ Failed to send: {str(e)}")
            return {"error": str(e)}

    def run_baseline_evals(self, agents: List[str], num_evals: int = 3):
        """Run baseline evals on agent sample"""

        print(f"🚀 Running baseline evals")
        print(f"   Agents: {len(agents)}")
        print(f"   Evals per agent: {num_evals}")
        print()

        metrics = ["correctness", "speed", "safety", "cost", "reliability"]
        total = 0

        for agent_id in agents:
            for metric in metrics[:num_evals]:
                # Simulate eval score (0-1)
                score = 0.5 + (hash(f"{agent_id}-{metric}") % 50) / 100
                passed = score > 0.7

                result = self.send_eval(
                    agent_id=agent_id,
                    metric=metric,
                    score=score,
                    passed=passed,
                    details={"comment": f"Baseline eval for {metric}"}
                )

                if "status" in result:
                    total += 1
                    status = "✅" if passed else "⚠️"
                    print(f"  {status} {agent_id} | {metric:<12} | {score:.2f}")

        print()
        print(f"✅ Sent {total} evals to LangSmith")
        return self.results

    def summary(self):
        """Print summary statistics"""
        if not self.results:
            return {}

        passed = sum(1 for r in self.results if r.get("passed", False))
        total = len(self.results)
        avg_score = sum(r.get("score", 0) for r in self.results) / total

        summary = {
            "total_evals": total,
            "passed": passed,
            "failed": total - passed,
            "pass_rate": passed / total if total > 0 else 0,
            "avg_score": avg_score
        }

        print("=" * 60)
        print("EVAL SUMMARY")
        print("=" * 60)
        print(f"Total evals sent: {summary['total_evals']}")
        print(f"Passed: {summary['passed']} | Failed: {summary['failed']}")
        print(f"Pass rate: {summary['pass_rate']:.1%}")
        print(f"Avg score: {summary['avg_score']:.2f}")
        print("=" * 60)

        return summary

if __name__ == "__main__":
    print("🔗 Eval Harness → LangSmith Integration")
    print("=" * 60)
    print()

    try:
        harness = EvalHarnessLangSmith()

        # Run baseline evals on 10-agent sample
        sample_agents = [f"AGT-{i:03d}" for i in range(1, 11)]

        results = harness.run_baseline_evals(
            agents=sample_agents,
            num_evals=3  # correctness, speed, safety
        )

        # Print summary
        summary = harness.summary()

        print()
        print("✨ Integration complete!")
        print()
        print("View your traces at:")
        print("  https://smith.langchain.com/")

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
