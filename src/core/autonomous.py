from .generator import generate_ideas
from .mutator import mutate_idea
from ..scorer import score_idea
from .storage import save_best_ideas


def evolve_ideas(n=5, generations=3):
    """
    Autonomously evolve ideas through generation, mutation, scoring, and selection.
    - n: number of ideas per generation
    - generations: number of generations to evolve
    """
    population = generate_ideas(n)

    for g in range(generations + 1):
        print(f"\nGeneration {g}")
        for idx, idea in enumerate(population, 1):
            idea_display = idea if idea else "(empty)"
            print(f"  Idea {idx}: {idea_display}")

        if g < generations:
            # Mutate and score new population
            mutated = [mutate_idea(idea) or idea for idea in population]
            scored = [(idea, score_idea(idea)) for idea in mutated if idea]
            scored.sort(key=lambda x: x[1], reverse=True)

            # Keep top n
            population = [idea for idea, _ in scored[:n]]

    save_best_ideas(population)
    print("\nEvolution Complete!")
    return population
