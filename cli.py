import click
from rich.console import Console
from src.core.generator import IdeaGenerator
from src.core.evolution import EvolutionEngine
from src.core.polisher import IdeaPolisher

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
def generate(n):
    gen = IdeaGenerator()
    ideas = gen.generate(n)
    for i, idea in enumerate(ideas, 1):
        console.print(f"[bold cyan]Idea {i}:[/] {idea}")

# -------------------
# Evolve Command
# -------------------
@cli.command()
@click.option("--n", default=5, help="Number of ideas per generation")
@click.option("--generations", default=3, help="Number of evolutionary steps")
def evolve(n, generations):
    evo = EvolutionEngine()
    history = evo.evolve(n=n, generations=generations)

    for g, ideas in enumerate(history):
        console.print(f"\n[bold yellow]Generation {g}[/]")
        for i, idea in enumerate(ideas, 1):
            console.print(f"  [cyan]Idea {i}:[/] {idea}")

# -------------------
# Polish Command
# -------------------
@cli.command()
@click.argument("idea", nargs=-1)
def polish(idea):
    idea_text = " ".join(idea)
    polisher = IdeaPolisher()
    refined = polisher.polish(idea_text)
    console.print(f"[bold green]Polished Idea:[/] {refined}")

if __name__ == "__main__":
    cli()
