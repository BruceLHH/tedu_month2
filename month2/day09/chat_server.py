from socket import *
import os, sys

ADDR = ("0.0.0.0", 9999)
dict_user_info = {}  # name: addr

def do_login(s,name,addr):
    if name in dict_user_info:
        s.sendto("the user existed.".encode(),addr)
        return
    s.sendto(b"OK",addr)
    # notice other
    msg = "\nWellcome '%s' enter chat."%name
    print (msg)
    for i in dict_user_info:
        s.sendto(msg.encode(),dict_user_info[i])
    dict_user_info[name] = addr

def make_chat(s,name,text):
    ## creat two process to deal with recv and send
    msg = "\n%s: %s"%(name,text)
    print (msg)
    for i in dict_user_info:
        if i != name:
            s.sendto(msg.encode(),dict_user_info[i])
def do_quit(s,name):
    msg = "\n%s exit the chat."%name
    for i in dict_user_info:
        if i != name:
            s.sendto(msg.encode(),dict_user_info[i])
        else:
            s.sendto(b"EXIT",dict_user_info[i])
    del dict_user_info[name]
def do_request(s):
    while True:
        data, addr = s.recvfrom(2048)
        temp =data.decode().split(" ")
        if temp[0] == "L":
            do_login(s,temp[1],addr)
        elif temp[0] == "C":
            text = " ".join(temp[2:])
            make_chat(s,temp[1],text)
        elif temp[0] == "Q":
            do_quit(s,temp[1])
def main():
    # udp
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)


    pid = os.fork()
    if pid == 0: ########  manager send to info all user.
        while True:
            text = input("manager msg:")
            msg = "C manager"+text
            s.sendto(msg.encode(),ADDR)
    # deal with request from client
    do_request(s)


main()