import click
from .process import process


@click.command()
@click.argument("text")
def main(text):
    """Process an input string."""
    click.echo(process(text))
