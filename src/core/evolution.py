from .mutator import Mutator

class EvolutionEngine:
    def __init__(self):
        self.mutator = Mutator()

    def evolve(self, n=5, generations=3):
        history = []

        # Initialize generation 0
        ideas = [self.mutator.random_idea() for _ in range(n)]
        history.append(ideas)

        for g in range(1, generations + 1):
            next_gen = []
            for idea in history[-1]:
                mutated = idea
                # stacking safeguard: mutate max 3 times per idea
                for _ in range(3):
                    mutated = self.mutator.mutate(mutated)
                next_gen.append(mutated)
            history.append(next_gen)

        return history
