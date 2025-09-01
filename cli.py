# cli.py
import click
from rich.console import Console
from src.core.generator import IdeaGenerator
from src.core.evolution import EvolutionEngine
from src.core.polisher import Polisher

console = Console()

@click.group()
def cli():
    """GenesisAgent CLI"""
    pass

# -------------------
# Generate Command
# -------------------
@cli.command()
@click.option("--n", default=3, help="Number of ideas to generate")
@click.option("--seed", default=None, type=int, help="Random seed for reproducibility")
def generate(n, seed):
    """Generate creative ideas"""
    gen = IdeaGenerator(seed=seed)
    ideas = gen.generate(n)
    for i, idea in enumerate(ideas, 1):
        console.print(f"[bold cyan]Idea {i}:[/] {idea}")

# -------------------
# Evolve Command
# -------------------
@cli.command()
@click.option("--n", default=5, help="Number of ideas per generation")
@click.option("--generations", default=3, help="Number of evolutionary steps")
@click.option("--max-twists", default=6, help="Maximum total twists per idea")
@click.option("--recomb", default=0.2, type=float, help="Recombination chance per generation (0..1)")
@click.option("--seed", default=None, type=int, help="Random seed for reproducibility")
def evolve(n, generations, max_twists, recomb, seed):
    """Evolve creative ideas over multiple generations"""
    evo = EvolutionEngine(seed=seed)
    history = evo.evolve(
        n=n,
        generations=generations,
        max_twists=max_twists,
        recombination_chance=recomb
    )

    for g, ideas in enumerate(history):
        console.print(f"\n[bold yellow]Generation {g}[/]")
        for i, idea in enumerate(ideas, 1):
            console.print(f"  [cyan]Idea {i}:[/] {idea}")

    console.print("\n[bold green]Evolution Complete![/]")

# -------------------
# Polish Command
# -------------------
@cli.command()
@click.argument("idea", nargs=-1)
def polish(idea):
    """Polish/refine a given idea"""
    idea_text = " ".join(idea).strip()
    if not idea_text:
        console.print("[red]Please provide an idea to polish.[/]")
        return
    polisher = Polisher()
    refined = polisher.polish(idea_text)
    console.print(f"[bold green]Polished Idea:[/] {refined}")

if __name__ == "__main__":
    cli()
