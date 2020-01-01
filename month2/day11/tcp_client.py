import socket
sockfd = socket.socket()
sockfd.connect(("192.168.1.24",8828))
while True:
    input_str = input("Input:")
    sockfd.send(input_str.encode())
    if not input_str:
        break
    data = sockfd.recv(1024)
    print ("Server:",data.decode())
sockfd.close()