import click
from rich.console import Console
from src.core.generator import IdeaGenerator
from src.core.evolution import EvolutionEngine
from src.core.polisher import IdeaPolisher
from src.utils.exporter import Exporter

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
    """Generate creative ideas"""
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
    """Evolve creative ideas over multiple generations"""
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
    """Polish/refine a given idea"""
    idea_text = " ".join(idea)
    polisher = IdeaPolisher()
    refined = polisher.polish(idea_text)
    console.print(f"[bold green]Polished Idea:[/] {refined}")


# -------------------
# Export Command
# -------------------
@cli.command()
@click.option("--filename", default="ideas.json", help="File to save ideas")
@click.option("--format", type=click.Choice(["json", "txt"]), default="json", help="Export format")
@click.option("--n", default=5, help="Number of ideas to generate before export")
def export(filename, format, n):
    """Generate ideas and export them to a file"""
    gen = IdeaGenerator()
    ideas = gen.generate(n)
    Exporter.save(ideas, filename, format=format)
    console.print(f"[bold magenta]Exported {len(ideas)} ideas to {filename} ({format})[/]")


if __name__ == "__main__":
    cli()
