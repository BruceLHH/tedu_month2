import os
print("+++++++++++++")
a = 1
pid= os.fork()
if pid<0:
    print ("failed")
elif(pid==0):
    print (a)
    a = 1000
    print ("creat new process success.")
else:
    print("the old process.",a)
print("over.")

