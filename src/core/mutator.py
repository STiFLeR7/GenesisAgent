import random

class Mutator:
    def __init__(self):
        self.twist_pool = [
            "for children", "for space missions", "using biodegradable materials",
            "using self-healing polymers", "with gamification elements",
            "with gesture control", "in extreme weather zones",
            "that adapts in real-time", "with collaborative features",
        ]
        self.max_total_twists = 3  # max twists added per idea

    def mutate(self, idea):
        """
        Adds a limited number of twists to an idea while avoiding excessive repetition.
        """
        twists = random.sample(self.twist_pool, k=self.max_total_twists)
        mutated = idea
        for twist in twists:
            if twist not in mutated:
                mutated += f" {twist}"
        return mutated
