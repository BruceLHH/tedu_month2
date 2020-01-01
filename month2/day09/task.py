from multiprocessing import Process
import os,sys
from time import sleep

def readfront(file):
    f1 = open("res01.txt","w")
    temp =file.read()
    print (temp[len(temp)/2])
def readlast(file):
    pass
fun_list = [readfront,readlast]
f = open("test.txt","r")
jobs =[]
for th in fun_list:
    p = Process(target=th,args =(f,))
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
f.close()