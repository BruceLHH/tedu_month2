from socket import *

s = socket()
s.bind(("0.0.0.0",8000))
s.listen(3)

c,addr = s.accept()
print ("Connet from ",addr)
data = c.recv(4096)
print (data)

c.close()
s.close()