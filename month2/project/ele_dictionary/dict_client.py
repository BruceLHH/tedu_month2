"""
dict client

function: input, send request, get result
struct :  interface --> register, log in, exit.
         sub interface --> find word , find history ,
"""
from socket import *
from getpass import *
import sys
ADDR = ("192.168.1.14",8000)
s = socket()
s.connect(ADDR)

class Dict_client:
    def __init__(self):
        pass
    def register(self):
        while True:
            name = input("User:")
            passwd = getpass()
            passwd1 = getpass("Again:")
            if passwd != passwd1:
                print("password diff.")
                continue
            if " " in name or " " in passwd:
                print("can't input space.")
                continue
            msg = "R %s %s"%(name,passwd)
            s.send(msg.encode())
            data = s.recv(128).decode()
            if data=="OK":
                print ("register success.")
            else:
                print("register failed.")
            return

    def login(self):
        name = input("User:")
        passwd = getpass("password:")
        msg = "L %s %s" % (name, passwd)
        s.send(msg.encode())
        data = s.recv(128).decode()
        if data == "OK":
            print("login success.")
            self.log_interface(name)
        else:
            print("login failed.")
        return

    def query(self,name):
        while True:
            word = input("Please input word:")
            if word == "##":
                break
            msg = "Q %s %s"%(name,word)
            s.send(msg.encode())
            data = s.recv(2048).decode()
            print(data)
    def history(self,name):
        msg = "H %s"%name
        s.send(msg.encode())
        while True:
            data = s.recv(1024).decode()
            if data == "END":
                break
            elif data == "you history is empty.":
                print (data)
                break
            print (data)

    def log_interface(self,name):
        while True:
            print(
""" -------------Query-----------------
        1.query  2.history  3.logout
    -----------------------------------""")
            num = input("please number:")
            if num == '1':
                self.query(name)
            elif num == '2':
                self.history(name)
            elif num == '3':
                break
            else:
                print("please repeat input number.")

    def main(self):
        while True:
            print(
"""   -------------welcome-------------
         1.register  2.log in  3.exit
      ---------------------------------""")
            num = input("please input number:")
            if num == '1':
                self.register()
            elif num =='2':
                self.login()
            elif num =='3':
                s.send(b'E')
                sys.exit("Thinks.")
            else:
                print ("please repeat input.")


if __name__ == "__main__":
    client = Dict_client()
    client.main()
