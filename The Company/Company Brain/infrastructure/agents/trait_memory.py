"""
Trait Memory Builder
Agents learn entity preferences over time
Confidence scores improve as decisions prove correct
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
import math
import logging

from memory_config import MemoryClient

logger = logging.getLogger(__name__)


@dataclass
class Trait:
    """Learned characteristic of an entity"""
    entity_id: str
    category: str  # "communication_style", "budget_preference", "risk_tolerance"
    value: str  # "prefers_email", "high_budget", "risk_averse"
    initial_confidence: float = 0.7
    current_confidence: float = 0.7
    observations: int = 1
    correct_predictions: int = 1
    learned_at: datetime = None
    last_reinforced: datetime = None

    def __post_init__(self):
        if self.learned_at is None:
            self.learned_at = datetime.utcnow()
        if self.last_reinforced is None:
            self.last_reinforced = datetime.utcnow()

    def reinforce(self, correct: bool):
        """Update confidence based on prediction outcome"""
        self.observations += 1

        if correct:
            self.correct_predictions += 1

        # Update confidence using Bayesian-like approach
        accuracy = self.correct_predictions / self.observations

        # Confidence increases with accuracy, decreases if wrong
        if correct:
            self.current_confidence = min(
                0.99,
                self.current_confidence + (1 - self.current_confidence) * 0.1
            )
        else:
            self.current_confidence = max(
                0.3,
                self.current_confidence - 0.15
            )

        self.last_reinforced = datetime.utcnow()
        logger.info(
            f"Trait {self.entity_id}.{self.category}: "
            f"confidence {self.current_confidence:.2f} after {self.observations} obs"
        )

    def decay(self, days_since_update: int):
        """Decay confidence over time"""
        decay_factor = 0.95 ** (days_since_update / 7)  # Decay by 5% per week
        self.current_confidence *= decay_factor

    def is_strong(self, threshold: float = 0.75) -> bool:
        """Is confidence strong enough to use?"""
        return self.current_confidence >= threshold


class TraitMemory:
    """
    Manage entity traits (preferences, patterns, risk profiles)
    Traits are learned from outcomes over time
    """

    def __init__(self, memory_client: MemoryClient):
        self.memory_client = memory_client
        self.traits: Dict[str, Dict[str, Trait]] = {}  # entity_id -> {category: trait}

    async def add_trait(
        self,
        entity_id: str,
        category: str,
        value: str,
        confidence: float = 0.7
    ) -> Trait:
        """Add new trait to entity"""
        trait = Trait(
            entity_id=entity_id,
            category=category,
            value=value,
            initial_confidence=confidence,
            current_confidence=confidence
        )

        if entity_id not in self.traits:
            self.traits[entity_id] = {}

        self.traits[entity_id][category] = trait

        # Persist to Neo4j
        await self.memory_client.add_preference(
            entity_id=entity_id,
            category=category,
            preference=value,
            confidence=confidence
        )

        return trait

    async def get_trait(self, entity_id: str, category: str) -> Optional[Trait]:
        """Get learned trait for entity"""
        if entity_id not in self.traits:
            return None

        trait = self.traits[entity_id].get(category)

        if trait:
            # Apply decay if old
            days_since = (datetime.utcnow() - trait.last_reinforced).days
            if days_since > 0:
                trait.decay(days_since)

        return trait

    async def get_strong_traits(
        self,
        entity_id: str,
        threshold: float = 0.75
    ) -> Dict[str, Trait]:
        """Get all high-confidence traits for entity"""
        if entity_id not in self.traits:
            return {}

        return {
            cat: trait for cat, trait in self.traits[entity_id].items()
            if trait.is_strong(threshold)
        }

    async def reinforce_trait(
        self,
        entity_id: str,
        category: str,
        correct: bool
    ) -> Optional[Trait]:
        """Update trait confidence based on outcome"""
        trait = await self.get_trait(entity_id, category)

        if not trait:
            return None

        trait.reinforce(correct)

        # Update Neo4j
        await self.memory_client.add_preference(
            entity_id=entity_id,
            category=category,
            preference=trait.value,
            confidence=trait.current_confidence
        )

        return trait

    async def predict_preference(
        self,
        entity_id: str,
        category: str
    ) -> Optional[Dict]:
        """Predict entity's preference based on learned traits"""
        trait = await self.get_trait(entity_id, category)

        if not trait:
            return None

        return {
            "value": trait.value,
            "confidence": trait.current_confidence,
            "is_strong": trait.is_strong(),
            "observations": trait.observations
        }

    async def get_entity_profile(self, entity_id: str) -> Dict:
        """Get complete preference profile for entity"""
        traits = self.traits.get(entity_id, {})

        profile = {
            "entity_id": entity_id,
            "traits": {},
            "confidence_average": 0,
            "learned_categories": list(traits.keys())
        }

        if traits:
            confidences = []
            for category, trait in traits.items():
                profile["traits"][category] = {
                    "value": trait.value,
                    "confidence": trait.current_confidence,
                    "observations": trait.observations
                }
                confidences.append(trait.current_confidence)

            profile["confidence_average"] = sum(confidences) / len(confidences)

        return profile


# Agent learning loop (runs daily)
async def run_trait_learning_loop(
    memory_client: MemoryClient,
    agent_id: str
):
    """
    Daily learning loop: analyze past decisions, update confidence
    Called by agent_reflection_loop job
    """
    trait_mem = TraitMemory(memory_client)

    # Get agent's recent decisions
    decisions = await memory_client.get_agent_reasoning_history(
        agent_id,
        limit=50
    )

    # Analyze outcomes and update traits
    for decision in decisions:
        if not decision.get("outcome"):
            continue

        entity_id = decision.get("entity_id")
        category = decision.get("category")

        if entity_id and category:
            correct = decision["outcome"] == "success"
            await trait_mem.reinforce_trait(entity_id, category, correct)

    logger.info(f"Learning loop complete for agent {agent_id}")


__all__ = [
    "Trait",
    "TraitMemory",
    "run_trait_learning_loop",
]
