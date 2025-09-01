import os
import json

# File to store best evolved ideas
STORAGE_FILE = os.path.join(os.path.dirname(__file__), "best_ideas.json")


def save_best_ideas(ideas):
    """
    Save the best evolved ideas into a JSON file.
    """
    if not ideas or not isinstance(ideas, list):
        raise ValueError("Ideas must be a non-empty list of strings")

    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(ideas, f, indent=2, ensure_ascii=False)

    print(f"[Storage] ✅ Saved {len(ideas)} ideas to {STORAGE_FILE}")


def load_best_ideas():
    """
    Load the previously saved best ideas.
    Returns a list of ideas, or [] if no file exists.
    """
    if not os.path.exists(STORAGE_FILE):
        print("[Storage] ⚠️ No stored ideas found, returning empty list.")
        return []

    with open(STORAGE_FILE, "r", encoding="utf-8") as f:
        ideas = json.load(f)

    print(f"[Storage] 📂 Loaded {len(ideas)} ideas from {STORAGE_FILE}")
    return ideas
