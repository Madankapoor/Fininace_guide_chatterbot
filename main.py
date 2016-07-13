from flask import Flask,render_template,request,request,make_response,abort, redirect, url_for,session,escape

app=Flask(__name__)

@app.route('/')
@app.route('/<user>/')
def index(user=None):
    return render_template(index.html,name=user)
    
