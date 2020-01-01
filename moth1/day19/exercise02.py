import time

def caculate_run_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        print ("fun01 runing %.3fs."%(time.time()-start_time))
    return wrapper

@caculate_run_time
def fun01():
    time.sleep(2)
    print ("fun01 finish.")
@caculate_run_time
def fun02(a):
    time.sleep(1)
    print ("fun02 finish argument is:",a)

fun01()
fun02(10)
