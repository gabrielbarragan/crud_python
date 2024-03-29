import os
import csv

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name','company','email','position']
clients = []


def _initialize_clients_from_storage():

    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f,fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table=f'{CLIENT_TABLE}.tmp'

    with open(tmp_table, mode = 'w') as f:
        writer = csv.DictWriter(f,fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table, CLIENT_TABLE)


def create_client (client):
    global clients
    
    if client not in clients:
        clients.append(client)
    else:
        print('''Client already is in client's list''')


def get_client_by_name():
    name = None

    while not name:

        name = input('''
             What is the client name?: ''')

        if name =='exit':
            name = None
            break

    if not name:
        exit()

    return name

def get_client_field(field_name):
    field = None

    while not field:

        field = input(f'''
             What is the client {field_name}?: ''')

        if field =='exit':
            field = None
            break

    if not field:
        exit()

    return field


def get_client_by_id():
    client_id = None
    while not client_id:

        client_id = input(f'''
             What is the client id ?: ''')
        
        if client_id =='exit':
            client_id = None
            break
        try:
            return int(client_id)
        
        except ValueError:
            print (f'entered values must be numeric, the input value: {client_id} not is numeric')
            client_id = None
    if not client_id:
        exit()


def delete_client(client_id):
    global clients

    if not clients[client_id]:
        print('''Client id was not found in the client's list''')
        input('...')
    else:
        clients.pop(client_id)


def update_client(client_id):
    global clients
    
    if len(clients)-1 < client_id:
        print(f'''Client {client_id} is not in client's list''')
        input('...')
    else:
        update_field_name =None
        while not update_field_name:
            update_field_name = input('What is the field to update?: ')

        try: 
            if not clients[client_id][update_field_name]:
                print(f''' The field {update_field_name} don't exist''')
                input('...')
            else:
                clients[client_id][update_field_name] = get_client_field(update_field_name)
                print (f''' The field {update_field_name} was updated to {clients[client_id][update_field_name]} ''')
                input('...')
        except KeyError:
            print('The Field Name was not found')
            input('...')


def search_client(client_name):
    
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def list_clients():

    clients_listados='''name     |    company     |       email        |       position        |\n'''
    for i in range(0, len(clients)):
        
        for idx, client in clients[i].items():
            if idx == 'position':
                clients_listados += f'''    {client}|\n''' 
            else:
                clients_listados += f'''    {client}|''' 
            
            
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
            | [exit] for finish program
            |---------------------------------------------------|
             
        This is de current list:
    {list_clients()}   ''')
    

def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        sistema = os.system('clear')
    else:
    # for windows platfrom
        sistema = os.system('cls')

if __name__ =='__main__':
    _initialize_clients_from_storage()

    paso = 'seguir'

    while paso == 'seguir':

        _print_welcome()
        command = input('''
             Please input option to do [C], [D], [U] or [Q]: 
             ''').upper()
        
        if command == 'Q':
            
            paso = 'parar'
        
        elif command == 'C':

            client = {
                'name': get_client_field('name'),
                'company':get_client_field('company'),
                'email':get_client_field('email'),
                'position':get_client_field('position'),
            }         
            create_client(client)
            
        elif command == 'D':

            client_id = get_client_by_id()
            delete_client(client_id)

        elif command == 'U':
            
            client_id = get_client_by_id()
            update_client(client_id)

        elif command == 'S':

            client_name = get_client_by_name()
            found = search_client(client_name)

            if found:
                print("The client is in client's list")
            else:
                print(f'''The client: {client_name}, is no in our client's List''')
                
            input('Back...')


        else: 
            print('Invalid Command')
            input('Back...')
        
        _save_clients_to_storage()
        
        screen_clear()