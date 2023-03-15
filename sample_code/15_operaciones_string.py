client_name = None

while not client_name:
    client_name = input('What is the client name?: ')

    if client_name == 'exit':
        client_name = None
        break

print(client_name)
