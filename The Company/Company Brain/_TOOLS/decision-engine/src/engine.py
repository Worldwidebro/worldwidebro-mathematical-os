"""Unified DecisionEngine facade for Company Brain and GBrain."""

from __future__ import annotations
import time
from typing import Any, Dict, List, Optional
from pathlib import Path
import numpy as np

from .dataset import GBrainCorpus
from .resolver import SkillResolver
from .signal_detector import AmbientSignalDetector
from .schemas import ChoiceDecision, SignalDetectionResult


class DecisionEngine:
    """The central high-speed reflex coordinator for Company Brain."""

    def __init__(self, workspace_root: Optional[Path] = None):
        self.corpus = GBrainCorpus(workspace_root=workspace_root)
        self.resolver = SkillResolver(corpus=self.corpus)
        self.signal_detector = AmbientSignalDetector()

    def resolve_skill(self, query: str, top_k: int = 5) -> ChoiceDecision:
        """Resolves natural language input to a target GBrain skill in sub-15ms."""
        return self.resolver.resolve(query, top_k=top_k)

    def detect_signal(self, text: str) -> SignalDetectionResult:
        """Evaluates ambient input for original thought, entities, and writeback trigger in sub-5ms."""
        return self.signal_detector.detect(text)

    def evaluate_turn(self, text: str) -> Dict[str, Any]:
        """Runs the complete reflex arc (signal detection + skill routing) over an incoming turn."""
        t0 = time.perf_counter()
        signal_res = self.detect_signal(text)
        route_res = self.resolve_skill(text)
        total_latency = (time.perf_counter() - t0) * 1000.0

        return {
            "signal": signal_res.model_dump(),
            "routing": route_res.model_dump(),
            "total_reflex_latency_ms": round(total_latency, 2),
            "reflex_action": {
                "writeback_recommended": signal_res.recommended_action != "PASS",
                "recommended_action": signal_res.recommended_action,
                "target_skill": route_res.selected,
                "routing_confidence": route_res.confidence,
            },
        }

    def benchmark_resolver(self) -> Dict[str, Any]:
        """Runs evaluation over all fixtures in gbrain/skills/*/routing-eval.jsonl."""
        fixtures = self.corpus.get_all_fixtures()
        if not fixtures:
            return {"status": "NO_FIXTURES", "total": 0}

        correct_top1 = 0
        correct_top3 = 0
        latencies = []

        for f in fixtures:
            intent = f["intent"]
            expected = f["expected_skill"]
            ambiguous = f.get("ambiguous_with", [])
            allowed = {expected} | set(ambiguous)

            dec = self.resolve_skill(intent, top_k=3)
            latencies.append(dec.latency_ms)

            # Top 1 accuracy
            if dec.selected in allowed:
                correct_top1 += 1

            # Top 3 accuracy
            top3_options = [c.option for c in dec.shortlist[:3]]
            if any(opt in allowed for opt in top3_options):
                correct_top3 += 1

        total = len(fixtures)
        top1_acc = correct_top1 / total if total > 0 else 0.0
        top3_acc = correct_top3 / total if total > 0 else 0.0
        avg_latency = sum(latencies) / len(latencies) if latencies else 0.0

        return {
            "total_fixtures": total,
            "top1_accuracy": round(top1_acc, 4),
            "top3_accuracy": round(top3_acc, 4),
            "p95_latency_ms": round(float(np.percentile(latencies, 95)), 2) if latencies else 0.0,
            "mean_latency_ms": round(avg_latency, 2),
        }
