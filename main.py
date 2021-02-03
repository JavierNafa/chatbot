from utils import useful_answer,help,clean
from chatbot_utils import proccess_response, learn, talk

print('***To see all the available commands type help***\r')

alive = 1
while alive:
    user_input = input('\nTalk to bot: ').lower()
    if user_input == '!help':
        help()
    elif user_input == '!search':
        search_mode_active = 1
        print('To exit from this mode, write !bye')
        print('BOT: You entered to the search mode, please write your question\n')
        while search_mode_active:
            user_input = input('Search: ').lower()
            if user_input == '!bye':
                search_mode_active = 0
            elif user_input == '!clean':
                clean()
            else:
                response,found = proccess_response(user_input)
                if found:
                    print(f'BOT: {response}')
                    useful =  input('\nWas this answer helpful to you? \nY/N: ').lower()
                    if(useful_answer(useful)):
                        learn(response,user_input)
                        print('BOT: Thank you :)')
                    else:
                        print('BOT: Sorry :( ')
                else:
                    print(f'BOT: {response}')
    elif user_input == '!bye':
        alive = 0
        print('BOT: Bye :)')
    elif user_input == '!clean':
        clean()
    else:
        bot_response = talk(user_input)
        print(f'BOT: {bot_response}')
            