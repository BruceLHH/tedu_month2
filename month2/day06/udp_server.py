
from socket import *
sockfd = socket(AF_INET,SOCK_DGRAM)


sockfd.bind(("127.0.0.1",9999))

while True:
    data,addr = sockfd.recvfrom(1024)
    print("receive info:",data.decode())
    if not data:
        break
    n = sockfd.sendto(b"Thanks data",addr)
sockfd.close()