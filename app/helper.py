from flask_mail import Message
import requests
import json
import random
team=['madankapoor10@gmail.com','manitkapoor2@gmail.com','chandrasoodan1996@gmail.com'];
factsloaded=False
facts=[]
def GetWelcomeMessage(Name,email):
   msg = Message('Welcome to Finchatbot Services', sender = 'finchatbot@gmail.com', recipients = [email])
   msg.body = "Welcome "+Name+" \nWe are Glad that you have registered and you are using our chat bot service,please contact us through the link below if you find any problems in our bot.\nThanking You.\n\n"+"https://finchatbot.herokuapp.com/contact"
   return msg

def GetContactMessage(Name,Email,M):
   msg = Message(Name+'('+Email+') has contacted us on Finchatbot Services', sender = 'finchatbot@gmail.com', recipients = team)
   msg.body = 'Message:\n'+M+'\n'
   return msg


def GetPasswordResetMessage(Name,Email,resetUrl):
   msg = Message('Request for Password Reset Finchatbot Services', sender = 'finchatbot@gmail.com', recipients = [Email])
   msg.body = "Welcome "+Name+" \nPlease use the below link to reset you password.The link will expire in 1 hours.\nThanking You.\n\n"+resetUrl
   return msg

def BotCheck(captcha):
   site='6Lca5CgTAAAAALU5hkWTwZaPC-pMJydosgG6wZBo'
   r = requests.post("https://www.google.com/recaptcha/api/siteverify", data={'secret': site, 'response': captcha})
   D = json.loads(r.text)
   return D['success']


def getfacts():
   if(len(facts)==0):
      Fp=open('./app/data/facts.html','r')
      for x in Fp:
         facts.append(x)
      Fp.close()
      factsloaded=True;
   num=random.randint(0,10000)
   if(num%3==0 or num%5==0):
      return '<h5>Did you know ?</h5><sub>'+facts[random.randint(0,len(facts))]+'</sub>'
   else:
      return ''