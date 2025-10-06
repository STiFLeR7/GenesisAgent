"""
Symbolic cognition layer — rule-based recombination + context inference.
"""

import random

def recombine_ideas(idea_a: str, idea_b: str | None) -> str:
    if not idea_b:
        return idea_a
    a, b = idea_a.split(), idea_b.split()
    pivot = random.randint(1, min(len(a), len(b)) - 1)
    return " ".join(a[:pivot] + b[pivot:]).capitalize()

def infer_context(idea: str) -> dict:
    tokens = idea.lower().split()
    return {"keywords": [t for t in tokens if len(t) > 4], "length": len(tokens)}
