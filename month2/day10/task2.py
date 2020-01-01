from threading import Thread
from multiprocessing import Process
import time

def count(x,y):
    c = 0
    while c<7000000:
        x += 1
        y += 1
        c += 1

##1. one process
one_pro_starttime = time.time()
for i in range(10):
    p = Process(target = count,args=(300,500))
    p.start()
    p.join()
print ("one process cost %d s."%(time.time() - one_pro_starttime))
## 2. multi process
ten_pro_start_time = time.time()
objs = []
for i in range(10):
    p = Process(target = count,args=(300,500))
    objs.append(p)
    p.start()

for i in objs:
    i.join()
print ("ten process cost %d s."%(time.time() - ten_pro_start_time))

## 3. multi Thread
ten_thread_s_t = time.time()
t_objs =[]
for i in range(10):
    t = Thread(target = count,args=(300,500))
    t_objs.append(t)
    t.start()

for i in t_objs:
    i.join()
print ("ten Thread cost %d s."%(time.time() - ten_thread_s_t))
