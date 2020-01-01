"""
test code.
"""
from day17.common.list_helper import *
class SkillData:
    def __init__(self,id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration
    def __str__(self):
        return "skill is: %d,%s,%d,%d"%(self.id,self.name,self.atk_ratio,self.duration)
list_skill = [
    SkillData(101,"qkdly",5,10),
    SkillData(101,"xlsbz",8,3),
    SkillData(101,"khbd",10,1)
]

###-----------------------------------

def fun01(item):
    return item.atk_ratio<6
def fun02(item):
    return 2<item.duration<15
def fun03(item):
    pass

for item in List_helper.find_number(list_skill,
                                    lambda item:item.duration<4):
    print (item)
print ()
print ( List_helper.count_number(list_skill,
                                    lambda item:
                                    item.duration<4))