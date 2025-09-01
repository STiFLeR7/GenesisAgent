# src/core/autonomous.py
from src.core.generator import IdeaGenerator
from src.core.mutator import mutate_idea
from src.scorer import score_idea
from src.core.storage import save_best_ideas


def evolve_ideas(n=5, generations=3, seed=None):
    """
    Autonomously evolve ideas through generation, mutation, scoring, and selection.
    """
    # Initialize IdeaGenerator
    generator = IdeaGenerator(seed=seed)
    population = generator.generate(n)

    for g in range(generations + 1):
        print(f"\nGeneration {g}")
        for idx, idea in enumerate(population, 1):
            print(f"  Idea {idx}: {idea}")

        if g < generations:
            # Apply mutation
            mutated = [mutate_idea(idea) for idea in population]
            # Score each mutated idea
            scored = [(idea, score_idea(idea)) for idea in mutated]
            # Sort by score descending
            scored.sort(key=lambda x: x[1], reverse=True)
            # Select top N
            population = [idea for idea, _ in scored[:n]]

    # Save the final top ideas
    save_best_ideas(population)
    print("\nEvolution Complete!")
    return population
