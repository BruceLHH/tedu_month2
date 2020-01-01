from socket import *
import struct
sockdf =  socket(AF_INET,SOCK_DGRAM)
# sockdf.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
st = struct.Struct("i8sif")
while True:
    name = input("input name:")
    if not name:
        break
    id = int(input("input id:"))
    score = float(input("input score:"))
    age = int(input("input age:"))
    data = st.pack(id,name.encode(),age,score)
    sockdf.sendto(data,("127.0.0.1",9999))