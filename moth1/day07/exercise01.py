
list01 = ["lin","xiaoming","xiaoli"]
dict01 = {}
for item in list01:
    dict01[item] = len(item)
print (dict01)

# dict02 = {item:len(item) for item in list01}
# print (dict02)

list02 = [101,102,103]
dict02 = {list01[index]:list02[index] for index in range(len(list01))}
print (dict02)