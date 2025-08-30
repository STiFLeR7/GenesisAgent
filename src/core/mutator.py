# src/core/mutator.py
import random

class Mutator:
    def __init__(self):
        # Possible twists categorized by idea type
        self.general_twists = [
            "in extreme weather zones",
            "with collaborative features",
            "that adapts in real-time",
            "with gamification elements",
        ]
        self.material_twists = [
            "using biodegradable materials",
            "using self-healing polymers",
        ]
        self.gesture_twists = ["with gesture control"]
        self.age_twists = ["for children", "for elderly"]
        self.context_twists = ["for space missions", "for urban environments"]

    def mutate(self, idea: str, max_twists: int = 3) -> str:
        """Evolve the idea with coherent twists."""
        twists = []

        # Pick twists intelligently
        for _ in range(random.randint(1, max_twists)):
            category = random.choice([
                self.general_twists,
                self.material_twists,
                self.gesture_twists,
                self.age_twists,
                self.context_twists
            ])
            twist = random.choice(category)
            if twist not in twists:
                twists.append(twist)

        # Merge twists smoothly
        if twists:
            idea = idea.rstrip(".")
            # Use commas and 'and' for readability
            if len(twists) == 1:
                idea += f" {twists[0]}"
            else:
                idea += ", " + ", ".join(twists[:-1]) + " and " + twists[-1]

        return idea
