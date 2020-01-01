from select import select
from socket import *

s = socket()
s.bind(("0.0.0.0",9999))
s.listen(5)

f = open("log.txt","r+")
print ("monitoring IO")
rs,ws,xs = select([s],[f],[],3)
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)