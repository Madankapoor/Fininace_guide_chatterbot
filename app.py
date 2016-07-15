from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Candru")
chatbot.set_trainer(ChatterBotCorpusTrainer)

chatbot.train("chatterbot.corpus.english.conversations")


app=Flask(__name__)






@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        sr=chatbot.get_response(request.form["message_box"])
    else:
        sr=""
    return render_template("index.html",botreply=sr)
    