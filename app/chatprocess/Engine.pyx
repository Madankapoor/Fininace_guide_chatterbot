from libc.stdio cimport fopen,fclose,FILE,fputs
import datetime

def getTime():
    return datetime.datetime.now().strftime("%I:%M %p %d/%m/%Y")

def reset(e,br):
    e="./app/templates/"+e
    r="<div class='messagebot'><div class='botreply'>"+br+"</div><br><sub>"+getTime()+"</sub></div>"
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
    r="<div class='messageuser'><div class='userrequest'>"+r+"</div><br><sub>"+getTime()+"</sub></div>"
    re="<div class='messagebot'><div class='botreply'>"+re+"</div><br><sub>"+getTime()+"</sub></div>"
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



    