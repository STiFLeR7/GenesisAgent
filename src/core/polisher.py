# src/core/polisher.py
import re
import math

def _clean_spaces(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    # Normalize punctuation spacing
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    text = re.sub(r"([(\[])\s+", r"\1", text)
    text = re.sub(r"\s+([)\]])", r"\1", text)
    return text

def heuristic_scores(idea_obj):
    """
    Compute simple (Novelty, Clarity, Feasibility) scores 1..10
    based on twist variety and length.
    """
    twists = idea_obj.get("twists", [])
    cat_variety = len(set(c for c, _ in twists))
    total = len(twists)

    # Novelty favors variety and moderate length
    novelty = min(10, 3 + cat_variety + (1 if total >= 3 else 0))

    # Clarity decreases with very long chains
    clarity_penalty = max(0, total - 6)
    clarity = max(3, 10 - clarity_penalty)

    # Feasibility penalizes very long chains and exotic contexts
    exotic = sum(1 for (c, p) in twists if c in ("context", "environment") and ("space" in p or "underwater" in p))
    feas = max(3, 10 - math.floor(total/2) - exotic)

    return novelty, clarity, feas

class Polisher:
    """
    Light-weight refiner that adds a succinct hook, removes clutter,
    and appends heuristic scores.
    """
    def polish(self, idea_text: str) -> str:
        idea = _clean_spaces(idea_text)
        if not idea:
            return "Please provide a non-empty idea."

        # Hook: add a surprising word if not present
        hook_prefix = "✨"
        if not any(sym in idea for sym in ["✨", "🔥"]):
            hook_prefix = "✨"
        # Ensure sentence starts capitalized
        idea = idea[0].upper() + idea[1:] if idea else idea

        # Very light rewrite patterns
        idea = idea.replace(" ,", ",").replace(" .", ".")
        idea = re.sub(r"\s*—\s*", " — ", idea)

        # Dummy (N/C/F) when polishing free text without structure
        n, c, f = 7, 9, 8
        return f"{hook_prefix} {idea} [N:{n}/10 | C:{c}/10 | F:{f}/10]"
