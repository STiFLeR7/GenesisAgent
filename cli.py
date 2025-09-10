# cli.py
import json
import re
from pathlib import Path

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


# -------------------
# Autonomous Command
# -------------------
@cli.command()
@click.option("--n", default=5, help="Number of ideas per generation")
@click.option("--generations", default=3, help="Number of generations")
@click.option("--seed", default=None, type=int, help="Random seed for reproducibility")
def auto(n, generations, seed):
    """Run autonomous idea evolution"""
    from src.core.autonomous import evolve_ideas

    # evolve_ideas will print progress and save best ideas
    evolve_ideas(n=n, generations=generations, seed=seed)


# -------------------
# Clean-best Command
# -------------------
@cli.command("clean-best")
@click.option("--file", default="src/core/best_ideas.json", help="Path to best_ideas.json")
def clean_best(file):
    """Clean and dedupe the saved best_ideas.json (in-place)."""
    path = Path(file)
    if not path.exists():
        console.print(f"[red]File not found:[/] {path}")
        return

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        console.print(f"[red]Failed to read JSON:[/] {e}")
        return

    if not isinstance(data, list):
        console.print("[red]Unexpected format: expected a JSON list.[/]")
        return

    def clean_phrase(text: str) -> str:
        s = (text or "").strip()
        s = re.sub(r"\s+", " ", s)
        parts = [p.strip() for p in s.split("—") if p.strip()]
        if not parts:
            return s

        base = parts[0]
        seen = set()
        suffixes = []
        for p in parts[1:]:
            key = re.sub(r"[^\w\s]", "", p).strip().lower()
            if not key or key in seen:
                continue
            seen.add(key)
            # normalize separators inside suffixes to semicolon
            suffixes.append(p.rstrip(" ."))
        if suffixes:
            cleaned = f"{base} — " + "; ".join(suffixes)
        else:
            cleaned = base
        cleaned = cleaned.strip()
        if not cleaned.endswith("."):
            cleaned += "."
        # Capitalize first char
        cleaned = cleaned[0].upper() + cleaned[1:] if cleaned else cleaned
        return cleaned

    cleaned = [clean_phrase(x) for x in data]
    path.write_text(json.dumps(cleaned, indent=2, ensure_ascii=False), encoding="utf-8")
    console.print(f"[green]Cleaned and wrote {len(cleaned)} ideas to {path}[/]")


if __name__ == "__main__":
    cli()
