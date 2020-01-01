"""
dict server

function: logic handle
model: muitlprocess, tcp , process
"""

from socket import *
from multiprocessing import Process
import signal,sys
from mysql import Database

HOST = "192.168.1.14"
PORT = 8000
ADDR = (HOST,PORT)
db = Database(database="dict")

def register(c,data):
    tmp = data.split(" ")
    name = tmp[1]
    passwd = tmp[2]
    if db.register(name,passwd):
        c.send(b"OK")
    else:
        c.send(b"Failed")

def login(c,data):
    tmp = data.split(" ")
    name = tmp[1]
    passwd = tmp[2]
    if db.login(name,passwd):
        c.send(b"OK")
    else:
        c.send(b"Failed")
def query(c,data):
    tmp = data.split(" ")
    name = tmp[1]
    word = tmp[2]
    ## 1. get mean.
    mean = db.query(word)
    if not mean:
        c.send(b"not found.")
    else:
        msg = "%s: %s"%(word,mean)
        c.send(msg.encode())
        ## 2. insert history
        db.insert_history(name,word)
def get_histroty(c,data):
    tmp = data.split(" ")
    name = tmp[1]
    hist = db.get_histroty(name)
    if not hist:
        c.send(b"you history is empty.")
    else:
        for index in range(len(hist)):
            print ("hist[%d][0]:  "%index,hist[index][0])
            c.send(hist[index][0].encode())
        c.send(b"END")
def request(c):
    db.create_cursor()
    while True:
        data = c.recv(1024).decode()
        print (c.getpeername(),":",data)
        if data[0] == "E" or not data:
            sys.exit()
        if data[0] == "R":
            register(c,data)
        elif data[0] == "L":
            login(c,data)
        elif data[0] == "Q":
            query(c,data)
        elif data[0] == "H":
            get_histroty(c,data)
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)

    print ("Listen the port 8000")
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            connfd,addr = s.accept()
            print("Connet from",addr)
        except KeyboardInterrupt:
            s.close()
            db.close()
            sys.exit("server exit.")
        except Exception as e:
            print (e)
            continue

        ## create sub process
        p = Process(target=request,args=(connfd,))
        p.daemon = True
        p.start()



if __name__ == "__main__":
    main()




