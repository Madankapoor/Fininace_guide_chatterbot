from flask import Flask,render_template,request
from statichatter import  StaticChatterBot


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        sr= StaticChatterBot.chatterbot.get_response(request.form["message_box"])
    else:
        sr="Hi, How can I help in your queries related to Investments ?"
        
    return render_template("index.html",botreply=sr)