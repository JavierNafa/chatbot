from os import system, name 

def useful_answer(input):
    return True if input == 'y' else False

def clean(): 
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear') 

def help():
    print('***COMMANDS***')
    print('!search')
    print('!bye')
    print('!clean')