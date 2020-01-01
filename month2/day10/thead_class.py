"""

"""
from threading import Thread
class ThreadClass(Thread):
    def __init__(self,*args,**kwargs):
        self.attr = args[0]
        super().__init__()
    def fun01(self):
        print ("fun01")
    def fun02(self):
        pass
    def run(self):  # rewrite.
        self.fun01()
        self.fun02()

t = ThreadClass("ab")
t.start() # diaoying run
t.join()