import re
import random


def score_idea(idea: str) -> float:
    """
    Scores an idea using a heuristic blend of:
    - Novelty: presence of innovative keywords
    - Clarity: shorter, readable phrasing
    - Feasibility: real-world plausibility cues

    Returns a float between 0 and 1.
    """
    if not idea or not isinstance(idea, str):
        return 0.0

    text = idea.lower()

    # -------------------
    # Novelty (0–0.4)
    # -------------------
    novelty_keywords = [
        "ai", "autonomous", "wearable", "biodegradable", "gesture",
        "collaborative", "adaptive", "space", "polymers",
        "underwater", "ar", "vr"
    ]
    novelty_hits = sum(1 for w in novelty_keywords if w in text)
    novelty = min(novelty_hits * 0.05, 0.4)

    # -------------------
    # Clarity (0–0.3)
    # Penalize if sentence is too long or repetitive
    # -------------------
    words = re.findall(r"\w+", idea)
    length_penalty = max(0, (len(words) - 25) * 0.01)  # slight penalty >25 words
    clarity = max(0.0, 0.3 - length_penalty)

    # -------------------
    # Feasibility (0–0.2)
    # Reward grounded/realistic terms
    # -------------------
    feasibility_keywords = [
        "students", "elderly", "urban", "remote", "workers",
        "recycled", "eco-friendly", "materials", "energy",
        "health", "education", "safety"
    ]
    feasibility_hits = sum(1 for w in feasibility_keywords if w in text)
    feasibility = min(feasibility_hits * 0.05, 0.2)

    # -------------------
    # Random factor (0–0.1)
    # Keeps diversity so not all similar ideas tie
    # -------------------
    randomness = random.uniform(0, 0.1)

    score = novelty + clarity + feasibility + randomness
    return round(min(score, 1.0), 3)
