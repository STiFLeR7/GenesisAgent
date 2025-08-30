# src/core/generator.py
import random

class IdeaGenerator:
    BASE_IDEAS = [
        "An AI that generates bedtime stories",
        "A wearable that translates emotions into colors",
        "A pen that converts handwriting directly to code",
        "Furniture that adapts its shape based on mood",
        "A drone that plants micro-seeds in urban cracks",
    ]

    def generate(self, n=3):
        return random.sample(self.BASE_IDEAS, n)
