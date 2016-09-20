import requests

url ='http://investmentchatter2-madankapoor.c9users.io/replyalone'
param={'message_box':'Hi'}
resp=requests.get(url=url,params=param)
print(resp.text);