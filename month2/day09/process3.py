from multiprocessing import Process
import os,sys
from time import sleep

def fun01():
    print ("start")
def fun02():
    print("end")
def fun03():
    pass

things = [fun01,fun02,fun03]
jobs = []
for th in things:
    p = Process(target=th)
    jobs.append(p)
    print(p.name)
    p.daemon = True
    p.start()
    print(p.pid)
# for i in jobs:
#     i.join()
