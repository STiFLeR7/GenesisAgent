# src/core/evolution.py
from .generator import IdeaGenerator
from .mutator import Mutator
from .polisher import IdeaPolisher
from rich.console import Console

console = Console()

class EvolutionEngine:
    def __init__(self):
        self.gen = IdeaGenerator()
        self.mutator = Mutator()
        self.polisher = IdeaPolisher()

    def evolve(self, n=5, generations=3):
        history = []

        # Step 0: generate initial ideas
        ideas = self.gen.generate(n)
        history.append(ideas)

        console.print(f"[bold yellow]Generation 0[/]")
        for i, idea in enumerate(ideas, 1):
            console.print(f"  [cyan]Idea {i}:[/] {idea}")

        # Step 1: evolve over generations
        for g in range(1, generations + 1):
            new_gen = []
            for idea in ideas:
                mutated = self.mutator.mutate(idea)
                polished = self.polisher.polish(mutated)
                new_gen.append(polished)

            ideas = new_gen
            history.append(ideas)

            console.print(f"\n[bold yellow]Generation {g}[/]")
            for i, idea in enumerate(ideas, 1):
                console.print(f"  [cyan]Idea {i}:[/] {idea}")

        return history
