PASSWORD = '0987654321'

def password_required(func):
    def wrapper(): #convención
        password = input('Please input your password: ')

        if password == PASSWORD:
            return func()
        else:
            print ('password wrong')
    return wrapper

@password_required
def needs_password():
    print('La contraseña es correcta')

def upper_name(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        return result.upper()
    return wrapper

@upper_name
def say_my_name(name):
    return f'Hello {name}'



if __name__=='__main__':
    print(say_my_name('David'))