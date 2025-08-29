import random

class IdeaGenerator:
    """
    Minimal creativity engine (Chunk 2).
    For now: random templates → later: evolve & mutate ideas.
    """

    seed_ideas = [
        "A wearable that translates emotions into colors",
        "A drone that plants micro-seeds in urban cracks",
        "An AI that generates bedtime stories based on your day",
        "Furniture that adapts its shape based on mood",
        "A pen that converts handwriting directly to code"
    ]

    def generate(self, n=3):
        """Return n random ideas"""
        return random.sample(self.seed_ideas, min(n, len(self.seed_ideas)))
