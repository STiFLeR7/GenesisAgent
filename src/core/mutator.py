# src/core/mutator.py
"""
Mutator: history-aware, de-duplicating mutation logic.

This file exposes:
- class Mutator(seed=None)
- convenience function mutate_idea_str(idea_str, seed=None)
"""

import random
from typing import Dict, List, Tuple, Optional

TWISTS = {
    "audience": [
        "for children", "for elderly", "for students", "for athletes",
        "for remote workers", "for visually impaired users"
    ],
    "context": [
        "for space missions", "for disaster relief", "for urban environments",
        "for underwater habitats", "for rural clinics"
    ],
    "materials": [
        "using biodegradable materials", "using self-healing polymers",
        "with recycled plastics", "with eco-friendly materials", "with nanomaterials"
    ],
    "dynamics": [
        "that adapts in real-time", "that upgrades itself monthly",
        "that learns from user feedback", "that personalizes via biometrics"
    ],
    "interaction": [
        "with gesture control", "with voice interaction",
        "with AR overlays", "with haptic feedback"
    ],
    "collab": [
        "with collaborative features", "with social challenge modes",
        "with peer-to-peer sharing"
    ],
    "motivation": [
        "with gamification elements", "with streak rewards",
        "with micro-goals", "with skill trees"
    ],
    "environment": [
        "in extreme weather zones", "in low-bandwidth settings",
        "off-grid", "in noisy environments"
    ],
}

ALL_CATEGORIES = list(TWISTS.keys())


class Mutator:
    def __init__(self, seed: Optional[int] = None):
        self.rng = random.Random(seed)

    def _unique_choice(self, category: str, used_phrases: set) -> Optional[str]:
        choices = [p for p in TWISTS.get(category, []) if p not in used_phrases]
        if not choices:
            return None
        return self.rng.choice(choices)

    def mutate_obj(self, idea_obj: Dict, add_min: int = 1, add_max: int = 2) -> Dict:
        """
        Mutate an idea object while avoiding duplicates.
        idea_obj = {"base": str, "twists": [(category, phrase), ...]}
        """
        if "twists" not in idea_obj or idea_obj["twists"] is None:
            idea_obj["twists"] = []

        used_phrases = {p for (_, p) in idea_obj["twists"]}
        k = self.rng.randint(add_min, add_max)
        cat_order = ALL_CATEGORIES.copy()
        self.rng.shuffle(cat_order)

        added = 0
        for cat in cat_order:
            if added >= k:
                break
            phrase = self._unique_choice(cat, used_phrases)
            if phrase:
                idea_obj["twists"].append((cat, phrase))
                used_phrases.add(phrase)
                added += 1

        return idea_obj

    def prune(self, idea_obj: Dict, max_twists: int = 6) -> Dict:
        """
        Keep first reasonable occurrence per structural category (except allow multiple motivations/collab).
        Cap total twists to max_twists.
        """
        seen_categories = set()
        cleaned: List[Tuple[str, str]] = []
        for cat, phrase in idea_obj.get("twists", []):
            if (cat in seen_categories) and cat not in ("motivation", "collab"):
                continue
            if (cat, phrase) in cleaned:
                continue
            cleaned.append((cat, phrase))
            seen_categories.add(cat)
            if len(cleaned) >= max_twists:
                break

        idea_obj["twists"] = cleaned
        return idea_obj

    def format(self, idea_obj: Dict) -> str:
        """
        Convert idea_obj to a human readable string. E.g.:
        "Base idea — phrase1; phrase2 and phrase3"
        """
        base = idea_obj.get("base", "").strip()
        phrases = [p for (_, p) in idea_obj.get("twists", [])]
        if not phrases:
            return base
        # join with commas and final 'and' for readability
        if len(phrases) == 1:
            suffix = phrases[0]
        elif len(phrases) == 2:
            suffix = f"{phrases[0]} and {phrases[1]}"
        else:
            suffix = ", ".join(phrases[:-1]) + f", and {phrases[-1]}"
        return f"{base} — {suffix}"

    # Convenience: for older code paths that expect a string-mutator function
    def mutate_str(self, idea_str: str, add_min: int = 1, add_max: int = 2) -> str:
        """
        Mutate a plain string idea by appending 1..k phrases safely (no duplicates).
        This function checks if a twist already exists in the string before appending.
        """
        if not idea_str or not idea_str.strip():
            return idea_str

        # gather existing lower-cased phrases present
        lower = idea_str.lower()
        used = set()
        for cat in ALL_CATEGORIES:
            for p in TWISTS[cat]:
                if p.lower() in lower:
                    used.add(p)

        k = self.rng.randint(add_min, add_max)
        added = 0
        picks = []
        cat_order = ALL_CATEGORIES.copy()
        self.rng.shuffle(cat_order)
        for cat in cat_order:
            if added >= k:
                break
            candidates = [p for p in TWISTS[cat] if p not in used]
            if not candidates:
                continue
            pick = self.rng.choice(candidates)
            picks.append(pick)
            used.add(pick)
            added += 1

        # if nothing to add, return original
        if not picks:
            return idea_str

        # format picks into readable suffix
        if len(picks) == 1:
            suffix = picks[0]
        elif len(picks) == 2:
            suffix = f"{picks[0]} and {picks[1]}"
        else:
            suffix = ", ".join(picks[:-1]) + f", and {picks[-1]}"

        # append with a dash separator
        return idea_str.rstrip(" .") + " — " + suffix

# Backwards-compatible top-level helpers
_default_mutator = Mutator()

def mutate_idea(idea_str: str) -> str:
    return _default_mutator.mutate_str(idea_str)

def mutate_obj(idea_obj: Dict) -> Dict:
    return _default_mutator.mutate_obj(idea_obj)
