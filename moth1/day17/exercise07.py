from day17.common_exercise07.list_helper import *
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
    SkillData(102,"xlsbz",8,3),
    SkillData(103,"khbd",10,1)
]

def get_namq():
    for item in list_skill:
        if item.name =="khbd":
            return item
def get_101():
    for item in list_skill:
        if item.id == 101:
            return item
def get_time():
    for item in list_skill:
        if item.duration >0:
            return item
# 1. fengzhuang
def fun01(item):
    return item.name == "khbd"
def fun02(item):
    return item.id == 101
def fun03(item):
    return item.duration > 5
# 2. inherit

print (List_helper.get_skill(list_skill,lambda item:item.duration >4))