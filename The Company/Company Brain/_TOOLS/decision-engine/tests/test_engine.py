"""Integration tests for DecisionEngine facade."""

from src.engine import DecisionEngine


def test_decision_engine_facade():
    engine = DecisionEngine()
    
    # 1. Resolve skill
    route = engine.resolve_skill("Who is Paul Graham?")
    assert route.selected == "query"
    assert route.confidence > 0.60
    
    # 2. Detect signal
    signal = engine.detect_signal("The architecture should decouple reflex from reasoning.")
    assert signal.is_original_thought is True
    assert signal.signal_strength >= 3
    
    # 3. Evaluate turn
    turn_eval = engine.evaluate_turn("Here is our strategy for LT-005 dispatch: route all STAT orders immediately.")
    assert turn_eval["signal"]["contains_entity"] is True
    assert turn_eval["total_reflex_latency_ms"] < 20.0
    assert "LT-005" in turn_eval["signal"]["entities"]
