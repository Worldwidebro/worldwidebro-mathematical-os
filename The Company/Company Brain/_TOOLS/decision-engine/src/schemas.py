"""Typed decision definitions matching Laya contracts and Company Brain standards."""

from __future__ import annotations
from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel, Field


class ChoiceCandidate(BaseModel):
    """A scored candidate option in a choice decision."""
    option: str
    score: float = Field(..., ge=0.0, le=1.0)


class ChoiceDecision(BaseModel):
    """Multiclass selection decision with candidate ranking and confidence."""
    decision_name: str
    selected: str
    confidence: float = Field(..., ge=0.0, le=1.0)
    shortlist: List[ChoiceCandidate] = Field(default_factory=list)
    margin: float = Field(0.0, description="Score delta between 1st and 2nd candidate")
    fallback: bool = Field(False, description="Whether fallback was invoked due to low confidence")
    latency_ms: float = Field(0.0, ge=0.0)


class ScoreDecision(BaseModel):
    """Ordinal or bounded numeric score decision."""
    decision_name: str
    score: float
    min_score: float = 1.0
    max_score: float = 5.0
    confidence: float = Field(..., ge=0.0, le=1.0)
    latency_ms: float = Field(0.0, ge=0.0)


class NoulDecision(BaseModel):
    """Calibrated boolean decision (True/False)."""
    decision_name: str
    value: bool
    probability: float = Field(..., ge=0.0, le=1.0)
    confidence: float = Field(..., ge=0.0, le=1.0)
    latency_ms: float = Field(0.0, ge=0.0)


class SignalDetectionResult(BaseModel):
    """Composite ambient signal capture evaluation."""
    is_original_thought: bool
    thought_category: Optional[str] = None
    contains_entity: bool
    entities: List[str] = Field(default_factory=list)
    signal_strength: int = Field(..., ge=1, le=5)
    recommended_action: Literal["STORE_CONCEPT", "STORE_ENTITY", "PASS"]
    rationale: str
    confidence: float = Field(..., ge=0.0, le=1.0)
    latency_ms: float = Field(0.0, ge=0.0)
