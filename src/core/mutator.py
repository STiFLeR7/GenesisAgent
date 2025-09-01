# src/core/mutator.py
import random

class Mutator:
    """
    Handles mutations for ideas.
    """

    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)

        self.mutations = [
            "with gamification elements",
            "for children",
            "using self-healing polymers",
            "in extreme weather zones",
            "with collaborative features",
            "adapts in real-time"
        ]

    def mutate(self, idea: str) -> str:
        if not idea:
            return idea
        mutation = random.choice(self.mutations)
        return f"{idea} — {mutation}"


# Optional helper function for backward compatibility
def mutate_idea(idea: str) -> str:
    mut = Mutator()
    return mut.mutate(idea)
