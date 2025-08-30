# src/core/polisher.py

import re
import random

class IdeaPolisher:
    """Refine raw ideas with novelty, clarity, and feasibility heuristics."""

    def __init__(self):
        self.prompts = [
            "Imagine pitching this to investors: ",
            "Think of this as a startup tagline: ",
            "Make it sound futuristic yet practical: ",
        ]

    def score(self, idea: str):
        """Return novelty, clarity, and feasibility scores (0-10)."""
        novelty = min(10, max(1, len(set(idea.split())) // 2))
        clarity = 10 - (idea.count(",") + idea.count(";"))  # penalize clutter
        feasibility = 10 - (len(idea.split()) // 12)        # very long → less feasible

        return {
            "novelty": max(1, novelty),
            "clarity": max(1, clarity),
            "feasibility": max(1, feasibility)
        }

    def polish(self, idea: str) -> str:
        if not idea or not isinstance(idea, str):
            return "Invalid idea"

        raw = idea.strip()
        scores = self.score(raw)

        # Remove redundant whitespace
        refined = re.sub(r"\s+", " ", raw)

        # Add engagement flair if too bland
        if scores["novelty"] < 5:
            refined = f"Unexpected twist: {refined}"

        # Ensure punchy ending
        if not refined.endswith(('.', '!', '?')):
            refined += "."

        # Inject a creative framing occasionally
        if scores["clarity"] < 6 or scores["feasibility"] < 6:
            refined = random.choice(self.prompts) + refined

        return f"✨ {refined} [N:{scores['novelty']}/10 | C:{scores['clarity']}/10 | F:{scores['feasibility']}/10]"
