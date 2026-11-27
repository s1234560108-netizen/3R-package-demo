"""Command-line interface for the three_r_package package."""

import click

from three_r_package.demo_module import calculate_yield, hello_world


@click.command()
@click.option("--message", help="Type a message to say.")
@click.option("--passed", type=int, help="Number of products that passed.")
@click.option("--total", type=int, help="Total number of products inspected.")
@click.version_option()
def three_r_package_cli(message, passed, total):
    """Display a message or calculate the product yield rate."""
    if passed is not None or total is not None:
        if message is not None:
            raise click.UsageError("Use either --message or the yield options.")

        if passed is None or total is None:
            raise click.UsageError("Both --passed and --total are required.")

        try:
            result = calculate_yield(passed, total)
        except ValueError as exc:
            raise click.ClickException(str(exc)) from exc

        click.echo(f"Yield rate: {result:.2f}%")
    else:
        if message is None:
            message = click.prompt("message")

        click.echo(hello_world(message))
