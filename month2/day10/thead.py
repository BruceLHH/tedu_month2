from threading import Thread
import os
a =1
def fun01():
    global a
    print ("a:",a)
    a = 999
    print ("sub thread.",os.getpid())

t = Thread(target = fun01)
t.start()
print (os.getpid())
t.join()
print ("a:",a)