from flask_wtf import Form
from wtforms import BooleanField, StringField, PasswordField, validators ,IntegerField ,ValidationError ,TextAreaField

class RegistrationForm(Form):
    username = StringField(u'Username', [validators.Length(min=4, max=25)])
   
    password = PasswordField(u'New Password', [
        validators.DataRequired(),
        validators.EqualTo(u'confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    age = IntegerField(u'Age')
    email = StringField(u'Email Address', [validators.Length(min=6, max=35)])
    
    def validate_age(form, field):
        if field.data < 13:
            raise ValidationError("We're sorry, you must be 13 or older to register")


class LoginForm(Form):
    Email= StringField(u'Email Address', [validators.Length(min=6, max=35),validators.DataRequired()])
    Password1 =PasswordField(u'Password', [validators.DataRequired()])

class ContactForm(Form):
     name = StringField(u'Username', [validators.Length(min=4, max=30)])
     email= StringField(u'Email Address', [validators.Length(min=6, max=35),validators.DataRequired()])
     message = TextAreaField(u'Message ', [validators.optional(), validators.length(max=200)])
    

class ResetRequestForm(Form):
     email= StringField(u'Email Address', [validators.Length(min=6, max=35),validators.DataRequired()])


class ResetForm(Form):
    password = PasswordField(u'New Password', [validators.DataRequired(),
        validators.EqualTo(u'confirm', message='Passwords must match')])
    confirm = PasswordField(u'Repeat Password')
    