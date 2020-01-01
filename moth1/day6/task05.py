str = input("please input a string")
dict_count = {}
for item in str:
    if item in dict_count:
        dict_count[item] += 1
    else:
        dict_count[item] = 1
for str,count in dict_count.items():
    print (str,count)