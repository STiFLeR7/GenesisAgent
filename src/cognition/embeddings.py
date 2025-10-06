"""
Handles vector embeddings for idea similarity and novelty metrics.
Currently stubbed with simple Jaccard-based token similarity.
"""

def idea_similarity(a: str, b: str) -> float:
    set_a, set_b = set(a.split()), set(b.split())
    return len(set_a & set_b) / len(set_a | set_b) if set_a and set_b else 0.0
