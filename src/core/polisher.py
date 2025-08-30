# src/core/polisher.py

import re

class IdeaPolisher:
    """Refine and polish raw ideas into more concise, appealing text."""

    def __init__(self):
        # could later plug into LLM-based refinement
        pass

    def polish(self, idea: str) -> str:
        if not idea or not isinstance(idea, str):
            return "Invalid idea"

        refined = idea.strip()

        # Capitalize first letter
        refined = refined[0].upper() + refined[1:] if refined else refined

        # Remove excessive whitespace
        refined = re.sub(r"\s+", " ", refined)

        # Ensure ending punctuation
        if not refined.endswith(('.', '!', '?')):
            refined += "."

        # Make it slightly more engaging (hacky heuristic)
        if "idea" not in refined.lower():
            refined = f"✨ {refined}"

        return refined
