
# from day15.common.list_helper import list_help



class SkillEffect:
    # def __init__(self):
    #     pass
    def generate_effect(self):
        pass
class DuzzingEffect(SkillEffect):
    def __init__(self,time):
        self.time = time
    def generate_effect(self):
        print ("duzzing %ds"%self.time)
class LifeEffect(SkillEffect):
    def __init__(self,value):
        self.value = value
    def generate_effect(self):
        print ("lose %d blood."%self.value)

class Realase:
    def __init__(self,skill_name):
        self.skill_name = skill_name
        self.__get_resource_data()
    def __get_resource_data(self):
        pass
    def __creat_effect_obj(self):
        pass
    def generate_skill(self):
        pass

xlsbz = Realase("xlsbz")
xlsbz.generate_skill()