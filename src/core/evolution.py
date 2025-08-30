from .mutator import Mutator
from .generator import IdeaGenerator

class EvolutionEngine:
    def __init__(self):
        self.mutator = Mutator()
        self.generator = IdeaGenerator()

    def evolve(self, n=5, generations=3):
        """
        Evolves ideas over multiple generations using stacking-safe mutations.
        """
        history = []
        # Generation 0: base ideas
        ideas = self.generator.generate(n)
        history.append(ideas)

        for g in range(1, generations + 1):
            new_generation = []
            for idea in ideas:
                mutated = self.mutator.mutate(idea)
                new_generation.append(mutated)
            history.append(new_generation)
            ideas = new_generation  # update for next generation

        return history
