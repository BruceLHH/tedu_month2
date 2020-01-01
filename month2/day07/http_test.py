from socket import *

s = socket()
s.bind(("0.0.0.0",8000))
s.listen(3)

c,addr = s.accept()
print ("Connet from ",addr)
data = c.recv(4096)
print (data)

response = """HTTP/1.1 200 ok
Content-Type:text/html

Hello lin little.
"""
c.send(response.encode())

c.close()
s.close()