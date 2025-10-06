"""
GenesisAgent v2.0.0 — CLI dashboard metrics.
"""

from src.analytics.metrics import compute_diversity, average_score

def print_dashboard(records: list[dict]):
    ideas = [r["idea"] for r in records]
    div = compute_diversity(ideas)
    avg = average_score(records)
    print("\n=== GenesisAgent Dashboard ===")
    print(f"Total ideas: {len(ideas)}")
    print(f"Average score: {avg:.3f}")
    print(f"Diversity index: {div:.3f}")
    print("==============================\n")
