import click, csv, os

from clients.services import ClientService
from clients.models import Client


@click.group
def clients():
    '''Manages the Client Life Cycle'''
    pass


@clients.command()
@click.pass_context
@click.argument('username')
@click.option('--byname', '-n', is_flag=True, default=False)
def search(ctx, username, byname):
    '''Search a client by name or ID'''

    username = username.capitalize()
    client_table = ctx.obj['clients_table']
    client_service = ClientService(client_table)

    if not byname:
        found = client_service.search_client_by_name(username)

        if found is None:
            os.system('echo NO MATCH! | lolcat')
        else:
            click.echo(click.style(f'{username} is in the client\'s DB', bold=True))
            ClientService.render_list([found])
    else:
        click.echo('not implemented')




@clients.command()
@click.pass_context
def list(ctx):
    '''List all the clients'''

    client_table = ctx.obj['clients_table']
    client_service = ClientService(client_table)
    clients_list = client_service.get_clients_list()
    ClientService.render_list(clients_list)



@clients.command()
@click.pass_context
@click.argument('new_client', nargs=4, type=str)
def create(ctx, new_client):
    ''' Create a new client: name company position salary'''

    name, company, position, salary = new_client
    salary = int(salary)

    client_table = ctx.obj['clients_table']
    client_service = ClientService(client_table)

    found = client_service.search_client_by_name(name.capitalize())

    if not found:
        new_client = Client(name, company, position, salary)
        client_service.create_client(new_client)
    else:
        click.echo(click.style(f'client {name} already exists', fg='green'))



all = clients

