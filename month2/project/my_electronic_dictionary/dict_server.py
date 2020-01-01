from socket import *
from select import *
from time import *
import os,pymysql

HOST = '192.168.1.14'
PORT = 9999
ADDR = (HOST,PORT)

class QueryWordManager:
    def __init__(self):
        self.__sockdf = socket()
        self.__rlist=[]
        self.__init_s()
    def __init_s(self):
        self.__sockdf.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.__sockdf.bind(ADDR)
        self.__sockdf.listen(10)
        self.__rlist.append(self.__sockdf)
        print("waiting for connect...")

    def __register(self,name,passwd):
        # print (name,passwd)
        db = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='123456',
                             database='dict',
                             charset="utf8"
                             )
        cur = db.cursor()
        sql = "select * from user where name=%s and password=%s;"
        cur.execute(sql,[name,passwd])
        db.commit()
        res=cur.fetchone()
        print ("fetchone,res:",res)
        if res:
            return "False"
        try:
            sql_inset = "insert into user (name,password) values(%s,%s);"
            cur.execute(sql_inset,[name,passwd])
            db.commit()
        except Exception as e:
            print(e)
            return "False"
        else:
            return "True"
    def __log_in(self):
        pass
    def __find_word(self):
        pass
    def __history(self):
        pass
    def main(self):
        wlist=[]
        xlist=[]
        while True:
            rs,ws,xs = select(self.__rlist,wlist,xlist)
            for r in rs:
                if r is self.__sockdf:
                    connfd,addr = r.accept()
                    self.__rlist.append(connfd)
                else:
                    data = r.recv(1024).decode()
                    data = data.strip().split(" ")
                    if not data:
                        self.__rlist.remove(r)
                        r.close()
                    elif data[0] == "R":
                        print (data[1],data[2])
                        r.send(self.__register(data[1],data[2]).encode())
                    elif data[0] == "L":
                        r.send(self.__log_in().encode())
                    elif data[0] == "W":
                        r.send(self.__find_word().encode)
                    elif data[0] == "H":
                        r.send(self.__history().encode())
                    else:
                        continue


if __name__ == "__main__":
    ser = QueryWordManager()
    ser.main()