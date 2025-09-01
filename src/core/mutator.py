# src/core/mutator.py
import random

# Twists grouped by category to improve coherence and deduping
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
    def __init__(self, seed=None):
        self.rng = random.Random(seed)

    def _unique_choice(self, category, used_phrases):
        """Pick a phrase from a category that's not been used yet."""
        options = [p for p in TWISTS[category] if p not in used_phrases]
        if not options:
            return None
        return self.rng.choice(options)

    def mutate(self, idea_obj, add_min=1, add_max=2):
        """
        Mutate an idea object by adding 1-2 new unique twists.
        idea_obj = {"base": str, "twists": [(category, phrase), ...]}
        """
        twists = list(idea_obj["twists"])
        used_phrases = {p for (_, p) in twists}

        # Choose categories to attempt adding
        k = self.rng.randint(add_min, add_max)
        cat_order = ALL_CATEGORIES[:]
        self.rng.shuffle(cat_order)

        added = 0
        for cat in cat_order:
            if added >= k:
                break
            phrase = self._unique_choice(cat, used_phrases)
            if phrase:
                twists.append((cat, phrase))
                used_phrases.add(phrase)
                added += 1

        idea_obj["twists"] = twists
        return idea_obj

    def prune(self, idea_obj, max_twists=6):
        """
        Prune repeated categories and cap total twists.
        Keeps the first occurrence of a category; removes redundant or duplicate phrases.
        """
        seen_categories = set()
        cleaned = []
        for cat, phrase in idea_obj["twists"]:
            if phrase.strip() == "":
                continue
            # Allow multiple categories but avoid exact duplicate phrases
            if (cat in seen_categories) and cat != "motivation" and cat != "collab":
                # Typically keep only first per structural category; allow multiple motivation/collab
                continue
            # Avoid exact duplicates
            if (cat, phrase) in cleaned:
                continue
            cleaned.append((cat, phrase))
            seen_categories.add(cat)

        # Cap
        if len(cleaned) > max_twists:
            cleaned = cleaned[:max_twists]

        idea_obj["twists"] = cleaned
        return idea_obj

    def format(self, idea_obj, score_tuple=None):
        """
        Convert idea object to a readable string with optional (N/C/F) scores.
        """
        base = idea_obj["base"]
        phrases = [p for (_, p) in idea_obj["twists"]]
        suffix = ""
        if phrases:
            suffix = " — " + "; ".join(phrases)
        if score_tuple:
            n, c, f = score_tuple
            return f"{base}{suffix} [N:{n}/10 | C:{c}/10 | F:{f}/10]"
        return f"{base}{suffix}"
