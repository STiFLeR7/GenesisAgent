"""
Idea Generator — creates initial concept seeds for agents to evolve.
"""

import random

_seed_ideas = [
    "a self-learning urban traffic optimizer",
    "a bio-inspired cooling system for edge devices",
    "an adaptive chatbot that rewrites its own prompts",
    "a solar-powered sensor mesh for smart agriculture",
    "a modular drone swarm for environmental mapping",
    "a personal AI curator for research summaries",
]

def generate_idea(theme: str | None = None) -> str:
    """Return a base idea; theme acts as optional bias."""
    base = random.choice(_seed_ideas)
    if theme:
        return f"{base} focused on {theme}"
    return base
