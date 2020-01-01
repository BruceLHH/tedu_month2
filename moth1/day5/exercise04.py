list01 = [54,25,12,42,35,17]
list02 = []
for index in range(len(list01)):
    if(list01[index]>30):
        list02.append(list01[index])
print (list02)


# maxdata = 0
# for i in range(5):
#     number = int(input("please input a data."))
#     if number >maxdata:
#         maxdata = number
# print (maxdata)

list01 = [54,25,12,42,35,17]
maxnum = list01[0]
for item in list01:
    if (maxnum<item):
        maxnum = item
print(maxnum)

# 3.
list03 = [9,25,12,8]
# index = 0
# while True:
#     if(list03[index] > 10):
#         del list03[index]
#     else:
#         index += 1
#     if(index==len(list03)):
#         break
# print (list03)
for index in range(len(list03)-1,-1,-1):
    if(list03[index]>10):
        del list03[index]
print(list03)