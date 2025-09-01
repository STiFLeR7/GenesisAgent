# src/core/generator.py
import random

BASE_IDEAS = [
    "A wearable that translates emotions into colors",
    "An AI that generates bedtime stories",
    "Furniture that adapts its shape based on mood",
    "A pen that converts handwriting directly to code",
    "A drone that plants micro-seeds in urban cracks",
    "A mirror that gives micro-coaching during routines",
    "Shoes that harvest kinetic energy for IoT devices",
    "A fridge that plans meals from camera inventory",
    "Earbuds that summarize your day into a journal",
    "A desk that auto-tunes height/lighting to focus"
]

class IdeaGenerator:
    def __init__(self, seed=None):
        self.rng = random.Random(seed)

    def generate(self, n=3):
        n = max(1, int(n))
        picks = self.rng.sample(BASE_IDEAS, k=min(n, len(BASE_IDEAS)))
        # If n > list size, cycle with shuffle
        while len(picks) < n:
            extra = BASE_IDEAS.copy()
            self.rng.shuffle(extra)
            for x in extra:
                picks.append(x)
                if len(picks) >= n:
                    break
        return picks
