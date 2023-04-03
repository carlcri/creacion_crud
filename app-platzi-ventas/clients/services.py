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
            
    
    def create_client(self, new_client):
        click.echo(type(new_client))
        new_client = new_client.to_dict()
        click.echo(type(new_client))
        click.echo(new_client)

        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(new_client)


    


    @staticmethod    
    def render_list(clients_list):
        click.echo(tabulate(clients_list, headers='keys', tablefmt='fancy_grid'))



