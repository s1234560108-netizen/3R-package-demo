"""Command-line interface for the three_r_package package."""

import click

from three_r_package.demo_module import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def three_r_package_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))
