import random

class Mutator:
    def __init__(self):
        self.twists = [
            "using self-healing polymers",
            "for children",
            "for space missions",
            "with gamification elements",
            "that adapts in real-time",
            "with collaborative features",
            "using biodegradable materials",
            "in extreme weather zones",
            "with gesture control"
        ]

    def mutate(self, idea):
        twist = random.choice(self.twists)
        return f"{idea} {twist}"

    def random_idea(self):
        base_ideas = [
            "An AI that generates bedtime stories",
            "Furniture that adapts its shape based on mood",
            "A wearable that translates emotions into colors",
            "A drone that plants micro-seeds in urban cracks",
            "A pen that converts handwriting directly to code"
        ]
        return random.choice(base_ideas)
