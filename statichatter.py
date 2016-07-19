from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer


class StaticChatterBot:
    chatterbot = ChatBot("Training Example")
    chatterbot.set_trainer(ChatterBotCorpusTrainer)
    chatterbot.train("chatterbot.corpus.english")
    chatterbot.train("chatterbot.corpus.english.greetings")
    chatterbot.train("chatterbot.corpus.english.conversations")
    
    