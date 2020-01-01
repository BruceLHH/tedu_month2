from socket import *
from time import ctime,sleep

f= open("log.txt","a+")
s = socket()
s.bind(("192.168.1.14",9990))
s.listen(5)

# s.setblocking(False)
s.settimeout(3)
while True:
    print ("Waiting for connect....")
    try:
        connfd,addr = s.accept()
    except (BlockingIOError,timeout) as e:
        sleep(5)
        f.write("%s :%s\n"%(ctime(),e))
        f.flush()
    else:
        print ("Connet from ",addr)
        data =connfd.recv(1024).decode()
