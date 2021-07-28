import os
clients = ['pablo', 'ricardo']

def clients_to_str(clients):

    separador = ', '
    clients_str= separador.join(clients)

    return clients_str


def create_client (client_name):
    global clients
    
    if client_name not in clients:
        clients. append(client_name)
    else:
        print('''Client already is in client's list''')


def get_client_name():
    client_name = None

    while not client_name:

        client_name = input('''
             What is the client name?: ''')

        if client_name =='exit':
            client_name = None
            break

    if not client_name:
        exit()

    return client_name


def delete_client(client_name):
    global clients

    if client_name not in clients:

        print('''Client was not found in the client's list''')
        input('...')
    else:

        clients.remove(client_name)


def update_client(client_name):
    global clients
    
    if client_name in clients:

        old_client_index = clients.index(client_name)
        update_client_name = input('What is the new client name?: ')

        clients[old_client_index] = update_client_name
        return update_client_name

    else:
        print("Client is not in client's list")
        input('...')


def search_client(client_name):
    
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def list_clients():

    clients_listados=''
    for idx, client in enumerate(clients):
        clients_listados += f'{idx}: {client} | ' 
        
    return clients_listados


def _print_welcome():
    global clients

    print(f'''
             ___________________________________________________
            | ************************************************* |
            | ||||||||||||| Welcome to Ventas CRUD |||||||||||| |
            | ************************************************* |
            |___________________________________________________| 
            | What would you like to do today                   |
            | [C]reate client                                   |
            | [U]pdate client                                   |
            | [D]elete client                                   |
            | [S]earch client                                   |
            | [Q]uit for Ventas CRUD                            |
            |---------------------------------------------------|
             
        This is de current list:
        {list_clients()}                     
            ''')
    

def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        sistema = os.system('clear')
    else:
    # for windows platfrom
        sistema = os.system('cls')

if __name__ =='__main__':

    paso = 'seguir'

    while paso == 'seguir':

        _print_welcome()
        command = input('''
             Please input option to do [C], [D], [U] or [Q]: 
             ''').upper()
        
        if command == 'Q':
            
            paso = 'parar'
        
        elif command == 'C':

            client_name = get_client_name()         
            create_client(client_name)
            
        elif command == 'D':

            client_name = get_client_name()
            delete_client(client_name)

        elif command == 'U':
            
            client_name = get_client_name()
            update_client(client_name)

        elif command == 'S':

            client_name = get_client_name()
            found = search_client(client_name)

            if found:
                print("The client is in client's list")
            else:
                print(f'''The client: {client_name}, is no in our client's List''')
                
            input('Back...')


        else: 
            print('Invalid Command')
            input('Back...')
        
        screen_clear()