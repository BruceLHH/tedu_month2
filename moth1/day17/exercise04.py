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

def get_skill():
    for item in list_skill:
        if 4<item.duration<11:
            yield item
# ite = get_skill()
# for item in ite:
#     print(item)
#
# for item in (item for item in list_skill if item.atk_ratio<6):
#     print(item.name)

###-----------------------------------

def fun01(item):
    return item.atk_ratio<6
def fun02(item):
    return 2<item.duration<15
def fun03(item):
    pass
## jicheng
def get_skills(fun_condition):
    for item in list_skill:
        ## duotai
        if fun_condition(item):
            yield item
for item in get_skills(fun02):
    print (item)