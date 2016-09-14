from flask import render_template,request,make_response,flash,redirect,url_for,g
from app import app,kernel,db,login_manager,bcrypt,mail
from helper import GetWelcomeMessage,GetContactMessage,GetPasswordResetMessage,BotCheck
from forms import RegistrationForm,LoginForm,ContactForm,ResetRequestForm,ResetForm
from models import User,Message,Reset
import chatprocess
import random
from flask_login import  login_required, login_user, logout_user, current_user
from hashinfo import Tags

# Helper Function
@login_manager.user_loader
def user_loader(user_id):
	return User.query.get(user_id)
#Main directory with out login
@app.route('/')
@app.route('/Home')
def index():
    return render_template("Home.html")

#Login Directory
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method ==  "POST":
        user = User.query.get(form.Email.data.lower())
        if user:
            if user.password == form.Password1.data:
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for("chat"))
            else:
            	flash("Please check your email Id or password as it is incorrect.")
        else:
        	flash("Please register as the entered Email ID doesn exists.")
    return render_template("login.html",form=form)


#Logout Directory
@app.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for("index"))

@app.route('/register',methods=['POST','GET'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        S=BotCheck(request.form.get('g-recaptcha-response'))
    	user = User.query.get(form.email.data.lower())
    	
    	if user:
    		flash('Entered Email ID is already registered with us.')
    		return render_template('register.html', form=form)
    	
    	if S==False:
    		flash('Entered Email ID is already registered with us or Invalid Bot Captcha')
    		return render_template('register.html', form=form)
    		
    	user=User(form.username.data,form.email.data.lower(),form.password.data,form.age.data)
    	db.session.add(user)
    	db.session.commit()
    	try:
    	    mail.send(GetWelcomeMessage(user.name,user.email))
        except:
            print("Error while Sending Mail")
        
        flash('Thanks for registering,you can login Now and start chating')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/team')
def team():
	return render_template("team.html")



@app.route('/contact', methods=["GET", "POST"])
def contact():
    form=ContactForm(request.form)
    if  request.method ==  "POST" and form.validate() :
        
        post_message=Message(form.name.data,form.email.data.lower(),form.message.data)
        db.session.add(post_message)
        db.session.commit()
        mail.send(GetContactMessage(post_message.name,post_message.email,post_message.message))
        flash('Your Message has been saved ,Thank you for contacting us.')
        app.logger.info(post_message.id)
    return render_template("contact.html",form=form)


@app.route('/resetrequest',methods=['GET','POST'])
def resetrequest():
    form=ResetRequestForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.get(form.email.data.lower())
        if user is None:
            flash("Entered email is not registerd,please check the email or register.")
            return redirect(url_for('resetrequest'))
        ResetRequest=Reset(form.email.data.lower())
        db.session.add(ResetRequest)
    	db.session.commit()
    	resetUrl='https://investmentchatter-madankapoor.c9users.io/reset?key='+str(ResetRequest.Key)+'&id='+str(ResetRequest.id)
    	mail.send(GetPasswordResetMessage(user.name,user.email,resetUrl))
        flash('Check you mail to reset you password and login in here to continue.')
        return redirect(url_for('login'))
    return render_template("resetrequest.html",form=form)

#Checking the request for validity
def CheckRequest(Id,KEY):
    row=Reset.query.get(Id)
    if row is None:
        return 0
    if row.Key == KEY and row.get_validity():
        return 1
    else:
        return 0
    
def get_email(Id):
    return Reset.query.get(Id).email

@app.route('/reset',methods=['GET','POST'])
def reset():
    form=ResetForm(request.form)
    if request.method == 'GET':
        id=int(request.args.get('id'))
        key=int(request.args.get('key'))
        if CheckRequest(id,key)==0:
            flash('The Request is invalid or expired.Please try again.')
            return redirect(url_for('login')) 
        resp = make_response(render_template('reset.html',form=form))
        resp.set_cookie('email',get_email(id))
        return resp
    
    if request.method == 'POST' and form.validate():
        S=BotCheck(request.form.get('g-recaptcha-response'))
        user=User.query.get(request.cookies.get('email'))
    	
    	if user is None:
    		flash("Entered Email ID is not registered with us.")
    		return render_template('register.html', form=form)
    	
    	if S==False:
    		flash('Invalid Bot Captcha,Please reuse the link.')
    		return redirect(url_for('login')) 
        user.password= form.confirm.data
        db.session.add(user)
        db.session.commit()
        flash('Password changed ,now you can login with you new password')
        return redirect(url_for('login')) 


@app.route('/chat')
@login_required
def chat():
	user=current_user
	Botreply="Hi "+current_user.name+", How can I help in your queries related to Investments ?"
	
	Greeting={'type':'bot','text':Botreply,'time':chatprocess.getTime()}
	
	try:
	    TextMessages=chatprocess.GetMessages(user.email)
	    #print(TextMessages)
	    TextMessages.append(Greeting)
	    return render_template('quotes.html',messages=TextMessages)
	except:
	    
	    chatprocess.reset(user.email,Botreply)
	    TextMessages=chatprocess.GetMessages(user.email)
	    return render_template('quotes.html')


@app.route('/chathome', methods=["GET"])
@login_required
def chathome():
    user=current_user
    Botreply="Hi "+current_user.name+", How can I help in your queries related to Investments ?"
    Greeting={'type':'bot','text':Botreply,'time':chatprocess.getTime()}
    form=ContactForm(request.form)
    try:
        TextMessages=chatprocess.GetMessages(user.email)
        #print(TextMessages)
        TextMessages.append(Greeting)
    except:
        chatprocess.reset(user.email,Botreply)
        TextMessages=chatprocess.GetMessages(user.email)
    return render_template("homel.html",messages=TextMessages)
    
@app.route('/chatteam', methods=["GET"])
@login_required
def chatteam():
    user=current_user
    Botreply="Hi "+current_user.name+", How can I help in your queries related to Investments ?"
    Greeting={'type':'bot','text':Botreply,'time':chatprocess.getTime()}
    form=ContactForm(request.form)
    try:
        TextMessages=chatprocess.GetMessages(user.email)
        #print(TextMessages)
        TextMessages.append(Greeting)
    except:
        chatprocess.reset(user.email,Botreply)
        TextMessages=chatprocess.GetMessages(user.email)
    return render_template("teaml.html",messages=TextMessages)

@app.route('/contactform', methods=["GET", "POST"])
@login_required
def chatcontact():
    user=current_user
    Botreply="Hi "+current_user.name+", How can I help in your queries related to Investments ?"
    Greeting={'type':'bot','text':Botreply,'time':chatprocess.getTime()}
    form=ContactForm(request.form)
    try:
        TextMessages=chatprocess.GetMessages(user.email)
        #print(TextMessages)
        TextMessages.append(Greeting)
    except:
        chatprocess.reset(user.email,Botreply)
        TextMessages=chatprocess.GetMessages(user.email)
	 
    if  request.method ==  "POST" and form.validate() :
        post_message=Message(form.name.data,form.email.data.lower(),form.message.data)
        db.session.add(post_message)
        db.session.commit()
        mail.send(GetContactMessage(post_message.name,post_message.email,post_message.message))
        flash('Your Message has been saved ,Thank you for contacting us.')
        app.logger.info(post_message.id)
    return render_template("contactform.html",form=form,messages=TextMessages)


#route for mobile service
@app.route('/replyalone',methods=['GET','POST'])
def replyalone():
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
		resp.set_cookie('SessionID', str(random.randint(1,999999)))
	return resp

@app.route('/reply',methods=['GET','POST'])
@login_required
def reply():
    if request.method == 'POST':
        userreply=request.form["message_box"]
    else:
        userreply=request.args.get('message_box')
    sr=""
    
    if '#'== userreply[0]:
        tag=userreply[1::].lower()
        if tag in Tags.keys():
            try:
                chatprocess.add(current_user.email,userreply,Tags[tag])
            except:
                print('Error in saving the chat')
            
            return Tags[tag]
        
    if request.cookies.get('SessionID'):
        SessionID=request.cookies.get('SessionID')
        sr=kernel.respond(userreply,SessionID)
    else:
        SessionID=str(random.randint(1,999999))
        sr=kernel.respond(userreply)
    
    try:
        resp = make_response(sr)
        resp.set_cookie('SessionID',SessionID )
        chatprocess.add(current_user.email,userreply,sr)
        return resp

    except:
        if sr==null:
            resp = make_response("Some error occured in bot Please try chatting again")
        else:
            resp = make_response("Some error occured Please try chatting again")
        return resp



@app.route("/mobilelogin", methods=[ "POST"])
def mlogin():
    form = LoginForm(request.form)
    if request.method ==  "POST":
        user = User.query.get(form.Email.data.lower())
        if user:
            if user.password == form.Password1.data:
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return "Success"
            else:
            	return "Please check your email Id or password as it is incorrect."
        else:
        	return "Please register as the entered Email ID doesn exists."
    return "Failed Please check if all inputs are valid or try after some time."





@app.route("/mobilelogout", methods=["GET"])
@login_required
def mlogout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return "Success"
