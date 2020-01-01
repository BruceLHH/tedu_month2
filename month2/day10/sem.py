from multiprocessing import Process,Semaphore
from time import sleep
import os

sem = Semaphore(3)

def fun01():
    sem.acquire()
    print ("%s run task"%os.getpid())
    sleep(2)
    print("%s task is ok." % os.getpid())
    sem.release()

for i in range(10):
    p = Process(target = fun01)
    p.start()
    p.join()