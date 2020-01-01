import struct
from socket import *
sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.bind(("127.0.0.1",9999))
st = struct.Struct("i8sif")

f = open("students_info.txt","a")
while True:
    data,addr = sockfd.recvfrom(1024)
    if not data:
        break
    data = st.unpack(data) # tuple (id,b'name',21,98)
    data = "%d,%-10s,%d,%.3f\n"%data
    f.write(data)
    n = sockfd.sendto(b"Thanks data",addr)
sockfd.close()
f.close()