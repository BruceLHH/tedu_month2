
from day18.common_exercise01.list_helper import *
class Enemy:
    def __init__(self,name,atk,defence,hp):
        self.name = name
        self.atk = atk
        self.defence = defence
        self.hp = hp
    def __str__(self):
        return ("The enemy info is: %s,%d,%d,%d"%(self.name,
                                                  self.atk,
                                                  self.defence,
                                                  self.hp))
list_enemy = [
   ##########  atk defence, hp
    Enemy("xiafeng",100,86,90),
    Enemy("meiba",150,19,30),
    Enemy("ww",80,25,0),
    Enemy("chengkun",28,190,20),
    Enemy("xidsaoig",14,116,10)
]
def sum01():
    sum = 0
    for item in list_enemy:
        sum += item.hp
    return sum
def sum02():
    sum = 0
    for item in list_enemy:
        sum += item.atk
    return sum
def filter1():
    list_res =[]
    for item in list_enemy:
        list_res.append(item.name)
    return list_res
def filter2():
    list_res =[]
    for item in list_enemy:
        list_res.append((item.name,item.hp))
    return list_res
# inherit
def filter_name(item):
    return item.name
res = ListHelper.caculate_sum(list_enemy,lambda item:item.defence)
print (res)

# res_filter = ListHelper.filter(list_enemy,lambda item:(item.name,item.hp))
# for item in res_filter:
#     print (item)
print (tuple(ListHelper.filter_yield(list_enemy,lambda item:(item.name,item.atk))))

def get_max(item):
    max_value = list_enemy[0]
    for item in list_enemy:
        if max_value.hp<item.hp: ## atk,defense
            max_value = item
    return max_value
### inherit
def max_common(item):
    return item.hp # atk, defense

def sort():
    for i in range(len(list_enemy)-2):
        temp = i
        for j in range(len(list_enemy)-1):
            #  atk, defense
            if list_enemy[temp].hp > list_enemy[j].hp:
                temp = j
        if (i != temp):
            list_enemy[temp].hp,list_enemy[i].hp = list_enemy[i].hp,list_enemy[temp].hp
def bian(item):
    return item.hp
print("max")
ListHelper.sort_ascending(list_enemy,lambda itme:itme.defence)
for item in list_enemy:
    print (item)

res_filter = ListHelper.filter_yield(list_enemy,lambda item:(item.name,item.hp,item.atk))
print ("res_filter:",list(res_filter))

re_map = map(lambda item:(item.name,item.hp,item.atk),list_enemy)
print (list(re_map))

re_filter = filter(lambda item:item.defence>100 and item.hp>0,list_enemy)
for item in re_filter:
    print ("re_filter: ",item)

res_filter1 = ListHelper.find_all_enemy(list_enemy,lambda item:item.defence>100 and item.hp>0)
for item in res_filter1:
    print(item)
sort_res = sorted(list_enemy,key=lambda item:item.defence,reverse=True)
for item in sort_res:
    print (item)

print ("min hp value:")
###----------------
print (ListHelper.get_min_value(list_enemy,lambda item:item.hp))

print ("sort decending:")
ListHelper.sort_decend(list_enemy,lambda item:item.hp)
for item in list_enemy:
    print(item)
print ("del enemy:")
ListHelper.del_enemy(list_enemy,lambda  item:item.hp>50)
for item in list_enemy:
    print (item)