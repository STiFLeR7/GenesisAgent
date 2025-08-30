# src/core/mutator.py
import random

TWISTS = [
    "for children",
    "for space missions",
    "in extreme weather zones",
    "with gamification elements",
    "with gesture control",
    "with collaborative features",
    "using self-healing polymers",
    "using biodegradable materials",
]

class Mutator:
    def random_idea(self):
        # Return a base idea randomly
        base_ideas = [
            "A drone that plants micro-seeds in urban cracks",
            "Furniture that adapts its shape based on mood",
            "An AI that generates bedtime stories",
            "A pen that converts handwriting directly to code",
            "A wearable that translates emotions into colors",
        ]
        return random.choice(base_ideas)

    def mutate(self, idea_text, max_twists=3):
        twists_applied = 0
        twists_to_apply = min(max_twists, len(TWISTS))
        twists = random.sample(TWISTS, twists_to_apply)
        for twist in twists:
            if twist not in idea_text:
                idea_text += f" {twist}"
                twists_applied += 1
        return idea_text, twists_applied
