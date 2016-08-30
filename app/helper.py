from flask_mail import Message
import requests
import json

team=['madankapoor10@gmail.com','manitkapoor2@gmail.com','chandrasoodan1996@gmail.com'];

def GetWelcomeMessage(Name,email):
   msg = Message('Welcome to Finchatbot Services', sender = 'finchatbot@gmail.com', recipients = [email])
   msg.body = "Welcome "+Name+" \nWe are Glad that you have registered and you are using our chat bot service,please contact us through the link below if you find any problems in our bot.\nThanking You.\n\n"+"https://finchatbot.herokuapp.com/contact"
   return msg

def GetContactMessage(Name,Email,M):
   msg = Message(Name+'('+Email+') has contacted us on Finchatbot Services', sender = 'finchatbot@gmail.com', recipients = team)
   msg.body = 'Message:\n'+M+'\n'
   return msg


def GetPasswordResetMessage(Name,Email,resetUrl):
   msg = Message('Request for Password Reset Finchatbot Services', sender = 'finchatbot@gmail.com', recipients = [email])
   msg.body = "Welcome "+Name+" \nPlease use the below link to reset you password.The link will expire in 24 hours.\nThanking You.\n\n"+resetUrl
   return msg

def BotCheck(captcha):
   site='6Lca5CgTAAAAALU5hkWTwZaPC-pMJydosgG6wZBo'
   r = requests.post("https://www.google.com/recaptcha/api/siteverify", data={'secret': site, 'response': captcha})
   D = json.loads(r.text)
   return D['success']