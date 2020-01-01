from threading import Thread,Lock

a = b =0
lock = Lock()
def fun01():
    while True:
        lock.acquire()
        if a!=b:
            print ("a=%d, b=%d"%(a,b))
        lock.release()
t = Thread(target = fun01)
t.start()

while True:
    with lock:
        a += 1
        b += 1
t.join()