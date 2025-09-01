# src/utils/exporter.py
import os
import json

class Exporter:
    @staticmethod
    def save(ideas, filename, format="json"):
        os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
        fmt = (format or "json").lower()
        if fmt == "json":
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(ideas, f, ensure_ascii=False, indent=2)
        elif fmt == "txt":
            with open(filename, "w", encoding="utf-8") as f:
                for i, idea in enumerate(ideas, 1):
                    f.write(f"{i}. {idea}\n")
        else:
            raise ValueError(f"Unsupported export format: {format}")
