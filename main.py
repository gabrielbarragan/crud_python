clients = ['pablo', 'ricardo']

def create_client (client_name):
    global clients
    
    if client_name not in clients:
        clients. append(client_name)
    else:
        print('''Client already is in client's list''')

def delete_client(client_name):
    global clients

    if client_name not in clients:
        print('''Client was not found in the client's list''')
    else:
        clients.remove(client_name)

def list_clients():
    global clients
    cliente_str=', '
    cliente_str = cliente_str.join(clients)
    print(cliente_str)

def _put_comma():
    global clients
    clients+=','

def _print_welcome():
    print('''
             *************************************************
             ||||||||||||| Welcome to Ventas CRUD ||||||||||||
             *************************************************''')
    print('What would you like to do today')
    print('[C]reate client')
    print('[D]elete client')
    print('[Q]uit for Ventas CRUD')


if __name__ =='__main__':

    paso = 'seguir'

    while paso == 'seguir':

        _print_welcome()
        command = input('Please input option to do [C], [D] or [Q]: ').upper()
        if command == 'Q':
            paso = 'parar'

        elif command == 'C':
            client_name = input('What is the client name?: ')
            create_client(client_name)
            list_clients()

        elif command == 'D':
            client_name = input ('What is the client to delete?: ')
            delete_client(client_name)
            list_clients()
        else: 
            print('Invalid Command')