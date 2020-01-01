from socket import *
from threading import Thread
import os,time
import signal

HOST = "192.168.1.14"
PORT = 9991
ADDR = (HOST,PORT)
FTP = "/home/lin/PycharmProjects/1905/month2/day06/"

class FTPServer(Thread):
    ## zi ding yi Thread class
    """
    look, upload, download, exit.
    """
    def __init__(self,connfd):
        self.__connfd = connfd
        super().__init__()

    def __get_list(self):
        files = os.listdir(FTP)
        if not files:
            self.__connfd.send(b"empty files")
            return
        else:
            self.__connfd.send(b"OK")
            time.sleep(0.1)
        ###
        filestr = ""
        for file in files:
            if file[0] != '.' and os.path.isfile(FTP+file):
                filestr += file + '\n'
        self.__connfd.send(filestr.encode())
    def __download(self,filename):
        try:
            f = open(FTP+filename,'rb')
        except Exception:
            self.__connfd.send(b"not found.")
            return
        else:
            self.__connfd.send(b"OK")
            time.sleep(0.1)
        while True:
            data = f.read(1024)  ### xunhuan read
            if not data:
                time.sleep(0.1) ## avoid zhanbao
                self.__connfd.send(b"##")
                break
            self.__connfd.send(data)
    def __upload(self,filename):
        if os.path.exists(FTP+filename):
            self.__connfd.send(b"file is exist.")
            return
        else:
            self.__connfd.send(b"OK")
        f = open(FTP+filename,"wb")
        while True:
            data = self.__connfd.recv(1024)
            if data == b"##":
                break
            f.write(data)
        f.close()
    def run(self):
        while True:
            data = self.__connfd.recv(1024).decode()
            if not data or data == "Q":
                return
            if data == "L":
                self.__get_list()
            elif data[0] == "G":
                filename = data.split(" ")[-1]
                self.__download(filename)
            elif data[0] == "P":
                filename = data.split(" ")[-1]
                self.__upload(filename)
            else:
                pass

def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(6)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    print("Listen the port 9991......")

    while True:
        try:
            c,addr = s.accept()
            print("Connet from", addr)
        except KeyboardInterrupt:
            os._exit(0)
        except Exception as e:
            print (e)
            continue

        t = FTPServer(c)
        t.setDaemon(True)
        t.start()  ## run

if __name__ == "__main__":
    main()