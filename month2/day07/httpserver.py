
"""
httpserver v1.0
1. get request from
2.
"""
from socket import *
error_req = """HTTP/1.1 404 Not Found
Content-Type:text/html

error!
"""

def request(connfd):
    data = connfd.recv(4096)
    if not data:
        return
    print(data)
    if data.decode().split('\n')[0].split(" ")[1] == "/":
        with open("index.html") as f:
            response = "HTTP/1.1 200 ok\r\n"
            response += "\r\n"
            response += f.read()
    else:
        response = error_req
    connfd.send(response.encode())
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8000))
s.listen(3)

c,addr = s.accept()
print ("Connet from ",addr)
request(c)
s.close()