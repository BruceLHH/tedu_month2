from multiprocessing import Process,Queue
from random import randint
from time import sleep
q = Queue()
def handle():
    for i in range(6):
        x = randint(1,33)
        q.put(x)
    q.put(randint(1,16))
def get_():
    list_res = []
    sleep(2)
    for i in range(6):
        x = q.get()
        list_res.append(x)
    list_res.sort()
    list_res.append(q.get())
    print (list_res)

p1 = Process(target = handle)
p2 = Process(target = get_)
p1.start()
p2.start()
p1.join()
p2.join()