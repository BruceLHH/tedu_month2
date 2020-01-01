from threading import Thread

class MyThread(Thread):
    def __init__(self,target=None,args=(),kwargs={}):
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()
    def run(self):
        return self.target(*self.args,**self.kwargs)
    def fun01(self):
        pass
