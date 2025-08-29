import click
from rich.console import Console
from src.core.generator import IdeaGenerator
from src.core.evolution import EvolutionEngine

console = Console()

@click.group()
def cli():
    """GenesisAgent CLI"""
    pass

@cli.command()
@click.option("--n", default=3, help="Number of ideas to generate")
def generate(n):
    """Generate creative ideas"""
    gen = IdeaGenerator()
    ideas = gen.generate(n)
    for i, idea in enumerate(ideas, 1):
        console.print(f"[bold cyan]Idea {i}:[/] {idea}")

@cli.command()
@click.option("--n", default=5, help="Number of ideas per generation")
@click.option("--generations", default=3, help="Number of evolutionary steps")
def evolve(n, generations):
    """Evolve creative ideas over multiple generations"""
    evo = EvolutionEngine()
    history = evo.evolve(n=n, generations=generations)

    for g, ideas in enumerate(history):
        console.print(f"\n[bold yellow]Generation {g}[/]")
        for i, idea in enumerate(ideas, 1):
            console.print(f"  [cyan]Idea {i}:[/] {idea}")

if __name__ == "__main__":
    cli()
