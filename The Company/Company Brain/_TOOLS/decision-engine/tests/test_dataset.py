"""Unit tests for corpus extraction."""

from src.dataset import GBrainCorpus


def test_corpus_loading():
    corpus = GBrainCorpus()
    assert len(corpus.skills) >= 70, f"Expected at least 70 skills, found {len(corpus.skills)}"
    assert len(corpus.fixtures) > 200, f"Expected >200 fixtures, found {len(corpus.fixtures)}"
    
    # Check that core skills exist
    assert "query" in corpus.skills
    assert "signal-detector" in corpus.skills
    assert "brain-taxonomist" in corpus.skills
    assert "eiirp" in corpus.skills
