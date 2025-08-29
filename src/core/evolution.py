import random
from src.core.generator import IdeaGenerator

class EvolutionEngine:
    """
    Handles mutation + selection of ideas
    """

    twists = [
        "for space missions",
        "with eco-friendly materials",
        "that adapts in real-time",
        "for children in remote areas",
        "with gamification elements"
    ]

    def __init__(self):
        self.generator = IdeaGenerator()

    def mutate(self, idea: str) -> str:
        """Add a random twist, avoiding duplicates"""
        twist = random.choice(self.twists)
        if twist in idea:
            # If already applied, pick another one
            available = [t for t in self.twists if t not in idea]
            if available:
                twist = random.choice(available)
            else:
                return idea  # no new twist possible
        return f"{idea} {twist}"


    def select(self, ideas, top_k=3):
        """
        Basic selection: pick top_k diverse ideas
        (for now, just random sample)
        """
        return random.sample(ideas, min(top_k, len(ideas)))

    def evolve(self, n=5, generations=3):
        """
        Full evolutionary loop
        """
        pool = self.generator.generate(n)
        history = [pool]

        for _ in range(generations):
            mutated = [self.mutate(idea) for idea in pool]
            pool = self.select(mutated, top_k=n)
            history.append(pool)

        return history
