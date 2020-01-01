# list01 = []
# for index in range(1,11):
#     list01.append(index**2)
# print (list01)

list01 =[index**2 for index in range(1,11)]
print (list01)

list02 = [item for item in list01 if item%2]
print("list02",list02)
list03 = [item for item in list01 if not item%2]
print("list03:",list03)
list04 = [item+1 for item in list01 if (not item%2 and item>5)]
print("list04:",list04)

