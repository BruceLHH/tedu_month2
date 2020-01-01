from socket import *

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(("127.0.0.1",9996))
sockfd.listen(1000)
while True:
    print ("waiting for connect...")
    try:
        connfd,addr = sockfd.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        print("Server exit.")
        break
    except Exception as e:
        print(e)
        continue

    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print("receive data: ",data.decode())
        send_data = input("server send info:")
        n = connfd.send(send_data.encode())
        print ("had send %d bytes."%n)
    connfd.close()
sockfd.close()