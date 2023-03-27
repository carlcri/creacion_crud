import click


@click.group
def clients():
    '''Manages the Client Life Cycle'''
    pass


@clients.command()
def search():
    '''Search a client by name'''
    click.echo(click.style('Hello World', fg='green'))


@clients.command()
@click.pass_context
def list(ctx):
    '''List all the clients'''
    client_service = ctx.obj['clients_table']
    click.echo(type(client_service))
    click.echo(click.style(client_service, fg='red'))

all = clients
