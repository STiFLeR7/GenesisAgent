# src/utils/exporter.py

import json

class Exporter:
    """Utility to export ideas to different formats."""

    @staticmethod
    def save(ideas, filename: str, format: str = "json"):
        if not ideas:
            raise ValueError("No ideas to export.")

        if format == "json":
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(ideas, f, indent=4, ensure_ascii=False)

        elif format == "txt":
            with open(filename, "w", encoding="utf-8") as f:
                for i, idea in enumerate(ideas, 1):
                    f.write(f"Idea {i}: {idea}\n")

        else:
            raise ValueError(f"Unsupported format: {format}")
