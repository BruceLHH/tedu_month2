from socket import *
ADDR = ("127.0.0.1",9999) #addr of server
socket = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input("Msg>>")
    if not data:
        break
    socket.sendto(data.encode(),ADDR)
socket.close()