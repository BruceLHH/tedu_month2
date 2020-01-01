"""
http server 2.0
"""
from socket import *
from select import *
import os,sys

class HTTPServer:
    def __init__(self,host="0.0.0.0",port=8000,dir=None):
        self.__host = host
        self.__port = port
        self.__dir = dir
        self.__addr = (host,port)
        self.__rlist = []
        self.__create_socket()
        self.__bind()
    def __create_socket(self):
        self.__sockfd = socket()
        self.__sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    def __bind(self):
        self.__sockfd.bind(self.__addr)

    def serve_forever(self):
        self.__sockfd.listen(4)
        print ("Listen the prot %d"%self.__port)
        ### IO duo lu fuyong
        self.__rlist.append(self.__sockfd)
        wlist = []
        xlist = []
        while True:
            rs,ws,xs = select(self.__rlist,wlist,xlist)
            for r in rs:
                if r is self.__sockfd:
                    connfd,addr = self.__sockfd.accept()
                    print ("Connect from",addr)
                    self.__rlist.append(connfd)
                else:
                    #print (r.recv(2048).decode())
                    self.__haddle(r)

    def __haddle(self, c):
        data = c.recv(1024).decode()
        ## analysis info
        if not data:
            # client interrupt
            self.__rlist.remove(c)
            c.close()
            print(data)
            return

        info =data.split('\n')[0].split(" ")[1]
        print (c.getpeername(),":",info)
        if info == "/" or info[-5:]==".html":
            self.__get_html(c,info)
        else:
            pass
            #self.__get_other()
    def __get_html(self,c,info):
        if info == "/":
            filename = self.__dir + info + "news.html"
        else:
            filename = self.__dir + info
        try:
            f = open(filename,"r")
        except Exception:
            # failed
            response = "HTTP/1.1 404 Not Found\r\n"
            response+= "Content-Type:text/html\r\n"
            response+= "\r\n"
            response+= "<h1> failed.</h1>"
        else:
            # sucess
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += f.read()
        finally:
            # process
            c.send(response.encode())

if __name__ == "__main__":
    """
    
    """
    HOST = "192.168.1.14" #"0.0.0.0"
    PORT = 8000
    DIR = './static'
    httpd = HTTPServer(HOST,PORT,DIR)
    httpd.serve_forever()


