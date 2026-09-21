"""Unit and accuracy tests for SkillResolver."""

from src.resolver import SkillResolver


def test_resolver_basic():
    resolver = SkillResolver()
    
    # Query intent
    res = resolver.resolve("Who is Paul Graham and what has he written about startups")
    assert res.selected == "query"
    assert res.confidence > 0.60
    assert res.latency_ms < 20.0

    # Taxonomy intent
    res2 = resolver.resolve("where does this brain page go")
    assert res2.selected == "brain-taxonomist"
    assert res2.confidence > 0.60


def test_resolver_latency():
    resolver = SkillResolver()
    res = resolver.resolve("Tell me about the recent funding rounds for Acme")
    assert res.latency_ms < 10.0, f"Expected latency <10ms, got {res.latency_ms}ms"
