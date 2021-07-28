import os

birthday_dict={
    'Gabriel':'07-07-1990',
    'Yole':'12-10-1991',
    'Niko':'25-06-2015',
    'Irene':'05-02-2020'
}

def list_birthdays():

    birthday_str = ''
    for key in birthday_dict.keys():
        birthday_str+= f'{key} | '
    return birthday_str
    

def _welcome():
    print(f''' 
             ___________________________________________________
            | ************************************************* |
            | |||||||| Welcome to birthday dictionary||||||||||| | 
            | ************************************************* |
            |___________________________________________________|
            |  We know the birthdays of: 
            | {list_birthdays()}
    ''')


def get_birthdayer():
    birthdayer_name = None

    while not birthdayer_name:
        birthdayer_name = input('''
             Who's birthday do you want to look up?: ''')

        if birthdayer_name =='exit':
            birthdayer_name = None
            break

    if not birthdayer_name:
        exit()

    return birthdayer_name

def search_birthdayer(birthdayer_name):
    
    for person in birthday_dict.keys():
        if person != birthdayer_name:
            continue
        else:
            return birthday_dict[person]

def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        sistema = os.system('clear')
    else:
    # for windows platfrom
        sistema = os.system('cls')


if __name__=='__main__':
    paso = 'seguir'

    while paso == 'seguir':

        _welcome()
        birthdayer = get_birthdayer().capitalize()

        if search_birthdayer(birthdayer) is None:
            print('''
            *** No Data ***
            ''')
            input('...')

        elif search_birthdayer(birthdayer): 
            print(f'''
            |*** {birthdayer}'s birthday is  in {search_birthdayer(birthdayer)} ***|
                   ''')
            input('...')
        screen_clear()