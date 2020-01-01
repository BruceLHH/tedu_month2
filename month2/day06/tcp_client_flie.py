import socket
sockfd = socket.socket()
sockfd.connect(("192.168.1.14",9999))
with open("test.egg","rb") as f:
    while True:
        data = f.read(1024)
        sockfd.send(data)
        if not data:
            break
# data = sockfd.recv(1024)
# print ("Server:",data.decode())
sockfd.close()