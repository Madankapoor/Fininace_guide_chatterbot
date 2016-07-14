from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Fin guide")
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.english")
chatbot.train("chatterbot.corpus.english.conversations")
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/', methods=['POST'])
def Botreply():
    if request.method == 'POST':
        sr=chatbot.get_response(request.form['message_box'])
    else:
        sr=""
    return render_template("index.html",botreply=sr)
