import os
from socket import *

HOST = '192.168.1.14'
PORT = 9999
ADDR = (HOST,PORT)

class QueryWordUI:
    def __init__(self,name,passwd):
        self.__s = socket()
        self.__s.connect(ADDR)
        self.__name=name
        self.__passwd = passwd
    def __register(self):
        send_str = "R "+self.__name+" " +self.__passwd
        self.__s.send(send_str.encode())
        data = self.__s.recv(64)
        return data.decode()
    def __sub_interface(self):
        pass
    def __log_in(self):
        pass
    def __exit(self):
        pass
    def interface(self):
        while True:
            print ("""
            ---------------Wellcome------------
            1.register  2.log in    3. exit
            -----------------------------------
            """)
            num_str = input("please input:")
            if num_str == '1':
                if self.__register()=="True":
                    print("register success.")
                    print ("log in success.")
                    self.__sub_interface()
                else:
                    print("The name is exist.")
            elif num_str == '2':
                if self.__log_in():
                    print("log in success.")
                    self.__sub_interface()
                else:
                    print("name or password is wrong.")
            elif num_str == '3':
                self.__exit()
            else:
                print("Please repeat input.")

if __name__ == "__main__":
    name = "anly"
    passwd = '123654'
    cli = QueryWordUI(name,passwd)
    cli.interface()