import socket
sockfd = socket.socket()
sockfd.connect(("127.0.0.1",9996))
while True:
    input_str = input("Input:")
    sockfd.send(input_str.encode())
    if not input_str:
        break
    data = sockfd.recv(1200)
    print ("Server:",data.decode())
sockfd.close()