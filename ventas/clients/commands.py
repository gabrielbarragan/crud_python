import click
from clients.services import ClientService
from clients.models import Client
from tabulate import tabulate

@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass

@clients.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='The client name')
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The client company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='The client email')
@click.option('-p', '--position',
              type=str,
              prompt=True,
              help='The client position')
@click.option('-s', '--salary',
              type=str,
              prompt=True,
              help='The client salary')
@click.pass_context
def create(ctx, name, company, email, position, salary):
    client = Client(name, company, email, position, salary)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """ Lis all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()

    headers = ['id','Name', 'Company', 'e-mail','Position','Salary']
    table = []
    
    print('-'*100)
    # print(clients_list)
    for client in clients_list:
        uid = client['uid']
        name = client['name']
        company = client['company']
        email = client['email']
        position = client['position']
        salary = client['salary']

        table.append( [uid,name,company,email,position,salary] )

    click.echo(tabulate(table, headers))

@click.argument('client_id')
@clients.command()
@click.pass_context
def update(ctx, client_id):
    """update a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()
    client = [client for client in client_list if client['uid'] == client_id]

    if client:
        client = _updated_client_flow(Client(**client[0]))
        client_service.update_client(client)
        click.echo("Client updated")
    else:
        click.echo("Client not found")

def _updated_client_flow(client):
    click.echo("leave empty if you don't want to modify the value")

    client.name = click.prompt('New name', type=str, default = client.name)
    client.company = click.prompt('New company', type=str, default = client.company)
    client.email = click.prompt('New email', type=str, default = client.email)
    client.position = click.prompt('New position', type=str, default = client.position)
    client.salary = click.prompt('New salary', type=str, default = client.salary)

    return client

@click.argument('client_id')
@clients.command()
@click.pass_context
def delete(ctx, client_id):
    """Deletes a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()
    client= [client for client in client_list if client['uid'] == client_id]

    if client:
        client = Client(**client[0])
        client_service.delete_client(client)
        click.echo("Client deleted")
    else:
        click.echo("Client not found")


all = clients