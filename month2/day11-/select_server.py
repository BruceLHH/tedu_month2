"""

"""
from socket import *
from select import select

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("192.168.1.14",9999))
s.listen(5)

rlist = [s]
wlist = []
xlist = []

while True:
    rs,ws,sx = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            connfd,addr = s.accept()
            print ("Connect from",addr)
            rlist.append(connfd)
        else:
            data = r.recv(1024).decode()
            if not data:
                r.close()
                rlist.remove(r)
                continue
            print (data)
            #r.send(b"OK")
            wlist.append(r) ######
    for w in ws:
        w.send(b"OK")
        wlist.remove(w)
    for x in sx:
        pass