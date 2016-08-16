from app import db
from datetime import datetime, timedelta

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
        
