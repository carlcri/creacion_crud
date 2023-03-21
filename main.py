import sys


clients = 'pablo,ricardo,oscar'


def search_client(client_name):
    global clients
    client_list = clients.split(',')

    for client in client_list:
        if client_name != client:
            continue
        else:
            return True
    


def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already in client\'s list')


def list_clients():
    print(clients)


def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_name + ',')
    else:
        print('Client not in client\'s list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client not in client\'s list')


def _add_comma():
    global clients

    clients += ','

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?: ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?:')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


if __name__ == '__main__':
    _print_welcome()

    command = input().upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()

    elif command == 'U':
        client_name = _get_client_name()
        updated_name = input('What is name of the new client? ')
        update_client(client_name, updated_name)
        list_clients()

    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        
        if found:
            print('{} is the client\'s list'.format(client_name))
        else:
            print('{} is not in the client\'s list'.format(client_name))
            print(f' el valor de found: {found}')

    else:
        print('Invalid command')