from socket import *
import sys,os,time
ADDR = ("192.168.1.14",9991)

class FTPClient:
    def __init__(self,sockfd):
        self.__sockfd = sockfd

    def get_list(self):
        self.__sockfd.send(b"L")
        data = self.__sockfd.recv(256).decode()
        if data == "OK":
            file_list = self.__sockfd.recv(4096)
            print(file_list.decode())
        else:
            print (data)
    def do_quit(self):
        self.__sockfd.send(b"Q")
        self.__sockfd.close()
        sys.exit("Thanks.")

    def get_file(self,filename):
        self.__sockfd.send(("G "+filename).encode())
        # wait for respose
        data = self.__sockfd.recv(128).decode()
        if data == "OK":
            f = open(filename,'wb+')
            while True:
                data = self.__sockfd.recv(1024)
                if data == b'##': ## mark
                    break
                f.write(data)
            #print (f.read().decode())
            f.close()
        else:
            print (data)
    def up_file(self,filename):
        try:
            f = open(filename, 'rb')
        except Exception:
            print("not find", filename)
            return
        time.sleep(0.1)
        filename = filename.split("/")[-1]
        self.__sockfd.send(("P "+filename).encode())
        data = self.__sockfd.recv(128).decode()
        if data == "OK":
            while True:
                data_file = f.read(1024)
                if not data_file:
                    time.sleep(0.1)
                    self.__sockfd.send(b"##")
                    break
                self.__sockfd.send(data_file)
        else:
            print (data)

def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print (e)
        return

    ftpclient = FTPClient(sockfd)
    while True:
        print ("-----------order list-----------")
        print ("""look list
download
upload
quit
--------------------------
        """)
        cmd = input("Please input order:")
        if cmd == "list":
            ftpclient.get_list()

        elif cmd.strip() == "quit":
            ftpclient.do_quit()
        elif cmd[:4] == "down":
            filename = cmd.strip().split(" ")[-1]
            ftpclient.get_file(filename)
        elif cmd[:2] == "up":
            filename = cmd.strip().split(" ")[-1]
            ftpclient.up_file(filename)
        else:
            print ("order wrong.")

if __name__ == "__main__":
    main()