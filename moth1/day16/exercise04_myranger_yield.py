

"""
make  a range iterator
for i in range(10):
    i
"""
# class Range:
#     pass
class MyRange:
    def __init__(self,stop_value):
        self.stop_value =
    def __iter__(self):
        return RangeIterator(self.stop_value)
class RangeIterator:
    def __init__(self,end_value):
        self.end_value = end_value
        self.__number = 0
    def __next__(self):
        if self.__number == self.end_value:
            raise StopIteration
        temp = self.__number
        self.__number +=1
        return temp

ite = MyRange(12)

iterator = ite.__iter__()
while True:
    try:
        temp = iterator.__next__()
        print (temp)
    except StopIteration:
        break
###
for item in MyRange(10):
    print(item)