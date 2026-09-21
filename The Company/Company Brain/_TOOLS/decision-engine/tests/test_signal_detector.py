"""Unit tests for AmbientSignalDetector."""

from src.signal_detector import AmbientSignalDetector


def test_high_signal_architectural_thesis():
    detector = AmbientSignalDetector()
    text = (
        "Here is my thesis on the Company Brain: We need to decouple the high-speed "
        "reflex arc from the cerebral cortex LLMs. Laya acts as the spinal reflex while OmniRoute "
        "dispatches to Claude."
    )
    res = detector.detect(text)
    assert res.is_original_thought is True
    assert res.thought_category == "ARCHITECTURE"
    assert res.signal_strength >= 3
    assert res.recommended_action == "STORE_CONCEPT"
    assert "Company Brain" in res.entities
    assert "Laya" in res.entities


def test_low_signal_chatter():
    detector = AmbientSignalDetector()
    res = detector.detect("ok thanks, sounds good!")
    assert res.is_original_thought is False
    assert res.signal_strength == 1
    assert res.recommended_action == "PASS"


def test_entity_mention():
    detector = AmbientSignalDetector()
    res = detector.detect("Please check if LT-005 and OPS-001 have updated registries.")
    assert res.contains_entity is True
    assert "LT-005" in res.entities
    assert "OPS-001" in res.entities
