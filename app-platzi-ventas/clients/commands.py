import click, csv, os

from clients.services import ClientService


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
    client_table = ctx.obj['clients_table']
    client_service = ClientService(client_table)
    clients_list = client_service.get_clients_list()
    ClientService.render_list(clients_list)


all = clients
