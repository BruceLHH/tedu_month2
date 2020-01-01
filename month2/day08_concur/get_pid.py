import os
from time import sleep
pid = os.fork()

if pid<0:
    print("error")
elif pid==0:
    sleep(1)
    print("get parent PID:",os.getppid())
    print ("child PID:",os.getpid())
else:
    print ("get child PID:",pid)
    print ("parent PID:",os.getpid())