from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Ron Obvious")
chatbot.set_trainer(ChatterBotCorpusTrainer)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        sr=chatbot.get_response(request.form["message_box"])
    else:
        sr="Hi, How can I help in your queries related to Investments ?"
        
    return render_template("index.html",botreply=sr)