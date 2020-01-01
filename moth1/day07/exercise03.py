"""
 *#*#*#
 *#*#*#
 *#*#*#
 *#*#*#
"""
for i in range(4):
    for j in range(6):
        if i%2 == 0:
            print ("*",end="")
        else:
            print ("#",end="")
    print ()


"""
    *
    **
    ***
    ****    
"""
for row in range(4):
    for col in range(row+1):
        print ("*",end="")
    print()

# sort
list01 = [3,80,45,5,7,1]
print (list01)
for i in range(len(list01)-1):
    min_index = i
    for j in range(i+1,len(list01)):
        if list01[j]<list01[min_index]:
            min_index = j
    if (min_index!=i):
        list01[min_index],list01[i]= list01[i],list01[min_index]
print (list01)
