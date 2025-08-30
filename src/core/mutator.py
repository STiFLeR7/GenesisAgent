import random

class IdeaMutator:
    def __init__(self):
        # Mutation operators (expandable later)
        self.mutations = [
            self.add_context,
            self.add_material,
            self.add_interactivity,
            self.add_audience,
            self.add_time_dimension
        ]

    def mutate(self, idea: str, n: int = 1):
        """Apply n random mutations without duplicating phrases."""
        mutated = idea
        for _ in range(n):
            op = random.choice(self.mutations)
            mutated = op(mutated)
        return self._deduplicate(mutated)

    # ----------------
    # Mutation Ops
    # ----------------
    def add_context(self, idea: str):
        contexts = [
            "for space missions",
            "in underwater habitats",
            "in extreme weather zones",
            "for disaster relief",
            "in smart cities"
        ]
        return f"{idea} {random.choice(contexts)}"

    def add_material(self, idea: str):
        materials = [
            "with biodegradable materials",
            "with recycled plastics",
            "using self-healing polymers",
            "with nanomaterials",
            "using 3D-printed components"
        ]
        return f"{idea} {random.choice(materials)}"

    def add_interactivity(self, idea: str):
        features = [
            "with gamification elements",
            "with voice interaction",
            "that adapts in real-time",
            "with gesture control",
            "with collaborative features"
        ]
        return f"{idea} {random.choice(features)}"

    def add_audience(self, idea: str):
        audiences = [
            "for children",
            "for the elderly",
            "for astronauts",
            "for urban farmers",
            "for remote learners"
        ]
        return f"{idea} {random.choice(audiences)}"

    def add_time_dimension(self, idea: str):
        times = [
            "that evolves over time",
            "that changes daily",
            "that adapts seasonally",
            "that learns from past usage",
            "that upgrades itself monthly"
        ]
        return f"{idea} {random.choice(times)}"

    # ----------------
    # Helper
    # ----------------
    def _deduplicate(self, text: str):
        """Remove accidental repeated phrases like 'for space missions for space missions'."""
        parts = text.split()
        dedup = []
        for i, word in enumerate(parts):
            if i > 0 and word == parts[i - 1]:
                continue
            dedup.append(word)
        return " ".join(dedup)
