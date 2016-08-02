from flask import Flask,render_template,request

 
import aiml
import os

kernel = aiml.Kernel()

app=Flask(__name__)

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

#Main index
@app.route('/')
def index():
    return render_template("index.html",botreply="Hi, How can I help in your queries related to Investments ?")


#route for mobile service
@app.route('/replyalone',methods=['GET','POST'])
def reply():
    if request.method == 'POST':
        sr=kernel.respond(request.form["message_box"])
    else:
        sr=kernel.respond(request.args.get('message_box'))
    return "Guide:"+sr

@app.route('/chat')
def chat():
    return render_template('chatui.html')