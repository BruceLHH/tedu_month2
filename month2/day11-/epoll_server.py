from select import *
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",9999))
s.listen(4)

fdmap = {s.fileno():s}

ep = epoll()
ep.register(s,EPOLLIN|EPOLLERR)

while True:
    events = ep.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print ("Connect from",addr)
            ep.register(c,EPOLLIN|EPOLLERR)
            fdmap[c.fileno()] = c
        elif event&POLLIN:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                ep.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print (data)
            fdmap[fd].send(b"OK")
