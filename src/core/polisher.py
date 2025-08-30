# polisher.py
import re

class Polisher:
    def __init__(self):
        pass

    def polish(self, idea: str) -> str:
        # Remove excessive spaces
        idea = re.sub(r'\s+', ' ', idea).strip()
        # Remove repetitive phrases (simple heuristic)
        phrases = idea.split(' ')
        seen = set()
        result = []
        for word in phrases:
            if word not in seen:
                result.append(word)
                seen.add(word)
        return ' '.join(result)
