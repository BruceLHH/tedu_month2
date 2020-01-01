list01 = [3,6,26,3,8,9,5,2,12]
def my_generate():
    number = 0
    while number<len(list01):
        yield number,list01[number]
        number += 1

ger = my_generate()
for index,vlaue in ger:
    print (index,vlaue)

# 2.
list02 = ["i","you","he"]
list03 = [101,102,103]
#
def my_generate02():
    for index in range(len(list02)):
        yield list02[index],list03[index]
for item in my_generate02():
    print(item)

