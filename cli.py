import click
from rich.console import Console

console = Console()

@click.group()
def cli():
    pass

@cli.command()
def run():
    console.print('[bold green]🚀 GenesisAgent is running...[/]')

if __name__ == '__main__':
    cli()
