"""Hierarchical candidate shortlister and calibrated skill resolver for GBrain."""

from __future__ import annotations
import math
import re
import time
from typing import Any, Dict, List, Optional, Tuple
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .dataset import GBrainCorpus
from .schemas import ChoiceCandidate, ChoiceDecision


class SkillResolver:
    """Two-stage resolver: Stage 1 Shortlist (BM25/TF-IDF) -> Stage 2 Calibrated Scoring."""

    def __init__(self, corpus: Optional[GBrainCorpus] = None, top_k: int = 5, confidence_threshold: float = 0.65):
        self.corpus = corpus or GBrainCorpus()
        self.top_k = top_k
        self.confidence_threshold = confidence_threshold
        
        self.skill_names: List[str] = self.corpus.get_skill_names()
        self.skill_docs: List[Dict[str, Any]] = self.corpus.get_skill_documents()
        
        # Build enriched document strings for indexing
        # Each document includes skill name, descriptions, frontmatter triggers, and fixture intents
        self.doc_texts: List[str] = []
        for doc in self.skill_docs:
            skill = doc["skill"]
            meta = self.corpus.skills.get(skill, {})
            fixture_texts = [f["intent"] for f in meta.get("routing_fixtures", [])]
            combined = (
                f"{skill} " * 4
                + f"{meta.get('description', '')} " * 2
                + " ".join(meta.get("triggers", [])) * 3
                + " ".join(fixture_texts)
            )
            self.doc_texts.append(combined)

        # Initialize TF-IDF Vectorizer with sublinear TF and n-grams
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 3),
            sublinear_tf=True,
            stop_words="english",
            token_pattern=r"(?u)\b[\w-]+\b",
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(self.doc_texts)

    def resolve(self, query: str, top_k: Optional[int] = None) -> ChoiceDecision:
        """Resolves an input query into the best matching GBrain skill with calibrated confidence."""
        t0 = time.perf_counter()
        k = top_k or self.top_k
        clean_query = query.strip()
        
        if not clean_query:
            elapsed_ms = (time.perf_counter() - t0) * 1000.0
            return ChoiceDecision(
                decision_name="gbrain_skill_resolve",
                selected="query",
                confidence=0.0,
                fallback=True,
                latency_ms=elapsed_ms,
            )

        # Stage 1: Shortlist retrieval via TF-IDF cosine similarity
        query_vec = self.vectorizer.transform([clean_query])
        raw_scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()

        # Check for direct trigger phrase exact/substring matches to boost precision
        lowered_query = clean_query.lower()
        boosted_scores = np.copy(raw_scores)
        
        for idx, doc in enumerate(self.skill_docs):
            skill = doc["skill"]
            meta = self.corpus.skills.get(skill, {})
            # Check triggers
            for trig in meta.get("triggers", []):
                trig_low = trig.lower().strip()
                if trig_low and (trig_low in lowered_query or lowered_query in trig_low):
                    boosted_scores[idx] += 0.45
                    break
            # Check exact skill name
            if skill.lower() in lowered_query:
                boosted_scores[idx] += 0.35

        # Extract Top-K indices
        top_indices = np.argsort(boosted_scores)[::-1][:k]
        
        # Stage 2: Temperature-scaled Softmax over top candidates
        top_scores = boosted_scores[top_indices]
        temperature = 0.25  # Sharpen the distribution over top candidates
        
        # Softmax computation
        exp_scores = np.exp((top_scores - np.max(top_scores)) / temperature)
        probs = exp_scores / (np.sum(exp_scores) + 1e-9)
        
        candidates: List[ChoiceCandidate] = []
        for idx, prob in zip(top_indices, probs):
            skill_name = self.skill_docs[idx]["skill"]
            candidates.append(ChoiceCandidate(option=skill_name, score=float(np.round(prob, 4))))

        best_candidate = candidates[0] if candidates else ChoiceCandidate(option="query", score=0.0)
        second_score = candidates[1].score if len(candidates) > 1 else 0.0
        margin = float(np.round(best_candidate.score - second_score, 4))

        # Check confidence threshold
        is_fallback = best_candidate.score < self.confidence_threshold or raw_scores[top_indices[0]] < 0.05
        selected = best_candidate.option if not is_fallback else "query"
        calibrated_conf = float(np.round(best_candidate.score if not is_fallback else 0.40, 4))

        elapsed_ms = (time.perf_counter() - t0) * 1000.0

        return ChoiceDecision(
            decision_name="gbrain_skill_resolve",
            selected=selected,
            confidence=calibrated_conf,
            shortlist=candidates,
            margin=margin,
            fallback=is_fallback,
            latency_ms=float(np.round(elapsed_ms, 2)),
        )
