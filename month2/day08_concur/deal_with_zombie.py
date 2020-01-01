import os,sys
from time import sleep

def f1():
    for i in range(3):
        sleep(2)
        print("write code")
def f2():
    for i in range(2):
        sleep(4)
        print("test code")

pid = os.fork()
if pid<0:
    print ("failed.")
elif pid == 0:
    p = os.fork()
    if p==0: #grandson
        f1()
    else:#chile
        os._exit(0)
else:
    os.wait()
    f2()