import random

class IdeaGenerator:
    def __init__(self):
        self.base_ideas = [
            "An AI that generates bedtime stories",
            "Furniture that adapts its shape based on mood",
            "A wearable that translates emotions into colors",
            "A drone that plants micro-seeds in urban cracks",
            "A pen that converts handwriting directly to code"
        ]

    def generate(self, n=3):
        return random.sample(self.base_ideas, min(n, len(self.base_ideas)))
