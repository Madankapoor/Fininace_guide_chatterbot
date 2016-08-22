from libc.stdio cimport fopen,fclose,FILE,fputs,fgets
import datetime

def getTime():
    return datetime.datetime.now().strftime("%I:%M %p %d/%m/%Y")

def reset(e,br):
    e="./app/templates/chat/"+e+".html"
    r="bot\n"+br+"\n"+getTime()+"\n"
    cdef FILE* p
    cdef char *email=e
    cdef char* reply=r
    p=fopen(e, "w+")
    if p==NULL:
        print("File not found")
    else:
        fputs(reply,p)
        fclose(p) 
    
def add(e,r,re):
    e="./app/templates/chats/"+e+".html"
    r="user\n"+r+"\n"+getTime()+"\n"
    re="bot\n"+re+"\n"+getTime()+"\n"
    cdef FILE* p
    cdef char *email=e
    cdef char* request=r
    cdef char* reply=re
    print("aSSIGN COMPLETE")
    p = fopen(e, "a")
    if p == NULL:
        print("Using write")
        p=fopen(e,"w")
    if p== NULL:
        print("File not found")
    else:
        print("Using write")
        fputs(request,p)
        fputs(reply,p)
        fclose(p)
    
def GetMessages(e):
    e="./app/templates/chats/"+e+".html"
    cdef FILE* p
    cdef char st[1000];
    cdef char* s;
    result=[]
    
    p = fopen(e, "r")
    
    if p ==NULL:
        return result
    s=fgets(st,999,p)
    while s!= NULL:
        message={}
        message['type']=s
        s=fgets(st,999,p)
        message['text']=s
        s=fgets(st,999,p)
        message['time']=s
        result.append(message)
        s=fgets(st,999,p)
        
    return result
    

    