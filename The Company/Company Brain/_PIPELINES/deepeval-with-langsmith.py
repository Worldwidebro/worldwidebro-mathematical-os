#!/usr/bin/env python3
"""
Deepeval + LangSmith Integration
Wires deepeval evals to send traces to LangSmith for observability
"""

import os
import json
from typing import Optional, List, Dict
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
    from deepeval.test_case import LLMTestCase
    import requests
except ImportError as e:
    logger.error(f"Missing dependency: {e}")
    logger.error("Install with: pip install deepeval requests")
    exit(1)


class LangSmithTracer:
    """Sends deepeval eval results to LangSmith"""

    def __init__(self):
        self.api_key = os.getenv('LANGSMITH_API_KEY')
        self.endpoint = os.getenv('LANGSMITH_ENDPOINT', 'https://api.smith.langchain.com')
        self.project = os.getenv('LANGSMITH_PROJECT', 'company-brain-evals')

        if not self.api_key:
            logger.warning("LANGSMITH_API_KEY not set - traces won't be sent")
            self.enabled = False
        else:
            self.enabled = True
            logger.info(f"LangSmith tracer initialized (project: {self.project})")

    def send_eval_trace(self, agent_id: str, test_case: dict, metric_name: str, score: float, passed: bool):
        """Send eval result to LangSmith as a trace"""
        if not self.enabled:
            return

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        trace_data = {
            "name": f"eval-{metric_name}-{agent_id}",
            "run_type": "evaluation",
            "inputs": {
                "agent_id": agent_id,
                "metric": metric_name,
                "test_input": test_case.get("input", ""),
            },
            "outputs": {
                "score": score,
                "passed": passed,
                "test_case": test_case.get("name", "unknown"),
            },
            "status": "success" if passed else "failed",
            "start_time": datetime.utcnow().isoformat() + "Z",
            "end_time": datetime.utcnow().isoformat() + "Z",
            "metadata": {
                "agent_id": agent_id,
                "metric_type": metric_name,
                "score": score,
                "source": "deepeval-wrapper"
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
                logger.debug(f"Trace sent: {metric_name} for {agent_id}")
            else:
                logger.warning(f"LangSmith response: {response.status_code}")
        except Exception as e:
            logger.warning(f"Failed to send trace: {str(e)}")


class DeepEvalWithLangSmith:
    """Wrapper combining deepeval metrics + LangSmith observability"""

    def __init__(self):
        self.tracer = LangSmithTracer()
        self.results = []

    def eval_correctness(self, agent_id: str, input_text: str, output_text: str, expected_output: str) -> Dict:
        """Run correctness eval (answer relevancy) with LangSmith tracing"""

        metric = AnswerRelevancyMetric(threshold=0.7)
        test_case = LLMTestCase(
            input=input_text,
            actual_output=output_text,
            expected_output=expected_output
        )

        try:
            metric.measure(test_case)
            score = metric.score
            passed = metric.is_successful()

            # Send to LangSmith
            self.tracer.send_eval_trace(
                agent_id=agent_id,
                test_case={"name": "correctness", "input": input_text},
                metric_name="correctness",
                score=score,
                passed=passed
            )

            result = {
                "agent_id": agent_id,
                "metric": "correctness",
                "score": score,
                "passed": passed,
                "timestamp": datetime.utcnow().isoformat()
            }
            self.results.append(result)
            return result
        except Exception as e:
            logger.error(f"Eval failed: {str(e)}")
            return {"error": str(e)}

    def eval_faithfulness(self, agent_id: str, input_text: str, output_text: str, context: str) -> Dict:
        """Run faithfulness eval (no hallucination) with LangSmith tracing"""

        metric = FaithfulnessMetric(threshold=0.7)
        test_case = LLMTestCase(
            input=input_text,
            actual_output=output_text,
            context=context
        )

        try:
            metric.measure(test_case)
            score = metric.score
            passed = metric.is_successful()

            # Send to LangSmith
            self.tracer.send_eval_trace(
                agent_id=agent_id,
                test_case={"name": "faithfulness", "input": input_text},
                metric_name="faithfulness",
                score=score,
                passed=passed
            )

            result = {
                "agent_id": agent_id,
                "metric": "faithfulness",
                "score": score,
                "passed": passed,
                "timestamp": datetime.utcnow().isoformat()
            }
            self.results.append(result)
            return result
        except Exception as e:
            logger.error(f"Eval failed: {str(e)}")
            return {"error": str(e)}

    def export_results(self, filepath: str = "eval-results.json"):
        """Export all eval results to JSON"""
        with open(filepath, 'w') as f:
            json.dump(self.results, f, indent=2)
        logger.info(f"Results exported to {filepath}")

    def summary(self) -> Dict:
        """Get summary statistics"""
        if not self.results:
            return {"error": "No results yet"}

        passed = sum(1 for r in self.results if r.get("passed", False))
        total = len(self.results)
        avg_score = sum(r.get("score", 0) for r in self.results) / total if total > 0 else 0

        return {
            "total_evals": total,
            "passed": passed,
            "failed": total - passed,
            "pass_rate": passed / total if total > 0 else 0,
            "avg_score": avg_score
        }


# Example usage
if __name__ == "__main__":
    print("🔗 Deepeval + LangSmith Integration Test")
    print("=" * 60)
    print("")

    # Initialize
    evaluator = DeepEvalWithLangSmith()

    # Test case 1: Correctness
    print("Running correctness eval...")
    result1 = evaluator.eval_correctness(
        agent_id="AGT-001",
        input_text="What is the capital of France?",
        output_text="Paris is the capital of France.",
        expected_output="Paris"
    )
    print(f"  Score: {result1.get('score', 'error')}, Passed: {result1.get('passed', False)}")

    # Test case 2: Faithfulness
    print("Running faithfulness eval...")
    result2 = evaluator.eval_faithfulness(
        agent_id="AGT-001",
        input_text="Summarize this context",
        output_text="The summary is accurate.",
        context="This is the original context to check against."
    )
    print(f"  Score: {result2.get('score', 'error')}, Passed: {result2.get('passed', False)}")

    # Summary
    print("")
    print("Summary:")
    summary = evaluator.summary()
    print(f"  Total evals: {summary.get('total_evals', 0)}")
    print(f"  Passed: {summary.get('passed', 0)} / Failed: {summary.get('failed', 0)}")
    print(f"  Pass rate: {summary.get('pass_rate', 0):.1%}")
    print(f"  Avg score: {summary.get('avg_score', 0):.2f}")

    print("")
    print("✅ Integration complete!")
    print("View traces at: https://smith.langchain.com/")
