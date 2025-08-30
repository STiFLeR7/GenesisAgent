from .mutator import Mutator

class EvolutionEngine:
    def __init__(self):
        self.mutator = Mutator()

    def evolve(self, n=5, generations=3):
        # Initialize first generation
        history = []
        ideas = [self.mutator.random_idea() for _ in range(n)]
        history.append(ideas)

        # Evolve subsequent generations
        for _ in range(1, generations + 1):
            next_gen = []
            for idea in history[-1]:
                mutated = self.mutator.mutate(idea, max_twists=3)
                next_gen.append(mutated)
            history.append(next_gen)

        return history
