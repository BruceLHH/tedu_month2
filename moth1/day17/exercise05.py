list01 = [43,4,5,6,7,8,98]

# fengzhuang   sixiang
def func01(item):
    return item%2 ==0
def func02(item):
    return item>10
def func03(item):
    return 10<item<50
## jicheng
def find_number(func_condition):
    for item in list01:
        if func_condition(item):
            yield item

for item in find_number(func02):
    print (item)