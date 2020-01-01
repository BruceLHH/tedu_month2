from socket import *
import signal
import os,sys
ADDR = ("127.0.0.1",9999)

def make_chat(name,s):
    # creat child process
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    pid = os.fork()
    if pid<0:
        sys.exit("Error.")
    if pid==0: # child
        ## send
        while True:
            try:
                text = input("input chat content:")
            except KeyboardInterrupt:
                text = 'quit'
            if text.strip() == 'quit':
                msg = "Q "+name
                s.sendto(msg.encode(),ADDR)
                sys.exit("exit chat.")
            msg = "C %s %s"%(name,text)
            s.sendto(msg.encode(),ADDR)
    else:
        ## receive infomation
        while True:
            try:
                data,addr = s.recvfrom(1024)
            except KeyboardInterrupt:
                sys.exit()
            if data.decode() == "EXIT":
                sys.exit()
            print (data.decode() + "\nsaid:",end='')

def main():
    # udp
    s = socket(AF_INET,SOCK_DGRAM)
    while True:
        name = input("Please input you name:")
        s.sendto(("L "+name).encode(),ADDR)
        rec_data,addr = s.recvfrom(2048)
        if rec_data.decode() == "OK":
            print("Entered chat.")
            break
        else:
            print(rec_data.decode())
    make_chat(name,s)

main()