import click, csv, os

from clients.services import ClientService


@click.group
def clients():
    '''Manages the Client Life Cycle'''
    pass


@clients.command()
@click.pass_context
@click.argument('username')
@click.option('--byname', '-n', is_flag=True, default=False)
def search(ctx, username, byname):
    username = username.capitalize()

    '''Search a client by name or ID'''
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


all = clients
