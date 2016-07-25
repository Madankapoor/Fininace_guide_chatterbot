from flask import Flask,render_template,request
import aiml
import os

kernel = aiml.Kernel()

app=Flask(__name__)

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml")
    kernel.saveBrain("bot_brain.brn")

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        sr= kernel.respond(request.form["message_box"])
    else:
        sr="Hi, How can I help in your queries related to Investments ?"
        
    return render_template("index.html",botreply=sr)