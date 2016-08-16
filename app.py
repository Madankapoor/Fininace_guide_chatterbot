from flask import Flask,render_template,request,make_response
#Importing Libs 
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
@app.route('/Home')
def index():
    return render_template("Home.html",botreply="Hi, How can I help in your queries related to Investments ?")

@app.route('/login')
def login():
	return render_template("login.html",botreply="Hi, How can I help in your queries related to Investments ?")
 

@app.route('/register')
def register():
	return render_template("register.html",botreply="Hi, How can I help in your queries related to Investments ?")


@app.route('/team')
def team():
	return render_template("team.html",botreply="Hi, How can I help in your queries related to Investments ?")


@app.route('/contact')
def contact():
	return render_template("contact.html",botreply="Hi, How can I help in your queries related to Investments ?")





#route for mobile service
@app.route('/replyalone',methods=['GET','POST'])
def reply():
	if request.cookies.get('SessionID'):
		SessionID=request.cookies.get('SessionID')
		if request.method == 'POST':
			sr=kernel.respond(request.form["message_box"],SessionID)
		else:
			sr=kernel.respond(request.args.get('message_box'),SessionID)
		resp = make_response(sr)
	else:
		if request.method == 'POST':
			sr=kernel.respond(request.form["message_box"])
		else:
			sr=kernel.respond(request.args.get('message_box'))
		resp = make_response(sr)
		resp.set_cookie('SessionID', '1234')
	return resp

@app.route('/chat')
def chat():
    return render_template('chatui.html',botreply="Hi, How can I help in your queries related to Investments ?")