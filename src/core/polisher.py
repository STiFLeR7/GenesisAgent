class IdeaPolisher:
    def polish(self, idea):
        # Simple polish logic: capitalize first letter and add punctuation
        idea = idea.strip()
        if not idea.endswith("."):
            idea += "."
        return idea[0].upper() + idea[1:]
