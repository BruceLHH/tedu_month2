from multiprocessing import Process
import signal
import os,sys
from socket import *
HOST = '192.168.1.14'
PORT = 9999
ADDR = (HOST,PORT)

def haddle(c):
    while True:
        data = c.recv(2048)
        if not data:
            break
        print(data.decode())
        c.send(b"OK.")
    c.close()

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

signal.signal(signal.SIGCHLD,signal.SIG_IGN)
print ("Listen the port 9999...")
####
while True:
    try:
        c,addr = s.accept()
        print ("Connect from",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print (e)

    ### multi process
    p = Process(target = haddle,args=(c,))
    p.daemon = True
    p.start()


