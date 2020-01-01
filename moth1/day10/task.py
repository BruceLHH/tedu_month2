
class Enemy:
    def __init__(self,name,blood,base_damage,defense):
        self.name = name
        self.blood = blood
        self.base_damage = base_damage
        self.defense = defense
    def print_info(self):
        print ("The enemy name is %s,blood:%d,base_damage:%d,defense:%d"%(self.name,
                                                                          self.blood,
                                                                          self.base_damage,
                                                                          self.defense))

enemy = [Enemy("huangshang",100,98,2000),
         Enemy("wushi",0,89,1500),
         Enemy("huanghou",98,99,1900),
         Enemy("soldier",30,25,150),
         Enemy("cuihua",50,89,8),
         Enemy("mieba",60,86,1300)]
def find_mieba_obj():
    for obj in enemy:
        if obj.name == "mieba":
            return obj
find_mieba_obj().print_info()
def find_all_dead_enemy():
    dead =[]
    for obj in enemy:
        if obj.blood == 0:
            dead.append(obj.name)
    return dead
print (find_all_dead_enemy())

def display_damage_mean():
    res = 0
    for obj in enemy:
        res += obj.base_damage
    return res/len(enemy)
print ("the mean is: ",display_damage_mean())

def del_enemy_defense_less_than_ten():
    """"""
    for index in range(len(enemy)-1,-1,-1):
        print (enemy[index].defense)
        if enemy[index].defense <10:
            del enemy[index]
del_enemy_defense_less_than_ten()
print ("delete enemy later.")
for obj in enemy:
    obj.print_info()

def add_damage():
    for obj in enemy:
        obj.base_damage += 50
