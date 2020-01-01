"""

"""
from threading import Thread
from time import sleep,ctime
class MyThread(Thread):
    def __init__(self,target =None,args=(),kwargs={}):
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()
    def __fun01(self,):
        # creat Thread
        pass
    def fun02(self):
        pass
    def run(self):  # rewrite.
        self.target(*self.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       args,**self.kwargs)
        #self.fun02()
def player(sec,song):
    for i in range(3):
        print("playing %s:%s"%(song,ctime()))
        sleep(sec)
t = MyThread(target = player,args=(2,),kwargs={'song':"liangliang"})
t.start() # diaoying run
t.join()