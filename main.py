import os
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


def list_clients():
    global clients
    cliente_str=', '
    cliente_str = cliente_str.join(clients)
    print(cliente_str)

def _put_comma():
    global clients
    clients+=','

def _print_welcome():
    global clients
    print('''
             *************************************************
             ||||||||||||| Welcome to Ventas CRUD ||||||||||||
             *************************************************
            ''')
    print('This is de current list:', clients )
    print('What would you like to do today')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[Q]uit for Ventas CRUD')
    

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
        command = input('Please input option to do [C], [D], [U] or [Q]: ').upper()
        
        if command == 'Q':
            
            paso = 'parar'
        
        elif command != 'Q':
            
            client_name = input('What is the client name?: ')

            if command == 'C':
                
                create_client(client_name)
                
            elif command == 'D':

                delete_client(client_name)

            elif command == 'U':
                
                update_client(client_name)

            else: 

                print('Invalid Command')
        
        screen_clear()