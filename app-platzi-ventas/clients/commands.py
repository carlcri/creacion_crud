import click


@click.group
def clients():
    '''Manages the Client Life Cycle'''
    pass


@clients.command()
def search():
    '''Search a client by name'''
    click.echo(click.style('Hello World', fg='green'))

all = clients
