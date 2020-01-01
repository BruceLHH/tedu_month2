from multiprocessing import Value,Array,Process
from random import randint
import time
obj = Value('i',5000)
def deposit():
    for day_ in range(30):
        time.sleep(.2)
        obj.value += randint(1,1000)

def withdraw():
    for day_ in range(30):
        time.sleep(.15)
        obj.value -= randint(200,800)

p1 = Process(target = deposit)
p2 = Process(target = withdraw)
p1.start()
p2.start()
p1.join()
p2.join()
print (obj.value)