
from day17.common_task.list_helper import *
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
    Enemy("xidsaoig",14,16,20)
]

for item in List_helper.find_enemy_info(list_enemy,
                                        lambda item:
                                        item.name == "meiba"):
    print (item)
print ()
for item in List_helper.find_enemy_info(list_enemy,
                                        lambda item:
                                        item.atk>10):
    print (item)
print ()
print (List_helper.find_enemy_count(list_enemy,
                                    lambda item:item.hp!=0))
print ()
print (List_helper.is_exist(list_enemy,
                                    lambda item:item.name=="chengkun"))
print ()
print (List_helper.is_exist(list_enemy,
                                    lambda item:
                                    item.atk<5 or item.defence<10))
