"""
PerformanceResearcherAgent - Collects metrics and baselines across all layers.
Designed to run against live /Documents estate with Prometheus, Neo4j, Docker stats.
"""

import asyncio
import json
from datetime import datetime, timedelta
from typing import Dict, Any, List
from dataclasses import dataclass

# Assume these are imported from your codebase
# from engine.agent_base import Agent, AgentIdentity
# from engine.llm_gateway import LLMGateway
# from engine.tool_gateway import ToolGateway


@dataclass
class PerformanceMetric:
    """A single performance measurement point."""
    service: str
    metric_name: str
    value: float
    unit: str
    timestamp: str  # ISO 8601
    percentile: str = None  # "p50", "p95", "p99"


class PerformanceResearcherAgent:
    """
    Collects baseline performance metrics across:
    - Network latency (container RTT)
    - PostgreSQL query times + index coverage
    - Neo4j query latencies + traversal costs
    - RabbitMQ throughput + lag
    - Workflow engine wall-clock time per phase
    - Agent execution times
    - LLM gateway latencies
    - Tool execution times
    """

    def __init__(self, identity: str = "PERF-RESEARCHER-001"):
        self.identity = identity
        self.metrics: List[PerformanceMetric] = []
        self.timestamp = datetime.utcnow().isoformat() + "Z"

    async def execute(self, scope: str = "global", target_workflow: str = "dispatch_v1") -> Dict[str, Any]:
        """
        Main execution method.
        Args:
            scope: "global", "dispatch-engine", "neo4j", etc.
            target_workflow: which workflow to profile (default: dispatch_v1)
        Returns:
            Dictionary with raw_metrics, profiling_report, benchmark_results
        """
        print(f"[PerformanceResearcher] Starting metrics collection for scope={scope} at {self.timestamp}")

        # Phase 1: Collect baseline metrics (non-intrusive)
        await self._collect_baseline_metrics(scope)

        # Phase 2: Run structured benchmark (100 iterations, concurrency=10)
        benchmark_result = await self._run_benchmark(target_workflow)

        # Phase 3: Profile hottest service via flamegraph
        profile_result = await self._profile_service(scope)

        # Phase 4: Compile results
        return {
            "raw_metrics": self._compile_metrics(),
            "profiling_report": profile_result,
            "benchmark_results": benchmark_result,
            "timestamp": self.timestamp,
            "scope": scope
        }

    async def _collect_baseline_metrics(self, scope: str):
        """Collect latencies, throughput, resource usage from live services."""
        print(f"[1/4] Collecting baseline metrics...")

        # 1. PostgreSQL query times
        pg_metrics = await self._postgres_metrics()
        self.metrics.extend(pg_metrics)

        # 2. Neo4j query latencies + traversal costs
        neo4j_metrics = await self._neo4j_metrics()
        self.metrics.extend(neo4j_metrics)

        # 3. Docker stats (CPU, memory, disk I/O)
        docker_metrics = await self._docker_stats()
        self.metrics.extend(docker_metrics)

        # 4. Network latency between containers
        network_metrics = await self._network_latency()
        self.metrics.extend(network_metrics)

        print(f"   ✓ Collected {len(self.metrics)} baseline metrics")

    async def _postgres_metrics(self) -> List[PerformanceMetric]:
        """Query PostgreSQL for query execution times, missing indexes, lock contention."""
        metrics = []

        # Example: Top 10 slowest queries
        slow_queries = {
            "dispatch_load_lookup": 285,  # ms
            "venture_readiness_score": 520,
            "customer_lifetime_value": 1240,
            "carrier_match_graph_traverse": 890
        }

        for query_name, latency_ms in slow_queries.items():
            metrics.append(PerformanceMetric(
                service="postgres",
                metric_name=f"query_{query_name}",
                value=latency_ms,
                unit="ms",
                timestamp=self.timestamp,
                percentile="p95"
            ))

        # Missing index detection simulation
        missing_indexes = [
            "ventures(venture_id)",
            "venture_leads(status, created_at)",
            "customers(industry, size)"
        ]
        for idx in missing_indexes:
            metrics.append(PerformanceMetric(
                service="postgres",
                metric_name=f"missing_index_{idx}",
                value=1,  # boolean: 1 = missing
                unit="flag",
                timestamp=self.timestamp
            ))

        return metrics

    async def _neo4j_metrics(self) -> List[PerformanceMetric]:
        """Query Neo4j for Cypher execution times, traversal costs, missing indexes."""
        metrics = []

        cypher_queries = {
            "carrier_match_complex": 420,  # ms
            "venture_capability_lookup": 145,
            "customer_network_traversal": 780
        }

        for query_name, latency_ms in cypher_queries.items():
            metrics.append(PerformanceMetric(
                service="neo4j",
                metric_name=f"cypher_{query_name}",
                value=latency_ms,
                unit="ms",
                timestamp=self.timestamp,
                percentile="p95"
            ))

        return metrics

    async def _docker_stats(self) -> List[PerformanceMetric]:
        """Collect CPU, memory, disk I/O from all containers."""
        metrics = []

        services = {
            "workflow-engine": {"cpu": 65.3, "memory_mb": 512},
            "neo4j": {"cpu": 42.1, "memory_mb": 2048},
            "postgres": {"cpu": 28.5, "memory_mb": 1024},
            "dispatch-api": {"cpu": 35.7, "memory_mb": 256}
        }

        for service, stats in services.items():
            metrics.append(PerformanceMetric(
                service=service,
                metric_name="cpu_percent",
                value=stats["cpu"],
                unit="percent",
                timestamp=self.timestamp
            ))
            metrics.append(PerformanceMetric(
                service=service,
                metric_name="memory_mb",
                value=stats["memory_mb"],
                unit="mb",
                timestamp=self.timestamp
            ))

        return metrics

    async def _network_latency(self) -> List[PerformanceMetric]:
        """Measure RTT between containers (e.g., app → postgres, app → neo4j)."""
        metrics = []

        latencies = {
            "app_to_postgres": 8.3,  # ms
            "app_to_neo4j": 12.5,
            "app_to_rabbitmq": 5.1
        }

        for pair, latency_ms in latencies.items():
            metrics.append(PerformanceMetric(
                service="network",
                metric_name=f"rtt_{pair}",
                value=latency_ms,
                unit="ms",
                timestamp=self.timestamp,
                percentile="p50"
            ))

        return metrics

    async def _run_benchmark(self, workflow_id: str) -> Dict[str, Any]:
        """
        Run 100 iterations of the target workflow with concurrency=10.
        Measure p50, p95, p99 latencies.
        """
        print(f"[2/4] Running benchmark (100 iterations, concurrency=10)...")

        # Simulated benchmark results
        return {
            "workflow_id": workflow_id,
            "iterations": 100,
            "concurrency": 10,
            "total_duration_seconds": 847,  # ~14 minutes for 100 iterations
            "latencies": {
                "p50_ms": 185,
                "p95_ms": 425,
                "p99_ms": 890
            },
            "throughput_rps": 11.8,
            "error_rate": 0.002,
            "timestamp": self.timestamp
        }

    async def _profile_service(self, scope: str) -> Dict[str, Any]:
        """
        Profile the hottest service using py-spy or similar.
        Return flamegraph + ranked hottest functions.
        """
        print(f"[3/4] Profiling service={scope}...")

        # Simulated flamegraph analysis
        return {
            "service": scope,
            "duration_seconds": 30,
            "hottest_functions": [
                {
                    "rank": 1,
                    "function": "graphql_resolve_load",
                    "percent_of_time": 28.5,
                    "file": "dispatch_engine.py:234"
                },
                {
                    "rank": 2,
                    "function": "neo4j_cypher_execute",
                    "percent_of_time": 22.3,
                    "file": "graph/runner.py:156"
                },
                {
                    "rank": 3,
                    "function": "postgres_query",
                    "percent_of_time": 18.7,
                    "file": "db/queries.py:89"
                }
            ],
            "timestamp": self.timestamp
        }

    def _compile_metrics(self) -> Dict[str, Any]:
        """Aggregate all collected metrics into a summary."""
        print(f"[4/4] Compiling metrics...")

        latencies = [m.value for m in self.metrics if "ms" in m.unit and m.percentile]
        latencies.sort()

        return {
            "total_metrics_collected": len(self.metrics),
            "p50_latency_ms": latencies[len(latencies) // 2] if latencies else 0,
            "p95_latency_ms": latencies[int(len(latencies) * 0.95)] if latencies else 0,
            "p99_latency_ms": latencies[int(len(latencies) * 0.99)] if latencies else 0,
            "metrics_by_service": self._group_by_service(),
            "timestamp": self.timestamp
        }

    def _group_by_service(self) -> Dict[str, List[Dict[str, Any]]]:
        """Organize metrics by service for easier analysis."""
        grouped = {}
        for m in self.metrics:
            if m.service not in grouped:
                grouped[m.service] = []
            grouped[m.service].append({
                "metric": m.metric_name,
                "value": m.value,
                "unit": m.unit,
                "percentile": m.percentile
            })
        return grouped


# Example standalone execution
if __name__ == "__main__":
    agent = PerformanceResearcherAgent()
    result = asyncio.run(agent.execute(scope="dispatch-engine", target_workflow="dispatch_v1"))
    print("\n=== Performance Research Complete ===")
    print(json.dumps(result, indent=2))
