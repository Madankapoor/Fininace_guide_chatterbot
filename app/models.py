from app import db
from datetime import datetime
import random


class User(db.Model):
    __tablename__ = "users"
    name=db.Column(db.String(50))
    email = db.Column(db.String(50),index=True,unique=True,primary_key=True )
    password = db.Column(db.String(40) )
    age = db.Column(db.Integer)
    registered_on = db.Column('registered_on' , db.DateTime)
    authenticated = db.Column(db.Boolean, default=False)
    
    def __init__(self , name ,email,password,age):
        self.name = name
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()
        self.age =age
    
    
    @property
    def is_authenticated(self):
        return self.authenticated
        
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email  # python 2
        
class Message(db.Model):
    __tablename__ = "Messages"
    id= db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50))
    email = db.Column(db.String(50))
    message = db.Column(db.String(200))
    time = db.Column('Sent_on' , db.DateTime)
    def __init__(self , name ,email,message):
        self.name = name
        self.email = email
        self.message = message
        self.time =datetime.utcnow()
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id  # python 2

class Reset(db.Model):
    __tablename__ = "reset"
    id= db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(50),db.ForeignKey("users.email"), nullable=False)
    time = db.Column('Sent_on' , db.DateTime)
    Key =db.Column(db.Integer,unique=True)
    
    def __init__(self ,email):
        self.email = email
        self.time =datetime.utcnow()
        self.Key = random.randrange(0,7897984561)
    
    def get_id(self):
        return self.id  # python 2
    
    
    
    def get_key(self):
        return self.Key
    
    def get_validity(self):
        Time = datetime.utcnow()
        if ((Time-(self.time)).total_seconds() <=3600):
            return True
        else:
            return False
    
    


