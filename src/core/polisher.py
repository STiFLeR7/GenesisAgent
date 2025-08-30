import random

class IdeaPolisher:
    def __init__(self):
        self.enhancements = [
            "for children",
            "for space missions",
            "with gamification elements",
            "that adapts in real-time",
            "with collaborative features",
            "using self-healing polymers",
            "using biodegradable materials",
            "in extreme weather zones",
            "with gesture control"
        ]

    def polish(self, idea):
        # safeguard: add 1-2 enhancements maximum
        num_additions = random.randint(1, 2)
        selected = random.sample(self.enhancements, num_additions)
        polished = idea + " " + " ".join(selected)
        return polished
