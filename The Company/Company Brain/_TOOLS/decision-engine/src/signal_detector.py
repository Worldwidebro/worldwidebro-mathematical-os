"""Ambient signal detector for original thinking and entity mentions."""

from __future__ import annotations
import re
import time
from typing import List, Optional, Set, Tuple
import numpy as np

from .schemas import SignalDetectionResult


class AmbientSignalDetector:
    """Evaluates conversation turns in sub-5ms for original thinking and entity extraction."""

    # Core linguistic cues for original frameworks, architectural theses, and mental models
    THESIS_PATTERNS = [
        r"\b(?:my|our|the)\s+(?:thesis|insight|hypothesis|observation|framework|mental model)\b",
        r"\b(?:here is|this is)\s+(?:how|why|what)\s+(?:we|the system|it)\b",
        r"\b(?:we should|we must|instead of|rather than)\b",
        r"\b(?:acts? as|functions? as|serves? as)\s+a\b",
        r"\b(?:reflex arc|cerebral cortex|architecture|operating system|control plane)\b",
        r"\b(?:the key idea|the core principle|the mental model|first principles)\b",
        r"\b(?:decouple|decoupling|orthogonal|sub-millisecond|zero-token)\b",
        r"\b(?:rule|law|axiom|invariant)\s*#?\d*:",
    ]

    # Category classification keywords
    CATEGORY_MAP = {
        "ARCHITECTURE": [
            "architecture", "layer", "orchestrator", "router", "reflex", "stack", "pipeline", "subsystem"
        ],
        "VENTURE_STRATEGY": [
            "venture", "holding", "monetization", "unit economics", "cac", "ltv", "margin", "market", "pricing"
        ],
        "OPERATIONAL_RULE": [
            "rule", "invariant", "sop", "protocol", "policy", "standard", "gate", "discipline"
        ],
        "SYSTEM_ENGINEERING": [
            "database", "latency", "pglite", "neo4j", "qdrant", "mps", "onnx", "tensor", "token", "cache"
        ],
    }

    # Entity pattern recognizers (tools, organizations, systems, repos, handles)
    ENTITY_PATTERNS = [
        r"\b[A-Z]{2,}-\d{3}\b",                      # OPCO/Venture codes like OPS-001, LT-005, CP-028
        r"\b(?:Laya|OmniRoute|GBrain|GStack|Neo4j|Qdrant|LiteLLM|Supabase|PostgreSQL|PGLite|ModernBERT|DeBERTa|Ollama|FastAPI)\b",
        r"\b(?:WorldwideBro|HealthRoute|Vex|Company Brain)\b",
        r"\b(?:Claude|OpenAI|Anthropic|Gemini|Mistral)\b",
        r"\b[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+\b",        # GitHub repos e.g. NandhaKishorM/laya
    ]

    # Low-signal noise / routine chatter patterns
    NOISE_PATTERNS = [
        r"^(?:ok|okay|yes|no|thanks|thank you|sounds good|proceed|commit and push|git status|ls|done)\b",
        r"^(?:hello|hi|hey|good morning|what's up)\b",
    ]

    def __init__(self, high_signal_threshold: int = 3):
        self.high_signal_threshold = high_signal_threshold
        self.thesis_regexes = [re.compile(p, re.IGNORECASE) for p in self.THESIS_PATTERNS]
        self.entity_regexes = [re.compile(p) for p in self.ENTITY_PATTERNS]
        self.noise_regexes = [re.compile(p, re.IGNORECASE) for p in self.NOISE_PATTERNS]

    def detect(self, text: str) -> SignalDetectionResult:
        """Evaluates text payload and outputs a structured SignalDetectionResult."""
        t0 = time.perf_counter()
        clean = text.strip()
        
        if not clean:
            elapsed_ms = (time.perf_counter() - t0) * 1000.0
            return SignalDetectionResult(
                is_original_thought=False,
                contains_entity=False,
                entities=[],
                signal_strength=1,
                recommended_action="PASS",
                rationale="Empty payload",
                confidence=1.0,
                latency_ms=elapsed_ms,
            )

        # Check for noise
        is_routine_noise = any(r.search(clean) for r in self.noise_regexes) and len(clean.split()) < 6

        # 1. Detect Thesis / Original Thinking
        thesis_matches = sum(1 for r in self.thesis_regexes if r.search(clean))
        word_count = len(clean.split())
        
        # Original thinking score
        has_thesis_syntax = thesis_matches >= 1 or (" vs " in clean.lower() and word_count > 15)
        has_structural_depth = word_count >= 30 and (":" in clean or "→" in clean or "•" in clean or "\n" in clean)
        
        is_original_thought = bool((has_thesis_syntax or has_structural_depth) and not is_routine_noise)

        # 2. Detect Entities
        found_entities: Set[str] = set()
        for r in self.entity_regexes:
            for match in r.finditer(clean):
                found_entities.add(match.group(0))
        
        contains_entity = len(found_entities) > 0

        # 3. Categorize Thought
        thought_category = None
        if is_original_thought:
            lowered = clean.lower()
            for cat, keywords in self.CATEGORY_MAP.items():
                if any(kw in lowered for kw in keywords):
                    thought_category = cat
                    break
            if not thought_category:
                thought_category = "CONCEPT"

        # 4. Compute Signal Strength (1 - 5)
        if is_routine_noise:
            signal_strength = 1
        else:
            base_score = 1
            if contains_entity:
                base_score += 1
            if is_original_thought:
                base_score += 2
            if thesis_matches >= 2:
                base_score += 1
            if word_count > 80 and has_structural_depth:
                base_score += 1
            signal_strength = min(5, max(1, base_score))

        # 5. Determine Recommended Action
        if signal_strength >= self.high_signal_threshold and is_original_thought:
            action = "STORE_CONCEPT"
            rationale = f"Detected high-value {thought_category} thesis with strength {signal_strength}/5."
        elif contains_entity and signal_strength >= 2:
            action = "STORE_ENTITY"
            rationale = f"Detected {len(found_entities)} key domain entities."
        else:
            action = "PASS"
            rationale = "Routine interaction or low-salience statement."

        # Calibrate confidence
        conf = 0.95 if is_routine_noise or signal_strength >= 4 else 0.82
        elapsed_ms = (time.perf_counter() - t0) * 1000.0

        return SignalDetectionResult(
            is_original_thought=is_original_thought,
            thought_category=thought_category,
            contains_entity=contains_entity,
            entities=sorted(list(found_entities)),
            signal_strength=signal_strength,
            recommended_action=action,
            rationale=rationale,
            confidence=float(np.round(conf, 4)),
            latency_ms=float(np.round(elapsed_ms, 2)),
        )
