from flask import Flask,render_template,request
from chatterbot.training.trainers import ListTrainer

chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ListTrainer)

chatterbot.train([
    "Hi there!",
    "Hello",
])

chatterbot.train([
    "Greetings!",
    "Hello",
])

app=Flask(__name__)






@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        sr=chatbot.get_response(request.form["message_box"])
    else:
        sr=""
    return render_template("index.html",botreply=sr)
    