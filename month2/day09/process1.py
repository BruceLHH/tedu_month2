from multiprocessing import Process
from time import time,sleep

def fun01():
    print("start a process.")
    sleep(2)
    print ("finish a process.")

p = Process(target = fun01)
p.start()
p.join()

"""
pid = os.fork()
if pid == 0:
    fun01()
    os._exit()
else:
    os.wait()
"""