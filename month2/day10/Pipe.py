from multiprocessing import Pipe,Process

fd1,fd2 = Pipe()

def app1():  # sub process 1
    print("start app1 log-in.")
    print ("need app2's authorization.")
    fd1.send("app1 ask log-in.")
    data = fd1.recv()
    if data:
        print ("success log-in:",data)
def app2(): # sub process 2
    data = fd2.recv()
    print (data)
    fd2.send(("xiaoming",123456))

p1 = Process(target=app1)
p2 = Process(target=app2)
p1.start()
p2.start()
p1.join()
p2.join()
