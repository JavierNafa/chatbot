from settings import db_url
from chatbot_search import search
from response_generator import generate_response
from chatterbot import ChatBot,utils,conversation
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer

bot = ChatBot('',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri=db_url,
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ])

corpus_trainer = ChatterBotCorpusTrainer(bot)
list_trainer = ListTrainer(bot)
list_trainer.show_training_progress = False
corpus_trainer.train(
    "chatterbot.corpus.english"
)

def proccess_response(user_input:str):
    raw_text = search(user_input)
    if raw_text:
        response = generate_response(raw_text,user_input)
        return response,True
    return "I'm sorry I can't find anything :(",False

def learn(response:str,user_input:str):
    list_trainer.train([
        user_input,
        response
    ])

def talk(user_input:str):
    bot_response = bot.get_response(user_input)
    return bot_response