import click
from clients import commands as client_commands

@click.group
def cli():
    pass

cli.add_command(client_commands.all)