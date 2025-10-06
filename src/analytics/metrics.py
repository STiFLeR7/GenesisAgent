"""
Compute evolution metrics — novelty, diversity, and average fitness.
"""

from src.cognition.embeddings import idea_similarity

def compute_diversity(ideas: list[str]) -> float:
    if len(ideas) < 2:
        return 0.0
    sims = [idea_similarity(a, b) for i, a in enumerate(ideas) for b in ideas[i+1:]]
    return 1 - (sum(sims) / len(sims))

def average_score(records: list[dict]) -> float:
    scores = [r["score"] for r in records if "score" in r]
    return sum(scores) / len(scores) if scores else 0.0
