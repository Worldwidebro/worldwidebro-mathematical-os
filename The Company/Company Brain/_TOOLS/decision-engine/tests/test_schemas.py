"""Unit tests for typed decision schemas."""

import pytest
from src.schemas import ChoiceCandidate, ChoiceDecision, ScoreDecision, NoulDecision, SignalDetectionResult


def test_choice_decision():
    cands = [
        ChoiceCandidate(option="query", score=0.85),
        ChoiceCandidate(option="enrich", score=0.10),
    ]
    dec = ChoiceDecision(
        decision_name="test_choice",
        selected="query",
        confidence=0.85,
        shortlist=cands,
        margin=0.75,
        fallback=False,
        latency_ms=1.2,
    )
    assert dec.selected == "query"
    assert dec.confidence == 0.85
    assert len(dec.shortlist) == 2
    assert dec.margin == 0.75


def test_score_decision():
    score = ScoreDecision(
        decision_name="urgency_score",
        score=4.0,
        min_score=1.0,
        max_score=5.0,
        confidence=0.92,
        latency_ms=0.5,
    )
    assert score.score == 4.0
    assert score.confidence == 0.92


def test_noul_decision():
    noul = NoulDecision(
        decision_name="is_safe",
        value=True,
        probability=0.98,
        confidence=0.98,
        latency_ms=0.4,
    )
    assert noul.value is True
    assert noul.probability == 0.98


def test_signal_detection_result():
    res = SignalDetectionResult(
        is_original_thought=True,
        thought_category="ARCHITECTURE",
        contains_entity=True,
        entities=["GBrain", "Laya"],
        signal_strength=4,
        recommended_action="STORE_CONCEPT",
        rationale="High-value architectural thesis",
        confidence=0.95,
        latency_ms=0.2,
    )
    assert res.is_original_thought is True
    assert res.recommended_action == "STORE_CONCEPT"
    assert "GBrain" in res.entities
