
class Persona:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    
    def say_hello (self):
        print(f'Hello, My name is {self.name} and i am {self.age} years old')

if __name__=='__main__':
    person = Persona('Gabriel', 30)
    print(f'The person name is {person.name}')
    person.say_hello()