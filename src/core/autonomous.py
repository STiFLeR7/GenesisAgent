# src/core/autonomous.py
from src.core.generator import IdeaGenerator
from src.core.mutator import Mutator
from src.scorer import score_idea
from src.core.storage import save_best_ideas
from rich.console import Console

console = Console()


def evolve_ideas(n=5, generations=3, seed=None):
    """
    Autonomously evolve ideas through generation, mutation, scoring, and selection.
    - Uses a Mutator instance seeded for reproducibility.
    - Prints per-generation scores and saves final top-N idea strings.
    """
    generator = IdeaGenerator(seed=seed)
    mutator = Mutator(seed=seed)

    # initial population: simple base strings
    population = generator.generate(n)

    # we will maintain final_top as the last generation's selected list
    final_top = population.copy()

    for g in range(generations + 1):
        console.print(f"\n[bold yellow]Generation {g}[/]")
        # Score/display current population
        scored_display = []
        for idx, idea in enumerate(population, 1):
            score = round(float(score_idea(idea)), 3)
            console.print(f"  [cyan]Idea {idx}:[/] {idea} [score: {score}]")
            scored_display.append((idea, score))

        if g < generations:
            # Mutate each idea using the seeded Mutator (avoids duplicates)
            mutated = [mutator.mutate_str(idea) for idea in population]

            # Score mutated ideas and select top-n
            scored = [(idea, score_idea(idea)) for idea in mutated]
            scored.sort(key=lambda x: float(x[1]), reverse=True)
            population = [idea for idea, _ in scored[:n]]

            # keep track of the last generation selection
            final_top = population.copy()

    # Save final top ideas (strings) using existing storage (keeps backward compatibility)
    save_best_ideas(final_top)

    console.print("\n[bold green]Evolution Complete![/]")
    return final_top
