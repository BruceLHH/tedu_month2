from threading import Thread,Event

s = None
e = Event()
def yangzirong():
    print ("kouling")
    global s
    s = "tianwanggaidihu"
    e.set()

t = Thread(target = yangzirong)
t.start()
e.wait()
if s == "tianwanggaidihu":
    print ("ok.")
else:
    print ("dead.")
t.join()