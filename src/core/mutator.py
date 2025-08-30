# src/core/mutator.py
import random

class Mutator:
    PREFIXES = [
        "✨ Unexpected twist: ",
        "🔥 Game-changing idea: ",
        "💡 Innovative concept: "
    ]

    SUFFIXES = [
        "for space missions",
        "with eco-friendly materials",
        "that adapts in real-time",
        "using self-healing polymers",
        "for children",
        "for the elderly",
        "with gamification elements",
        "with collaborative features",
        "in underwater habitats",
        "in extreme weather zones"
    ]

    def mutate(self, idea: str) -> str:
        """Mutate an idea by adding prefix/suffix without duplication."""
        new_idea = idea

        # Add prefix if none exist already
        if not any(pref.strip() in new_idea for pref in self.PREFIXES):
            new_idea = random.choice(self.PREFIXES) + new_idea

        # Add a suffix that is not already in the idea
        available_suffixes = [s for s in self.SUFFIXES if s not in new_idea]
        if available_suffixes:
            new_idea += " " + random.choice(available_suffixes)

        return new_idea
