import random


def score_idea(idea: str) -> float:
    """
    Scores an idea based on pseudo-random heuristics.
    Higher score = better idea.
    """
    if not idea or not isinstance(idea, str):
        return 0.0

    # Simple heuristic scoring
    base_score = random.uniform(0, 1)

    # Reward innovation buzzwords
    boosts = ["AI", "autonomous", "wearable", "biodegradable",
              "gesture", "collaborative", "adaptive", "space"]
    for word in boosts:
        if word.lower() in idea.lower():
            base_score += 0.2

    return round(min(base_score, 1.0), 3)
