import sys, os


CLIENTS = [
    {
        'name': 'Pablo',
        'company': 'GOOGLE',
        'email': 'pablo@google.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'FACEBOOK',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    },
    {
        'name': 'Mark',
        'company': 'YAHOO',
        'email': 'marc001@yahoo.com',
        'position': 'Frontend Developer',
    }
]


def search_client(client_name):
    global CLIENTS

    for idx, client in enumerate(CLIENTS):
        if client_name != client['name']:
            continue
        else:
            return idx
    


def create_client(client):
    global CLIENTS
    CLIENTS.append(client)



def list_clients():
    for idx, client in enumerate(CLIENTS):
        print('{uid}: {name} | {company} | {position}'.format(
            uid=idx+1, 
            name = client['name'],
            company = client['company'],
            position = client['position'] 
            ))



def update_client(client_name):
    global CLIENTS

    found = search_client(client_name)

    if found is None:
        print('Client not in client\'s list')
    else:
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company').upper(),
            'position': _get_client_field('position'),
        }

        CLIENTS[found] = client




def delete_client(client_name):
    global CLIENTS

    index = search_client(client_name)

    if index is not None:
        CLIENTS.pop(index)

    else:
        print('Client not in client\'s list')



def _get_client_field(field):
    client_field = None

    while not client_field:
        client_field = input(f'{field} of the client?: ').capitalize()

        if client_field == 'exit':
            client_field = None
            break

    if not client_field:
        sys.exit()

    return client_field



def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?: ').capitalize()

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    os.system('date +"Today is: %A %d %B"')

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
        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found is None:
            client = {
                'name': client_name,
                'company': _get_client_field('company').upper(),
                'position': _get_client_field('position')
            }
            create_client(client)
            list_clients()
        else:
            os.system('echo client already exists | lolcat')

    elif command == 'U':
        client_name = _get_client_field('name')
        print(client_name)
        found = search_client(client_name)
        print(found)

        if found is not None:
            update_client(client_name)
            list_clients()
            
        else:
            os.system('echo client does not exist | lolcat')


    elif command == 'D':
        client_name = _get_client_field('name')
        delete_client(client_name)
        list_clients()


    elif command == 'S':
        client_name = _get_client_field("name")
        found = search_client(client_name)
        
        if found is None:
            os.system('echo NO MATCH! | lolcat')
            print(f' el valor de found: {found}')
        else:
            print('{} is the client\'s data base'.format(client_name))

    else:
        os.system("echo Invalid Command | lolcat")
        