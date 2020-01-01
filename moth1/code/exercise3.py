max = 0
for i in range(4):
    data = int(input("please input %d number: "%(i+1)))
    if (max<data):
        max = data
print ("the max number of inputs is:",max)
