# src/core/evolution.py
from .generator import IdeaGenerator
from .mutator import Mutator

class EvolutionEngine:
    def __init__(self):
        self.generator = IdeaGenerator()
        self.mutator = Mutator()

    def evolve(self, n=5, generations=3, max_twists=3):
        """Evolve ideas over multiple generations."""
        # Generation 0: initial ideas
        ideas = self.generator.generate(n)
        history = [ideas.copy()]

        for gen in range(1, generations + 1):
            new_ideas = []
            for idea in ideas:
                mutated = self.mutator.mutate(idea, max_twists=max_twists)
                new_ideas.append(mutated)
            history.append(new_ideas)
            ideas = new_ideas

        return history
