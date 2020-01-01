from multiprocessing import Process
import os,sys
from time import sleep

def th1():
    sleep(3)
    print ("eat")
    print (os.getppid(),'--',os.getpid())
def th2():
    sleep(2)
    print ("sleep")
    print (os.getppid(),'--',os.getpid())
def th3():
    sleep(4)
    print ("da doudou")
    print (os.getppid(),'--',os.getpid())
things = [th1,th2,th3]
jobs = []
for th in things:
    p = Process(target = th)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()


