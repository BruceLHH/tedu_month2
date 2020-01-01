from socket import socket

sockfd = socket()
sockfd.bind(("127.0.0.1",9991))
sockfd.listen(5)

print ("waiting for connect...")
connfd,addr = sockfd.accept()
with open("test_server_receive.egg","wb") as f:
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        f.write(data)

connfd.close()
sockfd.close()