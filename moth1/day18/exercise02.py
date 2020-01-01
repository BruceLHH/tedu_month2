from day18.common_exercise01.list_helper import *

list01 = ([1,1,1],[2,2],[3,3,3,3])
print (max(list01,key =lambda item:len(item)))

res = ListHelper.get_max_value(list01,lambda item:len(item))
