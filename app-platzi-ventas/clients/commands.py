import click, csv, os
from tabulate import tabulate

CLIENT_SCHEMA = ['name', 'company', 'position']
CLIENTS = []

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
    click.echo(type(client_table))
    click.echo(click.style(client_table, fg='green'))

    _load_data_from_csv(client_table)
    click.echo(tabulate(CLIENTS, headers='keys', tablefmt='fancy_grid'))



def _load_data_from_csv(client_table):
    global CLIENTS
    with open(client_table, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)            
        for idx, row in enumerate(reader):
            CLIENTS.append(row)



all = clients
