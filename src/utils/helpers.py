"""
Utility helpers shared across GenesisAgent modules.
"""

import random

def pick_random(items):
    return random.choice(items) if items else None
