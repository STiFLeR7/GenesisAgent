import random
from rich.console import Console
from src.core.generator import IdeaGenerator
from src.core.polisher import IdeaPolisher
from src.core.mutator import IdeaMutator

console = Console()

class EvolutionEngine:
    def __init__(self):
        self.generator = IdeaGenerator()
        self.polisher = IdeaPolisher()
        self.mutator = IdeaMutator()

    def evolve(self, n=5, generations=3):
        """Run full evolutionary pipeline of ideas."""
        # Step 1: Generate initial population
        population = self.generator.generate(n)
        population = [self.polisher.polish(idea) for idea in population]

        history = [population.copy()]  # ✅ Keep history for return

        for gen in range(1, generations + 1):
            next_population = []
            for idea in population:
                mutated = self.mutator.mutate(idea, n=1)
                polished = self.polisher.polish(mutated)
                next_population.append(polished)
            population = next_population
            history.append(population.copy())  # ✅ Save generation in history

        return history  # ✅ Return full evolution history
