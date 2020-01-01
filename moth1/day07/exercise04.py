"""
compare comm
"""
list01 = [2,5,87,2,5,87,3,1,87,8,6]

is_com = False
for  i in range(len(list01)):
    for c in range(i+1,len(list01)):
        if list01[i] == list01[c]:
            print ("have common")
            is_com = True
            break
    if is_com:
        break
if not is_com:
    print ("no common!")

list02 = []
index =1
for row in range(4):
    temp = []
    for col in range(4):
        temp.append(index)
        index +=1
    list02.append(temp)
print (list02)
print ()
print (list02[1][2])
print (list02[2])
for row in range(len(list02)):
    print (list02[row][0],end="")

"""
[[1,2,3,4]
 [5,6,7,8]]"""
res = []
#
for col in range(len(list02[0])):
    temp = []
    # get 1
    # get 5   row
    for row in range(len(list02)):
        temp.append(list02[row][col])
    res.append(temp)
print (res)