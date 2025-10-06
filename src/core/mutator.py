"""
Idea Mutator — transforms ideas to simulate creative variation.
"""

import random

_mutations = [
    lambda idea: idea.replace("AI", "hybrid-AI"),
    lambda idea: idea + " using reinforcement learning.",
    lambda idea: idea + " optimized for low-power devices.",
    lambda idea: idea.replace("system", "ecosystem"),
    lambda idea: "Next-gen " + idea,
]

def mutate_idea(idea: str) -> str:
    """Randomly mutate an idea."""
    mutation = random.choice(_mutations)
    return mutation(idea)
