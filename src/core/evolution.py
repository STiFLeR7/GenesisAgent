# src/core/evolution.py
from .mutator import Mutator

class EvolutionEngine:
    def __init__(self):
        self.mutator = Mutator()
        self.max_total_twists = 5  # cap total twists per idea

    def evolve(self, n=5, generations=3):
        # Initialize ideas with a twist count tracker
        ideas = [{"text": self.mutator.random_idea(), "twists": 0} for _ in range(n)]
        history = []

        for gen in range(generations):
            gen_ideas = []
            for idea in ideas:
                available_twists = self.max_total_twists - idea["twists"]
                if available_twists <= 0:
                    mutated_text = idea["text"]  # no more twists allowed
                else:
                    mutated_text, added_twists = self.mutator.mutate(
                        idea["text"], max_twists=available_twists
                    )
                    idea["twists"] += added_twists
                    idea["text"] = mutated_text

                gen_ideas.append(mutated_text)
            history.append(gen_ideas)
        return history
