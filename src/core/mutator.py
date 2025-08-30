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

    def mutate(self, idea, max_twists=3):
        """
        Apply random twists to an idea without repeating twists already applied.
        """
        # Check which twists are not already in the idea
        available_twists = [t for t in self.twists if t not in idea]

        if not available_twists:
            return idea  # Nothing left to add

        num_additions = min(max_twists, len(available_twists))
        selected = random.sample(available_twists, num_additions)

        for twist in selected:
            idea += f" {twist}"

        return idea

    def random_idea(self):
        base_ideas = [
            "An AI that generates bedtime stories",
            "Furniture that adapts its shape based on mood",
            "A wearable that translates emotions into colors",
            "A drone that plants micro-seeds in urban cracks",
            "A pen that converts handwriting directly to code"
        ]
        return random.choice(base_ideas)
