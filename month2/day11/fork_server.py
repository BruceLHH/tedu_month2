from socket import *
import os
import signal


# global content
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
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

signal.signal(signal.SIGCHLD,signal.SIG_IGN)
print ("Listen the port 9999......")

while True:
    try:
        c,addr = s.accept()
        print ("Connet from",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    ###
    pid = os.fork()
    if pid==0:
        s.close()
        haddle(c)
        os._exit(0)
    else:
        c.close()