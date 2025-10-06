"""
Heuristic Scorer — assigns a pseudo-fitness score to evolved ideas.
"""

import random

def score_idea(idea: str) -> float:
    """Assign a synthetic score based on perceived novelty and length."""
    novelty = len(set(idea.split())) / max(1, len(idea.split()))
    randomness = random.uniform(0.2, 0.8)
    return round((novelty + randomness) / 2, 3)
