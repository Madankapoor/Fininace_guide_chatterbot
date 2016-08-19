from flask import render_template,request,make_response,flash,redirect,url_for,g
from app import app,kernel,db,login_manager,bcrypt
from forms import RegistrationForm , LoginForm ,ContactForm
from models import User,Message

from flask_login import  login_required, login_user, logout_user, current_user

@login_manager.user_loader
def user_loader(user_id):
	return User.query.get(user_id)

 
@app.route('/')
@app.route('/Home')
def index():
    return render_template("Home.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method ==  "POST":
        user = User.query.get(form.Email.data)
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
    	user = User.query.get(form.email.data)
    	if user:
    		flash('Entered Email ID is already registered with us.')
    		return render_template('register.html', form=form)
    	user=User(form.username.data,form.email.data,form.password.data,form.age.data)
    	db.session.add(user)
    	db.session.commit()
        flash('Thanks for registering,you can login Now and start chating')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
	


@app.route('/team')
def team():
	return render_template("team.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form=ContactForm()
    if form.validate_on_submit() and request.method ==  "POST":
        db.session.add(Message(form.name.data,form.email.data,form.message.data))
        db.session.commit()
        flash('Your Message has been saved ,Thank you for contacting us.')
        return redirect(url_for('home'))
    return render_template("contact.html",form=form)


@app.route('/chat')
@login_required
def chat():
	user=current_user
	return render_template('quotes.html',botreply="Hi, How can I help in your queries related to Investments ?")
	
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