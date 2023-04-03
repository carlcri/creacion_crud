import csv, click


from tabulate import tabulate
from clients.models import Client

class ClientService:

    def __init__(self, table_name):
        self.table_name = table_name

    def get_clients_list(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema()) 
 
            return list(reader)
        

    def search_client_by_name(self, client_name):
        clients = self.get_clients_list()

        for idx, client in enumerate(clients):
            if client_name != client['name']:
                continue
            else:
                return clients[idx]
    


    @staticmethod    
    def render_list(clients_list):
        click.echo(tabulate(clients_list, headers='keys', tablefmt='fancy_grid'))



